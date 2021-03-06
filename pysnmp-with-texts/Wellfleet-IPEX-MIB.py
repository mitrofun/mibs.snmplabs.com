#
# PySNMP MIB module Wellfleet-IPEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IPEX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ObjectIdentity, IpAddress, Counter64, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Integer32, ModuleIdentity, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Integer32", "ModuleIdentity", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfIpexGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIpexGroup")
wfIpex = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1))
wfIpexDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexDelete.setDescription('Create/Delete parameter. Default is created. Users perform an SNMP SET operation on this object in order to create/delete IPEX.')
wfIpexDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform an SNMP SET operation on this object in order to enable/disable IPEX.')
wfIpexState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexState.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexState.setDescription('The current state of IPEX.')
wfIpexMaxMessageSize = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 4096)).clone(1600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMaxMessageSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMaxMessageSize.setDescription('The maximum client message size that IPEX accepts. The size is in bytes.')
wfIpexInsCalledDte = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexInsCalledDte.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexInsCalledDte.setDescription('Enable/Disable parameter. Default is disabled. Users perform an SNMP SET operation on this object in order to enable/disable the support for inserting Called DTE address.')
wfIpexInsCallingDte = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexInsCallingDte.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexInsCallingDte.setDescription('Enable/disable the support for transmitting the calling DTE address over TCP tunnel. This changes the IPEX control message header format and hence this attribute should be enabled (only for 11.02 or up) on both ends (local & remote routers) for proper operation. This attribute applies only to End_to_End mode.')
wfIpexTcpRequestLimit = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexTcpRequestLimit.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexTcpRequestLimit.setDescription('The maximum number of TCP requests IPEX can have pending with TCP. Any addition requests will be queued until the number of pending requests fall below the limit.')
wfIpexTcpRequestCheck = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexTcpRequestCheck.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexTcpRequestCheck.setDescription('When IPEX has queued TCP requests, the time period (in milliseconds) between checking if the number of pending TCP requests have fallen below wfIpexTcpRequestLimit.')
wfIpexSendResetRequestOnTCPUp = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 9), Integer32().clone(9)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexSendResetRequestOnTCPUp.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSendResetRequestOnTCPUp.setDescription('Default(cause code) is 0x09 and PVC_TCP sends out the Reset Request with the cause code = 0x09 and TCP_PVC Router does not send the Reset Request when TCP is up. If the value is changed from the default cause code(0x09) then IPEX Gateway will send out the Reset Request with this value when network is operational. TCP_PVC will also send the Reset Request with this cause code when TCP connection is up.')
wfIpexTranslateNetworkOutOfOrder = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 10), Integer32().clone(29)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexTranslateNetworkOutOfOrder.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexTranslateNetworkOutOfOrder.setDescription('Default is 0x1d(29): Network out of order. If the value is changed from the default cause code = 0x1d then the IPEX Gateway will send the Reset Request with cause code specified when the network is out of order.')
wfIpexTcpUseIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexTcpUseIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexTcpUseIpAddress.setDescription('Enable/Disable parameter. Default is disabled. If set to Enabled, the IP address used for a TCP connection will be the coresponding address for the circuit.')
wfIpexBobEnabled = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexBobEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexBobEnabled.setDescription('This attribute will indicate whether IPEX supports Bank Of Bahrain enhancement. If it is enabled, only calling DTE will be send in ASCII format in user defined area of message header, if header type is full.')
wfIpexBobTimeout = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000)).clone(15000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexBobTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexBobTimeout.setDescription('This attribute will indicate the timeout in milliseconds, after which DEVICE UP message is to be send to BOB mainserver from router, as long as this service supports BOB functionality.')
wfIpexMaxAuditIp = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 14), Integer32().clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMaxAuditIp.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMaxAuditIp.setDescription("Default is 25. Specify the maximum of IP address and TCP port pairs that IPEX Audit gate can hold in its internal table when IPEX PVC-TCP Gateway is in TCP Retry Mode. Audit gate puts new ip address and TCP port pair to the internal table when it tries TCP connection. IPEX Audit gate will be re-trying TCP connections until the table is filled up. Once it is full then it won't re-try new TCP connections. Setting zero causes IPEX audit gate to try TCP connections without examining the IP address and TCP port pairs had already tried out or not.")
wfIpexSessionInstanceIdOffsetForSvc = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexSessionInstanceIdOffsetForSvc.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionInstanceIdOffsetForSvc.setDescription('Default is 0. Specify the offset value for wfIpexSessionEntry when instances for SVC are created. For example, when it is set to 1023, instance ID for wfIpexSessionEntry for SVC connections will be wfIpexSessionEntry.*.3.1024 and the next one will be wfIpexSessionEntry.*.3.1025 and so on. This MIB object is introduced not to assign same instance ID to PVC and SVC when SVCs and PVCs are configured with single circuit. Because wfIpexSessionEntry for PVCs are based on the LCNs and the ones for SVCs are based on the order of each SVC being created, there would be the cases that same instance IDs are assigned to both SVC and PVC and it will cause the router to fault. It needs to be set to the value which is greater than the maximum LCN of the PVC connections when PVCs and SVCs co-exist on a single circuit.')
wfIpexMappingTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2), )
if mibBuilder.loadTexts: wfIpexMappingTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingTable.setDescription('A table which contains the list of mappings between TCP connections and X.25 connections. This is the configuration table in which each entry sets up the association between a TCP port number and a X.25 DTE address or connection. inst_id[] = wfIpexMappingSrcConnCct wfIpexMappingSrcConnType wfIpexMappingID')
wfIpexMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1), ).setIndexNames((0, "Wellfleet-IPEX-MIB", "wfIpexMappingSrcConnCct"), (0, "Wellfleet-IPEX-MIB", "wfIpexMappingSrcConnType"), (0, "Wellfleet-IPEX-MIB", "wfIpexMappingID1"), (0, "Wellfleet-IPEX-MIB", "wfIpexMappingID2"))
if mibBuilder.loadTexts: wfIpexMappingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingEntry.setDescription('An entry in wfIpexMappingTable.')
wfIpexMappingDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingDelete.setDescription('Create/Delete attribute. Default is created. Users perform an SNMP SET operation on this object in order to create/delete a translation mapping record.')
wfIpexMappingDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingDisable.setDescription('Enables or Disables this Mapping entry. Setting this attribute to DISABLED will disconnect all active Sessions pertaining to this Mapping entry')
wfIpexMappingSrcConnCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexMappingSrcConnCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingSrcConnCct.setDescription('The circuit from which the connection attempt is received that initiates a translation session.')
wfIpexMappingSrcConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))).clone(namedValues=NamedValues(("pvc", 1), ("svc", 2), ("dcesvc", 4), ("lapb", 8), ("tcp", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexMappingSrcConnType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingSrcConnType.setDescription('Defines the type of original connection attempt. Whether it is a PVC, SVC, DCE_SVC, LAPB or TCP')
wfIpexMappingID1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexMappingID1.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingID1.setDescription('The translation mapping identifier which identifies the remote connection of the translation session. This is an identifier that is available from the incoming connection attempt. The meaning of this object (wfIpexMappingID1) and the next object (wfIpexMappingID2) is dependent on the value of wfIpexMappingSrcConnType. SrcConnType ID1 ID2 --------------------------------------------------- pvc(1) LCN value 0 (Null) svc(2) 0 Called X.121 Address dcesvc(4) 0 0 (Null) lapb(8) 0 0 (Null) tcp(16) Port Number 0 (Null) ')
wfIpexMappingID2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexMappingID2.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingID2.setDescription('(See description for wfIpexMappingID1 above)')
wfIpexMappingDstConnCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingDstConnCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingDstConnCct.setDescription('The circuit from which the connection to the destination is to be established to set up a translation session.')
wfIpexMappingDstConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))).clone(namedValues=NamedValues(("pvc", 1), ("svc", 2), ("dcesvc", 4), ("lapb", 8), ("tcp", 16))).clone('pvc')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingDstConnType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingDstConnType.setDescription('Defines type of connection at the destination end. Whether it is a PVC, SVC, DCE_SVC, LAPB or TCP')
wfIpexMappingLocalDTEAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingLocalDTEAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingLocalDTEAddr.setDescription('The Local DTE address (identifies the X.121 address of the X.25 interface on the IPEX). This attribute is only used in the case of a SVC connection initiated from the IPEX to the terminal')
wfIpexMappingRemoteDTEAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingRemoteDTEAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingRemoteDTEAddr.setDescription('The Remote DTE address (identifies the X.121 address of the X.25 interface on the terminal). This attribute is only used in the case of a SVC connection initiated from the IPEX to the terminal')
wfIpexMappingPvcLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingPvcLcn.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingPvcLcn.setDescription('The LCN of the PVC connection from the IPEX to the terminal (identifies the channel to be used to reset the PVC connection. This attribute * is only used in the case of a PVC connection initiated from the IPEX to the terminal')
wfIpexMappingRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingRemoteIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingRemoteIpAddr.setDescription('The IP address of the remote host with which this translation session is established. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexMappingRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingRemoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingRemoteTcpPort.setDescription('The remote TCP port number in the host to be used to establish a TCP connection from the IPEX to the host server. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexMappingQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 8192)).clone(8192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingQueueSize.setDescription('The size of the IPEX queues used for transfering data between TCP and X.25. The size is in bytes.')
wfIpexMappingSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingSlotNumber.setDescription('The slot of the access (X.25 or LAPB) circuit on which the X.25 or LAPB connections will be established.')
wfIpexMappingCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local", 1), ("end2end", 2), ("gateway", 3))).clone('end2end')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingCtrlMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingCtrlMode.setDescription('Local mode configuration terminates X.25 at the router interface. The end2end mode configuration allows X.25 signalling and data to operate between two remote X.25 networks, using the router to translate both call control and data over a TCP/IP network. The gateway mode terminates X.25 at the router interface, but allows the user to configure 3 message header types at the TCP application layer. These header values are described in wfIpexMappingMsgHdrType.')
wfIpexMappingX25CUDF = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 17), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingX25CUDF.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingX25CUDF.setDescription('The X.25 Call User Data field (CUDF) in a X.25 Call Request packet header. This attribute is only used in the case of a SVC connection initiated from the IPEX to the terminal. It is used as the network layer protocol identifier of the X.25 connection.')
wfIpexMappingIdleTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingIdleTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingIdleTimer.setDescription('Idle session timeout period, in seconds. If an established TCP connection remains inactive for this interval, KEEPALIVE messages will be sent to the peer (if the Keepalive Timer is non-zero). Setting the Idle Timer to zero disables the keepalive feature.')
wfIpexMappingKeepaliveTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingKeepaliveTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingKeepaliveTimer.setDescription('KEEPALIVE retransmit timeout period, in seconds. This is the interval at which unacknowledged KEEPALIVE messages will be retransmitted. If the Idle Timer is set to zero, this timer ignored. If the Idle Timer is non-zero and this timer IS zero, no KEEPALIVEs are sent and the session is terminated upon expiration of the Idle Timer.')
wfIpexMappingKeepaliveRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingKeepaliveRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingKeepaliveRetries.setDescription('Number of unacknowledged KEEPALIVE messages retransmitted before the TCP session is terminated. If this count is set to zero, only one KEEPALIVE message will be sent.')
wfIpexMappingTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingTrace.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingTrace.setDescription('This object is a bitmask, setting the low order bit enables tracing of IPEX internal events. Setting other individual bit postions disable logging of internal IPEX events. Values may be added together to disable multiple message groups. Hex Dec Value Value Message/Event --------------------------------------------------------- 0x0001 1 Enable IPEX tracing. 0x0002 2 Data packets from IPEX to X.25. 0x0004 4 Data packets from X.25 to IPEX. 0x0008 8 Window updates from X.25. 0x0010 16 Data from TCP to IPEX. 0x0020 32 Window updates from TCP. 0x0040 64 Window requests from TCP.')
wfIpexMappingMsgHdrType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("short", 2), ("long", 3), ("full", 4))).clone('full')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingMsgHdrType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingMsgHdrType.setDescription('This attribute enables the Message Boundary Protocol. When enabled, this bit is used to mark the boundary of TCP application data that is consistent with Gateway Operation. The first three message header types are used only with wfIpexMappingCtlMode in gateway mode. The default value is used with wfIpexMappingCtlMode in the local or end2end mode of operation. NONE = Msg Boundary Protocol is off, no msg header. SHORT = Msg header condtains a 2-Byte length field. LONG = Msg header contains a 1-Byte type, 1-Byte version, and a 2-Byte length fields. FULL = Msg Header contains a 2-Byte length1 field, 1-Byte Version field, 1-Byte Type field and, a 1-Byte length2 field')
wfIpexMappingRemoteBackupIp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 23), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingRemoteBackupIp.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingRemoteBackupIp.setDescription('The IP address of the remote host with which this translation session is established. This attribute is only used in the case of a TCP connection with the primary remote IP address (wfIpexMappingRemoteIpAddr) failed.')
wfIpexMappingXlateCallingX121 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingXlateCallingX121.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingXlateCallingX121.setDescription('If this attribute is configured then insert this X.121 addr as the calling addr in the Call request pkt.')
wfIpexMappingTcpMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingTcpMaxRetry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingTcpMaxRetry.setDescription('The maximum number of attempts that PVC-TCP will make to re-establish the connection to the remote peer. The TCP Retry takes place every 15 seconds hence default setting will perform the TCP Retry forever.')
wfIpexMappingCfgLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 26), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingCfgLocalIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingCfgLocalIpAddr.setDescription('The IP address on the router to use as the source of the TCP session. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexMappingRemoteBackupTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpexMappingRemoteBackupTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexMappingRemoteBackupTcpPort.setDescription('The TCP port of the remote host with which this translation session is established. This attribute is only used in the case of a TCP connection with the primary remote IP address (wfIpexMappingRemoteIpAddr) failed.')
wfIpexSessionTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3), )
if mibBuilder.loadTexts: wfIpexSessionTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionTable.setDescription('A table that contains the information about the current active IPEX translation sessions. The status and statistics information related to each translation session is provided here. inst_id[] = wfIpexSessionIndex')
wfIpexSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1), ).setIndexNames((0, "Wellfleet-IPEX-MIB", "wfIpexSessionSrcConnCct"), (0, "Wellfleet-IPEX-MIB", "wfIpexSessionIndex"))
if mibBuilder.loadTexts: wfIpexSessionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionEntry.setDescription('An entry in wfIpexSession.')
wfIpexSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("x25up", 1), ("tcpup", 2), ("ccestab", 3), ("notconn", 4), ("lapbup", 5))).clone('notconn')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionState.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionState.setDescription('The IPEX state of this translation session. These are the steady states of the IPEX state machine. Transition states are not reflected.')
wfIpexSessionSrcConnCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionSrcConnCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionSrcConnCct.setDescription('The circuit from which the original connection attempt is received that initiated a translation session.')
wfIpexSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionIndex.setDescription('The index of this translation session')
wfIpexSessionSrcConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))).clone(namedValues=NamedValues(("pvc", 1), ("svc", 2), ("dcesvc", 4), ("lapb", 8), ("tcp", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionSrcConnType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionSrcConnType.setDescription('Defines type of original connection attempt. Whether it is a PVC, SVC, DCE_SVC, LAPB or TCP')
wfIpexSessionDstConnCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionDstConnCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionDstConnCct.setDescription('The circuit from which the connection at the destination to be established to set up a translation session.')
wfIpexSessionDstConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))).clone(namedValues=NamedValues(("pvc", 1), ("svc", 2), ("dcesvc", 4), ("lapb", 8), ("tcp", 16))).clone('pvc')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionDstConnType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionDstConnType.setDescription('Defines type of connection at the destination end. Whether it is a PVC, SVC, DCE_SVC, LAPB or TCP')
wfIpexSessionLocalDTEAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionLocalDTEAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionLocalDTEAddr.setDescription('The Local DTE address (identifies the X.121 address of the X.25 interface on the IPEX). This attribute is only used in the case of a SVC connection initiated from the IPEX to the terminal')
wfIpexSessionRemoteDTEAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionRemoteDTEAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionRemoteDTEAddr.setDescription('The Remote DTE address (identifies the X.121 address of the X.25 interface on the terminal). This attribute is only used in the case of a SVC connection initiated from the IPEX to the terminal')
wfIpexSessionLCN = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionLCN.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionLCN.setDescription('The LCN of the PVC (identifies the channel to be used to establish a PVC connection from the IPEX to the terminal')
wfIpexSessionLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionLocalIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionLocalIpAddr.setDescription('The IP address of an interface on the IPEX to be used to establish a TCP connection with the host server. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexSessionLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionLocalTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionLocalTcpPort.setDescription('The local TCP port number in the IPEX to be used to establish a TCP connection to the host server This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexSessionRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionRemoteIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionRemoteIpAddr.setDescription('The IP address of the remote host with which this translation session is established. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexSessionRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionRemoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionRemoteTcpPort.setDescription('The remote TCP port number in the host to be used to establish a TCP connection from the IPEX to the host server. This attribute is only used in the case of a TCP connection initiated from the IPEX to a host')
wfIpexSessionQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpexSessionQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpexSessionQueueSize.setDescription('The size of the IPEX queues used for transfering data between IPEX and TCP. The size is in bytes.')
mibBuilder.exportSymbols("Wellfleet-IPEX-MIB", wfIpexSessionInstanceIdOffsetForSvc=wfIpexSessionInstanceIdOffsetForSvc, wfIpexMappingLocalDTEAddr=wfIpexMappingLocalDTEAddr, wfIpexSessionEntry=wfIpexSessionEntry, wfIpexMappingXlateCallingX121=wfIpexMappingXlateCallingX121, wfIpexMappingDisable=wfIpexMappingDisable, wfIpexMappingQueueSize=wfIpexMappingQueueSize, wfIpexMappingMsgHdrType=wfIpexMappingMsgHdrType, wfIpexMappingDstConnCct=wfIpexMappingDstConnCct, wfIpexSessionRemoteTcpPort=wfIpexSessionRemoteTcpPort, wfIpexBobEnabled=wfIpexBobEnabled, wfIpexDelete=wfIpexDelete, wfIpexMappingCfgLocalIpAddr=wfIpexMappingCfgLocalIpAddr, wfIpexMappingX25CUDF=wfIpexMappingX25CUDF, wfIpexSessionState=wfIpexSessionState, wfIpexTcpUseIpAddress=wfIpexTcpUseIpAddress, wfIpexMappingID2=wfIpexMappingID2, wfIpexMappingID1=wfIpexMappingID1, wfIpexSessionSrcConnCct=wfIpexSessionSrcConnCct, wfIpexMappingSlotNumber=wfIpexMappingSlotNumber, wfIpexDisable=wfIpexDisable, wfIpexSessionDstConnCct=wfIpexSessionDstConnCct, wfIpexInsCalledDte=wfIpexInsCalledDte, wfIpexMappingRemoteBackupIp=wfIpexMappingRemoteBackupIp, wfIpexMappingKeepaliveTimer=wfIpexMappingKeepaliveTimer, wfIpexMaxAuditIp=wfIpexMaxAuditIp, wfIpexMappingTable=wfIpexMappingTable, wfIpexSessionSrcConnType=wfIpexSessionSrcConnType, wfIpexMappingKeepaliveRetries=wfIpexMappingKeepaliveRetries, wfIpexSessionTable=wfIpexSessionTable, wfIpexSessionLocalIpAddr=wfIpexSessionLocalIpAddr, wfIpexMappingDstConnType=wfIpexMappingDstConnType, wfIpexMappingTcpMaxRetry=wfIpexMappingTcpMaxRetry, wfIpexInsCallingDte=wfIpexInsCallingDte, wfIpexSendResetRequestOnTCPUp=wfIpexSendResetRequestOnTCPUp, wfIpexSessionDstConnType=wfIpexSessionDstConnType, wfIpexMappingRemoteBackupTcpPort=wfIpexMappingRemoteBackupTcpPort, wfIpexTcpRequestCheck=wfIpexTcpRequestCheck, wfIpexState=wfIpexState, wfIpex=wfIpex, wfIpexMappingSrcConnType=wfIpexMappingSrcConnType, wfIpexMappingIdleTimer=wfIpexMappingIdleTimer, wfIpexSessionIndex=wfIpexSessionIndex, wfIpexSessionLocalDTEAddr=wfIpexSessionLocalDTEAddr, wfIpexSessionRemoteIpAddr=wfIpexSessionRemoteIpAddr, wfIpexTcpRequestLimit=wfIpexTcpRequestLimit, wfIpexMappingRemoteIpAddr=wfIpexMappingRemoteIpAddr, wfIpexSessionLocalTcpPort=wfIpexSessionLocalTcpPort, wfIpexMappingCtrlMode=wfIpexMappingCtrlMode, wfIpexMappingRemoteTcpPort=wfIpexMappingRemoteTcpPort, wfIpexSessionQueueSize=wfIpexSessionQueueSize, wfIpexMappingSrcConnCct=wfIpexMappingSrcConnCct, wfIpexTranslateNetworkOutOfOrder=wfIpexTranslateNetworkOutOfOrder, wfIpexMappingRemoteDTEAddr=wfIpexMappingRemoteDTEAddr, wfIpexMappingTrace=wfIpexMappingTrace, wfIpexSessionRemoteDTEAddr=wfIpexSessionRemoteDTEAddr, wfIpexMappingEntry=wfIpexMappingEntry, wfIpexMappingPvcLcn=wfIpexMappingPvcLcn, wfIpexBobTimeout=wfIpexBobTimeout, wfIpexSessionLCN=wfIpexSessionLCN, wfIpexMaxMessageSize=wfIpexMaxMessageSize, wfIpexMappingDelete=wfIpexMappingDelete)
