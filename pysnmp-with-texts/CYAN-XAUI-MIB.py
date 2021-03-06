#
# PySNMP MIB module CYAN-XAUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-XAUI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanAdminStateTc, CyanOpStateTc, CyanSecServiceStateTc, CyanOpStateQualTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanAdminStateTc", "CyanOpStateTc", "CyanSecServiceStateTc", "CyanOpStateQualTc")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, Integer32, Bits, Unsigned32, TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Integer32", "Bits", "Unsigned32", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanXauiModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170))
cyanXauiModule.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanXauiModule.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanXauiModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanXauiModule.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanXauiModule.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanXauiModule.setDescription('MIB module for Transport XAUI')
cyanXauiMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1))
cyanXauiTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1), )
if mibBuilder.loadTexts: cyanXauiTable.setStatus('current')
if mibBuilder.loadTexts: cyanXauiTable.setDescription('A list of Xaui entries.')
cyanXauiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1), ).setIndexNames((0, "CYAN-XAUI-MIB", "cyanXauiShelfId"), (0, "CYAN-XAUI-MIB", "cyanXauiModuleId"), (0, "CYAN-XAUI-MIB", "cyanXauiXauiId"))
if mibBuilder.loadTexts: cyanXauiEntry.setStatus('current')
if mibBuilder.loadTexts: cyanXauiEntry.setDescription('An entry of Xaui.')
cyanXauiShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanXauiShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanXauiShelfId.setDescription('Shelf Id')
cyanXauiModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanXauiModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanXauiModuleId.setDescription('Module Id')
cyanXauiXauiId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanXauiXauiId.setStatus('current')
if mibBuilder.loadTexts: cyanXauiXauiId.setDescription('Xaui Id')
cyanXauiAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiAdminState.setStatus('current')
if mibBuilder.loadTexts: cyanXauiAdminState.setDescription('Administrative state')
cyanXauiAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiAutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanXauiAutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanXauiOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 6), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiOperState.setStatus('current')
if mibBuilder.loadTexts: cyanXauiOperState.setDescription('Primary Operation State')
cyanXauiOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 7), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiOperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanXauiOperStateQual.setDescription('Operation state qualifier')
cyanXauiPortSpeedMbps = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiPortSpeedMbps.setStatus('current')
if mibBuilder.loadTexts: cyanXauiPortSpeedMbps.setDescription('Operating speed')
cyanXauiSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 9), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanXauiSecServState.setStatus('current')
if mibBuilder.loadTexts: cyanXauiSecServState.setDescription('Secondary service state')
cyanXauiObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 20)).setObjects(("CYAN-XAUI-MIB", "cyanXauiAdminState"), ("CYAN-XAUI-MIB", "cyanXauiAutoinserviceSoakTimeSec"), ("CYAN-XAUI-MIB", "cyanXauiOperState"), ("CYAN-XAUI-MIB", "cyanXauiOperStateQual"), ("CYAN-XAUI-MIB", "cyanXauiPortSpeedMbps"), ("CYAN-XAUI-MIB", "cyanXauiSecServState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanXauiObjectGroup = cyanXauiObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanXauiObjectGroup.setDescription('Group of objects that comes with Xaui module')
cyanXauiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 30)).setObjects(("CYAN-XAUI-MIB", "cyanXauiObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanXauiCompliance = cyanXauiCompliance.setStatus('current')
if mibBuilder.loadTexts: cyanXauiCompliance.setDescription('The basic info needed to be a cyan Xaui')
mibBuilder.exportSymbols("CYAN-XAUI-MIB", PYSNMP_MODULE_ID=cyanXauiModule, cyanXauiAutoinserviceSoakTimeSec=cyanXauiAutoinserviceSoakTimeSec, cyanXauiTable=cyanXauiTable, cyanXauiSecServState=cyanXauiSecServState, cyanXauiPortSpeedMbps=cyanXauiPortSpeedMbps, cyanXauiModule=cyanXauiModule, cyanXauiModuleId=cyanXauiModuleId, cyanXauiCompliance=cyanXauiCompliance, cyanXauiXauiId=cyanXauiXauiId, cyanXauiObjectGroup=cyanXauiObjectGroup, cyanXauiOperStateQual=cyanXauiOperStateQual, cyanXauiShelfId=cyanXauiShelfId, cyanXauiAdminState=cyanXauiAdminState, cyanXauiMibObjects=cyanXauiMibObjects, cyanXauiEntry=cyanXauiEntry, cyanXauiOperState=cyanXauiOperState)
