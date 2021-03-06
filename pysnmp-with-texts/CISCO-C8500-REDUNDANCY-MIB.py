#
# PySNMP MIB module CISCO-C8500-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-C8500-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Gauge32, MibIdentifier, Bits, Unsigned32, Integer32, Counter32, IpAddress, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "Integer32", "Counter32", "IpAddress", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TruthValue, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "TimeStamp")
ciscoC8500RedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 105))
ciscoC8500RedundancyMIB.setRevisions(('2003-05-04 00:00', '1998-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setRevisionsDescriptions(('Added the following scalar objects to ccrCpu group: ccrCpuStandbyEnableMode, ccrCpuSwitchoverTime, ccrForceCounterSync, ccrIfCounterSyncFreq, ccrVcCounterSyncFreq, ccrSigCounterSyncEnable.', 'Initial version of the MIB Module.',))
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setLastUpdated('200305040000Z')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setDescription('This MIB allows management of redundancy of CPU and switch cards for the Catalyst 8540 switch, and other products with similar implementations. The Catalyst 8540 is an ATM switch. It has 13 (or, in some models, 14) slots, of which 2 slots can hold CPU cards, and 3 (or, in some models, 4) slots can hold switch cards. A switch card is one that contains the ATM switching fabric. Two switch cards are combined to operate in 20Gbps switching mode. For CPU cards, 1+1 redundancy is supported. For switch cards, 2+1 redundancy is supported.')
class RedundancyStatus(TextualConvention, Integer32):
    description = 'The operational status of a card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("ok", 2), ("fault", 3))

class RedundancyMode(TextualConvention, Integer32):
    description = 'The redundancy mode of a card. The redundancy mode of a card is part of the state of the redundancy machine (i.e., the hardware or software that implements redundancy). The redundancy modes of all the cards in a redundancy group together represent the state of the redundancy machine for that redundancy group. The inputs to the redundancy machine that cause the redundancy mode of a card to transition from one value to another are events like card failure, card removal, user configuration, etc. Objects defined using this TC have a MAX-ACCESS of read-write or read-create. This allows a user to force the redundancy machine to transition to a desired state. The following values may be written: active(1) - Make this card an active member of the redundancy group. standby(2) - Make this card a standby member of the redundancy group. unused(3) - Do not use this card. Writing the above values may cause a switchover. When read, the values mean: active(1) - This card is an active member of the redundancy group. standby(2) - This card is a standby member of the redundancy group. unused(3) - This card is not being used at present. notPresent(4) - There is no card in the slot. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("standby", 2), ("unused", 3), ("notPresent", 4))

class RedundancySlotIndex(TextualConvention, Unsigned32):
    description = 'A value that identifies a physical slot in the chassis. For a chassis with slots that are numbered left to right, the leftmost slot has value 1. For a chassis with slots that are numbered top to bottom, the topmost slot has value 1.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

ciscoC8500RedundancyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1))
ccrCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1))
ccrSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2))
ccrCpuTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1), )
if mibBuilder.loadTexts: ccrCpuTable.setStatus('current')
if mibBuilder.loadTexts: ccrCpuTable.setDescription('There is an entry in this table for each slot that can hold a CPU card.')
ccrCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSlotIndex"))
if mibBuilder.loadTexts: ccrCpuEntry.setStatus('current')
if mibBuilder.loadTexts: ccrCpuEntry.setDescription('Redundancy information for a CPU card.')
ccrCpuSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 1), RedundancySlotIndex())
if mibBuilder.loadTexts: ccrCpuSlotIndex.setStatus('current')
if mibBuilder.loadTexts: ccrCpuSlotIndex.setDescription('Identifies a chassis slot.')
ccrCpuMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 2), RedundancyMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrCpuMode.setStatus('current')
if mibBuilder.loadTexts: ccrCpuMode.setDescription('The redundancy mode of this CPU card.')
ccrCpuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 3), RedundancyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrCpuStatus.setStatus('current')
if mibBuilder.loadTexts: ccrCpuStatus.setDescription('The operational status of this CPU card.')
ccrSyncConfigOnSet = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 2), Bits().clone(namedValues=NamedValues(("runningConfig", 0), ("startupConfig", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSyncConfigOnSet.setStatus('current')
if mibBuilder.loadTexts: ccrSyncConfigOnSet.setDescription("The device's running-configuration and startup-configuration both reside on the active CPU card. This object indicates whether these configurations should be copied from the active CPU to the standby CPU whenever they change. It is acceptable to copy either, both, or neither.")
ccrCpuStandbyEnableMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrCpuStandbyEnableMode.setStatus('current')
if mibBuilder.loadTexts: ccrCpuStandbyEnableMode.setDescription("This object is used to allow or disallow the execution of the enable exec command on the secondary CPU. When set to 'true', the enable exec command can be executed on secondary CPU, and the user may enter enable mode after keying in the password configured. When set to 'false', the enable exec command cannot be executed; thus, no user may enter enabled mode.")
ccrCpuSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrCpuSwitchoverTime.setStatus('current')
if mibBuilder.loadTexts: ccrCpuSwitchoverTime.setDescription('The time taken for the most recent CPU switchover.')
ccrForceCounterSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forcesync", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrForceCounterSync.setStatus('current')
if mibBuilder.loadTexts: ccrForceCounterSync.setDescription("This object is used to force the synchronization of counters from primary CPU to secondary CPU. It should generally be set just before a controlled Route Processor Switchover. When this object is retrieved, the value 'noop' is returned. When this object is set to 'noop' no operation is performed.")
ccrIfCounterSyncFreq = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrIfCounterSyncFreq.setStatus('current')
if mibBuilder.loadTexts: ccrIfCounterSyncFreq.setDescription('This object configures the periodicity of interface counter synchronization from primary CPU to secondary CPU. Setting this object to 0 will disable counter synchronization.')
ccrVcCounterSyncFreq = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrVcCounterSyncFreq.setStatus('current')
if mibBuilder.loadTexts: ccrVcCounterSyncFreq.setDescription('This object configures the periodicity of Virtual Circuit (VC) counter synchronization from primary CPU to secondary CPU. Setting this object to 0 will disable counter synchronization.')
ccrSigCounterSyncEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSigCounterSyncEnable.setStatus('current')
if mibBuilder.loadTexts: ccrSigCounterSyncEnable.setDescription("This object configures the synchronization of ATM Signalling Statistics from primary CPU to secondary CPU. When this object is set to 'true', sychronization is enabled. When this object is set to 'false', synchronization is disabled.")
ccrSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1), )
if mibBuilder.loadTexts: ccrSwitchTable.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchTable.setDescription("There is an entry in this table for each slot that can hold a switch card. A 'switch card' is a card that contains the ATM switch fabric.")
ccrSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchSlotIndex"))
if mibBuilder.loadTexts: ccrSwitchEntry.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchEntry.setDescription('Redundancy information for a switch card.')
ccrSwitchSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 1), RedundancySlotIndex())
if mibBuilder.loadTexts: ccrSwitchSlotIndex.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchSlotIndex.setDescription('Identifies a chassis slot.')
ccrSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 2), RedundancyMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSwitchMode.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchMode.setDescription('The redundancy mode of this switch card.')
ccrSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 3), RedundancyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchStatus.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchStatus.setDescription('The operational status of this switch card.')
ccrSwitchLastSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverTime.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverTime.setDescription('The value of sysUpTime at the last switchover of the switch cards. The value is zero if there was no switchover since agent initialization.')
ccrSwitchLastSwitchoverReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("notKnown", 2), ("userInitiated", 3), ("cardFailed", 4), ("cardRecovered", 5), ("cardRemoved", 6), ("cardInserted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverReason.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverReason.setDescription('The reason for the last switch card switchover. The value is none(1) if there was no switchover since agent initialization.')
ccrSwitchBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenGbps", 1), ("twentyGbps", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchBw.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchBw.setDescription('The switching capacity (i.e., bandwidth) of the switch fabric. tenGbps(1) - 10 Gigabits/sec twentyGbps(2) - 20 Gigabits/sec. ')
ccrDesiredSwitchBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenGbps", 1), ("twentyGbps", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrDesiredSwitchBw.setStatus('current')
if mibBuilder.loadTexts: ccrDesiredSwitchBw.setDescription('The desired switching capacity (i.e., bandwidth) of the switch fabric. tenGbps(1) - 10 Gigabits/sec twentyGbps(2) - 20 Gigabits/sec If the value configured by writing to this object is supported by the device, it will be applied at the next reboot. The speed at which the switch fabric is currently operating is reflected by the value of ccrSwitchBw.')
ciscoC8500RedundancyMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 2))
ccrMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0))
ccrCpuStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"))
if mibBuilder.loadTexts: ccrCpuStatusChange.setStatus('current')
if mibBuilder.loadTexts: ccrCpuStatusChange.setDescription('This notification is generated when the value of ccrCpuStatus changes for a CPU card. The varbind indicates the current status of the affected card.')
ccrSwitchStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus"))
if mibBuilder.loadTexts: ccrSwitchStatusChange.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchStatusChange.setDescription('This notification is generated when the value of ccrSwitchStatus changes for a switch card. The varbind indicates the current status of the affected card.')
ccrSwitchModeChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 3)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode"))
if mibBuilder.loadTexts: ccrSwitchModeChange.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchModeChange.setDescription('This notification is generated when the value of ccrSwitchMode changes from active(1) to either standby(2) or unused(3) or notPresent(4). The varbind indicates the current mode of the affected card.')
ciscoC8500RedundancyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3))
ciscoC8500RedundancyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1))
ciscoC8500RedundancyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2))
ciscoC8500RedundancyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMibGroup"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoC8500RedundancyMIBCompliance = ciscoC8500RedundancyMIBCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIBCompliance.setDescription('The compliance statement for Cisco agents which implement the CISCO-C8500-REDUNDANCY-MIB.')
ciscoC8500RedundancyMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMibGroup1"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMibGroup"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoC8500RedundancyMIBComplianceRev1 = ciscoC8500RedundancyMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIBComplianceRev1.setDescription('The compliance statement to include objects related to the redundancy features like enable password on secondary, switchover duration and counter.')
ccrCpuMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrCpuMibGroup = ccrCpuMibGroup.setStatus('obsolete')
if mibBuilder.loadTexts: ccrCpuMibGroup.setDescription('A collection of objects providing the ability to manage CPU card redundancy.')
ccrSwitchMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverTime"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverReason"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchBw"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrDesiredSwitchBw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrSwitchMibGroup = ccrSwitchMibGroup.setStatus('current')
if mibBuilder.loadTexts: ccrSwitchMibGroup.setDescription('A collection of objects providing the ability to manage Switch Fabric card redundancy.')
ccrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 3)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatusChange"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatusChange"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchModeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrNotificationsGroup = ccrNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ccrNotificationsGroup.setDescription('A collection of notifications related to redundancy.')
ccrCpuMibGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 4)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStandbyEnableMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSwitchoverTime"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrForceCounterSync"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrIfCounterSyncFreq"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrVcCounterSyncFreq"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSigCounterSyncEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrCpuMibGroup1 = ccrCpuMibGroup1.setStatus('current')
if mibBuilder.loadTexts: ccrCpuMibGroup1.setDescription('A collection of objects providing the ability to manage CPU card redundancy and redundancy feature for counter, enable password on secondary and switchover duration.')
mibBuilder.exportSymbols("CISCO-C8500-REDUNDANCY-MIB", ccrCpu=ccrCpu, ccrCpuStatusChange=ccrCpuStatusChange, ccrSigCounterSyncEnable=ccrSigCounterSyncEnable, ccrCpuSlotIndex=ccrCpuSlotIndex, ccrSwitchMibGroup=ccrSwitchMibGroup, ciscoC8500RedundancyMIBComplianceRev1=ciscoC8500RedundancyMIBComplianceRev1, ccrNotificationsGroup=ccrNotificationsGroup, ccrSwitchStatusChange=ccrSwitchStatusChange, ciscoC8500RedundancyMIB=ciscoC8500RedundancyMIB, ccrSwitchSlotIndex=ccrSwitchSlotIndex, ccrCpuSwitchoverTime=ccrCpuSwitchoverTime, ccrSwitchEntry=ccrSwitchEntry, RedundancySlotIndex=RedundancySlotIndex, ccrSwitch=ccrSwitch, ccrSwitchStatus=ccrSwitchStatus, ccrCpuTable=ccrCpuTable, ccrSwitchMode=ccrSwitchMode, ccrSwitchLastSwitchoverReason=ccrSwitchLastSwitchoverReason, ccrSyncConfigOnSet=ccrSyncConfigOnSet, ciscoC8500RedundancyMIBObjects=ciscoC8500RedundancyMIBObjects, ciscoC8500RedundancyMIBNotificationPrefix=ciscoC8500RedundancyMIBNotificationPrefix, ciscoC8500RedundancyMIBCompliances=ciscoC8500RedundancyMIBCompliances, PYSNMP_MODULE_ID=ciscoC8500RedundancyMIB, ccrIfCounterSyncFreq=ccrIfCounterSyncFreq, ccrSwitchLastSwitchoverTime=ccrSwitchLastSwitchoverTime, ccrCpuMibGroup=ccrCpuMibGroup, ccrCpuMode=ccrCpuMode, ciscoC8500RedundancyMIBCompliance=ciscoC8500RedundancyMIBCompliance, ccrCpuStatus=ccrCpuStatus, ciscoC8500RedundancyMIBGroups=ciscoC8500RedundancyMIBGroups, ccrCpuMibGroup1=ccrCpuMibGroup1, ccrDesiredSwitchBw=ccrDesiredSwitchBw, ccrSwitchTable=ccrSwitchTable, RedundancyMode=RedundancyMode, ccrSwitchModeChange=ccrSwitchModeChange, RedundancyStatus=RedundancyStatus, ccrCpuEntry=ccrCpuEntry, ccrSwitchBw=ccrSwitchBw, ccrMIBNotifications=ccrMIBNotifications, ciscoC8500RedundancyMIBConformance=ciscoC8500RedundancyMIBConformance, ccrForceCounterSync=ccrForceCounterSync, ccrCpuStandbyEnableMode=ccrCpuStandbyEnableMode, ccrVcCounterSyncFreq=ccrVcCounterSyncFreq)
