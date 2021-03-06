#
# PySNMP MIB module IB-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
IbIpoibClientIdentifier, IbVirtualLane, infinibandMIB = mibBuilder.importSymbols("IB-TC-MIB", "IbIpoibClientIdentifier", "IbVirtualLane", "infinibandMIB")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, iso, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32, Counter64, IpAddress, Counter32, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32", "Counter64", "IpAddress", "Counter32", "ObjectIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibIfMIB = ModuleIdentity((1, 3, 6, 1, 3, 117, 2))
ibIfMIB.setRevisions(('2006-06-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibIfMIB.setRevisionsDescriptions(('Initial version published as part of RFC XXXX.',))
if mibBuilder.loadTexts: ibIfMIB.setLastUpdated('200606270000Z')
if mibBuilder.loadTexts: ibIfMIB.setOrganization('IETF IP over IB (IPOIB) Working Group')
if mibBuilder.loadTexts: ibIfMIB.setContactInfo('Hal Rosenstock Postal: HNR Consulting 200 Old Harvard Road Boxboro MA 01719-1834 United States Email: hnrose@earthlink.net Email comments to the IPOIB WG Mailing List at ipoverib@ietf.org.')
if mibBuilder.loadTexts: ibIfMIB.setDescription('Copyright (C) The Internet Society (2006). The initial version of this MIB module was published in RFC XXXX; for full legal notices see the RFC itself. Supplementary information may be available on http://www.ietf.org/copyrights/ianamib.html. This module contains managed object definitions for managing InfiniBand interfaces.')
ibIfObjects = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 1))
ibIfNotifications = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 2))
ibIfConformance = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3))
ibIfPortStatTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 1), )
if mibBuilder.loadTexts: ibIfPortStatTable.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatTable.setDescription('This table provides detail statistics for all InfiniBand interfaces attached to a particular system. There will be one row in this table for each InfiniBand interface in the system.')
ibIfPortStatEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 1, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIfPortStatIfIndex"))
if mibBuilder.loadTexts: ibIfPortStatEntry.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatEntry.setDescription('Statistics for a particular interface to an InfiniBand medium.')
ibIfPortStatIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIfPortStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatIfIndex.setDescription('The ifIndex value of the InfiniBand interface to which these port statistics apply.')
ibIfPortSymbolErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortSymbolErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::SymbolErrorCounter.')
if mibBuilder.loadTexts: ibIfPortSymbolErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortSymbolErrs.setDescription('Total number of minor link errors detected on one or more physical lanes.')
ibIfPortLinkErrRecovery = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortLinkErrRecovery.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::LinkErrorRecoveryCounter.')
if mibBuilder.loadTexts: ibIfPortLinkErrRecovery.setStatus('current')
if mibBuilder.loadTexts: ibIfPortLinkErrRecovery.setDescription('Total number of times the Port Training state machine has successfully completed the link error recovery process.')
ibIfPortLinkDowned = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortLinkDowned.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::LinkDownedCounter.')
if mibBuilder.loadTexts: ibIfPortLinkDowned.setStatus('current')
if mibBuilder.loadTexts: ibIfPortLinkDowned.setDescription('Total number of times the Port Training state machine has failed the link error recovery process and downed the link.')
ibIfPortStatLocalPhyErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatLocalPhyErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::PortRcvErrors.')
if mibBuilder.loadTexts: ibIfPortStatLocalPhyErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatLocalPhyErrs.setDescription('Total number of packets received on the port that contain local physical errors (ICRC, VCRC, FCCRC, and all physical errors that cause entry into the BAD PACKET or BAD PACKET DISCARD states of the packet receiver state machine).')
ibIfPortStatMalPktErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatMalPktErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::PortRcvErrors.')
if mibBuilder.loadTexts: ibIfPortStatMalPktErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatMalPktErrs.setDescription('Total number of packets received on the port that contain malformed packet errors - data packets: LVer, length, VL - link packets: operand, length, VL')
ibIfPortStatRcvRemPhyErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatRcvRemPhyErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::PortRcvRemotePhysicalErrors.')
if mibBuilder.loadTexts: ibIfPortStatRcvRemPhyErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatRcvRemPhyErrs.setDescription('Total number of packets marked with the EBP delimiter received on the port.')
ibIfPortStatRcvConstrErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatRcvConstrErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::PortRcvConstraintErrors.')
if mibBuilder.loadTexts: ibIfPortStatRcvConstrErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatRcvConstrErrs.setDescription('Total number of packets received on the port that are discarded for the following reasons: - FilterRawInbound is true and packet is raw - PartitionEnforcementInbound is true and packet fails partition key check or IP version check.')
ibIfPortStatInactDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatInactDiscards.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.4.2; Table 229 PortXmitDiscardDetails::PortInactiveDiscards.')
if mibBuilder.loadTexts: ibIfPortStatInactDiscards.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatInactDiscards.setDescription('Total number of outbound packets discarded by the port because it is not in the active state.')
ibIfPortStatNeighMTUDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatNeighMTUDiscards.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.4.2; Table 229 PortXmitDiscardDetails::PortNeighborMTUDiscards.')
if mibBuilder.loadTexts: ibIfPortStatNeighMTUDiscards.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatNeighMTUDiscards.setDescription('Total number of outbound packets discarded by the port because packet length exceeded the neighbor MTU.')
ibIfPortStatSwLifetimeDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatSwLifetimeDiscards.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.4.2; Table 229 PortXmitDiscardDetails::PortSwLifetimeLimitDiscards.')
if mibBuilder.loadTexts: ibIfPortStatSwLifetimeDiscards.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatSwLifetimeDiscards.setDescription('Total number of outbound packets discarded by the port because the Switch Lifetime Limit was exceeded. Note this object is only incremented for switches.')
ibIfPortStatHOQLifetimeDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatHOQLifetimeDiscards.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.4.2; Table 229 PortXmitDiscardDetails::PortSwHOQLimitDiscards.')
if mibBuilder.loadTexts: ibIfPortStatHOQLifetimeDiscards.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatHOQLifetimeDiscards.setDescription('Total number of outbound packets discarded by the port because the switch HOQ lifetime was exceeded. Note this object is only incremented for switches.')
ibIfPortStatLinkIntergrityErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatLinkIntergrityErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::LocalLinkIntegrityErrors.; Also see Table 145 PortInfo.')
if mibBuilder.loadTexts: ibIfPortStatLinkIntergrityErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatLinkIntergrityErrs.setDescription('The number of times that the count of local physical errors exceeded the LocalPhyErrors threshold.')
ibIfPortStatExcBufOverrunErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatExcBufOverrunErrs.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::ExcessiveBufferOverrunErrors.; Also see Table 145 PortInfo.')
if mibBuilder.loadTexts: ibIfPortStatExcBufOverrunErrs.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatExcBufOverrunErrs.setDescription('The number of times that OverrunErrors consecutive flow control update periods occurred with at least one overrun error in each period.')
ibIfPortStatVL15Dropped = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatVL15Dropped.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.5; Table 225 PortCounters::VL15Dropped.')
if mibBuilder.loadTexts: ibIfPortStatVL15Dropped.setStatus('current')
if mibBuilder.loadTexts: ibIfPortStatVL15Dropped.setDescription('Number of incoming VL15 packets dropped due to resource limitations on the selected port (e.g., lack of buffers).')
ibIfVLTrafficTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 2), )
if mibBuilder.loadTexts: ibIfVLTrafficTable.setStatus('current')
if mibBuilder.loadTexts: ibIfVLTrafficTable.setDescription('This table provides traffic statistics for all virtual lanes that are configured on an InfiniBand interface. There will always be at least one data virtual lane in the range VL0-VL14 configured on an interface, as well as control channel VL15. Configuration of what VLs are available on a particular interface is done by IBA native management.')
ibIfVLTrafficEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 2, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIfVLTrafficIfIndex"), (0, "IB-IF-MIB", "ibIfVLIndex"))
if mibBuilder.loadTexts: ibIfVLTrafficEntry.setStatus('current')
if mibBuilder.loadTexts: ibIfVLTrafficEntry.setDescription('Information about a particular virtual lane (VL).')
ibIfVLTrafficIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIfVLTrafficIfIndex.setStatus('current')
if mibBuilder.loadTexts: ibIfVLTrafficIfIndex.setDescription('The ifIndex value of the InfiniBand interface to which these virtual lane (VL) traffic statistics apply.')
ibIfVLIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 2), IbVirtualLane())
if mibBuilder.loadTexts: ibIfVLIndex.setStatus('current')
if mibBuilder.loadTexts: ibIfVLIndex.setDescription('Identifies what Virtual Lane (VL) instance is being addressed.')
ibIfVLOutOctets = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLOutOctets.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.3; Table 223 CounterSelect::PortXmitDataVL.')
if mibBuilder.loadTexts: ibIfVLOutOctets.setStatus('current')
if mibBuilder.loadTexts: ibIfVLOutOctets.setDescription('The number of octets transmitted in valid data packets on this interface, including the START and END delimiters and the VCRC for this VL.')
ibIfVLOutPkts = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLOutPkts.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.3; Table 223 CounterSelect::PortXmitPktVL.')
if mibBuilder.loadTexts: ibIfVLOutPkts.setStatus('current')
if mibBuilder.loadTexts: ibIfVLOutPkts.setDescription('The number of packets successfully sent on this VL.')
ibIfVLInOctets = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLInOctets.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.3; Table 223 CounterSelect::PortRcvDataVL.')
if mibBuilder.loadTexts: ibIfVLInOctets.setStatus('current')
if mibBuilder.loadTexts: ibIfVLInOctets.setDescription('The number of octets in valid data packets received on this interface, including the START and END delimiters and the VCRC for this VL.')
ibIfVLInPkts = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLInPkts.setReference('InfiniBand Architecture Release 1.2 Vol. 1. Section 16.1.3.3; Table 223 CounterSelect::PortRcvPktVL.')
if mibBuilder.loadTexts: ibIfVLInPkts.setStatus('current')
if mibBuilder.loadTexts: ibIfVLInPkts.setDescription('The number of packets successfully received on this VL. This does not include link packets, since link packets are generated by the interface layer, and are not passed from any higher layer protocol.')
ibIpoibLinkLayerAddrTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 3), )
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrTable.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrTable.setDescription('This table contains information about all IPOIB link layer addresses associated with this InfiniBand interface (port).')
ibIpoibLinkLayerAddrEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 3, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIpoibLinkLayerIfIndex"), (0, "IB-IF-MIB", "ibIpoibLinkLayerIndex"))
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrEntry.setDescription('Information about specific IPOIB link layer addresses associated with this InfiniBand interface (port).')
ibIpoibLinkLayerIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIpoibLinkLayerIfIndex.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkLayerIfIndex.setDescription('The ifIndex of the IPOIB InfiniBand interface (port).')
ibIpoibLinkLayerIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ibIpoibLinkLayerIndex.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkLayerIndex.setDescription('Index of the IPOIB Link Layer address in the table.')
ibIpoibLinkLayerAddr = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 3), IbIpoibClientIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIpoibLinkLayerAddr.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkLayerAddr.setDescription('A Client Identifier for this interface (port). An implementation may associate multiple IPOIB interfaces on the same port. It is up to the implementation to ensure a unique Client Identifier when multiple IPOIB interfaces are defined over the same port and same GID. A unique, invariant interface-id value must be included in addition to the GID within the Client Identifier definition to achieve this. Note: a port may also be associated with multiple GIDs. Therefore, multiple IPOIB interfaces may exist on the same port while using a different GID from among the GIDs associated with the port. In either case, the IbIpoibLinkLayerAddr MUST be unique.')
ibIfCompliances = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3, 1))
ibIfMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3, 2))
ibIfBasicCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 2, 3, 1, 1)).setObjects(("IB-IF-MIB", "ibIfStatMandatoryPortStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfBasicCompliance = ibIfBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: ibIfBasicCompliance.setDescription('The basic implementation requirements for managed network entities that have InfiniBand network interfaces.')
ibIfFullCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 2, 3, 1, 2)).setObjects(("IB-IF-MIB", "ibIfStatMandatoryPortStatGroup"), ("IB-IF-MIB", "ibIfStatOptionalPortStatGroup"), ("IB-IF-MIB", "ibIfVLTrafficGroup"), ("IB-IF-MIB", "ibIpoibLinkAddrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfFullCompliance = ibIfFullCompliance.setStatus('current')
if mibBuilder.loadTexts: ibIfFullCompliance.setDescription('The full implementation requirements for managed network entities that have InfiniBand network interfaces.')
ibIfStatMandatoryPortStatGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 1)).setObjects(("IB-IF-MIB", "ibIfPortSymbolErrs"), ("IB-IF-MIB", "ibIfPortLinkErrRecovery"), ("IB-IF-MIB", "ibIfPortLinkDowned"), ("IB-IF-MIB", "ibIfPortStatRcvRemPhyErrs"), ("IB-IF-MIB", "ibIfPortStatRcvConstrErrs"), ("IB-IF-MIB", "ibIfPortStatLinkIntergrityErrs"), ("IB-IF-MIB", "ibIfPortStatExcBufOverrunErrs"), ("IB-IF-MIB", "ibIfPortStatVL15Dropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfStatMandatoryPortStatGroup = ibIfStatMandatoryPortStatGroup.setStatus('current')
if mibBuilder.loadTexts: ibIfStatMandatoryPortStatGroup.setDescription('Detailed error statistics group for mandatory InfiniBand-based Port Statistics counters.')
ibIfStatOptionalPortStatGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 2)).setObjects(("IB-IF-MIB", "ibIfPortStatLocalPhyErrs"), ("IB-IF-MIB", "ibIfPortStatMalPktErrs"), ("IB-IF-MIB", "ibIfPortStatInactDiscards"), ("IB-IF-MIB", "ibIfPortStatNeighMTUDiscards"), ("IB-IF-MIB", "ibIfPortStatSwLifetimeDiscards"), ("IB-IF-MIB", "ibIfPortStatHOQLifetimeDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfStatOptionalPortStatGroup = ibIfStatOptionalPortStatGroup.setStatus('current')
if mibBuilder.loadTexts: ibIfStatOptionalPortStatGroup.setDescription('Detailed error statistics group for optional InfiniBand-based Port Statistics counters.')
ibIfVLTrafficGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 3)).setObjects(("IB-IF-MIB", "ibIfVLOutOctets"), ("IB-IF-MIB", "ibIfVLOutPkts"), ("IB-IF-MIB", "ibIfVLInOctets"), ("IB-IF-MIB", "ibIfVLInPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfVLTrafficGroup = ibIfVLTrafficGroup.setStatus('current')
if mibBuilder.loadTexts: ibIfVLTrafficGroup.setDescription('Detailed per VL traffic statistics group.')
ibIpoibLinkAddrGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 4)).setObjects(("IB-IF-MIB", "ibIpoibLinkLayerAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIpoibLinkAddrGroup = ibIpoibLinkAddrGroup.setStatus('current')
if mibBuilder.loadTexts: ibIpoibLinkAddrGroup.setDescription('Detailed per port IPOIB link layer address group.')
mibBuilder.exportSymbols("IB-IF-MIB", ibIfPortLinkErrRecovery=ibIfPortLinkErrRecovery, ibIpoibLinkLayerAddr=ibIpoibLinkLayerAddr, ibIfVLIndex=ibIfVLIndex, ibIfNotifications=ibIfNotifications, ibIfVLInPkts=ibIfVLInPkts, ibIfVLTrafficEntry=ibIfVLTrafficEntry, ibIpoibLinkLayerIfIndex=ibIpoibLinkLayerIfIndex, ibIfPortStatLinkIntergrityErrs=ibIfPortStatLinkIntergrityErrs, ibIfObjects=ibIfObjects, ibIfVLTrafficGroup=ibIfVLTrafficGroup, ibIfPortStatRcvRemPhyErrs=ibIfPortStatRcvRemPhyErrs, ibIfPortStatExcBufOverrunErrs=ibIfPortStatExcBufOverrunErrs, ibIfPortStatIfIndex=ibIfPortStatIfIndex, ibIfPortStatNeighMTUDiscards=ibIfPortStatNeighMTUDiscards, ibIfConformance=ibIfConformance, ibIfPortStatRcvConstrErrs=ibIfPortStatRcvConstrErrs, ibIfCompliances=ibIfCompliances, ibIfPortSymbolErrs=ibIfPortSymbolErrs, ibIfVLOutOctets=ibIfVLOutOctets, ibIfPortStatVL15Dropped=ibIfPortStatVL15Dropped, ibIfPortLinkDowned=ibIfPortLinkDowned, ibIfStatOptionalPortStatGroup=ibIfStatOptionalPortStatGroup, ibIpoibLinkLayerAddrEntry=ibIpoibLinkLayerAddrEntry, ibIfBasicCompliance=ibIfBasicCompliance, ibIfPortStatLocalPhyErrs=ibIfPortStatLocalPhyErrs, ibIfVLTrafficTable=ibIfVLTrafficTable, ibIfVLInOctets=ibIfVLInOctets, ibIfPortStatMalPktErrs=ibIfPortStatMalPktErrs, ibIfMIB=ibIfMIB, PYSNMP_MODULE_ID=ibIfMIB, ibIpoibLinkLayerAddrTable=ibIpoibLinkLayerAddrTable, ibIpoibLinkLayerIndex=ibIpoibLinkLayerIndex, ibIfVLTrafficIfIndex=ibIfVLTrafficIfIndex, ibIpoibLinkAddrGroup=ibIpoibLinkAddrGroup, ibIfPortStatEntry=ibIfPortStatEntry, ibIfStatMandatoryPortStatGroup=ibIfStatMandatoryPortStatGroup, ibIfPortStatTable=ibIfPortStatTable, ibIfVLOutPkts=ibIfVLOutPkts, ibIfPortStatHOQLifetimeDiscards=ibIfPortStatHOQLifetimeDiscards, ibIfPortStatSwLifetimeDiscards=ibIfPortStatSwLifetimeDiscards, ibIfFullCompliance=ibIfFullCompliance, ibIfMIBGroups=ibIfMIBGroups, ibIfPortStatInactDiscards=ibIfPortStatInactDiscards)
