#
# PySNMP MIB module TPLINK-SPANNING-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SPANNING-TREE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, Counter32, ObjectIdentity, Bits, Integer32, Counter64, iso, TimeTicks, Gauge32, IpAddress, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Counter32", "ObjectIdentity", "Bits", "Integer32", "Counter64", "iso", "TimeTicks", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkSpanningTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 21))
tplinkSpanningTreeMIB.setRevisions(('2012-11-21 09:30',))
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setLastUpdated('201211210930Z')
if mibBuilder.loadTexts: tplinkSpanningTreeMIB.setOrganization('TPLINK')
tplinkSpanningTreeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1))
tpStpBasicCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1))
tpStpBasicGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1))
tpStpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpEnable.setStatus('current')
tpRstpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRstpEnable.setStatus('current')
tpMstpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpEnable.setStatus('current')
tpStpBasicParamConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2))
tpStpCistPriority = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpCistPriority.setStatus('current')
tpStpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpHelloTime.setStatus('current')
tpStpAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpAgingTime.setStatus('current')
tpStpForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpForwardDelay.setStatus('current')
tpStpHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpHoldCount.setStatus('current')
tpStpMaxHops = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpMaxHops.setStatus('current')
tpStpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3))
tpStpEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpEnableStatus.setStatus('current')
tpStpMode = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stp", 1), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpMode.setStatus('current')
tpStpLocalBridge = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpLocalBridge.setStatus('current')
tpStpCISTRoot = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpCISTRoot.setStatus('current')
tpStpExPathCost = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpExPathCost.setStatus('current')
tpStpRegionRoot = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpRegionRoot.setStatus('current')
tpStpInPathCost = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpInPathCost.setStatus('current')
tpStpDesignatedBridge = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDesignatedBridge.setStatus('current')
tpStpRootPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpRootPort.setStatus('current')
tpStpLastTopologyChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpLastTopologyChangeTime.setStatus('current')
tpStpTopologyChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpTopologyChangeCounter.setStatus('current')
tpStpPortCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2))
tpStpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1), )
if mibBuilder.loadTexts: tpStpPortConfigTable.setStatus('current')
tpStpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpStpPortConfigEntry.setStatus('current')
tpStpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortNumber.setStatus('current')
tpStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1), ("errPort", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortEnable.setStatus('current')
tpStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortPriority.setStatus('current')
tpStpPortExPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortExPathCost.setStatus('current')
tpStpPortInPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortInPathCost.setStatus('current')
tpStpEdgePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpEdgePortStatus.setStatus('current')
tpStpPointToPointStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("force-enable", 1), ("force-disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPointToPointStatus.setStatus('current')
tpStpPortMCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unChange", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpPortMCheck.setStatus('current')
tpStpPortStpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("n-a", 0), ("stp", 1), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortStpVersion.setStatus('current')
tpStpPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("alternate", 2), ("backup", 3), ("designated", 4), ("root", 5), ("master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortRole.setStatus('current')
tpStpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("n-a", 0), ("disconnected", 1), ("blocking", 2), ("learning", 3), ("forwarding", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortStatus.setStatus('current')
tpStpPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpPortLag.setStatus('current')
tpStpInstanceCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3))
tpMstpRegionConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1))
tpMstpRegionName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpRegionName.setStatus('current')
tpMstpRevision = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpRevision.setStatus('current')
tpMstpInstanceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2), )
if mibBuilder.loadTexts: tpMstpInstanceConfigTable.setStatus('current')
tpMstpInstanceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1), ).setIndexNames((0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstanceId"))
if mibBuilder.loadTexts: tpMstpInstanceConfigEntry.setStatus('current')
tpMstpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstanceId.setStatus('current')
tpMstpInstanceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstanceEnable.setStatus('current')
tpMstpInstancePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePriority.setStatus('current')
tpMstpInstanceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstanceVlanId.setStatus('current')
tpMstpClearInstanceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpClearInstanceVlanId.setStatus('current')
tpMstpInstancePortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3), )
if mibBuilder.loadTexts: tpMstpInstancePortConfigTable.setStatus('current')
tpMstpInstancePortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1), ).setIndexNames((0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstancePortConfigId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpMstpInstancePortConfigEntry.setStatus('current')
tpMstpInstancePortConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortConfigId.setStatus('current')
tpMstpInstancePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortNumber.setStatus('current')
tpMstpInstancePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePortPriority.setStatus('current')
tpMstpInstancePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpMstpInstancePortPathCost.setStatus('current')
tpMstpInstancePortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("alternate", 2), ("backup", 3), ("designated", 4), ("root", 5), ("master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortRole.setStatus('current')
tpMstpInstancePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("blocking", 2), ("learning", 3), ("forwarding", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortStatus.setStatus('current')
tpMstpInstancePortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMstpInstancePortLag.setStatus('current')
tpStpSecurityCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4))
tpStpPortDefendTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1), )
if mibBuilder.loadTexts: tpStpPortDefendTable.setStatus('current')
tpStpPortDefendEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpStpPortDefendEntry.setStatus('current')
tpStpDefendPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDefendPortNumber.setStatus('current')
tpStpLoopDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpLoopDefendEnable.setStatus('current')
tpStpRootBridgeDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpRootBridgeDefendEnable.setStatus('current')
tpStpTcDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendEnable.setStatus('current')
tpStpBPDUDefendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpBPDUDefendEnable.setStatus('current')
tpStpBPDUHoldEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpBPDUHoldEnable.setStatus('current')
tpStpDefendPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStpDefendPortLag.setStatus('current')
tpStpTcDefendConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2))
tpStpTcDefendThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendThreshold.setStatus('current')
tpStpTcDefendTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStpTcDefendTimer.setStatus('current')
tplinkSpanningTreeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 21, 2))
tpMstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 21, 2, 1))
if mibBuilder.loadTexts: tpMstpTopologyChange.setStatus('current')
mibBuilder.exportSymbols("TPLINK-SPANNING-TREE-MIB", tpStpPortInPathCost=tpStpPortInPathCost, tplinkSpanningTreeMIB=tplinkSpanningTreeMIB, tpStpRootPort=tpStpRootPort, tpMstpInstancePortPathCost=tpMstpInstancePortPathCost, PYSNMP_MODULE_ID=tplinkSpanningTreeMIB, tpMstpInstancePortPriority=tpMstpInstancePortPriority, tpStpPortCfg=tpStpPortCfg, tpStpExPathCost=tpStpExPathCost, tpStpBasicCfg=tpStpBasicCfg, tpStpCistPriority=tpStpCistPriority, tpMstpInstancePortConfigId=tpMstpInstancePortConfigId, tpStpPortLag=tpStpPortLag, tpStpPortConfigTable=tpStpPortConfigTable, tpMstpInstancePortConfigEntry=tpMstpInstancePortConfigEntry, tpMstpInstanceEnable=tpMstpInstanceEnable, tpMstpRegionName=tpMstpRegionName, tpMstpRevision=tpMstpRevision, tpStpPortMCheck=tpStpPortMCheck, tpStpInstanceCfg=tpStpInstanceCfg, tpStpCISTRoot=tpStpCISTRoot, tpStpHoldCount=tpStpHoldCount, tpStpBPDUHoldEnable=tpStpBPDUHoldEnable, tpStpPortPriority=tpStpPortPriority, tplinkSpanningTreeMIBObjects=tplinkSpanningTreeMIBObjects, tpStpTcDefendConfig=tpStpTcDefendConfig, tpMstpInstanceVlanId=tpMstpInstanceVlanId, tpStpLastTopologyChangeTime=tpStpLastTopologyChangeTime, tpMstpEnable=tpMstpEnable, tpMstpTopologyChange=tpMstpTopologyChange, tpStpPortDefendTable=tpStpPortDefendTable, tpStpMaxHops=tpStpMaxHops, tpMstpInstanceId=tpMstpInstanceId, tpStpEnable=tpStpEnable, tpStpRootBridgeDefendEnable=tpStpRootBridgeDefendEnable, tplinkSpanningTreeNotifications=tplinkSpanningTreeNotifications, tpStpPortStpVersion=tpStpPortStpVersion, tpStpTcDefendThreshold=tpStpTcDefendThreshold, tpStpForwardDelay=tpStpForwardDelay, tpStpBPDUDefendEnable=tpStpBPDUDefendEnable, tpStpPortNumber=tpStpPortNumber, tpStpDesignatedBridge=tpStpDesignatedBridge, tpStpInfo=tpStpInfo, tpStpPointToPointStatus=tpStpPointToPointStatus, tpStpPortStatus=tpStpPortStatus, tpMstpInstancePortStatus=tpMstpInstancePortStatus, tpStpBasicParamConfig=tpStpBasicParamConfig, tpStpPortDefendEntry=tpStpPortDefendEntry, tpMstpInstanceConfigEntry=tpMstpInstanceConfigEntry, tpStpTopologyChangeCounter=tpStpTopologyChangeCounter, tpMstpClearInstanceVlanId=tpMstpClearInstanceVlanId, tpMstpInstancePortLag=tpMstpInstancePortLag, tpStpInPathCost=tpStpInPathCost, tpStpLoopDefendEnable=tpStpLoopDefendEnable, tpStpPortRole=tpStpPortRole, tpStpTcDefendTimer=tpStpTcDefendTimer, tpStpBasicGlobalConfig=tpStpBasicGlobalConfig, tpMstpInstancePortNumber=tpMstpInstancePortNumber, tpStpEdgePortStatus=tpStpEdgePortStatus, tpRstpEnable=tpRstpEnable, tpStpTcDefendEnable=tpStpTcDefendEnable, tpStpSecurityCfg=tpStpSecurityCfg, tpStpPortConfigEntry=tpStpPortConfigEntry, tpMstpInstancePortRole=tpMstpInstancePortRole, tpStpHelloTime=tpStpHelloTime, tpMstpInstanceConfigTable=tpMstpInstanceConfigTable, tpMstpInstancePriority=tpMstpInstancePriority, tpStpRegionRoot=tpStpRegionRoot, tpMstpRegionConfig=tpMstpRegionConfig, tpStpAgingTime=tpStpAgingTime, tpStpMode=tpStpMode, tpStpPortExPathCost=tpStpPortExPathCost, tpStpPortEnable=tpStpPortEnable, tpStpLocalBridge=tpStpLocalBridge, tpMstpInstancePortConfigTable=tpMstpInstancePortConfigTable, tpStpDefendPortLag=tpStpDefendPortLag, tpStpEnableStatus=tpStpEnableStatus, tpStpDefendPortNumber=tpStpDefendPortNumber)