#
# PySNMP MIB module TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:23:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
IANAtunnelType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAtunnelType")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
IPv6FlowLabelOrAny, = mibBuilder.importSymbols("IPV6-FLOW-LABEL-MIB", "IPv6FlowLabelOrAny")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, transmission, NotificationType, Counter32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "transmission", "NotificationType", "Counter32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "Unsigned32", "Integer32", "ModuleIdentity")
RowStatus, StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "DisplayString")
tunnelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 131))
tunnelMIB.setRevisions(('2005-05-16 00:00', '1999-08-24 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tunnelMIB.setRevisionsDescriptions(('IPv4-specific objects were deprecated, including tunnelIfLocalAddress, tunnelIfRemoteAddress, the tunnelConfigTable, and the tunnelMIBBasicGroup. Added IP version-agnostic objects that should be used instead, including tunnelIfAddressType, tunnelIfLocalInetAddress, tunnelIfRemoteInetAddress, the tunnelInetConfigTable, and the tunnelIMIBInetGroup. The new tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress objects are read-write, rather than read-only. Updated DESCRIPTION clauses of existing version- agnostic objects (e.g., tunnelIfTOS) that contained IPv4-specific text to cover IPv6 as well. Added tunnelIfFlowLabel for tunnels over IPv6. The encapsulation method was previously an INTEGER type, and is now an IANA-maintained textual convention. Published as RFC 4087.', 'Initial version, published as RFC 2667.',))
if mibBuilder.loadTexts: tunnelMIB.setLastUpdated('200505160000Z')
if mibBuilder.loadTexts: tunnelMIB.setOrganization('IETF IP Version 6 (IPv6) Working Group')
if mibBuilder.loadTexts: tunnelMIB.setContactInfo(' Dave Thaler Microsoft Corporation One Microsoft Way Redmond, WA 98052-6399 EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: tunnelMIB.setDescription('The MIB module for management of IP Tunnels, independent of the specific encapsulation scheme in use. Copyright (C) The Internet Society (2005). This version of this MIB module is part of RFC 4087; see the RFC itself for full legal notices.')
tunnelMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 1))
tunnel = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 1, 1))
tunnelIfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1), )
if mibBuilder.loadTexts: tunnelIfTable.setStatus('current')
if mibBuilder.loadTexts: tunnelIfTable.setDescription('The (conceptual) table containing information on configured tunnels.')
tunnelIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tunnelIfEntry.setStatus('current')
if mibBuilder.loadTexts: tunnelIfEntry.setDescription('An entry (conceptual row) containing the information on a particular configured tunnel.')
tunnelIfLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfLocalAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelIfLocalAddress.setDescription('The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header), or 0.0.0.0 if unknown or if the tunnel is over IPv6. Since this object does not support IPv6, it is deprecated in favor of tunnelIfLocalInetAddress.')
tunnelIfRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfRemoteAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelIfRemoteAddress.setDescription('The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header), or 0.0.0.0 if unknown, or an IPv6 address, or the tunnel is not a point-to-point link (e.g., if it is a 6to4 tunnel). Since this object does not support IPv6, it is deprecated in favor of tunnelIfRemoteInetAddress.')
tunnelIfEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 3), IANAtunnelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfEncapsMethod.setStatus('current')
if mibBuilder.loadTexts: tunnelIfEncapsMethod.setDescription('The encapsulation method used by the tunnel.')
tunnelIfHopLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 255), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfHopLimit.setStatus('current')
if mibBuilder.loadTexts: tunnelIfHopLimit.setDescription("The IPv4 TTL or IPv6 Hop Limit to use in the outer IP header. A value of 0 indicates that the value is copied from the payload's header.")
tunnelIfSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ipsec", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfSecurity.setStatus('current')
if mibBuilder.loadTexts: tunnelIfSecurity.setDescription('The method used by the tunnel to secure the outer IP header. The value ipsec indicates that IPsec is used between the tunnel endpoints for authentication or encryption or both. More specific security-related information may be available in a MIB module for the security protocol in use.')
tunnelIfTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfTOS.setStatus('current')
if mibBuilder.loadTexts: tunnelIfTOS.setDescription("The method used to set the high 6 bits (the differentiated services codepoint) of the IPv4 TOS or IPv6 Traffic Class in the outer IP header. A value of -1 indicates that the bits are copied from the payload's header. A value of -2 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB module. A value between 0 and 63 inclusive indicates that the bit field is set to the indicated value. Note: instead of the name tunnelIfTOS, a better name would have been tunnelIfDSCPMethod, but the existing name appeared in RFC 2667 and existing objects cannot be renamed.")
tunnelIfFlowLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 7), IPv6FlowLabelOrAny()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfFlowLabel.setStatus('current')
if mibBuilder.loadTexts: tunnelIfFlowLabel.setDescription('The method used to set the IPv6 Flow Label value. This object need not be present in rows where tunnelIfAddressType indicates the tunnel is not over IPv6. A value of -1 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB. Any other value indicates that the Flow Label field is set to the indicated value.')
tunnelIfAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 8), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfAddressType.setStatus('current')
if mibBuilder.loadTexts: tunnelIfAddressType.setDescription('The type of address in the corresponding tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress objects.')
tunnelIfLocalInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfLocalInetAddress.setStatus('current')
if mibBuilder.loadTexts: tunnelIfLocalInetAddress.setDescription('The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header). If the address is unknown, the value is 0.0.0.0 for IPv4 or :: for IPv6. The type of this object is given by tunnelIfAddressType.')
tunnelIfRemoteInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfRemoteInetAddress.setStatus('current')
if mibBuilder.loadTexts: tunnelIfRemoteInetAddress.setDescription('The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header). If the address is unknown or the tunnel is not a point-to-point link (e.g., if it is a 6to4 tunnel), the value is 0.0.0.0 for tunnels over IPv4 or :: for tunnels over IPv6. The type of this object is given by tunnelIfAddressType.')
tunnelIfEncapsLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfEncapsLimit.setReference('RFC 2473, section 4.1.1')
if mibBuilder.loadTexts: tunnelIfEncapsLimit.setStatus('current')
if mibBuilder.loadTexts: tunnelIfEncapsLimit.setDescription('The maximum number of additional encapsulations permitted for packets undergoing encapsulation at this node. A value of -1 indicates that no limit is present (except as a result of the packet size).')
tunnelConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2), )
if mibBuilder.loadTexts: tunnelConfigTable.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigTable.setDescription('The (conceptual) table containing information on configured tunnels. This table can be used to map a set of tunnel endpoints to the associated ifIndex value. It can also be used for row creation. Note that every row in the tunnelIfTable with a fixed IPv4 destination address should have a corresponding row in the tunnelConfigTable, regardless of whether it was created via SNMP. Since this table does not support IPv6, it is deprecated in favor of tunnelInetConfigTable.')
tunnelConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1), ).setIndexNames((0, "TUNNEL-MIB", "tunnelConfigLocalAddress"), (0, "TUNNEL-MIB", "tunnelConfigRemoteAddress"), (0, "TUNNEL-MIB", "tunnelConfigEncapsMethod"), (0, "TUNNEL-MIB", "tunnelConfigID"))
if mibBuilder.loadTexts: tunnelConfigEntry.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigEntry.setDescription('An entry (conceptual row) containing the information on a particular configured tunnel. Since this entry does not support IPv6, it is deprecated in favor of tunnelInetConfigEntry.')
tunnelConfigLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: tunnelConfigLocalAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigLocalAddress.setDescription('The address of the local endpoint of the tunnel, or 0.0.0.0 if the device is free to choose any of its addresses at tunnel establishment time. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigLocalAddress.')
tunnelConfigRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: tunnelConfigRemoteAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigRemoteAddress.setDescription('The address of the remote endpoint of the tunnel. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigRemoteAddress.')
tunnelConfigEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 3), IANAtunnelType())
if mibBuilder.loadTexts: tunnelConfigEncapsMethod.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigEncapsMethod.setDescription('The encapsulation method used by the tunnel. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigEncapsMethod.')
tunnelConfigID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: tunnelConfigID.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigID.setDescription('An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints. If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP-in-IP), the value of this object is 1. For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not conflict with an existing row, such as choosing a random number. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigID.')
tunnelConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelConfigIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigIfIndex.setDescription('If the value of tunnelConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface. A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigIfIndex.')
tunnelConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelConfigStatus.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelConfigStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table. The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active. To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelConfigID of 1, and set tunnelConfigStatus to createAndGo. For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo-random number to use as the tunnelConfigID and set tunnelConfigStatus to createAndGo. In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo-random number and retry the operation. Creating a row in this table will cause an interface index to be assigned by the agent in an implementation-dependent manner, and corresponding rows will be instantiated in the ifTable and the tunnelIfTable. The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up. Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable. Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigStatus.')
tunnelInetConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3), )
if mibBuilder.loadTexts: tunnelInetConfigTable.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigTable.setDescription('The (conceptual) table containing information on configured tunnels. This table can be used to map a set of tunnel endpoints to the associated ifIndex value. It can also be used for row creation. Note that every row in the tunnelIfTable with a fixed destination address should have a corresponding row in the tunnelInetConfigTable, regardless of whether it was created via SNMP.')
tunnelInetConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1), ).setIndexNames((0, "TUNNEL-MIB", "tunnelInetConfigAddressType"), (0, "TUNNEL-MIB", "tunnelInetConfigLocalAddress"), (0, "TUNNEL-MIB", "tunnelInetConfigRemoteAddress"), (0, "TUNNEL-MIB", "tunnelInetConfigEncapsMethod"), (0, "TUNNEL-MIB", "tunnelInetConfigID"))
if mibBuilder.loadTexts: tunnelInetConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigEntry.setDescription('An entry (conceptual row) containing the information on a particular configured tunnel. Note that there is a 128 subid maximum for object OIDs. Implementers need to be aware that if the total number of octets in tunnelInetConfigLocalAddress and tunnelInetConfigRemoteAddress exceeds 110 then OIDs of column instances in this table will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3. In practice this is not expected to be a problem since IPv4 and IPv6 addresses will not cause the limit to be reached, but if other types are supported by an agent, care must be taken to ensure that the sum of the lengths do not cause the limit to be exceeded.')
tunnelInetConfigAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tunnelInetConfigAddressType.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigAddressType.setDescription('The address type over which the tunnel encapsulates packets.')
tunnelInetConfigLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: tunnelInetConfigLocalAddress.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigLocalAddress.setDescription('The address of the local endpoint of the tunnel, or 0.0.0.0 (for IPv4) or :: (for IPv6) if the device is free to choose any of its addresses at tunnel establishment time.')
tunnelInetConfigRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 3), InetAddress())
if mibBuilder.loadTexts: tunnelInetConfigRemoteAddress.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigRemoteAddress.setDescription('The address of the remote endpoint of the tunnel.')
tunnelInetConfigEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 4), IANAtunnelType())
if mibBuilder.loadTexts: tunnelInetConfigEncapsMethod.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigEncapsMethod.setDescription('The encapsulation method used by the tunnel.')
tunnelInetConfigID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: tunnelInetConfigID.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigID.setDescription('An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints. If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP-in-IP), the value of this object is 1. For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not conflict with an existing row, such as choosing a random number.')
tunnelInetConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInetConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigIfIndex.setDescription('If the value of tunnelInetConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface. A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned.')
tunnelInetConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelInetConfigStatus.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table. The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active. To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelInetConfigID of 1, and set tunnelInetConfigStatus to createAndGo. For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo-random number to use as the tunnelInetConfigID and set tunnelInetConfigStatus to createAndGo. In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo-random number and retry the operation. Creating a row in this table will cause an interface index to be assigned by the agent in an implementation-dependent manner, and corresponding rows will be instantiated in the ifTable and the tunnelIfTable. The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up. Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable.')
tunnelInetConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelInetConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: tunnelInetConfigStorageType.setDescription('The storage type of this row. If the row is permanent(4), no objects in the row need be writable.')
tunnelMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2))
tunnelMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2, 1))
tunnelMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2, 2))
tunnelMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 1)).setObjects(("TUNNEL-MIB", "tunnelMIBBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tunnelMIBCompliance = tunnelMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelMIBCompliance.setDescription('The (deprecated) IPv4-only compliance statement for the IP Tunnel MIB. This is deprecated in favor of tunnelMIBInetFullCompliance and tunnelMIBInetReadOnlyCompliance.')
tunnelMIBInetFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 2)).setObjects(("TUNNEL-MIB", "tunnelMIBInetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tunnelMIBInetFullCompliance = tunnelMIBInetFullCompliance.setStatus('current')
if mibBuilder.loadTexts: tunnelMIBInetFullCompliance.setDescription('The full compliance statement for the IP Tunnel MIB.')
tunnelMIBInetReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 3)).setObjects(("TUNNEL-MIB", "tunnelMIBInetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tunnelMIBInetReadOnlyCompliance = tunnelMIBInetReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: tunnelMIBInetReadOnlyCompliance.setDescription('The read-only compliance statement for the IP Tunnel MIB.')
tunnelMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 1)).setObjects(("TUNNEL-MIB", "tunnelIfLocalAddress"), ("TUNNEL-MIB", "tunnelIfRemoteAddress"), ("TUNNEL-MIB", "tunnelIfEncapsMethod"), ("TUNNEL-MIB", "tunnelIfHopLimit"), ("TUNNEL-MIB", "tunnelIfTOS"), ("TUNNEL-MIB", "tunnelIfSecurity"), ("TUNNEL-MIB", "tunnelConfigIfIndex"), ("TUNNEL-MIB", "tunnelConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tunnelMIBBasicGroup = tunnelMIBBasicGroup.setStatus('deprecated')
if mibBuilder.loadTexts: tunnelMIBBasicGroup.setDescription('A collection of objects to support basic management of IPv4 Tunnels. Since this group cannot support IPv6, it is deprecated in favor of tunnelMIBInetGroup.')
tunnelMIBInetGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 2)).setObjects(("TUNNEL-MIB", "tunnelIfAddressType"), ("TUNNEL-MIB", "tunnelIfLocalInetAddress"), ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"), ("TUNNEL-MIB", "tunnelIfEncapsMethod"), ("TUNNEL-MIB", "tunnelIfEncapsLimit"), ("TUNNEL-MIB", "tunnelIfHopLimit"), ("TUNNEL-MIB", "tunnelIfTOS"), ("TUNNEL-MIB", "tunnelIfFlowLabel"), ("TUNNEL-MIB", "tunnelIfSecurity"), ("TUNNEL-MIB", "tunnelInetConfigIfIndex"), ("TUNNEL-MIB", "tunnelInetConfigStatus"), ("TUNNEL-MIB", "tunnelInetConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tunnelMIBInetGroup = tunnelMIBInetGroup.setStatus('current')
if mibBuilder.loadTexts: tunnelMIBInetGroup.setDescription('A collection of objects to support basic management of IPv4 and IPv6 Tunnels.')
mibBuilder.exportSymbols("TUNNEL-MIB", tunnelInetConfigTable=tunnelInetConfigTable, tunnelConfigID=tunnelConfigID, tunnelConfigStatus=tunnelConfigStatus, tunnelInetConfigEncapsMethod=tunnelInetConfigEncapsMethod, tunnelInetConfigIfIndex=tunnelInetConfigIfIndex, tunnelIfHopLimit=tunnelIfHopLimit, tunnelInetConfigStatus=tunnelInetConfigStatus, tunnelIfAddressType=tunnelIfAddressType, tunnelIfRemoteInetAddress=tunnelIfRemoteInetAddress, tunnelIfRemoteAddress=tunnelIfRemoteAddress, tunnelConfigLocalAddress=tunnelConfigLocalAddress, tunnelInetConfigID=tunnelInetConfigID, tunnelMIBObjects=tunnelMIBObjects, tunnelInetConfigAddressType=tunnelInetConfigAddressType, PYSNMP_MODULE_ID=tunnelMIB, tunnelMIBCompliance=tunnelMIBCompliance, tunnelMIBGroups=tunnelMIBGroups, tunnelInetConfigStorageType=tunnelInetConfigStorageType, tunnel=tunnel, tunnelMIB=tunnelMIB, tunnelInetConfigRemoteAddress=tunnelInetConfigRemoteAddress, tunnelIfSecurity=tunnelIfSecurity, tunnelMIBInetReadOnlyCompliance=tunnelMIBInetReadOnlyCompliance, tunnelIfTOS=tunnelIfTOS, tunnelMIBConformance=tunnelMIBConformance, tunnelConfigRemoteAddress=tunnelConfigRemoteAddress, tunnelConfigTable=tunnelConfigTable, tunnelIfLocalInetAddress=tunnelIfLocalInetAddress, tunnelMIBCompliances=tunnelMIBCompliances, tunnelConfigIfIndex=tunnelConfigIfIndex, tunnelMIBBasicGroup=tunnelMIBBasicGroup, tunnelIfEntry=tunnelIfEntry, tunnelInetConfigLocalAddress=tunnelInetConfigLocalAddress, tunnelIfLocalAddress=tunnelIfLocalAddress, tunnelIfEncapsLimit=tunnelIfEncapsLimit, tunnelConfigEncapsMethod=tunnelConfigEncapsMethod, tunnelInetConfigEntry=tunnelInetConfigEntry, tunnelIfFlowLabel=tunnelIfFlowLabel, tunnelMIBInetFullCompliance=tunnelMIBInetFullCompliance, tunnelIfTable=tunnelIfTable, tunnelIfEncapsMethod=tunnelIfEncapsMethod, tunnelMIBInetGroup=tunnelMIBInetGroup, tunnelConfigEntry=tunnelConfigEntry)
