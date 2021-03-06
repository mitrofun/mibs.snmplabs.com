#
# PySNMP MIB module DELL-NETWORKING-FIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-FIB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:37:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Integer32, Counter64, iso, Unsigned32, Gauge32, ModuleIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Integer32", "Counter64", "iso", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
dellNetIpForwardMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 9))
dellNetIpForwardMib.setRevisions(('2011-07-08 12:00', '2007-09-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dellNetIpForwardMib.setRevisionsDescriptions(('This version of MIB module deprecates the dellNetIpForwardTable and replaces it with dellNetInetCidrRouteTable which adds the IP Protocol Independance ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: dellNetIpForwardMib.setLastUpdated('200709141200Z')
if mibBuilder.loadTexts: dellNetIpForwardMib.setOrganization('Dell Inc')
if mibBuilder.loadTexts: dellNetIpForwardMib.setContactInfo('http://www.dell.com/support')
if mibBuilder.loadTexts: dellNetIpForwardMib.setDescription('This MIB module is used to display CIDR multipath IP Routes.')
dellNetIpForwardMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1))
dellNetIpForwardMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 9, 2))
dellNetIpForwardVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 9, 3))
chSysCardNumber = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 9, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCardNumber.setStatus('current')
if mibBuilder.loadTexts: chSysCardNumber.setDescription('This is the card number assigned to the line cards and the RPM cards in the chassis. The line cards number are from 0 to 13 and the RPM are from 0 to 1.')
dellNetIpForwardVersionTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1), )
if mibBuilder.loadTexts: dellNetIpForwardVersionTable.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardVersionTable.setDescription("This entity's IP forward version table.")
dellNetIpForwardVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1), ).setIndexNames((0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpForwardAddrFamily"))
if mibBuilder.loadTexts: dellNetIpForwardVersionEntry.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardVersionEntry.setDescription('The row definition for the ip forward version Table.')
dellNetIpForwardAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: dellNetIpForwardAddrFamily.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardAddrFamily.setDescription('Address Family of the IP Forwarding Table for which this entry provides the Version information. ')
dellNetIpForwardVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpForwardVersion.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardVersion.setDescription('A version number on the Forwarding Table. This is always fetched from one line card.')
dellNetIpForwardTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2), )
if mibBuilder.loadTexts: dellNetIpForwardTable.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpForwardTable.setDescription("This entity's IP Routing table.")
dellNetIpForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1), ).setIndexNames((0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardDest"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardMask"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardNextHop"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardFirstHop"))
if mibBuilder.loadTexts: dellNetIpForwardEntry.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpForwardEntry.setDescription('A particular route to a particular destination, under a particular policy.')
dellNetIpforwardDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardDest.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardDest.setDescription('The destination IP address of this route. An entry with a value of 0.0.0.0 is considered a default route.')
dellNetIpforwardMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardMask.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the dellNetIpforwardDest field.')
dellNetIpforwardNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardNextHop.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardNextHop.setDescription('On remote routes, the address of the next system en route; Otherwise, 0.0.0.0.')
dellNetIpforwardFirstHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardFirstHop.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardFirstHop.setDescription('On remote routes, the address of the Gateway to the nexthop; 0.0.0.0 if the Nexthop itself is a Gateway to the Destination')
dellNetIpforwardIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardIfIndex.setDescription('The ifIndex value which identifies the local interface through which the next hop of this route should be reached.')
dellNetIpforwardMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardMacAddress.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardMacAddress.setDescription('The Mac address of the NextHop.')
dellNetIpforwardEgressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardEgressPort.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardEgressPort.setDescription('The name of the egress port to which the packets will be forwarded.')
dellNetIpforwardCamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetIpforwardCamIndex.setStatus('deprecated')
if mibBuilder.loadTexts: dellNetIpforwardCamIndex.setDescription('Cam Entry corresponding to a row.')
dellNetInetCidrIpv4RouteNumber = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrIpv4RouteNumber.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrIpv4RouteNumber.setDescription('The number of current dellNetInetCidrRouteTable entries that are not Invalid and whose dellNetInetCidrRouteDestType is ipv4(1)')
dellNetInetCidrIpv6RouteNumber = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrIpv6RouteNumber.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrIpv6RouteNumber.setDescription('The number of current dellNetInetCidrRouteTable entries that are not Invalid and whose dellNetInetCidrRouteDestType is ipv6(2)')
dellNetInetCidrRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5), )
if mibBuilder.loadTexts: dellNetInetCidrRouteTable.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteTable.setDescription("This entity's IP Routing table.")
dellNetInetCidrRouteTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1), ).setIndexNames((0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteDestType"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteDest"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRoutePfxLen"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteNextHopType"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteNextHop"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteFirstHopType"), (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteFirstHop"))
if mibBuilder.loadTexts: dellNetInetCidrRouteTableEntry.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteTableEntry.setDescription('A particular route to a particular destination Implementers need to be aware that if the total number of elements (octets or sub-identifiers) in inetCidrRouteDest, inetCidrRoutePolicy, and inetCidrRouteNextHop exceeds 111, then OIDs of column instances in this table will have more than 128 sub- identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3. For S-Series Platform, Value of chSysCardNumber will always be zero')
dellNetInetCidrRouteDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: dellNetInetCidrRouteDestType.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteDestType.setDescription('The type of the inetCidrRouteDest address, as defined in the InetAddress MIB. Only those address types that may appear in an actual routing table are allowed as values of this object.')
dellNetInetCidrRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 2), InetAddress())
if mibBuilder.loadTexts: dellNetInetCidrRouteDest.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteDest.setDescription('The destination IP address of this route. The type of this address is determined by the value of the inetCidrRouteDestType object.')
dellNetInetCidrRoutePfxLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: dellNetInetCidrRoutePfxLen.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRoutePfxLen.setDescription('Indicates the number of leading one bits that form the mask to be logical-ANDed with the destination address before being compared to the value in the inetCidrRouteDest field.')
dellNetInetCidrRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 4), InetAddressType())
if mibBuilder.loadTexts: dellNetInetCidrRouteNextHopType.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteNextHopType.setDescription('The type of the inetCidrRouteNextHop address, as defined in the InetAddress MIB. Value should be set to unknown(0) for non-remote routes. Only those address types that may appear in an actual routing table are allowed as values of this object.')
dellNetInetCidrRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 5), InetAddress())
if mibBuilder.loadTexts: dellNetInetCidrRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteNextHop.setDescription('On remote routes, the address of the next system en route. For non-remote routes, a zero length string. The type of this address is determined by the value of the inetCidrRouteNextHopType object.')
dellNetInetCidrRouteFirstHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 6), InetAddressType())
if mibBuilder.loadTexts: dellNetInetCidrRouteFirstHopType.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteFirstHopType.setDescription('The type of the inetCidrRouteFirstHop address, as defined in the InetAddress MIB. Value should be set to unknown(0) for non-remote routes. Only those address types that may appear in an actual routing table are allowed as values of this object.')
dellNetInetCidrRouteFirstHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 7), InetAddress())
if mibBuilder.loadTexts: dellNetInetCidrRouteFirstHop.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteFirstHop.setDescription('The address of the gateway to the Nexthop. If the nexthop itself is the gateway, a zero length string. The type of this address is determined by the value of the inetCidrRouteFirstHopType object.')
dellNetInetCidrRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrRouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteIfIndex.setDescription('The ifIndex value that identifies the local interface through which the next hop of this route should be reached. A value of 0 is valid and represents the scenario where no interface is specified.')
dellNetInetCidrRouteMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrRouteMacAddress.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteMacAddress.setDescription('The Mac address of the NextHop.')
dellNetInetCidrRouteEgressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrRouteEgressPort.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteEgressPort.setDescription('The name of the egress port to which the packets will be forwarded.')
dellNetInetCidrRouteCamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetInetCidrRouteCamIndex.setStatus('current')
if mibBuilder.loadTexts: dellNetInetCidrRouteCamIndex.setDescription('Cam Entry corresponding to a row.')
dellNetIpForwardMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1))
dellNetIpForwardMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2))
dellNetIpForwardMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1, 1)).setObjects(("DELL-NETWORKING-FIB-MIB", "dellNetIpForwardObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIpForwardMibCompliance = dellNetIpForwardMibCompliance.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardMibCompliance.setDescription('The basic implementation requirements for the Dell Networking OS Ip Forward MIB.')
dellNetIpForwardObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2, 1)).setObjects(("DELL-NETWORKING-FIB-MIB", "dellNetIpForwardVersion"), ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteIfIndex"), ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteMacAddress"), ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteEgressPort"), ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteCamIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetIpForwardObjectGroup = dellNetIpForwardObjectGroup.setStatus('current')
if mibBuilder.loadTexts: dellNetIpForwardObjectGroup.setDescription('Objects for the IP aware Route Table.')
mibBuilder.exportSymbols("DELL-NETWORKING-FIB-MIB", dellNetIpForwardMibGroups=dellNetIpForwardMibGroups, dellNetIpForwardEntry=dellNetIpForwardEntry, dellNetIpforwardDest=dellNetIpforwardDest, dellNetIpForwardObjectGroup=dellNetIpForwardObjectGroup, dellNetIpforwardCamIndex=dellNetIpforwardCamIndex, dellNetInetCidrIpv4RouteNumber=dellNetInetCidrIpv4RouteNumber, dellNetIpForwardMib=dellNetIpForwardMib, dellNetIpForwardMibCompliance=dellNetIpForwardMibCompliance, dellNetInetCidrRouteNextHopType=dellNetInetCidrRouteNextHopType, dellNetInetCidrRouteTableEntry=dellNetInetCidrRouteTableEntry, dellNetIpforwardIfIndex=dellNetIpforwardIfIndex, dellNetIpForwardVersionEntry=dellNetIpForwardVersionEntry, dellNetInetCidrRouteIfIndex=dellNetInetCidrRouteIfIndex, dellNetInetCidrRouteFirstHop=dellNetInetCidrRouteFirstHop, dellNetIpforwardEgressPort=dellNetIpforwardEgressPort, PYSNMP_MODULE_ID=dellNetIpForwardMib, dellNetIpForwardTable=dellNetIpForwardTable, dellNetInetCidrRouteEgressPort=dellNetInetCidrRouteEgressPort, dellNetInetCidrRouteCamIndex=dellNetInetCidrRouteCamIndex, dellNetInetCidrIpv6RouteNumber=dellNetInetCidrIpv6RouteNumber, chSysCardNumber=chSysCardNumber, dellNetInetCidrRouteTable=dellNetInetCidrRouteTable, dellNetIpForwardVersion=dellNetIpForwardVersion, dellNetInetCidrRouteNextHop=dellNetInetCidrRouteNextHop, dellNetInetCidrRouteMacAddress=dellNetInetCidrRouteMacAddress, dellNetIpforwardNextHop=dellNetIpforwardNextHop, dellNetIpForwardMibObjects=dellNetIpForwardMibObjects, dellNetIpforwardFirstHop=dellNetIpforwardFirstHop, dellNetInetCidrRouteFirstHopType=dellNetInetCidrRouteFirstHopType, dellNetInetCidrRouteDestType=dellNetInetCidrRouteDestType, dellNetInetCidrRouteDest=dellNetInetCidrRouteDest, dellNetIpForwardMibCompliances=dellNetIpForwardMibCompliances, dellNetIpForwardVariable=dellNetIpForwardVariable, dellNetIpforwardMacAddress=dellNetIpforwardMacAddress, dellNetInetCidrRoutePfxLen=dellNetInetCidrRoutePfxLen, dellNetIpForwardAddrFamily=dellNetIpForwardAddrFamily, dellNetIpforwardMask=dellNetIpforwardMask, dellNetIpForwardVersionTable=dellNetIpForwardVersionTable, dellNetIpForwardMibConformance=dellNetIpForwardMibConformance)
