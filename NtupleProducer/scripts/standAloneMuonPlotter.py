from PlotterBase import *

# initialize plotter
plotter = PlotterBase("BufferOverload")
filenames = ["BufferOverload_0p00.root",
             "BufferOverload_0p01.root",
             "BufferOverload_0p05.root",
             "BufferOverload_0p10.root",
             "BufferOverload_0p20.root",
             "BufferOverload_0p30.root",
             "BufferOverload_0p50.root",
             "BufferOverload_1p00.root"]
treename = "skim/RecoTree"
labels = ["No Failure", "1%", "5%", "10%", "20%", "30%", "50%", "100%"]
plotter.initialize_trees(filenames,treename)
plotter.set_labels(labels)

# make plots
plotter.plot_variable("StandAloneMuon.muStandAloneEta", "standAloneEta",
                      binning=[50,-2.5,2.5], xaxis="#eta")
plotter.plot_variable("StandAloneMuon.muonSize", "numberStandAloneMuons",
                      binning=[6,0,6], xaxis="Number of Standalone Muons", logy=1, legend="topLeft")
plotter.plot_variable("StandAloneMuon.muonSize1p6", "numberStandAloneMuonsEta1p6",
                      binning=[6,0,6], xaxis="Number of Standalone Muons (|#eta|>1.6)", logy=1)
plotter.plot_variable("StandAloneMuon.muStandAlonePt1p6", "standAlonePt1p6",
                      binning=[50,0,100], xaxis="p_{T} (|#eta|>1.6)", logy=1)
plotter.plot_variable("StandAloneMuon.muStandAloneEta", "standAloneEtaEfficiency",
                      binning=[50,-2.5,2.5], xaxis="#eta", makeEfficiency=1, legend="bottomRight")
plotter.plot_variable("StandAloneMuon.muStandAlonePt1p6", "standAlonePtEfficiency",
                      binning=[50,0,100], xaxis="p_{T} (|#eta|>1.6)", makeEfficiency=1,
                      legend="bottomRight")
