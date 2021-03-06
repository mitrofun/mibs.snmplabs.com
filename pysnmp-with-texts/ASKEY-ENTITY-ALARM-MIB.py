#
# PySNMP MIB module ASKEY-ENTITY-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASKEY-ENTITY-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AskeyVendorTypeEnum, ipDslam = mibBuilder.importSymbols("ASKEY-DSLAM-MIB", "AskeyVendorTypeEnum", "ipDslam")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, Unsigned32, Bits, Gauge32, NotificationType, ModuleIdentity, Integer32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "Unsigned32", "Bits", "Gauge32", "NotificationType", "ModuleIdentity", "Integer32", "MibIdentifier", "ObjectIdentity")
DisplayString, TruthValue, AutonomousType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "AutonomousType", "TextualConvention")
askeyEntityAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12))
askeyEntityAlarmMIB.setRevisions(('1904-11-22 15:41', '1904-10-13 14:00', '1904-08-10 16:10', '1904-08-10 10:10', '1904-07-30 14:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: askeyEntityAlarmMIB.setRevisionsDescriptions(('Add aeRelayInTable for alarm relay-in ports configuration.', 'Replace *VendorTypeEnum with *PlannedVendorTypeEnum and *OnlineendorTypeEnum. More detail information.', 'Remove import from ENTITY-MIB, use Unsigned32 instead of PhysicalIndex. This make this MIB has more compatibility', 'Remove unused objects.', 'Import PhysicalIndex from ENTITY-MIB, remove aeAlarmNotification from aeAlarmTable.',))
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setLastUpdated('0411221541Z')
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setOrganization('Askey Computer Corp.')
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setContactInfo('Caleb Chiu E-mail: caleb@askey.com.tw ')
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setDescription('The MIB module presents all managed objects extended to ENTITY-MIB, including alarm definition, alarm ,monitoring and entity status.')
class AskeyAlarmBit(TextualConvention, Integer32):
    description = 'An arbitrary value which uniquely identifies a type of alarm notified by hardware. It implies the bit position of alarm represented by a 32-bits unsigned integer, from 0 (bit0) to 31 (bit31). The value is a small positive integer; index values for different alarm bits are not necessarily contiguous. Related information about all alarm bits are defined in aeAlarmDefinitionTable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 31)

class AskeyAlarmSeverity(TextualConvention, Integer32):
    description = 'Defines the level of alarm severity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("info", 5), ("none", 99))

class AskeyAlarmName(DisplayString):
    description = 'Defines the name of alarm.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class AskeyAlarmList(TextualConvention, Unsigned32):
    description = 'For each set of physical entities sharing a unique aePhysicalVendorType, there an exists unique alarm space. An unsigned 32-bit integer represents an alarm list, in which each bit represents an alarm type. The LSB bit (bit 0) represent alarm types identified by the integer values 1. The bit 1 represent alarm types identified by the integer values 2, and so forth. So The MSB bit (bit 31) represent alarm types identified by the integer values 32. MSB LSB 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ | | | | | +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ | | | | | | | | | | | | | | | | | | | | | | | +- Alarm 24 .... | | | | | | | +- Alarm 0 | | | | | | +--- Alarm 25 | | | | | | +--- Alarm 1 | | | | | +----- Alarm 26 | | | | | +----- Alarm 2 | | | | +------- Alarm 27 | | | | +------- Alarm 3 | | | +--------- Alarm 28 | | | +--------- Alarm 4 | | +----------- Alarm 29 | | +----------- Alarm 5 | +------------- Alarm 30 | +------------- Alarm 6 +--------------- Alarm 31 +--------------- Alarm 7 '
    status = 'current'

class AskeyAlarmAction(TextualConvention, Integer32):
    description = 'Defines the action of alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("set", 1), ("clear", 2))

askeyEntityAlarmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1))
askeyEntityAlarmMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2))
aeAlarmDefinition = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2))
aeAlarmMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3))
aeAlarmHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4))
aeAlarmDefinitionTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1), )
if mibBuilder.loadTexts: aeAlarmDefinitionTable.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefinitionTable.setDescription('This table contains alarm definition. Each row defines a single alarm per vendor type, NOT an alarm list.')
aeAlarmDefinitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefVendorTypeEnum"), (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"))
if mibBuilder.loadTexts: aeAlarmDefinitionEntry.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefinitionEntry.setDescription('Information about an alarm definition to help an NMS find the meaning of an alarm, and object (aeAlarmFiltered) to help an NMS stop monitoring a type of alarm.')
aeAlarmDefVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 1), AskeyVendorTypeEnum())
if mibBuilder.loadTexts: aeAlarmDefVendorTypeEnum.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefVendorTypeEnum.setDescription('A reference of the vendor-specific hardware type of the physical entity.')
aeAlarmDefType = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 2), AskeyAlarmBit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefType.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefType.setDescription('The type of this alarm. It represents the position of bit in the AskeyAlarmList.')
aeAlarmDefName = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 3), AskeyAlarmName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefName.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefName.setDescription('The abbreviation of an alarm type, e.g. LOS, LOF, AIS.')
aeAlarmDefDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefDescr.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefDescr.setDescription('A textual description of an alarm type. This object should contain the description and trouble-shooting of a alarm.')
aeAlarmDefSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 5), AskeyAlarmSeverity().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefSeverity.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefSeverity.setDescription('The severity of an alarm type.')
aeAlarmDefFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 6), TruthValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefFiltered.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefFiltered.setDescription('To determine whether enable this alarm trap.')
aeAlarmDefSuppressedby = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 7), AskeyAlarmList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefSuppressedby.setStatus('current')
if mibBuilder.loadTexts: aeAlarmDefSuppressedby.setDescription('To determine which alarms make this alarm suppressed.')
aeAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1), )
if mibBuilder.loadTexts: aeAlarmTable.setStatus('current')
if mibBuilder.loadTexts: aeAlarmTable.setDescription('This table contains one row per physical entity. Information in this table are derived from AskeyAlarmList and aeAlarmDefinitionTable.')
aeAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"))
if mibBuilder.loadTexts: aeAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: aeAlarmEntry.setDescription('The status of an physical entity about active alarm includes highest-level alarm severity and service affection.')
aeAlarmPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: aeAlarmPhysicalIndex.setDescription('Physical entity index, encoded by shelf/slot/port, 2 decimal digits each field.')
aeAlarmPlannedVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 2), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmPlannedVendorTypeEnum.setStatus('current')
if mibBuilder.loadTexts: aeAlarmPlannedVendorTypeEnum.setDescription('An enumeration of the planned vendor-specific hardware type of the physical entity.')
aeAlarmOnlineVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 3), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmOnlineVendorTypeEnum.setStatus('current')
if mibBuilder.loadTexts: aeAlarmOnlineVendorTypeEnum.setDescription('An enumeration of the online vendor-specific hardware type of the physical entity.')
aeAlarmList = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 4), AskeyAlarmList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmList.setStatus('current')
if mibBuilder.loadTexts: aeAlarmList.setDescription("Defines the active alarms on physical entity. Alarm information is represented by AskeyAlarmList, A manager can use bitwise integer operation to retrieve what type of alarms are asserted. All the alarm types are defined in aeAlarmDefinitionTable. A bit value of '0' implies no such type of alarm and in contrast a bit value of '1' implies there is an such type of alarm asserted. All unused bits (or no alarm) are filled by 0.")
aeAlarmLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmLastChange.setStatus('current')
if mibBuilder.loadTexts: aeAlarmLastChange.setDescription('The system time of the alarm vector is changed.')
aeAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 6), AskeyAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: aeAlarmSeverity.setDescription('The highest level of alarm severity of a physical entity.')
aeHistoryAlarmTableSize = MibScalar((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmTableSize.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmTableSize.setDescription('The size of the aeHistoryAlarmTable in rows. A value of 0 means no alarm logged in this table.')
aeHistoryAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2), )
if mibBuilder.loadTexts: aeHistoryAlarmTable.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmTable.setDescription('This table contains all active alarms currently exist in the overall system. There is one row per active alarm of physical entity. When a manager misses those traps originated by a agent, it can also retrieve those events from this table.')
aeHistoryAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeHistoryAlarmIndex"))
if mibBuilder.loadTexts: aeHistoryAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmEntry.setDescription('The history of alarms recently ever existed in the system but removed.')
aeHistoryAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2146483647)))
if mibBuilder.loadTexts: aeHistoryAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmIndex.setDescription('The index of this entry.The value of index will wrap back to 1 while it reaching 2^31-1. So a manager must notice this condition by checking aeHistoryAlarmTime.')
aeHistoryAlarmPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmPhysicalIndex.setDescription('The index of physical entity for this alarm.')
aeHistoryAlarmPlannedVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 3), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmPlannedVendorTypeEnum.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmPlannedVendorTypeEnum.setDescription('An enumeration of the planned vendor-specific hardware type of the physical entity. ')
aeHistoryAlarmOnlineVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 4), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmOnlineVendorTypeEnum.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmOnlineVendorTypeEnum.setDescription('An enumeration of the online vendor-specific hardware type of the physical entity. ')
aeHistoryAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 5), AskeyAlarmBit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmType.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmType.setDescription('The type of this alarm.')
aeHistoryAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmTime.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmTime.setDescription('The value of sysUpTime at the time this alarm asserted.')
aeHistoryAlarmAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 7), AskeyAlarmAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmAction.setStatus('current')
if mibBuilder.loadTexts: aeHistoryAlarmAction.setDescription('The action of this alarm.')
aeRelayInTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5), )
if mibBuilder.loadTexts: aeRelayInTable.setStatus('current')
if mibBuilder.loadTexts: aeRelayInTable.setDescription('This table contains one row per relay in entity. Administrator use this table to management the normal/abnormal status of relay-in alarm ports.')
aeRelayInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeRelayInPhysicalIndex"))
if mibBuilder.loadTexts: aeRelayInEntry.setStatus('current')
if mibBuilder.loadTexts: aeRelayInEntry.setDescription('The configuration and status of an physical entity about alarm relay-in ports.')
aeRelayInPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeRelayInPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: aeRelayInPhysicalIndex.setDescription('Physical entity index, encoded by shelf/slot/port, 2 decimal digits each field.')
aeRelayInName = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeRelayInName.setStatus('current')
if mibBuilder.loadTexts: aeRelayInName.setDescription('User defined name for this relay-in port.')
aeRelayInNormalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("close", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeRelayInNormalStatus.setStatus('current')
if mibBuilder.loadTexts: aeRelayInNormalStatus.setDescription('User defined status for this relay-in port.')
aeRelayInCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("close", 2), ("disable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeRelayInCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: aeRelayInCurrentStatus.setDescription('Current status for this relay-in port.')
askeyEntityMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0))
askeyEntityAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0, 1)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
if mibBuilder.loadTexts: askeyEntityAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: askeyEntityAlarmTrap.setDescription('An askeyEntityAlarmClear trap is sent when a entity clears an alarm. It can be utilized by an NMS to trigger alarm definition table maintenance polls. An NMS should periodically check the items of aeHistoryAlarmTable to detect any missed askeyEntityAlarmClear trap events, e.g. due to throttling or transmission loss.')
askeyEntityAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3))
askeyEntityAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1))
askeyEntityAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2))
askeyEntityAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1, 1)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmDefinitionGroup"), ("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmMonitoringGroup"), ("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmCompliance = askeyEntityAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: askeyEntityAlarmCompliance.setDescription('The compliance statement for SNMP entities which implement the Askey EntityAlarm MIB.')
askeyEntityAlarmDefinitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 2)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefName"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefDescr"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSeverity"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefFiltered"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSuppressedby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmDefinitionGroup = askeyEntityAlarmDefinitionGroup.setStatus('current')
if mibBuilder.loadTexts: askeyEntityAlarmDefinitionGroup.setDescription('The collection of objects which are used to represent definition of alarms, for which a single agent provides management information.')
askeyEntityAlarmMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 3)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmMonitoringGroup = askeyEntityAlarmMonitoringGroup.setStatus('current')
if mibBuilder.loadTexts: askeyEntityAlarmMonitoringGroup.setDescription('The collection of objects which are used to represent monitoring of alarm status, for which a single agent provides management information.')
askeyEntityAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 4)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmNotificationsGroup = askeyEntityAlarmNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: askeyEntityAlarmNotificationsGroup.setDescription('The collection of notifications used to indicate Entity MIB data consistency and general status information.')
mibBuilder.exportSymbols("ASKEY-ENTITY-ALARM-MIB", aeAlarmTable=aeAlarmTable, askeyEntityAlarmGroups=askeyEntityAlarmGroups, aeRelayInNormalStatus=aeRelayInNormalStatus, aeHistoryAlarmEntry=aeHistoryAlarmEntry, aeRelayInTable=aeRelayInTable, aeAlarmPlannedVendorTypeEnum=aeAlarmPlannedVendorTypeEnum, aeRelayInCurrentStatus=aeRelayInCurrentStatus, askeyEntityAlarmNotificationsGroup=askeyEntityAlarmNotificationsGroup, AskeyAlarmSeverity=AskeyAlarmSeverity, AskeyAlarmBit=AskeyAlarmBit, aeRelayInName=aeRelayInName, AskeyAlarmList=AskeyAlarmList, aeAlarmDefDescr=aeAlarmDefDescr, aeAlarmDefSuppressedby=aeAlarmDefSuppressedby, askeyEntityAlarmConformance=askeyEntityAlarmConformance, askeyEntityAlarmTrap=askeyEntityAlarmTrap, aeHistoryAlarmTable=aeHistoryAlarmTable, aeAlarmDefName=aeAlarmDefName, aeHistoryAlarmPlannedVendorTypeEnum=aeHistoryAlarmPlannedVendorTypeEnum, askeyEntityAlarmDefinitionGroup=askeyEntityAlarmDefinitionGroup, aeHistoryAlarmIndex=aeHistoryAlarmIndex, askeyEntityMIBTrapPrefix=askeyEntityMIBTrapPrefix, aeAlarmOnlineVendorTypeEnum=aeAlarmOnlineVendorTypeEnum, aeHistoryAlarmTime=aeHistoryAlarmTime, aeHistoryAlarmTableSize=aeHistoryAlarmTableSize, aeAlarmDefFiltered=aeAlarmDefFiltered, aeHistoryAlarmPhysicalIndex=aeHistoryAlarmPhysicalIndex, aeHistoryAlarmType=aeHistoryAlarmType, aeAlarmSeverity=aeAlarmSeverity, askeyEntityAlarmMIBObjects=askeyEntityAlarmMIBObjects, aeRelayInPhysicalIndex=aeRelayInPhysicalIndex, askeyEntityAlarmMIBTraps=askeyEntityAlarmMIBTraps, aeAlarmDefSeverity=aeAlarmDefSeverity, aeRelayInEntry=aeRelayInEntry, PYSNMP_MODULE_ID=askeyEntityAlarmMIB, aeAlarmMonitoring=aeAlarmMonitoring, aeAlarmList=aeAlarmList, aeAlarmDefinitionEntry=aeAlarmDefinitionEntry, askeyEntityAlarmMIB=askeyEntityAlarmMIB, AskeyAlarmAction=AskeyAlarmAction, aeAlarmEntry=aeAlarmEntry, aeHistoryAlarmAction=aeHistoryAlarmAction, askeyEntityAlarmMonitoringGroup=askeyEntityAlarmMonitoringGroup, askeyEntityAlarmCompliances=askeyEntityAlarmCompliances, aeAlarmHistory=aeAlarmHistory, AskeyAlarmName=AskeyAlarmName, aeAlarmDefinitionTable=aeAlarmDefinitionTable, aeAlarmDefinition=aeAlarmDefinition, aeAlarmDefVendorTypeEnum=aeAlarmDefVendorTypeEnum, aeAlarmPhysicalIndex=aeAlarmPhysicalIndex, aeAlarmDefType=aeAlarmDefType, aeAlarmLastChange=aeAlarmLastChange, aeHistoryAlarmOnlineVendorTypeEnum=aeHistoryAlarmOnlineVendorTypeEnum, askeyEntityAlarmCompliance=askeyEntityAlarmCompliance)
