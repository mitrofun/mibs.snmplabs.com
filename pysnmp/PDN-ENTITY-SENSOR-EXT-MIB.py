#
# PySNMP MIB module PDN-ENTITY-SENSOR-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhySensorValue, EntitySensorValue, entPhySensorEntry = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorValue", "EntitySensorValue", "entPhySensorEntry")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Bits, MibIdentifier, Counter32, TimeTicks, ObjectIdentity, Gauge32, Integer32, Unsigned32, IpAddress, Counter64, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnEntitySensorExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45))
pdnEntitySensorExtMIB.setRevisions(('2003-06-06 00:00', '2003-04-24 00:00', '2003-04-16 00:00',))
if mibBuilder.loadTexts: pdnEntitySensorExtMIB.setLastUpdated('200306060000Z')
if mibBuilder.loadTexts: pdnEntitySensorExtMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnEntitySensorExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0))
pdnEntitySensorExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1))
pdnEntitySensorExtAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 2))
pdnEntitySensorExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3))
pdnEntPhySensorExtTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1), )
if mibBuilder.loadTexts: pdnEntPhySensorExtTable.setStatus('current')
pdnEntPhySensorExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1), )
entPhySensorEntry.registerAugmentions(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtEntry"))
pdnEntPhySensorExtEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
if mibBuilder.loadTexts: pdnEntPhySensorExtEntry.setStatus('current')
pdnEntPhySensorExtNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("thresholdExceeded", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnEntPhySensorExtNotificationEnable.setStatus('current')
pdnEntPhySensorExtUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 2), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnEntPhySensorExtUpperThreshold.setStatus('current')
pdnEntPhySensorExtLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 3), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnEntPhySensorExtLowerThreshold.setStatus('current')
pdnEntPhySensorExtThresholdState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noThresholdsExceeded", 1), ("upperThresholdExceeded", 2), ("lowerThresholdExceeded", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnEntPhySensorExtThresholdState.setStatus('current')
pdnEntPhySensorExtThresholdExceededSet = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0, 1)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
if mibBuilder.loadTexts: pdnEntPhySensorExtThresholdExceededSet.setStatus('current')
pdnEntPhySensorExtThresholdExceededCleared = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0, 100)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
if mibBuilder.loadTexts: pdnEntPhySensorExtThresholdExceededCleared.setStatus('current')
pdnEntitySensorExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 1))
pdnEntitySensorExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2))
pdnEntitySensorExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 1, 1)).setObjects(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntitySensorExtThresholdGroup"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntitySensorExtThresholdNtfyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntitySensorExtMIBCompliance = pdnEntitySensorExtMIBCompliance.setStatus('current')
pdnEntitySensorExtObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 1))
pdnEntitySensorExtAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 2))
pdnEntitySensorExtNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 3))
pdnEntitySensorExtThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 1, 1)).setObjects(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtNotificationEnable"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtUpperThreshold"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtLowerThreshold"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntitySensorExtThresholdGroup = pdnEntitySensorExtThresholdGroup.setStatus('current')
pdnEntitySensorExtThresholdNtfyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 3, 1)).setObjects(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdExceededSet"), ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdExceededCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntitySensorExtThresholdNtfyGroup = pdnEntitySensorExtThresholdNtfyGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-ENTITY-SENSOR-EXT-MIB", PYSNMP_MODULE_ID=pdnEntitySensorExtMIB, pdnEntPhySensorExtLowerThreshold=pdnEntPhySensorExtLowerThreshold, pdnEntPhySensorExtThresholdExceededSet=pdnEntPhySensorExtThresholdExceededSet, pdnEntitySensorExtNtfyGroups=pdnEntitySensorExtNtfyGroups, pdnEntPhySensorExtThresholdState=pdnEntPhySensorExtThresholdState, pdnEntPhySensorExtUpperThreshold=pdnEntPhySensorExtUpperThreshold, pdnEntitySensorExtAFNs=pdnEntitySensorExtAFNs, pdnEntitySensorExtMIB=pdnEntitySensorExtMIB, pdnEntPhySensorExtTable=pdnEntPhySensorExtTable, pdnEntitySensorExtGroups=pdnEntitySensorExtGroups, pdnEntitySensorExtNotifications=pdnEntitySensorExtNotifications, pdnEntitySensorExtMIBCompliance=pdnEntitySensorExtMIBCompliance, pdnEntitySensorExtConformance=pdnEntitySensorExtConformance, pdnEntPhySensorExtThresholdExceededCleared=pdnEntPhySensorExtThresholdExceededCleared, pdnEntitySensorExtThresholdGroup=pdnEntitySensorExtThresholdGroup, pdnEntitySensorExtObjects=pdnEntitySensorExtObjects, pdnEntitySensorExtThresholdNtfyGroup=pdnEntitySensorExtThresholdNtfyGroup, pdnEntitySensorExtAfnGroups=pdnEntitySensorExtAfnGroups, pdnEntPhySensorExtEntry=pdnEntPhySensorExtEntry, pdnEntitySensorExtCompliances=pdnEntitySensorExtCompliances, pdnEntPhySensorExtNotificationEnable=pdnEntPhySensorExtNotificationEnable, pdnEntitySensorExtObjGroups=pdnEntitySensorExtObjGroups)
