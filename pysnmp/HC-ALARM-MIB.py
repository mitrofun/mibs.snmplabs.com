#
# PySNMP MIB module HC-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HC-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
rmon, OwnerString, rmonEventGroup = mibBuilder.importSymbols("RMON-MIB", "rmon", "OwnerString", "rmonEventGroup")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity, TimeTicks, Integer32, Bits, Counter64, IpAddress, MibIdentifier, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32")
DisplayString, TextualConvention, RowStatus, StorageType, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType", "VariablePointer")
hcAlarmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 29))
hcAlarmMIB.setRevisions(('2002-12-16 00:00',))
if mibBuilder.loadTexts: hcAlarmMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: hcAlarmMIB.setOrganization('IETF RMONMIB Working Group')
hcAlarmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1))
hcAlarmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2))
hcAlarmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3))
hcAlarmControlObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 1))
hcAlarmCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 2))
class HcValueStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valueNotAvailable", 1), ("valuePositive", 2), ("valueNegative", 3))

hcAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1), )
if mibBuilder.loadTexts: hcAlarmTable.setStatus('current')
hcAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1), ).setIndexNames((0, "HC-ALARM-MIB", "hcAlarmIndex"))
if mibBuilder.loadTexts: hcAlarmEntry.setStatus('current')
hcAlarmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hcAlarmIndex.setStatus('current')
hcAlarmInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmInterval.setStatus('current')
hcAlarmVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmVariable.setStatus('current')
hcAlarmSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmSampleType.setStatus('current')
hcAlarmAbsValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmAbsValue.setStatus('current')
hcAlarmValueStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 6), HcValueStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueStatus.setStatus('current')
hcAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStartupAlarm.setStatus('current')
hcAlarmRisingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueLo.setStatus('current')
hcAlarmRisingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueHi.setStatus('current')
hcAlarmRisingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 10), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThresholdValStatus.setStatus('current')
hcAlarmFallingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueLo.setStatus('current')
hcAlarmFallingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueHi.setStatus('current')
hcAlarmFallingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 13), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThresholdValStatus.setStatus('current')
hcAlarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingEventIndex.setStatus('current')
hcAlarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingEventIndex.setStatus('current')
hcAlarmValueFailedAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueFailedAttempts.setStatus('current')
hcAlarmOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 17), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmOwner.setStatus('current')
hcAlarmStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 18), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStorageType.setStatus('current')
hcAlarmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStatus.setStatus('current')
hcAlarmCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 16, 29, 1, 2, 1), Bits().clone(namedValues=NamedValues(("hcAlarmCreation", 0), ("hcAlarmNvStorage", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmCapabilities.setStatus('current')
hcAlarmNotifPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2, 0))
hcRisingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"))
if mibBuilder.loadTexts: hcRisingAlarm.setStatus('current')
hcFallingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"))
if mibBuilder.loadTexts: hcFallingAlarm.setStatus('current')
hcAlarmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 1))
hcAlarmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 2))
hcAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 29, 3, 1, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmControlGroup"), ("HC-ALARM-MIB", "hcAlarmCapabilitiesGroup"), ("HC-ALARM-MIB", "hcAlarmNotificationsGroup"), ("RMON-MIB", "rmonEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmCompliance = hcAlarmCompliance.setStatus('current')
hcAlarmControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmInterval"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmStartupAlarm"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), ("HC-ALARM-MIB", "hcAlarmValueFailedAttempts"), ("HC-ALARM-MIB", "hcAlarmOwner"), ("HC-ALARM-MIB", "hcAlarmStorageType"), ("HC-ALARM-MIB", "hcAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmControlGroup = hcAlarmControlGroup.setStatus('current')
hcAlarmCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmCapabilitiesGroup = hcAlarmCapabilitiesGroup.setStatus('current')
hcAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 3)).setObjects(("HC-ALARM-MIB", "hcRisingAlarm"), ("HC-ALARM-MIB", "hcFallingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmNotificationsGroup = hcAlarmNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmOwner=hcAlarmOwner, hcAlarmCapabilitiesObjects=hcAlarmCapabilitiesObjects, hcAlarmStatus=hcAlarmStatus, hcAlarmTable=hcAlarmTable, hcAlarmConformance=hcAlarmConformance, hcAlarmNotifications=hcAlarmNotifications, hcAlarmStartupAlarm=hcAlarmStartupAlarm, hcAlarmFallingEventIndex=hcAlarmFallingEventIndex, hcAlarmNotifPrefix=hcAlarmNotifPrefix, hcAlarmCompliance=hcAlarmCompliance, hcAlarmFallingThresholdValStatus=hcAlarmFallingThresholdValStatus, hcAlarmCompliances=hcAlarmCompliances, hcAlarmRisingThreshAbsValueLo=hcAlarmRisingThreshAbsValueLo, HcValueStatus=HcValueStatus, hcAlarmIndex=hcAlarmIndex, hcAlarmRisingEventIndex=hcAlarmRisingEventIndex, hcAlarmInterval=hcAlarmInterval, hcAlarmControlGroup=hcAlarmControlGroup, hcAlarmSampleType=hcAlarmSampleType, hcAlarmFallingThreshAbsValueHi=hcAlarmFallingThreshAbsValueHi, hcAlarmStorageType=hcAlarmStorageType, hcAlarmRisingThresholdValStatus=hcAlarmRisingThresholdValStatus, hcRisingAlarm=hcRisingAlarm, hcAlarmAbsValue=hcAlarmAbsValue, hcAlarmGroups=hcAlarmGroups, hcAlarmCapabilitiesGroup=hcAlarmCapabilitiesGroup, hcAlarmMIB=hcAlarmMIB, hcAlarmVariable=hcAlarmVariable, hcAlarmObjects=hcAlarmObjects, hcAlarmValueStatus=hcAlarmValueStatus, hcAlarmValueFailedAttempts=hcAlarmValueFailedAttempts, hcFallingAlarm=hcFallingAlarm, PYSNMP_MODULE_ID=hcAlarmMIB, hcAlarmControlObjects=hcAlarmControlObjects, hcAlarmCapabilities=hcAlarmCapabilities, hcAlarmEntry=hcAlarmEntry, hcAlarmNotificationsGroup=hcAlarmNotificationsGroup, hcAlarmFallingThreshAbsValueLo=hcAlarmFallingThreshAbsValueLo, hcAlarmRisingThreshAbsValueHi=hcAlarmRisingThreshAbsValueHi)
