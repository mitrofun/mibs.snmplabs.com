#
# PySNMP MIB module BAS-ALIAS-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-ALIAS-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
BasInterfaceId, BasSlotId, BasLogicalPortId, basAliasIp, BasChassisId = mibBuilder.importSymbols("BAS-MIB", "BasInterfaceId", "BasSlotId", "BasLogicalPortId", "basAliasIp", "BasChassisId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, Integer32, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Gauge32, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Gauge32", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basAliasIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1))
if mibBuilder.loadTexts: basAliasIpMib.setLastUpdated('9810081200Z')
if mibBuilder.loadTexts: basAliasIpMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basAliasIpMib.setContactInfo(' Tech Support Broadband Access Systems 201 Forest Street Marlboro, MA 01752 U.S.A. 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basAliasIpMib.setDescription('This MIB module defines the Alias IP MIB objects for a Broadband Access System Cluster.')
basIpAlias = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1))
basIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2))
basIpTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1), )
if mibBuilder.loadTexts: basIpTable.setStatus('current')
if mibBuilder.loadTexts: basIpTable.setDescription('Per Chassis Stack IP objects.')
basIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1), ).setIndexNames((0, "BAS-ALIAS-IP-MIB", "basIpChassis"), (0, "BAS-ALIAS-IP-MIB", "basIpSlot"), (0, "BAS-ALIAS-IP-MIB", "basIpIf"), (0, "BAS-ALIAS-IP-MIB", "basIpLPort"))
if mibBuilder.loadTexts: basIpEntry.setStatus('current')
if mibBuilder.loadTexts: basIpEntry.setDescription('IP objects for a Chassis Stack.')
basIpForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basIpForwarding.setStatus('current')
if mibBuilder.loadTexts: basIpForwarding.setDescription('The indication of whether this entity is acting as an IP router in respect to the forwarding of datagrams received by, but not addressed to, this entity. IP routers forward datagrams. IP hosts do not (except those source-routed via the host).')
basIpDefaultTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basIpDefaultTTL.setStatus('current')
if mibBuilder.loadTexts: basIpDefaultTTL.setDescription('The default value inserted into the Time-To-Live field of the IP header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer protocol.')
basIpInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInReceives.setStatus('current')
if mibBuilder.loadTexts: basIpInReceives.setDescription('The total number of input datagrams received from interfaces, including those received in error.')
basIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInHdrErrors.setStatus('current')
if mibBuilder.loadTexts: basIpInHdrErrors.setDescription('The number of input datagrams discarded due to errors in their IP headers, including bad checksums, version number mismatch, other format errors, time-to-live exceeded, errors discovered in processing their IP options, etc.')
basIpInAddrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInAddrErrors.setStatus('current')
if mibBuilder.loadTexts: basIpInAddrErrors.setDescription("The number of input datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E). For entities which are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address.")
basIpForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpForwDatagrams.setStatus('current')
if mibBuilder.loadTexts: basIpForwDatagrams.setDescription('The number of input datagrams for which this entity was not their final IP destination, as a result of which an attempt was made to find a route to forward them to that final destination. In entities which do not act as IP routers, this counter will include only those packets which were Source-Routed via this entity, and the Source-Route option processing was successful.')
basIpInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: basIpInUnknownProtos.setDescription('The number of locally-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol.')
basIpInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInDiscards.setStatus('current')
if mibBuilder.loadTexts: basIpInDiscards.setDescription('The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space). Note that this counter does not include any datagrams discarded while awaiting re-assembly.')
basIpInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInDelivers.setStatus('current')
if mibBuilder.loadTexts: basIpInDelivers.setDescription('The total number of input datagrams successfully delivered to IP user-protocols (including ICMP).')
basIpOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutRequests.setStatus('current')
if mibBuilder.loadTexts: basIpOutRequests.setDescription('The total number of IP datagrams which local IP user- protocols (including ICMP) supplied to IP in requests for transmission. Note that this counter does not include any datagrams counted in ipForwDatagrams.')
basIpOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutDiscards.setStatus('current')
if mibBuilder.loadTexts: basIpOutDiscards.setDescription('The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space). Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion.')
basIpOutNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutNoRoutes.setStatus('current')
if mibBuilder.loadTexts: basIpOutNoRoutes.setDescription("The number of IP datagrams discarded because no route could be found to transmit them to their destination. Note that this counter includes any packets counted in ipForwDatagrams which meet this `no-route' criterion. Note that this includes any datagrams which a host cannot route because all of its default routers are down.")
basIpReasmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmTimeout.setStatus('current')
if mibBuilder.loadTexts: basIpReasmTimeout.setDescription('The maximum number of seconds which received fragments are held while they are awaiting reassembly at this entity.')
basIpReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmReqds.setStatus('current')
if mibBuilder.loadTexts: basIpReasmReqds.setDescription('The number of IP fragments received which needed to be reassembled at this entity.')
basIpReasmOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmOKs.setStatus('current')
if mibBuilder.loadTexts: basIpReasmOKs.setDescription('The number of IP datagrams successfully re-assembled.')
basIpReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmFails.setStatus('current')
if mibBuilder.loadTexts: basIpReasmFails.setDescription('The number of failures detected by the IP re-assembly algorithm (for whatever reason: timed out, errors, etc). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.')
basIpFragOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragOKs.setStatus('current')
if mibBuilder.loadTexts: basIpFragOKs.setDescription('The number of IP datagrams that have been successfully fragmented at this entity.')
basIpFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragFails.setStatus('current')
if mibBuilder.loadTexts: basIpFragFails.setDescription("The number of IP datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set.")
basIpFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragCreates.setStatus('current')
if mibBuilder.loadTexts: basIpFragCreates.setDescription('The number of IP datagram fragments that have been generated as a result of fragmentation at this entity.')
basIpChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 20), BasChassisId())
if mibBuilder.loadTexts: basIpChassis.setStatus('current')
if mibBuilder.loadTexts: basIpChassis.setDescription('The BAS Chassis ID of this card.')
basIpSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 21), BasSlotId())
if mibBuilder.loadTexts: basIpSlot.setStatus('current')
if mibBuilder.loadTexts: basIpSlot.setDescription('The BAS Slot ID of this card.')
basIpIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 22), BasInterfaceId())
if mibBuilder.loadTexts: basIpIf.setStatus('current')
if mibBuilder.loadTexts: basIpIf.setDescription('The BAS interface ID of this card.')
basIpLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 23), BasLogicalPortId())
if mibBuilder.loadTexts: basIpLPort.setStatus('current')
if mibBuilder.loadTexts: basIpLPort.setDescription('The BAS logical port ID of this card.')
basIcmpTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1), )
if mibBuilder.loadTexts: basIcmpTable.setStatus('current')
if mibBuilder.loadTexts: basIcmpTable.setDescription('Per Chassis Stack ICMP objects.')
basIcmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1), ).setIndexNames((0, "BAS-ALIAS-IP-MIB", "basIcmpChassis"), (0, "BAS-ALIAS-IP-MIB", "basIcmpSlot"), (0, "BAS-ALIAS-IP-MIB", "basIcmpIf"), (0, "BAS-ALIAS-IP-MIB", "basIcmpLPort"))
if mibBuilder.loadTexts: basIcmpEntry.setStatus('current')
if mibBuilder.loadTexts: basIcmpEntry.setDescription('ICMP objects for a Chassis Stack.')
basIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInMsgs.setStatus('current')
if mibBuilder.loadTexts: basIcmpInMsgs.setDescription('The total number of ICMP messages which the entity received. Note that this counter includes all those counted by icmpInErrors.')
basIcmpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInErrors.setStatus('current')
if mibBuilder.loadTexts: basIcmpInErrors.setDescription('The number of ICMP messages which the entity received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.).')
basIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInDestUnreachs.setStatus('current')
if mibBuilder.loadTexts: basIcmpInDestUnreachs.setDescription('The number of ICMP Destination Unreachable messages received.')
basIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimeExcds.setStatus('current')
if mibBuilder.loadTexts: basIcmpInTimeExcds.setDescription('The number of ICMP Time Exceeded messages received.')
basIcmpInParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInParmProbs.setStatus('current')
if mibBuilder.loadTexts: basIcmpInParmProbs.setDescription('The number of ICMP Parameter Problem messages received.')
basIcmpInSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInSrcQuenchs.setStatus('current')
if mibBuilder.loadTexts: basIcmpInSrcQuenchs.setDescription('The number of ICMP Source Quench messages received.')
basIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInRedirects.setStatus('current')
if mibBuilder.loadTexts: basIcmpInRedirects.setDescription('The number of ICMP Redirect messages received.')
basIcmpInEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInEchos.setStatus('current')
if mibBuilder.loadTexts: basIcmpInEchos.setDescription('The number of ICMP Echo (request) messages received.')
basIcmpInEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInEchoReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpInEchoReps.setDescription('The number of ICMP Echo Reply messages received.')
basIcmpInTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimestamps.setStatus('current')
if mibBuilder.loadTexts: basIcmpInTimestamps.setDescription('The number of ICMP Timestamp (request) messages received.')
basIcmpInTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimestampReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpInTimestampReps.setDescription('The number of ICMP Timestamp Reply messages received.')
basIcmpInAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInAddrMasks.setStatus('current')
if mibBuilder.loadTexts: basIcmpInAddrMasks.setDescription('The number of ICMP Address Mask Request messages received.')
basIcmpInAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInAddrMaskReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpInAddrMaskReps.setDescription('The number of ICMP Address Mask Reply messages received.')
basIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutMsgs.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutMsgs.setDescription('The total number of ICMP messages which this entity attempted to send. Note that this counter includes all those counted by icmpOutErrors.')
basIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutErrors.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutErrors.setDescription("The number of ICMP messages which this entity did not send due to problems discovered within ICMP such as a lack of buffers. This value should not include errors discovered outside the ICMP layer such as the inability of IP to route the resultant datagram. In some implementations there may be no types of error which contribute to this counter's value.")
basIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutDestUnreachs.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutDestUnreachs.setDescription('The number of ICMP Destination Unreachable messages sent.')
basIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimeExcds.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutTimeExcds.setDescription('The number of ICMP Time Exceeded messages sent.')
basIcmpOutParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutParmProbs.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutParmProbs.setDescription('The number of ICMP Parameter Problem messages sent.')
basIcmpOutSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutSrcQuenchs.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutSrcQuenchs.setDescription('The number of ICMP Source Quench messages sent.')
basIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutRedirects.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutRedirects.setDescription('The number of ICMP Redirect messages sent. For a host, this object will always be zero, since hosts do not send redirects.')
basIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutEchos.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutEchos.setDescription('The number of ICMP Echo (request) messages sent.')
basIcmpOutEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutEchoReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutEchoReps.setDescription('The number of ICMP Echo Reply messages sent.')
basIcmpOutTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimestamps.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutTimestamps.setDescription('The number of ICMP Timestamp (request) messages sent.')
basIcmpOutTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimestampReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutTimestampReps.setDescription('The number of ICMP Timestamp Reply messages sent.')
basIcmpOutAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutAddrMasks.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutAddrMasks.setDescription('The number of ICMP Address Mask Request messages sent.')
basIcmpOutAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutAddrMaskReps.setStatus('current')
if mibBuilder.loadTexts: basIcmpOutAddrMaskReps.setDescription('The number of ICMP Address Mask Reply messages sent.')
basIcmpChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 27), BasChassisId())
if mibBuilder.loadTexts: basIcmpChassis.setStatus('current')
if mibBuilder.loadTexts: basIcmpChassis.setDescription('The BAS Chassis ID of this card.')
basIcmpSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 28), BasSlotId())
if mibBuilder.loadTexts: basIcmpSlot.setStatus('current')
if mibBuilder.loadTexts: basIcmpSlot.setDescription('The BAS Slot ID of this card.')
basIcmpIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 29), BasInterfaceId())
if mibBuilder.loadTexts: basIcmpIf.setStatus('current')
if mibBuilder.loadTexts: basIcmpIf.setDescription('The BAS interface ID of this card.')
basIcmpLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 30), BasLogicalPortId())
if mibBuilder.loadTexts: basIcmpLPort.setStatus('current')
if mibBuilder.loadTexts: basIcmpLPort.setDescription('The BAS logical port ID of this card.')
mibBuilder.exportSymbols("BAS-ALIAS-IP-MIB", basIcmpLPort=basIcmpLPort, basIcmpInEchoReps=basIcmpInEchoReps, basIcmpSlot=basIcmpSlot, basIcmpInAddrMasks=basIcmpInAddrMasks, basIpReasmTimeout=basIpReasmTimeout, basIpChassis=basIpChassis, basIpReasmOKs=basIpReasmOKs, basIcmpOutParmProbs=basIcmpOutParmProbs, basIpForwDatagrams=basIpForwDatagrams, basIcmpInParmProbs=basIcmpInParmProbs, basIcmpInSrcQuenchs=basIcmpInSrcQuenchs, basIcmp=basIcmp, basIcmpOutSrcQuenchs=basIcmpOutSrcQuenchs, basIcmpOutTimeExcds=basIcmpOutTimeExcds, basIcmpInTimestamps=basIcmpInTimestamps, basIcmpOutEchos=basIcmpOutEchos, basIcmpOutTimestamps=basIcmpOutTimestamps, basIcmpOutTimestampReps=basIcmpOutTimestampReps, basIpFragCreates=basIpFragCreates, basIcmpEntry=basIcmpEntry, basIcmpOutMsgs=basIcmpOutMsgs, basIpInDiscards=basIpInDiscards, basIpOutRequests=basIpOutRequests, basIcmpInRedirects=basIcmpInRedirects, basIcmpOutErrors=basIcmpOutErrors, basIpInHdrErrors=basIpInHdrErrors, basIpReasmFails=basIpReasmFails, basIcmpOutDestUnreachs=basIcmpOutDestUnreachs, basIcmpOutRedirects=basIcmpOutRedirects, basIcmpOutAddrMasks=basIcmpOutAddrMasks, basIcmpOutAddrMaskReps=basIcmpOutAddrMaskReps, basIcmpInAddrMaskReps=basIcmpInAddrMaskReps, basIpOutDiscards=basIpOutDiscards, PYSNMP_MODULE_ID=basAliasIpMib, basIpOutNoRoutes=basIpOutNoRoutes, basIpAlias=basIpAlias, basIcmpInTimestampReps=basIcmpInTimestampReps, basIpDefaultTTL=basIpDefaultTTL, basIpInReceives=basIpInReceives, basIcmpInTimeExcds=basIcmpInTimeExcds, basIcmpChassis=basIcmpChassis, basIcmpIf=basIcmpIf, basIpEntry=basIpEntry, basIcmpInMsgs=basIcmpInMsgs, basIcmpInEchos=basIcmpInEchos, basIpFragFails=basIpFragFails, basIpLPort=basIpLPort, basIpInUnknownProtos=basIpInUnknownProtos, basIpForwarding=basIpForwarding, basIcmpInErrors=basIcmpInErrors, basIpSlot=basIpSlot, basIpInDelivers=basIpInDelivers, basIpReasmReqds=basIpReasmReqds, basIpFragOKs=basIpFragOKs, basIpTable=basIpTable, basAliasIpMib=basAliasIpMib, basIcmpOutEchoReps=basIcmpOutEchoReps, basIpInAddrErrors=basIpInAddrErrors, basIcmpTable=basIcmpTable, basIpIf=basIpIf, basIcmpInDestUnreachs=basIcmpInDestUnreachs)
