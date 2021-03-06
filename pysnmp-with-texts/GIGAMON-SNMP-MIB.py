#
# PySNMP MIB module GIGAMON-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GIGAMON-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
MibIdentifier, Counter64, enterprises, TimeTicks, Integer32, Bits, Gauge32, NotificationType, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "enterprises", "TimeTicks", "Integer32", "Bits", "Gauge32", "NotificationType", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Unsigned32")
DisplayString, PhysAddress, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention", "TimeStamp")
gigamonSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 26866))
gigamonSnmp.setRevisions(('2013-09-25 00:00', '2013-08-09 00:00', '2013-04-15 00:00', '2012-12-04 00:00', '2012-05-09 00:00', '2012-05-09 00:00', '2012-03-27 00:00', '2011-03-25 00:00', '2011-03-24 00:00', '2011-03-03 00:00', '2010-07-10 10:00', '2010-07-10 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gigamonSnmp.setRevisionsDescriptions(('Added powerSupply OID to gigamonSystem MIB group', "Top-level infrastructure of Gigamon's MIB objects for GigaVUE-212, GigaVUE-420, GigaVUE-2404, GigaVUE-HD and GigaVUE-TA1", "Added 'license-mismatch' to gigamonSnmpNotifModuleOperationType", "Added 'up' to gigamonSnmpNotifModuleOperationType", 'Added new information found under gigamonSystem MIB group', '1) Updated GigaVUE product line support: (a) Added GigaVUE-TA1 (b) Removed G-TAP and GigaVUE-MP 2) Added speed40000 and speed100000 in gigamonSnmpPortLinkSpeed for representing 40G and 100G port speed', "Added 'shutdown' to gigamonSnmpNotifModuleOperationType", 'Added the following notifications: - gigamonSnmpCpuUtilHighNotification - gigamonSnmpUnexpectedShutdownNotification - gigamonSnmpDiskSpaceLowNotification', 'Added G-TAP support', 'Added GigaVUE-HD support', 'Created notification definitions', 'First draft',))
if mibBuilder.loadTexts: gigamonSnmp.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: gigamonSnmp.setOrganization('www.gigamon.com')
if mibBuilder.loadTexts: gigamonSnmp.setContactInfo('postal: Gigamon LLC 598 Gibraltar Drive Milpitas, CA 95035 email: support@gigamon.com')
if mibBuilder.loadTexts: gigamonSnmp.setDescription('Added notification type: - gigamonSnmpBpsFailoverNotification Added notification objects: - gigamonSnmpNotifBpsUnitName - gigamonSnmpNotifBpsFailoverStatus')
gigamonSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1))
gigamonGigaVUE = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1, 1))
gigamonSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 1, 2))
gigamonSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 2))
manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturer.setStatus('current')
if mibBuilder.loadTexts: manufacturer.setDescription('Displays the manufacturer name of the system.')
model = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
if mibBuilder.loadTexts: model.setDescription('Displays the model name of the system.')
name = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: name.setStatus('current')
if mibBuilder.loadTexts: name.setDescription('Displays the name of the system.')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('Displays the serial number of the system.')
systemDescription = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDescription.setStatus('current')
if mibBuilder.loadTexts: systemDescription.setDescription('Displays the description of the system.')
version = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('Displays the software version of the system.')
chassisModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisModelNumber.setStatus('current')
if mibBuilder.loadTexts: chassisModelNumber.setDescription('Displays the chassis model number of the system.')
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('current')
if mibBuilder.loadTexts: chassisSerialNumber.setDescription('Displays the chassis serial number of the system.')
bladeSerialNumbers = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bladeSerialNumbers.setStatus('current')
if mibBuilder.loadTexts: bladeSerialNumbers.setDescription('Displays the blade serial numbers in the system.')
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareVersion.setDescription('Displays the firmware version of the system.')
hardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareVersion.setStatus('current')
if mibBuilder.loadTexts: hardwareVersion.setDescription('Displays the hardware version of the system.')
cpuRAMSize = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuRAMSize.setStatus('current')
if mibBuilder.loadTexts: cpuRAMSize.setDescription('Displays the CPU RAM size of the system.')
cpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilization.setStatus('current')
if mibBuilder.loadTexts: cpuUtilization.setDescription('Displays the CPU utilization of the system.')
fans = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fans.setStatus('current')
if mibBuilder.loadTexts: fans.setDescription('Displays the fans in the system.')
temperatureSensors = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureSensors.setStatus('current')
if mibBuilder.loadTexts: temperatureSensors.setDescription('Displays the temperature sensors in the system.')
powerSupply = MibScalar((1, 3, 6, 1, 4, 1, 26866, 2, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupply.setStatus('current')
if mibBuilder.loadTexts: powerSupply.setDescription('Displays the power supplies in the system.')
gigamonProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3))
gigamonGV2404 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 1))
gigamonGV420 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 2))
gigamonGV212 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 3))
gigamonGV216 = MibIdentifier((1, 3, 6, 1, 4, 1, 26866, 3, 4))
gigamonSnmpNotifLevel = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("information", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifLevel.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifLevel.setDescription("It acts as a payload for the level of Gigamon's Notifications.")
gigamonSnmpNotifDescription = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifDescription.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifDescription.setDescription("It acts as a payload for the description of Gigamon's Notifications. The value is to describe the reason for the notification.")
gigamonSnmpNotifOpType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("delete", 3), ("validate", 4), ("change", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifOpType.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifOpType.setDescription("It specifies the type of operation of Gigamon's Notifications.")
gigamonSnmpNotifPortName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifPortName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifPortName.setDescription("The alpha-numerical name of a port shown in Gigamon's Notifications.")
gigamonSnmpNotifPortLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifPortLinkStatus.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifPortLinkStatus.setDescription("It indicates port link status of Gigamon's Notifications.")
gigamonSnmpNotifTAPRelayStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("passive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifTAPRelayStatus.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifTAPRelayStatus.setDescription("It indicates TAP relay status of Gigamon's Notifications.")
gigamonSnmpNotifRxTxType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("rx", 0), ("tx", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxType.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxType.setDescription('It indicates Incoming/RX or outgoing/TX packets')
gigamonSnmpNotifRxTxErrorType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("under-size", 0), ("fragments", 1), ("obsolete", 2), ("jabbers", 3), ("crc-align", 4), ("unknown", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxErrorType.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifRxTxErrorType.setDescription("It indicates RX/TX error type of Gigamon's Notifications.")
gigamonSnmpNotifCounter = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifCounter.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifCounter.setDescription('32-bit Counter.')
gigamonSnmpNotifFirmwareName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFirmwareName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifFirmwareName.setDescription('Name of GigaVUE firmware.')
gigamonSnmpNotifModuleOperationType = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("removed", 0), ("inserted", 1), ("changed", 2), ("mismatch", 3), ("shutdown", 4), ("up", 5), ("license-mismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifModuleOperationType.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifModuleOperationType.setDescription('It indicates the operation performed on module')
gigamonSnmpNotifModuleName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 12), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifModuleName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifModuleName.setDescription('Module name of GigaVUE module')
gigamonNotifSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("mid-plane", 0), ("slot-1", 1), ("slot-2", 2), ("slot-3", 3), ("gigaLink-Back", 4), ("daughter-Card", 5), ("slot-4", 10), ("slot-5", 11), ("slot-6", 12), ("slot-7", 13), ("slot-8", 14), ("slot-CC1", 15), ("slot-CC2", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifSlotNumber.setStatus('current')
if mibBuilder.loadTexts: gigamonNotifSlotNumber.setDescription('Slot number')
gigamonSnmpNotifUserName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 14), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUserName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifUserName.setDescription('User login name typed in')
gigamonSnmpNotifFileName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 15), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFileName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifFileName.setDescription('Saved configuration file name')
gigamonNotifPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("failure", -1), ("abnormal", 0), ("normal", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifPowerStatus.setStatus('current')
if mibBuilder.loadTexts: gigamonNotifPowerStatus.setDescription('Power Status')
gigamonSnmpNotifHardWareName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 17), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifHardWareName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifHardWareName.setDescription('Description of Hardware')
gigamonSnmpNotifGigaVUE420SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("mid-plane", 0), ("expansion-slot-1", 1), ("expansion-slot-2", 2), ("expansion-slot-3", 3), ("expansion-slot-4", 4), ("expansion-slot-5", 5), ("x1-slot", 6), ("x2-slot", 7), ("x3-slot", 8), ("x4-slot", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifGigaVUE420SlotNumber.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifGigaVUE420SlotNumber.setDescription('Slot number')
gigamonSnmpNotifFanName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 19), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFanName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifFanName.setDescription('Name of fan')
gigamonNotifFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("failure", -1), ("abnormal", 0), ("normal", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonNotifFanStatus.setStatus('current')
if mibBuilder.loadTexts: gigamonNotifFanStatus.setDescription('Fan Status')
gigamonSnmpNotifUtilizationAlarm = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("below", 0), ("exceed", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationAlarm.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationAlarm.setDescription("It indicates over-threshold port utilization alarm of Gigamon's Notifications.")
gigamonSnmpNotifUtilizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 22), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationThreshold.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifUtilizationThreshold.setDescription('Utilization threshold percentage')
gigamonSnmpBatteryLevel = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("batteryChargeComplete", 0), ("downBelow75", 1), ("downBelow50", 2), ("downBelow25", 3), ("shutDownSystem", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gigamonSnmpBatteryLevel.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpBatteryLevel.setDescription(' battery level: 0 - battery charge complete 1 - battery level has been down below 75% 2 - battery level has been down below 50% 3 - battery level has been down below 25% 4 - battery level has down to 15% or below and shutting down the system ')
gigamonSnmpPortLinkSpeed = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApply", 0), ("speed10", 1), ("speed100", 2), ("speed1000", 3), ("speed10000", 4), ("speed40000", 5), ("speed100000", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpPortLinkSpeed.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpPortLinkSpeed.setDescription(' port link speed: 0 - Not Apply if link is down 1 - 10 Mbps 2 - 100 Mbps 3 - 1000 Mbps 4 - 10000 Mbps 5 - 40000 Mbps 6 - 100000 Mbps ')
gigamonSnmpPortLinkDuplex = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notApply", 0), ("full", 1), ("half", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpPortLinkDuplex.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpPortLinkDuplex.setDescription(' port link duplex: 0 - Not Apply if link is down 1 - full duplex 2 - half duplex ')
gigamonSnmpNotifCpuIndex = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 26), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifCpuIndex.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifCpuIndex.setDescription('Index of CPU, starting from 0')
gigamonSnmpNotifFsMountPoint = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 27), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifFsMountPoint.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifFsMountPoint.setDescription('Mount point for this filesystem')
gigamonSnmpPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mainPower", 0), ("poe", 1), ("power48V", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gigamonSnmpPowerSource.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpPowerSource.setDescription(' power source: 0 - main power 1 - poe(Power over Ethernet) 2 - -48V Power ')
gigamonSnmpNotifBpsUnitName = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 29), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifBpsUnitName.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifBpsUnitName.setDescription('Name of BPS unit')
gigamonSnmpNotifBpsFailoverStatus = MibScalar((1, 3, 6, 1, 4, 1, 26866, 1, 2, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("primary", 0), ("secondary", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: gigamonSnmpNotifBpsFailoverStatus.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpNotifBpsFailoverStatus.setDescription('Inline-bypass active unit change')
gigamonSnmpResetSystemNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 1)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpResetSystemNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpResetSystemNotification.setDescription('System reset notification triggered by cold or warm start.')
gigamonSnmpUserAuthFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 2)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUserName"))
if mibBuilder.loadTexts: gigamonSnmpUserAuthFailNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpUserAuthFailNotification.setDescription('Failure in user login operation is the triggered Event.')
gigamonSnmpFirmwareChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 3)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFirmwareName"))
if mibBuilder.loadTexts: gigamonSnmpFirmwareChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpFirmwareChangeNotification.setDescription('Firmware Change notification is the Edge/Level Triggered Event.')
gigamonSnmpConfigSaveNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 4)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFileName"))
if mibBuilder.loadTexts: gigamonSnmpConfigSaveNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpConfigSaveNotification.setDescription('Config save notification is the Edge/Level Triggered Event.')
gigamonSnmpModuleChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 5)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleOperationType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleName"), ("GIGAMON-SNMP-MIB", "gigamonNotifSlotNumber"))
if mibBuilder.loadTexts: gigamonSnmpModuleChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpModuleChangeNotification.setDescription('GigaVUE HW module swapping is the triggered Event.')
gigamonSnmpPacketDropNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 6)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
if mibBuilder.loadTexts: gigamonSnmpPacketDropNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpPacketDropNotification.setDescription('Packet Drop notification is the Edge/Level Triggered Event.')
gigamonSnmpTapRelayChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 7)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifTAPRelayStatus"))
if mibBuilder.loadTexts: gigamonSnmpTapRelayChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpTapRelayChangeNotification.setDescription('TAP relay change notification is the Edge/Level Triggered Event.')
gigamonSnmpPortLinkChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 8)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
if mibBuilder.loadTexts: gigamonSnmpPortLinkChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpPortLinkChangeNotification.setDescription('Port link status change notification is the Edge/Level Triggered Event.')
gigamonSnmpRxTxErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 9)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxErrorType"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
if mibBuilder.loadTexts: gigamonSnmpRxTxErrorNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpRxTxErrorNotification.setDescription('Packet receive/transmit error notification is the Edge/Level Triggered Event.')
gigamonPowerChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 10)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
if mibBuilder.loadTexts: gigamonPowerChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonPowerChangeNotification.setDescription('Power supply status change notification is the Edge/Level Triggered Event.')
gigamonFanChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 11)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFanName"), ("GIGAMON-SNMP-MIB", "gigamonNotifFanStatus"))
if mibBuilder.loadTexts: gigamonFanChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonFanChangeNotification.setDescription('Fan status change notification is the Edge/Level Triggered Event.')
gigamonSnmpOverThresholdChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 12)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationAlarm"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
if mibBuilder.loadTexts: gigamonSnmpOverThresholdChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpOverThresholdChangeNotification.setDescription('Utilization alarm notification is the Edge/Level Triggered Event.')
gigamonSnmpBatteryLevelChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 13)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpBatteryLevel"))
if mibBuilder.loadTexts: gigamonSnmpBatteryLevelChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpBatteryLevelChangeNotification.setDescription('Battery level down notification.')
gigamonLinkSpeedStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 14)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkSpeed"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPortLinkDuplex"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
if mibBuilder.loadTexts: gigamonLinkSpeedStatusChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonLinkSpeedStatusChangeNotification.setDescription('Link status or speed change notification. ')
gigamonPowerSourceChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 15)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpPowerSource"), ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
if mibBuilder.loadTexts: gigamonPowerSourceChangeNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonPowerSourceChangeNotification.setDescription('Power source or status change notification.')
gigamonSnmpCpuUtilHighNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 16)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCpuIndex"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
if mibBuilder.loadTexts: gigamonSnmpCpuUtilHighNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpCpuUtilHighNotification.setDescription('The average CPU utilization in the past minute has gone above the acceptable threshold')
gigamonSnmpUnexpectedShutdownNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 17)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpUnexpectedShutdownNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpUnexpectedShutdownNotification.setDescription('The system has shut down unexpectedly')
gigamonSnmpDiskSpaceLowNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 18)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFsMountPoint"))
if mibBuilder.loadTexts: gigamonSnmpDiskSpaceLowNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpDiskSpaceLowNotification.setDescription('Free space in one of the filesystems is low')
gigamonSnmpWatchdogResetNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 19)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
if mibBuilder.loadTexts: gigamonSnmpWatchdogResetNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpWatchdogResetNotification.setDescription('System reset notification triggered by watchdog timer.')
gigamonSnmpBpsFailoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 26866, 1, 1, 20)).setObjects(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsUnitName"), ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifBpsFailoverStatus"))
if mibBuilder.loadTexts: gigamonSnmpBpsFailoverNotification.setStatus('current')
if mibBuilder.loadTexts: gigamonSnmpBpsFailoverNotification.setDescription('Inline-bypass active unit change notification is the Edge/Level Triggered Event.')
mibBuilder.exportSymbols("GIGAMON-SNMP-MIB", name=name, temperatureSensors=temperatureSensors, gigamonSnmpNotifFileName=gigamonSnmpNotifFileName, gigamonGV2404=gigamonGV2404, gigamonProducts=gigamonProducts, gigamonSnmpNotificationObjects=gigamonSnmpNotificationObjects, gigamonSnmpNotifModuleName=gigamonSnmpNotifModuleName, gigamonLinkSpeedStatusChangeNotification=gigamonLinkSpeedStatusChangeNotification, powerSupply=powerSupply, firmwareVersion=firmwareVersion, gigamonPowerSourceChangeNotification=gigamonPowerSourceChangeNotification, gigamonSnmpNotifGigaVUE420SlotNumber=gigamonSnmpNotifGigaVUE420SlotNumber, gigamonNotifFanStatus=gigamonNotifFanStatus, PYSNMP_MODULE_ID=gigamonSnmp, gigamonSnmpModuleChangeNotification=gigamonSnmpModuleChangeNotification, gigamonSnmpNotifUtilizationAlarm=gigamonSnmpNotifUtilizationAlarm, gigamonSnmpWatchdogResetNotification=gigamonSnmpWatchdogResetNotification, gigamonSnmpPortLinkSpeed=gigamonSnmpPortLinkSpeed, gigamonSnmpOverThresholdChangeNotification=gigamonSnmpOverThresholdChangeNotification, systemDescription=systemDescription, gigamonSnmpDiskSpaceLowNotification=gigamonSnmpDiskSpaceLowNotification, gigamonSnmpNotifPortLinkStatus=gigamonSnmpNotifPortLinkStatus, cpuRAMSize=cpuRAMSize, gigamonSnmpPortLinkChangeNotification=gigamonSnmpPortLinkChangeNotification, model=model, gigamonSnmpNotifLevel=gigamonSnmpNotifLevel, manufacturer=manufacturer, serialNumber=serialNumber, gigamonSnmpNotifPortName=gigamonSnmpNotifPortName, gigamonSnmpNotifHardWareName=gigamonSnmpNotifHardWareName, gigamonGV216=gigamonGV216, gigamonSnmpConfigSaveNotification=gigamonSnmpConfigSaveNotification, version=version, hardwareVersion=hardwareVersion, gigamonSnmpNotifBpsFailoverStatus=gigamonSnmpNotifBpsFailoverStatus, gigamonSnmpNotifFsMountPoint=gigamonSnmpNotifFsMountPoint, gigamonNotifSlotNumber=gigamonNotifSlotNumber, gigamonSnmpNotifCpuIndex=gigamonSnmpNotifCpuIndex, fans=fans, cpuUtilization=cpuUtilization, chassisModelNumber=chassisModelNumber, gigamonSnmpNotifications=gigamonSnmpNotifications, gigamonSnmpNotifBpsUnitName=gigamonSnmpNotifBpsUnitName, gigamonSnmpNotifUtilizationThreshold=gigamonSnmpNotifUtilizationThreshold, gigamonGV420=gigamonGV420, chassisSerialNumber=chassisSerialNumber, gigamonSnmpNotifFirmwareName=gigamonSnmpNotifFirmwareName, gigamonNotifPowerStatus=gigamonNotifPowerStatus, gigamonSnmpBpsFailoverNotification=gigamonSnmpBpsFailoverNotification, gigamonSnmpFirmwareChangeNotification=gigamonSnmpFirmwareChangeNotification, gigamonSnmpNotifOpType=gigamonSnmpNotifOpType, gigamonSnmp=gigamonSnmp, gigamonSnmpPacketDropNotification=gigamonSnmpPacketDropNotification, gigamonGV212=gigamonGV212, gigamonPowerChangeNotification=gigamonPowerChangeNotification, gigamonSnmpNotifRxTxType=gigamonSnmpNotifRxTxType, gigamonSnmpRxTxErrorNotification=gigamonSnmpRxTxErrorNotification, gigamonSnmpNotifUserName=gigamonSnmpNotifUserName, gigamonSnmpPowerSource=gigamonSnmpPowerSource, gigamonSnmpBatteryLevel=gigamonSnmpBatteryLevel, gigamonSnmpResetSystemNotification=gigamonSnmpResetSystemNotification, gigamonSnmpBatteryLevelChangeNotification=gigamonSnmpBatteryLevelChangeNotification, gigamonSnmpNotifCounter=gigamonSnmpNotifCounter, gigamonFanChangeNotification=gigamonFanChangeNotification, gigamonSnmpNotifDescription=gigamonSnmpNotifDescription, gigamonSnmpNotifModuleOperationType=gigamonSnmpNotifModuleOperationType, gigamonSnmpUnexpectedShutdownNotification=gigamonSnmpUnexpectedShutdownNotification, gigamonSnmpPortLinkDuplex=gigamonSnmpPortLinkDuplex, bladeSerialNumbers=bladeSerialNumbers, gigamonSnmpNotifFanName=gigamonSnmpNotifFanName, gigamonSnmpNotifTAPRelayStatus=gigamonSnmpNotifTAPRelayStatus, gigamonSystem=gigamonSystem, gigamonSnmpNotifRxTxErrorType=gigamonSnmpNotifRxTxErrorType, gigamonSnmpCpuUtilHighNotification=gigamonSnmpCpuUtilHighNotification, gigamonSnmpUserAuthFailNotification=gigamonSnmpUserAuthFailNotification, gigamonGigaVUE=gigamonGigaVUE, gigamonSnmpTapRelayChangeNotification=gigamonSnmpTapRelayChangeNotification)
