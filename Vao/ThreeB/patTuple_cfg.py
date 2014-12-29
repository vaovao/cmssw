## import skeleton process
from Vao.ThreeB.patTemplate_cfg import *


## ------------------------------------------------------
#  NOTE: you can use a bunch of core tools of PAT to
#  taylor your PAT configuration; for a few examples
#  uncomment the lines below
## ------------------------------------------------------
#from PhysicsTools.PatAlgos.tools.coreTools import *

## remove MC matching from the default sequence
# removeMCMatching(process, ['Muons'])
# runOnData(process)

## remove certain objects from the default sequence
# removeAllPATObjectsBut(process, ['Muons'])
# removeSpecificPATObjects(process, ['Electrons', 'Muons', 'Taus'])

process.source.fileNames = cms.untracked.vstring("file:///tmp/vao/0047A57E-AFD4-E111-80F7-00304867BEC0.root")

## uncomment the following line to add tcMET to the event content
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')

## uncomment the following line to add different b-taggers collections
## to the event content
from PhysicsTools.PatAlgos.tools.jetTools import *

process.patJets.addTagInfos = True

# uncomment the following lines to add ak5PFJets with new b-tags to your PAT output
addJetCollection(process,cms.InputTag('ak5PFJets'),
                 'AK5', 'PF',
                 doJTA        = True,
                 doBTagging   = True,
                 btagInfo           = cms.vstring('impactParameterTagInfos','secondaryVertexTagInfos','secondaryVertexNegativeTagInfos','inclusiveSecondaryVertexFinderTagInfos'),
                 btagdiscriminators = cms.vstring('jetBProbabilityBJetTags','jetProbabilityBJetTags','trackCountingHighPurBJetTags','trackCountingHighEffBJetTags','simpleSecondaryVertexHighEffBJetTags','simpleSecondaryVertexHighPurBJetTags','combinedSecondaryVertexBJetTags','combinedInclusiveSecondaryVertexBJetTags'),
                 jetCorrLabel = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])),
                 doType1MET   = True,
                 doL1Cleaning = True,
                 doL1Counters = False,
                 genJetCollection=cms.InputTag("ak5GenJets"),
                 doJetID      = True,
                 jetIdLabel   = "ak5"
                 )

process.out.fileName = cms.untracked.string('/tmp/vao/btag.root')

process.bjets = cms.EDFilter("CandViewSelector",
     src = cms.InputTag("cleanPatJetsAK5PF"),
     cut = cms.string('bDiscriminator("trackCountingBJetTags") > 0.898')
)

process.out.outputCommands.append("keep *_bjets_*_*")

## let it run
process.p = cms.Path(
    process.patDefaultSequence*process.bjets
    )



process.GlobalTag.globaltag = cms.string('FT_R_53_V6::All')
process.maxEvents.input = cms.untracked.int32(10)

process.MessageLogger.cerr.FwkReport.reportEvery = 100
## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
process.source.fileNames = filesRelValProdTTbarAODSIM
#                                         ##

#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##

process.out.fileName = '/tmp/vao/patTuple_standard.root'

#                                         ##
#   process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)

