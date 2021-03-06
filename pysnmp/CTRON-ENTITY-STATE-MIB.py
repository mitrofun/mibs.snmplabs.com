#
# PySNMP MIB module CTRON-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
EntityStandbyStatus, EntityAlarmStatus, EntityOperState, EntityAdminState, EntityUsageState = mibBuilder.importSymbols("CTRON-ENTITY-STATE-TC-MIB", "EntityStandbyStatus", "EntityAlarmStatus", "EntityOperState", "EntityAdminState", "EntityUsageState")
ctEntityStateMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateMib")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, TimeTicks, NotificationType, iso, Bits, Integer32, mib_2, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "iso", "Bits", "Integer32", "mib-2", "Counter64")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
ctEntityStateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1))
ctEntityStateMIB.setRevisions(('2005-01-23 00:00',))
if mibBuilder.loadTexts: ctEntityStateMIB.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateMIB.setOrganization('IETF Entity MIB Working Group')
ctEntStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1))
ctEntStateTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1), )
if mibBuilder.loadTexts: ctEntStateTable.setStatus('current')
ctEntStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ctEntStateEntry.setStatus('current')
ctEntStateLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateLastChanged.setStatus('current')
ctEntStateAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEntStateAdmin.setStatus('current')
ctEntStateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateOper.setStatus('current')
ctEntStateUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateUsage.setStatus('current')
ctEntStateAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateAlarm.setStatus('current')
ctEntStateStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateStandby.setStatus('current')
ctEntStateNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0))
ctEntStateOperEnabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperEnabled.setStatus('current')
ctEntStateOperDisabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperDisabled.setStatus('current')
ctEntStateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2))
ctEntStateCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1))
ctEntStateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateGroup"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateCompliance = ctEntStateCompliance.setStatus('current')
ctEntStateGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2))
ctEntStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateLastChanged"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOper"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateUsage"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateGroup = ctEntStateGroup.setStatus('current')
ctEntStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateOperEnabled"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateNotificationsGroup = ctEntStateNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CTRON-ENTITY-STATE-MIB", ctEntStateStandby=ctEntStateStandby, ctEntityStateMIB=ctEntityStateMIB, ctEntStateAdmin=ctEntStateAdmin, ctEntStateAlarm=ctEntStateAlarm, ctEntStateTable=ctEntStateTable, ctEntStateOper=ctEntStateOper, ctEntStateUsage=ctEntStateUsage, ctEntStateCompliances=ctEntStateCompliances, ctEntStateGroup=ctEntStateGroup, ctEntStateOperDisabled=ctEntStateOperDisabled, ctEntStateOperEnabled=ctEntStateOperEnabled, PYSNMP_MODULE_ID=ctEntityStateMIB, ctEntStateObjects=ctEntStateObjects, ctEntStateGroups=ctEntStateGroups, ctEntStateNotificationsGroup=ctEntStateNotificationsGroup, ctEntStateLastChanged=ctEntStateLastChanged, ctEntStateCompliance=ctEntStateCompliance, ctEntStateNotifications=ctEntStateNotifications, ctEntStateConformance=ctEntStateConformance, ctEntStateEntry=ctEntStateEntry)
