#
# PySNMP MIB module MSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, Gauge32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "Counter32", "iso")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
swMSTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 15))
if mibBuilder.loadTexts: swMSTPMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swMSTPMIB.setOrganization(' ')
class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

swMSTPGblMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 15, 1))
swMSTPCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 15, 2))
swMSTPStpAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpAdminState.setStatus('current')
swMSTPStpVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 1), ("mstp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpVersion.setStatus('current')
swMSTPStpMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpMaxAge.setStatus('current')
swMSTPStpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpHelloTime.setStatus('current')
swMSTPStpForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpForwardDelay.setStatus('current')
swMSTPStpMaxHops = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpMaxHops.setStatus('current')
swMSTPStpTxHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpTxHoldCount.setStatus('current')
swMSTPStpForwardBPDU = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpForwardBPDU.setStatus('current')
swMSTPStpLBD = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpLBD.setStatus('current')
swMSTPStpLBDRecoverTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPStpLBDRecoverTime.setStatus('current')
swMSTPName = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPName.setStatus('current')
swMSTPRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPRevisionLevel.setStatus('current')
swMSTPInstanceCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3), )
if mibBuilder.loadTexts: swMSTPInstanceCtrlTable.setStatus('current')
swMSTPInstanceCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1), ).setIndexNames((0, "MSTP-MIB", "swMSTPInstId"))
if mibBuilder.loadTexts: swMSTPInstanceCtrlEntry.setStatus('current')
swMSTPInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstId.setStatus('current')
swMSTPInstVlanRangeList1to64 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList1to64.setStatus('current')
swMSTPInstVlanRangeList65to128 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList65to128.setStatus('current')
swMSTPInstVlanRangeList129to192 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList129to192.setStatus('current')
swMSTPInstVlanRangeList193to256 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList193to256.setStatus('current')
swMSTPInstVlanRangeList257to320 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList257to320.setStatus('current')
swMSTPInstVlanRangeList321to384 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList321to384.setStatus('current')
swMSTPInstVlanRangeList385to448 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList385to448.setStatus('current')
swMSTPInstVlanRangeList449to512 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstVlanRangeList449to512.setStatus('current')
swMSTPInstType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("cist", 0), ("msti", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstType.setStatus('current')
swMSTPInstStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstStatus.setStatus('current')
swMSTPInstPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstPriority.setStatus('current')
swMSTPInstDesignatedRootBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 13), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstDesignatedRootBridge.setStatus('current')
swMSTPInstExternalRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstExternalRootCost.setStatus('current')
swMSTPInstRegionalRootBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 15), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstRegionalRootBridge.setStatus('current')
swMSTPInstInternalRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstInternalRootCost.setStatus('current')
swMSTPInstDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 17), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstDesignatedBridge.setStatus('current')
swMSTPInstRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstRootPort.setStatus('current')
swMSTPInstMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstMaxAge.setStatus('current')
swMSTPInstForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstForwardDelay.setStatus('current')
swMSTPInstLastTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 21), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstLastTopologyChange.setStatus('current')
swMSTPInstTopChangesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstTopChangesCount.setStatus('current')
swMSTPInstRemainHops = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPInstRemainHops.setStatus('current')
swMSTPInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 24), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swMSTPInstRowStatus.setStatus('current')
swMSTPPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4), )
if mibBuilder.loadTexts: swMSTPPortTable.setStatus('current')
swMSTPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1), ).setIndexNames((0, "MSTP-MIB", "swMSTPPort"))
if mibBuilder.loadTexts: swMSTPPortEntry.setStatus('current')
swMSTPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPPort.setStatus('current')
swMSTPPortOperHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPPortOperHelloTime.setStatus('current')
swMSTPPortAdminHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortAdminHelloTime.setStatus('current')
swMSTPSTPPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPSTPPortEnable.setStatus('current')
swMSTPPortExternalPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortExternalPathCost.setStatus('current')
swMSTPPortMigration = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortMigration.setStatus('current')
swMSTPPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortAdminEdgePort.setStatus('current')
swMSTPPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPPortOperEdgePort.setStatus('current')
swMSTPPortAdminP2P = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("true", 0), ("false", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortAdminP2P.setStatus('current')
swMSTPPortOperP2P = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("true", 0), ("false", 1), ("auto", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPPortOperP2P.setStatus('current')
swMSTPPortLBD = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortLBD.setStatus('current')
swMSTPPortBPDUFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortBPDUFiltering.setStatus('current')
swMSTPPortRestrictedRole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortRestrictedRole.setStatus('current')
swMSTPPortRestrictedTCN = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPPortRestrictedTCN.setStatus('current')
swMSTPMstPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5), )
if mibBuilder.loadTexts: swMSTPMstPortTable.setStatus('current')
swMSTPMstPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1), ).setIndexNames((0, "MSTP-MIB", "swMSTPMstPort"), (0, "MSTP-MIB", "swMSTPMstPortInsID"))
if mibBuilder.loadTexts: swMSTPMstPortEntry.setStatus('current')
swMSTPMstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPMstPort.setStatus('current')
swMSTPMstPortInsID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPMstPortInsID.setStatus('current')
swMSTPMstPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 3), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPMstPortDesignatedBridge.setStatus('current')
swMSTPMstPortInternalPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPMstPortInternalPathCost.setStatus('current')
swMSTPMstPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swMSTPMstPortPriority.setStatus('current')
swMSTPMstPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("discarding", 3), ("learning", 4), ("forwarding", 5), ("broken", 6), ("no-stp-enabled", 7), ("err-disabled", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPMstPortStatus.setStatus('current')
swMSTPMstPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 0), ("alternate", 1), ("backup", 2), ("root", 3), ("designated", 4), ("master", 5), ("nonstp", 6), ("loopback", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMSTPMstPortRole.setStatus('current')
mibBuilder.exportSymbols("MSTP-MIB", swMSTPInstanceCtrlTable=swMSTPInstanceCtrlTable, swMSTPPortOperEdgePort=swMSTPPortOperEdgePort, swMSTPMstPortPriority=swMSTPMstPortPriority, PYSNMP_MODULE_ID=swMSTPMIB, swMSTPInstRowStatus=swMSTPInstRowStatus, swMSTPMstPortRole=swMSTPMstPortRole, swMSTPInstInternalRootCost=swMSTPInstInternalRootCost, swMSTPPortMigration=swMSTPPortMigration, swMSTPMstPortTable=swMSTPMstPortTable, swMSTPMIB=swMSTPMIB, swMSTPMstPortInternalPathCost=swMSTPMstPortInternalPathCost, swMSTPMstPortDesignatedBridge=swMSTPMstPortDesignatedBridge, swMSTPMstPort=swMSTPMstPort, swMSTPStpAdminState=swMSTPStpAdminState, swMSTPInstRootPort=swMSTPInstRootPort, swMSTPPortOperP2P=swMSTPPortOperP2P, swMSTPPortTable=swMSTPPortTable, swMSTPInstTopChangesCount=swMSTPInstTopChangesCount, swMSTPInstDesignatedRootBridge=swMSTPInstDesignatedRootBridge, swMSTPPortOperHelloTime=swMSTPPortOperHelloTime, swMSTPPortLBD=swMSTPPortLBD, swMSTPRevisionLevel=swMSTPRevisionLevel, swMSTPMstPortEntry=swMSTPMstPortEntry, swMSTPMstPortStatus=swMSTPMstPortStatus, swMSTPStpTxHoldCount=swMSTPStpTxHoldCount, swMSTPGblMgmt=swMSTPGblMgmt, swMSTPName=swMSTPName, swMSTPStpMaxAge=swMSTPStpMaxAge, swMSTPInstRemainHops=swMSTPInstRemainHops, swMSTPPortBPDUFiltering=swMSTPPortBPDUFiltering, swMSTPPortRestrictedRole=swMSTPPortRestrictedRole, swMSTPCtrl=swMSTPCtrl, swMSTPStpHelloTime=swMSTPStpHelloTime, swMSTPSTPPortEnable=swMSTPSTPPortEnable, swMSTPInstExternalRootCost=swMSTPInstExternalRootCost, swMSTPPortAdminEdgePort=swMSTPPortAdminEdgePort, BridgeId=BridgeId, swMSTPPortExternalPathCost=swMSTPPortExternalPathCost, swMSTPPort=swMSTPPort, swMSTPInstVlanRangeList1to64=swMSTPInstVlanRangeList1to64, swMSTPInstVlanRangeList129to192=swMSTPInstVlanRangeList129to192, swMSTPMstPortInsID=swMSTPMstPortInsID, swMSTPStpForwardBPDU=swMSTPStpForwardBPDU, swMSTPInstVlanRangeList321to384=swMSTPInstVlanRangeList321to384, swMSTPStpLBD=swMSTPStpLBD, swMSTPInstVlanRangeList385to448=swMSTPInstVlanRangeList385to448, swMSTPInstId=swMSTPInstId, swMSTPInstVlanRangeList193to256=swMSTPInstVlanRangeList193to256, swMSTPInstanceCtrlEntry=swMSTPInstanceCtrlEntry, swMSTPInstDesignatedBridge=swMSTPInstDesignatedBridge, swMSTPStpForwardDelay=swMSTPStpForwardDelay, swMSTPPortAdminHelloTime=swMSTPPortAdminHelloTime, swMSTPInstVlanRangeList257to320=swMSTPInstVlanRangeList257to320, swMSTPInstPriority=swMSTPInstPriority, swMSTPInstStatus=swMSTPInstStatus, swMSTPPortEntry=swMSTPPortEntry, swMSTPStpMaxHops=swMSTPStpMaxHops, swMSTPInstType=swMSTPInstType, swMSTPInstForwardDelay=swMSTPInstForwardDelay, swMSTPPortRestrictedTCN=swMSTPPortRestrictedTCN, swMSTPInstLastTopologyChange=swMSTPInstLastTopologyChange, swMSTPInstRegionalRootBridge=swMSTPInstRegionalRootBridge, swMSTPInstMaxAge=swMSTPInstMaxAge, swMSTPInstVlanRangeList449to512=swMSTPInstVlanRangeList449to512, swMSTPStpLBDRecoverTime=swMSTPStpLBDRecoverTime, swMSTPPortAdminP2P=swMSTPPortAdminP2P, swMSTPInstVlanRangeList65to128=swMSTPInstVlanRangeList65to128, swMSTPStpVersion=swMSTPStpVersion)
