#
# PySNMP MIB module OG-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OG-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:23:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ogModules, ogProducts = mibBuilder.importSymbols("OG-SMI-MIB", "ogModules", "ogProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, Counter64, NotificationType, iso, IpAddress, Gauge32, TimeTicks, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter64", "NotificationType", "iso", "IpAddress", "Gauge32", "TimeTicks", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 11, 2))
ogProductsMib.setRevisions(('2016-02-10 00:00', '2015-06-02 00:00', '2013-08-11 00:00', '2011-08-15 01:23', '2010-04-15 11:27',))
if mibBuilder.loadTexts: ogProductsMib.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: ogProductsMib.setOrganization('Opengear Inc.')
ogCM4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 1))
ogCM4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 2))
ogCM4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 3))
ogCM41xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 10))
ogCM71xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 11))
ogSD4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 20))
ogSD4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 21))
ogSD4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 22))
ogSD4001DW = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 23))
ogSD4002DX = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 24))
ogCD = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 30))
ogCMx86 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 31))
ogCMS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 40))
ogLighthouse = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 41))
ogIM4004 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 50))
ogIM42xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 60))
ogIM72xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 61))
ogKCS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 70))
ogACM500x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 80))
ogACM550x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 81))
ogACM700x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 90))
ogACM70045 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 91))
mibBuilder.exportSymbols("OG-PRODUCTS-MIB", ogACM500x=ogACM500x, ogKCS61xx=ogKCS61xx, ogACM550x=ogACM550x, ogLighthouse=ogLighthouse, ogSD4001DW=ogSD4001DW, PYSNMP_MODULE_ID=ogProductsMib, ogSD4001=ogSD4001, ogCM4001=ogCM4001, ogCMS61xx=ogCMS61xx, ogCD=ogCD, ogIM42xx=ogIM42xx, ogCM4002=ogCM4002, ogIM4004=ogIM4004, ogCM71xx=ogCM71xx, ogIM72xx=ogIM72xx, ogSD4002=ogSD4002, ogProductsMib=ogProductsMib, ogACM700x=ogACM700x, ogSD4002DX=ogSD4002DX, ogACM70045=ogACM70045, ogSD4008=ogSD4008, ogCM4008=ogCM4008, ogCM41xx=ogCM41xx, ogCMx86=ogCMx86)