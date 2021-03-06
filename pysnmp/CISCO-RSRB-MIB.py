#
# PySNMP MIB module CISCO-RSRB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RSRB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, TimeTicks, Bits, Unsigned32, MibIdentifier, NotificationType, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "TimeTicks", "Bits", "Unsigned32", "MibIdentifier", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32")
DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
ciscoRsrbMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 29))
ciscoRsrbMIB.setRevisions(('1995-08-21 00:00',))
if mibBuilder.loadTexts: ciscoRsrbMIB.setLastUpdated('9508210000Z')
if mibBuilder.loadTexts: ciscoRsrbMIB.setOrganization('Cisco Systems, Inc.')
rsrbObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 1))
rsrbVirtualRings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1))
rsrbRemotePeers = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2))
rsrbPhysicalRings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3))
rsrbVirtRingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1), )
if mibBuilder.loadTexts: rsrbVirtRingTable.setStatus('current')
rsrbVirtRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"))
if mibBuilder.loadTexts: rsrbVirtRingEntry.setStatus('current')
rsrbVirtRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rsrbVirtRingIndex.setStatus('current')
rsrbVirtRingIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbVirtRingIPAddr.setStatus('current')
rsrbVirtRingMaxTcpQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbVirtRingMaxTcpQSize.setStatus('current')
rsrbRemotePeerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1), )
if mibBuilder.loadTexts: rsrbRemotePeerTable.setStatus('current')
rsrbRemotePeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"), (0, "CISCO-RSRB-MIB", "rsrbRemotePeerIndex"))
if mibBuilder.loadTexts: rsrbRemotePeerEntry.setStatus('current')
rsrbRemotePeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rsrbRemotePeerIndex.setStatus('current')
rsrbRemotePeerEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("tcp", 1), ("serial", 2), ("lan", 3), ("fst", 4), ("frameRelay", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerEncapsulation.setStatus('current')
rsrbRemotePeerIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerIPAddr.setStatus('current')
rsrbRemotePeerLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerLocalIfIndex.setStatus('current')
rsrbRemotePeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("dead", 1), ("closed", 2), ("opening", 3), ("openWaitXport", 4), ("waitRemoteRsp", 5), ("remoteResponded", 6), ("remoteOpened", 7), ("draining", 8), ("connected", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerState.setStatus('current')
rsrbRemotePeerPacketsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerPacketsRx.setStatus('current')
rsrbRemotePeerPacketsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerPacketsTx.setStatus('current')
rsrbRemotePeerBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerBytesRx.setStatus('current')
rsrbRemotePeerBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerBytesTx.setStatus('current')
rsrbRemotePeerExplorersRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerExplorersRx.setStatus('current')
rsrbRemotePeerTcpQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerTcpQueue.setStatus('current')
rsrbRemotePeerDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerDrops.setStatus('current')
rsrbRemotePeerLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerLocalAck.setStatus('current')
rsrbRemotePeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRemotePeerVersion.setStatus('current')
rsrbRingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1), )
if mibBuilder.loadTexts: rsrbRingTable.setStatus('current')
rsrbRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-RSRB-MIB", "rsrbVirtRingIndex"), (0, "CISCO-RSRB-MIB", "rsrbRingIndex"))
if mibBuilder.loadTexts: rsrbRingEntry.setStatus('current')
rsrbRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rsrbRingIndex.setStatus('current')
rsrbRingBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingBridge.setStatus('current')
rsrbRingLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingLocal.setStatus('current')
rsrbRingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("sdllc", 3), ("qllc", 4), ("virtual", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingType.setStatus('current')
rsrbRingMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingMacAddr.setStatus('current')
rsrbRingLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingLocalIfIndex.setStatus('current')
rsrbRingRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingRemoteIpAddress.setStatus('current')
rsrbRingNbrPacketsFwd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 29, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsrbRingNbrPacketsFwd.setStatus('current')
rsrbNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 2))
rsrbNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 2, 0))
rsrbPeerStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 29, 2, 0, 1)).setObjects(("CISCO-RSRB-MIB", "rsrbRemotePeerState"))
if mibBuilder.loadTexts: rsrbPeerStateChangeNotification.setStatus('current')
rsrbMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 3))
rsrbMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 1))
rsrbMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2))
rsrbMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 1, 1)).setObjects(("CISCO-RSRB-MIB", "rsrbVirtRingGroup"), ("CISCO-RSRB-MIB", "rsrbRemotePeerGroup"), ("CISCO-RSRB-MIB", "rsrbRingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsrbMibCompliance = rsrbMibCompliance.setStatus('current')
rsrbVirtRingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 1)).setObjects(("CISCO-RSRB-MIB", "rsrbVirtRingIPAddr"), ("CISCO-RSRB-MIB", "rsrbVirtRingMaxTcpQSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsrbVirtRingGroup = rsrbVirtRingGroup.setStatus('current')
rsrbRemotePeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 2)).setObjects(("CISCO-RSRB-MIB", "rsrbRemotePeerEncapsulation"), ("CISCO-RSRB-MIB", "rsrbRemotePeerIPAddr"), ("CISCO-RSRB-MIB", "rsrbRemotePeerLocalIfIndex"), ("CISCO-RSRB-MIB", "rsrbRemotePeerState"), ("CISCO-RSRB-MIB", "rsrbRemotePeerPacketsRx"), ("CISCO-RSRB-MIB", "rsrbRemotePeerPacketsTx"), ("CISCO-RSRB-MIB", "rsrbRemotePeerBytesRx"), ("CISCO-RSRB-MIB", "rsrbRemotePeerBytesTx"), ("CISCO-RSRB-MIB", "rsrbRemotePeerExplorersRx"), ("CISCO-RSRB-MIB", "rsrbRemotePeerTcpQueue"), ("CISCO-RSRB-MIB", "rsrbRemotePeerDrops"), ("CISCO-RSRB-MIB", "rsrbRemotePeerLocalAck"), ("CISCO-RSRB-MIB", "rsrbRemotePeerVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsrbRemotePeerGroup = rsrbRemotePeerGroup.setStatus('current')
rsrbRingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 29, 3, 2, 3)).setObjects(("CISCO-RSRB-MIB", "rsrbRingBridge"), ("CISCO-RSRB-MIB", "rsrbRingLocal"), ("CISCO-RSRB-MIB", "rsrbRingType"), ("CISCO-RSRB-MIB", "rsrbRingMacAddr"), ("CISCO-RSRB-MIB", "rsrbRingLocalIfIndex"), ("CISCO-RSRB-MIB", "rsrbRingRemoteIpAddress"), ("CISCO-RSRB-MIB", "rsrbRingNbrPacketsFwd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsrbRingGroup = rsrbRingGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-RSRB-MIB", rsrbMibGroups=rsrbMibGroups, rsrbRingTable=rsrbRingTable, ciscoRsrbMIB=ciscoRsrbMIB, rsrbMibCompliance=rsrbMibCompliance, rsrbRemotePeerIPAddr=rsrbRemotePeerIPAddr, rsrbObjects=rsrbObjects, rsrbVirtualRings=rsrbVirtualRings, rsrbRingLocal=rsrbRingLocal, rsrbRingType=rsrbRingType, PYSNMP_MODULE_ID=ciscoRsrbMIB, rsrbRemotePeerLocalAck=rsrbRemotePeerLocalAck, rsrbVirtRingTable=rsrbVirtRingTable, rsrbNotifications=rsrbNotifications, rsrbRemotePeerPacketsRx=rsrbRemotePeerPacketsRx, rsrbRingRemoteIpAddress=rsrbRingRemoteIpAddress, rsrbRingEntry=rsrbRingEntry, rsrbRemotePeers=rsrbRemotePeers, rsrbRingNbrPacketsFwd=rsrbRingNbrPacketsFwd, rsrbRemotePeerExplorersRx=rsrbRemotePeerExplorersRx, rsrbMibCompliances=rsrbMibCompliances, rsrbRemotePeerLocalIfIndex=rsrbRemotePeerLocalIfIndex, rsrbMibConformance=rsrbMibConformance, rsrbRemotePeerDrops=rsrbRemotePeerDrops, rsrbRingLocalIfIndex=rsrbRingLocalIfIndex, rsrbRingBridge=rsrbRingBridge, rsrbNotificationPrefix=rsrbNotificationPrefix, rsrbPeerStateChangeNotification=rsrbPeerStateChangeNotification, rsrbRemotePeerState=rsrbRemotePeerState, rsrbRemotePeerEncapsulation=rsrbRemotePeerEncapsulation, rsrbRemotePeerIndex=rsrbRemotePeerIndex, rsrbRemotePeerBytesTx=rsrbRemotePeerBytesTx, rsrbRemotePeerGroup=rsrbRemotePeerGroup, rsrbRemotePeerBytesRx=rsrbRemotePeerBytesRx, rsrbVirtRingGroup=rsrbVirtRingGroup, rsrbVirtRingMaxTcpQSize=rsrbVirtRingMaxTcpQSize, rsrbPhysicalRings=rsrbPhysicalRings, rsrbVirtRingIndex=rsrbVirtRingIndex, rsrbRemotePeerEntry=rsrbRemotePeerEntry, rsrbRemotePeerTable=rsrbRemotePeerTable, rsrbRemotePeerVersion=rsrbRemotePeerVersion, rsrbRingMacAddr=rsrbRingMacAddr, rsrbVirtRingEntry=rsrbVirtRingEntry, rsrbRingIndex=rsrbRingIndex, rsrbRingGroup=rsrbRingGroup, rsrbRemotePeerTcpQueue=rsrbRemotePeerTcpQueue, rsrbRemotePeerPacketsTx=rsrbRemotePeerPacketsTx, rsrbVirtRingIPAddr=rsrbVirtRingIPAddr)
