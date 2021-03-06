#
# PySNMP MIB module BTI7800-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-INVENTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, MibIdentifier, Unsigned32, Gauge32, NotificationType, Bits, Counter32, Counter64, iso, TimeTicks, ModuleIdentity, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibIdentifier", "Unsigned32", "Gauge32", "NotificationType", "Bits", "Counter32", "Counter64", "iso", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
bTI7800_INVENTORY_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2)).setLabel("bTI7800-INVENTORY-MIB")
bTI7800_INVENTORY_MIB.setRevisions(('2014-12-23 00:00',))
if mibBuilder.loadTexts: bTI7800_INVENTORY_MIB.setLastUpdated('201412230000Z')
if mibBuilder.loadTexts: bTI7800_INVENTORY_MIB.setOrganization('@ORGANIZATION')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class BicIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2)

class FanIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 6)

class PemIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class CmmIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2)

class PortIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 12)

class ModuleIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 14)

class ChassisIndexT(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

inventory_chassisTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1), ).setLabel("inventory-chassisTable")
if mibBuilder.loadTexts: inventory_chassisTable.setStatus('current')
inventory_chassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1), ).setLabel("inventory-chassisEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-chassisChassisNum"))
if mibBuilder.loadTexts: inventory_chassisEntry.setStatus('current')
inventory_chassisChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 1), ChassisIndexT()).setLabel("inventory-chassisChassisNum")
if mibBuilder.loadTexts: inventory_chassisChassisNum.setStatus('current')
inventory_chassisName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 2), String()).setLabel("inventory-chassisName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisName.setStatus('current')
inventory_chassisPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 3), String()).setLabel("inventory-chassisPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisPEC.setStatus('current')
inventory_chassisRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 4), UnsignedShort()).setLabel("inventory-chassisRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisRevision.setStatus('current')
inventory_chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 5), String()).setLabel("inventory-chassisSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisSerialNumber.setStatus('current')
inventory_chassisManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 6), DateAndTime()).setLabel("inventory-chassisManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisManufactureDate.setStatus('current')
inventory_chassisVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 1, 1, 7), String()).setLabel("inventory-chassisVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_chassisVendor.setStatus('current')
inventory_fanTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2), ).setLabel("inventory-fanTable")
if mibBuilder.loadTexts: inventory_fanTable.setStatus('current')
inventory_fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1), ).setLabel("inventory-fanEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-fanChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-fanSlotNum"))
if mibBuilder.loadTexts: inventory_fanEntry.setStatus('current')
inventory_fanChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 1), ChassisIndexT()).setLabel("inventory-fanChassisNum")
if mibBuilder.loadTexts: inventory_fanChassisNum.setStatus('current')
inventory_fanSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 2), FanIndexT()).setLabel("inventory-fanSlotNum")
if mibBuilder.loadTexts: inventory_fanSlotNum.setStatus('current')
inventory_fanName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 3), String()).setLabel("inventory-fanName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanName.setStatus('current')
inventory_fanPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 4), String()).setLabel("inventory-fanPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanPEC.setStatus('current')
inventory_fanRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 5), UnsignedShort()).setLabel("inventory-fanRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanRevision.setStatus('current')
inventory_fanSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 6), String()).setLabel("inventory-fanSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanSerialNumber.setStatus('current')
inventory_fanManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 7), DateAndTime()).setLabel("inventory-fanManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanManufactureDate.setStatus('current')
inventory_fanVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 2, 1, 8), String()).setLabel("inventory-fanVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_fanVendor.setStatus('current')
inventory_pemTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3), ).setLabel("inventory-pemTable")
if mibBuilder.loadTexts: inventory_pemTable.setStatus('current')
inventory_pemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1), ).setLabel("inventory-pemEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-pemChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-pemSlotNum"))
if mibBuilder.loadTexts: inventory_pemEntry.setStatus('current')
inventory_pemChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 1), ChassisIndexT()).setLabel("inventory-pemChassisNum")
if mibBuilder.loadTexts: inventory_pemChassisNum.setStatus('current')
inventory_pemSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 2), PemIndexT()).setLabel("inventory-pemSlotNum")
if mibBuilder.loadTexts: inventory_pemSlotNum.setStatus('current')
inventory_pemName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 3), String()).setLabel("inventory-pemName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemName.setStatus('current')
inventory_pemPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 4), String()).setLabel("inventory-pemPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemPEC.setStatus('current')
inventory_pemRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 5), UnsignedShort()).setLabel("inventory-pemRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemRevision.setStatus('current')
inventory_pemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 6), String()).setLabel("inventory-pemSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemSerialNumber.setStatus('current')
inventory_pemManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 7), DateAndTime()).setLabel("inventory-pemManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemManufactureDate.setStatus('current')
inventory_pemVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 3, 1, 8), String()).setLabel("inventory-pemVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_pemVendor.setStatus('current')
inventory_cmmTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4), ).setLabel("inventory-cmmTable")
if mibBuilder.loadTexts: inventory_cmmTable.setStatus('current')
inventory_cmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1), ).setLabel("inventory-cmmEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-cmmChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-cmmSlotNum"))
if mibBuilder.loadTexts: inventory_cmmEntry.setStatus('current')
inventory_cmmChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 1), ChassisIndexT()).setLabel("inventory-cmmChassisNum")
if mibBuilder.loadTexts: inventory_cmmChassisNum.setStatus('current')
inventory_cmmSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 2), CmmIndexT()).setLabel("inventory-cmmSlotNum")
if mibBuilder.loadTexts: inventory_cmmSlotNum.setStatus('current')
inventory_cmmName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 3), String()).setLabel("inventory-cmmName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmName.setStatus('current')
inventory_cmmPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 4), String()).setLabel("inventory-cmmPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmPEC.setStatus('current')
inventory_cmmRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 5), UnsignedShort()).setLabel("inventory-cmmRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmRevision.setStatus('current')
inventory_cmmSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 6), String()).setLabel("inventory-cmmSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmSerialNumber.setStatus('current')
inventory_cmmManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 7), DateAndTime()).setLabel("inventory-cmmManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmManufactureDate.setStatus('current')
inventory_cmmVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 4, 1, 8), String()).setLabel("inventory-cmmVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_cmmVendor.setStatus('current')
inventory_moduleTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5), ).setLabel("inventory-moduleTable")
if mibBuilder.loadTexts: inventory_moduleTable.setStatus('current')
inventory_moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1), ).setLabel("inventory-moduleEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-moduleChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-moduleSlotNum"))
if mibBuilder.loadTexts: inventory_moduleEntry.setStatus('current')
inventory_moduleChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 1), ChassisIndexT()).setLabel("inventory-moduleChassisNum")
if mibBuilder.loadTexts: inventory_moduleChassisNum.setStatus('current')
inventory_moduleSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 2), ModuleIndexT()).setLabel("inventory-moduleSlotNum")
if mibBuilder.loadTexts: inventory_moduleSlotNum.setStatus('current')
inventory_moduleName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 3), String()).setLabel("inventory-moduleName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_moduleName.setStatus('current')
inventory_modulePEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 4), String()).setLabel("inventory-modulePEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_modulePEC.setStatus('current')
inventory_moduleRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 5), UnsignedShort()).setLabel("inventory-moduleRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_moduleRevision.setStatus('current')
inventory_moduleSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 6), String()).setLabel("inventory-moduleSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_moduleSerialNumber.setStatus('current')
inventory_moduleManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 7), DateAndTime()).setLabel("inventory-moduleManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_moduleManufactureDate.setStatus('current')
inventory_moduleVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 5, 1, 8), String()).setLabel("inventory-moduleVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_moduleVendor.setStatus('current')
inventory_bicTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6), ).setLabel("inventory-bicTable")
if mibBuilder.loadTexts: inventory_bicTable.setStatus('current')
inventory_bicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1), ).setLabel("inventory-bicEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-bicChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-bicSlotNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-bicSubslotNum"))
if mibBuilder.loadTexts: inventory_bicEntry.setStatus('current')
inventory_bicChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 1), ChassisIndexT()).setLabel("inventory-bicChassisNum")
if mibBuilder.loadTexts: inventory_bicChassisNum.setStatus('current')
inventory_bicSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 2), ModuleIndexT()).setLabel("inventory-bicSlotNum")
if mibBuilder.loadTexts: inventory_bicSlotNum.setStatus('current')
inventory_bicSubslotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 3), BicIndexT()).setLabel("inventory-bicSubslotNum")
if mibBuilder.loadTexts: inventory_bicSubslotNum.setStatus('current')
inventory_bicName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 4), String()).setLabel("inventory-bicName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicName.setStatus('current')
inventory_bicPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 5), String()).setLabel("inventory-bicPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicPEC.setStatus('current')
inventory_bicRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 6), UnsignedShort()).setLabel("inventory-bicRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicRevision.setStatus('current')
inventory_bicSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 7), String()).setLabel("inventory-bicSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicSerialNumber.setStatus('current')
inventory_bicManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 8), DateAndTime()).setLabel("inventory-bicManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicManufactureDate.setStatus('current')
inventory_bicVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 6, 1, 9), String()).setLabel("inventory-bicVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_bicVendor.setStatus('current')
inventory_xcvrTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7), ).setLabel("inventory-xcvrTable")
if mibBuilder.loadTexts: inventory_xcvrTable.setStatus('current')
inventory_xcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1), ).setLabel("inventory-xcvrEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-xcvrChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrSlotNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrSubslotNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-xcvrPortNum"))
if mibBuilder.loadTexts: inventory_xcvrEntry.setStatus('current')
inventory_xcvrChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 1), ChassisIndexT()).setLabel("inventory-xcvrChassisNum")
if mibBuilder.loadTexts: inventory_xcvrChassisNum.setStatus('current')
inventory_xcvrSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 2), ModuleIndexT()).setLabel("inventory-xcvrSlotNum")
if mibBuilder.loadTexts: inventory_xcvrSlotNum.setStatus('current')
inventory_xcvrSubslotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 3), BicIndexT()).setLabel("inventory-xcvrSubslotNum")
if mibBuilder.loadTexts: inventory_xcvrSubslotNum.setStatus('current')
inventory_xcvrPortNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 4), PortIndexT()).setLabel("inventory-xcvrPortNum")
if mibBuilder.loadTexts: inventory_xcvrPortNum.setStatus('current')
inventory_xcvrName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 5), String()).setLabel("inventory-xcvrName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrName.setStatus('current')
inventory_xcvrPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 6), String()).setLabel("inventory-xcvrPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrPEC.setStatus('current')
inventory_xcvrRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 7), UnsignedShort()).setLabel("inventory-xcvrRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrRevision.setStatus('current')
inventory_xcvrSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 8), String()).setLabel("inventory-xcvrSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrSerialNumber.setStatus('current')
inventory_xcvrManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 9), DateAndTime()).setLabel("inventory-xcvrManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrManufactureDate.setStatus('current')
inventory_xcvrVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 10), String()).setLabel("inventory-xcvrVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrVendor.setStatus('current')
inventory_xcvrVendorPartNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 11), String()).setLabel("inventory-xcvrVendorPartNum").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrVendorPartNum.setStatus('current')
inventory_xcvrType = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 7, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("sfp", 1), ("sfpPlus", 2), ("cfp", 3), ("msa", 4), ("qsfp", 5), ("qsfp28", 6), ("msa400", 7)))).setLabel("inventory-xcvrType").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_xcvrType.setStatus('current')
inventory_preampTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8), ).setLabel("inventory-preampTable")
if mibBuilder.loadTexts: inventory_preampTable.setStatus('current')
inventory_preampEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1), ).setLabel("inventory-preampEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-preampChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-preampSlotNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-preampSubslotNum"))
if mibBuilder.loadTexts: inventory_preampEntry.setStatus('current')
inventory_preampChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 1), ChassisIndexT()).setLabel("inventory-preampChassisNum")
if mibBuilder.loadTexts: inventory_preampChassisNum.setStatus('current')
inventory_preampSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 2), ModuleIndexT()).setLabel("inventory-preampSlotNum")
if mibBuilder.loadTexts: inventory_preampSlotNum.setStatus('current')
inventory_preampSubslotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 3), BicIndexT()).setLabel("inventory-preampSubslotNum")
if mibBuilder.loadTexts: inventory_preampSubslotNum.setStatus('current')
inventory_preampName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 4), String()).setLabel("inventory-preampName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampName.setStatus('current')
inventory_preampPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 5), String()).setLabel("inventory-preampPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampPEC.setStatus('current')
inventory_preampRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 6), UnsignedShort()).setLabel("inventory-preampRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampRevision.setStatus('current')
inventory_preampSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 7), String()).setLabel("inventory-preampSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampSerialNumber.setStatus('current')
inventory_preampManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 8), DateAndTime()).setLabel("inventory-preampManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampManufactureDate.setStatus('current')
inventory_preampVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 8, 1, 9), String()).setLabel("inventory-preampVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_preampVendor.setStatus('current')
inventory_eslTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9), ).setLabel("inventory-eslTable")
if mibBuilder.loadTexts: inventory_eslTable.setStatus('current')
inventory_eslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1), ).setLabel("inventory-eslEntry").setIndexNames((0, "BTI7800-INVENTORY-MIB", "inventory-eslChassisNum"), (0, "BTI7800-INVENTORY-MIB", "inventory-eslSlotNum"))
if mibBuilder.loadTexts: inventory_eslEntry.setStatus('current')
inventory_eslChassisNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 1), ChassisIndexT()).setLabel("inventory-eslChassisNum")
if mibBuilder.loadTexts: inventory_eslChassisNum.setStatus('current')
inventory_eslSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 2), UnsignedByte()).setLabel("inventory-eslSlotNum")
if mibBuilder.loadTexts: inventory_eslSlotNum.setStatus('current')
inventory_eslName = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 3), String()).setLabel("inventory-eslName").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslName.setStatus('current')
inventory_eslPEC = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 4), String()).setLabel("inventory-eslPEC").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslPEC.setStatus('current')
inventory_eslRevision = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 5), UnsignedShort()).setLabel("inventory-eslRevision").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslRevision.setStatus('current')
inventory_eslSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 6), String()).setLabel("inventory-eslSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslSerialNumber.setStatus('current')
inventory_eslManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 7), DateAndTime()).setLabel("inventory-eslManufactureDate").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslManufactureDate.setStatus('current')
inventory_eslVendor = MibScalar((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 2, 9, 1, 8), String()).setLabel("inventory-eslVendor").setMaxAccess("readonly")
if mibBuilder.loadTexts: inventory_eslVendor.setStatus('current')
mibBuilder.exportSymbols("BTI7800-INVENTORY-MIB", inventory_cmmRevision=inventory_cmmRevision, inventory_eslTable=inventory_eslTable, inventory_xcvrSerialNumber=inventory_xcvrSerialNumber, inventory_pemPEC=inventory_pemPEC, inventory_xcvrSlotNum=inventory_xcvrSlotNum, inventory_cmmPEC=inventory_cmmPEC, inventory_pemName=inventory_pemName, inventory_eslSlotNum=inventory_eslSlotNum, FanIndexT=FanIndexT, inventory_moduleSerialNumber=inventory_moduleSerialNumber, inventory_bicName=inventory_bicName, inventory_fanChassisNum=inventory_fanChassisNum, inventory_eslRevision=inventory_eslRevision, inventory_xcvrTable=inventory_xcvrTable, String=String, inventory_chassisName=inventory_chassisName, inventory_fanManufactureDate=inventory_fanManufactureDate, inventory_xcvrEntry=inventory_xcvrEntry, inventory_eslChassisNum=inventory_eslChassisNum, inventory_moduleTable=inventory_moduleTable, inventory_preampVendor=inventory_preampVendor, inventory_pemTable=inventory_pemTable, inventory_xcvrPortNum=inventory_xcvrPortNum, inventory_preampRevision=inventory_preampRevision, inventory_preampSlotNum=inventory_preampSlotNum, inventory_fanName=inventory_fanName, inventory_preampSerialNumber=inventory_preampSerialNumber, inventory_moduleVendor=inventory_moduleVendor, inventory_eslName=inventory_eslName, inventory_bicRevision=inventory_bicRevision, inventory_cmmManufactureDate=inventory_cmmManufactureDate, inventory_preampManufactureDate=inventory_preampManufactureDate, inventory_moduleSlotNum=inventory_moduleSlotNum, inventory_cmmEntry=inventory_cmmEntry, inventory_bicSubslotNum=inventory_bicSubslotNum, inventory_pemManufactureDate=inventory_pemManufactureDate, inventory_xcvrSubslotNum=inventory_xcvrSubslotNum, inventory_bicManufactureDate=inventory_bicManufactureDate, ConfdString=ConfdString, inventory_pemVendor=inventory_pemVendor, inventory_fanSlotNum=inventory_fanSlotNum, inventory_pemSlotNum=inventory_pemSlotNum, inventory_pemChassisNum=inventory_pemChassisNum, inventory_fanEntry=inventory_fanEntry, inventory_cmmChassisNum=inventory_cmmChassisNum, inventory_cmmTable=inventory_cmmTable, inventory_cmmName=inventory_cmmName, UnsignedByte=UnsignedByte, inventory_eslVendor=inventory_eslVendor, PortIndexT=PortIndexT, inventory_cmmSlotNum=inventory_cmmSlotNum, inventory_eslPEC=inventory_eslPEC, ChassisIndexT=ChassisIndexT, inventory_bicEntry=inventory_bicEntry, inventory_preampEntry=inventory_preampEntry, inventory_bicPEC=inventory_bicPEC, inventory_chassisSerialNumber=inventory_chassisSerialNumber, inventory_preampName=inventory_preampName, inventory_xcvrVendorPartNum=inventory_xcvrVendorPartNum, inventory_xcvrType=inventory_xcvrType, inventory_bicChassisNum=inventory_bicChassisNum, inventory_moduleRevision=inventory_moduleRevision, inventory_preampSubslotNum=inventory_preampSubslotNum, inventory_pemEntry=inventory_pemEntry, inventory_xcvrPEC=inventory_xcvrPEC, inventory_xcvrManufactureDate=inventory_xcvrManufactureDate, CmmIndexT=CmmIndexT, inventory_modulePEC=inventory_modulePEC, inventory_moduleManufactureDate=inventory_moduleManufactureDate, inventory_xcvrChassisNum=inventory_xcvrChassisNum, inventory_chassisEntry=inventory_chassisEntry, inventory_chassisManufactureDate=inventory_chassisManufactureDate, inventory_moduleEntry=inventory_moduleEntry, inventory_fanSerialNumber=inventory_fanSerialNumber, inventory_cmmVendor=inventory_cmmVendor, inventory_eslManufactureDate=inventory_eslManufactureDate, InetAddressIP=InetAddressIP, inventory_pemSerialNumber=inventory_pemSerialNumber, inventory_preampChassisNum=inventory_preampChassisNum, inventory_fanRevision=inventory_fanRevision, inventory_moduleChassisNum=inventory_moduleChassisNum, inventory_xcvrVendor=inventory_xcvrVendor, inventory_bicTable=inventory_bicTable, inventory_preampTable=inventory_preampTable, inventory_eslEntry=inventory_eslEntry, PYSNMP_MODULE_ID=bTI7800_INVENTORY_MIB, inventory_chassisPEC=inventory_chassisPEC, inventory_xcvrRevision=inventory_xcvrRevision, inventory_chassisChassisNum=inventory_chassisChassisNum, inventory_preampPEC=inventory_preampPEC, inventory_xcvrName=inventory_xcvrName, inventory_bicVendor=inventory_bicVendor, inventory_bicSerialNumber=inventory_bicSerialNumber, inventory_cmmSerialNumber=inventory_cmmSerialNumber, inventory_chassisTable=inventory_chassisTable, inventory_chassisRevision=inventory_chassisRevision, PemIndexT=PemIndexT, inventory_bicSlotNum=inventory_bicSlotNum, inventory_eslSerialNumber=inventory_eslSerialNumber, UnsignedShort=UnsignedShort, inventory_pemRevision=inventory_pemRevision, inventory_fanTable=inventory_fanTable, inventory_moduleName=inventory_moduleName, BicIndexT=BicIndexT, bTI7800_INVENTORY_MIB=bTI7800_INVENTORY_MIB, inventory_fanPEC=inventory_fanPEC, inventory_chassisVendor=inventory_chassisVendor, inventory_fanVendor=inventory_fanVendor, ModuleIndexT=ModuleIndexT)
