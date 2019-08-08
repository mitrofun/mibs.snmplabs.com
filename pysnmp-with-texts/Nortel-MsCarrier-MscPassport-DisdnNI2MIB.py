#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DisdnNI2MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DisdnNI2MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:29:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
mscDataSigChanIndex, mscDataSigChan = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex", "mscDataSigChan")
StorageType, DisplayString, Unsigned32, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "DisplayString", "Unsigned32", "RowStatus")
Link, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Bits, TimeTicks, ObjectIdentity, MibIdentifier, Counter32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Counter32", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
disdnNI2MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126))
mscDataSigChanNi2 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12))
mscDataSigChanNi2RowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1), )
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanNi2 components.')
mscDataSigChanNi2RowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanNi2 component.')
mscDataSigChanNi2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanNi2 components. These components can be added and deleted.')
mscDataSigChanNi2ComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2ComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanNi2StorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2StorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2StorageType.setDescription('This variable represents the storage type value for the mscDataSigChanNi2 tables.')
mscDataSigChanNi2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanNi2Index.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2Index.setDescription('This variable represents the index for the mscDataSigChanNi2 tables.')
mscDataSigChanNi2L2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11), )
if mibBuilder.loadTexts: mscDataSigChanNi2L2Table.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2L2Table.setDescription('This group represents the provisionable Layer 2 attributes of the Q931 CCITT protocol.')
mscDataSigChanNi2L2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2L2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2L2Entry.setDescription('An entry in the mscDataSigChanNi2L2Table.')
mscDataSigChanNi2T23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T23.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2T23.setDescription('This attribute specifies the layer2 enable request timer.')
mscDataSigChanNi2T200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2T200.setDescription('This attribute specifies the maximum time between a layer 2 frame and its acknowledgement')
mscDataSigChanNi2N200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2N200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2N200.setDescription('This attribute specifies the maximum number of re-transmissions of a layer2 frame.')
mscDataSigChanNi2T203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T203.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2T203.setDescription('This attribute specifies the maximum time that a no layer 2 traffic situation can last. Expiry triggers a check on whether the far end is a live.')
mscDataSigChanNi2N201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2N201.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2N201.setDescription('This attribute specifies the maximum number of octets in an information field.')
mscDataSigChanNi2CircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2CircuitSwitchedK.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2CircuitSwitchedK.setDescription('This attribute specifies the maximum number of frames for B channel use.')
mscDataSigChanNi2ProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13), )
if mibBuilder.loadTexts: mscDataSigChanNi2ProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ProvTable.setDescription('This group defines the general options of the d-channel signalling link.')
mscDataSigChanNi2ProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2ProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ProvEntry.setDescription('An entry in the mscDataSigChanNi2ProvTable.')
mscDataSigChanNi2Side = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2Side.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2Side.setDescription('This attribute specifies whether the layer 2 HDLC interface is the network or user side of the connection.')
mscDataSigChanNi2OperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15), )
if mibBuilder.loadTexts: mscDataSigChanNi2OperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2OperTable.setDescription('This group provides the operational attributes for the signalling protocol.')
mscDataSigChanNi2OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2OperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2OperEntry.setDescription('An entry in the mscDataSigChanNi2OperTable.')
mscDataSigChanNi2ActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2ActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ActiveChannels.setDescription('This attribute indicates the number of currently active channels. This includes data and voice channels.')
mscDataSigChanNi2PeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2PeakActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2PeakActiveChannels.setDescription('This attribute indicates the maximum number of channels that have been active on this signalling channel during the last polling period.')
mscDataSigChanNi2DChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2DChanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2DChanStatus.setDescription('This attribute indicates the state of the D-channel. outOfService means that there is no layer 2 or layer 3 connectivity to the PBX. establishing means that the signalling channel is attempting to stage the layer 2. established means that the layer 2 is enabled. If the signalling channel stays in the established state, then it is waiting for a restart from the PBX. enabling means that the resources for processing calls are being initialized. If the signalling channel stays in the enabling state then it is waiting for a restart acknowledgement from the PBX. inService means that the resources for processing calls are available. restarting means that the resources for call processing are being rei- initialized.')
mscDataSigChanNi2ToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16), )
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsTable.setDescription('This group contains a series of operational attributes which turn on and off several kinds of tracing.')
mscDataSigChanNi2ToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsEntry.setDescription('An entry in the mscDataSigChanNi2ToolsTable.')
mscDataSigChanNi2Tracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2Tracing.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2Tracing.setDescription('This attribute defines which types of tracing are active for this signalling channel. The tracing messages are sent to the debug stream. To see the messages the agentQueue attribute in Col/debug must be greater than 0 and a Telnet NMIS session must list the debug stream in in its data streams (ex. set nmis telnet session/1 dataStreams debug). Different types of tracing can be enabled simultaneously. Note that tracing consumes additional CPU resources and will slow down call processing on a heavily loaded card. If there is message block exhaustion tracing will be suspended for a period and then automatically reenabled. An alarm is generated on tracing suspension and resumption. This mechanism protects the function processor against excessive numbers of tracing messages. Types of tracing include: protocolErrors - get details of any protocol errors which are occuring. Protocol errors are also reported in summary form as alarms. q931Summary - Summary of the Q.931 messages on the signalling link, including certain call details (calling number, called number, release codes). q931Hex - Q.931 messages displayed in hex format. Useful to determine protocol compliance in case of errors reported on local or remote ends. q931Symbolic - Q.931 messages parsed to give maximum detail. Useful for understanding content of messages flowing on the link. portHex - Messages in hex format being sent and received on the link. Description of bits: protocolErrors(0) q931Summary(1) q931Hex(2) q931Symbolic(3) portHex(4)')
mscDataSigChanNi2Framer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2))
mscDataSigChanNi2FramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanNi2Framer components.')
mscDataSigChanNi2FramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanNi2Framer component.')
mscDataSigChanNi2FramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanNi2Framer components. These components cannot be added nor deleted.')
mscDataSigChanNi2FramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanNi2FramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanNi2Framer tables.')
mscDataSigChanNi2FramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanNi2FramerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerIndex.setDescription('This variable represents the index for the mscDataSigChanNi2Framer tables.')
mscDataSigChanNi2FramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvTable.setDescription('This group contains the base provisioning data for the Framer component. Application or hardware interface specific provisioning data is contained in other provisionable Framer groups.')
mscDataSigChanNi2FramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvEntry.setDescription('An entry in the mscDataSigChanNi2FramerProvTable.')
mscDataSigChanNi2FramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerInterfaceName.setDescription("This attribute contains a hardware component name. The attribute associates the application with a specific link. This defines the module processor on which Framer's parent component (as well as Framer itself) will run.")
mscDataSigChanNi2FramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscDataSigChanNi2FramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateEntry.setDescription('An entry in the mscDataSigChanNi2FramerStateTable.')
mscDataSigChanNi2FramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscDataSigChanNi2FramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscDataSigChanNi2FramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscDataSigChanNi2FramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsTable.setDescription('This group contains the operational statistics data for a Framer component.')
mscDataSigChanNi2FramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsEntry.setDescription('An entry in the mscDataSigChanNi2FramerStatsTable.')
mscDataSigChanNi2FramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmToIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmToIf.setDescription('This attribute counts the number of frames transmitted to the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmFromIf.setDescription('This attribute counts the number of frames received from the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOctetFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOctetFromIf.setDescription('The number of bytes received from the link interface by Framer.')
mscDataSigChanNi2FramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAborts.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAborts.setDescription('This attribute counts the total number of aborts received. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerCrcErrors.setDescription('This attribute counts the total number of frames with CRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLrcErrors.setDescription('This attribute counts the total number of frames with LRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerNonOctetErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerNonOctetErrors.setDescription('This attribute counts the total number of frames that were non octet aligned. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOverruns.setDescription('This attribute counts the total number of frames received from the link for which overruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUnderruns.setDescription('This attribute counts the total number of frames transmitted to the link for which underruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanNi2FramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLargeFrmErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLargeFrmErrors.setDescription('This attribute counts the total number of frames received which were too large. The frame was longer than 500 bytes. This count wraps to zero after reaching its maximum value.')
disdnNI2Group = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1))
disdnNI2GroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1))
disdnNI2GroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3))
disdnNI2GroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3, 2))
disdnNI2Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3))
disdnNI2CapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1))
disdnNI2CapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3))
disdnNI2CapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DisdnNI2MIB", mscDataSigChanNi2FramerLargeFrmErrors=mscDataSigChanNi2FramerLargeFrmErrors, disdnNI2MIB=disdnNI2MIB, mscDataSigChanNi2FramerLrcErrors=mscDataSigChanNi2FramerLrcErrors, mscDataSigChanNi2DChanStatus=mscDataSigChanNi2DChanStatus, mscDataSigChanNi2T200=mscDataSigChanNi2T200, mscDataSigChanNi2FramerProvEntry=mscDataSigChanNi2FramerProvEntry, disdnNI2GroupCA02=disdnNI2GroupCA02, mscDataSigChanNi2FramerFrmToIf=mscDataSigChanNi2FramerFrmToIf, disdnNI2CapabilitiesCA02=disdnNI2CapabilitiesCA02, mscDataSigChanNi2FramerProvTable=mscDataSigChanNi2FramerProvTable, mscDataSigChanNi2FramerRowStatus=mscDataSigChanNi2FramerRowStatus, mscDataSigChanNi2OperTable=mscDataSigChanNi2OperTable, mscDataSigChanNi2FramerUsageState=mscDataSigChanNi2FramerUsageState, mscDataSigChanNi2Tracing=mscDataSigChanNi2Tracing, disdnNI2CapabilitiesCA=disdnNI2CapabilitiesCA, mscDataSigChanNi2FramerOperationalState=mscDataSigChanNi2FramerOperationalState, mscDataSigChanNi2=mscDataSigChanNi2, mscDataSigChanNi2OperEntry=mscDataSigChanNi2OperEntry, mscDataSigChanNi2N200=mscDataSigChanNi2N200, mscDataSigChanNi2FramerIndex=mscDataSigChanNi2FramerIndex, mscDataSigChanNi2FramerOverruns=mscDataSigChanNi2FramerOverruns, mscDataSigChanNi2FramerRowStatusTable=mscDataSigChanNi2FramerRowStatusTable, mscDataSigChanNi2FramerStatsEntry=mscDataSigChanNi2FramerStatsEntry, mscDataSigChanNi2FramerAdminState=mscDataSigChanNi2FramerAdminState, mscDataSigChanNi2FramerStateEntry=mscDataSigChanNi2FramerStateEntry, mscDataSigChanNi2PeakActiveChannels=mscDataSigChanNi2PeakActiveChannels, mscDataSigChanNi2ToolsTable=mscDataSigChanNi2ToolsTable, mscDataSigChanNi2FramerOctetFromIf=mscDataSigChanNi2FramerOctetFromIf, mscDataSigChanNi2Framer=mscDataSigChanNi2Framer, mscDataSigChanNi2FramerUnderruns=mscDataSigChanNi2FramerUnderruns, disdnNI2Capabilities=disdnNI2Capabilities, mscDataSigChanNi2ToolsEntry=mscDataSigChanNi2ToolsEntry, mscDataSigChanNi2CircuitSwitchedK=mscDataSigChanNi2CircuitSwitchedK, mscDataSigChanNi2RowStatusTable=mscDataSigChanNi2RowStatusTable, mscDataSigChanNi2StorageType=mscDataSigChanNi2StorageType, mscDataSigChanNi2ProvTable=mscDataSigChanNi2ProvTable, mscDataSigChanNi2RowStatus=mscDataSigChanNi2RowStatus, mscDataSigChanNi2N201=mscDataSigChanNi2N201, mscDataSigChanNi2FramerInterfaceName=mscDataSigChanNi2FramerInterfaceName, mscDataSigChanNi2FramerAborts=mscDataSigChanNi2FramerAborts, disdnNI2GroupCA=disdnNI2GroupCA, mscDataSigChanNi2FramerRowStatusEntry=mscDataSigChanNi2FramerRowStatusEntry, mscDataSigChanNi2FramerCrcErrors=mscDataSigChanNi2FramerCrcErrors, mscDataSigChanNi2ComponentName=mscDataSigChanNi2ComponentName, mscDataSigChanNi2FramerNonOctetErrors=mscDataSigChanNi2FramerNonOctetErrors, mscDataSigChanNi2L2Entry=mscDataSigChanNi2L2Entry, mscDataSigChanNi2FramerFrmFromIf=mscDataSigChanNi2FramerFrmFromIf, mscDataSigChanNi2T203=mscDataSigChanNi2T203, mscDataSigChanNi2FramerStateTable=mscDataSigChanNi2FramerStateTable, mscDataSigChanNi2L2Table=mscDataSigChanNi2L2Table, disdnNI2Group=disdnNI2Group, mscDataSigChanNi2FramerStatsTable=mscDataSigChanNi2FramerStatsTable, mscDataSigChanNi2FramerComponentName=mscDataSigChanNi2FramerComponentName, mscDataSigChanNi2ActiveChannels=mscDataSigChanNi2ActiveChannels, mscDataSigChanNi2RowStatusEntry=mscDataSigChanNi2RowStatusEntry, disdnNI2GroupCA02A=disdnNI2GroupCA02A, mscDataSigChanNi2Side=mscDataSigChanNi2Side, mscDataSigChanNi2FramerStorageType=mscDataSigChanNi2FramerStorageType, disdnNI2CapabilitiesCA02A=disdnNI2CapabilitiesCA02A, mscDataSigChanNi2ProvEntry=mscDataSigChanNi2ProvEntry, mscDataSigChanNi2T23=mscDataSigChanNi2T23, mscDataSigChanNi2Index=mscDataSigChanNi2Index)