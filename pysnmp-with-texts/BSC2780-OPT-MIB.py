#
# PySNMP MIB module BSC2780-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSC2780-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, MibIdentifier, Integer32, Gauge32, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, iso, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "iso", "TimeTicks", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
class DisplayString(OctetString):
    pass

cdx6500PPCTBSC2780Table = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11), )
if mibBuilder.loadTexts: cdx6500PPCTBSC2780Table.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTBSC2780Table.setDescription('A table of BSC2780 Port configuration entries.')
cdx6500bsc2780PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1), ).setIndexNames((0, "BSC2780-OPT-MIB", "cdx6500bsc2780PortNumber"))
if mibBuilder.loadTexts: cdx6500bsc2780PortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortConfigEntry.setDescription('A BSC2780 Configuration Table entry. Each entry contains the configuration parameters for a single BSC2780 port. ')
cdx6500bsc2780PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortNumber.setDescription('The BSC2780 port number described by this entry.')
cdx6500bsc2780ClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("int", 0), ("ext", 1), ("newvalInt", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ClockSource.setDescription("int - internal clock source. ext - external clock source. newvalInt - same functionality as 'int', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780ClockSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1200, 19200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ClockSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ClockSpeed.setDescription('This is the speed of the port in bits per second, when using internal clocking.')
cdx6500bsc2780Contention = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("hdx", 0), ("fdx", 1), ("newvalHdx", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780Contention.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780Contention.setDescription("Indicates whether Half Duplex (hdx) or Full Duplex (fdx) modem signals are being generated. Full Duplex indicates communication is occuring in both directions simultaneously between devices. Half Duplex indicates transmission is occuring in both directions, but only in one direction at a time. newvalHdx : same functionality as 'hdx', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780ErrThreshCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ErrThreshCount.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ErrThreshCount.setDescription('Indicates number of consecutive errors that can occur before a device is considered down.')
cdx6500bsc2780DisConnOnError = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("no", 0), ("yes", 1), ("newvalNo", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780DisConnOnError.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780DisConnOnError.setDescription("Specifies whether a session should be disconnected if a control unit has not responded once the Error Threshold Count has been exceeded. newvalNo : same functionality as 'no',new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780ConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 5, 13, 14, 16, 19, 50))).clone(namedValues=NamedValues(("simp", 0), ("emri", 3), ("dimo", 5), ("v25b", 13), ("rs366", 14), ("emrih", 16), ("dimoh", 19), ("newvalSimp", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ConnType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ConnType.setDescription("Specify the control signal handshake required for a connection to be made to this port: simp - simple, no control signals required v25b - port emulates a dial modem using V.25 bis mode 108/2 rs366 - port emulates data port for the 801 autodialer emri - port emulates a dial modem with ring indicator (RI) dimo - port handshakes with attached modem NODE BOOT will be required when this type is changed to/from rs366 or v25b. newvalSimp - same functionality as 'simp', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780InterBuffTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780InterBuffTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780InterBuffTimeout.setDescription('Specifies the maximum amount of time in seconds the PAD will wait for the end of a multi-packet message from the network. If this time limit is exceeded, the PAD will abort the entire message and request retransmission.')
cdx6500bsc2780PortSubAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortSubAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortSubAddr.setDescription('0 - 3 Decimal digits Calls addressed to this node and with this subaddress will be routed to this port.')
cdx6500bsc2780ReConnRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ReConnRetry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ReConnRetry.setDescription('Number of times connection will be reattempted after a network induced disconnect.')
cdx6500bsc2780AutocallMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780AutocallMnemonic.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780AutocallMnemonic.setDescription('This mnemonic name is used if this device is configured as a call originator.')
cdx6500bsc2780RestrictConnDest = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780RestrictConnDest.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780RestrictConnDest.setDescription('All calls originating from this port will be routed to the destination specified in this parameter, irrespective of route selection table entries. For example, to route calls to port 1, use P1. To route calls to port 2, station 4, use P2S4. Blank this field to disable this function.')
cdx6500bsc2780BillRec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("newvalOff", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780BillRec.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780BillRec.setDescription("This controls whether billing (accounting) records will be created for calls on this port. off - billing (accounting) records will not be created. on - billing (accounting) records will be created. newvalOff - same functionality as 'off', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780DSRfollowSVC = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("no", 0), ("yes", 1), ("newvalNo", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780DSRfollowSVC.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780DSRfollowSVC.setDescription("Specify whether DSR on/off required with circuit on/off. This is only available with connection type SIMP or RS366. yes = DSR will be ON only while a call is in place, The DTE connected to the port can not originate a call no = DSR is always ON. newvalNo : same functionality as 'no', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780DSRholdTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780DSRholdTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780DSRholdTime.setDescription('Time in steps of 50 ms to drop DSR signal after the circuit is disconnected in DSR-Follow-SVC mode. This timer value is ignored otherwise. ')
cdx6500bsc2780PortOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deprecatedObj", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortOption.setStatus('deprecated')
if mibBuilder.loadTexts: cdx6500bsc2780PortOption.setDescription('This object has been deprecated, It is replaced by cdx6500bsc2780PortOptString.')
cdx6500bsc2780TrafficPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 50))).clone(namedValues=NamedValues(("lowPriority", 0), ("medPriority", 1), ("hiPriority", 2), ("xpPriority", 3), ("newvalLowPriority", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780TrafficPriority.setStatus('optional')
if mibBuilder.loadTexts: cdx6500bsc2780TrafficPriority.setDescription("This is the traffic priority of the 2780 device; low, medium, high, and expedite. newvalLowPriority : same functionality as 'lowPriority', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780PortOptString = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortOptString.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortOptString.setDescription('This is the new object for cdx6500bsc2780PortOption. Specify any of the following port control options: NONE - no option specified. EOT - EOT will be dropped when no data has been sent across network. ACK - End-to-End Acknowledgements are to be used. TID - Host/Terminal ID(0-120 characters) with initial line Bid/Response is to be exchanged. NOTTD - does not send a TTD control character. Any combination of above specified by summing(e.g. ACK+TID).')
cdx6500bsc2780IdleDiscTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780IdleDiscTimer.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780IdleDiscTimer.setDescription('The call on the port will be cleared when this timer is expired. This timer will be started when it received an EOT. 0 - Timer Disabled. 1 to 60 - Timer Value in seconds.')
cdx6500bsc2780ElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780ElectricalInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780ElectricalInterfaceType.setDescription('Specify the Electrical Interface Type: V.24 - V.24 Interface Type V.35 - V.35 Electrical Interface Type V.36 - V.36 Electrical Interface Type X.21 - X.21 Electrical Interface Type NONE - Electrically disabled')
cdx6500bsc2780V24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780V24ElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780V24ElectricalInterfaceOption.setDescription('Specify the Pin 22 option: RI - V.24 uses Pin 22 for Ring Indicator output signal TM - V.24 uses Pin 22 for Test Mode input signal')
cdx6500bsc2780HighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780HighSpeedElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780HighSpeedElectricalInterfaceOption.setDescription('Specify the cable type: NONE - V.35/V.36/X.21 DCE with straight through cable XOVER - V.35/V.36/X.21 DCE with crossover adapter cable')
cdx6500bsc2780RemoteType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t2780", 1), ("snaint", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780RemoteType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780RemoteType.setDescription(' Specify the remote type: T2780 - remote is BSC2780 PAD SNAINT - remote is SNA/2780 Interactive')
cdx6500PPSTBSC2780Table = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11), )
if mibBuilder.loadTexts: cdx6500PPSTBSC2780Table.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPSTBSC2780Table.setDescription('A table of BSC2780 port statistics entries.')
cdx6500bsc2780PortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1), ).setIndexNames((0, "BSC2780-OPT-MIB", "cdx6500bsc2780StatPortNumber"))
if mibBuilder.loadTexts: cdx6500bsc2780PortStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortStatEntry.setDescription('A BSC2780 Port Statistic Table entry. Each entry contains the statistics for a single BSC2780 port.')
cdx6500bsc2780StatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780StatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780StatPortNumber.setDescription('The BSC2780 port number described by this entry.')
cdx6500bsc2780PortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 50))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("busyOut", 2), ("up", 3), ("down", 4), ("newvalDisabled", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortStatus.setDescription("Port Status indicates whether or not the port is switched on and is ready for operation. This value may be one of : up - Port is up and running. down - port is down. disabled - port has been disabled. enabled - port has been enabled, but is not yet Up. busyOut - port has been set to be disabled as soon as last active session is disestablished. No new sessions will be established. newvalDisabled - same functionality as 'disabled', new enumeration introduced for RFC1155 compatibility.")
cdx6500bsc2780PortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortState.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortState.setDescription('Port State indicates what the port is actually in the process of doing. This value may be one of : DISC - No call is currently connected to the specified port. The port is IDLE. PENACC - The specified port is waiting for a call accept. DATA - The port is busy. Data is being passed between 2780/3780 devices. PENDACK - The port has sent a message (text) or an enquiry (ENQ) and is waiting for an acknowledgement (ACK). EOT - End of transmission (EOT) is received. The port is waiting for a new line bid. DRO - Outbound Data is restrained. DRI - Inbound Data is restrained. PENDISC - The port is waiting for disconnection. The device sends an EOT perior to accepting a call. PENDNAK - The port has sent a message (text) with the bad BCC and is waiting for a negative acknowledgement (NAK). PENDEIA - The port is waiting for connecting to the attached device. PENEIADISC - The port is waiting for receiving all packets acknowledged from remote before disconnecting to the local device. WT4TIMEOUT - The port is waiting for clearing the internal buffers before dropping the EIA signals. TTD - Temporary text delay (TTD) is received. The port is waiting for sending a negative acknowledgement (NAK) to the local device. WTTDNAK - The port has sent a temporary text delay (TTD) and is waiting for a negative acknowledgement (NAK). RACK - The port has sent a message (text) to the remote and is waiting for an End-to-End acknowledgement. TID - The port is waiting for an initial enquiry (ENQ) or acknowledgement (ACK0) with the host/terminal ID from the local device. RTID - The port is waiting for an initial enquiry (ENQ) or acknowledgement (ACK0) with the host/terminal ID from the remote device.')
cdx6500bsc2780PortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortSpeed.setDescription('This is the speed of the port if clock is internal. If clock is external, this is the detected clock speed. If Port Speed is 0, clock is external, but clocking is not being received from attatched device.')
cdx6500bsc2780PortUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortUtilIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortUtilIn.setDescription('Percentage of Port input bandwidth in use.')
cdx6500bsc2780PortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780PortUtilOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780PortUtilOut.setDescription('Percentage of Port output bandwidth in use.')
cdx6500bsc2780InMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780InMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780InMsgs.setDescription('Number of message received since last node, port, or statistics reset.')
cdx6500bsc2780OutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780OutMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780OutMsgs.setDescription('Number of message sent since last node, port, or statistics reset.')
cdx6500bsc2780InChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780InChars.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780InChars.setDescription('Number of characters received since last node, port, or statistics reset.')
cdx6500bsc2780OutChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780OutChars.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780OutChars.setDescription('Number of characters sent since last node, port, or statistics reset.')
cdx6500bsc2780CharRateIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780CharRateIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780CharRateIn.setDescription('Number of characters received per second.')
cdx6500bsc2780CharRateOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780CharRateOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780CharRateOut.setDescription('Number of characters sent per second.')
cdx6500bsc2780CrcBccErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500bsc2780CrcBccErrs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500bsc2780CrcBccErrs.setDescription('Number of CRC errors since last node, port, or statistics reset.')
mibBuilder.exportSymbols("BSC2780-OPT-MIB", cdx6500bsc2780PortNumber=cdx6500bsc2780PortNumber, cdx6500bsc2780PortSubAddr=cdx6500bsc2780PortSubAddr, cdx6500bsc2780InterBuffTimeout=cdx6500bsc2780InterBuffTimeout, cdx6500bsc2780ConnType=cdx6500bsc2780ConnType, cdx6500bsc2780ClockSource=cdx6500bsc2780ClockSource, cdx6500bsc2780PortOption=cdx6500bsc2780PortOption, cdx6500Configuration=cdx6500Configuration, cdx6500bsc2780PortConfigEntry=cdx6500bsc2780PortConfigEntry, cdx6500bsc2780PortUtilIn=cdx6500bsc2780PortUtilIn, cdx6500bsc2780CrcBccErrs=cdx6500bsc2780CrcBccErrs, cdx6500bsc2780PortStatEntry=cdx6500bsc2780PortStatEntry, cdx6500Statistics=cdx6500Statistics, cdxProductSpecific=cdxProductSpecific, cdx6500bsc2780ClockSpeed=cdx6500bsc2780ClockSpeed, cdx6500bsc2780TrafficPriority=cdx6500bsc2780TrafficPriority, cdx6500bsc2780InMsgs=cdx6500bsc2780InMsgs, cdx6500bsc2780CharRateIn=cdx6500bsc2780CharRateIn, cdx6500bsc2780ElectricalInterfaceType=cdx6500bsc2780ElectricalInterfaceType, cdx6500bsc2780AutocallMnemonic=cdx6500bsc2780AutocallMnemonic, cdx6500bsc2780PortStatus=cdx6500bsc2780PortStatus, cdx6500bsc2780DSRholdTime=cdx6500bsc2780DSRholdTime, cdx6500bsc2780StatPortNumber=cdx6500bsc2780StatPortNumber, cdx6500bsc2780Contention=cdx6500bsc2780Contention, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500bsc2780ErrThreshCount=cdx6500bsc2780ErrThreshCount, cdx6500=cdx6500, cdx6500bsc2780PortUtilOut=cdx6500bsc2780PortUtilOut, cdx6500bsc2780DSRfollowSVC=cdx6500bsc2780DSRfollowSVC, cdx6500PPCTBSC2780Table=cdx6500PPCTBSC2780Table, cdx6500bsc2780PortOptString=cdx6500bsc2780PortOptString, cdx6500bsc2780V24ElectricalInterfaceOption=cdx6500bsc2780V24ElectricalInterfaceOption, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500bsc2780InChars=cdx6500bsc2780InChars, cdx6500bsc2780HighSpeedElectricalInterfaceOption=cdx6500bsc2780HighSpeedElectricalInterfaceOption, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500bsc2780RestrictConnDest=cdx6500bsc2780RestrictConnDest, cdx6500bsc2780OutMsgs=cdx6500bsc2780OutMsgs, cdx6500bsc2780DisConnOnError=cdx6500bsc2780DisConnOnError, cdx6500PPSTBSC2780Table=cdx6500PPSTBSC2780Table, cdx6500bsc2780ReConnRetry=cdx6500bsc2780ReConnRetry, cdx6500bsc2780BillRec=cdx6500bsc2780BillRec, cdx6500bsc2780PortSpeed=cdx6500bsc2780PortSpeed, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500bsc2780CharRateOut=cdx6500bsc2780CharRateOut, DisplayString=DisplayString, cdx6500bsc2780IdleDiscTimer=cdx6500bsc2780IdleDiscTimer, cdx6500bsc2780PortState=cdx6500bsc2780PortState, codex=codex, cdx6500bsc2780RemoteType=cdx6500bsc2780RemoteType, cdx6500bsc2780OutChars=cdx6500bsc2780OutChars)
