#
# PySNMP MIB module Fore-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-DS3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, ObjectIdentity, Counter32, Counter64, iso, NotificationType, MibIdentifier, Bits, ModuleIdentity, Integer32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "iso", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreDs3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3))
if mibBuilder.loadTexts: foreDs3.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreDs3.setOrganization('FORE')
if mibBuilder.loadTexts: foreDs3.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreDs3.setDescription(' This MIB module supports the FORE DS3 port module.')
ds3ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1))
ds3StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2))
ds3ConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ds3ConfTable.setStatus('current')
if mibBuilder.loadTexts: ds3ConfTable.setDescription('A table of DS3 switch port configuration information.')
ds3ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "Fore-DS3-MIB", "ds3ConfBoard"), (0, "Fore-DS3-MIB", "ds3ConfModule"), (0, "Fore-DS3-MIB", "ds3ConfPort"))
if mibBuilder.loadTexts: ds3ConfEntry.setStatus('current')
if mibBuilder.loadTexts: ds3ConfEntry.setDescription('A table entry containing DS3 configuration information for each port. Not all RFC1407 configuration table variables are included, and some are modified.')
ds3ConfBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ConfBoard.setStatus('current')
if mibBuilder.loadTexts: ds3ConfBoard.setDescription("The index of this port's switch board.")
ds3ConfModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ConfModule.setStatus('current')
if mibBuilder.loadTexts: ds3ConfModule.setDescription('The network module of this port.')
ds3ConfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ConfPort.setStatus('current')
if mibBuilder.loadTexts: ds3ConfPort.setDescription('The number of this port.')
ds3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds3Other", 1), ("ds3M23", 2), ("ds3SYNTRAN", 3), ("ds3CbitParity", 4), ("ds3ClearChannel", 5))).clone('ds3CbitParity')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LineType.setStatus('current')
if mibBuilder.loadTexts: ds3LineType.setDescription('This variable indicates the variety of DS3 C-bit application implementing this interface. The type of interface affects the interpretation of the usage and error statistics. This variable is defined in the rfc1407 configuration table as dsx3LineType. According to rfc1407, the different values are: ds3M23 specification: ANSI T1.107-1988 ds3SYNTRAN specification: ANSI T1.107-1988 ds3CbitParity specification: ANSI T1.107a-1989 ds3CleatChannel specification: ANSI T1.102-1987.')
ds3LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3Other", 1), ("ds3B3ZS", 2))).clone('ds3B3ZS')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3LineCoding.setStatus('current')
if mibBuilder.loadTexts: ds3LineCoding.setDescription('This variable describes the variety of Zero Code suppression used on this interface, which in turn affects a number of its characteristics. ds3B3ZS (2) refers to the use of specified pattern of normal bits and bipolar violations which are used to replaced sequences of zero bits of specified length. This variable is defined in the rfc1407 configuration table as dsx3LineCoding.')
ds3SendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds3SendNoCode", 1), ("ds3SendLineCode", 2), ("ds3SendPayloadCode", 3), ("ds3SendResetCode", 4), ("ds3SendDS1LoopCode", 5), ("ds3SendTestPattern", 6))).clone('ds3SendNoCode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3SendCode.setStatus('current')
if mibBuilder.loadTexts: ds3SendCode.setDescription('This variable indicates what type of code is being sent across the DS3/E3 interface by the device. The values mean: ds3SendNoCode sending looped or normal data ds3SendLineCode sending request for a line loopback ds3SendPayloadCode sending a request for a payload loopback (i.e. all DS1/E1 in a DS3/E3 frame) ds3SendResetCode sending a loopback deactivation request ds3SendDS1LoopCode requesting to loopback a particular DS1/E1 within a DS3/E3 frame ds3SendTestPattern sending a test pattern.')
ds3ReceiveCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds3ReceiveNoCode", 1), ("ds3ReceiveLineCode", 2), ("ds3ReceivePayloadCode", 3), ("ds3ReceiveResetCode", 4), ("ds3ReceiveDS1LoopCode", 5), ("ds3ReceiveTestPattern", 6))).clone('ds3ReceiveNoCode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ReceiveCode.setStatus('current')
if mibBuilder.loadTexts: ds3ReceiveCode.setDescription('This variable indicates the type of code that was received across the DS3/E3 interface. The values mean: ds3ReceiveNoCode receiving looped or normal data ds3ReceiveLineCode receiving request for a line loopback ds3ReceivePayloadCode receiving a request for a payload loopback (i.e. all DS1/E1 in a DS3/E3 frame) ds3ReceiveResetCode receiving a loopback deactivation request ds3ReceiveDS1LoopCode receiving a request to loopback a particular DS1/E1 within a DS3/E3 frame ds3ReceiveTestPattern receiving a test pattern.')
ds3LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds3NoLoop", 1), ("ds3CellLoop", 2), ("ds3PayloadLoop", 3), ("ds3DiagLoop", 4), ("ds3LineLoop", 5), ("ds3OtherLoop", 6))).clone('ds3NoLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LoopbackConfig.setStatus('current')
if mibBuilder.loadTexts: ds3LoopbackConfig.setDescription("This variable represents the loopback configuration of the DS3 interface. This variable is defined in the rfc1407 configuration table as dsx3LoopbackConfig, with slightly different values. ds3NoLoop (1) means that the interface is not in a loopback state. ds3CellLoop (2) means that cells that are processed by the receiving component are not written into the receive FIFO, but into the transmit FIFO for retransmission. ds3PayloadLoop (3) means that the receive signal is looped back for retransmission after it has passed through the port's reframing function. ds3DiagLoop (4) means that the transmit data stream is looped back to the receiver. ds3LineLoop (5) is only supported on series B and later netmods. ds3OtherLoop (6) means that the interface is in a loopback that is not defined here.")
ds3TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rxTiming", 1), ("localTiming", 2))).clone('localTiming')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3TxClockSource.setStatus('current')
if mibBuilder.loadTexts: ds3TxClockSource.setDescription('The source of the transmit clock.')
ds3RxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("descrambling", 1), ("noDescrambling", 2))).clone('noDescrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3RxScrambling.setStatus('current')
if mibBuilder.loadTexts: ds3RxScrambling.setDescription('This variable indicates whether the information is being descrambled on receiving. It should be set the same as the transmitting side.')
ds3TxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2))).clone('noScrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3TxScrambling.setStatus('current')
if mibBuilder.loadTexts: ds3TxScrambling.setDescription('This variable indicates whether the information (48 octet payload) is being scrambled before transmitting. It should be set the same as the receiving side.')
ds3LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3LineStatus.setStatus('current')
if mibBuilder.loadTexts: ds3LineStatus.setDescription('This variable indicates the Line Status of the interface. A similar object is defined in the rfc1407 configuration table as dsx3LineStatus (the ds3RxFERF bit is not defined in rfc1407) . The variable contains loopback state information and failure state information. It is a bit map represented as a sum. The ds3NoAlarm should be set if and only if no other flag is set. The various bit positions are: 1 No Alarm. 2 Receiving PLCP Yellow Alarm Indication. 4 Transmitting PLCP Yellow alarm indication. 8 Receiving PLCP LOF. 16 Receiving FERF. 32 Transmiting FERF. 64 Receiving AIS failure indication. 128 Receiving LOF failure indication. 256 Receiving LOS failure indication. 512 Loopback State. 1024 Receiving a test pattern. 2048 Other failures. 16384 Receiving IDLE failure indication. 32768 Receiving LCD failure indication.')
ds3IdleUnassignedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3IdleUnassignedCells.setStatus('current')
if mibBuilder.loadTexts: ds3IdleUnassignedCells.setDescription("This variable indicates the types of cells that should be sent in case there is no real data to send. According to the ATM Forum, Unassigned cells should be sent (octet 1-3 are 0's, octet 4 is 0000xxx0, where x is 'don't care'). According to the CCITT specifications, Idle cells should be sent (everything is '0' except for the CLP bit which is '1'). By default, unassigned cells are transmitted is case there is no data to send.")
ds3LineTypeFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3Hcs", 1), ("ds3Plcp", 2))).clone('ds3Hcs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LineTypeFraming.setStatus('current')
if mibBuilder.loadTexts: ds3LineTypeFraming.setDescription('This variable indicates the way ATM cells are constructed from the DS3 stream. ds3Hcs(1) indicates that the ATM cells are constructed upon the Header Check Sequence (HCS) inside the ATM cell header. ds3Plcp(2) indicates that the ATM cells are constructed from the DS3 PLCP (Physical Layer Convergence Protocol) bits.')
ds3LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3LineLt225", 1), ("ds3LineGt225", 2))).clone('ds3LineGt225')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LineLength.setStatus('current')
if mibBuilder.loadTexts: ds3LineLength.setDescription('This variable represents the length of the physical cable connected to the ds3 port. The user has to set this object to match the physical cable in order to get the netmod to receive the signal on the cable. The different values are: ds3LineLt225 (1) means the line is shorter than 225 ft, ds1LineGt225 (2) means the line length is greater than 220 ft. This value is not settable for Series A netmods and the value for these netmods is Gt225')
ds3PbitPErrThrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 16), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PbitPErrThrSeconds.setStatus('current')
if mibBuilder.loadTexts: ds3PbitPErrThrSeconds.setDescription('This variable represents the consecutive number of BAD/GOOD seconds to detect/clear an Excessive P-bit Parity Error Defect. The range of values it can take is between 2 and 10 inclusive.')
ds3PbitPErrThrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PbitPErrThrErrors.setStatus('current')
if mibBuilder.loadTexts: ds3PbitPErrThrErrors.setDescription('This variable is a threshold for the number of P-bit Parity Errors per second and is used as a parameter to the Excessive P-bit Parity Error Defect. If the number of errors exceeds the threshold, the particular second is declared BAD, otherwise it is declared GOOD.')
ds3PbitPErrFailEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PbitPErrFailEnable.setStatus('current')
if mibBuilder.loadTexts: ds3PbitPErrFailEnable.setDescription("This variable controls whether declaration of an Excessive P-bit Parity Error Defect forces the port's operState to Down.")
ds3SigFailBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3SigFailBer.setStatus('current')
if mibBuilder.loadTexts: ds3SigFailBer.setDescription('This is the exponent of 10 for the current signal fail bit error rate (BER) threshold for this port. The value -4, for example, represents a BER of 1E-4. This variable is only applicable when ds3BerErrorModel is set to errorModelRandom.')
ds3SigDegradeBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3SigDegradeBer.setStatus('current')
if mibBuilder.loadTexts: ds3SigDegradeBer.setDescription('This is the exponent of 10 for the current signal degrade bit error rate (BER) threshold for this port. The value -8, for example, represents a BER of 1E-8. This variable is only applicable when ds3BerErrorModel is set to errorModelRandom.')
ds3BerErrorModel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("errorModelNone", 0), ("errorModelRandom", 1), ("errorModelBurst", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3BerErrorModel.setStatus('current')
if mibBuilder.loadTexts: ds3BerErrorModel.setDescription('This is the error distribution model to be used to identify signal degrade and signal fail conditions. errorModelRandom selects a random error distribution and declares signal conditions based on the thresholds set in ds3SigDegradeBer and ds3SigFailBer. errorModelBurst selects a burst error model and declares signal degrade conditions based on the thresholds set in ds3PErrThrSeconds and ds1PErrThrErrors. errorModelNone disables detection of signal conditions.')
ds3BerState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("berStateOk", 0), ("berStateSigDegrade", 1), ("berStateSigFail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3BerState.setStatus('current')
if mibBuilder.loadTexts: ds3BerState.setDescription('This value describes the current state of the port as determined through bit error rate analysis.')
ds3FramingTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1), )
if mibBuilder.loadTexts: ds3FramingTable.setStatus('current')
if mibBuilder.loadTexts: ds3FramingTable.setDescription('A table of DS3 framing statistics information.')
ds3FramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1), ).setIndexNames((0, "Fore-DS3-MIB", "ds3FramingBoard"), (0, "Fore-DS3-MIB", "ds3FramingModule"), (0, "Fore-DS3-MIB", "ds3FramingPort"))
if mibBuilder.loadTexts: ds3FramingEntry.setStatus('current')
if mibBuilder.loadTexts: ds3FramingEntry.setDescription('A table entry containing DS3 framing statistics information.')
ds3FramingBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingBoard.setStatus('current')
if mibBuilder.loadTexts: ds3FramingBoard.setDescription("The index of this port's switch board.")
ds3FramingModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingModule.setStatus('current')
if mibBuilder.loadTexts: ds3FramingModule.setDescription('The network module of this port.')
ds3FramingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingPort.setStatus('current')
if mibBuilder.loadTexts: ds3FramingPort.setDescription('The number of this port.')
ds3FramingLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingLOSs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingLOSs.setDescription('The number of seconds in which Loss Of Signal (LOS) errors were detected by the DS3 Receive Framer block.')
ds3FramingLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingLCVs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingLCVs.setDescription('The number of Line Code Violations (LCV) that were detected by the DS3 Receive Framer block.')
ds3FramingSumLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingSumLCVs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingSumLCVs.setDescription('The number of DS3 information blocks (85 bits) which contain one or more Line Code Violations (LCV).')
ds3FramingFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingFERRs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingFERRs.setDescription('Number of DS3 framing error (FERR) events.')
ds3FramingOOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingOOFs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingOOFs.setDescription('Number of seconds DS3 Out Of Frame (OOF) error events were experienced.')
ds3FramingFERFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingFERFs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingFERFs.setDescription('The number of seconds in which Far End Receive Failure (FERF) state has been detected by the DS3 Receive Framer block. FERF signal alerts the upstream terminal that a failure has been detected along the downstream line.')
ds3FramingAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingAISs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingAISs.setDescription('The number of seconds in which Alarm Indication Signals (AIS) were detected by the DS3 Receive Framer block. AIS indicates that an upstream failure has been detected by the far end.')
ds3FramingPbitPERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingPbitPERRs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingPbitPERRs.setDescription('Number of P-bit parity error (PERR) events.')
ds3FramingCbitPERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingCbitPERRs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingCbitPERRs.setDescription('Number of C-bit parity error (PERR) events.')
ds3FramingFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingFEBEs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingFEBEs.setDescription('Number of DS3 far end block error (FEBE) events.')
ds3FramingIDLEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FramingIDLEs.setStatus('current')
if mibBuilder.loadTexts: ds3FramingIDLEs.setDescription('The number of seconds in which IDLE signal was detected by the DS3 Receive Framer block.')
ds3PlcpTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2), )
if mibBuilder.loadTexts: ds3PlcpTable.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpTable.setDescription('A table of DS3 Physical Layer Convergence Protocol (Procedure) statistics information.')
ds3PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1), ).setIndexNames((0, "Fore-DS3-MIB", "ds3PlcpBoard"), (0, "Fore-DS3-MIB", "ds3PlcpModule"), (0, "Fore-DS3-MIB", "ds3PlcpPort"))
if mibBuilder.loadTexts: ds3PlcpEntry.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpEntry.setDescription('A table entry containing DS3 PLCP statistics information.')
ds3PlcpBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpBoard.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpBoard.setDescription("The index of this port's switch board.")
ds3PlcpModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpModule.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpModule.setDescription('The network module of this port.')
ds3PlcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpPort.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpPort.setDescription('The number of this port.')
ds3PlcpFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpFERRs.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpFERRs.setDescription('Number of Physical Layer Convergence Protocol (PLCP) octet error events.')
ds3PlcpLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpLOFs.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpLOFs.setDescription('The number of seconds in which Loss Of Frame (LOF) errors were detected by the PLCP (Physical Layer Convergence Protocol) receiver. LOF is declared when an Out-Of-Frame state persists for more than 1ms. LOF is removed when in-frame state persists for more than 12ms.')
ds3PlcpBIP8s = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpBIP8s.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpBIP8s.setDescription('Number of BIP-8 (Bit Interleaved Parity - 8) error events. The BIP-8 is calculated over the Path Overhead field and the associated ATM cell of the previous frame. A BIP-N is a method of error monitoring. An N bit code is generated by the transmitting equipment in such a manner that the first bit of the code provides even parity over the first bit of all N-bit sequences in the previous VT SPE, the second bit provides even parity over the second bits of all N-bit sequences within the specified portion, etc.')
ds3PlcpFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpFEBEs.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpFEBEs.setDescription('Number of ATM Far End Block Error (FEBE) events.')
ds3PlcpYellows = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PlcpYellows.setStatus('current')
if mibBuilder.loadTexts: ds3PlcpYellows.setDescription('The number of seconds in which Yellow alarm errors were detected by the PLCP (Physical Layer Convergence Protocol) receiver. Yellow alarm is asserted when 10 consecutive yellow signal bits are set to logical 1. Yellow signals are used to alert upstream terminals of a downstream failure in order to initiate trunk conditioning on the failure circuit.')
ds3AtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3), )
if mibBuilder.loadTexts: ds3AtmTable.setStatus('current')
if mibBuilder.loadTexts: ds3AtmTable.setDescription('A table of DS3 ATM statistics information.')
ds3AtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1), ).setIndexNames((0, "Fore-DS3-MIB", "ds3AtmBoard"), (0, "Fore-DS3-MIB", "ds3AtmModule"), (0, "Fore-DS3-MIB", "ds3AtmPort"))
if mibBuilder.loadTexts: ds3AtmEntry.setStatus('current')
if mibBuilder.loadTexts: ds3AtmEntry.setDescription('A table entry containing DS3 ATM statistics information.')
ds3AtmBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmBoard.setStatus('current')
if mibBuilder.loadTexts: ds3AtmBoard.setDescription("The index of this port's switch board.")
ds3AtmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmModule.setStatus('current')
if mibBuilder.loadTexts: ds3AtmModule.setDescription('The network module of this port.')
ds3AtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmPort.setStatus('current')
if mibBuilder.loadTexts: ds3AtmPort.setDescription('The number of this port.')
ds3AtmHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmHCSs.setStatus('current')
if mibBuilder.loadTexts: ds3AtmHCSs.setDescription('Number of header check sequence (HCS) error events. The HCS is a CRC-8 calculation over the first 4 octets of the ATM cell header.')
ds3AtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmRxCells.setStatus('current')
if mibBuilder.loadTexts: ds3AtmRxCells.setDescription('Number of ATM cells that were received.')
ds3AtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmTxCells.setStatus('current')
if mibBuilder.loadTexts: ds3AtmTxCells.setDescription('Number of non-null ATM cells that were transmitted.')
ds3AtmLCDs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AtmLCDs.setStatus('current')
if mibBuilder.loadTexts: ds3AtmLCDs.setDescription('The number of seconds in which Loss of Cell Delineation (LCD) has occurred. An LCD defect is detected when an out of cell delination state has persisted for 4ms. An LCD defect is cleared when the sync state has been maintained for 4ms.')
mibBuilder.exportSymbols("Fore-DS3-MIB", ds3ConfGroup=ds3ConfGroup, ds3FramingLOSs=ds3FramingLOSs, ds3AtmHCSs=ds3AtmHCSs, ds3AtmLCDs=ds3AtmLCDs, ds3PlcpFEBEs=ds3PlcpFEBEs, ds3StatsGroup=ds3StatsGroup, ds3PlcpLOFs=ds3PlcpLOFs, ds3SigDegradeBer=ds3SigDegradeBer, ds3FramingFEBEs=ds3FramingFEBEs, ds3FramingBoard=ds3FramingBoard, PYSNMP_MODULE_ID=foreDs3, ds3FramingPbitPERRs=ds3FramingPbitPERRs, ds3FramingCbitPERRs=ds3FramingCbitPERRs, ds3PbitPErrThrErrors=ds3PbitPErrThrErrors, ds3FramingFERRs=ds3FramingFERRs, ds3PlcpBIP8s=ds3PlcpBIP8s, ds3FramingModule=ds3FramingModule, ds3FramingSumLCVs=ds3FramingSumLCVs, ds3RxScrambling=ds3RxScrambling, ds3AtmPort=ds3AtmPort, ds3AtmEntry=ds3AtmEntry, ds3AtmRxCells=ds3AtmRxCells, ds3AtmTable=ds3AtmTable, ds3ConfEntry=ds3ConfEntry, ds3PbitPErrThrSeconds=ds3PbitPErrThrSeconds, ds3BerErrorModel=ds3BerErrorModel, ds3PlcpModule=ds3PlcpModule, foreDs3=foreDs3, ds3PlcpYellows=ds3PlcpYellows, ds3AtmTxCells=ds3AtmTxCells, ds3PlcpPort=ds3PlcpPort, ds3ConfTable=ds3ConfTable, ds3LineType=ds3LineType, ds3ConfBoard=ds3ConfBoard, ds3SendCode=ds3SendCode, ds3PlcpBoard=ds3PlcpBoard, ds3FramingLCVs=ds3FramingLCVs, ds3AtmModule=ds3AtmModule, ds3LineLength=ds3LineLength, ds3ConfModule=ds3ConfModule, ds3PlcpFERRs=ds3PlcpFERRs, ds3AtmBoard=ds3AtmBoard, ds3FramingEntry=ds3FramingEntry, ds3TxScrambling=ds3TxScrambling, ds3LineTypeFraming=ds3LineTypeFraming, ds3LoopbackConfig=ds3LoopbackConfig, ds3FramingOOFs=ds3FramingOOFs, ds3BerState=ds3BerState, ds3LineStatus=ds3LineStatus, ds3ConfPort=ds3ConfPort, ds3PbitPErrFailEnable=ds3PbitPErrFailEnable, ds3FramingPort=ds3FramingPort, ds3PlcpTable=ds3PlcpTable, ds3PlcpEntry=ds3PlcpEntry, ds3FramingTable=ds3FramingTable, ds3LineCoding=ds3LineCoding, ds3TxClockSource=ds3TxClockSource, ds3ReceiveCode=ds3ReceiveCode, ds3FramingAISs=ds3FramingAISs, ds3FramingFERFs=ds3FramingFERFs, ds3FramingIDLEs=ds3FramingIDLEs, ds3SigFailBer=ds3SigFailBer, ds3IdleUnassignedCells=ds3IdleUnassignedCells)
