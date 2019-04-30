#
# PySNMP MIB module WWP-LEOS-VLAN-TAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-VLAN-TAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Integer32, IpAddress, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, Counter64, Bits, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Integer32", "IpAddress", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "Counter64", "Bits", "MibIdentifier", "iso")
RowStatus, TruthValue, TimeStamp, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TimeStamp", "MacAddress", "DisplayString", "TextualConvention")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5))
wwpLeosVlanMIB.setRevisions(('2007-09-29 17:00', '2003-01-15 17:00',))
if mibBuilder.loadTexts: wwpLeosVlanMIB.setLastUpdated('200709291700Z')
if mibBuilder.loadTexts: wwpLeosVlanMIB.setOrganization('Ciena, Inc')
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 24576)

class VlanTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpLeosVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1))
wwpLeosVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1))
wwpLeosVlanEPR = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2))
wwpLeosVlanMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 2))
wwpLeosVlanMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 2, 0))
wwpLeosVlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3))
wwpLeosVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3, 1))
wwpLeosVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3, 2))
wwpLeosMaxVlans = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosMaxVlans.setStatus('current')
wwpLeosMaxSupportedVlanTagId = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosMaxSupportedVlanTagId.setStatus('current')
wwpLeosNumVlans = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosNumVlans.setStatus('current')
wwpLeosVlanTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4), )
if mibBuilder.loadTexts: wwpLeosVlanTable.setStatus('current')
wwpLeosVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"))
if mibBuilder.loadTexts: wwpLeosVlanEntry.setStatus('current')
wwpLeosVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanId.setStatus('current')
wwpLeosVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanName.setStatus('current')
wwpLeosVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanStatus.setStatus('current')
wwpLeosVlanMacLrnState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanMacLrnState.setStatus('current')
wwpLeosVlanMacLrnOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("vsOverride", 3))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanMacLrnOperState.setStatus('current')
wwpLeosVlanTranslationVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24576))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanTranslationVlan.setStatus('current')
wwpLeosVlanEgressTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tpid8100", 1), ("tpid9100", 2), ("tpid88A8", 3))).clone('tpid8100')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanEgressTpid.setStatus('current')
wwpLeosVlanTagMemberTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5), )
if mibBuilder.loadTexts: wwpLeosVlanTagMemberTable.setStatus('current')
wwpLeosVlanTagMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberPortId"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberTagId"))
if mibBuilder.loadTexts: wwpLeosVlanTagMemberEntry.setStatus('current')
wwpLeosVlanMemberPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanMemberPortId.setStatus('current')
wwpLeosVlanMemberTagId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 2), VlanTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanMemberTagId.setStatus('current')
wwpLeosVlanMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanMemberStatus.setStatus('current')
wwpLeosVlanCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6), )
if mibBuilder.loadTexts: wwpLeosVlanCircuitTable.setStatus('deprecated')
wwpLeosVlanCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"))
if mibBuilder.loadTexts: wwpLeosVlanCircuitEntry.setStatus('deprecated')
wwpLeosCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosCircuitIndex.setStatus('deprecated')
wwpLeosCircuitVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitVlanId.setStatus('deprecated')
wwpLeosCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("mpls", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitType.setStatus('deprecated')
wwpLeosCircuitName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitName.setStatus('deprecated')
wwpLeosCircuitPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitPriority.setStatus('deprecated')
wwpLeosCircuitDataTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitDataTunnelState.setStatus('deprecated')
wwpLeosCircuitCtrlProtocolTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosCircuitCtrlProtocolTunnelState.setStatus('deprecated')
wwpLeosCircuitNumEndPoints = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosCircuitNumEndPoints.setStatus('deprecated')
wwpLeosCircuitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosCircuitStatus.setStatus('deprecated')
wwpLeosVlanCircuitPortExclusiveTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7), )
if mibBuilder.loadTexts: wwpLeosVlanCircuitPortExclusiveTable.setStatus('deprecated')
wwpLeosVlanCircuitPortExclusiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosPortId"))
if mibBuilder.loadTexts: wwpLeosVlanCircuitPortExclusiveEntry.setStatus('deprecated')
wwpLeosPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPortId.setStatus('deprecated')
wwpLeosPortExclusiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosPortExclusiveStatus.setStatus('deprecated')
wwpLeosVlanCircuitCtrlProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8), )
if mibBuilder.loadTexts: wwpLeosVlanCircuitCtrlProtocolTable.setStatus('deprecated')
wwpLeosVlanCircuitCtrlProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanl2ProtocolNum"))
if mibBuilder.loadTexts: wwpLeosVlanCircuitCtrlProtocolEntry.setStatus('deprecated')
wwpLeosVlanl2ProtocolNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("l28021x", 1), ("rstp", 2), ("ciscoCdp", 3), ("ciscoDtp", 4), ("ciscoPagp", 5), ("ciscoPvst", 6), ("ciscoUplinkFast", 7), ("ciscoUdlp", 8), ("ciscoVtp", 9), ("gvrp", 10), ("lacp", 11), ("lacpMarker", 12), ("lldp", 13), ("oam", 14), ("vlanBridge", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2ProtocolNum.setStatus('deprecated')
wwpLeosVlanl2Type = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("peer", 2), ("tunnel", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanl2Type.setStatus('deprecated')
wwpLeosVlanCircuitStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9))
wwpLeosVlanl2AllRxPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllRxPkts.setStatus('deprecated')
wwpLeosVlanl2AllTunneledPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllTunneledPkts.setStatus('deprecated')
wwpLeosVlanl2AllPeerPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllPeerPkts.setStatus('deprecated')
wwpLeosVlanl2AllDiscardedPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllDiscardedPkts.setStatus('deprecated')
wwpLeosVlanl2AllDecodedPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllDecodedPkts.setStatus('deprecated')
wwpLeosVlanl2AllDecodedFailures = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllDecodedFailures.setStatus('deprecated')
wwpLeosVlanl2AllTunneledSubcriberPortPkts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2AllTunneledSubcriberPortPkts.setStatus('deprecated')
wwpLeosVlanCircuitProtocolStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10), )
if mibBuilder.loadTexts: wwpLeosVlanCircuitProtocolStatsTable.setStatus('deprecated')
wwpLeosVlanCircuitProtocolStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanl2ProtocolNum"))
if mibBuilder.loadTexts: wwpLeosVlanCircuitProtocolStatsEntry.setStatus('deprecated')
wwpLeosVlanl2RxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2RxPkts.setStatus('deprecated')
wwpLeosVlanl2TunneledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2TunneledPkts.setStatus('deprecated')
wwpLeosVlanl2PeerPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2PeerPkts.setStatus('deprecated')
wwpLeosVlanl2DiscardedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2DiscardedPkts.setStatus('deprecated')
wwpLeosVlanl2DecodedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2DecodedPkts.setStatus('deprecated')
wwpLeosVlanl2DecodedFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2DecodedFailures.setStatus('deprecated')
wwpLeosVlanl2TunneledSubcriberPortPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanl2TunneledSubcriberPortPkts.setStatus('deprecated')
wwpLeosVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11), )
if mibBuilder.loadTexts: wwpLeosVlanStatsTable.setStatus('current')
wwpLeosVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanStatsVlanId"))
if mibBuilder.loadTexts: wwpLeosVlanStatsEntry.setStatus('current')
wwpLeosVlanStatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 1), VlanTag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanStatsVlanId.setStatus('current')
wwpLeosVlanStatsCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanStatsCreateTime.setStatus('current')
wwpLeosVlanStatsUniOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanStatsUniOctets.setStatus('current')
wwpLeosVlanStatsUniPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanStatsUniPkts.setStatus('current')
wwpLeosVlanStatsNonUniOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanStatsNonUniOctets.setStatus('current')
wwpLeosVlanStatsNonUniPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanStatsNonUniPkts.setStatus('current')
wwpLeosVlanStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanStatsStatus.setStatus('current')
wwpLeosVlanStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanStatsClear.setStatus('current')
wwpLeosVlanStatsPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanStatsPortId.setStatus('current')
wwpLeosVlanTotalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12), )
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsTable.setStatus('current')
wwpLeosVlanTotalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTotalStatsVlanId"))
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsEntry.setStatus('current')
wwpLeosVlanTotalStatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 1), VlanTag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsVlanId.setStatus('current')
wwpLeosVlanTotalStatsCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsCreateTime.setStatus('current')
wwpLeosVlanTotalStatsUniOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsUniOctets.setStatus('current')
wwpLeosVlanTotalStatsUniPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsUniPkts.setStatus('current')
wwpLeosVlanTotalStatsNonUniOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsNonUniOctets.setStatus('current')
wwpLeosVlanTotalStatsNonUniPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsNonUniPkts.setStatus('current')
wwpLeosVlanTotalStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsStatus.setStatus('current')
wwpLeosVlanTotalStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsClear.setStatus('current')
wwpLeosVlanTotalStatsPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanTotalStatsPortId.setStatus('current')
wwpLeosVlanTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13), )
if mibBuilder.loadTexts: wwpLeosVlanTranslationTable.setStatus('current')
wwpLeosVlanTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTranslationPgId"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTranslationFrameVid"))
if mibBuilder.loadTexts: wwpLeosVlanTranslationEntry.setStatus('current')
wwpLeosVlanTranslationPgId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: wwpLeosVlanTranslationPgId.setStatus('current')
wwpLeosVlanTranslationFrameVid = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 2), VlanTag())
if mibBuilder.loadTexts: wwpLeosVlanTranslationFrameVid.setStatus('current')
wwpLeosVlanTranslationVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 3), VlanTag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanTranslationVlanId.setStatus('current')
wwpLeosVlanTranslationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosVlanTranslationStatus.setStatus('current')
wwpLeosVlanEPRTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1), )
if mibBuilder.loadTexts: wwpLeosVlanEPRTable.setStatus('current')
wwpLeosVlanEPREntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"))
if mibBuilder.loadTexts: wwpLeosVlanEPREntry.setStatus('current')
wwpLeosVlanEPRState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanEPRState.setStatus('current')
wwpLeosVlanEPRGrpMemTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2), )
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpMemTable.setStatus('current')
wwpLeosVlanEPRGrpMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberPortId"), (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberTagId"))
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpMemEntry.setStatus('current')
wwpLeosVlanEPRGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("groupA", 1), ("groupB", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpName.setStatus('current')
wwpLeosVlanEPRGrpAccessTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3), )
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpAccessTable.setStatus('current')
wwpLeosVlanEPRGrpAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1), ).setIndexNames((0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"))
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpAccessEntry.setStatus('current')
wwpLeosVlanEPRGrpAAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("groupA", 1), ("groupB", 2), ("groupAB", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpAAccess.setStatus('current')
wwpLeosVlanEPRGrpBAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("groupA", 1), ("groupB", 2), ("groupAB", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosVlanEPRGrpBAccess.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-VLAN-TAG-MIB", wwpLeosVlanTranslationEntry=wwpLeosVlanTranslationEntry, wwpLeosPortId=wwpLeosPortId, wwpLeosCircuitName=wwpLeosCircuitName, wwpLeosVlanTranslationTable=wwpLeosVlanTranslationTable, wwpLeosVlanTotalStatsUniOctets=wwpLeosVlanTotalStatsUniOctets, wwpLeosVlanTranslationPgId=wwpLeosVlanTranslationPgId, wwpLeosVlanTranslationVlanId=wwpLeosVlanTranslationVlanId, wwpLeosCircuitStatus=wwpLeosCircuitStatus, wwpLeosPortExclusiveStatus=wwpLeosPortExclusiveStatus, wwpLeosVlanl2TunneledSubcriberPortPkts=wwpLeosVlanl2TunneledSubcriberPortPkts, wwpLeosVlanl2AllTunneledPkts=wwpLeosVlanl2AllTunneledPkts, wwpLeosVlanl2Type=wwpLeosVlanl2Type, wwpLeosVlanName=wwpLeosVlanName, wwpLeosVlanTagMemberEntry=wwpLeosVlanTagMemberEntry, wwpLeosVlanCircuitProtocolStatsTable=wwpLeosVlanCircuitProtocolStatsTable, wwpLeosVlanMemberTagId=wwpLeosVlanMemberTagId, wwpLeosVlanTotalStatsPortId=wwpLeosVlanTotalStatsPortId, wwpLeosVlanMIBNotifications=wwpLeosVlanMIBNotifications, wwpLeosCircuitType=wwpLeosCircuitType, wwpLeosVlanStatsTable=wwpLeosVlanStatsTable, wwpLeosVlanMIBConformance=wwpLeosVlanMIBConformance, wwpLeosVlanEPRGrpBAccess=wwpLeosVlanEPRGrpBAccess, wwpLeosVlanStatsEntry=wwpLeosVlanStatsEntry, wwpLeosVlanTotalStatsNonUniOctets=wwpLeosVlanTotalStatsNonUniOctets, wwpLeosVlanCircuitPortExclusiveTable=wwpLeosVlanCircuitPortExclusiveTable, wwpLeosVlanCircuitCtrlProtocolTable=wwpLeosVlanCircuitCtrlProtocolTable, wwpLeosNumVlans=wwpLeosNumVlans, wwpLeosVlanStatsUniOctets=wwpLeosVlanStatsUniOctets, wwpLeosVlanCircuitTable=wwpLeosVlanCircuitTable, VlanId=VlanId, wwpLeosVlanTotalStatsUniPkts=wwpLeosVlanTotalStatsUniPkts, wwpLeosVlanCircuitProtocolStatsEntry=wwpLeosVlanCircuitProtocolStatsEntry, VlanTag=VlanTag, wwpLeosVlanStatsStatus=wwpLeosVlanStatsStatus, wwpLeosCircuitPriority=wwpLeosCircuitPriority, wwpLeosVlanStatsUniPkts=wwpLeosVlanStatsUniPkts, wwpLeosMaxVlans=wwpLeosMaxVlans, wwpLeosVlanEPREntry=wwpLeosVlanEPREntry, wwpLeosVlanl2DiscardedPkts=wwpLeosVlanl2DiscardedPkts, wwpLeosVlanStatsPortId=wwpLeosVlanStatsPortId, wwpLeosVlanl2AllTunneledSubcriberPortPkts=wwpLeosVlanl2AllTunneledSubcriberPortPkts, wwpLeosVlanl2AllDecodedFailures=wwpLeosVlanl2AllDecodedFailures, wwpLeosVlanId=wwpLeosVlanId, wwpLeosVlanEPRGrpAccessTable=wwpLeosVlanEPRGrpAccessTable, wwpLeosVlanMacLrnState=wwpLeosVlanMacLrnState, wwpLeosVlanStatsClear=wwpLeosVlanStatsClear, wwpLeosVlanTranslationVlan=wwpLeosVlanTranslationVlan, wwpLeosVlanStatsVlanId=wwpLeosVlanStatsVlanId, wwpLeosVlanl2AllDecodedPkts=wwpLeosVlanl2AllDecodedPkts, wwpLeosVlanEgressTpid=wwpLeosVlanEgressTpid, wwpLeosVlanTotalStatsEntry=wwpLeosVlanTotalStatsEntry, wwpLeosVlanStatsNonUniPkts=wwpLeosVlanStatsNonUniPkts, wwpLeosVlanTable=wwpLeosVlanTable, wwpLeosVlanStatus=wwpLeosVlanStatus, wwpLeosVlanTagMemberTable=wwpLeosVlanTagMemberTable, wwpLeosCircuitDataTunnelState=wwpLeosCircuitDataTunnelState, wwpLeosVlanl2ProtocolNum=wwpLeosVlanl2ProtocolNum, wwpLeosVlanCircuitStats=wwpLeosVlanCircuitStats, wwpLeosVlanEPRGrpMemEntry=wwpLeosVlanEPRGrpMemEntry, wwpLeosVlanMIB=wwpLeosVlanMIB, wwpLeosVlanMIBCompliances=wwpLeosVlanMIBCompliances, wwpLeosVlanMemberPortId=wwpLeosVlanMemberPortId, wwpLeosVlanl2AllRxPkts=wwpLeosVlanl2AllRxPkts, wwpLeosVlanl2AllPeerPkts=wwpLeosVlanl2AllPeerPkts, wwpLeosVlanCircuitEntry=wwpLeosVlanCircuitEntry, wwpLeosVlanTotalStatsClear=wwpLeosVlanTotalStatsClear, wwpLeosCircuitCtrlProtocolTunnelState=wwpLeosCircuitCtrlProtocolTunnelState, wwpLeosVlanl2TunneledPkts=wwpLeosVlanl2TunneledPkts, wwpLeosVlanl2DecodedFailures=wwpLeosVlanl2DecodedFailures, wwpLeosCircuitIndex=wwpLeosCircuitIndex, wwpLeosVlanTranslationFrameVid=wwpLeosVlanTranslationFrameVid, wwpLeosVlanMacLrnOperState=wwpLeosVlanMacLrnOperState, wwpLeosVlanl2RxPkts=wwpLeosVlanl2RxPkts, PYSNMP_MODULE_ID=wwpLeosVlanMIB, wwpLeosVlanl2AllDiscardedPkts=wwpLeosVlanl2AllDiscardedPkts, wwpLeosVlanMIBGroups=wwpLeosVlanMIBGroups, wwpLeosVlanTranslationStatus=wwpLeosVlanTranslationStatus, wwpLeosVlanl2DecodedPkts=wwpLeosVlanl2DecodedPkts, wwpLeosVlanEPRTable=wwpLeosVlanEPRTable, wwpLeosVlanEPR=wwpLeosVlanEPR, wwpLeosVlanMIBNotificationPrefix=wwpLeosVlanMIBNotificationPrefix, wwpLeosCircuitVlanId=wwpLeosCircuitVlanId, wwpLeosVlanMIBObjects=wwpLeosVlanMIBObjects, wwpLeosVlanMemberStatus=wwpLeosVlanMemberStatus, wwpLeosVlanStatsCreateTime=wwpLeosVlanStatsCreateTime, wwpLeosVlanEPRGrpMemTable=wwpLeosVlanEPRGrpMemTable, wwpLeosVlanTotalStatsNonUniPkts=wwpLeosVlanTotalStatsNonUniPkts, wwpLeosVlanl2PeerPkts=wwpLeosVlanl2PeerPkts, wwpLeosCircuitNumEndPoints=wwpLeosCircuitNumEndPoints, wwpLeosVlanEntry=wwpLeosVlanEntry, wwpLeosVlanCircuitCtrlProtocolEntry=wwpLeosVlanCircuitCtrlProtocolEntry, wwpLeosVlanTotalStatsStatus=wwpLeosVlanTotalStatsStatus, wwpLeosVlanEPRGrpAAccess=wwpLeosVlanEPRGrpAAccess, wwpLeosVlanEPRState=wwpLeosVlanEPRState, wwpLeosVlanEPRGrpAccessEntry=wwpLeosVlanEPRGrpAccessEntry, wwpLeosVlanTotalStatsCreateTime=wwpLeosVlanTotalStatsCreateTime, wwpLeosMaxSupportedVlanTagId=wwpLeosMaxSupportedVlanTagId, wwpLeosVlanTotalStatsVlanId=wwpLeosVlanTotalStatsVlanId, wwpLeosVlanStatsNonUniOctets=wwpLeosVlanStatsNonUniOctets, wwpLeosVlanTotalStatsTable=wwpLeosVlanTotalStatsTable, wwpLeosVlanCircuitPortExclusiveEntry=wwpLeosVlanCircuitPortExclusiveEntry, wwpLeosVlan=wwpLeosVlan, wwpLeosVlanEPRGrpName=wwpLeosVlanEPRGrpName)