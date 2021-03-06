#
# PySNMP MIB module HUAWEI-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LLDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
lldpLocSysCapEnabled, lldpPortConfigPortNum, lldpLocSysCapSupported = mibBuilder.importSymbols("LLDP-MIB", "lldpLocSysCapEnabled", "lldpPortConfigPortNum", "lldpLocSysCapSupported")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Gauge32, Integer32, MibIdentifier, TimeTicks, Counter32, IpAddress, iso, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier", "TimeTicks", "Counter32", "IpAddress", "iso", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hwLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134))
if mibBuilder.loadTexts: hwLldpMIB.setLastUpdated('200611240000Z')
if mibBuilder.loadTexts: hwLldpMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwLldpMIB.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwLldpMIB.setDescription('This file is an extension of LLDP-MIB. It provides such functions of globally enabling or disabling the LLDP protocol, enabling the global alarm, clearing statistics on ports and configuring network management IP addresses and some alarms.')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hwLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1))
hwLldpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2))
hwLldpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3))
hwLldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1))
hwLldpRemoteSystemData = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2))
hwLldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 1), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpEnable.setStatus('current')
if mibBuilder.loadTexts: hwLldpEnable.setDescription('Globally enable or disable the LLDP configuration. If the hwLldpEnable is 1, LLDP is enabled. If the hwLldpEnable is 2, LLDP is disabled. By default, LLDP is disabled.')
hwLldpLocManIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpLocManIPAddr.setStatus('current')
if mibBuilder.loadTexts: hwLldpLocManIPAddr.setDescription('Specifies the management IP address of the local device. The management IP address is carried in the management address TLV of LLDP packet and is used to identify NM devices in network management. The management IP address configured here must be a valid one and must be an IP address in the address chain. If the IP address is not valid or is not configured, the management IP address will be chosen from default IP addressees of the system. The sequence of address searching is: loopback interface, management network interface, VLANIF port and IP address chain (The smallest IP is chosen). If the default IP is not found, the bridge MAC of the system is used.')
hwLldpCounterReset = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpCounterReset.setStatus('current')
if mibBuilder.loadTexts: hwLldpCounterReset.setDescription('Clears the statistics of packets received and sent on all ports.')
hwLldpNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 4), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: hwLldpNotificationEnable.setDescription('The global alarming that is used to control alarms on all ports. If it is 1, the global alarming is enabled. If it is 2, the global alarming is disabled. By default, the global alarming is disabled.')
hwLldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5), )
if mibBuilder.loadTexts: hwLldpPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwLldpPortConfigTable.setDescription('LLDP port congfiguration table.')
hwLldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: hwLldpPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwLldpPortConfigEntry.setDescription('Entries of the LLDP port congfiguration table.')
hwLldpPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 11), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLldpPortConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwLldpPortConfigIfIndex.setDescription('Port index.')
hwLldpPortConfigCounterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 12), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpPortConfigCounterReset.setStatus('current')
if mibBuilder.loadTexts: hwLldpPortConfigCounterReset.setDescription('Clears the statistics of packets received and sent on the current port.')
hwLldpRemProtoTypeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1), )
if mibBuilder.loadTexts: hwLldpRemProtoTypeTable.setStatus('current')
if mibBuilder.loadTexts: hwLldpRemProtoTypeTable.setDescription('LLDP remote neighbour protocol version table.')
hwLldpRemProtoTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: hwLldpRemProtoTypeEntry.setStatus('current')
if mibBuilder.loadTexts: hwLldpRemProtoTypeEntry.setDescription('Entries of the LLDP remote neighbour protocol version table.')
hwLldpRemProtoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("lldp", 1), ("cdp", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLldpRemProtoType.setStatus('current')
if mibBuilder.loadTexts: hwLldpRemProtoType.setDescription('Protocol type of the remote neighbour.')
hwLldpEnabled = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 1))
if mibBuilder.loadTexts: hwLldpEnabled.setStatus('current')
if mibBuilder.loadTexts: hwLldpEnabled.setDescription('Notify the NMS that the LLDP is globally enabled. This alarm is not restricted by the alarm delay.')
hwLldpDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 2))
if mibBuilder.loadTexts: hwLldpDisabled.setStatus('current')
if mibBuilder.loadTexts: hwLldpDisabled.setDescription('Notify the NMS that the LLDP is globally disabled. This alarm is not restricted by the alarm delay.')
hwLldpLocSysCapSupportedChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 3)).setObjects(("LLDP-MIB", "lldpLocSysCapSupported"))
if mibBuilder.loadTexts: hwLldpLocSysCapSupportedChange.setStatus('current')
if mibBuilder.loadTexts: hwLldpLocSysCapSupportedChange.setDescription('Alarm on the change of capabilities supported of a local device.')
hwLldpLocSysCapEnabledChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 4)).setObjects(("LLDP-MIB", "lldpLocSysCapEnabled"))
if mibBuilder.loadTexts: hwLldpLocSysCapEnabledChange.setStatus('current')
if mibBuilder.loadTexts: hwLldpLocSysCapEnabledChange.setDescription('Alarm on the change of capabilities enabled of a local device.')
hwLldpLocManIPAddrChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 5)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr"))
if mibBuilder.loadTexts: hwLldpLocManIPAddrChange.setStatus('current')
if mibBuilder.loadTexts: hwLldpLocManIPAddrChange.setDescription('Alarm on the change of management IP address of a local device.')
hwLldpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1))
hwLldpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2))
lldpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1, 1)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpConfigGroup"), ("HUAWEI-LLDP-MIB", "hwLldpStatsGroup"), ("HUAWEI-LLDP-MIB", "hwLldpPortGroup"), ("HUAWEI-LLDP-MIB", "hwLldpTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpCompliance = lldpCompliance.setStatus('current')
if mibBuilder.loadTexts: lldpCompliance.setDescription('The compliance statement for SNMP entities which implement the HUAWEI-LLDP-MIB.')
hwLldpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 1)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpEnable"), ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr"), ("HUAWEI-LLDP-MIB", "hwLldpNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpConfigGroup = hwLldpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hwLldpConfigGroup.setDescription('The collection of objects which are used to configure the LLDP implementation behavior. This group is mandatory for agents which implement the LLDP.')
hwLldpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 2)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpCounterReset"), ("HUAWEI-LLDP-MIB", "hwLldpPortConfigCounterReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpStatsGroup = hwLldpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hwLldpStatsGroup.setDescription('The collection of objects which are used to represent LLDP statistics. This group is mandatory for agents which implement the LLDP and have the capability of receiving and transmitting LLDP frames.')
hwLldpPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 3)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpPortConfigIfIndex"), ("HUAWEI-LLDP-MIB", "hwLldpRemProtoType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpPortGroup = hwLldpPortGroup.setStatus('current')
if mibBuilder.loadTexts: hwLldpPortGroup.setDescription('The collection of objects indicate index of port.')
hwLldpTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 4)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpEnabled"), ("HUAWEI-LLDP-MIB", "hwLldpDisabled"), ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapSupportedChange"), ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapEnabledChange"), ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddrChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpTrapGroup = hwLldpTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwLldpTrapGroup.setDescription('The collection of notifications used to indicate HUAWEI-LLDP-MIB data consistency and general status information. This group is mandatory for agents which implement the LLDP and have the capability of receiving LLDP frames.')
mibBuilder.exportSymbols("HUAWEI-LLDP-MIB", hwLldpMIB=hwLldpMIB, hwLldpLocManIPAddrChange=hwLldpLocManIPAddrChange, hwLldpCounterReset=hwLldpCounterReset, hwLldpLocSysCapSupportedChange=hwLldpLocSysCapSupportedChange, EnabledStatus=EnabledStatus, hwLldpTrapGroup=hwLldpTrapGroup, hwLldpLocSysCapEnabledChange=hwLldpLocSysCapEnabledChange, hwLldpRemProtoTypeEntry=hwLldpRemProtoTypeEntry, hwLldpConfigGroup=hwLldpConfigGroup, hwLldpPortConfigIfIndex=hwLldpPortConfigIfIndex, hwLldpNotificationEnable=hwLldpNotificationEnable, hwLldpCompliances=hwLldpCompliances, hwLldpPortConfigTable=hwLldpPortConfigTable, hwLldpRemoteSystemData=hwLldpRemoteSystemData, hwLldpObjects=hwLldpObjects, hwLldpPortConfigEntry=hwLldpPortConfigEntry, hwLldpConformance=hwLldpConformance, hwLldpGroups=hwLldpGroups, hwLldpPortGroup=hwLldpPortGroup, hwLldpRemProtoType=hwLldpRemProtoType, PYSNMP_MODULE_ID=hwLldpMIB, hwLldpConfiguration=hwLldpConfiguration, hwLldpEnable=hwLldpEnable, hwLldpTraps=hwLldpTraps, hwLldpStatsGroup=hwLldpStatsGroup, hwLldpEnabled=hwLldpEnabled, hwLldpPortConfigCounterReset=hwLldpPortConfigCounterReset, hwLldpDisabled=hwLldpDisabled, hwLldpRemProtoTypeTable=hwLldpRemProtoTypeTable, hwLldpLocManIPAddr=hwLldpLocManIPAddr, lldpCompliance=lldpCompliance)
