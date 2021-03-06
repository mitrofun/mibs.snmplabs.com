#
# PySNMP MIB module Unisphere-Data-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-LOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:31:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, TimeTicks, Counter64, MibIdentifier, NotificationType, Bits, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "Bits", "ModuleIdentity", "ObjectIdentity")
TruthValue, TimeStamp, DisplayString, TextualConvention, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention", "RowStatus", "DateAndTime")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdLogSeverity, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdLogSeverity")
usdLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28))
usdLogMIB.setRevisions(('2001-03-16 19:02', '2000-03-27 05:00', '1999-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdLogMIB.setRevisionsDescriptions(('Make it SMIv2 conformant.', 'Replace single syslog destination with table of syslog destinations, and add syslog facility as an attribute for syslogs.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdLogMIB.setLastUpdated('200103161902Z')
if mibBuilder.loadTexts: usdLogMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdLogMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdLogMIB.setDescription('The Log MIB for the Unisphere Networks Inc. enterprise.')
class UsdLogCatName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    description = 'The name of a log category. Represents textual information taken from the NVT ASCII character set.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class UsdLogVerbosity(TextualConvention, Integer32):
    description = 'The log verbosity level. Not all event types offer medium- or high-verbosity levels of detail.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("medium", 1), ("high", 2))

class UsdLogSyslogFacility(TextualConvention, Integer32):
    description = 'The syslog daemon facility id.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))

usdLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1))
usdLogDestinations = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1))
usdLogCategories = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2))
usdLogMessages = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3))
usdLogDestSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1))
usdLogDestConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2))
usdLogDestNvFile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3))
usdLogDestSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestSyslogSeverity.setStatus('obsolete')
if mibBuilder.loadTexts: usdLogDestSyslogSeverity.setDescription("The minimum severity level of messages sent to the SYSLOG server. A value of 'off' indicates no log messages are sent to this destination.")
usdLogDestSyslogAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestSyslogAddress.setStatus('obsolete')
if mibBuilder.loadTexts: usdLogDestSyslogAddress.setDescription('The IP address of the SYSLOG server to which log messages are to be sent. A value of 0.0.0.0 indicates no server address is configured.')
usdLogSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3), )
if mibBuilder.loadTexts: usdLogSyslogTable.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogTable.setDescription('A table describing the characteristics of each syslog destination.')
usdLogSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogSyslogIpAddress"))
if mibBuilder.loadTexts: usdLogSyslogEntry.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogEntry.setDescription('An entry describingthe characteristics of a syslog destination.')
usdLogSyslogIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: usdLogSyslogIpAddress.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogIpAddress.setDescription('The IP address of this syslog destination. This value must be a unicast IP address.')
usdLogSyslogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogRowStatus.setDescription("Controls creation/deletion of entries in this table. Only 'createAndGo' and 'destroy' are supported.")
usdLogSyslogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 3), UsdLogSeverity().clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogSeverity.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogSeverity.setDescription("The severity level for this syslog destination. Setting this value to 'off' suppresses log messages from being sent to this syslog destination.")
usdLogSyslogFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 4), UsdLogSyslogFacility().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogFacility.setStatus('current')
if mibBuilder.loadTexts: usdLogSyslogFacility.setDescription('The facility id attached to messages sent to this syslog destination.')
usdLogDestConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestConsoleSeverity.setStatus('current')
if mibBuilder.loadTexts: usdLogDestConsoleSeverity.setDescription("The minimum severity level of messages sent to the console. A value of 'off' indicates no log messages are sent to this destination.")
usdLogDestNvFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestNvFileSeverity.setStatus('current')
if mibBuilder.loadTexts: usdLogDestNvFileSeverity.setDescription("The minimum severity level of messages sent to the nonvolatile log file. A value of 'off' indicates no log messages are to be sent to this destination.")
usdLogCatScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 1))
usdLogCatTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2), )
if mibBuilder.loadTexts: usdLogCatTable.setStatus('current')
if mibBuilder.loadTexts: usdLogCatTable.setDescription('A table describing the characteristics of each log category.')
usdLogCatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogCatIndex"))
if mibBuilder.loadTexts: usdLogCatEntry.setStatus('current')
if mibBuilder.loadTexts: usdLogCatEntry.setDescription('An entry describing the characteristics of a log category.')
usdLogCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: usdLogCatIndex.setStatus('current')
if mibBuilder.loadTexts: usdLogCatIndex.setDescription('An integer index uniquely associated with a log. Index values do not necessarily persist across system reboots. Following reboot, mappings of (reboot-invariant) log category names to log index values is available in the usdLogCatNameTable.')
usdLogCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 2), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatName.setStatus('current')
if mibBuilder.loadTexts: usdLogCatName.setDescription('The name of this log category.')
usdLogCatDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatDescr.setStatus('current')
if mibBuilder.loadTexts: usdLogCatDescr.setDescription('A description of the functionality for which events are recorded by this log category.')
usdLogCatEngineering = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatEngineering.setStatus('current')
if mibBuilder.loadTexts: usdLogCatEngineering.setDescription('An indication of whether this log is intended mainly for engineering development and debug purposes.')
usdLogCatDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatDiscards.setStatus('current')
if mibBuilder.loadTexts: usdLogCatDiscards.setDescription('The number of messages generated by this log category that were discarded because of resource limitations.')
usdLogCatSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 6), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogCatSeverity.setStatus('current')
if mibBuilder.loadTexts: usdLogCatSeverity.setDescription("The severity level for this log category. The value 'off' disables recording of this log category's messages. For other severity level values, only messages at or above this severity level will be logged in usdLogMsgTable.")
usdLogCatVerbosity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 7), UsdLogVerbosity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogCatVerbosity.setStatus('current')
if mibBuilder.loadTexts: usdLogCatVerbosity.setDescription('The verbosity level for this log category. Supplementary information may be available for certain event types. This object controls whether that additional information, if available for a given event, is recorded.')
usdLogCatNameTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3), )
if mibBuilder.loadTexts: usdLogCatNameTable.setStatus('current')
if mibBuilder.loadTexts: usdLogCatNameTable.setDescription("A table mapping each log category's name to its index.")
usdLogCatNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1), ).setIndexNames((1, "Unisphere-Data-LOG-MIB", "usdLogCatNameName"))
if mibBuilder.loadTexts: usdLogCatNameEntry.setStatus('current')
if mibBuilder.loadTexts: usdLogCatNameEntry.setDescription("An entry mapping a log category's name to its index.")
usdLogCatNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 1), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatNameName.setStatus('current')
if mibBuilder.loadTexts: usdLogCatNameName.setDescription('The name of the log category.')
usdLogCatNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatNameIndex.setStatus('current')
if mibBuilder.loadTexts: usdLogCatNameIndex.setDescription('The log index associated with this log category.')
usdLogMsgScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1))
usdLogMsgCapacity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 1), Integer32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCapacity.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgCapacity.setDescription('The maximum capacity, in number of log messages, of the usdLogMsgTable.')
usdLogMsgLastSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgLastSeqNumber.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgLastSeqNumber.setDescription("The sequence number of the most recent usdLogMsgTable entry. By monitoring this object's rate of change in relation to the usdLogMsgTable capacity, a management client can determine whether it is polling usdLogMsgTable frequently enough to avoid missing log messages.")
usdLogMsgTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2), )
if mibBuilder.loadTexts: usdLogMsgTable.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgTable.setDescription('A table of log messages generated by this device.')
usdLogMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogMsgSysUpTimeStamp"), (0, "Unisphere-Data-LOG-MIB", "usdLogMsgSequenceNumber"))
if mibBuilder.loadTexts: usdLogMsgEntry.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgEntry.setDescription('A log message generated by this device.')
usdLogMsgSysUpTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 1), TimeStamp())
if mibBuilder.loadTexts: usdLogMsgSysUpTimeStamp.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgSysUpTimeStamp.setDescription('The value of sysUpTime when this log message was recorded.')
usdLogMsgSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: usdLogMsgSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgSequenceNumber.setDescription('A sequence number that uniquely identifies this entry. Sequence numbers are assigned consecutively beginning with 1. More recent entries have higher sequence numbers.')
usdLogMsgCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 3), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCatName.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgCatName.setDescription('Name of the log category that contributed this message.')
usdLogMsgCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCatIndex.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgCatIndex.setDescription('Index of the log category that contributed this message.')
usdLogMsgSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 5), UsdLogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgSeverity.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgSeverity.setDescription('The severity of the message.')
usdLogMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgText.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgText.setDescription("The text of the log message. Truncation of log message text is indicated by n asterisk character ('*') in the last octet of a maximum-size string.")
usdLogMsgDateAndTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgDateAndTimeStamp.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgDateAndTimeStamp.setDescription('The date and time this message was generated.')
usdLogTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2))
usdLogMsgThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogMsgThreshold.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgThreshold.setDescription('Number of log messages which, when added to usdLogMsgTable, cause a usdLogMsgThresholdTrap to be generated. This value is expressed as a percentage of the capacity of usdLogMsgTable. A value of zero disables trap generation.')
usdLogTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0))
usdLogMsgThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if mibBuilder.loadTexts: usdLogMsgThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: usdLogMsgThresholdTrap.setDescription('This trap is generated to report that an incremental number of log messages (described by the value of usdLogMsgThreshold) have been added to usdLogMsgTable.')
usdLogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4))
usdLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1))
usdLogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2))
usdLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogCompliance = usdLogCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdLogCompliance.setDescription('The compliance statement for entities which implement the Unisphere Networks, Inc. Log MIB.')
usdLogCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 2)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogGroup2"), ("Unisphere-Data-LOG-MIB", "usdLogTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogCompliance2 = usdLogCompliance2.setStatus('current')
if mibBuilder.loadTexts: usdLogCompliance2.setDescription('The compliance statement for entities which implement the Unisphere Networks. Log MIB., including support for multiple SYSLOG destinations.')
usdLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogDestSyslogSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestSyslogAddress"), ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatName"), ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"), ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"), ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"), ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgText"), ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogGroup = usdLogGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdLogGroup.setDescription('A collection of objects providing management of Unisphere Networks, Inc. logging capabilities.')
usdLogGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 2)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogSyslogRowStatus"), ("Unisphere-Data-LOG-MIB", "usdLogSyslogSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogSyslogFacility"), ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatName"), ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"), ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"), ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"), ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgText"), ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogGroup2 = usdLogGroup2.setStatus('current')
if mibBuilder.loadTexts: usdLogGroup2.setDescription('A collection of objects providing management of Unisphere Networks, Inc logging capabilities, including support for multiple SYSLOG destinations.')
usdLogTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 3)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogMsgThresholdTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogTrapGroup = usdLogTrapGroup.setStatus('current')
if mibBuilder.loadTexts: usdLogTrapGroup.setDescription('A management notification pertaining to logging operations.')
mibBuilder.exportSymbols("Unisphere-Data-LOG-MIB", usdLogGroup2=usdLogGroup2, usdLogSyslogEntry=usdLogSyslogEntry, usdLogDestConsoleSeverity=usdLogDestConsoleSeverity, usdLogSyslogRowStatus=usdLogSyslogRowStatus, usdLogDestNvFileSeverity=usdLogDestNvFileSeverity, usdLogCategories=usdLogCategories, usdLogTrapGroup=usdLogTrapGroup, usdLogSyslogSeverity=usdLogSyslogSeverity, usdLogCatName=usdLogCatName, usdLogMIBCompliances=usdLogMIBCompliances, usdLogDestConsole=usdLogDestConsole, usdLogSyslogIpAddress=usdLogSyslogIpAddress, usdLogCatScalars=usdLogCatScalars, usdLogMsgEntry=usdLogMsgEntry, usdLogCatSeverity=usdLogCatSeverity, usdLogSyslogTable=usdLogSyslogTable, usdLogMsgLastSeqNumber=usdLogMsgLastSeqNumber, usdLogSyslogFacility=usdLogSyslogFacility, usdLogCatEngineering=usdLogCatEngineering, usdLogMsgScalars=usdLogMsgScalars, usdLogMIB=usdLogMIB, usdLogCatDiscards=usdLogCatDiscards, usdLogMsgSysUpTimeStamp=usdLogMsgSysUpTimeStamp, usdLogCatEntry=usdLogCatEntry, usdLogCatNameName=usdLogCatNameName, usdLogMsgThreshold=usdLogMsgThreshold, usdLogDestSyslog=usdLogDestSyslog, usdLogDestNvFile=usdLogDestNvFile, usdLogMsgCapacity=usdLogMsgCapacity, usdLogDestSyslogSeverity=usdLogDestSyslogSeverity, usdLogTrapPrefix=usdLogTrapPrefix, usdLogCatDescr=usdLogCatDescr, usdLogCatVerbosity=usdLogCatVerbosity, usdLogMsgTable=usdLogMsgTable, usdLogGroup=usdLogGroup, usdLogMsgSequenceNumber=usdLogMsgSequenceNumber, usdLogMsgSeverity=usdLogMsgSeverity, usdLogCatNameEntry=usdLogCatNameEntry, usdLogMIBConformance=usdLogMIBConformance, usdLogCompliance=usdLogCompliance, usdLogCatTable=usdLogCatTable, usdLogMIBGroups=usdLogMIBGroups, usdLogCatNameIndex=usdLogCatNameIndex, usdLogDestSyslogAddress=usdLogDestSyslogAddress, usdLogMsgText=usdLogMsgText, UsdLogVerbosity=UsdLogVerbosity, usdLogMsgCatName=usdLogMsgCatName, usdLogCatNameTable=usdLogCatNameTable, usdLogCompliance2=usdLogCompliance2, UsdLogCatName=UsdLogCatName, usdLogDestinations=usdLogDestinations, usdLogTrapControl=usdLogTrapControl, usdLogCatIndex=usdLogCatIndex, usdLogMsgThresholdTrap=usdLogMsgThresholdTrap, usdLogMessages=usdLogMessages, usdLogObjects=usdLogObjects, PYSNMP_MODULE_ID=usdLogMIB, usdLogMsgCatIndex=usdLogMsgCatIndex, usdLogMsgDateAndTimeStamp=usdLogMsgDateAndTimeStamp, UsdLogSyslogFacility=UsdLogSyslogFacility)
