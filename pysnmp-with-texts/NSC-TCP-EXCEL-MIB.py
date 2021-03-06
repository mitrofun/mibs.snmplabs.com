#
# PySNMP MIB module NSC-TCP-EXCEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSC-TCP-EXCEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:24:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
nscDx, = mibBuilder.importSymbols("NSC-MIB", "nscDx")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Unsigned32, IpAddress, Bits, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Unsigned32", "IpAddress", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nscDxTcpXcel = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6))
nscDxTcpXcelTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1))
nscDxTcpXcelUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2))
nscDxTcpXcelTcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoAlgorithm.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoAlgorithm.setDescription('The algorithm used to determine the timeout value used for retransmitting unacknowledged octets.')
nscDxTcpXcelTcpRtoMin = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoMin.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoMin.setDescription('The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout. In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the LBOUND quantity described in RFC 793.')
nscDxTcpXcelTcpRtoMax = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoMax.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRtoMax.setDescription('The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout. In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the UBOUND quantity described in RFC 793.')
nscDxTcpXcelTcpMaxConn = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpMaxConn.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpMaxConn.setDescription('The limit on the total number of TCP connections the entity can support. In entities where the maximum number of connections is dynamic, this object should contain the value -1.')
nscDxTcpXcelTcpActiveOpens = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpActiveOpens.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpActiveOpens.setDescription('The number of times TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state.')
nscDxTcpXcelTcpPassiveOpens = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpPassiveOpens.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpPassiveOpens.setDescription('The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state.')
nscDxTcpXcelTcpAttemptFails = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpAttemptFails.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpAttemptFails.setDescription('The number of times TCP connections have made a direct transition to the CLOSED state from either the SYN-SENT state or the SYN-RCVD state, plus the number of times TCP connections have made a direct transition to the LISTEN state from the SYN-RCVD state.')
nscDxTcpXcelTcpEstabResets = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpEstabResets.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpEstabResets.setDescription('The number of times TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE-WAIT state.')
nscDxTcpXcelTcpCurrEstab = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpCurrEstab.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpCurrEstab.setDescription('The number of TCP connections for which the current state is either ESTABLISHED or CLOSE- WAIT.')
nscDxTcpXcelTcpInSegs = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpInSegs.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpInSegs.setDescription('The total number of segments received, including those received in error. This count includes segments received on currently established connections.')
nscDxTcpXcelTcpOutSegs = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpOutSegs.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpOutSegs.setDescription('The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.')
nscDxTcpXcelTcpRetransSegs = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRetransSegs.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRetransSegs.setDescription('The total number of segments retransmitted - that is, the number of TCP segments transmitted containing one or more previously transmitted octets.')
nscDxTcpXcelTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13), )
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnTable.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnTable.setDescription('A table containing TCP connection-specific information.')
nscDxTcpXcelTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1), ).setIndexNames((0, "NSC-TCP-EXCEL-MIB", "nscDxTcpXcelTcpSapId"))
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnEntry.setDescription('Information about a particular current TCP connection. An object of this type is transient, in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state.')
nscDxTcpXcelTcpSapId = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSapId.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSapId.setDescription('The SAP ID number for this TCP listener.')
nscDxTcpXcelTcpHostIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpHostIdx.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpHostIdx.setDescription('The logical host number for this TCP connection.')
nscDxTcpXcelTcpHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpHostName.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpHostName.setDescription('The logical host name for this TCP connection.')
nscDxTcpXcelTcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnState.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnState.setDescription('The state of this TCP connection.')
nscDxTcpXcelTcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnLocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnLocalAddress.setDescription('The local IP address for this TCP connection. In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used.')
nscDxTcpXcelTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnLocalPort.setDescription('The local port number for this TCP connection.')
nscDxTcpXcelTcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnRemAddress.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnRemAddress.setDescription('The remote IP address for this TCP connection.')
nscDxTcpXcelTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnRemPort.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnRemPort.setDescription('The remote port number for this TCP connection.')
nscDxTcpXcelTcpInErrs = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpInErrs.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpInErrs.setDescription('The total number of segments received in error (e.g., bad TCP checksums).')
nscDxTcpXcelTcpOutRsts = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpOutRsts.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpOutRsts.setDescription('The number of TCP segments sent containing the RST flag. This object is not supported in this version.')
nscDxTcpXcelTcpConnAttempt = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnAttempt.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpConnAttempt.setDescription('The total number of connections initiated. ')
nscDxTcpXcelTcpClosed = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpClosed.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpClosed.setDescription('The total number of connections closed.')
nscDxTcpXcelTcpSegsTimed = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSegsTimed.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSegsTimed.setDescription('The total number of segments we tried to get rtt.')
nscDxTcpXcelTcpRttUpdated = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRttUpdated.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRttUpdated.setDescription('The total number of rtt segments updated.')
nscDxTcpXcelTcpDelAck = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpDelAck.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpDelAck.setDescription('The total number of delayed acks sent.')
nscDxTcpXcelTcpTimeoutDrop = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpTimeoutDrop.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpTimeoutDrop.setDescription('The total number of conn. dropped in rxmt timeout.')
nscDxTcpXcelTcpRexmtTimeo = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRexmtTimeo.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRexmtTimeo.setDescription('The total number of retransmit timeouts.')
nscDxTcpXcelTcpPersistTimeo = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpPersistTimeo.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpPersistTimeo.setDescription('The total number of persist timeouts.')
nscDxTcpXcelTcpKeepTimeo = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepTimeo.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepTimeo.setDescription('The total number of keepalive timeouts.')
nscDxTcpXcelTcpKeepProbe = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepProbe.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepProbe.setDescription('The total number of keepalive probes sent.')
nscDxTcpXcelTcpKeepDrop = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepDrop.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpKeepDrop.setDescription('The total number of connections dropped in keepalive.')
nscDxTcpXcelTcpSndPack = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndPack.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndPack.setDescription('The total number of data packets sent.')
nscDxTcpXcelTcpSndByte = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndByte.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndByte.setDescription('The total number of data bytes sent.')
nscDxTcpXcelTcpSndRexmitPack = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndRexmitPack.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndRexmitPack.setDescription('The total number of data packets retransmitted.')
nscDxTcpXcelTcpSndRexmitByte = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndRexmitByte.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndRexmitByte.setDescription('The total number of data bytes retransmitted.')
nscDxTcpXcelTcpSndAcks = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndAcks.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndAcks.setDescription('The total number of ack-only packets sent.')
nscDxTcpXcelTcpSndProbe = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndProbe.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndProbe.setDescription('The total number of window probes sent.')
nscDxTcpXcelTcpSndUrg = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndUrg.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndUrg.setDescription('The total number of packets sent with URG only.')
nscDxTcpXcelTcpSndWinUp = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndWinUp.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndWinUp.setDescription('The total number of window update only packets sent.')
nscDxTcpXcelTcpSndCtrl = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndCtrl.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpSndCtrl.setDescription('The total number of control (syn|fin|rst) packets sent.')
nscDxTcpXcelTcpPcbCacheMiss = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpPcbCacheMiss.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpPcbCacheMiss.setDescription('The total number of input packets missing pcb cache.')
nscDxTcpXcelTcpRcvPack = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvPack.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvPack.setDescription('The total number of packets received in sequence.')
nscDxTcpXcelTcpRcvBytes = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvBytes.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvBytes.setDescription('The total number of bytes received in Sequence.')
nscDxTcpXcelTcpRcvByteAfterWin = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvByteAfterWin.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvByteAfterWin.setDescription('The total number of bytes rcvd after window.')
nscDxTcpXcelTcpRcvAfterClose = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAfterClose.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAfterClose.setDescription('The total number of bytes rcvd after close.')
nscDxTcpXcelTcpRcvWinProbe = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvWinProbe.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvWinProbe.setDescription('The total number of rcvd window probe packets.')
nscDxTcpXcelTcpRcvdUpack = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvdUpack.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvdUpack.setDescription('The total number of received duplicate acks.')
nscDxTcpXcelTcpRcvAckTooMuch = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckTooMuch.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckTooMuch.setDescription('The total number of rcvd acks for unsent data.')
nscDxTcpXcelTcpRcvAckPack = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckPack.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckPack.setDescription('The total number of rcvd ack packets.')
nscDxTcpXcelTcpRcvAckByte = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckByte.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvAckByte.setDescription('The total number of bytes acked by rcvd acks.')
nscDxTcpXcelTcpRcvWinUpd = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvWinUpd.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelTcpRcvWinUpd.setDescription('The total number of rcvd window update packets.')
nscDxTcpXcelUdpInDatagrams = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpInDatagrams.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpInDatagrams.setDescription('The total number of UDP datagrams delivered to UDP users.')
nscDxTcpXcelUdpNoPorts = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpNoPorts.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpNoPorts.setDescription('The total number of received UDP datagrams for which there was no application at the destination port.')
nscDxTcpXcelUdpInErrors = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpInErrors.setDescription('The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port.')
nscDxTcpXcelUdpOutDatagrams = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpOutDatagrams.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpOutDatagrams.setDescription('The total number of UDP datagrams sent from this entity.')
nscDxTcpXcelUdpNoPortBcast = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpNoPortBcast.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpNoPortBcast.setDescription('The total number of received UDP datagrams for which there was no application at the destination port and arrived as broadcast.')
nscDxTcpXcelUdpPcbCacheMissing = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpPcbCacheMissing.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpPcbCacheMissing.setDescription('The total number of received UDP datagrams which does not have a pcb cache.')
nscDxTcpXcelUdpTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7), )
if mibBuilder.loadTexts: nscDxTcpXcelUdpTable.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpTable.setDescription('A table containing UDP listener information.')
nscDxTcpXcelUdpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1), ).setIndexNames((0, "NSC-TCP-EXCEL-MIB", "nscDxTcpXcelUdpSapId"))
if mibBuilder.loadTexts: nscDxTcpXcelUdpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpEntry.setDescription('Information about a particular current UDP listener.')
nscDxTcpXcelUdpSapId = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpSapId.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpSapId.setDescription('The SAP ID number for this UDP listener.')
nscDxTcpXcelUdpHostIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpHostIdx.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpHostIdx.setDescription('The logical host number for this UDP listener.')
nscDxTcpXcelUdpHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpHostName.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpHostName.setDescription('The logical host name for this UDP listener.')
nscDxTcpXcelUdpLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpLocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpLocalAddress.setDescription('The local IP address for this UDP listener. In the case of a UDP listener which is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used.')
nscDxTcpXcelUdpLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nscDxTcpXcelUdpLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: nscDxTcpXcelUdpLocalPort.setDescription('The local port number for this UDP listener.')
mibBuilder.exportSymbols("NSC-TCP-EXCEL-MIB", nscDxTcpXcelTcpCurrEstab=nscDxTcpXcelTcpCurrEstab, nscDxTcpXcelTcpAttemptFails=nscDxTcpXcelTcpAttemptFails, nscDxTcpXcelTcpRcvBytes=nscDxTcpXcelTcpRcvBytes, nscDxTcpXcelTcpSndByte=nscDxTcpXcelTcpSndByte, nscDxTcpXcelTcpEstabResets=nscDxTcpXcelTcpEstabResets, nscDxTcpXcelTcpPersistTimeo=nscDxTcpXcelTcpPersistTimeo, nscDxTcpXcelTcpSndRexmitPack=nscDxTcpXcelTcpSndRexmitPack, nscDxTcpXcelTcpInSegs=nscDxTcpXcelTcpInSegs, nscDxTcpXcelTcpConnAttempt=nscDxTcpXcelTcpConnAttempt, nscDxTcpXcelTcpRcvWinUpd=nscDxTcpXcelTcpRcvWinUpd, nscDxTcpXcelTcpRexmtTimeo=nscDxTcpXcelTcpRexmtTimeo, nscDxTcpXcelUdpPcbCacheMissing=nscDxTcpXcelUdpPcbCacheMissing, nscDxTcpXcelTcpInErrs=nscDxTcpXcelTcpInErrs, nscDxTcpXcelTcpRcvAckTooMuch=nscDxTcpXcelTcpRcvAckTooMuch, nscDxTcpXcelTcpSndRexmitByte=nscDxTcpXcelTcpSndRexmitByte, nscDxTcpXcelTcpConnRemPort=nscDxTcpXcelTcpConnRemPort, nscDxTcpXcelUdpEntry=nscDxTcpXcelUdpEntry, nscDxTcpXcelTcpRttUpdated=nscDxTcpXcelTcpRttUpdated, nscDxTcpXcelTcpPcbCacheMiss=nscDxTcpXcelTcpPcbCacheMiss, nscDxTcpXcelTcpOutRsts=nscDxTcpXcelTcpOutRsts, nscDxTcpXcel=nscDxTcpXcel, nscDxTcpXcelTcpMaxConn=nscDxTcpXcelTcpMaxConn, nscDxTcpXcelTcpTimeoutDrop=nscDxTcpXcelTcpTimeoutDrop, nscDxTcpXcelUdpLocalAddress=nscDxTcpXcelUdpLocalAddress, nscDxTcpXcelTcpActiveOpens=nscDxTcpXcelTcpActiveOpens, nscDxTcpXcelTcpClosed=nscDxTcpXcelTcpClosed, nscDxTcpXcelTcpSndPack=nscDxTcpXcelTcpSndPack, nscDxTcpXcelTcpSndAcks=nscDxTcpXcelTcpSndAcks, nscDxTcpXcelTcpRtoMax=nscDxTcpXcelTcpRtoMax, nscDxTcpXcelTcpConnLocalPort=nscDxTcpXcelTcpConnLocalPort, nscDxTcpXcelTcpSndProbe=nscDxTcpXcelTcpSndProbe, nscDxTcpXcelTcpSndUrg=nscDxTcpXcelTcpSndUrg, nscDxTcpXcelTcpConnState=nscDxTcpXcelTcpConnState, nscDxTcpXcelTcpKeepProbe=nscDxTcpXcelTcpKeepProbe, nscDxTcpXcelTcpRcvdUpack=nscDxTcpXcelTcpRcvdUpack, nscDxTcpXcelTcpSapId=nscDxTcpXcelTcpSapId, nscDxTcpXcelTcpKeepTimeo=nscDxTcpXcelTcpKeepTimeo, nscDxTcpXcelTcpRcvWinProbe=nscDxTcpXcelTcpRcvWinProbe, nscDxTcpXcelTcpRcvAckByte=nscDxTcpXcelTcpRcvAckByte, nscDxTcpXcelTcpConnTable=nscDxTcpXcelTcpConnTable, nscDxTcpXcelUdpOutDatagrams=nscDxTcpXcelUdpOutDatagrams, nscDxTcpXcelUdpInDatagrams=nscDxTcpXcelUdpInDatagrams, nscDxTcpXcelTcpRtoAlgorithm=nscDxTcpXcelTcpRtoAlgorithm, nscDxTcpXcelTcpOutSegs=nscDxTcpXcelTcpOutSegs, nscDxTcpXcelTcpConnLocalAddress=nscDxTcpXcelTcpConnLocalAddress, nscDxTcpXcelTcp=nscDxTcpXcelTcp, nscDxTcpXcelTcpKeepDrop=nscDxTcpXcelTcpKeepDrop, nscDxTcpXcelTcpRcvByteAfterWin=nscDxTcpXcelTcpRcvByteAfterWin, nscDxTcpXcelTcpRcvAckPack=nscDxTcpXcelTcpRcvAckPack, nscDxTcpXcelUdpInErrors=nscDxTcpXcelUdpInErrors, nscDxTcpXcelTcpHostIdx=nscDxTcpXcelTcpHostIdx, nscDxTcpXcelUdpTable=nscDxTcpXcelUdpTable, nscDxTcpXcelUdpLocalPort=nscDxTcpXcelUdpLocalPort, nscDxTcpXcelTcpRtoMin=nscDxTcpXcelTcpRtoMin, nscDxTcpXcelTcpRcvPack=nscDxTcpXcelTcpRcvPack, nscDxTcpXcelUdpHostName=nscDxTcpXcelUdpHostName, nscDxTcpXcelUdpNoPortBcast=nscDxTcpXcelUdpNoPortBcast, nscDxTcpXcelUdpHostIdx=nscDxTcpXcelUdpHostIdx, nscDxTcpXcelTcpRetransSegs=nscDxTcpXcelTcpRetransSegs, nscDxTcpXcelTcpPassiveOpens=nscDxTcpXcelTcpPassiveOpens, nscDxTcpXcelTcpRcvAfterClose=nscDxTcpXcelTcpRcvAfterClose, nscDxTcpXcelTcpConnEntry=nscDxTcpXcelTcpConnEntry, nscDxTcpXcelUdpNoPorts=nscDxTcpXcelUdpNoPorts, nscDxTcpXcelTcpDelAck=nscDxTcpXcelTcpDelAck, nscDxTcpXcelTcpSndCtrl=nscDxTcpXcelTcpSndCtrl, nscDxTcpXcelTcpSegsTimed=nscDxTcpXcelTcpSegsTimed, nscDxTcpXcelTcpSndWinUp=nscDxTcpXcelTcpSndWinUp, nscDxTcpXcelUdpSapId=nscDxTcpXcelUdpSapId, nscDxTcpXcelUdp=nscDxTcpXcelUdp, nscDxTcpXcelTcpHostName=nscDxTcpXcelTcpHostName, nscDxTcpXcelTcpConnRemAddress=nscDxTcpXcelTcpConnRemAddress)
