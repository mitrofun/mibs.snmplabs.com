#
# PySNMP MIB module PDN-ADSL-SELT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-ADSL-SELT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ModuleIdentity, Integer32, Gauge32, IpAddress, Counter64, iso, MibIdentifier, Counter32, TimeTicks, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "IpAddress", "Counter64", "iso", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnAdslSeltMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31))
pdnAdslSeltMIB.setRevisions(('2005-03-28 00:00', '2005-03-10 00:00', '2004-12-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnAdslSeltMIB.setRevisionsDescriptions(('Added clearResults(4) to pdnAdslSeltCmd to allow an entry in the pdnAdslSeltLcTable or the pdnAdslSeltLnfTable to be removed. Added resultsCleared(5) to pdnAdslSeltStatus to indicate that clearResults(4) have been executed.', 'Added notStarted(4) to pdnAdslSeltStatus. This solves the problem of what to return when the pdnAdslSeltTable is walked prior to a test being run on an interface.', 'Initial release.',))
if mibBuilder.loadTexts: pdnAdslSeltMIB.setLastUpdated('200403280000Z')
if mibBuilder.loadTexts: pdnAdslSeltMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
if mibBuilder.loadTexts: pdnAdslSeltMIB.setContactInfo('Paradyne Networks, Inc. 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editors Jesus Pinto, Clay Sikes')
if mibBuilder.loadTexts: pdnAdslSeltMIB.setDescription("This MIB module defines a portion of the management information base (MIB) for managing configuration and monitoring results of SELT (Single Ended Line Test) tests over ADSL interfaces. At the time this MIB was defined, the IETF ADSL MIB Working does not have any work on the 'standard' MIBs planned and/or has not produced a schedule to address G.SELT needs. As a result, these objects may be a `temporary' solution until MIBs/Objects are defined meet the needs of ADSL SELT testing. ===================================================================== == == == Copyright (C) 2005 Paradyne Corporation. == == == =====================================================================")
pdnAdslSeltNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 0))
pdnAdslSeltObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1))
pdnAdslSeltAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 2))
pdnAdslSeltConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3))
class PdnSeltTypes(TextualConvention, Integer32):
    description = 'This textual convention defines the SELT test types available for configuration.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loopCharacterization", 1), ("loopNoiseFloor", 2))

pdnAdslSeltWireSize = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("awg", 1), ("metric", 2), ("metricJapan", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnAdslSeltWireSize.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltWireSize.setDescription('This object permits the selection of the metric unit to be used when reporting SELT test results. (i.e for AWG results are in feet and for metric/metricJapan results are in meters). This configuration parameter applies to all the SELT tests run in the device. ')
pdnAdslSeltTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2), )
if mibBuilder.loadTexts: pdnAdslSeltTable.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltTable.setDescription('This table allows initiation/termination of SELT Tests.')
pdnAdslSeltEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltType"))
if mibBuilder.loadTexts: pdnAdslSeltEntry.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltEntry.setDescription('Each entry represents an instance of a SELT test currently running or ever run (since last system reset) on an ADSL interface. There should be entries in this table for every active running tests and test that are in the process of being stopped or have terminated already. There should be no entries for ADSL interfaces that have not run a test since last since reset; thus, the agent should return NO_SUCH_NAME for those cases. ')
pdnAdslSeltType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 1), PdnSeltTypes())
if mibBuilder.loadTexts: pdnAdslSeltType.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltType.setDescription('This object is used to specify the SELT test type that will be initiated. If a SELT Test is already running on the ADSL interface, writing to this object is prohibited by the agent until the previous test is completed or terminated. ')
pdnAdslSeltCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noOp", 1), ("start", 2), ("stop", 3), ("clearResults", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnAdslSeltCmd.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltCmd.setDescription("This object corresponds to the list of test operations that can be performed. The possible values are noOp(1), start(2), stop(3), or clearResults(4). Reading this object will always return the value 'noOp (1)'. If SELT test is already running on an ADSL interface, the only possible test command is 'stop (1)'. The clearResults(4) command clears test results by removing and entry in the pdnAdslSeltLcTable or the pdnAdslSeltLnfTable. After the execution of this command, the appropriate value for pdnAdslSeltStatus would be resultsCleared(5). ")
pdnAdslSeltStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inProgress", 1), ("stoppedInProgress", 2), ("complete", 3), ("notStarted", 4), ("resultsCleared", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltStatus.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltStatus.setDescription('This object provides status about any SELT test running or ever run (since last reset) on an ADSL interface. This object can be read by NMS managers to determine the status of a test; that is: inProgress (1) - if the test is currently running. stoppedInProgress (2) - if a request to stop the test is still in progress. complete (3) - if the test has been run at least once since system reset and has completed. notStarted (4) - if the test has not been run on this interface since last system reset. resultsCleared (5) - if the entry in the test results table, Lc or Lnf, was removed as the result of the execution of the clearResults(4) pdnAdslSeltCmd. ')
pdnAdslSeltDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnAdslSeltDuration.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltDuration.setDescription('This object provides the approximate time in Seconds that the SELT test measurement will take. This object should return 0 if no test is actively running on the ADSL interface specified. ')
pdnAdslSeltTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltTimeLeft.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltTimeLeft.setDescription('This object provides the approximate time left in Seconds for the test running on this ADSL interface. This object should return 0 if no test is actively running on the ADSL interface specified. ')
pdnAdslSeltLcTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3), )
if mibBuilder.loadTexts: pdnAdslSeltLcTable.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcTable.setDescription('This table post results for loop characterization tests completed. ')
pdnAdslSeltLcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentIndex"))
if mibBuilder.loadTexts: pdnAdslSeltLcEntry.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcEntry.setDescription('Each entry represents the results of a loop characterization test performed over an ADSL interface. ')
pdnAdslSeltLcSegmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9)))
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentIndex.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentIndex.setDescription('This object indicates the index of the segment being reported. From no segments to a possible of 10 segments could be identified in the loop topology. ')
pdnAdslSeltLcSegmentLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentLength.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentLength.setDescription('This object indicates an estimate of the segment Length being reported ')
pdnAdslSeltLcSegmentGauge = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("unknown", 1), ("awg26", 2), ("awg24", 3), ("awg22", 4), ("awg19", 5), ("metric32", 10), ("metric40", 11), ("metric50", 12), ("metric63", 13), ("metric90", 14), ("metricJapan32", 20), ("metricJapan40", 21), ("metricJapan50", 22), ("metricJapan65", 23), ("metricJapan90", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentGauge.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentGauge.setDescription('This object indicates the estimated Gauge of the segment being reported. The gauge reported back is based on the pdnAdslSeltWireSizeWireSize configuration parameter passed when the test is started. ')
pdnAdslSeltLcSegmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("inline", 2), ("bridgeTap", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentType.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcSegmentType.setDescription('This object indicates the segment type being reported. ')
pdnAdslSeltLnfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4), )
if mibBuilder.loadTexts: pdnAdslSeltLnfTable.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfTable.setDescription('This table post results for loop noise floor tests completed. ')
pdnAdslSeltLnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfSubCarrierIndex"))
if mibBuilder.loadTexts: pdnAdslSeltLnfEntry.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfEntry.setDescription('Each entry represents the results of a Loop Noise Floor test performed over an ADSL interface. ')
pdnAdslSeltLnfSubCarrierIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: pdnAdslSeltLnfSubCarrierIndex.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfSubCarrierIndex.setDescription("Identifies a row in the table based on a subcarrier. The subcarrier index ranges from 0 to NSCus-1 (NSC is Number of Subcarriers) as specified in G.997.1 where NSCus is the higher subcarrier that can be transmitted in the upstream direction. Please refer to the corresponding ITU recommendation for specific values of NSCus. The `ADSL Values for NSC' comment above lists those recommendations.")
pdnAdslSeltLnfPeakPsd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLnfPeakPsd.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfPeakPsd.setDescription('This object indicates the peak Psd of the tone indicated by the sub-carrier index. The value returned by the agent for this object is expressed in units of 1/256 dBm. ')
pdnAdslSeltLnfTotalPsd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLnfTotalPsd.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfTotalPsd.setDescription('This object indicates the total Psd of the tone indicated by the sub-carrier index. The value returned by the agent for this object is expressed in units of 1/256 dBm. ')
pdnAdslSeltLnfSignalPsd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnAdslSeltLnfSignalPsd.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfSignalPsd.setDescription('This object indicates the signal Psd of the tone indicated by the sub-carrier index. The value returned by the agent for this object is expressed in units of 1/256 dBm. ')
pdnAdslSeltCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 1))
pdnAdslSeltGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2))
pdnAdslSeltMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 1, 1)).setObjects(("PDN-ADSL-SELT-MIB", "pdnAdslSeltGroup"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcGroup"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAdslSeltMIBCompliance = pdnAdslSeltMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltMIBCompliance.setDescription('The compliance statement for the entities which implement the pdnAdslSeltMIB.')
pdnAdslSeltObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1))
pdnAdslSeltAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 2))
pdnAdslSeltNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 3))
pdnAdslSeltGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 1)).setObjects(("PDN-ADSL-SELT-MIB", "pdnAdslSeltCmd"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltStatus"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltWireSize"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltDuration"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltTimeLeft"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAdslSeltGroup = pdnAdslSeltGroup.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltGroup.setDescription('General configuration of SELT tests.')
pdnAdslSeltLcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 2)).setObjects(("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentLength"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentGauge"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAdslSeltLcGroup = pdnAdslSeltLcGroup.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLcGroup.setDescription('Objects related to results posted for Loop Characterization Test.')
pdnAdslSeltLnfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 3)).setObjects(("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfPeakPsd"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfTotalPsd"), ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfSignalPsd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAdslSeltLnfGroup = pdnAdslSeltLnfGroup.setStatus('current')
if mibBuilder.loadTexts: pdnAdslSeltLnfGroup.setDescription('Objects related to results posted for Loop Signal Floor Test.')
mibBuilder.exportSymbols("PDN-ADSL-SELT-MIB", pdnAdslSeltLnfTable=pdnAdslSeltLnfTable, pdnAdslSeltLnfGroup=pdnAdslSeltLnfGroup, pdnAdslSeltNtfyGroups=pdnAdslSeltNtfyGroups, pdnAdslSeltStatus=pdnAdslSeltStatus, pdnAdslSeltLnfSignalPsd=pdnAdslSeltLnfSignalPsd, pdnAdslSeltLnfTotalPsd=pdnAdslSeltLnfTotalPsd, pdnAdslSeltTable=pdnAdslSeltTable, pdnAdslSeltCompliances=pdnAdslSeltCompliances, pdnAdslSeltNotifications=pdnAdslSeltNotifications, pdnAdslSeltLnfEntry=pdnAdslSeltLnfEntry, pdnAdslSeltLnfPeakPsd=pdnAdslSeltLnfPeakPsd, pdnAdslSeltObjects=pdnAdslSeltObjects, pdnAdslSeltLcGroup=pdnAdslSeltLcGroup, pdnAdslSeltMIB=pdnAdslSeltMIB, pdnAdslSeltLcTable=pdnAdslSeltLcTable, PdnSeltTypes=PdnSeltTypes, pdnAdslSeltLcSegmentType=pdnAdslSeltLcSegmentType, pdnAdslSeltAFNs=pdnAdslSeltAFNs, pdnAdslSeltTimeLeft=pdnAdslSeltTimeLeft, pdnAdslSeltConformance=pdnAdslSeltConformance, PYSNMP_MODULE_ID=pdnAdslSeltMIB, pdnAdslSeltLcSegmentLength=pdnAdslSeltLcSegmentLength, pdnAdslSeltEntry=pdnAdslSeltEntry, pdnAdslSeltLcSegmentGauge=pdnAdslSeltLcSegmentGauge, pdnAdslSeltType=pdnAdslSeltType, pdnAdslSeltLcEntry=pdnAdslSeltLcEntry, pdnAdslSeltGroup=pdnAdslSeltGroup, pdnAdslSeltWireSize=pdnAdslSeltWireSize, pdnAdslSeltObjGroups=pdnAdslSeltObjGroups, pdnAdslSeltGroups=pdnAdslSeltGroups, pdnAdslSeltAfnGroups=pdnAdslSeltAfnGroups, pdnAdslSeltMIBCompliance=pdnAdslSeltMIBCompliance, pdnAdslSeltCmd=pdnAdslSeltCmd, pdnAdslSeltDuration=pdnAdslSeltDuration, pdnAdslSeltLcSegmentIndex=pdnAdslSeltLcSegmentIndex, pdnAdslSeltLnfSubCarrierIndex=pdnAdslSeltLnfSubCarrierIndex)
