import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/149DE53F-9BC8-E611-ACE6-02163E019DC3.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/209E1412-22CA-E611-A6B5-02163E019B31.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2E963E07-8BC8-E611-BE9B-02163E019E89.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/603C8340-8FC8-E611-B226-02163E019D73.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6080CACD-DAC8-E611-ABD0-02163E019DD7.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/861F84AE-A8C8-E611-8CB2-02163E019BCF.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/922CA745-85C8-E611-8821-02163E019C78.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/982D8A06-9EC8-E611-B518-02163E019CE4.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A2800EC1-98C8-E611-A2AE-02163E019CD8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C80A48EF-A3C8-E611-87B4-02163E019DBF.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FEE264F1-B2C8-E611-843A-02163E019C26.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/02E63559-F6C7-E611-8CD1-E41D2D08E0B0.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08FB378B-D8C8-E611-BF06-001E67E6F544.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C3E217E-43C7-E611-81DD-FA163E702259.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/14CBA03B-0CC8-E611-8EB8-44A842CF0600.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/24028DAA-FAC8-E611-B1FB-02163E019D97.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/282B8400-1DC8-E611-A904-00266CFCCC38.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/34914EC2-FBC7-E611-BA1D-0025905A608E.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E1B89CF-34C7-E611-9318-6C3BE5B533A8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C657245-F4C8-E611-AD80-02163E019DEA.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/567026E1-31C7-E611-BDA5-FA163E26664A.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5CC18C06-1DC7-E611-B525-02163E0176B1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/666B7D6E-56C7-E611-B0D0-02163E013EDF.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/68256814-22C8-E611-AE3F-FA163E1CADB1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/70E65B4C-1FC7-E611-ACE9-0025904B2016.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C4AE38A-2FC7-E611-B71B-FA163E0ED805.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7EE3BBDA-16C7-E611-B1CB-FA163E2645E6.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/80FF484D-F7C8-E611-89F3-02163E019DD1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/84D7FF35-2DC7-E611-8D95-02163E012F83.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88E1F5F6-E8C8-E611-A8C3-02163E019B64.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E0820F3-03C9-E611-B7B9-02163E019B4D.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E39DB61-41C7-E611-B29B-FA163E2DF99A.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9019FF70-B2C8-E611-9BDB-7CD30ABD2EEA.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9EFD7498-F1C7-E611-A039-009C02AAB258.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A42F8445-C5C8-E611-B591-549F35AC7DEE.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A633EAE9-1FC7-E611-A32D-02163E00C914.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AAAAACD7-CBC7-E611-A584-00266CF3323C.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B088446E-0EC8-E611-8003-0CC47AC08904.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B0CFCA7A-CEC9-E611-A5FC-02163E019CE0.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B4EBCCD9-22C7-E611-9FD9-02163E012E35.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B6D2D0F3-2AC7-E611-A2FA-FA163E96D081.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B8C3B830-85C8-E611-BC8A-C4346BC808B8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BCDB33E5-F3C7-E611-9D63-842B2B7680A2.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C0999E05-FCC7-E611-BA55-0CC47A7C3410.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CCD05352-35C7-E611-9C38-0CC47A044870.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4314691-B2C8-E611-B75C-02163E019A6B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4CE5851-0BC9-E611-806B-7845C4FC3A07.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E2B26070-98C8-E611-A373-0025904C4F52.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E67728E3-C7C7-E611-B141-A0369F7FC524.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EC63D736-FFC8-E611-95F2-02163E019BA1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/ECED5141-4CC7-E611-AC48-FA163EB9C423.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FAFD6053-F7C8-E611-B790-02163E019BF2.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/04397080-9ED2-E611-ACC5-02163E013394.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/20B15A1D-B0D2-E611-BD84-02163E011DD7.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2243A8F0-A5D2-E611-861A-02163E0142D4.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/26D91C11-C7D2-E611-8591-02163E014645.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/32BECCC9-BDD2-E611-BDA3-02163E0142D4.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/50641DDF-98D2-E611-B69D-02163E0140E1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58FD451C-B0D2-E611-B40F-02163E012194.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5EB06229-B4D2-E611-B764-02163E011B13.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/76DD4164-91D2-E611-968A-02163E019BD6.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/98595F72-95D2-E611-AE91-02163E014611.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A62EB33B-B8D2-E611-9B49-02163E0138C0.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C66EF27E-8FD2-E611-B740-02163E019C95.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C8145BCE-A2D2-E611-9349-02163E019B23.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA61673C-ACD2-E611-9E94-02163E019C9D.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CE00DDF4-A8D2-E611-860D-02163E019D35.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E2846B67-9CD2-E611-9CCC-02163E019D28.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F8D0B2FE-B5D2-E611-B699-02163E019E12.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14C3695D-50C9-E611-B539-02163E019CEB.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/260442F7-4EC9-E611-B164-02163E019E6D.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/32ABBDF0-76C9-E611-8C2C-02163E019E7B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3A872E77-41C9-E611-8081-02163E019B7C.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3AAA40F3-4EC9-E611-A01E-02163E019B7C.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3AED8203-55C9-E611-84A0-02163E019E23.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/44FD0CC0-57CA-E611-9702-02163E019D95.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5220342F-5FC9-E611-A43A-02163E019C7E.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5261C0CC-71C9-E611-A3F5-02163E019C29.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/58F6AA67-51C9-E611-876D-02163E019BDD.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A71BD7B-52C9-E611-8794-02163E019D75.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6CC8E714-4AC9-E611-9649-02163E019DF7.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/76A72E1D-58C9-E611-A6E0-02163E019E58.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9047AD16-5DC9-E611-9F5C-02163E019C99.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96B0454D-79C9-E611-8DF3-02163E019BAA.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA0F25A7-62C9-E611-921C-02163E019E69.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C82F047C-6CC9-E611-B98F-02163E019D39.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C89635FF-64C9-E611-B815-02163E019E7B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F6AFBFC3-4CC9-E611-9957-02163E019D8B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0AD87500-BBC7-E611-A3CB-02163E01371B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1294A57B-A6C7-E611-BB4C-02163E019CBF.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/142EB5A0-79C9-E611-9801-848F69FD4565.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2E9433E2-C2C7-E611-AA1A-44A842CFC998.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3251016F-83C8-E611-9A92-009C02AABEB8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/343DC0F8-89C7-E611-8748-02163E019C07.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A581CF9-A1C8-E611-8ED5-008CFAFBF618.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4AA2E511-DFC7-E611-8E01-24B6FDFFBB7F.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4ECBAE8C-49C9-E611-9DDD-00259073E41E.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/56CC7692-4FC9-E611-AFB6-0CC47A1DF60C.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5AA7932E-98CA-E611-AC4D-001E673965FE.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6C1A29EB-E5C8-E611-8F6A-FACADE000158.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6EF691C9-B7C7-E611-90DD-FA163E31F20F.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72047FEB-A5C7-E611-814F-02163E00B75B.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/766DFEFF-B3C7-E611-959B-28924A33AFC2.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7CA28AAF-A6C7-E611-BCF5-0CC47A7FC746.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80921C58-9BC7-E611-BE35-02163E019D97.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80D8BFB6-6BC8-E611-B639-0025904C7DFA.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9874C0DD-F5C6-E611-B0CD-44A842CFD5D8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9A709229-9DC7-E611-A908-FA163EECE5C8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A8AC9044-7FC8-E611-945E-00A0D1EC7FB8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AE888987-98C8-E611-BA09-02163E019CC7.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B0C3C674-CDC7-E611-A24E-02163E0119B1.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B22F71AB-E6C8-E611-A076-842B2B765E01.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B2EAE21B-6DC8-E611-8757-001E67F120AD.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B868D795-94C7-E611-8314-02163E019C0F.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BE52B96F-F8C6-E611-9084-549F358EB762.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D457FE1C-AEC7-E611-BFC7-02163E019BDC.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DEAE918E-2CCA-E611-B473-002590DE6E5E.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E8764DFE-B3C7-E611-91C7-02163E019CE3.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA30E4A4-ABC7-E611-A817-7CD30AC030F8.root',
'/store/mc/RunIISummer16MiniAODv2/QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F883FA2D-BFC7-E611-A176-02163E019D4F.root' ] );

