#
# PySNMP MIB module CISCO-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, = mibBuilder.importSymbols("CISCO-TC", "Unsigned64")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, IpAddress, MibIdentifier, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits")
DisplayString, DateAndTime, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "TruthValue")
ciscoConfigManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 43))
ciscoConfigManMIB.setRevisions(('2007-04-27 00:00', '2006-08-17 00:00', '2004-06-18 00:00', '2002-06-07 00:00', '2002-03-12 00:00', '1995-11-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoConfigManMIB.setRevisionsDescriptions(('Changes to definition of terminal as an output location.', 'Added a new group of objects to store the information related to the Config Change Tracking ID (CTID) feature. CTID will provide a version number that is unique for version-incrementing changes to the IOS running-configuration. It will also provide information about when CTID last changed. Added scalars: * ccmCTID * ccmCTIDLastChangeTime * ccmCTIDWhoChanged * ccmCTIDRolledOverNotifEnable Added Notification: * ccmCTIDRolledOver Added Object Group: * ciscoConfigManCTIDObjectGroup Added Notification Group: * ciscoConfigManCTIDNotifyGroup Added Compliance: ciscoConfigManMIBComplianceRev4', 'The Objects ccmHistoryEventCommandSourceAddress and ccmHistoryEventServerAddress are deprecated since they support only IPv4 address. These objects have been replaced by two new objects ccmHistoryEventCommandSourceAddrRev1 and ccmHistoryEventServerAddrRev1. In addition to these objects two more new objects are defined ccmHistoryEventCommandSourceAddrType and ccmHistoryEventServerAddrType', 'Added new enumerations networkFtp(8) and networkScp(9) to HistoryEventMedium.', 'Added ccmCLIHistoryCommandTable for storing the CLI commands that took effect during a configuration event. Added scalars ccmCLIHistoryMaxCmdEntries ccmCLIHistoryCmdEntries and ccmCLIHistoryCmdEntriesAllowed. Added ccmHistoryCLICmdEntriesBumped to ccmHistoryEventTable to store the number of corresponding bumped entries in the ccmCLIHistoryCommandTable. Added the ccmCLIRunningConfigChanged notification. Added ccmCLICfgRunConfNotifEnable to control the ccmCLIRunningConfigChanged notification. Added notification group ciscoConfigManHistNotifyGroup. Updated the MIB description to indicate the use of the above additions.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoConfigManMIB.setLastUpdated('200704270000Z')
if mibBuilder.loadTexts: ciscoConfigManMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoConfigManMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoConfigManMIB.setDescription("Configuration management MIB. The MIB represents a model of configuration data that exists in various locations: running in use by the running system terminal saved to whatever is attached as the terminal local saved locally in NVRAM or flash remote saved to some server on the network Although some of the system functions that relate here can be used for general file storage and transfer, this MIB intends to include only such operations as clearly relate to configuration. Its primary emphasis is to track changes and saves of the running configuration. As saved data moves further from startup use, such as into different local flash files or onto the network, tracking becomes difficult to impossible, so the MIB's interest and functions are confined in that area. Information from ccmCLIHistoryCommandTable can be used to track the exact configuration changes that took place within a particular Configuration History event. NMS' can use this information to update the related components. For example: If commands related only to MPLS are entered then the NMS need to update only the MPLS related management information rather than updating all of its management information. Acronyms and terms: CLI Command Line Interface.")
ciscoConfigManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1))
ccmHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1))
ccmCLIHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2))
ccmCLICfg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3))
ccmCTIDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4))
class HistoryEventMedium(TextualConvention, Integer32):
    description = 'The source or destination of a configuration change, save, or copy. erase erasing destination (source only) running live operational data commandSource the command source itself startup what the system will use next reboot local local NVRAM or flash networkTftp network host via Trivial File Transfer networkRcp network host via Remote Copy networkFtp network host via File transfer networkScp network host via Secure Copy '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("erase", 1), ("commandSource", 2), ("running", 3), ("startup", 4), ("local", 5), ("networkTftp", 6), ("networkRcp", 7), ("networkFtp", 8), ("networkScp", 9))

ccmHistoryRunningLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastChanged.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryRunningLastChanged.setDescription('The value of sysUpTime when the running configuration was last changed. If the value of ccmHistoryRunningLastChanged is greater than ccmHistoryRunningLastSaved, the configuration has been changed but not saved.')
ccmHistoryRunningLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryRunningLastSaved.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryRunningLastSaved.setDescription('The value of sysUpTime when the running configuration was last saved (written). If the value of ccmHistoryRunningLastChanged is greater than ccmHistoryRunningLastSaved, the configuration has been changed but not saved. What constitutes a safe saving of the running configuration is a management policy issue beyond the scope of this MIB. For some installations, writing the running configuration to a terminal may be a way of capturing and saving it. Others may use local or remote storage. Thus ANY write is considered saving for the purposes of the MIB.')
ccmHistoryStartupLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryStartupLastChanged.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryStartupLastChanged.setDescription('The value of sysUpTime when the startup configuration was last written to. In general this is the default configuration used when cold starting the system. It may have been changed by a save of the running configuration or by a copy from elsewhere.')
ccmHistoryMaxEventEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryMaxEventEntries.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryMaxEventEntries.setDescription('The maximum number of entries that can be held in ccmHistoryEventTable. The recommended value for implementations is 10.')
ccmHistoryEventEntriesBumped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventEntriesBumped.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventEntriesBumped.setDescription('The number of times the oldest entry in ccmHistoryEventTable was deleted to make room for a new entry.')
ccmHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6), )
if mibBuilder.loadTexts: ccmHistoryEventTable.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTable.setDescription('A table of configuration events on this router.')
ccmHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"))
if mibBuilder.loadTexts: ccmHistoryEventEntry.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventEntry.setDescription('Information about a configuration event on this router.')
ccmHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccmHistoryEventIndex.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventIndex.setDescription('A monotonically increasing integer for the sole purpose of indexing events. When it reaches the maximum value, an extremely unlikely event, the agent wraps the value back to 1 and may flush existing entries.')
ccmHistoryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTime.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTime.setDescription('The value of sysUpTime when the event occurred.')
ccmHistoryEventCommandSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("commandLine", 1), ("snmp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSource.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventCommandSource.setDescription('The source of the command that instigated the event.')
ccmHistoryEventConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 4), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigSource.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventConfigSource.setDescription('The configuration data source for the event.')
ccmHistoryEventConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 5), HistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventConfigDestination.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventConfigDestination.setDescription('The configuration data destination for the event.')
ccmHistoryEventTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("console", 3), ("terminal", 4), ("virtual", 5), ("auxiliary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalType.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTerminalType.setDescription("If ccmHistoryEventCommandSource is 'commandLine', the terminal type, otherwise 'notApplicable'.")
ccmHistoryEventTerminalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalNumber.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTerminalNumber.setDescription("If ccmHistoryEventCommandSource is 'commandLine', the terminal number. The value is -1 if not available or not applicable.")
ccmHistoryEventTerminalUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalUser.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTerminalUser.setDescription("If ccmHistoryEventCommandSource is 'commandLine', the name of the logged in user. The length is zero if not available or not applicable.")
ccmHistoryEventTerminalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventTerminalLocation.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventTerminalLocation.setDescription("If ccmHistoryEventCommandSource is 'commandLine', the hard-wired location of the terminal or the remote host for an incoming connection. The length is zero if not available or not applicable.")
ccmHistoryEventCommandSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddress.setStatus('deprecated')
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddress.setDescription("If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system. If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester. The value is 0.0.0.0 if not available or not applicable. This object is deprecated by ccmHistoryEventCommandSourceAddrRev1")
ccmHistoryEventVirtualHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventVirtualHostName.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventVirtualHostName.setDescription("If ccmHistoryEventTerminalType is 'virtual', the host name of the connected system. The length is zero if not available or not applicable.")
ccmHistoryEventServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddress.setStatus('deprecated')
if mibBuilder.loadTexts: ccmHistoryEventServerAddress.setDescription("If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server. The value is 0.0.0.0 if not applicable or not available. This object is deprecated by ccmHistoryEventServerAddrRev1")
ccmHistoryEventFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventFile.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventFile.setDescription("If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the configuration file name at the storage file server. The length is zero if not available or not applicable.")
ccmHistoryEventRcpUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventRcpUser.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventRcpUser.setDescription("If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkRcp', the remote user name. The length is zero if not applicable or not available.")
ccmHistoryCLICmdEntriesBumped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryCLICmdEntriesBumped.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryCLICmdEntriesBumped.setDescription("The number of times the oldest entry in ccmCLIHistoryCommandTable with first index as ccmHistoryEventIndex was deleted to make room for a new entry. This object is applicable only if ccmHistoryEventCommandSource has a value of 'commandLine'.")
ccmHistoryEventCommandSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 16), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrType.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrType.setDescription('This object indicates the transport type of the address contained in ccmHistoryEventCommandSourceAddrRev1. The value will be zero if not available or not applicable.')
ccmHistoryEventCommandSourceAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 17), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrRev1.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventCommandSourceAddrRev1.setDescription("If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system. If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester. The value of all bit's is zero if not available or not applicable. The Format of this address depends on the value of the ccmHistoryEventCommandSourceAddrType object. This object deprecates ccmHistoryEventCommandSourceAddress")
ccmHistoryEventServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 18), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrType.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventServerAddrType.setDescription('This object indicates the transport type of the address contained in ccmHistoryEventServerAddrRev1. The value will be zero if not available or not aplicable.')
ccmHistoryEventServerAddrRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 19), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmHistoryEventServerAddrRev1.setStatus('current')
if mibBuilder.loadTexts: ccmHistoryEventServerAddrRev1.setDescription("If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server. The value of all bits is 0s if not applicable or not available. The Format of this address depends on the value of the ccmHistoryEventServerAddrType object. This object deprecates ccmHistoryEventServerAddress.")
ccmCLIHistoryMaxCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLIHistoryMaxCmdEntries.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryMaxCmdEntries.setDescription('The maximum number of entries that can be held in ccmCLIHistoryCommandTable. The recommended value for implementations is 100. If the number of entries in ccmCLIHistoryCommandTable exceeds the value of this object, old entries will be bumped to make room for new entries. The ccmCLIHistoryCommandTable will not be populated if the value of this object is 0.')
ccmCLIHistoryCmdEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntries.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntries.setDescription('The current number of entries in ccmCLIHistoryCommandTable.')
ccmCLIHistoryCmdEntriesAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntriesAllowed.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCmdEntriesAllowed.setDescription('This object indicates the upper limit on the number of entries allowed in ccmCLIHistoryCommandTable by the managed system.')
ccmCLIHistoryCommandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4), )
if mibBuilder.loadTexts: ccmCLIHistoryCommandTable.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCommandTable.setDescription('A table of CLI commands that took effect during configuration events.')
ccmCLIHistoryCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"), (0, "CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommandIndex"))
if mibBuilder.loadTexts: ccmCLIHistoryCommandEntry.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCommandEntry.setDescription("Information about the CLI commands that took effect during the configuration event pointed by ccmCLIHistoryEventIndex. A set of rows in this table having the first index as ccmHistoryEventIndex will store the CLI commands entered during the corresponding configuration event in ccmHistoryEventTable. An entry will be created in this table only if the corresponding entry in ccmHistoryEventTable has a value of 'commandLine' for ccmHistoryEventCommandSource.")
ccmCLIHistoryCommandIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ccmCLIHistoryCommandIndex.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCommandIndex.setDescription('A monotonically increasing integer for the purpose of indexing CLI commands which took effect during a configuration event.')
ccmCLIHistoryCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCLIHistoryCommand.setStatus('current')
if mibBuilder.loadTexts: ccmCLIHistoryCommand.setDescription('The CLI command entered which took effect during the configuration event pointed by ccmHistoryEventIndex.')
ccmCLICfgRunConfNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCLICfgRunConfNotifEnable.setStatus('current')
if mibBuilder.loadTexts: ccmCLICfgRunConfNotifEnable.setDescription('This variable indicates whether the system produces the ccmCLIRunningConfigChanged notification. A false value will prevent notifications from being generated by this system.')
ccmCTID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTID.setStatus('current')
if mibBuilder.loadTexts: ccmCTID.setDescription('This object indicates the Config Change Tracking ID which uniquely represents version-incrementing changes to the IOS running configuration.')
ccmCTIDLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDLastChangeTime.setStatus('current')
if mibBuilder.loadTexts: ccmCTIDLastChangeTime.setDescription('This object indicates the time when the Config Change Tracking ID last changed.')
ccmCTIDWhoChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCTIDWhoChanged.setStatus('current')
if mibBuilder.loadTexts: ccmCTIDWhoChanged.setDescription('This object indicates the user who last reset the Config Change Tracking ID.')
ccmCTIDRolledOverNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCTIDRolledOverNotifEnable.setStatus('current')
if mibBuilder.loadTexts: ccmCTIDRolledOverNotifEnable.setDescription('This variable indicates whether the system produces the ccmCTIDRolledOver notification. A false value will prevent notifications from being generated by this system.')
ciscoConfigManMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2))
ciscoConfigManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0))
ciscoConfigManEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"))
if mibBuilder.loadTexts: ciscoConfigManEvent.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManEvent.setDescription('Notification of a configuration management event as recorded in ccmHistoryEventTable.')
ccmCLIRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"))
if mibBuilder.loadTexts: ccmCLIRunningConfigChanged.setStatus('current')
if mibBuilder.loadTexts: ccmCLIRunningConfigChanged.setDescription('This notification indicates that the running configuration of the managed system has changed from the CLI. If the managed system supports a separate configuration mode(where the configuration commands are entered under a configuration session which affects the running configuration of the system), then this notification is sent when the configuration mode is exited. During this configuration session there can be one or more running configuration changes.')
ccmCTIDRolledOver = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 3))
if mibBuilder.loadTexts: ccmCTIDRolledOver.setStatus('current')
if mibBuilder.loadTexts: ccmCTIDRolledOver.setDescription('This notification indicates that the Config Change Tracking ID has rolled over and will be reset.')
ciscoConfigManMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3))
ciscoConfigManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1))
ciscoConfigManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2))
ciscoConfigManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBCompliance = ciscoConfigManMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoConfigManMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Configuration Management MIB')
ciscoConfigManMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev1"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev2 = ciscoConfigManMIBComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev2.setDescription('The compliance statement for entities which implement the Cisco Configuration Management MIB')
ciscoConfigManMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 3)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev3 = ciscoConfigManMIBComplianceRev3.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev3.setDescription('The compliance statement for entities which implement the Cisco Configuration Management MIB. This compliance module deprecates ciscoConfigManMIBCompliance.')
ciscoConfigManMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 4)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistoryGroupRev2"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCLIHistCmdGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManHistNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDNotifyGroup"), ("CISCO-CONFIG-MAN-MIB", "ciscoConfigManCTIDObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManMIBComplianceRev4 = ciscoConfigManMIBComplianceRev4.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManMIBComplianceRev4.setDescription('The compliance statement for entities which implement the Cisco Configuration Management MIB. This compliance module deprecates ciscoConfigManMIBCompliance.')
ciscoConfigManHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 1)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroup = ciscoConfigManHistoryGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoConfigManHistoryGroup.setDescription('Configuration history.')
ciscoConfigManHistoryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 2)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroupRev1 = ciscoConfigManHistoryGroupRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoConfigManHistoryGroupRev1.setDescription('Configuration history.')
ciscoConfigManHistNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 3)).setObjects(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManEvent"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIRunningConfigChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistNotifyGroup = ciscoConfigManHistNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManHistNotifyGroup.setDescription('Notifications of a configuration management event.')
ciscoConfigManHistoryGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 5)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrRev1"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrType"), ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManHistoryGroupRev2 = ciscoConfigManHistoryGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManHistoryGroupRev2.setDescription('Configuration history. This group deprecates the old group ciscoConfigManHistoryGroupRev1')
ciscoConfigManCLIHistCmdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 4)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryMaxCmdEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntries"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntriesAllowed"), ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommand"), ("CISCO-CONFIG-MAN-MIB", "ccmCLICfgRunConfNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCLIHistCmdGroup = ciscoConfigManCLIHistCmdGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManCLIHistCmdGroup.setDescription('CLI commands entered during a configuration history event.')
ciscoConfigManCTIDNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 6)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOver"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCTIDNotifyGroup = ciscoConfigManCTIDNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManCTIDNotifyGroup.setDescription('Notifications of a Config Change Tracking ID event.')
ciscoConfigManCTIDObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 7)).setObjects(("CISCO-CONFIG-MAN-MIB", "ccmCTID"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDLastChangeTime"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDWhoChanged"), ("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOverNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigManCTIDObjectGroup = ciscoConfigManCTIDObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigManCTIDObjectGroup.setDescription('Information about the current CTID value, when CTID last changed, and who last changed the CTID.')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-MIB", ciscoConfigManMIBComplianceRev2=ciscoConfigManMIBComplianceRev2, ccmHistoryEventServerAddrType=ccmHistoryEventServerAddrType, ccmCTID=ccmCTID, ccmHistoryEventConfigDestination=ccmHistoryEventConfigDestination, ccmHistoryRunningLastSaved=ccmHistoryRunningLastSaved, ccmCTIDObjects=ccmCTIDObjects, ccmHistoryEventVirtualHostName=ccmHistoryEventVirtualHostName, ciscoConfigManMIBNotifications=ciscoConfigManMIBNotifications, ccmHistoryEventServerAddress=ccmHistoryEventServerAddress, ccmHistoryEventTime=ccmHistoryEventTime, ccmCLIHistoryCmdEntries=ccmCLIHistoryCmdEntries, ccmCTIDRolledOverNotifEnable=ccmCTIDRolledOverNotifEnable, ccmHistoryEventEntry=ccmHistoryEventEntry, ccmHistoryMaxEventEntries=ccmHistoryMaxEventEntries, ccmHistoryEventCommandSourceAddrType=ccmHistoryEventCommandSourceAddrType, ccmCLIHistoryCommandIndex=ccmCLIHistoryCommandIndex, ciscoConfigManHistNotifyGroup=ciscoConfigManHistNotifyGroup, ccmHistoryEventRcpUser=ccmHistoryEventRcpUser, ccmCLIRunningConfigChanged=ccmCLIRunningConfigChanged, ciscoConfigManMIBComplianceRev4=ciscoConfigManMIBComplianceRev4, ciscoConfigManCLIHistCmdGroup=ciscoConfigManCLIHistCmdGroup, ciscoConfigManCTIDNotifyGroup=ciscoConfigManCTIDNotifyGroup, ccmHistoryEventFile=ccmHistoryEventFile, ciscoConfigManMIBNotificationPrefix=ciscoConfigManMIBNotificationPrefix, ciscoConfigManHistoryGroup=ciscoConfigManHistoryGroup, ccmCLIHistoryMaxCmdEntries=ccmCLIHistoryMaxCmdEntries, ccmHistoryEventTerminalUser=ccmHistoryEventTerminalUser, ccmHistoryEventCommandSourceAddrRev1=ccmHistoryEventCommandSourceAddrRev1, ccmCTIDLastChangeTime=ccmCTIDLastChangeTime, ccmHistoryRunningLastChanged=ccmHistoryRunningLastChanged, ccmHistoryEventTerminalType=ccmHistoryEventTerminalType, ciscoConfigManHistoryGroupRev1=ciscoConfigManHistoryGroupRev1, ccmHistoryEventServerAddrRev1=ccmHistoryEventServerAddrRev1, HistoryEventMedium=HistoryEventMedium, ccmHistoryEventIndex=ccmHistoryEventIndex, ccmCLICfg=ccmCLICfg, ccmHistoryEventTable=ccmHistoryEventTable, ccmHistoryEventTerminalLocation=ccmHistoryEventTerminalLocation, ccmCLIHistoryCommand=ccmCLIHistoryCommand, ciscoConfigManEvent=ciscoConfigManEvent, ciscoConfigManCTIDObjectGroup=ciscoConfigManCTIDObjectGroup, ccmCLICfgRunConfNotifEnable=ccmCLICfgRunConfNotifEnable, ciscoConfigManMIBObjects=ciscoConfigManMIBObjects, ccmCTIDWhoChanged=ccmCTIDWhoChanged, ccmHistoryStartupLastChanged=ccmHistoryStartupLastChanged, ciscoConfigManMIBCompliances=ciscoConfigManMIBCompliances, ciscoConfigManMIBGroups=ciscoConfigManMIBGroups, ccmCTIDRolledOver=ccmCTIDRolledOver, ccmHistoryEventCommandSource=ccmHistoryEventCommandSource, ccmCLIHistoryCommandTable=ccmCLIHistoryCommandTable, ciscoConfigManMIBCompliance=ciscoConfigManMIBCompliance, ccmHistory=ccmHistory, ccmHistoryEventTerminalNumber=ccmHistoryEventTerminalNumber, ccmCLIHistory=ccmCLIHistory, ciscoConfigManHistoryGroupRev2=ciscoConfigManHistoryGroupRev2, PYSNMP_MODULE_ID=ciscoConfigManMIB, ccmHistoryCLICmdEntriesBumped=ccmHistoryCLICmdEntriesBumped, ciscoConfigManMIBConformance=ciscoConfigManMIBConformance, ciscoConfigManMIB=ciscoConfigManMIB, ccmHistoryEventConfigSource=ccmHistoryEventConfigSource, ccmCLIHistoryCommandEntry=ccmCLIHistoryCommandEntry, ccmHistoryEventEntriesBumped=ccmHistoryEventEntriesBumped, ccmCLIHistoryCmdEntriesAllowed=ccmCLIHistoryCmdEntriesAllowed, ciscoConfigManMIBComplianceRev3=ciscoConfigManMIBComplianceRev3, ccmHistoryEventCommandSourceAddress=ccmHistoryEventCommandSourceAddress)
