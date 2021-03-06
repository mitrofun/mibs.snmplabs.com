#
# PySNMP MIB module CISCO-DOT11-HT-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-PHY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, iso, Counter64, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, NotificationType, ObjectIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoDot11HtPhyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 607))
ciscoDot11HtPhyMIB.setRevisions(('2006-12-11 00:00',))
if mibBuilder.loadTexts: ciscoDot11HtPhyMIB.setLastUpdated('200612110000Z')
if mibBuilder.loadTexts: ciscoDot11HtPhyMIB.setOrganization('Cisco Systems, Inc.')
ciscoDot11HtPhyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 0))
ciscoDot11HtPhyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 1))
ciscoDot11HtPhyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 2))
cD11HtPhy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1))
class CD11HtPhyBeamformFeedback(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("unsolicited", 0), ("immediate", 1), ("aggregated", 2))

cD11HtPhyAntennaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1), )
if mibBuilder.loadTexts: cD11HtPhyAntennaTable.setStatus('current')
cD11HtPhyAntennaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtPhyAntennaEntry.setStatus('current')
cD11HtPhyAntennaSelectionImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyAntennaSelectionImplemented.setStatus('current')
cD11HtPhyXmitExpCSIFdbkASImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyXmitExpCSIFdbkASImplemented.setStatus('current')
cD11HtPhyXmitIndFdbkASImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyXmitIndFdbkASImplemented.setStatus('current')
cD11HtPhyExplCSIFdbkASImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplCSIFdbkASImplemented.setStatus('current')
cD11HtPhyXmitIndCompFdbkASImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyXmitIndCompFdbkASImplemented.setStatus('current')
cD11HtPhyRcvAntennaSelImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyRcvAntennaSelImplemented.setStatus('current')
cD11HtPhyXmitSoundPPDUImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyXmitSoundPPDUImplemented.setStatus('current')
cD11HtPhyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2), )
if mibBuilder.loadTexts: cD11HtPhyTable.setStatus('current')
cD11HtPhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtPhyEntry.setStatus('current')
cD11HtPhyOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("legacy", 1), ("mixed", 2), ("greenField", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyOperatingMode.setStatus('current')
cD11HtPhyOperModeFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("legacyMode", 1), ("htMode", 2), ("dupLegacyMode", 3), ("fortyMHzUpperMode", 4), ("fortyMHzLowerMode", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyOperModeFrequency.setStatus('current')
cD11HtPhyOperBand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("band24GHz", 1), ("band5GHz", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyOperBand.setStatus('current')
cD11HtPhyFortyMHzOperationImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyFortyMHzOperationImplemented.setStatus('current')
cD11HtPhyFortyMHzOperationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyFortyMHzOperationEnabled.setStatus('current')
cD11HtPhyCurrentControlChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyCurrentControlChannel.setStatus('current')
cD11HtPhyCurrentExtensionChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noExtension", 1), ("extensionAbove", 2), ("extensionBelow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyCurrentExtensionChannel.setStatus('current')
cD11HtPhyExtChannelCCAImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExtChannelCCAImplemented.setStatus('current')
cD11HtPhyNumberOfSpatialStreamsImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyNumberOfSpatialStreamsImplemented.setStatus('current')
cD11HtPhyNumberOfSpatialStreamsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyNumberOfSpatialStreamsEnabled.setStatus('current')
cD11HtPhyGreenFieldImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyGreenFieldImplemented.setStatus('current')
cD11HtPhyGreenFieldEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyGreenFieldEnabled.setStatus('current')
cD11HtPhyShortGIInTwentyImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 13), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyShortGIInTwentyImplemented.setStatus('current')
cD11HtPhyShortGIInTwentyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyShortGIInTwentyEnabled.setStatus('current')
cD11HtPhyShortGIInFortyImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyShortGIInFortyImplemented.setStatus('current')
cD11HtPhyShortGIInFortyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyShortGIInFortyEnabled.setStatus('current')
cD11HtPhyAdvancedCodingImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 17), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyAdvancedCodingImplemented.setStatus('current')
cD11HtPhyAdvancedCodingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 18), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyAdvancedCodingEnabled.setStatus('current')
cD11HtPhyTxSTBCImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 19), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyTxSTBCImplemented.setStatus('current')
cD11HtPhyTxSTBCEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyTxSTBCEnabled.setStatus('current')
cD11HtPhyRxSTBCImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 21), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyRxSTBCImplemented.setStatus('current')
cD11HtPhyRxSTBCEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyRxSTBCEnabled.setStatus('current')
cD11HtPhyBeamFormingImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 23), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyBeamFormingImplemented.setStatus('current')
cD11HtPhyBeamFormingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 24), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtPhyBeamFormingEnabled.setStatus('current')
cD11HtPhySupportedMCSTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3), )
if mibBuilder.loadTexts: cD11HtPhySupportedMCSTable.setStatus('current')
cD11HtPhySupportedMCSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtPhySupportedMCSEntry.setStatus('current')
cD11HtPhySupportedMCSTxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhySupportedMCSTxValue.setStatus('current')
cD11HtPhySupportedMCSRxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhySupportedMCSRxValue.setStatus('current')
cD11HtPhyTxBFConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4), )
if mibBuilder.loadTexts: cD11HtPhyTxBFConfigTable.setStatus('current')
cD11HtPhyTxBFConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtPhyTxBFConfigEntry.setStatus('current')
cD11HtPhyRxStaggerSoundImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyRxStaggerSoundImplemented.setStatus('current')
cD11HtPhyTxStaggerSoundImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyTxStaggerSoundImplemented.setStatus('current')
cD11HtPhyRxZLFImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyRxZLFImplemented.setStatus('current')
cD11HtPhyTxZLFImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyTxZLFImplemented.setStatus('current')
cD11HtPhyImplicitTxBFImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyImplicitTxBFImplemented.setStatus('current')
cD11HtPhyCalibrationImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inCapable", 1), ("unableToInitiate", 2), ("ableToInitiate", 3), ("fullyCapable", 4))).clone('inCapable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyCalibrationImplemented.setStatus('current')
cD11HtPhyExplCSITxBFImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplCSITxBFImplemented.setStatus('current')
cD11HtPhyExplUncompSteerMatrixImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplUncompSteerMatrixImplemented.setStatus('current')
cD11HtPhyExplBFCSIFdbkImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 9), CD11HtPhyBeamformFeedback()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplBFCSIFdbkImplemented.setStatus('current')
cD11HtPhyExplUncompSteerMatrixFdbkImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 10), CD11HtPhyBeamformFeedback()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplUncompSteerMatrixFdbkImplemented.setStatus('current')
cD11HtPhyExplCompSteerMatrixFdbkImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 11), CD11HtPhyBeamformFeedback()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyExplCompSteerMatrixFdbkImplemented.setStatus('current')
cD11HtPhyNumberBeamFormingCSISupportAntenna = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyNumberBeamFormingCSISupportAntenna.setStatus('current')
cD11HtPhyNumberUncompSteerMatrixSupportAntenna = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyNumberUncompSteerMatrixSupportAntenna.setStatus('current')
cD11HtPhyNumberCompSteerMatrixSupportAntenna = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyNumberCompSteerMatrixSupportAntenna.setStatus('current')
cD11HtPhyEnhPowerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5), )
if mibBuilder.loadTexts: cD11HtPhyEnhPowerTable.setStatus('current')
cD11HtPhyEnhPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtPhyEnhPowerEntry.setStatus('current')
cD11HtPhyEnhPowerLevel20MHz = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyEnhPowerLevel20MHz.setStatus('current')
cD11HtPhyEnhPowerLevel40MHz = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtPhyEnhPowerLevel40MHz.setStatus('current')
ciscoDot11HtPhyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 1))
ciscoDot11HtPhyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2))
ciscoDot11HtMacCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 1, 1)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "ciscoDot11HtPhyAntennaGroup"), ("CISCO-DOT11-HT-PHY-MIB", "ciscoDot11HtPhyConfigGroup"), ("CISCO-DOT11-HT-PHY-MIB", "ciscoDot11HtPhyMcsGroup"), ("CISCO-DOT11-HT-PHY-MIB", "ciscoDot11HtPhyTxBfGroup"), ("CISCO-DOT11-HT-PHY-MIB", "ciscoDot11HtPhyEnhPowerLevelsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtMacCompliance = ciscoDot11HtMacCompliance.setStatus('current')
ciscoDot11HtPhyAntennaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 1)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAntennaSelectionImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitExpCSIFdbkASImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitIndFdbkASImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCSIFdbkASImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitIndCompFdbkASImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRcvAntennaSelImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitSoundPPDUImplemented"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtPhyAntennaGroup = ciscoDot11HtPhyAntennaGroup.setStatus('current')
ciscoDot11HtPhyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 2)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperatingMode"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperModeFrequency"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperBand"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyFortyMHzOperationImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyFortyMHzOperationEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCurrentControlChannel"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCurrentExtensionChannel"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExtChannelCCAImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberOfSpatialStreamsImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberOfSpatialStreamsEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyGreenFieldImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyGreenFieldEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInTwentyImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInTwentyEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInFortyImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInFortyEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAdvancedCodingImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAdvancedCodingEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxSTBCImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxSTBCEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxSTBCImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxSTBCEnabled"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyBeamFormingImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyBeamFormingEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtPhyConfigGroup = ciscoDot11HtPhyConfigGroup.setStatus('current')
ciscoDot11HtPhyMcsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 3)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhySupportedMCSTxValue"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhySupportedMCSRxValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtPhyMcsGroup = ciscoDot11HtPhyMcsGroup.setStatus('current')
ciscoDot11HtPhyTxBfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 4)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxStaggerSoundImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxStaggerSoundImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxZLFImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxZLFImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyImplicitTxBFImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCalibrationImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCSITxBFImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplUncompSteerMatrixImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplBFCSIFdbkImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplUncompSteerMatrixFdbkImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCompSteerMatrixFdbkImplemented"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberBeamFormingCSISupportAntenna"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberUncompSteerMatrixSupportAntenna"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberCompSteerMatrixSupportAntenna"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtPhyTxBfGroup = ciscoDot11HtPhyTxBfGroup.setStatus('current')
ciscoDot11HtPhyEnhPowerLevelsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 5)).setObjects(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyEnhPowerLevel20MHz"), ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyEnhPowerLevel40MHz"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtPhyEnhPowerLevelsGroup = ciscoDot11HtPhyEnhPowerLevelsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-HT-PHY-MIB", cD11HtPhyXmitIndCompFdbkASImplemented=cD11HtPhyXmitIndCompFdbkASImplemented, cD11HtPhyXmitExpCSIFdbkASImplemented=cD11HtPhyXmitExpCSIFdbkASImplemented, ciscoDot11HtMacCompliance=ciscoDot11HtMacCompliance, cD11HtPhyAntennaTable=cD11HtPhyAntennaTable, cD11HtPhyExtChannelCCAImplemented=cD11HtPhyExtChannelCCAImplemented, ciscoDot11HtPhyAntennaGroup=ciscoDot11HtPhyAntennaGroup, cD11HtPhyEnhPowerTable=cD11HtPhyEnhPowerTable, cD11HtPhyExplCompSteerMatrixFdbkImplemented=cD11HtPhyExplCompSteerMatrixFdbkImplemented, cD11HtPhyFortyMHzOperationImplemented=cD11HtPhyFortyMHzOperationImplemented, ciscoDot11HtPhyEnhPowerLevelsGroup=ciscoDot11HtPhyEnhPowerLevelsGroup, cD11HtPhyShortGIInFortyImplemented=cD11HtPhyShortGIInFortyImplemented, cD11HtPhyTable=cD11HtPhyTable, CD11HtPhyBeamformFeedback=CD11HtPhyBeamformFeedback, ciscoDot11HtPhyMIBConform=ciscoDot11HtPhyMIBConform, cD11HtPhyOperModeFrequency=cD11HtPhyOperModeFrequency, cD11HtPhyTxSTBCImplemented=cD11HtPhyTxSTBCImplemented, cD11HtPhyRxSTBCEnabled=cD11HtPhyRxSTBCEnabled, cD11HtPhyRcvAntennaSelImplemented=cD11HtPhyRcvAntennaSelImplemented, ciscoDot11HtPhyMcsGroup=ciscoDot11HtPhyMcsGroup, cD11HtPhyNumberCompSteerMatrixSupportAntenna=cD11HtPhyNumberCompSteerMatrixSupportAntenna, ciscoDot11HtPhyMIBObjects=ciscoDot11HtPhyMIBObjects, cD11HtPhyRxZLFImplemented=cD11HtPhyRxZLFImplemented, cD11HtPhyCurrentControlChannel=cD11HtPhyCurrentControlChannel, cD11HtPhySupportedMCSRxValue=cD11HtPhySupportedMCSRxValue, cD11HtPhyShortGIInFortyEnabled=cD11HtPhyShortGIInFortyEnabled, cD11HtPhyNumberBeamFormingCSISupportAntenna=cD11HtPhyNumberBeamFormingCSISupportAntenna, cD11HtPhyNumberOfSpatialStreamsImplemented=cD11HtPhyNumberOfSpatialStreamsImplemented, cD11HtPhyBeamFormingEnabled=cD11HtPhyBeamFormingEnabled, cD11HtPhyNumberUncompSteerMatrixSupportAntenna=cD11HtPhyNumberUncompSteerMatrixSupportAntenna, cD11HtPhyAdvancedCodingImplemented=cD11HtPhyAdvancedCodingImplemented, ciscoDot11HtPhyMIBCompliances=ciscoDot11HtPhyMIBCompliances, cD11HtPhyFortyMHzOperationEnabled=cD11HtPhyFortyMHzOperationEnabled, cD11HtPhyExplCSIFdbkASImplemented=cD11HtPhyExplCSIFdbkASImplemented, cD11HtPhyAdvancedCodingEnabled=cD11HtPhyAdvancedCodingEnabled, ciscoDot11HtPhyMIBNotifs=ciscoDot11HtPhyMIBNotifs, cD11HtPhyBeamFormingImplemented=cD11HtPhyBeamFormingImplemented, cD11HtPhyAntennaEntry=cD11HtPhyAntennaEntry, cD11HtPhyAntennaSelectionImplemented=cD11HtPhyAntennaSelectionImplemented, cD11HtPhyCurrentExtensionChannel=cD11HtPhyCurrentExtensionChannel, cD11HtPhyExplBFCSIFdbkImplemented=cD11HtPhyExplBFCSIFdbkImplemented, PYSNMP_MODULE_ID=ciscoDot11HtPhyMIB, ciscoDot11HtPhyMIB=ciscoDot11HtPhyMIB, cD11HtPhyTxBFConfigEntry=cD11HtPhyTxBFConfigEntry, cD11HtPhyTxStaggerSoundImplemented=cD11HtPhyTxStaggerSoundImplemented, ciscoDot11HtPhyMIBGroups=ciscoDot11HtPhyMIBGroups, cD11HtPhyExplUncompSteerMatrixImplemented=cD11HtPhyExplUncompSteerMatrixImplemented, cD11HtPhyTxZLFImplemented=cD11HtPhyTxZLFImplemented, cD11HtPhyShortGIInTwentyEnabled=cD11HtPhyShortGIInTwentyEnabled, cD11HtPhyTxBFConfigTable=cD11HtPhyTxBFConfigTable, cD11HtPhyTxSTBCEnabled=cD11HtPhyTxSTBCEnabled, cD11HtPhyNumberOfSpatialStreamsEnabled=cD11HtPhyNumberOfSpatialStreamsEnabled, cD11HtPhyRxSTBCImplemented=cD11HtPhyRxSTBCImplemented, cD11HtPhyExplUncompSteerMatrixFdbkImplemented=cD11HtPhyExplUncompSteerMatrixFdbkImplemented, cD11HtPhyRxStaggerSoundImplemented=cD11HtPhyRxStaggerSoundImplemented, cD11HtPhyCalibrationImplemented=cD11HtPhyCalibrationImplemented, cD11HtPhyXmitIndFdbkASImplemented=cD11HtPhyXmitIndFdbkASImplemented, cD11HtPhyImplicitTxBFImplemented=cD11HtPhyImplicitTxBFImplemented, cD11HtPhyOperBand=cD11HtPhyOperBand, cD11HtPhySupportedMCSTxValue=cD11HtPhySupportedMCSTxValue, cD11HtPhyEnhPowerLevel20MHz=cD11HtPhyEnhPowerLevel20MHz, ciscoDot11HtPhyTxBfGroup=ciscoDot11HtPhyTxBfGroup, ciscoDot11HtPhyConfigGroup=ciscoDot11HtPhyConfigGroup, cD11HtPhyGreenFieldEnabled=cD11HtPhyGreenFieldEnabled, cD11HtPhy=cD11HtPhy, cD11HtPhyOperatingMode=cD11HtPhyOperatingMode, cD11HtPhySupportedMCSTable=cD11HtPhySupportedMCSTable, cD11HtPhyGreenFieldImplemented=cD11HtPhyGreenFieldImplemented, cD11HtPhyEnhPowerEntry=cD11HtPhyEnhPowerEntry, cD11HtPhySupportedMCSEntry=cD11HtPhySupportedMCSEntry, cD11HtPhyExplCSITxBFImplemented=cD11HtPhyExplCSITxBFImplemented, cD11HtPhyXmitSoundPPDUImplemented=cD11HtPhyXmitSoundPPDUImplemented, cD11HtPhyShortGIInTwentyImplemented=cD11HtPhyShortGIInTwentyImplemented, cD11HtPhyEntry=cD11HtPhyEntry, cD11HtPhyEnhPowerLevel40MHz=cD11HtPhyEnhPowerLevel40MHz)
