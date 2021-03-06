#
# PySNMP MIB module CXGIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXGIM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
SapIndex, cxGim, Alias, ThruputClass = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "cxGim", "Alias", "ThruputClass")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, NotificationType, Counter32, iso, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "iso", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PSapIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TypeIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class DteIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class SubRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PacketSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("bytes16", 4), ("bytes32", 5), ("bytes64", 6), ("bytes128", 7), ("bytes256", 8), ("bytes512", 9), ("bytes1024", 10), ("bytes2048", 11), ("bytes4096", 12))

gimSysRouteConnectInterval = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 900)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSysRouteConnectInterval.setStatus('mandatory')
if mibBuilder.loadTexts: gimSysRouteConnectInterval.setDescription('Determines the number of seconds between attempts to establish a connection for a X25 system route. A connection is attempted only for defined non-connected routes. Range of Values: 10 - 900 seconds Default Value: 30 seconds Configuration Changed: administrative and operative')
gimMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimMibLevel.setStatus('mandatory')
if mibBuilder.loadTexts: gimMibLevel.setDescription('Used to determine current MIB module release supported by the agent. Object is in decimal.')
gimSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10), )
if mibBuilder.loadTexts: gimSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTable.setDescription('A table containing configuration information about each X25 convergence service access point. Service access points of this type exist at the upper interface of the X25 Convergence layer, and are used to communicate with the X25 or IAM layers.')
gimSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1), ).setIndexNames((0, "CXGIM-MIB", "gimSapType"), (0, "CXGIM-MIB", "gimSapNumber"))
if mibBuilder.loadTexts: gimSapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapEntry.setDescription('Defines a row in the Service Access Point Configuration table. Each row contains the objects which are used to define a service access point upper interface of the X25 Convergence layer.')
gimSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 1), TypeIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapType.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapType.setDescription('Identifies the type of this SAP (service access point) with a numerical value. Values are unique for each type.')
gimSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 2), PSapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapNumber.setDescription('Identifies this SAP (service access point) with a numerical value. Values are unique for each service access point.')
gimSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRowStatus.setDescription('Determines the status of the objects in a table row. Options: invalid (1): Row is deleted from the table immediately, however values are still in effect until the next reset. valid (2): Use this value to add a new row to the table, or modify an existing row. Default Value: valid (2) Configuration Changed: administrative')
gimSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapAlias.setDescription('Identifies this service access point by a textual name. Names must be unique across all service access points at all layers. Range of Values: 1 -16 alphanumeric characters (first character must be a letter) Default Value: none Configuration Changed: administrative')
gimSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapCompanionAlias.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapCompanionAlias.setDescription('Determines the name which uniquely identifies the X.25 Upper SAP (service access point) which will communicate with this SAP. Range of Values: 1 -16 alphanumeric characters (first character must be a letter) Default Value: none Configuration Changed: administrative')
gimSapInactivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapInactivityTimer.setReference('RFC 1356 Section 3.9')
if mibBuilder.loadTexts: gimSapInactivityTimer.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapInactivityTimer.setDescription('Defines the time of inactivity, in seconds, after which the SAP (service access point) will send a disconnect request to the X25 layer. The timer starts whenever data is received from the X25 layer or the IAM layer. Range of Values: 0 to 3600 Note: A value of 0 means that the timer is disabled. The circuit is permanently open. Default Value: 90 Configuration Changed: Operative ')
gimSapProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 11)).clone('01,00,00,00')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapProtocolId.setReference('CCITT X.28 3.1.3, X.29 4.2, RFC 1356 3.2')
if mibBuilder.loadTexts: gimSapProtocolId.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapProtocolId.setDescription('Defines the protocol format that is used for incoming call or call request packets to the X.25 call data field. The field consists of 4 hexadecimal octets where the first octet is coded as follows: ASYNC PAD bits 8 & 7 - 00 for CCITT use - 01 for national use - 10 reserved for international user bodies - 11 for DTE-DTE use When bits 8 & 7 are equal to 00, bits 6 to 1 will be equal to 000001. The first octet is shown as 01, 00, 00, 00. The first 0 in each number is optional and may be shown as 1, 0, 0, 0. IP over X.25 The value hex CC is required for IP. All bits of octets 2, 3 and 4 are set to 0. They are reserved as a future mechanism for providing the called PAD or packet mode DTE (user) with additional information pertaining to the calling party. A value of 00,00,00,00 will disable the protocol id formatting for x.25 call request packet or validation for incoming call. Default Value: 01,00,00,00 Configuration Changed: Operative ')
gimSapAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapAddress.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapAddress.setDescription('Defines the calling address for this SAP (service access point). Range of Values: 1 to 15 digits Default Value: 0 Configuration Changed: Operative ')
gimSapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: gimSapControl.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapControl.setDescription('Permits control of a specific SAP (service access point). Options: clearStats (1): Clear all statistics stored by statistics objects. Configuration Changed: operative')
gimSapState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("offLine", 1), ("unbound", 2), ("notConnected", 3), ("inProgress", 4), ("connected", 5))).clone('unbound')).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapState.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapState.setDescription('Indicates the current state of this SAP (service access point). Options: offLine (1): Indicates a newly created service access point whose configuration has not yet been sent to the X25 Convergence layer. unbound (2): SAP is not yet bound to its companion SAP at an upper layer. notConnected (3): The associated route with this SAP is not connected, or there is no route associated with this SAP. inProgress (4): The associated route is in the process of connecting. connected (5): The associated route is connected.')
gimSapLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConnected", 1), ("inProgress", 2), ("connected", 3))).clone('notConnected')).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapLinkState.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapLinkState.setDescription('Indicates the current state of the x25 link for this SAP (service access point). Options: notConnected (1): There is no x25 circuit established associated with this SAP. inProgress (2): The associated x25 call is in the process of being established. connected (3): The associated x25 call is established.')
gimSapTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapTxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxFrames.setDescription('Indicates the number of frames transmitted by this service access point.')
gimSapRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapRxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxFrames.setDescription('Indicates the number of frames received by this service access point.')
gimSapTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapTxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxOctets.setDescription('Indicates the number of octets transmitted by this service access point.')
gimSapRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapRxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxOctets.setDescription('Indicates the number of octets received by this service access point.')
gimSapOutSuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapOutSuccessfullConnects.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapOutSuccessfullConnects.setDescription('Indicates the number of successful outgoing connections established by this SAP (service access point). An outgoing connection is always attempted from X25 convergence to the Inter-Application Module (IAM). At the PSAP, this object represents the total number of outgoing connections established by all SAPs. At each individual SAP, this object represents the number of outgoing connections established by only that SAP.')
gimSapOutUnsuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapOutUnsuccessfullConnects.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapOutUnsuccessfullConnects.setDescription('Indicates the number of unsuccessful outgoing connections attempted by this SAP (service access point). An outgoing connection is always attempted from X25 convergence to the Inter-Application Module (IAM). At the PSAP, this object represents the total number of unsuccessful outgoing connections attempted by all SAPs. At each individual SAP, this object represents the number of unsuccessful outgoing connections attempted by only that SAP.')
gimSapInSuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapInSuccessfullConnects.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapInSuccessfullConnects.setDescription('Indicates the number of successful incoming connections established at this SAP (service access point). An incoming connection is always attempted from the Inter-Application Module (IAM) to X25 convergence. At the PSAP, this object represents the total number of successful incoming connections for all SAPs. At each individual SAP, this object represents the number of successful incoming connections for only that SAP.')
gimSapInUnsuccessfullConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapInUnsuccessfullConnects.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapInUnsuccessfullConnects.setDescription('Indicates the number of unsuccessful incoming connections attempted at this SAP (service access point). An incoming connection is always attempted from the Inter-Application Module (IAM) to X25 convergence. At the PSAP, this object represents the total number of unsuccessful incoming connections for all SAPs. At each individual SAP, this object represents the number of unsuccessful incoming connections for only that SAP.')
gimSapUnopenedServiceDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapUnopenedServiceDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapUnopenedServiceDiscards.setDescription('This object applies only to the PSAP (public service access point). Indicates the number of frames received and discarded by the PSAP because: - no route was associated with the frame - the frame was destined for a route that is not connected')
gimSapTxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapTxResets.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxResets.setDescription('This object applies only to the PSAP (public service access point). Indicates the number of Inter- Application Module (IAM) reset frames sent by the PSAP.')
gimSapRxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSapRxResets.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxResets.setDescription('This object applies only to the PSAP. Indicates the number of Inter- Application Module (IAM) reset frames received by the PSAP.')
gimSapRxThruputClass = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 50), ThruputClass().clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapRxThruputClass.setReference('CCITT(1988) Section 7.2.2.2 and Table 30/X.25')
if mibBuilder.loadTexts: gimSapRxThruputClass.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxThruputClass.setDescription('Defines the default receive throughput class that is used at this SAP (service access point). Range of Values: 75 - 64000 bps Default Value: 9600 bps Configuration Changed: Operative ')
gimSapTxThruputClass = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 51), ThruputClass().clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapTxThruputClass.setReference('CCITT(1988) Section 7.2.2.2 and Table 30/X.25')
if mibBuilder.loadTexts: gimSapTxThruputClass.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxThruputClass.setDescription('Defines the default transmit throughput class that is used at this SAP (service access point). Range of Values: 75 to 64000 bps Default Value: 9600 bps Configuration Changed: Operative ')
gimSapTxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 52), PacketSize().clone('bytes128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapTxPacketSize.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxPacketSize.setDescription('Defines the size of the transmit packet for the Xim layer. Range of Values: 16 to 4096 bytes Default Value: 128 bytes Configuration Changed: Operative ')
gimSapRxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 53), PacketSize().clone('bytes128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapRxPacketSize.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxPacketSize.setDescription('Defines the size of the receive packet for the Xim layer. Range of Values: 16 to 4096 bytes Default Value: 128 bytes Configuration Changed: Operative ')
gimSapTxWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 54), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapTxWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapTxWindowSize.setDescription('Defines the size of the transmit window for the Xim layer. Range of Values: 1 to 127 Default Value: 2 Configuration Changed: Operative ')
gimSapRxWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 55), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSapRxWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: gimSapRxWindowSize.setDescription('Defines the size of the receive window for the Xim layer. Range of Values: 1 to 127 Default Value: 2 Configuration Changed: Operative ')
gimSysRouteTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11), )
if mibBuilder.loadTexts: gimSysRouteTable.setStatus('mandatory')
if mibBuilder.loadTexts: gimSysRouteTable.setDescription('A table containing information about each X25 system route. Routes allow this X25 layer to link with another X25 layer across a frame relay network, or with the X25 layer on another similar card in the same chassis (for future use with the CX1000).')
gimSysRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1), ).setIndexNames((0, "CXGIM-MIB", "gimSRSapType"), (0, "CXGIM-MIB", "gimSRSapNumber"))
if mibBuilder.loadTexts: gimSysRouteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: gimSysRouteEntry.setDescription('Defines a row in the gimSysRouteTable. Each row contains the objects which define a system route.')
gimSRSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 1), TypeIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSRSapType.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRSapType.setDescription('Identifies the type of service access point this route entry is associated with.')
gimSRSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 2), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSRSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRSapNumber.setDescription('Identifies the service access point this route entry is associated with.')
gimSRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSRRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRRowStatus.setDescription('Determines the status of the objects in a table row. Options: invalid (1): Row is deleted from the table immediately, however values are still in effect until the next reset. valid (2): Use this value to add a new row to the table, or modify an existing row. Default Value: none Configuration Changed: administrative and operative')
gimSRDestAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSRDestAlias.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRDestAlias.setDescription('Determines the textual name of the destination service this route connects to. When attempting a X25 connection across Frame Relay, this object specifies the name of the outgoing circuit at the Frame Relay layer. When attempting a X25 connection between cards within the same chassis (future use within CX1000), this object specifies the name of the X25 Convergence SAP on the remote card. Range of Values: 1 -16 characters (first character must be a letter) Default Value: none Configuration Changed: administrative and operative')
gimSRSubRef = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 5), SubRef()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gimSRSubRef.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRSubRef.setDescription('Specifies a reference number that uniquely identifies this route. This number is used by the FRIM (Frame Relay Interface Module) to identify routes using the same DLCI (enables PVC consolidation). This number must be unique for all routes sharing the same DLCI. Range of Values: 1 - 255 (when using PVC consolidation) 0 (when not using PVC consolidation) Default Value: 0 Configuration Changed: administrative and operative')
gimSRRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("offLine", 1), ("notConnected", 2), ("inProgress", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSRRouteStatus.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRRouteStatus.setDescription('Indicates the connection status of this X25 route. Options: offLine (1): Indicates that the X25 Convergence SAP this route is associated with does not exist or is offline. notConnected (2): Indicates that the remote destination does not exist, or has refused the connection. inProgress (3): Indicates that the connection is in the process of being established. This is a transient state. connected (4): Indicates that the connection is established and is ready for data transfer.')
gimSRClearStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("noFailure", 1), ("internalError", 2), ("localAllocFailure", 3), ("remoteAllocFailure", 4), ("localNoAccess", 5), ("remoteNoAccess", 6), ("localPvcDown", 7), ("remotePvcDown", 8), ("localPvcBusy", 9), ("remotePvcBusy", 10), ("localFcnFailure", 11), ("remoteFcnFailure", 12), ("localDsnFailure", 13), ("localRefInUse", 14), ("remoteAliasNotFound", 15), ("remoteNoPvcService", 16), ("mpeInvalidSubref", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gimSRClearStatus.setStatus('mandatory')
if mibBuilder.loadTexts: gimSRClearStatus.setDescription("Indicates the status of a failed connection. The value of this object is only valid only between attempts to establish the route connection (gimSRRouteStatus = notConnected), and may or may not change after successive failed attempts. Options: noFailure (1): Once a system route has been successfully connected, this value is maintained for the duration of the connection. internalError (2): An internal error has occurred. localAllocFailure (3): There is insufficient memory available for X25 Convergence to establish this connection. remoteAllocFailure (4): There is insufficient memory available for the destination protocol layer to establish this connection. localNoAccess (5): This route is associated with a SAP that does not exist. remoteNoAccess (6): This route is associated with a SAP that does not exist at the destination layer. localPvcDown (7): For future use. remotePvcDown (8): The PVC at the destination protocol layer is down. localPvcBusy (9): The SAP associated with this route is already connected. remotePvcBusy (10): The destination associated with this route is already connected. This typically occurs when the route is a non-MPE (PVC consolidating) circuit. localFcnFailure (11): Flow control negotiation failed. remoteFcnFailure (12): Flow control negotiation failed at the destination protocol layer. localDsnFailure (13): Data size negotiation failed. localRefInUse (14): Data size negotiation failed at the destination protocol layer. remoteAliasNotFound (15): The destination alias (gimSRDestAlias) does not exist. remoteNoPvcService (16): The destination protocol layer does not support PVC service. mpeInvalidSubref (17): The value of gimSRSubRef is invalid at the destination protocol layer. (i.e., lapcnvSRSubRef is set to '0' and the destination frame relay circuit is configured for PVC consolidation).")
ximDteTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12), )
if mibBuilder.loadTexts: ximDteTable.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteTable.setDescription("A table containing the DTE X.28 Selection command objects for each defined 'abbreviated address'.")
ximDteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1), ).setIndexNames((0, "CXGIM-MIB", "ximDteSapNumber"), (0, "CXGIM-MIB", "ximDteDteNumber"))
if mibBuilder.loadTexts: ximDteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteEntry.setDescription('The objects for a specific DTE X.28 Selection entry.')
ximDteSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ximDteSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteSapNumber.setDescription("Associates the DTE entries defined by the object 'ximDteDteNumber' with an xim sap number.")
ximDteDteNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 2), DteIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ximDteDteNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteDteNumber.setDescription("Associates this DTE entry with the xim sap number defined by the object 'ximDteSapNumber', Currently the XIM will support ONLY one entry. ")
ximDteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ximDteRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteRowStatus.setDescription("Indicates whether this specific entry is configured within the MIB. Entries (rows) may be created by setting this object value to 'valid', or deleted by changing this object value to 'invalid'.")
ximDteCalledAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ximDteCalledAddress.setReference('CCITT X.28 3.5.15.2.1, CCiTT X.25, CCITT X.121')
if mibBuilder.loadTexts: ximDteCalledAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteCalledAddress.setDescription('Defines the network address of a remote device for this DTE entry. Allowable values: 1 to 15 numerical digits. ')
ximDteFacilityField = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ximDteFacilityField.setReference('CCITT X.28 3.5.15.1')
if mibBuilder.loadTexts: ximDteFacilityField.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteFacilityField.setDescription("Defines the facility codes and parameters requires for the X.28 Selection command for this DTE entry. The facility codes and parameters must be entered as defined in the CCITT X.28 Recommendation. The following facilities are supported: - Reverse charge ('R') A value of null string (blank) means no facilities. ")
ximDteUserDataField = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ximDteUserDataField.setReference('CCITT X.28 3.5.15.3')
if mibBuilder.loadTexts: ximDteUserDataField.setStatus('mandatory')
if mibBuilder.loadTexts: ximDteUserDataField.setDescription('Defines the user data field of the X.28 Selection command for this DTE entry. A value of nul string (blank) means no user data. ')
mibBuilder.exportSymbols("CXGIM-MIB", SubRef=SubRef, gimSRDestAlias=gimSRDestAlias, gimSapInSuccessfullConnects=gimSapInSuccessfullConnects, ximDteUserDataField=ximDteUserDataField, gimSRRouteStatus=gimSRRouteStatus, gimSRRowStatus=gimSRRowStatus, gimSapInactivityTimer=gimSapInactivityTimer, gimSapTxPacketSize=gimSapTxPacketSize, ximDteFacilityField=ximDteFacilityField, gimSapOutUnsuccessfullConnects=gimSapOutUnsuccessfullConnects, gimSapAlias=gimSapAlias, gimSapControl=gimSapControl, gimSapOutSuccessfullConnects=gimSapOutSuccessfullConnects, gimSysRouteEntry=gimSysRouteEntry, PacketSize=PacketSize, gimSapLinkState=gimSapLinkState, gimSapNumber=gimSapNumber, gimSapRxThruputClass=gimSapRxThruputClass, gimSapTable=gimSapTable, DteIndex=DteIndex, ximDteTable=ximDteTable, gimSapCompanionAlias=gimSapCompanionAlias, gimSapRxResets=gimSapRxResets, gimSapTxOctets=gimSapTxOctets, gimSapUnopenedServiceDiscards=gimSapUnopenedServiceDiscards, gimSapTxThruputClass=gimSapTxThruputClass, gimSapType=gimSapType, gimSapProtocolId=gimSapProtocolId, gimSapInUnsuccessfullConnects=gimSapInUnsuccessfullConnects, gimSapTxFrames=gimSapTxFrames, ximDteEntry=ximDteEntry, gimSRSapNumber=gimSRSapNumber, ximDteCalledAddress=ximDteCalledAddress, PSapIndex=PSapIndex, gimSapTxResets=gimSapTxResets, gimSRSapType=gimSRSapType, ximDteRowStatus=ximDteRowStatus, gimSapRxOctets=gimSapRxOctets, gimSapRowStatus=gimSapRowStatus, gimSysRouteConnectInterval=gimSysRouteConnectInterval, gimSapState=gimSapState, ximDteDteNumber=ximDteDteNumber, gimMibLevel=gimMibLevel, gimSRClearStatus=gimSRClearStatus, gimSapRxWindowSize=gimSapRxWindowSize, TypeIndex=TypeIndex, gimSapTxWindowSize=gimSapTxWindowSize, gimSapAddress=gimSapAddress, gimSRSubRef=gimSRSubRef, ximDteSapNumber=ximDteSapNumber, gimSapEntry=gimSapEntry, gimSapRxPacketSize=gimSapRxPacketSize, gimSapRxFrames=gimSapRxFrames, gimSysRouteTable=gimSysRouteTable)
