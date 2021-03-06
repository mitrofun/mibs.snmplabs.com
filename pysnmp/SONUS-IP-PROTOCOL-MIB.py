#
# PySNMP MIB module SONUS-IP-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-IP-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso, Unsigned32, Counter32, Counter64, NotificationType, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "Counter64", "NotificationType", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonusPacketMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusPacketMIBs")
sonusIpProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4))
if mibBuilder.loadTexts: sonusIpProtocolMIB.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: sonusIpProtocolMIB.setOrganization('Sonus Networks, Inc.')
sonusMib_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2)).setLabel("sonusMib-2")
sonusIp = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4))
sonusIpGeneralGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1), )
if mibBuilder.loadTexts: sonusIpGeneralGroupTable.setStatus('current')
sonusIpGeneralGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupInstance"))
if mibBuilder.loadTexts: sonusIpGeneralGroupEntry.setStatus('current')
sonusIpForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpForwarding.setStatus('current')
sonusIpDefaultTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpDefaultTTL.setStatus('current')
sonusIpInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInReceives.setStatus('current')
sonusIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInHdrErrors.setStatus('current')
sonusIpInAddrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInAddrErrors.setStatus('current')
sonusIpForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpForwDatagrams.setStatus('current')
sonusIpInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInUnknownProtos.setStatus('current')
sonusIpInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInDiscards.setStatus('current')
sonusIpInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpInDelivers.setStatus('current')
sonusIpOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpOutRequests.setStatus('current')
sonusIpOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpOutDiscards.setStatus('current')
sonusIpOutNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpOutNoRoutes.setStatus('current')
sonusIpReasmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpReasmTimeout.setStatus('current')
sonusIpReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpReasmReqds.setStatus('current')
sonusIpReasmOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpReasmOKs.setStatus('current')
sonusIpReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpReasmFails.setStatus('current')
sonusIpFragOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpFragOKs.setStatus('current')
sonusIpFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpFragFails.setStatus('current')
sonusIpFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpFragCreates.setStatus('current')
sonusIpRoutingDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpRoutingDiscards.setStatus('current')
sonusIpGeneralGroupShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpGeneralGroupShelf.setStatus('current')
sonusIpGeneralGroupSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpGeneralGroupSlot.setStatus('current')
sonusIpGeneralGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIpGeneralGroupInstance.setStatus('current')
sonusIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5))
sonusIcmpGeneralGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1), )
if mibBuilder.loadTexts: sonusIcmpGeneralGroupTable.setStatus('current')
sonusIcmpGeneralGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupInstance"))
if mibBuilder.loadTexts: sonusIcmpGeneralGroupEntry.setStatus('current')
sonusIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInMsgs.setStatus('current')
sonusIcmpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInErrors.setStatus('current')
sonusIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInDestUnreachs.setStatus('current')
sonusIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInTimeExcds.setStatus('current')
sonusIcmpInParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInParmProbs.setStatus('current')
sonusIcmpInSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInSrcQuenchs.setStatus('current')
sonusIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInRedirects.setStatus('current')
sonusIcmpInEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInEchos.setStatus('current')
sonusIcmpInEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInEchoReps.setStatus('current')
sonusIcmpInTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInTimestamps.setStatus('current')
sonusIcmpInTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInTimestampReps.setStatus('current')
sonusIcmpInAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInAddrMasks.setStatus('current')
sonusIcmpInAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpInAddrMaskReps.setStatus('current')
sonusIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutMsgs.setStatus('current')
sonusIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutErrors.setStatus('current')
sonusIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutDestUnreachs.setStatus('current')
sonusIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutTimeExcds.setStatus('current')
sonusIcmpOutParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutParmProbs.setStatus('current')
sonusIcmpOutSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutSrcQuenchs.setStatus('current')
sonusIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutRedirects.setStatus('current')
sonusIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutEchos.setStatus('current')
sonusIcmpOutEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutEchoReps.setStatus('current')
sonusIcmpOutTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutTimestamps.setStatus('current')
sonusIcmpOutTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutTimestampReps.setStatus('current')
sonusIcmpOutAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutAddrMasks.setStatus('current')
sonusIcmpOutAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpOutAddrMaskReps.setStatus('current')
sonusIcmpGeneralGroupShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpGeneralGroupShelf.setStatus('current')
sonusIcmpGeneralGroupSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpGeneralGroupSlot.setStatus('current')
sonusIcmpGeneralGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusIcmpGeneralGroupInstance.setStatus('current')
sonusTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6))
sonusTcpGeneralGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1), )
if mibBuilder.loadTexts: sonusTcpGeneralGroupTable.setStatus('current')
sonusTcpGeneralGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupInstance"))
if mibBuilder.loadTexts: sonusTcpGeneralGroupEntry.setStatus('current')
sonusTcpRtoAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpRtoAlgorithm.setStatus('current')
sonusTcpRtoMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpRtoMin.setStatus('current')
sonusTcpRtoMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpRtoMax.setStatus('current')
sonusTcpMaxConn = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpMaxConn.setStatus('current')
sonusTcpActiveOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpActiveOpens.setStatus('current')
sonusTcpPassiveOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpPassiveOpens.setStatus('current')
sonusTcpAttemptFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpAttemptFails.setStatus('current')
sonusTcpEstabResets = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpEstabResets.setStatus('current')
sonusTcpCurrEstab = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpCurrEstab.setStatus('current')
sonusTcpInSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpInSegs.setStatus('current')
sonusTcpOutSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpOutSegs.setStatus('current')
sonusTcpRetransSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpRetransSegs.setStatus('current')
sonusTcpInErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpInErrs.setStatus('current')
sonusTcpOutRsts = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpOutRsts.setStatus('current')
sonusTcpGeneralGroupShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpGeneralGroupShelf.setStatus('current')
sonusTcpGeneralGroupSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpGeneralGroupSlot.setStatus('current')
sonusTcpGeneralGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpGeneralGroupInstance.setStatus('current')
sonusTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13), )
if mibBuilder.loadTexts: sonusTcpConnTable.setStatus('current')
sonusTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnInstance"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnLocalAddress"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnLocalPort"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnRemAddress"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnRemPort"))
if mibBuilder.loadTexts: sonusTcpConnEntry.setStatus('current')
sonusTcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnState.setStatus('current')
sonusTcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnLocalAddress.setStatus('current')
sonusTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnLocalPort.setStatus('current')
sonusTcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnRemAddress.setStatus('current')
sonusTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnRemPort.setStatus('current')
sonusTcpConnShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnShelf.setStatus('current')
sonusTcpConnSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnSlot.setStatus('current')
sonusTcpConnInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusTcpConnInstance.setStatus('current')
sonusUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7))
sonusUdpGeneralGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1), )
if mibBuilder.loadTexts: sonusUdpGeneralGroupTable.setStatus('current')
sonusUdpGeneralGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupInstance"))
if mibBuilder.loadTexts: sonusUdpGeneralGroupEntry.setStatus('current')
sonusUdpInDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpInDatagrams.setStatus('current')
sonusUdpNoPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpNoPorts.setStatus('current')
sonusUdpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpInErrors.setStatus('current')
sonusUdpOutDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpOutDatagrams.setStatus('current')
sonusUdpGeneralGroupShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpGeneralGroupShelf.setStatus('current')
sonusUdpGeneralGroupSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpGeneralGroupSlot.setStatus('current')
sonusUdpGeneralGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpGeneralGroupInstance.setStatus('current')
sonusUdpTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5), )
if mibBuilder.loadTexts: sonusUdpTable.setStatus('current')
sonusUdpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1), ).setIndexNames((0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpShelf"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpSlot"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpInstance"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpLocalAddress"), (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpLocalPort"))
if mibBuilder.loadTexts: sonusUdpEntry.setStatus('current')
sonusUdpLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpLocalAddress.setStatus('current')
sonusUdpLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpLocalPort.setStatus('current')
sonusUdpShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpShelf.setStatus('current')
sonusUdpSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpSlot.setStatus('current')
sonusUdpInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusUdpInstance.setStatus('current')
mibBuilder.exportSymbols("SONUS-IP-PROTOCOL-MIB", sonusTcpConnLocalAddress=sonusTcpConnLocalAddress, sonusUdpInErrors=sonusUdpInErrors, sonusIpOutNoRoutes=sonusIpOutNoRoutes, sonusIcmpInEchoReps=sonusIcmpInEchoReps, sonusTcpConnEntry=sonusTcpConnEntry, sonusIcmpOutAddrMaskReps=sonusIcmpOutAddrMaskReps, sonusTcpConnRemAddress=sonusTcpConnRemAddress, sonusUdpInDatagrams=sonusUdpInDatagrams, sonusIpDefaultTTL=sonusIpDefaultTTL, sonusIpInDelivers=sonusIpInDelivers, sonusIpForwDatagrams=sonusIpForwDatagrams, sonusUdpShelf=sonusUdpShelf, sonusTcpCurrEstab=sonusTcpCurrEstab, sonusUdpGeneralGroupInstance=sonusUdpGeneralGroupInstance, sonusTcpInErrs=sonusTcpInErrs, sonusTcpConnState=sonusTcpConnState, sonusTcpRtoMin=sonusTcpRtoMin, sonusUdpGeneralGroupTable=sonusUdpGeneralGroupTable, sonusUdp=sonusUdp, sonusTcpMaxConn=sonusTcpMaxConn, sonusIpInAddrErrors=sonusIpInAddrErrors, sonusTcpConnInstance=sonusTcpConnInstance, sonusIcmpOutErrors=sonusIcmpOutErrors, sonusIcmpInAddrMaskReps=sonusIcmpInAddrMaskReps, sonusUdpEntry=sonusUdpEntry, sonusIpOutDiscards=sonusIpOutDiscards, sonusIpProtocolMIB=sonusIpProtocolMIB, sonusTcpRetransSegs=sonusTcpRetransSegs, sonusIcmpOutMsgs=sonusIcmpOutMsgs, sonusIpGeneralGroupSlot=sonusIpGeneralGroupSlot, sonusIpReasmOKs=sonusIpReasmOKs, sonusUdpLocalAddress=sonusUdpLocalAddress, sonusUdpOutDatagrams=sonusUdpOutDatagrams, sonusMib_2=sonusMib_2, sonusIcmpInTimeExcds=sonusIcmpInTimeExcds, sonusTcpRtoMax=sonusTcpRtoMax, sonusIcmpInTimestamps=sonusIcmpInTimestamps, sonusIpForwarding=sonusIpForwarding, sonusIcmpOutAddrMasks=sonusIcmpOutAddrMasks, sonusIpInDiscards=sonusIpInDiscards, sonusTcpRtoAlgorithm=sonusTcpRtoAlgorithm, sonusTcpConnSlot=sonusTcpConnSlot, sonusIcmpOutEchoReps=sonusIcmpOutEchoReps, sonusIpOutRequests=sonusIpOutRequests, sonusIpGeneralGroupEntry=sonusIpGeneralGroupEntry, sonusTcpGeneralGroupEntry=sonusTcpGeneralGroupEntry, sonusIpInHdrErrors=sonusIpInHdrErrors, sonusUdpGeneralGroupSlot=sonusUdpGeneralGroupSlot, sonusUdpInstance=sonusUdpInstance, sonusIcmpInSrcQuenchs=sonusIcmpInSrcQuenchs, sonusIcmpOutSrcQuenchs=sonusIcmpOutSrcQuenchs, sonusIcmpOutTimestampReps=sonusIcmpOutTimestampReps, sonusIcmpInDestUnreachs=sonusIcmpInDestUnreachs, sonusIcmpInMsgs=sonusIcmpInMsgs, sonusIpGeneralGroupShelf=sonusIpGeneralGroupShelf, sonusIcmpOutTimestamps=sonusIcmpOutTimestamps, sonusIcmpGeneralGroupShelf=sonusIcmpGeneralGroupShelf, sonusUdpGeneralGroupShelf=sonusUdpGeneralGroupShelf, sonusIpFragCreates=sonusIpFragCreates, sonusIpReasmTimeout=sonusIpReasmTimeout, sonusIpGeneralGroupTable=sonusIpGeneralGroupTable, PYSNMP_MODULE_ID=sonusIpProtocolMIB, sonusIpFragOKs=sonusIpFragOKs, sonusIcmpGeneralGroupInstance=sonusIcmpGeneralGroupInstance, sonusIcmpInAddrMasks=sonusIcmpInAddrMasks, sonusIcmpGeneralGroupSlot=sonusIcmpGeneralGroupSlot, sonusIpReasmFails=sonusIpReasmFails, sonusIpGeneralGroupInstance=sonusIpGeneralGroupInstance, sonusUdpSlot=sonusUdpSlot, sonusIcmpOutRedirects=sonusIcmpOutRedirects, sonusTcpAttemptFails=sonusTcpAttemptFails, sonusIcmpInRedirects=sonusIcmpInRedirects, sonusTcp=sonusTcp, sonusTcpPassiveOpens=sonusTcpPassiveOpens, sonusIpReasmReqds=sonusIpReasmReqds, sonusTcpInSegs=sonusTcpInSegs, sonusUdpLocalPort=sonusUdpLocalPort, sonusIcmpOutDestUnreachs=sonusIcmpOutDestUnreachs, sonusTcpOutSegs=sonusTcpOutSegs, sonusTcpConnRemPort=sonusTcpConnRemPort, sonusIcmpInTimestampReps=sonusIcmpInTimestampReps, sonusTcpGeneralGroupInstance=sonusTcpGeneralGroupInstance, sonusTcpGeneralGroupSlot=sonusTcpGeneralGroupSlot, sonusUdpNoPorts=sonusUdpNoPorts, sonusTcpOutRsts=sonusTcpOutRsts, sonusIpFragFails=sonusIpFragFails, sonusTcpGeneralGroupTable=sonusTcpGeneralGroupTable, sonusUdpGeneralGroupEntry=sonusUdpGeneralGroupEntry, sonusIcmpOutTimeExcds=sonusIcmpOutTimeExcds, sonusIcmpGeneralGroupTable=sonusIcmpGeneralGroupTable, sonusUdpTable=sonusUdpTable, sonusIcmpInErrors=sonusIcmpInErrors, sonusIpInReceives=sonusIpInReceives, sonusTcpEstabResets=sonusTcpEstabResets, sonusIcmpGeneralGroupEntry=sonusIcmpGeneralGroupEntry, sonusIcmpInParmProbs=sonusIcmpInParmProbs, sonusTcpGeneralGroupShelf=sonusTcpGeneralGroupShelf, sonusIcmpOutParmProbs=sonusIcmpOutParmProbs, sonusTcpConnTable=sonusTcpConnTable, sonusIpRoutingDiscards=sonusIpRoutingDiscards, sonusTcpConnShelf=sonusTcpConnShelf, sonusTcpConnLocalPort=sonusTcpConnLocalPort, sonusIpInUnknownProtos=sonusIpInUnknownProtos, sonusIcmpInEchos=sonusIcmpInEchos, sonusIcmpOutEchos=sonusIcmpOutEchos, sonusIcmp=sonusIcmp, sonusTcpActiveOpens=sonusTcpActiveOpens, sonusIp=sonusIp)
