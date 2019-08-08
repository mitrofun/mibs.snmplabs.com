#
# PySNMP MIB module HPHOTSWAP2SUBSYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPHOTSWAP2SUBSYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, ModuleIdentity, iso, enterprises, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter64, Integer32, MibIdentifier, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ModuleIdentity", "iso", "enterprises", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter64", "Integer32", "MibIdentifier", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaHotswap2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 27))
hpnsaHS2MibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1))
hpnsaHS2Cage = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2))
hpnsaHS2Slot = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3))
hpnsaHS2MibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2MibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2MibRevMajor.setDescription('The major revision level of the MIB.')
hpnsaHS2MibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2MibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2MibRevMinor.setDescription('The minor revision level of the MIB.')
hpnsaHS2CageTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1), )
if mibBuilder.loadTexts: hpnsaHS2CageTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTable.setDescription(' A table of Hotswap 2 Subsystem cage information entries.')
hpnsaHS2CageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1), ).setIndexNames((0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2CageIndex"))
if mibBuilder.loadTexts: hpnsaHS2CageEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageEntry.setDescription(' Hotswap 2 Subsystem cage information.')
hpnsaHS2CageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageIndex.setDescription('A unique index for the Hotswap 2 Cage.')
hpnsaHS2Cage12VPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2Cage12VPower.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2Cage12VPower.setDescription('The current state of the 12V DC power.')
hpnsaHS2CageTerminator1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-attached", 1), ("attached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageTerminator1.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTerminator1.setDescription('The current state of Terminator 1.')
hpnsaHS2CageTerminator2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-attached", 1), ("attached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageTerminator2.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTerminator2.setDescription('The current state of Terminator 2.')
hpnsaHS2CageSCSICable1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-attached", 1), ("attached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageSCSICable1.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageSCSICable1.setDescription('The current state of SCSI Cable 1.')
hpnsaHS2CageSCSICable2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-attached", 1), ("attached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageSCSICable2.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageSCSICable2.setDescription('The current state of SCSI Cable 2.')
hpnsaHS2CageBaseSCSIAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaHS2CageBaseSCSIAddress.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageBaseSCSIAddress.setDescription('The base SCSI address of this cage.')
hpnsaHS2CageTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTemperature.setDescription('The current temperature reading for the temperature sensor (in celcius).')
hpnsaHS2CageTemperatureWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaHS2CageTemperatureWarningThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTemperatureWarningThreshold.setDescription('The warning threshold for the temperature sensor (in celsius).')
hpnsaHS2CageTemperatureAlertThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaHS2CageTemperatureAlertThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageTemperatureAlertThreshold.setDescription('The alert threshold for the temperature sensor (in celsius).')
hpnsaHS2CageManagementBoardFRU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageManagementBoardFRU.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageManagementBoardFRU.setDescription('The Field Replaceable Unit (FRU) Management Board information.')
hpnsaHS2CageInterconnectFRU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageInterconnectFRU.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageInterconnectFRU.setDescription('The Field Replaceable Unit (FRU) Interconnect Board information.')
hpnsaHS2CageFirmwareMajorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageFirmwareMajorRev.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageFirmwareMajorRev.setDescription('The major firmware revision of the Management Board.')
hpnsaHS2CageFirmwareMinorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2CageFirmwareMinorRev.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2CageFirmwareMinorRev.setDescription('The minor firmware revision of the Management Board.')
hpnsaHS2SlotTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1), )
if mibBuilder.loadTexts: hpnsaHS2SlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2SlotTable.setDescription('A table of Hotswap 2 Subsystem Slot information entries.')
hpnsaHS2SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1), ).setIndexNames((0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2SlotCageIndex"), (0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2SlotIndex"))
if mibBuilder.loadTexts: hpnsaHS2SlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2SlotEntry.setDescription(' Hotswap 2 Subsystem Slot information.')
hpnsaHS2SlotCageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2SlotCageIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2SlotCageIndex.setDescription('A unique index for the Hotswap 2 cage.')
hpnsaHS2SlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2SlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2SlotIndex.setDescription('Physical slot number in the Hotswap 2 cage.')
hpnsaHS2DrivePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-present", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2DrivePresent.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2DrivePresent.setDescription('Defines whether there is a drive present in this slot.')
hpnsaHS2DriveSCSIBusType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("se", 1), ("lvd", 2), ("hvd", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaHS2DriveSCSIBusType.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2DriveSCSIBusType.setDescription('The SCSI Bus type with which this drive is attached.')
hpnsaHS2DriveIdentify = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaHS2DriveIdentify.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaHS2DriveIdentify.setDescription('Select or unselect a drive to provide a visual indicator signal for user to locate drive.')
mibBuilder.exportSymbols("HPHOTSWAP2SUBSYSTEM-MIB", hpnsaHS2DrivePresent=hpnsaHS2DrivePresent, nm=nm, hpnsaHS2Cage12VPower=hpnsaHS2Cage12VPower, hpnsa=hpnsa, hpnsaHS2SlotCageIndex=hpnsaHS2SlotCageIndex, hpnsaHS2MibRevMinor=hpnsaHS2MibRevMinor, hpnsaHS2SlotEntry=hpnsaHS2SlotEntry, hpnsaHS2CageIndex=hpnsaHS2CageIndex, hpnsaHS2CageTable=hpnsaHS2CageTable, hpnsaHS2CageInterconnectFRU=hpnsaHS2CageInterconnectFRU, hpnsaHS2CageTemperatureAlertThreshold=hpnsaHS2CageTemperatureAlertThreshold, hp=hp, hpnsaHS2CageBaseSCSIAddress=hpnsaHS2CageBaseSCSIAddress, hpnsaHS2CageFirmwareMajorRev=hpnsaHS2CageFirmwareMajorRev, hpnsaHS2CageTerminator2=hpnsaHS2CageTerminator2, hpnsaHS2Cage=hpnsaHS2Cage, hpnsaHS2DriveIdentify=hpnsaHS2DriveIdentify, hpnsaHS2CageTemperature=hpnsaHS2CageTemperature, hpnsaHS2Slot=hpnsaHS2Slot, hpnsaHS2DriveSCSIBusType=hpnsaHS2DriveSCSIBusType, hpnsaHS2CageFirmwareMinorRev=hpnsaHS2CageFirmwareMinorRev, hpnsaHS2CageSCSICable2=hpnsaHS2CageSCSICable2, hpnsaHS2CageTerminator1=hpnsaHS2CageTerminator1, hpnsaHotswap2=hpnsaHotswap2, hpnsaHS2CageEntry=hpnsaHS2CageEntry, hpnsaHS2CageSCSICable1=hpnsaHS2CageSCSICable1, hpnsaHS2SlotIndex=hpnsaHS2SlotIndex, hpnsaHS2SlotTable=hpnsaHS2SlotTable, hpnsaHS2MibRevMajor=hpnsaHS2MibRevMajor, hpnsaHS2MibRev=hpnsaHS2MibRev, hpnsaHS2CageManagementBoardFRU=hpnsaHS2CageManagementBoardFRU, hpnsaHS2CageTemperatureWarningThreshold=hpnsaHS2CageTemperatureWarningThreshold)