#
# PySNMP MIB module CISCO-VSI-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VSI-MASTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter32, Integer32, Bits, ModuleIdentity, Gauge32, TimeTicks, Unsigned32, MibIdentifier, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Integer32", "Bits", "ModuleIdentity", "Gauge32", "TimeTicks", "Unsigned32", "MibIdentifier", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoVsiMasterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 162))
if mibBuilder.loadTexts: ciscoVsiMasterMIB.setLastUpdated('200006010000Z')
if mibBuilder.loadTexts: ciscoVsiMasterMIB.setOrganization('Cisco Systems, Inc.')
class VsiControllerIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VsiSessionIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VsiLogicalIfIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VsiXCIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

ciscoVsiMasterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 162, 1))
ciscoVsiMasterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 162, 2))
ciscoVsiMasterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 162, 3))
vsiMasterControllerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1), )
if mibBuilder.loadTexts: vsiMasterControllerTable.setStatus('current')
vsiMasterControllerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1), ).setIndexNames((0, "CISCO-VSI-MASTER-MIB", "vsiControllerIndex"))
if mibBuilder.loadTexts: vsiMasterControllerEntry.setStatus('current')
vsiControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 1), VsiControllerIndex())
if mibBuilder.loadTexts: vsiControllerIndex.setStatus('current')
vsiControllerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControllerId.setStatus('current')
vsiCrossConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiCrossConnects.setStatus('current')
vsiControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("mpls", 2), ("pnni", 3), ("par", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControllerType.setStatus('current')
vsiBaseVersionSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiBaseVersionSupported.setStatus('current')
vsiTopVersionSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiTopVersionSupported.setStatus('current')
vsiVersionInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiVersionInUse.setStatus('current')
vsiSpecifiedVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsiSpecifiedVersion.setStatus('current')
vsiControlInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControlInterface.setStatus('current')
vsiLogicalControlInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 1, 1, 10), VsiLogicalIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalControlInterface.setStatus('current')
vsiSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2), )
if mibBuilder.loadTexts: vsiSessionTable.setStatus('current')
vsiSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1), ).setIndexNames((0, "CISCO-VSI-MASTER-MIB", "vsiSessionControllerIndex"), (0, "CISCO-VSI-MASTER-MIB", "vsiSessionIndex"))
if mibBuilder.loadTexts: vsiSessionEntry.setStatus('current')
vsiSessionControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 1), VsiControllerIndex())
if mibBuilder.loadTexts: vsiSessionControllerIndex.setStatus('current')
vsiSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 2), VsiSessionIndex())
if mibBuilder.loadTexts: vsiSessionIndex.setStatus('current')
vsiSessionVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionVpi.setStatus('current')
vsiSessionVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionVci.setStatus('current')
vsiSessionSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionSwitchId.setStatus('current')
vsiSessionSwitchName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionSwitchName.setStatus('current')
vsiSessionSlaveId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionSlaveId.setStatus('current')
vsiSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("inactive", 1), ("unknown", 2), ("configuring", 3), ("resyncStarting", 4), ("resyncUnderway", 5), ("resyncEnding", 6), ("discovery", 7), ("established", 8), ("shutdownStarting", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionState.setStatus('current')
vsiSessionWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionWindowSize.setStatus('current')
vsiSessionCmdsPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionCmdsPending.setStatus('current')
vsiSessionActiveId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionActiveId.setStatus('current')
vsiSessionPowerupId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiSessionPowerupId.setStatus('current')
vsiLogicalIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3), )
if mibBuilder.loadTexts: vsiLogicalIfTable.setStatus('current')
vsiLogicalIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1), ).setIndexNames((0, "CISCO-VSI-MASTER-MIB", "vsiLogicalIfControllerIndex"), (0, "CISCO-VSI-MASTER-MIB", "vsiLogicalIfIndex"))
if mibBuilder.loadTexts: vsiLogicalIfEntry.setStatus('current')
vsiLogicalIfControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 1), VsiControllerIndex())
if mibBuilder.loadTexts: vsiLogicalIfControllerIndex.setStatus('current')
vsiLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 2), VsiLogicalIfIndex())
if mibBuilder.loadTexts: vsiLogicalIfIndex.setStatus('current')
vsiLogicalIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfName.setStatus('current')
vsiLogicalIfOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("removed", 1), ("active", 2), ("failedExternal", 3), ("failedInternal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfOperState.setStatus('current')
vsiLogicalIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("pendingDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfAdminState.setStatus('current')
vsiLogicalIfRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfRxCells.setStatus('current')
vsiLogicalIfTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfTxCells.setStatus('current')
vsiLogicalIfRxCellsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfRxCellsDiscarded.setStatus('current')
vsiLogicalIfTxCellsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfTxCellsDiscarded.setStatus('current')
vsiLogicalIfRxHeaderErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfRxHeaderErrors.setStatus('current')
vsiLogicalIfRxInvalidAddrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfRxInvalidAddrs.setStatus('current')
vsiLogicalIfEndPointsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfEndPointsInUse.setStatus('current')
vsiLogicalIfAvailIngressChnls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfAvailIngressChnls.setStatus('current')
vsiLogicalIfAvailEgressChnls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfAvailEgressChnls.setStatus('current')
vsiLogicalIfAvailIngressCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfAvailIngressCellRate.setStatus('current')
vsiLogicalIfAvailEgressCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfAvailEgressCellRate.setStatus('current')
vsiLogicalIfVcMergeSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfVcMergeSupported.setStatus('current')
vsiLogicalIfMulticastSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMulticastSupported.setStatus('current')
vsiLogicalIfVpiTranslated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfVpiTranslated.setStatus('current')
vsiLogicalIfStrictSigRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfStrictSigRange.setStatus('current')
vsiLogicalIfMaxIngressCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMaxIngressCellRate.setStatus('current')
vsiLogicalIfMaxEgressCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMaxEgressCellRate.setStatus('current')
vsiLogicalIfMinVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMinVpi.setStatus('current')
vsiLogicalIfMaxVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMaxVpi.setStatus('current')
vsiLogicalIfMinVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMinVci.setStatus('current')
vsiLogicalIfMaxVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfMaxVci.setStatus('current')
vsiLogicalControlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 27), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalControlIfIndex.setStatus('current')
vsiLogicalIfSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 3, 1, 28), VsiSessionIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiLogicalIfSessionIndex.setStatus('current')
vsiXCTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4), )
if mibBuilder.loadTexts: vsiXCTable.setStatus('current')
vsiXCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1), ).setIndexNames((0, "CISCO-VSI-MASTER-MIB", "vsiXCControllerIndex"), (0, "CISCO-VSI-MASTER-MIB", "vsiXCLogicalIfLow"), (0, "CISCO-VSI-MASTER-MIB", "vsiXCLogicalIfHi"), (0, "CISCO-VSI-MASTER-MIB", "vsiXCIndex"))
if mibBuilder.loadTexts: vsiXCEntry.setStatus('current')
vsiXCControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 1), VsiControllerIndex())
if mibBuilder.loadTexts: vsiXCControllerIndex.setStatus('current')
vsiXCLogicalIfLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 2), VsiLogicalIfIndex())
if mibBuilder.loadTexts: vsiXCLogicalIfLow.setStatus('current')
vsiXCLogicalIfHi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 3), VsiLogicalIfIndex())
if mibBuilder.loadTexts: vsiXCLogicalIfHi.setStatus('current')
vsiXCIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 4), VsiXCIndex())
if mibBuilder.loadTexts: vsiXCIndex.setStatus('current')
vsiXCState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("deleted", 1), ("reserved", 2), ("committed", 3), ("reservedFail", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiXCState.setStatus('current')
vsiXCVpiLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiXCVpiLow.setStatus('current')
vsiXCVciLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiXCVciLow.setStatus('current')
vsiXCVpiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiXCVpiHi.setStatus('current')
vsiXCVciHi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 162, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiXCVciHi.setStatus('current')
ciscoVsiMasterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1))
ciscoVsiMasterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 2))
ciscoVsiMasterModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 2, 1)).setObjects(("CISCO-VSI-MASTER-MIB", "ciscoVsiMasterGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiMasterModuleCompliance = ciscoVsiMasterModuleCompliance.setStatus('current')
ciscoVsiMasterGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 162, 3, 1, 1)).setObjects(("CISCO-VSI-MASTER-MIB", "vsiControllerId"), ("CISCO-VSI-MASTER-MIB", "vsiCrossConnects"), ("CISCO-VSI-MASTER-MIB", "vsiControllerType"), ("CISCO-VSI-MASTER-MIB", "vsiBaseVersionSupported"), ("CISCO-VSI-MASTER-MIB", "vsiTopVersionSupported"), ("CISCO-VSI-MASTER-MIB", "vsiVersionInUse"), ("CISCO-VSI-MASTER-MIB", "vsiSpecifiedVersion"), ("CISCO-VSI-MASTER-MIB", "vsiControlInterface"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalControlInterface"), ("CISCO-VSI-MASTER-MIB", "vsiSessionVpi"), ("CISCO-VSI-MASTER-MIB", "vsiSessionVci"), ("CISCO-VSI-MASTER-MIB", "vsiSessionSwitchId"), ("CISCO-VSI-MASTER-MIB", "vsiSessionSwitchName"), ("CISCO-VSI-MASTER-MIB", "vsiSessionSlaveId"), ("CISCO-VSI-MASTER-MIB", "vsiSessionState"), ("CISCO-VSI-MASTER-MIB", "vsiSessionWindowSize"), ("CISCO-VSI-MASTER-MIB", "vsiSessionCmdsPending"), ("CISCO-VSI-MASTER-MIB", "vsiSessionActiveId"), ("CISCO-VSI-MASTER-MIB", "vsiSessionPowerupId"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfName"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfOperState"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfAdminState"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfRxCells"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfTxCells"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfRxCellsDiscarded"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfTxCellsDiscarded"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfRxHeaderErrors"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfRxInvalidAddrs"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfEndPointsInUse"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfAvailIngressChnls"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfAvailEgressChnls"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfAvailIngressCellRate"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfAvailEgressCellRate"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMaxIngressCellRate"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMaxEgressCellRate"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfVcMergeSupported"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMulticastSupported"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfVpiTranslated"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfStrictSigRange"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMinVpi"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMaxVpi"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMinVci"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfMaxVci"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalControlIfIndex"), ("CISCO-VSI-MASTER-MIB", "vsiLogicalIfSessionIndex"), ("CISCO-VSI-MASTER-MIB", "vsiXCState"), ("CISCO-VSI-MASTER-MIB", "vsiXCVpiLow"), ("CISCO-VSI-MASTER-MIB", "vsiXCVciLow"), ("CISCO-VSI-MASTER-MIB", "vsiXCVpiHi"), ("CISCO-VSI-MASTER-MIB", "vsiXCVciHi"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiMasterGeneralGroup = ciscoVsiMasterGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSI-MASTER-MIB", vsiLogicalControlInterface=vsiLogicalControlInterface, vsiControllerId=vsiControllerId, vsiXCState=vsiXCState, vsiLogicalIfTable=vsiLogicalIfTable, vsiTopVersionSupported=vsiTopVersionSupported, vsiLogicalIfStrictSigRange=vsiLogicalIfStrictSigRange, vsiSessionSwitchName=vsiSessionSwitchName, vsiLogicalIfAvailIngressChnls=vsiLogicalIfAvailIngressChnls, VsiSessionIndex=VsiSessionIndex, vsiLogicalIfAvailEgressChnls=vsiLogicalIfAvailEgressChnls, ciscoVsiMasterModuleCompliance=ciscoVsiMasterModuleCompliance, vsiControlInterface=vsiControlInterface, ciscoVsiMasterMIB=ciscoVsiMasterMIB, vsiLogicalIfMaxIngressCellRate=vsiLogicalIfMaxIngressCellRate, VsiControllerIndex=VsiControllerIndex, vsiVersionInUse=vsiVersionInUse, vsiLogicalIfAvailIngressCellRate=vsiLogicalIfAvailIngressCellRate, vsiLogicalIfMaxVpi=vsiLogicalIfMaxVpi, vsiLogicalIfRxCellsDiscarded=vsiLogicalIfRxCellsDiscarded, vsiBaseVersionSupported=vsiBaseVersionSupported, vsiSessionEntry=vsiSessionEntry, ciscoVsiMasterConformance=ciscoVsiMasterConformance, vsiLogicalIfIndex=vsiLogicalIfIndex, vsiSessionPowerupId=vsiSessionPowerupId, vsiControllerType=vsiControllerType, vsiXCLogicalIfLow=vsiXCLogicalIfLow, VsiLogicalIfIndex=VsiLogicalIfIndex, vsiXCTable=vsiXCTable, vsiXCVciLow=vsiXCVciLow, PYSNMP_MODULE_ID=ciscoVsiMasterMIB, vsiLogicalIfMaxVci=vsiLogicalIfMaxVci, vsiLogicalIfEndPointsInUse=vsiLogicalIfEndPointsInUse, vsiXCLogicalIfHi=vsiXCLogicalIfHi, vsiLogicalIfRxCells=vsiLogicalIfRxCells, vsiLogicalIfRxHeaderErrors=vsiLogicalIfRxHeaderErrors, ciscoVsiMasterGeneralGroup=ciscoVsiMasterGeneralGroup, vsiMasterControllerEntry=vsiMasterControllerEntry, vsiLogicalIfControllerIndex=vsiLogicalIfControllerIndex, vsiSessionVpi=vsiSessionVpi, vsiLogicalIfOperState=vsiLogicalIfOperState, vsiSessionControllerIndex=vsiSessionControllerIndex, vsiSessionIndex=vsiSessionIndex, vsiSessionState=vsiSessionState, ciscoVsiMasterGroups=ciscoVsiMasterGroups, vsiSessionWindowSize=vsiSessionWindowSize, vsiSessionVci=vsiSessionVci, vsiLogicalIfVcMergeSupported=vsiLogicalIfVcMergeSupported, vsiXCControllerIndex=vsiXCControllerIndex, vsiLogicalIfTxCellsDiscarded=vsiLogicalIfTxCellsDiscarded, vsiXCEntry=vsiXCEntry, vsiXCIndex=vsiXCIndex, vsiLogicalIfMinVpi=vsiLogicalIfMinVpi, vsiLogicalIfVpiTranslated=vsiLogicalIfVpiTranslated, vsiControllerIndex=vsiControllerIndex, vsiLogicalIfAvailEgressCellRate=vsiLogicalIfAvailEgressCellRate, vsiCrossConnects=vsiCrossConnects, vsiLogicalIfAdminState=vsiLogicalIfAdminState, vsiLogicalIfMinVci=vsiLogicalIfMinVci, vsiSessionActiveId=vsiSessionActiveId, VsiXCIndex=VsiXCIndex, ciscoVsiMasterObjects=ciscoVsiMasterObjects, vsiLogicalIfMaxEgressCellRate=vsiLogicalIfMaxEgressCellRate, vsiLogicalIfEntry=vsiLogicalIfEntry, vsiLogicalIfTxCells=vsiLogicalIfTxCells, ciscoVsiMasterNotifications=ciscoVsiMasterNotifications, vsiSessionCmdsPending=vsiSessionCmdsPending, vsiLogicalControlIfIndex=vsiLogicalControlIfIndex, vsiSpecifiedVersion=vsiSpecifiedVersion, vsiLogicalIfRxInvalidAddrs=vsiLogicalIfRxInvalidAddrs, vsiSessionSwitchId=vsiSessionSwitchId, vsiMasterControllerTable=vsiMasterControllerTable, vsiXCVpiHi=vsiXCVpiHi, vsiXCVciHi=vsiXCVciHi, vsiSessionTable=vsiSessionTable, vsiLogicalIfName=vsiLogicalIfName, vsiXCVpiLow=vsiXCVpiLow, ciscoVsiMasterCompliances=ciscoVsiMasterCompliances, vsiSessionSlaveId=vsiSessionSlaveId, vsiLogicalIfMulticastSupported=vsiLogicalIfMulticastSupported, vsiLogicalIfSessionIndex=vsiLogicalIfSessionIndex)
