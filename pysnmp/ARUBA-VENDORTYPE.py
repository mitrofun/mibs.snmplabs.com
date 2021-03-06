#
# PySNMP MIB module ARUBA-VENDORTYPE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARUBA-VENDORTYPE
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
arubaMIBModules, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMIBModules")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, NotificationType, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
arubaVendorTypeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1))
arubaVendorTypeMIB.setRevisions(('2012-08-27 00:00',))
if mibBuilder.loadTexts: arubaVendorTypeMIB.setLastUpdated('201208270000Z')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setOrganization('Aruba Wireless Networks')
arubaVendorTypeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1))
arubaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1))
aSystemUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 1))
aSystemChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 2))
aSystemBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 3))
aSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 4))
aSystemPSU = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 5))
aSystemFAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 6))
aSystemContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 7))
aSystemPort = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 8))
aSystemSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 9))
mibBuilder.exportSymbols("ARUBA-VENDORTYPE", aSystemSensor=aSystemSensor, aSystemBackplane=aSystemBackplane, aSystemContainer=aSystemContainer, arubaSystem=arubaSystem, arubaVendorTypeMIB=arubaVendorTypeMIB, PYSNMP_MODULE_ID=arubaVendorTypeMIB, aSystemFAN=aSystemFAN, aSystemPort=aSystemPort, aSystemUnknown=aSystemUnknown, aSystemPSU=aSystemPSU, aSystemChassis=aSystemChassis, aSystemModule=aSystemModule, arubaVendorTypeMIBObjects=arubaVendorTypeMIBObjects)
