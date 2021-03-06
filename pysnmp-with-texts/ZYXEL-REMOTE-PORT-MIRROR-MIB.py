#
# PySNMP MIB module ZYXEL-REMOTE-PORT-MIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-REMOTE-PORT-MIRROR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Unsigned32, Counter32, ObjectIdentity, ModuleIdentity, TimeTicks, Integer32, Gauge32, NotificationType, Counter64, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Integer32", "Gauge32", "NotificationType", "Counter64", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelRemotePortMirror = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73))
if mibBuilder.loadTexts: zyxelRemotePortMirror.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelRemotePortMirror.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelRemotePortMirror.setContactInfo('')
if mibBuilder.loadTexts: zyxelRemotePortMirror.setDescription('The subtree for remote port mirror')
zyxelRemotePortMirrorSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1))
zyRemotePortMirrorMaxNumberOfVlans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyRemotePortMirrorMaxNumberOfVlans.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorMaxNumberOfVlans.setDescription('The maximum number of remote mirror VLAN entries that can be created.')
zyxelRemotePortMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2), )
if mibBuilder.loadTexts: zyxelRemotePortMirrorTable.setStatus('current')
if mibBuilder.loadTexts: zyxelRemotePortMirrorTable.setDescription('The table contains remote port mirror configuration.')
zyxelRemotePortMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1), ).setIndexNames((0, "ZYXEL-REMOTE-PORT-MIRROR-MIB", "zyRemotePortMirrorVid"))
if mibBuilder.loadTexts: zyxelRemotePortMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelRemotePortMirrorEntry.setDescription('An entry contains remote port mirror configuration. ')
zyRemotePortMirrorVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyRemotePortMirrorVid.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorVid.setDescription('Enter the VLAN ID (1 to 4094) of the remote mirror VLAN. ')
zyRemotePortMirrorSource8021pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorSource8021pPriority.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorSource8021pPriority.setDescription('Select a priority level (0-7) with which the Switch replaces the priority of packets from source port (belonging to this remote mirror VLAN). ')
zyRemotePortMirrorSourceIngressMirrorPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorSourceIngressMirrorPorts.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorSourceIngressMirrorPorts.setDescription('Set port members to be the source ingress mirror-port. The mirror-port is the port traffic that we mirrored: 1. Mirror-ports is only existed in source switch. 2. It can be any port type, such as Ether Channel, Fast Ethernet, Gigabit Ethernet, and so forth. 3. It can be monitored in multiple remote mirror VLAN. 4. It cannot be a monitor-port, reflector-port and connected-port.')
zyRemotePortMirrorSourceEgressMirrorPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorSourceEgressMirrorPorts.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorSourceEgressMirrorPorts.setDescription('Set port members to be the source egress mirror-port. The mirror-port is the port traffic that we mirrored: 1. Mirror-ports is only existed in source switch. 2. It can be any port type, such as Ether Channel, Fast Ethernet, Gigabit Ethernet, and so forth. 3. It can be monitored in multiple remote mirror VLAN. 4. It cannot be a monitor-port, reflector-port and connected-port.')
zyRemotePortMirrorSourceReflectorPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorSourceReflectorPortState.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorSourceReflectorPortState.setDescription('Enable/disable multi-mirroring on RMirror Source. Once the multi-mirroring is enabled, the reflector-port can be used in the RMirrore Source.')
zyRemotePortMirrorSourceReflectorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorSourceReflectorPort.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorSourceReflectorPort.setDescription('Set port members to be the source reflector-port. The reflector port is the mechanism that copies packets onto an remote mirror VLAN. The reflector port forwards only traffic from remote mirror VLAN with which it is affiliated: 1. A reflector-port is only existed in source switch. 2. Spanning tree is automatically disabled on a reflector-port. 3. It is a port set to loopback. 4. The reflector port loops back untagged traffic to the switch. The traffic is then placed on the RSPAN VLAN and flooded to any trunk ports that carry the RSPAN VLAN. 5. The reflector-port can not be mirror-port and monitor-port.')
zyRemotePortMirrorDestinationMonitorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorDestinationMonitorPort.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorDestinationMonitorPort.setDescription('Set the port number of the destination monitor port. The monitor-port is the port that we can monitor the RMirror traffic: 1. A monitor-port is only in destination switch. 2. It can participate in only one RMirror VLAN at a time. 3. A monitor-port in one RMirror VLAN cannot be another RMirror VLAN. 4. A monitor-port can not be a mirror-port, reflector-port and connected-port.')
zyRemotePortMirrorDestinationMonitorPortTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 8), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorDestinationMonitorPortTagging.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorDestinationMonitorPortTagging.setDescription('Enable/Disable the destination monitor port which packet with tag.')
zyRemotePortMirrorConnectedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 9), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRemotePortMirrorConnectedPorts.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorConnectedPorts.setDescription('Set port members to be the connected-port. The connected-port is the physical port connected to other switch in the same remote mirror VLAN: 1. The port must join the remote mirror VLAN. 2. The connected-port can not be mirror-port and monitor-port.')
zyRemotePortMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyRemotePortMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyRemotePortMirrorRowStatus.setDescription('This object allows entries to be created and deleted from the remote mirror table.')
mibBuilder.exportSymbols("ZYXEL-REMOTE-PORT-MIRROR-MIB", zyRemotePortMirrorSourceReflectorPortState=zyRemotePortMirrorSourceReflectorPortState, zyRemotePortMirrorMaxNumberOfVlans=zyRemotePortMirrorMaxNumberOfVlans, zyRemotePortMirrorSource8021pPriority=zyRemotePortMirrorSource8021pPriority, PYSNMP_MODULE_ID=zyxelRemotePortMirror, zyRemotePortMirrorSourceIngressMirrorPorts=zyRemotePortMirrorSourceIngressMirrorPorts, zyRemotePortMirrorConnectedPorts=zyRemotePortMirrorConnectedPorts, zyxelRemotePortMirrorSetup=zyxelRemotePortMirrorSetup, zyRemotePortMirrorDestinationMonitorPortTagging=zyRemotePortMirrorDestinationMonitorPortTagging, zyRemotePortMirrorVid=zyRemotePortMirrorVid, zyRemotePortMirrorSourceEgressMirrorPorts=zyRemotePortMirrorSourceEgressMirrorPorts, zyRemotePortMirrorRowStatus=zyRemotePortMirrorRowStatus, zyRemotePortMirrorDestinationMonitorPort=zyRemotePortMirrorDestinationMonitorPort, zyxelRemotePortMirrorEntry=zyxelRemotePortMirrorEntry, zyxelRemotePortMirror=zyxelRemotePortMirror, zyxelRemotePortMirrorTable=zyxelRemotePortMirrorTable, zyRemotePortMirrorSourceReflectorPort=zyRemotePortMirrorSourceReflectorPort)
