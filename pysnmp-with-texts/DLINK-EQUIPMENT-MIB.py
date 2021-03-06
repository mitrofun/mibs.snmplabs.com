#
# PySNMP MIB module DLINK-EQUIPMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-EQUIPMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:49:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
AgentNotifyLevel, dlink_common_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "AgentNotifyLevel", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Unsigned32, Gauge32, IpAddress, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ObjectIdentity, TimeTicks, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ObjectIdentity", "TimeTicks", "iso", "Counter64")
DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
swDlinkEquipmentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 11))
if mibBuilder.loadTexts: swDlinkEquipmentMIB.setLastUpdated('0202140000Z')
if mibBuilder.loadTexts: swDlinkEquipmentMIB.setOrganization('DLink Corporation')
if mibBuilder.loadTexts: swDlinkEquipmentMIB.setContactInfo('')
if mibBuilder.loadTexts: swDlinkEquipmentMIB.setDescription('DLink equipments MIB .')
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

swDlinkEquipmentMib = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1))
swDlinkEquipmentNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2))
swDlinkEquipmentCapacity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 1), Bits().clone(namedValues=NamedValues(("fanCapable", 0), ("redundantPowerCapable", 1), ("tempteratureDetection", 2), ("stackingCapable", 3), ("chassisCapable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlinkEquipmentCapacity.setStatus('current')
if mibBuilder.loadTexts: swDlinkEquipmentCapacity.setDescription('Indicates the equipment capacity supported in the system .')
swPowerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6), )
if mibBuilder.loadTexts: swPowerTable.setStatus('current')
if mibBuilder.loadTexts: swPowerTable.setDescription('A list of temperature.')
swPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1), ).setIndexNames((0, "DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"), (0, "DLINK-EQUIPMENT-MIB", "swPowerID"))
if mibBuilder.loadTexts: swPowerEntry.setStatus('current')
if mibBuilder.loadTexts: swPowerEntry.setDescription('A entry of Power information.')
swPowerUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerUnitIndex.setStatus('current')
if mibBuilder.loadTexts: swPowerUnitIndex.setDescription('Indicates ID of the unit in the System')
swPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerID.setStatus('current')
if mibBuilder.loadTexts: swPowerID.setDescription('Indicates ID of the power 1 : main power 2 : redundant power .')
swPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 0), ("lowVoltage", 1), ("overCurrent", 2), ("working", 3), ("fail", 4), ("connect", 5), ("disconnect", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerStatus.setStatus('current')
if mibBuilder.loadTexts: swPowerStatus.setDescription('Indicates status of the power ')
swUnitMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9))
swUnitStackingVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitStackingVersion.setStatus('current')
if mibBuilder.loadTexts: swUnitStackingVersion.setDescription('This object indicates the version of this stacking system .')
swUnitMaxSupportedUnits = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMaxSupportedUnits.setStatus('current')
if mibBuilder.loadTexts: swUnitMaxSupportedUnits.setDescription('Maximum number of units are supported in the system.')
swUnitNumOfUnit = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitNumOfUnit.setStatus('current')
if mibBuilder.loadTexts: swUnitNumOfUnit.setDescription('The current number of units.')
swUnitMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4), )
if mibBuilder.loadTexts: swUnitMgmtTable.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtTable.setDescription('This table contains the unit information.')
swUnitMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1), ).setIndexNames((0, "DLINK-EQUIPMENT-MIB", "swUnitMgmtId"))
if mibBuilder.loadTexts: swUnitMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtEntry.setDescription('A list of management information for each unit in the system.')
swUnitMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtId.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtId.setDescription('This object indicates the specific entry in the stacking/chassis table.')
swUnitMgmtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtMacAddr.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtMacAddr.setDescription('The Mac address of this unit.')
swUnitMgmtStartPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtStartPort.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtStartPort.setDescription('This object indicates the start port of this unit.')
swUnitMgmtPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtPortRange.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtPortRange.setDescription('This object indicates the total ports of this unit.')
swUnitMgmtFrontPanelLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtFrontPanelLedStatus.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtFrontPanelLedStatus.setDescription('This object is a set of system LED indications. The first three octets is defined as system LED. The first LED is power LED. The second LED is console LED. The third LED is RPS (Redundancy Power Supply) LED. The other octets following the second octets are the logical port LED (following dot1dBasePort ordering). One byte is presented to one port and this byte is presentd to the Link/Activity LED. Link/Activity LED : The most significant bit is used for blink/solid: 8 = The LED blinks. The second significant bit is used for link status: 1 = link fail. 2 = link pass. The four remaining bits are currently unused and must be 0.')
swUnitMgmtCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("stand-alone", 3), ("master", 4), ("slave", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitMgmtCtrlMode.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtCtrlMode.setDescription('This object indicates the stack mode that user configed for this unit. The object only can be configed when the device is stand alone. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. auto(2) - the system will auto assign this stack role of this unit to be stand-alone(3), master(4), or slave(5). stand-alone(3) - the unit is forced to stand alone. master(4) - the unit is forced to master. If this unit is seleted to be master, it can modify the configuration of the stacking system. slave(5) - the unit is forced to slave. If this unit is seleted to be slave, it only can view the configuration of the stacking system.')
swUnitMgmtCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("stand-alone", 3), ("master", 4), ("slave", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtCurrentMode.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtCurrentMode.setDescription('The current stack role of this unit.')
swUnitMgmtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtVersion.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtVersion.setDescription('This object indicates the version of this stacking unit.')
swUnitMgmtModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtModuleName.setStatus('current')
if mibBuilder.loadTexts: swUnitMgmtModuleName.setDescription('A textual string containing module name of the stacking unit. ')
swEquipmentNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2))
swEquipPowerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2))
swEquipPowerNotifyPerfix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0))
swPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 2)).setObjects(("DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"), ("DLINK-EQUIPMENT-MIB", "swPowerID"), ("DLINK-EQUIPMENT-MIB", "swPowerStatus"))
if mibBuilder.loadTexts: swPowerFailure.setStatus('current')
if mibBuilder.loadTexts: swPowerFailure.setDescription('Power Failure notification.')
swPowerRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 3)).setObjects(("DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"), ("DLINK-EQUIPMENT-MIB", "swPowerID"), ("DLINK-EQUIPMENT-MIB", "swPowerStatus"))
if mibBuilder.loadTexts: swPowerRecover.setStatus('current')
if mibBuilder.loadTexts: swPowerRecover.setDescription('Power Recover notification.')
swNotificationBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3))
mibBuilder.exportSymbols("DLINK-EQUIPMENT-MIB", swUnitStackingVersion=swUnitStackingVersion, swPowerUnitIndex=swPowerUnitIndex, PYSNMP_MODULE_ID=swDlinkEquipmentMIB, swPowerTable=swPowerTable, swUnitMaxSupportedUnits=swUnitMaxSupportedUnits, swDlinkEquipmentMib=swDlinkEquipmentMib, swUnitMgmtEntry=swUnitMgmtEntry, swPowerEntry=swPowerEntry, swUnitMgmtCurrentMode=swUnitMgmtCurrentMode, swEquipPowerNotification=swEquipPowerNotification, swDlinkEquipmentNotify=swDlinkEquipmentNotify, swUnitMgmtId=swUnitMgmtId, swUnitMgmtStartPort=swUnitMgmtStartPort, swUnitMgmtFrontPanelLedStatus=swUnitMgmtFrontPanelLedStatus, swPowerFailure=swPowerFailure, swUnitMgmt=swUnitMgmt, swUnitMgmtMacAddr=swUnitMgmtMacAddr, swNotificationBindings=swNotificationBindings, swPowerStatus=swPowerStatus, swEquipmentNotification=swEquipmentNotification, swEquipPowerNotifyPerfix=swEquipPowerNotifyPerfix, MacAddress=MacAddress, swUnitMgmtCtrlMode=swUnitMgmtCtrlMode, swUnitNumOfUnit=swUnitNumOfUnit, swDlinkEquipmentMIB=swDlinkEquipmentMIB, swUnitMgmtTable=swUnitMgmtTable, swPowerID=swPowerID, swPowerRecover=swPowerRecover, swUnitMgmtPortRange=swUnitMgmtPortRange, swUnitMgmtModuleName=swUnitMgmtModuleName, swDlinkEquipmentCapacity=swDlinkEquipmentCapacity, swUnitMgmtVersion=swUnitMgmtVersion)
