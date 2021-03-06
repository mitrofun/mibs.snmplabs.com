#
# PySNMP MIB module CROSSBEAM-SYSTEMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CROSSBEAM-SYSTEMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Bits, NotificationType, iso, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, Unsigned32, IpAddress, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "NotificationType", "iso", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "Unsigned32", "IpAddress", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
crossbeamSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 6848))
cbsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1))
cbsMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2))
cbsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 3))
cbsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 4))
crossbeamSystemsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6848, 3, 1))
crossbeamSystemsMIB.setRevisions(('2003-05-09 00:00', '2002-03-15 00:00', '2004-03-10 00:00', '2004-05-10 00:00', '2004-07-07 00:00', '2005-08-22 00:00', '2005-10-25 00:00', '2006-02-07 00:00', '2010-04-14 00:00', '2010-06-17 00:00', '2010-08-10 00:00', '2010-08-11 00:00', '2010-10-08 00:00',))
if mibBuilder.loadTexts: crossbeamSystemsMIB.setLastUpdated('200203150000Z')
if mibBuilder.loadTexts: crossbeamSystemsMIB.setOrganization('Crossbeam Systems, Inc.')
cbsX40 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1))
cbsXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2))
cbsCSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3))
cbsXChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1))
cbsX45Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 1))
cbsX80Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 2))
cbsX60Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 3))
cbsX20Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 4))
cbsX30Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 5))
cbsX40Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 1))
cbsCChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1))
cbsC30Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 1))
cbsC10Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 2))
cbsC30iChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 3))
cbsC2Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 4))
cbsC6Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 5))
cbsC12Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 6))
cbsC25Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 7))
cbsX40Modules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2))
cbsCPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1))
cbsAPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2))
cbsNPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3))
cbsCPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 1))
cbsCPM8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 2))
cbsCPM8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 3))
cbsCPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 4))
cbsCPM9600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 5))
cbsAPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 1))
cbsAPM4200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 2))
cbsAPM4250 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 3))
cbsAPM8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 4))
cbsAPM8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 5))
cbsAPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 6))
cbsAPM8650 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 7))
cbsAPM9600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 8))
cbsAPM2030 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 9))
cbsNPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 1))
cbsNPM4110 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 2))
cbsNPM8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 3))
cbsNPM8210 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 4))
cbsNPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 5))
cbsNPM8650 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 6))
cbsNPM30 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 8))
cbsNPM8620 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 7))
cbsNPM20 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 9))
mibBuilder.exportSymbols("CROSSBEAM-SYSTEMS-MIB", cbsX40=cbsX40, PYSNMP_MODULE_ID=crossbeamSystemsMIB, cbsMgmt=cbsMgmt, cbsCChassis=cbsCChassis, cbsNPM8600=cbsNPM8600, crossbeamSystemsMIB=crossbeamSystemsMIB, cbsAPM8650=cbsAPM8650, cbsC25Chassis=cbsC25Chassis, cbsMIBs=cbsMIBs, cbsX60Chassis=cbsX60Chassis, cbsNPM4110=cbsNPM4110, cbsC30iChassis=cbsC30iChassis, cbsNPM8650=cbsNPM8650, cbsTraps=cbsTraps, cbsCPM4100=cbsCPM4100, cbsX30Chassis=cbsX30Chassis, cbsXSeries=cbsXSeries, cbsAPM8600=cbsAPM8600, cbsAPM9600=cbsAPM9600, cbsAPM2030=cbsAPM2030, cbsNPM20=cbsNPM20, cbsX45Chassis=cbsX45Chassis, cbsCPM9600=cbsCPM9600, cbsCPModules=cbsCPModules, cbsCPM8100=cbsCPM8100, cbsCSeries=cbsCSeries, cbsX40Chassis=cbsX40Chassis, cbsX80Chassis=cbsX80Chassis, cbsCPM8600=cbsCPM8600, cbsAPM4100=cbsAPM4100, cbsNPM4100=cbsNPM4100, cbsAPM8200=cbsAPM8200, cbsProducts=cbsProducts, cbsC12Chassis=cbsC12Chassis, cbsNPM8210=cbsNPM8210, cbsC30Chassis=cbsC30Chassis, cbsAPM4250=cbsAPM4250, cbsNPM8200=cbsNPM8200, cbsX20Chassis=cbsX20Chassis, cbsNPModules=cbsNPModules, cbsNPM8620=cbsNPM8620, cbsC10Chassis=cbsC10Chassis, cbsC2Chassis=cbsC2Chassis, cbsCPM8400=cbsCPM8400, cbsNPM30=cbsNPM30, cbsC6Chassis=cbsC6Chassis, cbsXChassis=cbsXChassis, cbsX40Modules=cbsX40Modules, cbsAPM8400=cbsAPM8400, cbsAPModules=cbsAPModules, cbsAPM4200=cbsAPM4200, crossbeamSystems=crossbeamSystems)
