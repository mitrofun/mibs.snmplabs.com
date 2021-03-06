#
# PySNMP MIB module JUNIPER-IPFORWARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-IPFORWARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
inetCidrRouteEntry, ipCidrRouteEntry = mibBuilder.importSymbols("IP-FORWARD-MIB", "inetCidrRouteEntry", "ipCidrRouteEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Unsigned32, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Unsigned32", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxIpForwardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 38))
jnxIpForwardMIB.setRevisions(('2011-11-13 00:00',))
if mibBuilder.loadTexts: jnxIpForwardMIB.setLastUpdated('201111130000Z')
if mibBuilder.loadTexts: jnxIpForwardMIB.setOrganization('Juniper Networks, Inc.')
jnxIpCidrRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 38, 1), )
if mibBuilder.loadTexts: jnxIpCidrRouteTable.setStatus('deprecated')
jnxIpCidrRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1), )
ipCidrRouteEntry.registerAugmentions(("JUNIPER-IPFORWARD-MIB", "jnxIpCidrRouteEntry"))
jnxIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
if mibBuilder.loadTexts: jnxIpCidrRouteEntry.setStatus('deprecated')
jnxIpCidrRouteTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpCidrRouteTunnelName.setStatus('deprecated')
jnxInetCidrRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 38, 2), )
if mibBuilder.loadTexts: jnxInetCidrRouteTable.setStatus('current')
jnxInetCidrRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1), )
inetCidrRouteEntry.registerAugmentions(("JUNIPER-IPFORWARD-MIB", "jnxInetCidrRouteEntry"))
jnxInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
if mibBuilder.loadTexts: jnxInetCidrRouteEntry.setStatus('current')
jnxInetCidrRouteTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxInetCidrRouteTunnelName.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-IPFORWARD-MIB", PYSNMP_MODULE_ID=jnxIpForwardMIB, jnxIpForwardMIB=jnxIpForwardMIB, jnxIpCidrRouteEntry=jnxIpCidrRouteEntry, jnxIpCidrRouteTable=jnxIpCidrRouteTable, jnxIpCidrRouteTunnelName=jnxIpCidrRouteTunnelName, jnxInetCidrRouteTunnelName=jnxInetCidrRouteTunnelName, jnxInetCidrRouteTable=jnxInetCidrRouteTable, jnxInetCidrRouteEntry=jnxInetCidrRouteEntry)
