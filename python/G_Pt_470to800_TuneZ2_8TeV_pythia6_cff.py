import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(8000.0),
	crossSection = cms.untracked.double(2.120056e-01),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 10       ! Photon+Jets production',
			'CKIN(3) = 470   ! minimum pt hat for hard interactions',
			'CKIN(4) = 800   ! maximum pt hat for hard interactions',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
		)
	)
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision$'),
	name = cms.untracked.string('\$Source$'),
	annotation = cms.untracked.string('Spring2011 sample with PYTHIA6: Prompt photon production, pThat = 470 .. 800 GeV, TuneZ2')
)
