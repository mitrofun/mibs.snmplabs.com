#
# PySNMP MIB module ZYXEL-L3-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-L3-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, MibIdentifier, Gauge32, TimeTicks, ObjectIdentity, IpAddress, Integer32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "ObjectIdentity", "IpAddress", "Integer32", "ModuleIdentity", "Unsigned32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelL3Ip = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40))
if mibBuilder.loadTexts: zyxelL3Ip.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelL3Ip.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelL3Ip.setContactInfo('')
if mibBuilder.loadTexts: zyxelL3Ip.setDescription('The subtree for layer 3 switch ip address')
zyxelLayer3IpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1))
zyLayer3IpDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDnsIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpDnsIpAddress.setDescription('Enter a domain name server IP address in order to be able to use a domain name instead of an IP address.')
zyLayer3IpDefaultMgmt = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inBand", 0), ("outOfBand", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDefaultMgmt.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpDefaultMgmt.setDescription('Specify which traffic flow (In-Band or Out-of-band) the switch is to send packets originating from it or packets with unknown source.')
zyLayer3IpDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpDefaultGateway.setDescription('IP address of the default outgoing gateway.')
zyLayer3IpInbandMaxNumberOfInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyLayer3IpInbandMaxNumberOfInterfaces.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpInbandMaxNumberOfInterfaces.setDescription('The maximum number of in-band IP that can be created.')
zyxelLayer3IpInbandTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5), )
if mibBuilder.loadTexts: zyxelLayer3IpInbandTable.setStatus('current')
if mibBuilder.loadTexts: zyxelLayer3IpInbandTable.setDescription('The table contains layer3 IP in-band configuration.')
zyxelLayer3IpInbandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1), ).setIndexNames((0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandIpAddress"), (0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandMask"))
if mibBuilder.loadTexts: zyxelLayer3IpInbandEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelLayer3IpInbandEntry.setDescription('An entry contains layer3 IP in-band configuration.')
zyLayer3IpInbandIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: zyLayer3IpInbandIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpInbandIpAddress.setDescription('Enter the IP address of your switch in dotted decimal notation, for example, 192.168.1.1. This is the IP address of the Switch in an IP routing domain.')
zyLayer3IpInbandMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: zyLayer3IpInbandMask.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpInbandMask.setDescription('Enter the IP subnet mask of an IP routing domain in dotted decimal notation, for example, 255.255.255.0.')
zyLayer3IpInbandVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpInbandVid.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpInbandVid.setDescription('Enter the VLAN identification number to which an IP routing domain belongs.')
zyLayer3IpInbandRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyLayer3IpInbandRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyLayer3IpInbandRowStatus.setDescription('This object allows entries to be created and deleted from the in-band IP table.')
mibBuilder.exportSymbols("ZYXEL-L3-IP-MIB", zyLayer3IpInbandVid=zyLayer3IpInbandVid, PYSNMP_MODULE_ID=zyxelL3Ip, zyxelLayer3IpSetup=zyxelLayer3IpSetup, zyxelL3Ip=zyxelL3Ip, zyLayer3IpDnsIpAddress=zyLayer3IpDnsIpAddress, zyLayer3IpInbandIpAddress=zyLayer3IpInbandIpAddress, zyLayer3IpDefaultGateway=zyLayer3IpDefaultGateway, zyLayer3IpInbandMaxNumberOfInterfaces=zyLayer3IpInbandMaxNumberOfInterfaces, zyxelLayer3IpInbandTable=zyxelLayer3IpInbandTable, zyLayer3IpDefaultMgmt=zyLayer3IpDefaultMgmt, zyLayer3IpInbandRowStatus=zyLayer3IpInbandRowStatus, zyxelLayer3IpInbandEntry=zyxelLayer3IpInbandEntry, zyLayer3IpInbandMask=zyLayer3IpInbandMask)
