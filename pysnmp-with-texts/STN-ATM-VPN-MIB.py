#
# PySNMP MIB module STN-ATM-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-ATM-VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Counter32, NotificationType, iso, Bits, IpAddress, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Counter32", "NotificationType", "iso", "Bits", "IpAddress", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnRouterAtmVpn, = mibBuilder.importSymbols("STN-ROUTER-MIB", "stnRouterAtmVpn")
stnAtmVpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1))
if mibBuilder.loadTexts: stnAtmVpn.setLastUpdated('0008080000Z')
if mibBuilder.loadTexts: stnAtmVpn.setOrganization('Spring Tide Networks')
if mibBuilder.loadTexts: stnAtmVpn.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Suite 200 Maynard, MA 01754 USA Tel: +1 978 298 2000 Email: custserv@springtidenet.com ')
if mibBuilder.loadTexts: stnAtmVpn.setDescription('This MIB module describes managed objects of Spring Tide Networks ATM VPN Interfaces.')
stnAtmVpnTrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1))
stnAtmVpnLinkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2))
stnAtmVpnTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1), )
if mibBuilder.loadTexts: stnAtmVpnTrunkTable.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkTable.setDescription('A list of ATM VPN Trunk entries.')
stnAtmVpnTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1), ).setIndexNames((0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkIfIndex"))
if mibBuilder.loadTexts: stnAtmVpnTrunkEntry.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkEntry.setDescription('Entry contains information about a particular ATM VPN Trunk.')
stnAtmVpnTrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkIfIndex.setDescription('The ifIndex of the ATM VPN Trunk Interface.')
stnAtmVpnTrunkViId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkViId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkViId.setDescription('The instance of the configuration record corresponding to this ATM VPN Trunk.')
stnAtmVpnTrunkName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkName.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkName.setDescription('The name configured for this ATM VPN Trunk.')
stnAtmVpnTrunkState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkState.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkState.setDescription('The current operational state of the ATM VPN Trunk.')
stnAtmVpnTrunkLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkLowerIfIndex.setDescription('The ifIndex of the Interface below the ATM VPN Trunk Interface.')
stnAtmVpnTrunkVpnPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkVpnPaths.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkVpnPaths.setDescription('The number of VPN Paths that this ATM VPN Trunk has in its forwarding table.')
stnAtmVpnTrunkInUnknownVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkInUnknownVpnId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkInUnknownVpnId.setDescription("The number packets received with a Vpn-Id that was not present it the ATM VPN Trunk's forwarding table.")
stnAtmVpnTrunkInVpnIdIfaceInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkInVpnIdIfaceInvalid.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkInVpnIdIfaceInvalid.setDescription('The number packets received with a Vpn-Id that was known, but the entry in the FIB refered to an invalid or non-existant interface. This can indicate an invalid configuration.')
stnAtmVpnTrunkOutUnknownVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkOutUnknownVpnId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkOutUnknownVpnId.setDescription("The number packets passed to this trunk from another ATM VPN Trunk or Link with a Vpn-Id that was not present it the ATM VPN Trunk's forwarding table.")
stnAtmVpnTrunkOutVpnIdIfaceInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkOutVpnIdIfaceInvalid.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkOutVpnIdIfaceInvalid.setDescription('The number packets passed to this trunk from another ATM VPN Trunk or Link when there was no suitable interface below the ATM VPN Trunk.')
stnAtmVpnTrunkPathTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2), )
if mibBuilder.loadTexts: stnAtmVpnTrunkPathTable.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathTable.setDescription('A list of the ATM VPN Paths known to a ATM VPN Trunk.')
stnAtmVpnTrunkPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1), ).setIndexNames((0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathTrunkIfIndex"), (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnOUI"), (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnIndex"), (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnSubIndex"))
if mibBuilder.loadTexts: stnAtmVpnTrunkPathEntry.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathEntry.setDescription('Entry contains information about a particular remote MAC learned on a VEI VcLink.')
stnAtmVpnTrunkPathTrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathTrunkIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathTrunkIfIndex.setDescription('The IfIndex of the ATM VPN Trunk Interface which owns the VPN Path entry.')
stnAtmVpnTrunkPathVpnOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnOUI.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnOUI.setDescription('The VPN OUI for which packets this VPN Path pertains to.')
stnAtmVpnTrunkPathVpnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnIndex.setDescription('The VPN Index for which packets this VPN Path pertains to.')
stnAtmVpnTrunkPathVpnSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnSubIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathVpnSubIndex.setDescription('The VPN SubIndex for which packets this VPN Path pertains to.')
stnAtmVpnTrunkPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vpnLearnedPath", 1), ("vpnStaticPath", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathType.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathType.setDescription('Indicates the type of the VPN Path database entry. Learned indicates that the entry was dynamically learned from link/trunk configuration or other dynamic means. Static indicates that the entry was configured explicitly using a VirtualInterfaceInfo Entry.')
stnAtmVpnTrunkPathNextIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("atmVpnLink", 1), ("atmVpnTrunk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathNextIfType.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathNextIfType.setDescription('Indicates the type of ATM VPN Interface that this path points to.')
stnAtmVpnTrunkPathNextIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 7), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathNextIfIndex.setDescription('The IfIndex of the destination ATM VPN Interface which this path entry refers to.')
stnAtmVpnTrunkPathInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathInPackets.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathInPackets.setDescription('The number of packets that have been received by the ATM VPN Trunk for this VPN path.')
stnAtmVpnTrunkPathInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathInOctets.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathInOctets.setDescription('The number of octets that have been received by the ATM VPN Trunk for this VPN path.')
stnAtmVpnTrunkPathOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathOutPackets.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathOutPackets.setDescription('The number of packets that have been transmitted by the ATM VPN Trunk for this VPN path.')
stnAtmVpnTrunkPathOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnTrunkPathOutOctets.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnTrunkPathOutOctets.setDescription('The number of octets that have been transmitted by the ATM VPN Trunk for this VPN path.')
stnAtmVpnLinkTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1), )
if mibBuilder.loadTexts: stnAtmVpnLinkTable.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkTable.setDescription('A list of ATM VPN Link entries.')
stnAtmVpnLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1), ).setIndexNames((0, "STN-ATM-VPN-MIB", "stnAtmVpnLinkIfIndex"))
if mibBuilder.loadTexts: stnAtmVpnLinkEntry.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkEntry.setDescription('Entry contains information about a particular ATM VPN Link.')
stnAtmVpnLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkIfIndex.setDescription('The ifIndex of the ATM VPN Link Interface.')
stnAtmVpnLinkViId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkViId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkViId.setDescription('The instance of the configuration record corresponding to this ATM VPN Link.')
stnAtmVpnLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkName.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkName.setDescription('The name configured for this ATM VPN Link.')
stnAtmVpnLinkVpnOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkVpnOUI.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkVpnOUI.setDescription('The Vpn OUI that is associated with this ATM VPN Link.')
stnAtmVpnLinkVpnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkVpnIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkVpnIndex.setDescription('The Vpn Index that is associated with this ATM VPN Link.')
stnAtmVpnLinkVpnSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkVpnSubIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkVpnSubIndex.setDescription('The Vpn SubIndex that is associated with this ATM VPN Link.')
stnAtmVpnLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkState.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkState.setDescription('The current operational state of the ATM VPN LINK.')
stnAtmVpnLinkTrunkViId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkTrunkViId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkTrunkViId.setDescription('The instance of the configuration record corresponding to the ATM VPN Trunk associated with this ATM VPN Link. If the value is zero, then no ATM VPN Trunk is currently associated with this ATM VPN Link.')
stnAtmVpnLinkLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkLowerIfIndex.setDescription('The ifIndex of the Interface below the ATM VPN Link Interface.')
stnAtmVpnLinkOutUnknownVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkOutUnknownVpnId.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkOutUnknownVpnId.setDescription("The number packets passed from an ATM VPN Trunk with a Vpn-Id that was appropriate for the ATM VPN Link's forwarding table.")
stnAtmVpnLinkOutVpnIdIfaceInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkOutVpnIdIfaceInvalid.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkOutVpnIdIfaceInvalid.setDescription('The number packets passed from an ATM VPN Trunk when no appropriate interface exists below this ATM VPN Link.')
stnAtmVpnLinkInVpnIdIfaceInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAtmVpnLinkInVpnIdIfaceInvalid.setStatus('current')
if mibBuilder.loadTexts: stnAtmVpnLinkInVpnIdIfaceInvalid.setDescription('The number packets received when there was no appropriate ATM VPN Trunk Interface present.')
mibBuilder.exportSymbols("STN-ATM-VPN-MIB", stnAtmVpnLinkName=stnAtmVpnLinkName, stnAtmVpnTrunkOutUnknownVpnId=stnAtmVpnTrunkOutUnknownVpnId, stnAtmVpnTrunkOutVpnIdIfaceInvalid=stnAtmVpnTrunkOutVpnIdIfaceInvalid, stnAtmVpnLinkEntry=stnAtmVpnLinkEntry, stnAtmVpnTrunkState=stnAtmVpnTrunkState, stnAtmVpnLinkVpnOUI=stnAtmVpnLinkVpnOUI, stnAtmVpnLinkViId=stnAtmVpnLinkViId, stnAtmVpnTrunkLowerIfIndex=stnAtmVpnTrunkLowerIfIndex, stnAtmVpnLinkOutUnknownVpnId=stnAtmVpnLinkOutUnknownVpnId, stnAtmVpnTrunkPathEntry=stnAtmVpnTrunkPathEntry, stnAtmVpnTrunkInUnknownVpnId=stnAtmVpnTrunkInUnknownVpnId, stnAtmVpnTrunkPathNextIfType=stnAtmVpnTrunkPathNextIfType, stnAtmVpnTrunkPathOutOctets=stnAtmVpnTrunkPathOutOctets, stnAtmVpnTrunkPathType=stnAtmVpnTrunkPathType, stnAtmVpnTrunkEntry=stnAtmVpnTrunkEntry, stnAtmVpnLinkTable=stnAtmVpnLinkTable, stnAtmVpnLinkVpnSubIndex=stnAtmVpnLinkVpnSubIndex, stnAtmVpnTrunkVpnPaths=stnAtmVpnTrunkVpnPaths, stnAtmVpnTrunkPathInOctets=stnAtmVpnTrunkPathInOctets, stnAtmVpnLinkInVpnIdIfaceInvalid=stnAtmVpnLinkInVpnIdIfaceInvalid, stnAtmVpnTrunkPathVpnSubIndex=stnAtmVpnTrunkPathVpnSubIndex, stnAtmVpnTrunkIfIndex=stnAtmVpnTrunkIfIndex, stnAtmVpnTrunkPathInPackets=stnAtmVpnTrunkPathInPackets, stnAtmVpnTrunkTable=stnAtmVpnTrunkTable, stnAtmVpnTrunkObjects=stnAtmVpnTrunkObjects, stnAtmVpnTrunkPathTrunkIfIndex=stnAtmVpnTrunkPathTrunkIfIndex, stnAtmVpnLinkIfIndex=stnAtmVpnLinkIfIndex, stnAtmVpnTrunkPathVpnOUI=stnAtmVpnTrunkPathVpnOUI, PYSNMP_MODULE_ID=stnAtmVpn, stnAtmVpnTrunkViId=stnAtmVpnTrunkViId, stnAtmVpnTrunkName=stnAtmVpnTrunkName, stnAtmVpnLinkLowerIfIndex=stnAtmVpnLinkLowerIfIndex, stnAtmVpnTrunkInVpnIdIfaceInvalid=stnAtmVpnTrunkInVpnIdIfaceInvalid, stnAtmVpnTrunkPathNextIfIndex=stnAtmVpnTrunkPathNextIfIndex, stnAtmVpnTrunkPathOutPackets=stnAtmVpnTrunkPathOutPackets, stnAtmVpn=stnAtmVpn, stnAtmVpnLinkTrunkViId=stnAtmVpnLinkTrunkViId, stnAtmVpnLinkObjects=stnAtmVpnLinkObjects, stnAtmVpnTrunkPathTable=stnAtmVpnTrunkPathTable, stnAtmVpnLinkOutVpnIdIfaceInvalid=stnAtmVpnLinkOutVpnIdIfaceInvalid, stnAtmVpnTrunkPathVpnIndex=stnAtmVpnTrunkPathVpnIndex, stnAtmVpnLinkState=stnAtmVpnLinkState, stnAtmVpnLinkVpnIndex=stnAtmVpnLinkVpnIndex)
