#
# PySNMP MIB module HPN-ICF-ISSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-ISSU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, iso, Counter64, NotificationType, ModuleIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "Unsigned32")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
hpnicfIssuUpgrade = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133))
hpnicfIssuUpgrade.setRevisions(('2013-01-15 15:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfIssuUpgrade.setRevisionsDescriptions(('Initial version of this MIB module. Added hpnicfIssuUpgradeImageTable hpnicfIssuOp hpnicfIssuCompatibleResult hpnicfIssuTestResultTable hpnicfIssuUpgradeResultTable',))
if mibBuilder.loadTexts: hpnicfIssuUpgrade.setLastUpdated('201301151536Z')
if mibBuilder.loadTexts: hpnicfIssuUpgrade.setOrganization('')
if mibBuilder.loadTexts: hpnicfIssuUpgrade.setContactInfo('')
if mibBuilder.loadTexts: hpnicfIssuUpgrade.setDescription("This MIB provides objects for upgrading images on modules in the system, objects for showing the result of an upgrade operation, and objects for showing the result of a test operation. To perform an upgrade operation, a management application must first read the hpnicfIssuUpgradeImageTable table and use the information in other tables, as explained below. You can configure a new image name for each image type as listed in hpnicfIssuUpgradeImageTable. The system will use this image on the particular module at the next reboot. The management application used to perform an upgrade operation must first check if an upgrade operation is already in progress in the system. This is done by reading the hpnicfIssuOpType ('none' indicates that no other upgrade operation is in progress. Any other value indicates that an upgrade is already in progress and a new upgrade operation is not allowed. To start an 'install' operation, the user must first perform a 'test' operation to examine the version compatibility between the given set of images and the running images. Only if the result of the 'test' operation is 'success' can the user proceed to do an install operation. The table hpnicfIssuTestResultTable provides the result of the 'test' operation performed by using hpnicfIssuOpType. The table hpnicfIssuUpgradeResultTable provides the result of the 'install' operation performed by using hpnicfIssuOpType. ")
hpnicfIssuUpgradeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1))
hpnicfIssuUpgradeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1))
hpnicfIssuUpgradeImageTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageTable.setDescription('A table listing the image variable types that exist in the device.')
hpnicfIssuUpgradeImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-ISSU-MIB", "hpnicfIssuUpgradeImageIndex"))
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageEntry.setDescription('An hpnicfIssuUpgradeImageEntry entry. Each entry provides an image variable type that exists in the device.')
hpnicfIssuUpgradeImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageIndex.setDescription('Index of each image.')
hpnicfIssuUpgradeImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot", 1), ("system", 2), ("feature", 3), ("ipe", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageType.setDescription("Types of images that the system can run. The value of this object has four image variables names - 'boot', 'system', 'feature' and 'ipe'. This table will then list these four strings as follows: hpnicfIssuUpgradeImageType boot system feature IPE The user can assign images (using hpnicfIssuUpgradeImageURL) to these variables and the system will use the assigned images to boot.")
hpnicfIssuUpgradeImageURL = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageURL.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageURL.setDescription('This object contains the path of the image of this entity.')
hpnicfIssuUpgradeImageRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeImageRowStatus.setDescription('Row-status of image table.')
hpnicfIssuOp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2))
hpnicfIssuOpType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("test", 3), ("install", 4), ("rollback", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIssuOpType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuOpType.setDescription("Command to be executed. The 'test' command must be performed before the 'install' command can be executed. The 'install' command is allowed only if a read of this object returns 'test' and the value of object hpnicfIssuOpStatus is 'success'. Command Remarks none If the user sets this object to 'none', the agent will return a success without performing an upgrade operation. done If this object returns any value other than 'none', setting this to 'done' will do the required cleanup of the previous upgrade operation and get the system ready for a new upgrade operation. test Check the version compatibility and upgrade method for the given set of image files. install For all the image entities listed in the hpnicfIssuUpgradeImageTable, perform the required upgrade operation listed in that table. rollback Abort the current 'install' operation and roll back to the previous version. ")
hpnicfIssuImageFileOverwrite = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIssuImageFileOverwrite.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuImageFileOverwrite.setDescription('If you want to overwrite the existing file, set the value of this object to enable. Otherwise, set the value of this object to disable.')
hpnicfIssuOpTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIssuOpTrapEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuOpTrapEnable.setDescription('If you want to enable the trap, set the value of this object to enable. Otherwise, set the value of this object to disable.')
hpnicfIssuOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("failure", 2), ("inProgress", 3), ("success", 4), ("rollbackInProgress", 5), ("rollbackSuccess", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuOpStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuOpStatus.setDescription('Status of the specified operation. none - No operation was performed. failure - Specified operation has failed. inProgress - Specified operation is in progress. success - Specified operation completed successfully. rollbackInProgress - Rollback operation is in progress. rollbackSuccess - Rollback operation completed successfully. ')
hpnicfIssuFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuFailedReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuFailedReason.setDescription("Indicates the the cause of 'failure' state of the object 'hpnicfIssuOpStatus'. This object would be a null string if the value of 'hpnicfIssuOpStatus' is not 'failure'.")
hpnicfIssuOpTimeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuOpTimeCompleted.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuOpTimeCompleted.setDescription("Indicates the time when the upgrade operation was completed. This object would be a null string if hpnicfIssuOpType is 'none'. ")
hpnicfIssuLastOpType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("test", 3), ("install", 4), ("rollback", 5))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuLastOpType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuLastOpType.setDescription("This object indicates the previous hpnicfIssuOp value. It will be updated after a new hpnicfIssuOp is set and delivered to the upgrade process. Command Remarks none If the user sets this object to 'none', agent will return a success without performing an upgrade operation. done If this object returns any value other than 'none', setting this to 'done' will do the required cleanup of the previous upgrade operation and get the system ready for a new upgrade operation. test Check the version compatibility and upgrade method for the given set of image files. install For all the image entities listed in the hpnicfIssuUpgradeImageTable, perform the required upgrade operation listed in that table. rollback Abort the current install operation and roll back to the previous version. ")
hpnicfIssuLastOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("failure", 2), ("inProgress", 3), ("success", 4), ("rollbackInProgress", 5), ("rollbackSuccess", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuLastOpStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuLastOpStatus.setDescription('This object indicates previous hpnicfIssuOpStatus value. It will be updated after new hpnicfIssuOp is set and delivered to upgrade process. none - No operation was performed. failure - Specified operation has failed. inProgress - Specified operation is active. success - Specified operation completed successfully. rollbackInProgress - Rollback operation is in progress. rollbackSuccess - Rollback operation completed successfully. ')
hpnicfIssuLastOpFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuLastOpFailedReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuLastOpFailedReason.setDescription("Indicates the cause of 'failure' state of the object 'hpnicfIssuOpStatus'. This object would be a null string if the value of 'hpnicfIssuOpStatus' is not 'failure'. The value will be updated when new hpnicfIssuOp is set and delivered to the upgrade process.")
hpnicfIssuLastOpTimeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuLastOpTimeCompleted.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuLastOpTimeCompleted.setDescription('Indicates the previous hpnicfIssuOpTimeCompleted value. The value will be updated when new hpnicfIssuOp is set and delivered to the upgrade process.')
hpnicfIssuUpgradeResultGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2))
hpnicfIssuCompatibleResult = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1))
hpnicfIssuCompatibleResultStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inCompatible", 2), ("compatible", 3), ("failure", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuCompatibleResultStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuCompatibleResultStatus.setDescription('Specifies whether the images provided in hpnicfIssuUpgradeImageTable are compatible with each other as far as this module is concerned. none - No operation was performed. inCompatible - The images provided are compatible and can be run on this module. compatible - The images provided are incompatible and can be run on this module. failure - Failed to get the compatibility. ')
hpnicfIssuCompatibleResultFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuCompatibleResultFailedReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuCompatibleResultFailedReason.setDescription("Indicates the cause of 'failure' state of the object 'hpnicfIssuCompatibleResultStatus'. This object would be a null string if the value of 'hpnicfIssuCompatibleResultStatus' is not 'failure'.")
hpnicfIssuTestResultTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2), )
if mibBuilder.loadTexts: hpnicfIssuTestResultTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestResultTable.setDescription('Shows the result of the test operation, from which you can see the upgrade method.')
hpnicfIssuTestResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-ISSU-MIB", "hpnicfIssuTestResultIndex"))
if mibBuilder.loadTexts: hpnicfIssuTestResultEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestResultEntry.setDescription('An hpnicfIssuTestResultEntry entry. Each entry provides the test result of a card in the device.')
hpnicfIssuTestResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfIssuTestResultIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestResultIndex.setDescription('Internal index, not accessible.')
hpnicfIssuTestDeviceChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuTestDeviceChassisID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestDeviceChassisID.setDescription('Chassis ID of the card.')
hpnicfIssuTestDeviceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuTestDeviceSlotID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestDeviceSlotID.setDescription('Slot ID of the card.')
hpnicfIssuTestDeviceCpuID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuTestDeviceCpuID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestDeviceCpuID.setDescription('CPU ID of the card.')
hpnicfIssuTestDeviceUpgradeWay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("reboot", 2), ("sequenceReboot", 3), ("issuReboot", 4), ("serviceUpgrade", 5), ("fileUpgrade", 6), ("incompatibleUpgrade", 7))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuTestDeviceUpgradeWay.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuTestDeviceUpgradeWay.setDescription('Upgrade method of the device. none - No operation was performed. reboot - The upgrade method of this device is Reboot. sequenceReboot - The upgrade method of this device is SequenceReboot. issuReboot - The upgrade method of this device is IssuReboot. serviceUpgrade - The upgrade method of this device is ServiceReboot. fileUpgrade - The upgrade method of this device is FileReboot. incompatibleUpgrade - The upgrade method of this device is IncompatibleUpgrade. ')
hpnicfIssuUpgradeResultTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3), )
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultTable.setDescription('Shows the result of the install operation.')
hpnicfIssuUpgradeResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-ISSU-MIB", "hpnicfIssuUpgradeResultIndex"))
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultEntry.setDescription('An hpnicfIssuUpgradeResultEntry entry. Each entry provides the upgrade result of a card in the device.')
hpnicfIssuUpgradeResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeResultIndex.setDescription('Internal Index, not accessible.')
hpnicfIssuUpgradeDeviceChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceChassisID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceChassisID.setDescription('Chassis ID of the card.')
hpnicfIssuUpgradeDeviceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceSlotID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceSlotID.setDescription('Slot ID of the card.')
hpnicfIssuUpgradeDeviceCpuID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceCpuID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceCpuID.setDescription('CPU ID of the card.')
hpnicfIssuUpgradeState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("init", 1), ("loading", 2), ("loaded", 3), ("switching", 4), ("switchover", 5), ("committing", 6), ("committed", 7), ("rollbacking", 8), ("rollbacked", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeState.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeState.setDescription('Upgrade status of the device. init -The current status of the device is Init. loading -The current status of the device is Loading. loaded -The current status of the device is Loaded. switching -The current status of the device is Switching. switchover -The current status of the device is Switchover. committing -The current status of the device is Committing. committed -The current status of the device is Committed. rollbacking -The current status of the device is Rollbacking. rollbacked -The current status of the device is Rollbacked. ')
hpnicfIssuDeviceUpgradeWay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("reboot", 2), ("sequenceReboot", 3), ("issuReboot", 4), ("serviceUpgrade", 5), ("fileUpgrade", 6), ("incompatibleUpgrade", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuDeviceUpgradeWay.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuDeviceUpgradeWay.setDescription('Upgrade method of the card. none - No operation was performed. reboot - The upgrade method of this device is Reboot. sequenceReboot - The upgrade method of this device is SequenceReboot. issuReboot - The upgrade method of this device is IssuReboot. serviceUpgrade - The upgrade method of this device is ServiceReboot. fileUpgrade - The upgrade method of this device is FileReboot. incompatibleUpgrade - The upgrade method of this device is IncompatibleUpgrade. ')
hpnicfIssuUpgradeDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("waitingUpgrade", 1), ("inProcess", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeDeviceStatus.setDescription('Upgrade status of the device.')
hpnicfIssuUpgradeFailedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIssuUpgradeFailedReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeFailedReason.setDescription("Indicates the cause of 'failure' state of the object 'hpnicfIssuUpgradeDeviceStatus'. This object would be a null string if the value of 'hpnicfIssuCompatibleResultStatus' is not 'failure'.")
hpnicfIssuUpgradeNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2))
hpnicfIssuUpgradeTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2, 0))
hpnicfIssuUpgradeOpCompletionNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2, 0, 1)).setObjects(("HPN-ICF-ISSU-MIB", "hpnicfIssuOpType"), ("HPN-ICF-ISSU-MIB", "hpnicfIssuOpStatus"), ("HPN-ICF-ISSU-MIB", "hpnicfIssuFailedReason"), ("HPN-ICF-ISSU-MIB", "hpnicfIssuOpTimeCompleted"))
if mibBuilder.loadTexts: hpnicfIssuUpgradeOpCompletionNotify.setStatus('current')
if mibBuilder.loadTexts: hpnicfIssuUpgradeOpCompletionNotify.setDescription('An hpnicfIssuUpgradeOpCompletionNotify is sent at the completion of upgrade operation denoted by hpnicfIssuOp object, if such a notification was requested when the operation was initiated. hpnicfIssuOpType indicates the type of the operation. hpnicfIssuOpStatus indicates the result of the operation. hpnicfIssuFailedReason indicates the operation failure reason. hpnicfIssuOpTimeCompleted indicates the time when the operation was completed.')
mibBuilder.exportSymbols("HPN-ICF-ISSU-MIB", hpnicfIssuUpgradeImageRowStatus=hpnicfIssuUpgradeImageRowStatus, hpnicfIssuImageFileOverwrite=hpnicfIssuImageFileOverwrite, hpnicfIssuOpTrapEnable=hpnicfIssuOpTrapEnable, hpnicfIssuUpgradeFailedReason=hpnicfIssuUpgradeFailedReason, hpnicfIssuUpgradeImageType=hpnicfIssuUpgradeImageType, hpnicfIssuUpgradeImageTable=hpnicfIssuUpgradeImageTable, hpnicfIssuOpStatus=hpnicfIssuOpStatus, hpnicfIssuTestResultTable=hpnicfIssuTestResultTable, hpnicfIssuUpgradeDeviceStatus=hpnicfIssuUpgradeDeviceStatus, hpnicfIssuCompatibleResultFailedReason=hpnicfIssuCompatibleResultFailedReason, hpnicfIssuUpgradeImageEntry=hpnicfIssuUpgradeImageEntry, hpnicfIssuCompatibleResult=hpnicfIssuCompatibleResult, hpnicfIssuUpgradeImageURL=hpnicfIssuUpgradeImageURL, hpnicfIssuOpType=hpnicfIssuOpType, hpnicfIssuUpgradeMibObjects=hpnicfIssuUpgradeMibObjects, hpnicfIssuOp=hpnicfIssuOp, hpnicfIssuUpgradeDeviceChassisID=hpnicfIssuUpgradeDeviceChassisID, hpnicfIssuUpgradeResultEntry=hpnicfIssuUpgradeResultEntry, hpnicfIssuUpgradeNotify=hpnicfIssuUpgradeNotify, hpnicfIssuLastOpType=hpnicfIssuLastOpType, hpnicfIssuTestDeviceUpgradeWay=hpnicfIssuTestDeviceUpgradeWay, hpnicfIssuUpgradeImageIndex=hpnicfIssuUpgradeImageIndex, hpnicfIssuUpgradeOpCompletionNotify=hpnicfIssuUpgradeOpCompletionNotify, hpnicfIssuUpgradeResultGroup=hpnicfIssuUpgradeResultGroup, hpnicfIssuUpgradeDeviceSlotID=hpnicfIssuUpgradeDeviceSlotID, hpnicfIssuOpTimeCompleted=hpnicfIssuOpTimeCompleted, hpnicfIssuLastOpTimeCompleted=hpnicfIssuLastOpTimeCompleted, hpnicfIssuUpgradeTrapPrefix=hpnicfIssuUpgradeTrapPrefix, hpnicfIssuTestDeviceChassisID=hpnicfIssuTestDeviceChassisID, hpnicfIssuDeviceUpgradeWay=hpnicfIssuDeviceUpgradeWay, hpnicfIssuUpgrade=hpnicfIssuUpgrade, PYSNMP_MODULE_ID=hpnicfIssuUpgrade, hpnicfIssuTestResultIndex=hpnicfIssuTestResultIndex, hpnicfIssuUpgradeDeviceCpuID=hpnicfIssuUpgradeDeviceCpuID, hpnicfIssuUpgradeState=hpnicfIssuUpgradeState, hpnicfIssuLastOpFailedReason=hpnicfIssuLastOpFailedReason, hpnicfIssuLastOpStatus=hpnicfIssuLastOpStatus, hpnicfIssuTestDeviceSlotID=hpnicfIssuTestDeviceSlotID, hpnicfIssuTestDeviceCpuID=hpnicfIssuTestDeviceCpuID, hpnicfIssuCompatibleResultStatus=hpnicfIssuCompatibleResultStatus, hpnicfIssuUpgradeGroup=hpnicfIssuUpgradeGroup, hpnicfIssuFailedReason=hpnicfIssuFailedReason, hpnicfIssuUpgradeResultTable=hpnicfIssuUpgradeResultTable, hpnicfIssuUpgradeResultIndex=hpnicfIssuUpgradeResultIndex, hpnicfIssuTestResultEntry=hpnicfIssuTestResultEntry)