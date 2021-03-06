#
# PySNMP MIB module MITEL-IPLOGICAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPLOGICAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Bits, IpAddress, Counter64, enterprises, Gauge32, Integer32, Unsigned32, NotificationType, MibIdentifier, Counter32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Bits", "IpAddress", "Counter64", "enterprises", "Gauge32", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
mitelIpGrpLogicalGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5))
mitelIpGrpLogicalGroup.setRevisions(('2003-03-24 09:13', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setRevisionsDescriptions(('Convert to SMIv2', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setLastUpdated('200303240913Z')
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelIpLogGrpLogicalTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1), )
if mibBuilder.loadTexts: mitelIpLogGrpLogicalTable.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogGrpLogicalTable.setDescription('A table containing information about logical IP LAN destinations.')
mitelIpLogGrpLogicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIpLogGrpLogicalEntry.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogGrpLogicalEntry.setDescription('Each entry of this table contains information about a specific logical interface to a local area network. Each logical LAN can support routing or bridging functions, these are considered virtual interfaces.')
mitelIpLogAdvertisementAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogAdvertisementAddress.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogAdvertisementAddress.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogAdvertisementAddress.setDescription('The IP destination address to be used for multicast Router Advertisements sent from the interface. The only permissible values are the all-systems multicast address, 224.0.0.1, or the limited-broadcast address, 255.255.255.255. (The all-systems address is preferred wherever possible, i.e., on any link where all listening hosts support IP multicast.) Default Value is 224.0.0.1')
mitelIpLogMaxAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 1800)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogMaxAdvertisementInterval.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogMaxAdvertisementInterval.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogMaxAdvertisementInterval.setDescription('The maximum time allowed between sending multicast Router Advertisements from the interface, in seconds.')
mitelIpLogMinAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1800)).clone(450)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogMinAdvertisementInterval.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogMinAdvertisementInterval.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogMinAdvertisementInterval.setDescription('The minimum time allowed between sending unsolicited multicast Router Advertisements from the interface, in seconds. Must be no greater than grIpLMaxAdvertisementInterval.')
mitelIpLogAdvertisementLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 9000)).clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogAdvertisementLifetime.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogAdvertisementLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogAdvertisementLifetime.setDescription('The value to be placed in the Lifetime field of Router Advertisements sent from the interface, in seconds. Must be no less than grIpLMaxAdvertisementInterval.')
mitelIpLogPerformRouterDiscovery = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogPerformRouterDiscovery.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogPerformRouterDiscovery.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogPerformRouterDiscovery.setDescription('A flag indicating whether or not the host is to perform ICMP router discovery on the interface.')
mitelIpLogSolicitationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogSolicitationAddress.setReference('ICMP Router Discovery Messages (RFC 1256).')
if mibBuilder.loadTexts: mitelIpLogSolicitationAddress.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogSolicitationAddress.setDescription('The IP destination address to be used for sending Router Solicitations from the interface. The only permissible values are the all-routers multicast address, 224.0.0.2, or the limited-broadcast address, 255.255.255.255. (The all-routers address is preferred wherever possible, i.e., on any link where all advertising routers support IP multicast.) Default 224.0.0.2')
mitelIpLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIpLogStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelIpLogStatus.setStatus('current')
if mibBuilder.loadTexts: mitelIpLogStatus.setDescription('The current status of this entry.')
mibBuilder.exportSymbols("MITEL-IPLOGICAL-MIB", mitelProprietary=mitelProprietary, mitelIpLogAdvertisementAddress=mitelIpLogAdvertisementAddress, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup, PYSNMP_MODULE_ID=mitelIpGrpLogicalGroup, mitelIpLogSolicitationAddress=mitelIpLogSolicitationAddress, mitelIpLogMinAdvertisementInterval=mitelIpLogMinAdvertisementInterval, mitelIpLogGrpLogicalEntry=mitelIpLogGrpLogicalEntry, mitelIpLogStatus=mitelIpLogStatus, mitelIpLogMaxAdvertisementInterval=mitelIpLogMaxAdvertisementInterval, mitel=mitel, mitelIpNetRouter=mitelIpNetRouter, mitelIpLogGrpLogicalTable=mitelIpLogGrpLogicalTable, mitelIpLogPerformRouterDiscovery=mitelIpLogPerformRouterDiscovery, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpLogAdvertisementLifetime=mitelIpLogAdvertisementLifetime)
