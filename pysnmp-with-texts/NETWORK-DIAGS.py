#
# PySNMP MIB module NETWORK-DIAGS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-DIAGS
# Produced by pysmi-0.3.4 at Wed May  1 14:21:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
nwDiagnostics, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "nwDiagnostics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, ModuleIdentity, Integer32, IpAddress, Gauge32, ObjectIdentity, iso, Counter32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nwRevision = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1))
nwInternet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2))
nwIpPing = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1))
nwIpTraceRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2))
nwRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwRevisionLevel.setStatus('mandatory')
if mibBuilder.loadTexts: nwRevisionLevel.setDescription('This shows the current revision level of this mib.')
nwIpPingTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1), )
if mibBuilder.loadTexts: nwIpPingTable.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingTable.setDescription('This table allows outbound ping requests to be generated from the Cabletron device to a specified destination IP address. It is indexed by destination address and source address to allow multiple ping requests by different owner IP addresses.')
nwIpPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpPingDestination"), (0, "NETWORK-DIAGS", "nwIpPingOwner"))
if mibBuilder.loadTexts: nwIpPingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingEntry.setDescription('An IP Ping Table entry containing objects for a particular ping request.')
nwIpPingDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingDestination.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingDestination.setDescription('The IP address of the host/device to be pinged.')
nwIpPingOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingOwner.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingOwner.setDescription('The IP address of the client which created this ping request. A value of 0.0.0.0 indicates the request was made from the local console.')
nwIpPingType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2))).clone('other')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingType.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingType.setDescription('The administrative control of this ping request entry. This leaf is used to create a ping request entry.')
nwIpPingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("activate", 2), ("suspend", 3))).clone('activate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingAction.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingAction.setDescription('The action to be performed with this ping entry.')
nwIpPingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("other", 1), ("not-sent", 2), ("in-progress", 3), ("alive", 4), ("timeout", 5), ("bad-results", 6), ("failed", 7), ("net-unreach", 8), ("host-unreach", 9), ("proto-unreach", 10), ("port-unreach", 11), ("cant-frag", 12), ("sr-failed", 13), ("net-unknown", 14), ("host-unknown", 15), ("isolated", 16), ("no-net-comm", 17), ("no-host-comm", 18), ("no-net-tos", 19), ("no-host-tos", 20), ("source-quence", 21), ("ttl-exceeded", 22), ("frag-exceeded", 23), ("parameter", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpPingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpPingStatus.setDescription('The results of a ping request. A result of alive(4) means the device is responding.')
nwIpTraceRouteTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1), )
if mibBuilder.loadTexts: nwIpTraceRouteTable.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteTable.setDescription('This table allows outbound traceroute requests to be generated from the Cabletron device to a specified destination IP address. It is indexed by destination address and source address to allow multiple requests by different owner IP addresses.')
nwIpTraceRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpTraceRouteDestination"), (0, "NETWORK-DIAGS", "nwIpTraceRouteOwner"))
if mibBuilder.loadTexts: nwIpTraceRouteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteEntry.setDescription('An IP TraceRoute Table entry containing objects for a particular traceroute request.')
nwIpTraceRouteDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteDestination.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteDestination.setDescription('The IP address of the host/device to be traced.')
nwIpTraceRouteOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteOwner.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteOwner.setDescription('The IP address of the client which created this trace request.')
nwIpTraceRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2))).clone('other')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteType.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteType.setDescription('The administrative control of this trace request entry. This leaf is used to create a traceroute request entry.')
nwIpTraceRouteAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("activate", 2), ("suspend", 3))).clone('activate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteAction.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteAction.setDescription('The action to be perfomed with this request.')
nwIpTraceRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("other", 1), ("not-sent", 2), ("in-progress", 3), ("alive", 4), ("timeout", 5), ("bad-results", 6), ("failed", 7), ("net-unreach", 8), ("host-unreach", 9), ("proto-unreach", 10), ("port-unreach", 11), ("cant-frag", 12), ("sr-failed", 13), ("net-unknown", 14), ("host-unknown", 15), ("isolated", 16), ("no-net-comm", 17), ("no-host-comm", 18), ("no-net-tos", 19), ("no-host-tos", 20), ("source-quence", 21), ("ttl-exceeded", 22), ("frag-exceeded", 23), ("parameter", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteStatus.setDescription('The results of a trace request. A result of alive(3) means the end device has responded. Otherwise the next hop count will indicate how many hops were traversed.')
nwIpTraceRouteNextHops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteNextHops.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteNextHops.setDescription('The number of next-hop routers/gateways traversed. This value should be used to read entries in the TraveRouteHop Table.')
nwIpTraceRouteHopTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2), )
if mibBuilder.loadTexts: nwIpTraceRouteHopTable.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopTable.setDescription('This table contains the next-hop Ip Addresses of each hop traversed for a particular TraceRoute request.')
nwIpTraceRouteHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpTraceRouteHopDestination"), (0, "NETWORK-DIAGS", "nwIpTraceRouteHopOwner"), (0, "NETWORK-DIAGS", "nwIpTraceRouteHopNumber"))
if mibBuilder.loadTexts: nwIpTraceRouteHopEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopEntry.setDescription('An IP NextHop Table entry containing objects for a particular traceroute request.')
nwIpTraceRouteHopDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopDestination.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopDestination.setDescription('The IP address of the host/device for which this entry exists.')
nwIpTraceRouteHopOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopOwner.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopOwner.setDescription('The IP address of the client for which this entry exists.')
nwIpTraceRouteHopNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopNumber.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopNumber.setDescription('The hop number of this gateway in the table of next-hop routers/gateways traversed. This value indicated how many hops away this router/gateway is.')
nwIpTraceRouteHopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopIp.setStatus('mandatory')
if mibBuilder.loadTexts: nwIpTraceRouteHopIp.setDescription('The IP address of this next-hop gateway.')
mibBuilder.exportSymbols("NETWORK-DIAGS", nwRevisionLevel=nwRevisionLevel, nwIpTraceRouteHopTable=nwIpTraceRouteHopTable, nwIpTraceRouteEntry=nwIpTraceRouteEntry, nwIpPingDestination=nwIpPingDestination, nwIpPingType=nwIpPingType, nwIpPingAction=nwIpPingAction, nwIpTraceRouteType=nwIpTraceRouteType, nwIpTraceRouteHopDestination=nwIpTraceRouteHopDestination, nwIpPingEntry=nwIpPingEntry, nwIpTraceRoute=nwIpTraceRoute, nwRevision=nwRevision, nwIpTraceRouteOwner=nwIpTraceRouteOwner, nwIpPing=nwIpPing, nwIpTraceRouteAction=nwIpTraceRouteAction, nwInternet=nwInternet, nwIpPingOwner=nwIpPingOwner, nwIpTraceRouteDestination=nwIpTraceRouteDestination, nwIpTraceRouteStatus=nwIpTraceRouteStatus, nwIpTraceRouteHopOwner=nwIpTraceRouteHopOwner, nwIpTraceRouteHopNumber=nwIpTraceRouteHopNumber, nwIpTraceRouteHopIp=nwIpTraceRouteHopIp, nwIpPingStatus=nwIpPingStatus, nwIpTraceRouteNextHops=nwIpTraceRouteNextHops, nwIpTraceRouteTable=nwIpTraceRouteTable, nwIpTraceRouteHopEntry=nwIpTraceRouteHopEntry, nwIpPingTable=nwIpPingTable)
