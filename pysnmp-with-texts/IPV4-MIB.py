#
# PySNMP MIB module IPV4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4, = mibBuilder.importSymbols("APENT-MIB", "apIpv4")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, IpAddress, Integer32, NotificationType, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier, Counter64, ModuleIdentity, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "Bits", "Gauge32")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
apIpv4Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 1))
if mibBuilder.loadTexts: apIpv4Mib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: apIpv4Mib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIpv4Mib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIpv4Mib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for IPv4 Global Information')
apIpv4SourceRoute = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4SourceRoute.setStatus('current')
if mibBuilder.loadTexts: apIpv4SourceRoute.setDescription('If enabled, IP packets with a source route option will be processed. If disabled, they are dropped.')
apIpv4RecordRoute = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RecordRoute.setStatus('current')
if mibBuilder.loadTexts: apIpv4RecordRoute.setDescription('If enabled, IP packets with a record route option will be processed. If disabled, they are dropped.')
apIpv4SubnetBcast = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4SubnetBcast.setStatus('current')
if mibBuilder.loadTexts: apIpv4SubnetBcast.setDescription('If enabled, IP packets addressed to a broadcast address of a local subnet will be forwarded. If disabled, they are dropped.')
apIpv4EcmpMethod = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("address", 1), ("round", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4EcmpMethod.setStatus('current')
if mibBuilder.loadTexts: apIpv4EcmpMethod.setDescription("Defines the algorithm to use when multiple equal-cost paths are available to the same destination. 'address' uses the IP addresses to assign a path. 'round' does a simple round-robin.")
apIpv4OrphanTimer = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 6), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4OrphanTimer.setStatus('current')
if mibBuilder.loadTexts: apIpv4OrphanTimer.setDescription('The amount of time, in seconds, that a route will be kept after an SCM recovery. Default is 3 minutes.')
apIpv4LogRouteChanges = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4LogRouteChanges.setStatus('current')
if mibBuilder.loadTexts: apIpv4LogRouteChanges.setDescription('If enabled, IP route changes will be displayed in the system log.')
apIpv4ReachRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4ReachRoutes.setStatus('current')
if mibBuilder.loadTexts: apIpv4ReachRoutes.setDescription('Current number of reachable routes.')
apIpv4ReachRoutesMem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4ReachRoutesMem.setStatus('current')
if mibBuilder.loadTexts: apIpv4ReachRoutesMem.setDescription('Amount of memory used to maintain reachable routes.')
apIpv4TotalRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4TotalRoutes.setStatus('current')
if mibBuilder.loadTexts: apIpv4TotalRoutes.setDescription('Current number of routes maintainted, both reachable and unreachable.')
apIpv4TotalRoutesMem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4TotalRoutesMem.setStatus('current')
if mibBuilder.loadTexts: apIpv4TotalRoutesMem.setDescription('Amount of memory used to maintain all routes.')
apIpv4ReachHosts = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4ReachHosts.setStatus('current')
if mibBuilder.loadTexts: apIpv4ReachHosts.setDescription('Current number of reachable host entries.')
apIpv4ReachHostsMem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4ReachHostsMem.setStatus('current')
if mibBuilder.loadTexts: apIpv4ReachHostsMem.setDescription('Amount of memory used to maintain reachable host entries.')
apIpv4TotalHosts = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4TotalHosts.setStatus('current')
if mibBuilder.loadTexts: apIpv4TotalHosts.setDescription('Current number of host entries maintainted, both reachable and unreachable.')
apIpv4TotalHostsMem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4TotalHostsMem.setStatus('current')
if mibBuilder.loadTexts: apIpv4TotalHostsMem.setDescription('Amount of memory used to maintain all host entries.')
apIpv4PoolMem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4PoolMem.setStatus('current')
if mibBuilder.loadTexts: apIpv4PoolMem.setDescription('Amount of memory held in IP routing table pool.')
apIpv4B2BRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4B2BRedundancy.setStatus('current')
if mibBuilder.loadTexts: apIpv4B2BRedundancy.setDescription('Indicates whether box-to-box redundancy is configured on this box.')
apIpv4Opportunistic = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local", 1), ("all", 2), ("disable", 3))).clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4Opportunistic.setStatus('current')
if mibBuilder.loadTexts: apIpv4Opportunistic.setDescription("Indicates the operating mode for layer-3 opportunistic forwarding. In 'local' mode (the default), packets whose IP address equals a resolved node attached to a local subnet will be forwarded to that node regardless of the destination MAC address of the packet. In 'all' mode, packets whose IP address matches any reachable IP routing entry will be forwarded according to the routing entry regardless of the destination MAC address of the packet. In 'disable' mode, only packets whose destination MAC address equal this node's MAC address will be forwarded using an IP route entry.")
apIpv4RedundancyState = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("init", 1), ("backup", 2), ("master", 3))).clone('init')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RedundancyState.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyState.setDescription('The current redundancy state')
apIpv4RedundancyIf = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RedundancyIf.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyIf.setDescription('The IP address of the redundant link')
apIpv4RedundancyMaster = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 21), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RedundancyMaster.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyMaster.setDescription('The IP address of the redundant Master')
apIpv4RedundancyMasterMode = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RedundancyMasterMode.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyMasterMode.setDescription('Indicates whether box-to-box redundancy is configured to always be the master.')
apIpv4EcmpSticky = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4EcmpSticky.setStatus('current')
if mibBuilder.loadTexts: apIpv4EcmpSticky.setDescription('This object specifies whether when making an ECMP decision on the return port, should the ingress port be the preferred path.')
apIpv4ImplicitService = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4ImplicitService.setStatus('current')
if mibBuilder.loadTexts: apIpv4ImplicitService.setDescription('This object specifies whether when configuring a static route, if an implicit service should be started for the next hop address.')
apIpv4RedundancyLinkFailTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25), )
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailTable.setDescription('The IP redundancy Interface failure monitor table.')
apIpv4RedundancyLinkFailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1), ).setIndexNames((0, "IPV4-MIB", "apIpv4RedundancyLinkFailIfIndex"))
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailEntry.setDescription('An entry in the IP redundancy Interface failure monitor table.')
apIpv4RedundancyLinkFailIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailIfIndex.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyLinkFailIfIndex.setDescription('Interface Index used to uniquely identify ethernet interface ')
apIpv4RedundancyLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RedundancyLinkStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyLinkStatus.setDescription('Monitor this interface for physical link failure if true')
apIpv4RedundancyFailReason = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noFailure", 0), ("phylinkFail", 1), ("uplinkFailure", 2), ("otherSwitchAssertMaster", 3))).clone('noFailure')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RedundancyFailReason.setStatus('current')
if mibBuilder.loadTexts: apIpv4RedundancyFailReason.setDescription('The redundancy state change reason')
apIpv4VrrpVRID = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4VrrpVRID.setStatus('current')
if mibBuilder.loadTexts: apIpv4VrrpVRID.setDescription('This object tells virtual router ID in vrrp protocol.')
apIpv4VrrpPriority = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4VrrpPriority.setStatus('current')
if mibBuilder.loadTexts: apIpv4VrrpPriority.setDescription('This object tells virtual router priority in vrrp.')
apIpv4numUplinkServices = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4numUplinkServices.setStatus('current')
if mibBuilder.loadTexts: apIpv4numUplinkServices.setDescription('This object tells number of uplink services enabled.')
apIpv4numViableUplinks = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4numViableUplinks.setStatus('current')
if mibBuilder.loadTexts: apIpv4numViableUplinks.setDescription('This object tells number of uplink services alive.')
apIpv4numPhylinkMarked = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4numPhylinkMarked.setStatus('current')
if mibBuilder.loadTexts: apIpv4numPhylinkMarked.setDescription('This object tells number of redundant-physical links monitored.')
apIpv4toMasterStateCnt = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4toMasterStateCnt.setStatus('current')
if mibBuilder.loadTexts: apIpv4toMasterStateCnt.setDescription('This object tells number of times the box become master.')
apIpv4toBackupStateCnt = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4toBackupStateCnt.setStatus('current')
if mibBuilder.loadTexts: apIpv4toBackupStateCnt.setDescription('This object tells number of times the box become backup.')
apIpv4RedundancyTrap = NotificationType((1, 3, 6, 1, 4, 1, 2467, 1, 9, 1) + (0,1))
if mibBuilder.loadTexts: apIpv4RedundancyTrap.setDescription('This trap is generated when the state of Redundancy changes.')
mibBuilder.exportSymbols("IPV4-MIB", apIpv4numUplinkServices=apIpv4numUplinkServices, apIpv4TotalHostsMem=apIpv4TotalHostsMem, apIpv4toBackupStateCnt=apIpv4toBackupStateCnt, apIpv4EcmpMethod=apIpv4EcmpMethod, apIpv4numViableUplinks=apIpv4numViableUplinks, apIpv4RedundancyIf=apIpv4RedundancyIf, apIpv4OrphanTimer=apIpv4OrphanTimer, apIpv4SubnetBcast=apIpv4SubnetBcast, apIpv4VrrpPriority=apIpv4VrrpPriority, apIpv4RedundancyFailReason=apIpv4RedundancyFailReason, apIpv4RedundancyMasterMode=apIpv4RedundancyMasterMode, apIpv4ReachHosts=apIpv4ReachHosts, apIpv4B2BRedundancy=apIpv4B2BRedundancy, apIpv4VrrpVRID=apIpv4VrrpVRID, apIpv4ReachRoutesMem=apIpv4ReachRoutesMem, apIpv4RedundancyLinkFailTable=apIpv4RedundancyLinkFailTable, apIpv4TotalHosts=apIpv4TotalHosts, apIpv4SourceRoute=apIpv4SourceRoute, apIpv4ReachRoutes=apIpv4ReachRoutes, apIpv4numPhylinkMarked=apIpv4numPhylinkMarked, apIpv4RedundancyLinkStatus=apIpv4RedundancyLinkStatus, apIpv4Opportunistic=apIpv4Opportunistic, apIpv4RedundancyLinkFailIfIndex=apIpv4RedundancyLinkFailIfIndex, apIpv4ReachHostsMem=apIpv4ReachHostsMem, apIpv4EcmpSticky=apIpv4EcmpSticky, apIpv4ImplicitService=apIpv4ImplicitService, apIpv4TotalRoutesMem=apIpv4TotalRoutesMem, apIpv4RedundancyTrap=apIpv4RedundancyTrap, apIpv4PoolMem=apIpv4PoolMem, apIpv4RedundancyMaster=apIpv4RedundancyMaster, apIpv4TotalRoutes=apIpv4TotalRoutes, apIpv4RedundancyLinkFailEntry=apIpv4RedundancyLinkFailEntry, apIpv4LogRouteChanges=apIpv4LogRouteChanges, apIpv4toMasterStateCnt=apIpv4toMasterStateCnt, apIpv4RedundancyState=apIpv4RedundancyState, apIpv4Mib=apIpv4Mib, apIpv4RecordRoute=apIpv4RecordRoute, PYSNMP_MODULE_ID=apIpv4Mib)
