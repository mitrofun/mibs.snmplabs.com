#
# PySNMP MIB module EX02-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EX02-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, Counter64, IpAddress, Bits, Gauge32, Unsigned32, Counter32, iso, ModuleIdentity, Integer32, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "IpAddress", "Bits", "Gauge32", "Unsigned32", "Counter32", "iso", "ModuleIdentity", "Integer32", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ex01Module = ModuleIdentity((1, 3, 6, 1, 3, 1194))
if mibBuilder.loadTexts: ex01Module.setLastUpdated('9602010000Z')
if mibBuilder.loadTexts: ex01Module.setOrganization('MIB Testers')
if mibBuilder.loadTexts: ex01Module.setContactInfo(' Dave Perkins Email: dperkins@scruznet.com')
if mibBuilder.loadTexts: ex01Module.setDescription('Test MIB module to show valid SMI constructs which are not valid in ASN.1.')
ex01Test = MibIdentifier((1, 3, 6, 1, 3, 1195))
aTable = MibTable((1, 3, 6, 1, 3, 1195, 1), )
if mibBuilder.loadTexts: aTable.setStatus('current')
if mibBuilder.loadTexts: aTable.setDescription('An example table.')
aEntry = MibTableRow((1, 3, 6, 1, 3, 1195, 1, 1), ).setIndexNames((0, "EX02-MIB", "aIndex"))
if mibBuilder.loadTexts: aEntry.setStatus('current')
if mibBuilder.loadTexts: aEntry.setDescription('An entry in the example table.')
aIndex = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red", 1), ("green", 2), ("blue", 3))))
if mibBuilder.loadTexts: aIndex.setStatus('current')
if mibBuilder.loadTexts: aIndex.setDescription('Index for table.')
aOct1 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone('a default value')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aOct1.setStatus('current')
if mibBuilder.loadTexts: aOct1.setDescription('An example object with OCTET STRING syntax.')
aOct2 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="0a23bc")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aOct2.setStatus('current')
if mibBuilder.loadTexts: aOct2.setDescription('An example object with OCTET STRING syntax.')
aInt1 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aInt1.setStatus('current')
if mibBuilder.loadTexts: aInt1.setDescription('An example object with Integer32 syntax.')
oG = ObjectGroup((1, 3, 6, 1, 3, 1194, 1)).setObjects(("EX02-MIB", "aOct1"), ("EX02-MIB", "aOct2"), ("EX02-MIB", "aInt1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oG = oG.setStatus('current')
if mibBuilder.loadTexts: oG.setDescription('Group for objects.')
mibBuilder.exportSymbols("EX02-MIB", PYSNMP_MODULE_ID=ex01Module, aIndex=aIndex, aInt1=aInt1, oG=oG, aTable=aTable, aEntry=aEntry, aOct2=aOct2, ex01Module=ex01Module, ex01Test=ex01Test, aOct1=aOct1)
