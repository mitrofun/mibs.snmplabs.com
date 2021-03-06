#
# PySNMP MIB module HP-ICF-CHASSIS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-CHASSIS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpicfCommon, hpicfObjectModules, hpicfCommonTrapsPrefix = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon", "hpicfObjectModules", "hpicfCommonTrapsPrefix")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Integer32, ModuleIdentity, ObjectIdentity, iso, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, MibIdentifier, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "Gauge32")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
hpicfChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3))
hpicfChassisMib.setRevisions(('2013-02-10 08:47', '2011-08-25 08:47', '2010-08-25 00:00', '2009-04-22 00:00', '2000-11-03 22:16', '1997-03-06 03:34', '1996-09-10 02:45', '1995-07-13 00:00', '1994-11-20 00:00', '1993-07-09 00:00',))
if mibBuilder.loadTexts: hpicfChassisMib.setLastUpdated('201302100847Z')
if mibBuilder.loadTexts: hpicfChassisMib.setOrganization('HP Networking')
hpicfChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2))
hpicfChassisId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfChassisId.setStatus('deprecated')
hpicfChassisNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfChassisNumSlots.setStatus('deprecated')
hpicfSlotTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3), )
if mibBuilder.loadTexts: hpicfSlotTable.setStatus('deprecated')
hpicfSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpicfSlotIndex"))
if mibBuilder.loadTexts: hpicfSlotEntry.setStatus('deprecated')
hpicfSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotIndex.setStatus('deprecated')
hpicfSlotObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotObjectId.setStatus('deprecated')
hpicfSlotLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotLastChange.setStatus('deprecated')
hpicfSlotDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotDescr.setStatus('deprecated')
hpicfEntityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4), )
if mibBuilder.loadTexts: hpicfEntityTable.setStatus('deprecated')
hpicfEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpicfEntityIndex"))
if mibBuilder.loadTexts: hpicfEntityEntry.setStatus('deprecated')
hpicfEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfEntityIndex.setStatus('deprecated')
hpicfEntityFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfEntityFunction.setStatus('deprecated')
hpicfEntityObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfEntityObjectId.setStatus('deprecated')
hpicfEntityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfEntityDescr.setStatus('deprecated')
hpicfEntityTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfEntityTimestamp.setStatus('deprecated')
hpicfSlotMapTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5), )
if mibBuilder.loadTexts: hpicfSlotMapTable.setStatus('deprecated')
hpicfSlotMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpicfSlotMapSlot"), (0, "HP-ICF-CHASSIS", "hpicfSlotMapEntity"))
if mibBuilder.loadTexts: hpicfSlotMapEntry.setStatus('deprecated')
hpicfSlotMapSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotMapSlot.setStatus('deprecated')
hpicfSlotMapEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotMapEntity.setStatus('deprecated')
hpicfSensorTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6), )
if mibBuilder.loadTexts: hpicfSensorTable.setStatus('current')
hpicfSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpicfSensorIndex"))
if mibBuilder.loadTexts: hpicfSensorEntry.setStatus('current')
hpicfSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorIndex.setStatus('current')
hpicfSensorObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorObjectId.setStatus('current')
hpicfSensorNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorNumber.setStatus('current')
hpicfSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("bad", 2), ("warning", 3), ("good", 4), ("notPresent", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorStatus.setStatus('current')
hpicfSensorWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorWarnings.setStatus('current')
hpicfSensorFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorFailures.setStatus('current')
hpicfSensorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSensorDescr.setStatus('current')
hpicfChassisAddrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7), )
if mibBuilder.loadTexts: hpicfChassisAddrTable.setStatus('deprecated')
hpicfChassisAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpicfChasAddrType"), (0, "HP-ICF-CHASSIS", "hpicfChasAddrAddress"))
if mibBuilder.loadTexts: hpicfChassisAddrEntry.setStatus('deprecated')
hpicfChasAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipAddr", 1), ("ipxAddr", 2), ("macAddr", 3))))
if mibBuilder.loadTexts: hpicfChasAddrType.setStatus('deprecated')
hpicfChasAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 10)))
if mibBuilder.loadTexts: hpicfChasAddrAddress.setStatus('deprecated')
hpicfChasAddrEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfChasAddrEntity.setStatus('deprecated')
hpChassisTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8))
hpSystemAirTempTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1), )
if mibBuilder.loadTexts: hpSystemAirTempTable.setStatus('current')
hpSystemAirTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1), ).setIndexNames((0, "HP-ICF-CHASSIS", "hpSystemAirSensor"))
if mibBuilder.loadTexts: hpSystemAirTempEntry.setStatus('current')
hpSystemAirSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpSystemAirSensor.setStatus('current')
hpSystemAirName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirName.setStatus('current')
hpSystemAirCurrentTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirCurrentTemp.setStatus('current')
hpSystemAirMaxTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirMaxTemp.setStatus('current')
hpSystemAirMinTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirMinTemp.setStatus('current')
hpSystemAirOverTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirOverTemp.setStatus('current')
hpSystemAirThresholdTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirThresholdTemp.setStatus('current')
hpSystemAirAvgTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirAvgTemp.setStatus('deprecated')
hpSystemAirEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 9), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirEntPhysicalIndex.setStatus('current')
hpSystemAirAvgTemp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 8, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSystemAirAvgTemp1.setStatus('current')
hpicfFanTrayType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("highPerformance", 2))).clone('standard')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanTrayType.setStatus('current')
hpicfOpacityShieldInstalled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 10), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfOpacityShieldInstalled.setStatus('current')
hpicfSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 3)).setObjects(("HP-ICF-CHASSIS", "hpicfSensorStatus"), ("HP-ICF-CHASSIS", "hpicfSensorDescr"))
if mibBuilder.loadTexts: hpicfSensorTrap.setStatus('current')
hpicfChassisConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1))
hpicfChassisCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1))
hpicfChassisGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2))
hpicfChasAdvStkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 1)).setObjects(("HP-ICF-CHASSIS", "hpicfChassisBasicGroup"), ("HP-ICF-CHASSIS", "hpicfSensorGroup"), ("HP-ICF-CHASSIS", "hpicfSensorNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasAdvStkCompliance = hpicfChasAdvStkCompliance.setStatus('deprecated')
hpicfChasAdvStk2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 2)).setObjects(("HP-ICF-CHASSIS", "hpicfChassisBasicGroup"), ("HP-ICF-CHASSIS", "hpicfChassisAddrGroup"), ("HP-ICF-CHASSIS", "hpicfSensorGroup"), ("HP-ICF-CHASSIS", "hpicfSensorNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasAdvStk2Compliance = hpicfChasAdvStk2Compliance.setStatus('deprecated')
hpicfChasSensorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 3)).setObjects(("HP-ICF-CHASSIS", "hpicfSensorGroup"), ("HP-ICF-CHASSIS", "hpicfSensorNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasSensorCompliance = hpicfChasSensorCompliance.setStatus('current')
hpicfChasTempCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 4)).setObjects(("HP-ICF-CHASSIS", "hpicfChasTempGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasTempCompliance = hpicfChasTempCompliance.setStatus('deprecated')
hpicfOpacityShieldsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 5)).setObjects(("HP-ICF-CHASSIS", "hpicfOpacityShieldsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOpacityShieldsCompliance = hpicfOpacityShieldsCompliance.setStatus('current')
hpicfChasTempCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 1, 6)).setObjects(("HP-ICF-CHASSIS", "hpicfChasTempGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasTempCompliance1 = hpicfChasTempCompliance1.setStatus('current')
hpicfChassisBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 1)).setObjects(("HP-ICF-CHASSIS", "hpicfChassisId"), ("HP-ICF-CHASSIS", "hpicfChassisNumSlots"), ("HP-ICF-CHASSIS", "hpicfSlotIndex"), ("HP-ICF-CHASSIS", "hpicfSlotObjectId"), ("HP-ICF-CHASSIS", "hpicfSlotLastChange"), ("HP-ICF-CHASSIS", "hpicfSlotDescr"), ("HP-ICF-CHASSIS", "hpicfEntityIndex"), ("HP-ICF-CHASSIS", "hpicfEntityFunction"), ("HP-ICF-CHASSIS", "hpicfEntityObjectId"), ("HP-ICF-CHASSIS", "hpicfEntityDescr"), ("HP-ICF-CHASSIS", "hpicfEntityTimestamp"), ("HP-ICF-CHASSIS", "hpicfSlotMapSlot"), ("HP-ICF-CHASSIS", "hpicfSlotMapEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChassisBasicGroup = hpicfChassisBasicGroup.setStatus('deprecated')
hpicfSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 2)).setObjects(("HP-ICF-CHASSIS", "hpicfSensorIndex"), ("HP-ICF-CHASSIS", "hpicfSensorObjectId"), ("HP-ICF-CHASSIS", "hpicfSensorNumber"), ("HP-ICF-CHASSIS", "hpicfSensorStatus"), ("HP-ICF-CHASSIS", "hpicfSensorWarnings"), ("HP-ICF-CHASSIS", "hpicfSensorFailures"), ("HP-ICF-CHASSIS", "hpicfSensorDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSensorGroup = hpicfSensorGroup.setStatus('current')
hpicfChassisAddrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 3)).setObjects(("HP-ICF-CHASSIS", "hpicfChasAddrEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChassisAddrGroup = hpicfChassisAddrGroup.setStatus('deprecated')
hpicfSensorNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 4)).setObjects(("HP-ICF-CHASSIS", "hpicfSensorTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSensorNotifyGroup = hpicfSensorNotifyGroup.setStatus('current')
hpicfChasTempGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 5)).setObjects(("HP-ICF-CHASSIS", "hpSystemAirName"), ("HP-ICF-CHASSIS", "hpSystemAirCurrentTemp"), ("HP-ICF-CHASSIS", "hpSystemAirMaxTemp"), ("HP-ICF-CHASSIS", "hpSystemAirMinTemp"), ("HP-ICF-CHASSIS", "hpSystemAirThresholdTemp"), ("HP-ICF-CHASSIS", "hpSystemAirOverTemp"), ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp"), ("HP-ICF-CHASSIS", "hpSystemAirEntPhysicalIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasTempGroup = hpicfChasTempGroup.setStatus('deprecated')
hpicfOpacityShieldsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 6)).setObjects(("HP-ICF-CHASSIS", "hpicfFanTrayType"), ("HP-ICF-CHASSIS", "hpicfOpacityShieldInstalled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOpacityShieldsGroup = hpicfOpacityShieldsGroup.setStatus('current')
hpicfChasTempGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3, 1, 2, 7)).setObjects(("HP-ICF-CHASSIS", "hpSystemAirName"), ("HP-ICF-CHASSIS", "hpSystemAirCurrentTemp"), ("HP-ICF-CHASSIS", "hpSystemAirMaxTemp"), ("HP-ICF-CHASSIS", "hpSystemAirMinTemp"), ("HP-ICF-CHASSIS", "hpSystemAirThresholdTemp"), ("HP-ICF-CHASSIS", "hpSystemAirOverTemp"), ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp"), ("HP-ICF-CHASSIS", "hpSystemAirAvgTemp1"), ("HP-ICF-CHASSIS", "hpSystemAirEntPhysicalIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfChasTempGroup1 = hpicfChasTempGroup1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-CHASSIS", hpicfSlotObjectId=hpicfSlotObjectId, hpicfSensorFailures=hpicfSensorFailures, hpicfChassisGroups=hpicfChassisGroups, hpSystemAirName=hpSystemAirName, hpicfSensorDescr=hpicfSensorDescr, hpicfEntityIndex=hpicfEntityIndex, hpSystemAirTempEntry=hpSystemAirTempEntry, hpicfChassisMib=hpicfChassisMib, hpicfChassisAddrTable=hpicfChassisAddrTable, hpicfSensorTable=hpicfSensorTable, hpicfSensorGroup=hpicfSensorGroup, hpSystemAirOverTemp=hpSystemAirOverTemp, hpicfChasTempCompliance=hpicfChasTempCompliance, hpicfSlotEntry=hpicfSlotEntry, hpicfSlotMapTable=hpicfSlotMapTable, hpSystemAirMaxTemp=hpSystemAirMaxTemp, hpicfChassisNumSlots=hpicfChassisNumSlots, hpicfEntityFunction=hpicfEntityFunction, hpicfChasSensorCompliance=hpicfChasSensorCompliance, hpicfSensorObjectId=hpicfSensorObjectId, hpicfSensorNumber=hpicfSensorNumber, hpicfFanTrayType=hpicfFanTrayType, hpicfChasAdvStk2Compliance=hpicfChasAdvStk2Compliance, hpicfChassisId=hpicfChassisId, hpicfEntityTimestamp=hpicfEntityTimestamp, hpicfChassisBasicGroup=hpicfChassisBasicGroup, hpicfSlotLastChange=hpicfSlotLastChange, PYSNMP_MODULE_ID=hpicfChassisMib, hpSystemAirAvgTemp1=hpSystemAirAvgTemp1, hpicfChassisCompliances=hpicfChassisCompliances, hpicfOpacityShieldsGroup=hpicfOpacityShieldsGroup, hpicfChasTempGroup1=hpicfChasTempGroup1, hpicfOpacityShieldsCompliance=hpicfOpacityShieldsCompliance, hpicfSensorEntry=hpicfSensorEntry, hpicfEntityDescr=hpicfEntityDescr, hpicfSlotTable=hpicfSlotTable, hpSystemAirEntPhysicalIndex=hpSystemAirEntPhysicalIndex, hpicfSlotDescr=hpicfSlotDescr, hpicfSlotIndex=hpicfSlotIndex, hpicfSensorWarnings=hpicfSensorWarnings, hpSystemAirTempTable=hpSystemAirTempTable, hpicfSlotMapEntry=hpicfSlotMapEntry, hpicfChassisAddrGroup=hpicfChassisAddrGroup, hpSystemAirCurrentTemp=hpSystemAirCurrentTemp, hpicfChasTempGroup=hpicfChasTempGroup, hpicfEntityEntry=hpicfEntityEntry, hpicfSlotMapSlot=hpicfSlotMapSlot, hpicfSlotMapEntity=hpicfSlotMapEntity, hpSystemAirThresholdTemp=hpSystemAirThresholdTemp, hpSystemAirAvgTemp=hpSystemAirAvgTemp, hpicfChassisConformance=hpicfChassisConformance, hpicfChassis=hpicfChassis, hpicfChassisAddrEntry=hpicfChassisAddrEntry, hpicfChasAddrType=hpicfChasAddrType, hpicfSensorStatus=hpicfSensorStatus, hpSystemAirMinTemp=hpSystemAirMinTemp, hpChassisTemperature=hpChassisTemperature, hpicfSensorIndex=hpicfSensorIndex, hpicfEntityObjectId=hpicfEntityObjectId, hpicfChasAddrEntity=hpicfChasAddrEntity, hpicfChasTempCompliance1=hpicfChasTempCompliance1, hpicfOpacityShieldInstalled=hpicfOpacityShieldInstalled, hpSystemAirSensor=hpSystemAirSensor, hpicfChasAdvStkCompliance=hpicfChasAdvStkCompliance, hpicfChasAddrAddress=hpicfChasAddrAddress, hpicfSensorNotifyGroup=hpicfSensorNotifyGroup, hpicfSensorTrap=hpicfSensorTrap, hpicfEntityTable=hpicfEntityTable)
