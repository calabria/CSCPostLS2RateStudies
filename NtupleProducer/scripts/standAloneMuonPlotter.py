from PlotterBase import *

channels = ["ZZ", "HZZ", "Zprime"]
for channel in channels:
    # initialize plotter
    plotter = PlotterBase("BufferOverload")
    filenames = ["BufferOverload_%s_0p00.root" % channel,
                 "BufferOverload_%s_0p01.root" % channel,
                 "BufferOverload_%s_0p02.root" % channel,
                 "BufferOverload_%s_0p05.root" % channel,
                 "BufferOverload_%s_0p10.root" % channel,
                 "BufferOverload_%s_0p20.root" % channel,
                 "BufferOverload_%s_0p30.root" % channel,
                 "BufferOverload_%s_0p50.root" % channel,
                 "BufferOverload_%s_1p00.root" % channel]
    treename = "skim/RecoTree"
    labels = ["No Failure", "1%", "2%", "5%", "10%", "20%", "30%", "50%", "100%"]
    plotter.initialize_trees(filenames,treename)
    plotter.set_labels(labels)
    
    # make plots
    plotter.plot_variable("StandAloneMuon.muStandAloneEta", "%sStandAloneEta" % channel,
                          binning=[50,-2.5,2.5], xaxis="#eta")
    plotter.plot_variable("StandAloneMuon.muonSize", "%sNumberStandAloneMuons" % channel,
                          binning=[6,0,6], xaxis="Number of Standalone Muons", logy=1, legend="topLeft")
    plotter.plot_variable("StandAloneMuon.muonSize1p6", "%sNumberStandAloneMuonsEta1p6" % channel,
                          binning=[6,0,6], xaxis="Number of Standalone Muons (|#eta|>1.6)", logy=1)
    plotter.plot_variable("StandAloneMuon.muStandAlonePt1p6", "%sStandAlonePt1p6" % channel,
                          binning=[50,0,100], xaxis="p_{T} (|#eta|>1.6)", logy=1)
    plotter.plot_variable("StandAloneMuon.muStandAloneP1p6", "%sStandAloneP1p6" % channel,
                          binning=[50,0,500], xaxis="p (|#eta|>1.6)", logy=1)
    plotter.plot_variable("StandAloneMuon.muStandAloneZ", "%sStandAloneZ" % channel,
                          binning=[60,20,140], xaxis="M_{#mu#mu}", legend="topLeft")
    plotter.plot_variable("StandAloneMuon.muStandAloneZmumu", "%sStandAloneZmumu" % channel,
                          binning=[70,0,3500], xaxis="M_{#mu#mu}", legend="topLeft")
    plotter.plot_variable("StandAloneMuon.muStandAloneEta", "%sStandAloneEtaEfficiency" % channel,
                          binning=[50,-2.5,2.5], xaxis="#eta", makeEfficiency=1, legend="bottomRight")
    plotter.plot_variable("StandAloneMuon.muStandAlonePt1p6", "%sStandAlonePtEfficiency" % channel,
                          binning=[50,0,100], xaxis="p_{T} (|#eta|>1.6)", makeEfficiency=1,
                          legend="bottomRight")
    plotter.plot_variable("StandAloneMuon.muStandAloneEta", "%sStandAloneEtaEfficiencyZoom" % channel,
                          binning=[50,-2.5,2.5], xaxis="#eta", makeEfficiency=1, zoomEfficiency=1)
    plotter.plot_variable("StandAloneMuon.muStandAlonePt1p6", "%sStandAlonePtEfficiencyZoom" % channel,
                          binning=[20,0,40], xaxis="p_{T} (|#eta|>1.6)", makeEfficiency=1, zoomEfficiency=1)
