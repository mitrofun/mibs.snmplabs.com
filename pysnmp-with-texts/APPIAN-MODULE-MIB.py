#
# PySNMP MIB module APPIAN-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-MODULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acChassisCurrentTime, acChassisRingId = mibBuilder.importSymbols("APPIAN-CHASSIS-MIB", "acChassisCurrentTime", "acChassisRingId")
AcNodeId, acOsap, AcOpStatus, AcAdminStatus, AcSwVersion, AcSlotNumber = mibBuilder.importSymbols("APPIAN-SMI-MIB", "AcNodeId", "acOsap", "AcOpStatus", "AcAdminStatus", "AcSwVersion", "AcSlotNumber")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, TimeTicks, IpAddress, Gauge32, ModuleIdentity, Integer32, MibIdentifier, Counter64, ObjectIdentity, iso, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier", "Counter64", "ObjectIdentity", "iso", "Bits", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
acModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 2))
acModule.setRevisions(('1999-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acModule.setRevisionsDescriptions(('Draft MIB for Engineering use only.',))
if mibBuilder.loadTexts: acModule.setLastUpdated('9911040000Z')
if mibBuilder.loadTexts: acModule.setOrganization('Appian Communications, Inc.')
if mibBuilder.loadTexts: acModule.setContactInfo('Douglas Theriault')
if mibBuilder.loadTexts: acModule.setDescription('Appian Communications OSAP Modules MIB contain the definitions for module hardware information and status.')
class AcModuleType(TextualConvention, Integer32):
    description = 'List of module types currently supported on the OSAP platform. Some details of certain types are shown below: Note that the designation in parentheses is connector style gbe-sx - built with 8 ports of short-reach multi-mode (MT_RJ) gbe-lx - built with 8 ports of intermediate-reach single-mode laser gbe-sfp - built with 8 Small Form-factor Pluggable transceivers Note: This card will use instances of acPfot to describe each port oc3-ir-1 - built with 1 intermediate-reach oc-3 port (SC) oc3-ir-2 - built with 2 intermediate-reach oc-3 port2 (SC) oc3-sr-1 - built with 1 short-reach oc-3 port (SC) oc3-sr-2 - built with 2 short-reach oc-3 ports (SC) oc3-lr-1 - built with 1 long-reach oc-3 port (SC) oc3-lr-2 - built with 2 long-reach oc-3 ports (SC) oc3c-ir-4 - built with 4 intermediate-reach oc-3c ports (LC) oc12-ir-1-oc3c-ir-4 - built with 1 intermediate reach oc12 port (LC) and 4 intermediate-reach oc3c ports (LC) oc12-ir-1 - built with 1 intermediate-reach oc-12 port (SC) oc12-ir-2 - built with 2 intermediate-reach oc-12 ports (SC) oc12-lr-1 - built with 1 long-reach oc-12 port (SC) oc12-lr-2 - built with 2 long-reach oc-12 ports (SC) oc48-ir-1-oc12-ir-4 - built with 1 intermediate reach oc48 port (LC) and 4 intermediate-reach oc12 ports (LC) oc48-ir-1 - built with 1 intermediate-reach oc-48 port (SC) oc48-ir-2 - built with 2 intermediate-reach oc-48 ports (SC) oc48-lr-1 - built with 1 long-reach oc-48 port (SC) oc48-lr-2 - built with 2 long-reach oc-48 ports (SC)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37))
    namedValues = NamedValues(("unknown", 0), ("not-present", 1), ("bits-s3", 2), ("svcproc-1", 3), ("fe16-mc", 4), ("fe8-tx-io", 5), ("fe8-fx-io", 6), ("gbe-sx", 7), ("gbe-lx", 8), ("gbe-sfp", 9), ("oc48-ir-2", 10), ("oc48-ir-1", 11), ("ds1-14-mc", 12), ("ds1-7-io", 13), ("ds3-network", 14), ("ds3-access", 15), ("ds3-io", 16), ("oc3-ir-1", 17), ("oc3-ir-2", 18), ("oc3-sr-1", 19), ("oc3-sr-2", 20), ("oc3-lr-1", 21), ("oc3-lr-2", 22), ("oc3c-ir-4", 23), ("oc12-ir-1-oc3c-ir-4", 24), ("oc12-ir-1", 25), ("oc12-ir-2", 26), ("oc12-ir-4", 27), ("oc12-lr-1", 28), ("oc12-lr-2", 29), ("oc48-ir-1-oc12-ir-4", 30), ("oc48-lr-2", 31), ("oc48-lr-1", 32), ("e1", 33), ("e1-io", 34), ("e3", 35), ("e3-io", 36), ("enet-agg", 37))

class AcModuleNumber(TextualConvention, Integer32):
    description = 'A module number in an OSAP Chassis which is within the range of (1..2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2)

class AcMediaSlotNumber(TextualConvention, Integer32):
    description = 'A slot number in an OSAP Chassis which is within the range of (0..9). This type indicates the slot number for a media card in the OSAP chassis and is in the range 5-9 if valid, and 0 if not valid.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

acModuleTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1), )
if mibBuilder.loadTexts: acModuleTable.setStatus('current')
if mibBuilder.loadTexts: acModuleTable.setDescription('A table containing the module information for each module within the chassis. This table is automatically created during system initialization and updated when modules are removed and inserted. When a module is removed, the row is automatically removed.')
acModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1), ).setIndexNames((0, "APPIAN-MODULE-MIB", "acModuleNodeId"), (0, "APPIAN-MODULE-MIB", "acModuleSlot"), (0, "APPIAN-MODULE-MIB", "acModuleNumber"))
if mibBuilder.loadTexts: acModuleEntry.setStatus('current')
if mibBuilder.loadTexts: acModuleEntry.setDescription("Module information record containing hardware, software, firmware, name data for a specific node.slot within a chassis. Row's in this table are automatically instantiated at system initialization.")
acModuleNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 1), AcNodeId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acModuleNodeId.setStatus('current')
if mibBuilder.loadTexts: acModuleNodeId.setDescription("The unique node identification number representing a chassis within a ring of OSAP's.")
acModuleSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 2), AcSlotNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acModuleSlot.setStatus('current')
if mibBuilder.loadTexts: acModuleSlot.setDescription('The slot number within the chassis where this module resides.')
acModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 3), AcModuleNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acModuleNumber.setStatus('current')
if mibBuilder.loadTexts: acModuleNumber.setDescription('The module number within the slot where this module resides.')
acModuleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 4), AcAdminStatus().clone('inactivate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acModuleAdminStatus.setStatus('current')
if mibBuilder.loadTexts: acModuleAdminStatus.setDescription('The administrative status. See AcAdminStatus for the semantics.')
acModuleCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 5), AcModuleType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acModuleCfgType.setStatus('current')
if mibBuilder.loadTexts: acModuleCfgType.setDescription('The acModuleCfgType field enumeration is used to uniquely identify the module type which is currently in a slot within the chassis, as defined by the AppianVista EMS.')
acModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 6), AcModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleType.setStatus('current')
if mibBuilder.loadTexts: acModuleType.setDescription('The acModuleType field enumeration is used to uniquely identify the module type which is currently in a slot within the chassis.')
acModuleOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 7), AcOpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleOpStatus.setStatus('current')
if mibBuilder.loadTexts: acModuleOpStatus.setDescription('This field indicates the current operational status for the module. Only the following values are applicable to the module: operational, offline, initializing, selfTesting, upgrading, standby, shuttingDown and failed.')
acModuleRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleRevision.setStatus('current')
if mibBuilder.loadTexts: acModuleRevision.setDescription('Contains the manufacturing revision number for this module.')
acModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleSerialNumber.setStatus('current')
if mibBuilder.loadTexts: acModuleSerialNumber.setDescription('A display string representing the manufacturing serial number as stored in the modules I2C prom.')
acModuleProductionDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleProductionDate.setStatus('current')
if mibBuilder.loadTexts: acModuleProductionDate.setDescription('The date code when this module was manufactured. This field is read-only and set by manufacturing in the I2C prom. The format used is YYWW; with YY = year and WW = week.')
acModuleFirmwareName = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleFirmwareName.setStatus('current')
if mibBuilder.loadTexts: acModuleFirmwareName.setDescription('This string contains the name of the firmware file resident on the switch controller file system. Note: Not all modules contain firmware.')
acModuleFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: acModuleFirmwareRevision.setDescription('The revision of the firmware.')
acModuleNumberFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleNumberFailures.setStatus('current')
if mibBuilder.loadTexts: acModuleNumberFailures.setDescription('The total number of failure events reported by the module.')
acModuleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acModuleReset.setStatus('current')
if mibBuilder.loadTexts: acModuleReset.setDescription('This field allows the user to reset a specified module within the chassis. Note: If resetting the active SCP on which the management session is active, loss of connection will result as the standby SCP gains control.')
acModuleNumberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleNumberPorts.setStatus('current')
if mibBuilder.loadTexts: acModuleNumberPorts.setDescription('A count of the total number of ports located on this module. Not all modules contain user configurable or usable ports.')
acModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleName.setStatus('current')
if mibBuilder.loadTexts: acModuleName.setDescription('The official human readable name for the type of module indicated by acModuleType.')
acModuleSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 17), AcSwVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleSwVersion.setStatus('current')
if mibBuilder.loadTexts: acModuleSwVersion.setDescription('The current software version if any which is operational on this module. This attribute will be NULL if the physical module does not execute a software image (re: it is controlled by the switch controller).')
acModuleDiagTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("basic", 1), ("advanced", 2), ("stress", 3))).clone('basic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acModuleDiagTestMode.setStatus('current')
if mibBuilder.loadTexts: acModuleDiagTestMode.setDescription('The diagnostics test mode allows the user to select a basic(1), advanced(2) or stress(3) series of powerup self tests to be run when the acModuleOpStatus field is changed to selfTesting(4). A basic(1) test performs a quick self test and is the mode which is by default selected at powerup. Advanced(2) mode is used to run a more thorough series of tests and stress(3) mode is used to execute a system test packet loopback type of powerup test. In all test modes, the acModuleDiagStatus field contains a unique results code (Refer to diagnostics utility guide). The results of a test request is also written as a string to the acModuleDiagResultString field.')
acModuleDiagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleDiagStatus.setStatus('current')
if mibBuilder.loadTexts: acModuleDiagStatus.setDescription('The unique results code as returned from the test mode issued via acModuleDiagTestMode. Refer to the diagnostic utility guide for details.')
acModuleDiagResultString = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleDiagResultString.setStatus('current')
if mibBuilder.loadTexts: acModuleDiagResultString.setDescription('The results of the diagnostic test returned as a printable ASCII string. Refer to the diagnostics utility guide for details.')
acModuleActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 21), AcMediaSlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleActiveSlot.setStatus('current')
if mibBuilder.loadTexts: acModuleActiveSlot.setDescription('The slot number within the chassis where the media module that is driving this module resides. This attribute is set to 0 for rows in which the module is either not an IO card or is an IO card that has no appropriate media card present in the chassis.')
acModulePrimarySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 22), AcMediaSlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModulePrimarySlot.setStatus('current')
if mibBuilder.loadTexts: acModulePrimarySlot.setDescription('The slot number within the chassis where the primary media module that could drive this module resides. This attribute is set to 0 for rows in which the module is either not an IO card or is an IO card that has no appropriate media card present in the chassis.')
acModuleBackupSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 2, 1, 1, 23), AcMediaSlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModuleBackupSlot.setStatus('current')
if mibBuilder.loadTexts: acModuleBackupSlot.setDescription('The slot number within the chassis where the backup media module that could drive this module resides. This attribute is set to 0 for rows in which the module is either not an IO card or is an IO card that has no appropriate media card present in the chassis.')
acModuleTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0))
acModuleCfgMismatchTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 1)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleSlot"), ("APPIAN-MODULE-MIB", "acModuleCfgType"), ("APPIAN-MODULE-MIB", "acModuleType"))
if mibBuilder.loadTexts: acModuleCfgMismatchTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleCfgMismatchTrap.setDescription('The configured module type does not match with the actual module present.')
acModuleResetFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 2)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleReset"), ("APPIAN-MODULE-MIB", "acModuleSlot"))
if mibBuilder.loadTexts: acModuleResetFailedTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleResetFailedTrap.setDescription("The module couldn't be reset.")
acModuleSwVersionTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 3)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleSlot"), ("APPIAN-MODULE-MIB", "acModuleSwVersion"))
if mibBuilder.loadTexts: acModuleSwVersionTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleSwVersionTrap.setDescription('Two different version of software are currently running within the same chassis. This is an unsupported operational mode.')
acModuleRemovalTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 4)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleSlot"))
if mibBuilder.loadTexts: acModuleRemovalTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleRemovalTrap.setDescription('A module has been removed from this chassis.')
acModuleInsertedTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 5)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleSlot"), ("APPIAN-MODULE-MIB", "acModuleType"))
if mibBuilder.loadTexts: acModuleInsertedTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleInsertedTrap.setDescription('A module has been inserted into this chassis.')
acModuleFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 2, 0, 6)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-MODULE-MIB", "acModuleNodeId"), ("APPIAN-MODULE-MIB", "acModuleSlot"), ("APPIAN-MODULE-MIB", "acModuleType"), ("APPIAN-MODULE-MIB", "acModuleDiagStatus"), ("APPIAN-MODULE-MIB", "acModuleDiagResultString"))
if mibBuilder.loadTexts: acModuleFailureTrap.setStatus('current')
if mibBuilder.loadTexts: acModuleFailureTrap.setDescription('The module in this slot did not pass diagnostics or has been marked as a failed board by operational software.')
mibBuilder.exportSymbols("APPIAN-MODULE-MIB", acModuleTable=acModuleTable, acModuleNumber=acModuleNumber, acModuleDiagStatus=acModuleDiagStatus, acModuleSwVersionTrap=acModuleSwVersionTrap, acModuleName=acModuleName, acModuleFirmwareName=acModuleFirmwareName, acModuleFailureTrap=acModuleFailureTrap, acModuleProductionDate=acModuleProductionDate, acModuleNodeId=acModuleNodeId, acModuleSwVersion=acModuleSwVersion, acModuleDiagResultString=acModuleDiagResultString, acModuleAdminStatus=acModuleAdminStatus, acModuleNumberFailures=acModuleNumberFailures, acModuleBackupSlot=acModuleBackupSlot, PYSNMP_MODULE_ID=acModule, AcModuleNumber=AcModuleNumber, acModuleCfgType=acModuleCfgType, acModuleNumberPorts=acModuleNumberPorts, acModuleSlot=acModuleSlot, acModule=acModule, acModuleEntry=acModuleEntry, acModuleTraps=acModuleTraps, acModuleSerialNumber=acModuleSerialNumber, acModuleActiveSlot=acModuleActiveSlot, acModulePrimarySlot=acModulePrimarySlot, acModuleOpStatus=acModuleOpStatus, acModuleFirmwareRevision=acModuleFirmwareRevision, acModuleDiagTestMode=acModuleDiagTestMode, acModuleType=acModuleType, acModuleRemovalTrap=acModuleRemovalTrap, acModuleCfgMismatchTrap=acModuleCfgMismatchTrap, acModuleRevision=acModuleRevision, acModuleReset=acModuleReset, acModuleResetFailedTrap=acModuleResetFailedTrap, acModuleInsertedTrap=acModuleInsertedTrap, AcModuleType=AcModuleType, AcMediaSlotNumber=AcMediaSlotNumber)