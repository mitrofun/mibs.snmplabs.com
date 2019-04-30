#
# PySNMP MIB module PICA-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PICA-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Gauge32, snmpModules, Counter64, IpAddress, Unsigned32, NotificationType, enterprises, Bits, ModuleIdentity, ObjectIdentity, Integer32, mib_2, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Gauge32", "snmpModules", "Counter64", "IpAddress", "Unsigned32", "NotificationType", "enterprises", "Bits", "ModuleIdentity", "ObjectIdentity", "Integer32", "mib-2", "MibIdentifier", "iso")
TextualConvention, AutonomousType, TruthValue, DisplayString, PhysAddress, RowStatus, TimeStamp, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "TruthValue", "DisplayString", "PhysAddress", "RowStatus", "TimeStamp", "TestAndIncr")
picaPrivateMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 35098))
picaPrivateMib.setRevisions(('2011-04-28 00:00',))
if mibBuilder.loadTexts: picaPrivateMib.setLastUpdated('201104280000Z')
if mibBuilder.loadTexts: picaPrivateMib.setOrganization('Pica8 Inc.')
hostStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 1))
cpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUsage.setStatus('current')
totalPhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPhyMemory.setStatus('current')
usedPhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usedPhyMemory.setStatus('current')
freePhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freePhyMemory.setStatus('current')
switchTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchTemperature.setStatus('current')
cpuTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTemperature.setStatus('current')
switchChipTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchChipTemperature.setStatus('current')
sfpstatusTable = MibTable((1, 3, 6, 1, 4, 1, 35098, 1, 8), )
if mibBuilder.loadTexts: sfpstatusTable.setStatus('current')
sfpstatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1), ).setIndexNames((0, "PICA-PRIVATE-MIB", "sfpIndex"))
if mibBuilder.loadTexts: sfpstatusEntry.setStatus('current')
sfpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpIndex.setStatus('current')
sfpVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorName.setStatus('current')
sfpSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpSerialNumber.setStatus('current')
sfpTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTemp.setStatus('current')
sfpVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVoltage.setStatus('current')
sfpBias = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpBias.setStatus('current')
sfpTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxPower.setStatus('current')
sfpRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRxPower.setStatus('current')
sfpType = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpType.setStatus('current')
rpsustatusTable = MibTable((1, 3, 6, 1, 4, 1, 35098, 1, 9), )
if mibBuilder.loadTexts: rpsustatusTable.setStatus('current')
rpsustatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35098, 1, 9, 1), ).setIndexNames((0, "PICA-PRIVATE-MIB", "rpsuIndex"))
if mibBuilder.loadTexts: rpsustatusEntry.setStatus('current')
rpsuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuIndex.setStatus('current')
rpsuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuStatus.setStatus('current')
switchConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 2))
tftpConfigFilePath = MibScalar((1, 3, 6, 1, 4, 1, 35098, 2, 0), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpConfigFilePath.setStatus('current')
tftpBatchFilePath = MibScalar((1, 3, 6, 1, 4, 1, 35098, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpBatchFilePath.setStatus('current')
picaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20))
picaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20, 1))
picaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20, 2))
picaBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 1)).setObjects(("PICA-PRIVATE-MIB", "cpuUsage"), ("PICA-PRIVATE-MIB", "totalPhyMemory"), ("PICA-PRIVATE-MIB", "usedPhyMemory"), ("PICA-PRIVATE-MIB", "freePhyMemory"), ("PICA-PRIVATE-MIB", "switchTemperature"), ("PICA-PRIVATE-MIB", "cpuTemperature"), ("PICA-PRIVATE-MIB", "switchChipTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaBasicGroup = picaBasicGroup.setStatus('current')
picasfpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 2)).setObjects(("PICA-PRIVATE-MIB", "sfpIndex"), ("PICA-PRIVATE-MIB", "sfpVendorName"), ("PICA-PRIVATE-MIB", "sfpSerialNumber"), ("PICA-PRIVATE-MIB", "sfpTemp"), ("PICA-PRIVATE-MIB", "sfpVoltage"), ("PICA-PRIVATE-MIB", "sfpBias"), ("PICA-PRIVATE-MIB", "sfpTxPower"), ("PICA-PRIVATE-MIB", "sfpRxPower"), ("PICA-PRIVATE-MIB", "sfpType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picasfpGroup = picasfpGroup.setStatus('current')
picarpsuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 3)).setObjects(("PICA-PRIVATE-MIB", "rpsuIndex"), ("PICA-PRIVATE-MIB", "rpsuStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picarpsuGroup = picarpsuGroup.setStatus('current')
picaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 4)).setObjects(("PICA-PRIVATE-MIB", "tftpConfigFilePath"), ("PICA-PRIVATE-MIB", "tftpBatchFilePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaConfigGroup = picaConfigGroup.setStatus('current')
picaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 35098, 20, 2, 1)).setObjects(("PICA-PRIVATE-MIB", "picaBasicGroup"), ("PICA-PRIVATE-MIB", "picasfpGroup"), ("PICA-PRIVATE-MIB", "picarpsuGroup"), ("PICA-PRIVATE-MIB", "picaConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaCompliance = picaCompliance.setStatus('current')
mibBuilder.exportSymbols("PICA-PRIVATE-MIB", sfpVendorName=sfpVendorName, switchConfigGroup=switchConfigGroup, picaConfigGroup=picaConfigGroup, sfpSerialNumber=sfpSerialNumber, freePhyMemory=freePhyMemory, sfpRxPower=sfpRxPower, cpuUsage=cpuUsage, sfpBias=sfpBias, tftpConfigFilePath=tftpConfigFilePath, picasfpGroup=picasfpGroup, sfpstatusTable=sfpstatusTable, PYSNMP_MODULE_ID=picaPrivateMib, sfpTxPower=sfpTxPower, sfpTemp=sfpTemp, picarpsuGroup=picarpsuGroup, sfpstatusEntry=sfpstatusEntry, sfpIndex=sfpIndex, picaCompliance=picaCompliance, rpsustatusEntry=rpsustatusEntry, switchChipTemperature=switchChipTemperature, rpsuIndex=rpsuIndex, rpsuStatus=rpsuStatus, picaPrivateMib=picaPrivateMib, totalPhyMemory=totalPhyMemory, picaGroups=picaGroups, hostStatusGroup=hostStatusGroup, switchTemperature=switchTemperature, usedPhyMemory=usedPhyMemory, cpuTemperature=cpuTemperature, tftpBatchFilePath=tftpBatchFilePath, sfpVoltage=sfpVoltage, picaCompliances=picaCompliances, rpsustatusTable=rpsustatusTable, sfpType=sfpType, picaConformance=picaConformance, picaBasicGroup=picaBasicGroup)