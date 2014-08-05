'''
PlotterBase.py
A basic plotter base class. Accepts multiple root trees and plots variables from the trees.
Author: Devin N. Taylor (U.W. Madison)
'''

import sys
import os
import errno
import glob
import ROOT
import numpy

ROOT.gROOT.SetBatch(ROOT.kTRUE)

def python_mkdir(dir):
    '''A function to make a unix directory as well as subdirectories'''
    try:
        os.makedirs(dir)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(dir):
            pass
        else: raise

class PlotterBase(object):
    '''A plotting base class'''
    def __init__(self, output):
        '''Initialize plotter'''
        self.canvas = ROOT.TCanvas("c1","c1",700,700)
        ROOT.gStyle.SetOptStat(0)
        self.outputdir = '/afs/hep.wisc.edu/user/dntaylor/public_html/%s/' % (output)
        python_mkdir(self.outputdir)
        self.colors = [ROOT.EColor.kRed,ROOT.EColor.kBlue,ROOT.EColor.kGreen,ROOT.EColor.kBlack,ROOT.EColor.kOrange,ROOT.EColor.kTeal,ROOT.EColor.kViolet,ROOT.EColor.kMagenta,ROOT.EColor.kTeal]
        self.markerStyles = [22,21,20,23,29,33,3,4,5,6]
        self.trees = []
        self.labels = []

    def set_file_names(self, filenames):
        '''Set the file names of the trees to be plotted'''
        self.filenames = filenames

    def set_tree_name(self, treename):
        '''Set the tree name of the ntuples to be plotted (assumes all files have same structure)'''
        self.treename = treename

    def initialize_plotter(self):
        '''Initialize the ntuple trees'''
        numFiles = len(self.filenames)
        self.files = []
        self.trees = []
        for f in range(numFiles):
            self.files.append(ROOT.TFile(self.filenames[f]))
            self.trees.append(self.files[f].Get(self.treename))

    def initialize_trees(self, filenames, treename):
        '''Initialize ntuple trees and filenames at same time'''
        self.set_file_names(filenames)
        self.set_tree_name(treename)
        self.initialize_plotter()

    def set_labels(self,labels):
        '''Set legend labels'''
        self.labels = labels

    def make_plot(self, tree, variable, selection, binning, color=ROOT.EColor.kBlue, markerStyle=20, xaxis='', title=''):
        ''' Plot a variable using draw and return the histogram '''
        draw_string = "%s>>htemp(%s)" % (variable, ", ".join(str(x) for x in binning))
        print draw_string
        print selection
        tree.Draw(draw_string, selection, "goff")
        output_histo = ROOT.gDirectory.Get("htemp").Clone()
        output_histo.GetXaxis().SetTitle(xaxis)
        output_histo.SetTitle(title)
        output_histo.SetLineColor(color)
        output_histo.SetMarkerStyle(markerStyle)
        output_histo.SetMarkerColor(color)
        return output_histo

    def make_efficiency(self, tree_denom, tree_num, variable, selection, binning, color=ROOT.EColor.kBlue, markerStyle=20, xaxis='', title=''):
        ''' Plot a variable using draw and return the histogram '''
        hist = ROOT.TH1F('a','a',*binning)
        draw_string_denom = "%s>>htempd(%s)" % (variable, ", ".join(str(x) for x in binning))
        draw_string_num = "%s>>htempn(%s)" % (variable, ", ".join(str(x) for x in binning))
        print draw_string_num
        print draw_string_denom
        print selection
        tree_denom.Draw(draw_string_denom,selection,"goff")
        tree_num.Draw(draw_string_num,selection,"goff")
        hist_denom = ROOT.gDirectory.Get("htempd")
        hist_num = ROOT.gDirectory.Get("htempn")
        for bin in range(binning[0]):
            if hist_denom.GetBinContent(bin):
                efficiency = hist_num.GetBinContent(bin)/hist_denom.GetBinContent(bin)
            else:
                efficiency = 0
            hist.SetBinContent(bin,efficiency)
        hist.GetXaxis().SetTitle(xaxis)
        hist.SetTitle(title)
        hist.SetLineColor(color)
        hist.SetMarkerStyle(markerStyle)
        hist.SetMarkerColor(color)
        return hist

    def plot_variable(self, variable, filename, **kwargs):
        '''Plot a variable with a given selection.
           
           kwargs accepts:
               Argument         Type                     Description
               selection        string                   A cut to be applied to all trees
               selections       list (string)            A cut to be applied to a single tree
               binning          [int, double, double]    Rebin a plot [Numbins, min, max]
                                list (double)            Rebin a plot with variable bin size (N/A)
               logy             bool                     Plot log scale (Default: 0)
               xaxis            string                   Label for xaxis
               title            string                   Title string
               makeEfficiency   bool                     Make efficiency plot (Default 0)
               legend           string                   Legend location (Default topRight)
                                                         topRight, topLeft, bottomRight, bottomLeft
               zoomEfficiency   bool                     Zoom effiency
           '''
        selection = kwargs.pop('selection','')
        selections = kwargs.pop('selections',[])
        if not selections: selections = [''] * len(self.filenames)
        binning = kwargs.pop('binning',[])
        logy = kwargs.pop('logy',0)
        xaxis = kwargs.pop('xaxis','')
        yaxis = kwargs.pop('yaxis','')
        title = kwargs.pop('title','')
        makeEfficiency = kwargs.pop('makeEfficiency',0)
        zoomEfficiency = kwargs.pop('zoomEfficiency',0)
        if makeEfficiency and not yaxis: yaxis = "Efficiency"
        if not yaxis: yaxis = "Events"
        legendLocation = kwargs.pop('legend','topRight')
        legendPositions = [0.65, 0.60, 0.89, 0.89]
        if legendLocation == "topLeft": legendPositions = [0.11, 0.60, 0.35, 0.89]
        if legendLocation == "bottomRight": legendPositions = [0.65, 0.11, 0.89, 0.40]
        if legendLocation == "bottomLeft": legendPositions = [0.11, 0.11, 0.35, 0.40]
        legendPositions += ["","brNDC"]

        plots = []
        numPlots = len(self.filenames)
        if makeEfficiency: numPlots -= 1
        for i in range(numPlots):
            selection_temp = selection
            if selections[i]!="":
                selection_temp += "&&"+selections[i]
            if makeEfficiency:
                plots.append(self.make_efficiency(
                    self.trees[0], self.trees[i+1], variable, selection_temp,
                    binning, self.colors[i+1], self.markerStyles[i+1]
                    )
                )
            else:
                plots.append(self.make_plot(
                    self.trees[i], variable, selection_temp,
                    binning, self.colors[i], self.markerStyles[i]
                    )
                )
        legend = ROOT.TLegend(*legendPositions)
        legend.SetFillColor(ROOT.EColor.kWhite)
        legend.SetBorderSize(1)
        for i in range(numPlots):
            if i == 0:
                plots[i].SetTitle(title)
                if makeEfficiency: plots[i].SetMaximum(1.2)
                if zoomEfficiency: plots[i].SetMaximum(1.1)
                if zoomEfficiency: plots[i].SetMinimum(0.9)
                plots[i].GetXaxis().SetTitle(xaxis)
                plots[i].GetYaxis().SetTitle(yaxis)
                plots[i].Draw('ph')
            else:
                plots[i].Draw('phsame')
            if self.labels:
                j = i+1 if makeEfficiency else i
                legend.AddEntry(plots[i],self.labels[j], "p")
        if self.labels:
            legend.Draw("same")
        saveas = self.outputdir+filename+'.png'
        self.canvas.SetLogy(logy)
        self.canvas.SaveAs(saveas)



