#
# PySNMP MIB module HP-SN-APPLETALK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-APPLETALK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:36:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ATNetworkNumber, ATName, DdpNodeAddress = mibBuilder.importSymbols("APPLETALK-MIB", "ATNetworkNumber", "ATName", "DdpNodeAddress")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
Action, RtrStatus, PortIndex, RowSts, ClearStatus = mibBuilder.importSymbols("HP-SN-IP-MIB", "Action", "RtrStatus", "PortIndex", "RowSts", "ClearStatus")
snAppleTalk, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snAppleTalk")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, NotificationType, Counter64, Gauge32, Integer32, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, IpAddress, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "Counter64", "Gauge32", "Integer32", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snRtATGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1))
snRtATRoutingEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 1), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATRoutingEnable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATRoutingEnable.setDescription('Enable/disable AppleTalk routing function on this box.')
snRtATClearArpCache = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 2), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATClearArpCache.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATClearArpCache.setDescription('clear(1) will clear AppleTalk arp cache table.')
snRtATClearFwdCache = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 3), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATClearFwdCache.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATClearFwdCache.setDescription('clear(1) will clear AppleTalk forward cache table.')
snRtATClearRoute = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 4), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATClearRoute.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATClearRoute.setDescription('clear(1) will clear AppleTalk route table.')
snRtATClearTrafficCounters = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 5), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATClearTrafficCounters.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATClearTrafficCounters.setDescription('clear(1) will clear AppleTalk network statistics counters.')
snRtATArpRetransmitCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATArpRetransmitCount.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATArpRetransmitCount.setDescription('The number of AppleTalk ARP request retransmits if the first request timeouts.')
snRtATArpRetransmitInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATArpRetransmitInterval.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATArpRetransmitInterval.setDescription('The waiting time interval for an AppleTalk ARP response before retransmission of an ARP request. Each unit value is one second.')
snRtATGleanPacketsEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 8), RtrStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATGleanPacketsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATGleanPacketsEnable.setDescription('Enable/disable AppleTalk glean packets function on this box.')
snRtATRtmpUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATRtmpUpdateInterval.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATRtmpUpdateInterval.setDescription('The periodic time interval to transmit a RTMP update. Each unit value is one second.')
snRtATZipQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATZipQueryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZipQueryInterval.setDescription('The periodic time interval to transmit a ZIP query. Each unit value is one second.')
snRtATInRtmpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInRtmpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInRtmpPkts.setDescription('The total number of RTMP packets received by this entity.')
snRtATOutRtmpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutRtmpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutRtmpPkts.setDescription('The total number of RTMP packets which were transmitted from this entity.')
snRtATFilteredRtmpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFilteredRtmpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFilteredRtmpPkts.setDescription('The total number of RTMP packets which were filtered by this entity.')
snRtATInZipPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInZipPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInZipPkts.setDescription('The total number of ZIP packets received by this entity.')
snRtATOutZipPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutZipPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutZipPkts.setDescription('The total number of ZIP packets which were transmitted from this entity.')
snRtATInZipGZLPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInZipGZLPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInZipGZLPkts.setDescription('The total number of ZIP get zone list packets received by this entity.')
snRtATOutZipGZLPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutZipGZLPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutZipGZLPkts.setDescription('The total number of ZIP get zone list packets which were transmitted from this entity.')
snRtATInZipNetInfoPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInZipNetInfoPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInZipNetInfoPkts.setDescription('The total number of ZIP network information packets received by this entity.')
snRtATOutZipNetInfoPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutZipNetInfoPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutZipNetInfoPkts.setDescription('The total number of ZIP network information packets which were transmitted from this entity.')
snRtATInDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInDdpPkts.setDescription('The total number of DDP datagrams received by this entity.')
snRtATOutDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutDdpPkts.setDescription('The total number of DDP datagrams which were transmitted from this entity.')
snRtATForwardedDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATForwardedDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATForwardedDdpPkts.setDescription('The number of input DDP datagrams for which this entity was not their final DDP destination, as a result of which an attempt was made to find a route to forward them to that final destination.')
snRtATInDeliveredDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInDeliveredDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInDeliveredDdpPkts.setDescription('The total number of input DDP datagrams for which this entity was their final DDP destination.')
snRtATDroppedNoRouteDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATDroppedNoRouteDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATDroppedNoRouteDdpPkts.setDescription('The total number of DDP datagrams dropped because a route could not be found to their final destination.')
snRtATDroppedBadHopCountsDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATDroppedBadHopCountsDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATDroppedBadHopCountsDdpPkts.setDescription('The total number of input DDP datagrams dropped because this entity was not their final destination and their hop count would exceed 15.')
snRtATDroppedOtherReasonsDdpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATDroppedOtherReasonsDdpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATDroppedOtherReasonsDdpPkts.setDescription('The total number of DDP datagrams dropped because of other reasons, e.g. run out of resouces.')
snRtATInAarpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATInAarpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATInAarpPkts.setDescription('The total number of AppleTalk ARP packets received by this entity.')
snRtATOutAarpPkts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATOutAarpPkts.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATOutAarpPkts.setDescription('The total number of AppleTalk ARP packets which were transmitted from this entity.')
snRtATSocketPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 2), )
if mibBuilder.loadTexts: snRtATSocketPriorityTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATSocketPriorityTable.setDescription('AppleTalk socket priority table.')
snRtATSocketPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 2, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATSocketPrioritySocket"))
if mibBuilder.loadTexts: snRtATSocketPriorityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATSocketPriorityEntry.setDescription('An entry in the AppleTalk socket priority table.')
snRtATSocketPrioritySocket = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATSocketPrioritySocket.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATSocketPrioritySocket.setDescription('Socket number for a socket priority entry.')
snRtATSocketPriorityPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("level0", 0), ("level1", 1), ("level2", 2), ("level3", 3), ("level4", 4), ("level5", 5), ("level6", 6), ("level7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATSocketPriorityPriority.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATSocketPriorityPriority.setDescription('The Standalone router Priority level applies to a socket number: low(0) -- low prority high(1) -- high prority. The BigIron Priority levels applies to a socket number are: level0(0), level1(1), level2(2), level3(3), level4(4), level5(5), level6(6), level7(7) ')
snRtATPortZoneFilterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3), )
if mibBuilder.loadTexts: snRtATPortZoneFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterTable.setDescription('AppleTalk interface zone filter table.')
snRtATPortZoneFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATPortZoneFilterPortIndex"), (0, "HP-SN-APPLETALK-MIB", "snRtATPortZoneFilterZone"))
if mibBuilder.loadTexts: snRtATPortZoneFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterEntry.setDescription('An entry in the AppleTalk interface zone filter table.')
snRtATPortZoneFilterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortZoneFilterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterPortIndex.setDescription('The port index for a zone filter entry.')
snRtATPortZoneFilterZone = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1, 2), ATName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortZoneFilterZone.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterZone.setDescription('The zone name granted for this filter.')
snRtATPortZoneFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1, 3), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATPortZoneFilterAction.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterAction.setDescription('Action to take if the AppleTalk packet match with this filter.')
snRtATPortZoneFilterRtmpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1, 4), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATPortZoneFilterRtmpEnable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterRtmpEnable.setDescription('Enable/disable RTMP filtering.')
snRtATPortZoneFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 3, 1, 5), RowSts()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATPortZoneFilterRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortZoneFilterRowStatus.setDescription('To create or delete a zone filter entry.')
snRtATPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4), )
if mibBuilder.loadTexts: snRtATPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortTable.setDescription('AppleTalk port table.')
snRtATPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATPortIndex"))
if mibBuilder.loadTexts: snRtATPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortEntry.setDescription('An entry in the AppleTalk port table.')
snRtATPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortIndex.setDescription('The port index for port table entry.')
snRtATPortArpAge = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATPortArpAge.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortArpAge.setDescription("The time in minutes an ARP entry can be valid without relearning. 0 - Don't age.")
snRtATPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortState.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortState.setDescription('The up and down state of this port.')
snRtATPortSeedRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("seedRouter", 2), ("nonSeedRouter", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortSeedRouter.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortSeedRouter.setDescription('This port was configured to seed or non-seed router.')
snRtATPortOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("seedRouter", 2), ("nonSeedRouter", 3), ("notOperational", 4), ("routingDisabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATPortOperationMode.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATPortOperationMode.setDescription('The operation mode of this port.')
snRtATFwdCacheTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5), )
if mibBuilder.loadTexts: snRtATFwdCacheTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheTable.setDescription('AppleTalk forwarding cache table.')
snRtATFwdCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATFwdCacheIndex"))
if mibBuilder.loadTexts: snRtATFwdCacheEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheEntry.setDescription('An entry in the AppleTalk forwarding cache table.')
snRtATFwdCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheIndex.setDescription('The table index for an AppleTalk forwarding cache table entry.')
snRtATFwdCacheNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 2), DdpNodeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheNetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheNetAddr.setDescription('The AppleTalk network address of a station.')
snRtATFwdCacheMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheMacAddr.setDescription('The Mac address of an AppleTalk station.')
snRtATFwdCacheNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 4), DdpNodeAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheNextHop.setDescription('The next hop router network address.')
snRtATFwdCacheOutgoingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheOutgoingPort.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheOutgoingPort.setDescription('The outgoing port of which packets will forward to. Return port value of zero to indicate no outgoing port associated to this entry.')
snRtATFwdCacheType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("permanent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheType.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheType.setDescription("The 'dynamic' or 'permanent' type for an AppleTalk forwarding cache table entry.")
snRtATFwdCacheAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("forward", 2), ("forUs", 3), ("waitForArp", 4), ("dropPacket", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheAction.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheAction.setDescription('The action to take.')
snRtATFwdCacheVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATFwdCacheVLanId.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATFwdCacheVLanId.setDescription('The VLAN ID for an AppleTalk forwarding cache table entry. Return VLAN ID value of zero to indicate no VLAN associated to this entry.')
snRtATZoneTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6), )
if mibBuilder.loadTexts: snRtATZoneTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneTable.setDescription('AppleTalk zone table.')
snRtATZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATZoneIndex"))
if mibBuilder.loadTexts: snRtATZoneEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneEntry.setDescription('An entry in the AppleTalk zone table.')
snRtATZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATZoneIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneIndex.setDescription('The table index for an AppleTalk zone table entry.')
snRtATZoneNetStart = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6, 1, 2), ATNetworkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATZoneNetStart.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneNetStart.setDescription('The first AppleTalk network address in the range of this zone name.')
snRtATZoneNetEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6, 1, 3), ATNetworkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATZoneNetEnd.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneNetEnd.setDescription('The last AppleTalk network address in the range of this zone name.')
snRtATZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 6, 1, 4), ATName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATZoneName.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATZoneName.setDescription('The zone name.')
snRtATAddZoneFilterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 7), )
if mibBuilder.loadTexts: snRtATAddZoneFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATAddZoneFilterTable.setDescription('AppleTalk additional zone filter table. Additional zones are those zones that do not match any zones defined in the zone filter table.')
snRtATAddZoneFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 7, 1), ).setIndexNames((0, "HP-SN-APPLETALK-MIB", "snRtATAddZoneFilterPortIndex"))
if mibBuilder.loadTexts: snRtATAddZoneFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATAddZoneFilterEntry.setDescription('An entry in the AppleTalk additional zone filter table.')
snRtATAddZoneFilterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 7, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snRtATAddZoneFilterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATAddZoneFilterPortIndex.setDescription('The port index for additional zone filter table entry.')
snRtATAddZoneFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 7, 1, 2), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATAddZoneFilterAction.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATAddZoneFilterAction.setDescription('Action to take if no zone filter match.')
snRtATAddZoneFilterRtmpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10, 7, 1, 3), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snRtATAddZoneFilterRtmpEnable.setStatus('mandatory')
if mibBuilder.loadTexts: snRtATAddZoneFilterRtmpEnable.setDescription('Enable/disable RTMP filtering on additional zone.')
mibBuilder.exportSymbols("HP-SN-APPLETALK-MIB", snRtATFwdCacheNetAddr=snRtATFwdCacheNetAddr, snRtATFwdCacheOutgoingPort=snRtATFwdCacheOutgoingPort, snRtATAddZoneFilterTable=snRtATAddZoneFilterTable, snRtATClearTrafficCounters=snRtATClearTrafficCounters, snRtATArpRetransmitInterval=snRtATArpRetransmitInterval, snRtATForwardedDdpPkts=snRtATForwardedDdpPkts, snRtATOutAarpPkts=snRtATOutAarpPkts, snRtATClearRoute=snRtATClearRoute, snRtATPortZoneFilterRtmpEnable=snRtATPortZoneFilterRtmpEnable, snRtATFwdCacheType=snRtATFwdCacheType, snRtATInAarpPkts=snRtATInAarpPkts, snRtATClearFwdCache=snRtATClearFwdCache, snRtATZoneTable=snRtATZoneTable, snRtATZoneName=snRtATZoneName, snRtATFwdCacheTable=snRtATFwdCacheTable, snRtATPortZoneFilterRowStatus=snRtATPortZoneFilterRowStatus, snRtATFwdCacheAction=snRtATFwdCacheAction, snRtATZoneIndex=snRtATZoneIndex, snRtATZoneNetEnd=snRtATZoneNetEnd, snRtATPortZoneFilterAction=snRtATPortZoneFilterAction, snRtATFwdCacheEntry=snRtATFwdCacheEntry, snRtATInDeliveredDdpPkts=snRtATInDeliveredDdpPkts, snRtATPortZoneFilterPortIndex=snRtATPortZoneFilterPortIndex, snRtATOutZipNetInfoPkts=snRtATOutZipNetInfoPkts, snRtATGeneral=snRtATGeneral, snRtATFwdCacheNextHop=snRtATFwdCacheNextHop, snRtATOutZipPkts=snRtATOutZipPkts, snRtATPortArpAge=snRtATPortArpAge, snRtATFwdCacheVLanId=snRtATFwdCacheVLanId, snRtATRtmpUpdateInterval=snRtATRtmpUpdateInterval, snRtATFwdCacheMacAddr=snRtATFwdCacheMacAddr, snRtATDroppedBadHopCountsDdpPkts=snRtATDroppedBadHopCountsDdpPkts, snRtATInZipGZLPkts=snRtATInZipGZLPkts, snRtATInDdpPkts=snRtATInDdpPkts, snRtATPortTable=snRtATPortTable, snRtATPortOperationMode=snRtATPortOperationMode, snRtATFilteredRtmpPkts=snRtATFilteredRtmpPkts, snRtATOutZipGZLPkts=snRtATOutZipGZLPkts, snRtATInZipPkts=snRtATInZipPkts, snRtATPortSeedRouter=snRtATPortSeedRouter, snRtATSocketPriorityPriority=snRtATSocketPriorityPriority, snRtATPortEntry=snRtATPortEntry, snRtATSocketPriorityEntry=snRtATSocketPriorityEntry, snRtATAddZoneFilterAction=snRtATAddZoneFilterAction, snRtATSocketPrioritySocket=snRtATSocketPrioritySocket, snRtATClearArpCache=snRtATClearArpCache, snRtATAddZoneFilterRtmpEnable=snRtATAddZoneFilterRtmpEnable, snRtATGleanPacketsEnable=snRtATGleanPacketsEnable, snRtATOutDdpPkts=snRtATOutDdpPkts, snRtATPortZoneFilterZone=snRtATPortZoneFilterZone, snRtATArpRetransmitCount=snRtATArpRetransmitCount, snRtATInZipNetInfoPkts=snRtATInZipNetInfoPkts, snRtATAddZoneFilterEntry=snRtATAddZoneFilterEntry, snRtATSocketPriorityTable=snRtATSocketPriorityTable, snRtATZoneNetStart=snRtATZoneNetStart, snRtATPortZoneFilterTable=snRtATPortZoneFilterTable, snRtATInRtmpPkts=snRtATInRtmpPkts, snRtATPortZoneFilterEntry=snRtATPortZoneFilterEntry, snRtATRoutingEnable=snRtATRoutingEnable, snRtATDroppedOtherReasonsDdpPkts=snRtATDroppedOtherReasonsDdpPkts, snRtATZipQueryInterval=snRtATZipQueryInterval, snRtATFwdCacheIndex=snRtATFwdCacheIndex, snRtATPortState=snRtATPortState, snRtATZoneEntry=snRtATZoneEntry, snRtATPortIndex=snRtATPortIndex, snRtATDroppedNoRouteDdpPkts=snRtATDroppedNoRouteDdpPkts, snRtATOutRtmpPkts=snRtATOutRtmpPkts, snRtATAddZoneFilterPortIndex=snRtATAddZoneFilterPortIndex)
