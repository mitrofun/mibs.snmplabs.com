#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:59:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, Unsigned64, CiscoAlarmSeverity, CiscoInetAddressMask, CiscoNetworkAddress = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "Unsigned64", "CiscoAlarmSeverity", "CiscoInetAddressMask", "CiscoNetworkAddress")
CucsManagedObjectDn, CucsManagedObjectId, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects")
CucsEquipmentPresence, CucsEquipmentPowerState, CucsEquipmentOperability, CucsEquipmentSensorThresholdStatus, CucsFsmLifecycle = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsEquipmentPresence", "CucsEquipmentPowerState", "CucsEquipmentOperability", "CucsEquipmentSensorThresholdStatus", "CucsFsmLifecycle")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, MibIdentifier, TimeTicks, NotificationType, iso, Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibIdentifier", "TimeTicks", "NotificationType", "iso", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "Counter32")
MacAddress, TimeInterval, TruthValue, DateAndTime, TimeStamp, DisplayString, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeInterval", "TruthValue", "DateAndTime", "TimeStamp", "DisplayString", "TextualConvention", "RowPointer")
cucsGraphicsObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73))
if mibBuilder.loadTexts: cucsGraphicsObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsGraphicsObjects.setOrganization('Cisco Systems Inc.')
cucsGraphicsCardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1), )
if mibBuilder.loadTexts: cucsGraphicsCardTable.setStatus('current')
cucsGraphicsCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB", "cucsGraphicsCardInstanceId"))
if mibBuilder.loadTexts: cucsGraphicsCardEntry.setStatus('current')
cucsGraphicsCardInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGraphicsCardInstanceId.setStatus('current')
cucsGraphicsCardDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardDn.setStatus('current')
cucsGraphicsCardRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardRn.setStatus('current')
cucsGraphicsCardDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardDeviceId.setStatus('current')
cucsGraphicsCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardId.setStatus('current')
cucsGraphicsCardIsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardIsSupported.setStatus('current')
cucsGraphicsCardLc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 7), CucsFsmLifecycle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardLc.setStatus('current')
cucsGraphicsCardModel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardModel.setStatus('current')
cucsGraphicsCardOperQualifierReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardOperQualifierReason.setStatus('current')
cucsGraphicsCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 10), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardOperState.setStatus('current')
cucsGraphicsCardOperability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 11), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardOperability.setStatus('current')
cucsGraphicsCardPciAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPciAddr.setStatus('current')
cucsGraphicsCardPciSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPciSlot.setStatus('current')
cucsGraphicsCardPerf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 14), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPerf.setStatus('current')
cucsGraphicsCardPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 15), CucsEquipmentPowerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPower.setStatus('current')
cucsGraphicsCardPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 16), CucsEquipmentPresence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPresence.setStatus('current')
cucsGraphicsCardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 17), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardRevision.setStatus('current')
cucsGraphicsCardSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 18), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardSerial.setStatus('current')
cucsGraphicsCardSubDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardSubDeviceId.setStatus('current')
cucsGraphicsCardSubVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardSubVendorId.setStatus('current')
cucsGraphicsCardThermal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 21), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardThermal.setStatus('current')
cucsGraphicsCardVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 22), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardVendor.setStatus('current')
cucsGraphicsCardVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardVendorId.setStatus('current')
cucsGraphicsCardVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 24), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardVoltage.setStatus('current')
cucsGraphicsCardLocationDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 25), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardLocationDn.setStatus('current')
cucsGraphicsCardStepping = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 26), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardStepping.setStatus('current')
cucsGraphicsCardExpanderSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 27), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardExpanderSlot.setStatus('current')
cucsGraphicsCardFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 28), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardFirmwareVersion.setStatus('current')
cucsGraphicsCardPciAddrList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 29), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsCardPciAddrList.setStatus('current')
cucsGraphicsControllerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2), )
if mibBuilder.loadTexts: cucsGraphicsControllerTable.setStatus('current')
cucsGraphicsControllerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB", "cucsGraphicsControllerInstanceId"))
if mibBuilder.loadTexts: cucsGraphicsControllerEntry.setStatus('current')
cucsGraphicsControllerInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsGraphicsControllerInstanceId.setStatus('current')
cucsGraphicsControllerDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerDn.setStatus('current')
cucsGraphicsControllerRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerRn.setStatus('current')
cucsGraphicsControllerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerId.setStatus('current')
cucsGraphicsControllerModel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerModel.setStatus('current')
cucsGraphicsControllerOperQualifierReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerOperQualifierReason.setStatus('current')
cucsGraphicsControllerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 7), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerOperState.setStatus('current')
cucsGraphicsControllerOperability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 8), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerOperability.setStatus('current')
cucsGraphicsControllerPciAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerPciAddr.setStatus('current')
cucsGraphicsControllerPciSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerPciSlot.setStatus('current')
cucsGraphicsControllerPerf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 11), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerPerf.setStatus('current')
cucsGraphicsControllerPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 12), CucsEquipmentPowerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerPower.setStatus('current')
cucsGraphicsControllerPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 13), CucsEquipmentPresence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerPresence.setStatus('current')
cucsGraphicsControllerRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerRevision.setStatus('current')
cucsGraphicsControllerSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerSerial.setStatus('current')
cucsGraphicsControllerThermal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 16), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerThermal.setStatus('current')
cucsGraphicsControllerVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 17), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerVendor.setStatus('current')
cucsGraphicsControllerVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 18), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerVoltage.setStatus('current')
cucsGraphicsControllerLocationDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 19), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsGraphicsControllerLocationDn.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB", cucsGraphicsCardSubVendorId=cucsGraphicsCardSubVendorId, cucsGraphicsControllerVoltage=cucsGraphicsControllerVoltage, cucsGraphicsCardPciSlot=cucsGraphicsCardPciSlot, cucsGraphicsControllerThermal=cucsGraphicsControllerThermal, cucsGraphicsControllerVendor=cucsGraphicsControllerVendor, cucsGraphicsCardDn=cucsGraphicsCardDn, PYSNMP_MODULE_ID=cucsGraphicsObjects, cucsGraphicsControllerRevision=cucsGraphicsControllerRevision, cucsGraphicsCardLocationDn=cucsGraphicsCardLocationDn, cucsGraphicsControllerInstanceId=cucsGraphicsControllerInstanceId, cucsGraphicsCardPerf=cucsGraphicsCardPerf, cucsGraphicsCardVoltage=cucsGraphicsCardVoltage, cucsGraphicsCardModel=cucsGraphicsCardModel, cucsGraphicsCardSerial=cucsGraphicsCardSerial, cucsGraphicsCardId=cucsGraphicsCardId, cucsGraphicsCardFirmwareVersion=cucsGraphicsCardFirmwareVersion, cucsGraphicsControllerOperState=cucsGraphicsControllerOperState, cucsGraphicsControllerPciAddr=cucsGraphicsControllerPciAddr, cucsGraphicsControllerPerf=cucsGraphicsControllerPerf, cucsGraphicsCardPciAddr=cucsGraphicsCardPciAddr, cucsGraphicsCardVendorId=cucsGraphicsCardVendorId, cucsGraphicsControllerPciSlot=cucsGraphicsControllerPciSlot, cucsGraphicsControllerModel=cucsGraphicsControllerModel, cucsGraphicsControllerId=cucsGraphicsControllerId, cucsGraphicsCardIsSupported=cucsGraphicsCardIsSupported, cucsGraphicsControllerRn=cucsGraphicsControllerRn, cucsGraphicsObjects=cucsGraphicsObjects, cucsGraphicsCardRevision=cucsGraphicsCardRevision, cucsGraphicsControllerLocationDn=cucsGraphicsControllerLocationDn, cucsGraphicsCardSubDeviceId=cucsGraphicsCardSubDeviceId, cucsGraphicsCardDeviceId=cucsGraphicsCardDeviceId, cucsGraphicsCardOperState=cucsGraphicsCardOperState, cucsGraphicsCardTable=cucsGraphicsCardTable, cucsGraphicsCardThermal=cucsGraphicsCardThermal, cucsGraphicsCardExpanderSlot=cucsGraphicsCardExpanderSlot, cucsGraphicsCardPciAddrList=cucsGraphicsCardPciAddrList, cucsGraphicsControllerEntry=cucsGraphicsControllerEntry, cucsGraphicsControllerSerial=cucsGraphicsControllerSerial, cucsGraphicsCardInstanceId=cucsGraphicsCardInstanceId, cucsGraphicsCardPresence=cucsGraphicsCardPresence, cucsGraphicsControllerTable=cucsGraphicsControllerTable, cucsGraphicsCardPower=cucsGraphicsCardPower, cucsGraphicsCardEntry=cucsGraphicsCardEntry, cucsGraphicsControllerOperability=cucsGraphicsControllerOperability, cucsGraphicsCardVendor=cucsGraphicsCardVendor, cucsGraphicsCardOperQualifierReason=cucsGraphicsCardOperQualifierReason, cucsGraphicsControllerOperQualifierReason=cucsGraphicsControllerOperQualifierReason, cucsGraphicsControllerPower=cucsGraphicsControllerPower, cucsGraphicsCardStepping=cucsGraphicsCardStepping, cucsGraphicsControllerDn=cucsGraphicsControllerDn, cucsGraphicsCardOperability=cucsGraphicsCardOperability, cucsGraphicsCardRn=cucsGraphicsCardRn, cucsGraphicsCardLc=cucsGraphicsCardLc, cucsGraphicsControllerPresence=cucsGraphicsControllerPresence)
