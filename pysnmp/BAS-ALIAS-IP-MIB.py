#
# PySNMP MIB module BAS-ALIAS-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-ALIAS-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
BasChassisId, BasLogicalPortId, basAliasIp, BasSlotId, BasInterfaceId = mibBuilder.importSymbols("BAS-MIB", "BasChassisId", "BasLogicalPortId", "basAliasIp", "BasSlotId", "BasInterfaceId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Unsigned32, ModuleIdentity, Counter64, iso, Integer32, NotificationType, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "Integer32", "NotificationType", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basAliasIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1))
if mibBuilder.loadTexts: basAliasIpMib.setLastUpdated('9810081200Z')
if mibBuilder.loadTexts: basAliasIpMib.setOrganization('Broadband Access Systems')
basIpAlias = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1))
basIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2))
basIpTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1), )
if mibBuilder.loadTexts: basIpTable.setStatus('current')
basIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1), ).setIndexNames((0, "BAS-ALIAS-IP-MIB", "basIpChassis"), (0, "BAS-ALIAS-IP-MIB", "basIpSlot"), (0, "BAS-ALIAS-IP-MIB", "basIpIf"), (0, "BAS-ALIAS-IP-MIB", "basIpLPort"))
if mibBuilder.loadTexts: basIpEntry.setStatus('current')
basIpForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basIpForwarding.setStatus('current')
basIpDefaultTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basIpDefaultTTL.setStatus('current')
basIpInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInReceives.setStatus('current')
basIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInHdrErrors.setStatus('current')
basIpInAddrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInAddrErrors.setStatus('current')
basIpForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpForwDatagrams.setStatus('current')
basIpInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInUnknownProtos.setStatus('current')
basIpInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInDiscards.setStatus('current')
basIpInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpInDelivers.setStatus('current')
basIpOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutRequests.setStatus('current')
basIpOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutDiscards.setStatus('current')
basIpOutNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpOutNoRoutes.setStatus('current')
basIpReasmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmTimeout.setStatus('current')
basIpReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmReqds.setStatus('current')
basIpReasmOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmOKs.setStatus('current')
basIpReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpReasmFails.setStatus('current')
basIpFragOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragOKs.setStatus('current')
basIpFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragFails.setStatus('current')
basIpFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIpFragCreates.setStatus('current')
basIpChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 20), BasChassisId())
if mibBuilder.loadTexts: basIpChassis.setStatus('current')
basIpSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 21), BasSlotId())
if mibBuilder.loadTexts: basIpSlot.setStatus('current')
basIpIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 22), BasInterfaceId())
if mibBuilder.loadTexts: basIpIf.setStatus('current')
basIpLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 23), BasLogicalPortId())
if mibBuilder.loadTexts: basIpLPort.setStatus('current')
basIcmpTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1), )
if mibBuilder.loadTexts: basIcmpTable.setStatus('current')
basIcmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1), ).setIndexNames((0, "BAS-ALIAS-IP-MIB", "basIcmpChassis"), (0, "BAS-ALIAS-IP-MIB", "basIcmpSlot"), (0, "BAS-ALIAS-IP-MIB", "basIcmpIf"), (0, "BAS-ALIAS-IP-MIB", "basIcmpLPort"))
if mibBuilder.loadTexts: basIcmpEntry.setStatus('current')
basIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInMsgs.setStatus('current')
basIcmpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInErrors.setStatus('current')
basIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInDestUnreachs.setStatus('current')
basIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimeExcds.setStatus('current')
basIcmpInParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInParmProbs.setStatus('current')
basIcmpInSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInSrcQuenchs.setStatus('current')
basIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInRedirects.setStatus('current')
basIcmpInEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInEchos.setStatus('current')
basIcmpInEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInEchoReps.setStatus('current')
basIcmpInTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimestamps.setStatus('current')
basIcmpInTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInTimestampReps.setStatus('current')
basIcmpInAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInAddrMasks.setStatus('current')
basIcmpInAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpInAddrMaskReps.setStatus('current')
basIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutMsgs.setStatus('current')
basIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutErrors.setStatus('current')
basIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutDestUnreachs.setStatus('current')
basIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimeExcds.setStatus('current')
basIcmpOutParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutParmProbs.setStatus('current')
basIcmpOutSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutSrcQuenchs.setStatus('current')
basIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutRedirects.setStatus('current')
basIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutEchos.setStatus('current')
basIcmpOutEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutEchoReps.setStatus('current')
basIcmpOutTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimestamps.setStatus('current')
basIcmpOutTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutTimestampReps.setStatus('current')
basIcmpOutAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutAddrMasks.setStatus('current')
basIcmpOutAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basIcmpOutAddrMaskReps.setStatus('current')
basIcmpChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 27), BasChassisId())
if mibBuilder.loadTexts: basIcmpChassis.setStatus('current')
basIcmpSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 28), BasSlotId())
if mibBuilder.loadTexts: basIcmpSlot.setStatus('current')
basIcmpIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 29), BasInterfaceId())
if mibBuilder.loadTexts: basIcmpIf.setStatus('current')
basIcmpLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 30), BasLogicalPortId())
if mibBuilder.loadTexts: basIcmpLPort.setStatus('current')
mibBuilder.exportSymbols("BAS-ALIAS-IP-MIB", basAliasIpMib=basAliasIpMib, basIpInReceives=basIpInReceives, basIpFragCreates=basIpFragCreates, basIcmpSlot=basIcmpSlot, basIcmpOutAddrMaskReps=basIcmpOutAddrMaskReps, basIcmpOutErrors=basIcmpOutErrors, basIcmpLPort=basIcmpLPort, basIcmpInParmProbs=basIcmpInParmProbs, basIcmpInEchoReps=basIcmpInEchoReps, basIcmpInRedirects=basIcmpInRedirects, basIpReasmTimeout=basIpReasmTimeout, basIpReasmOKs=basIpReasmOKs, basIpFragOKs=basIpFragOKs, basIpChassis=basIpChassis, basIcmpInAddrMaskReps=basIcmpInAddrMaskReps, basIcmpChassis=basIcmpChassis, basIcmpInTimestampReps=basIcmpInTimestampReps, basIpInAddrErrors=basIpInAddrErrors, basIcmpOutParmProbs=basIcmpOutParmProbs, basIcmpOutAddrMasks=basIcmpOutAddrMasks, basIpReasmReqds=basIpReasmReqds, basIcmpIf=basIcmpIf, basIpLPort=basIpLPort, basIcmpInDestUnreachs=basIcmpInDestUnreachs, basIcmpInMsgs=basIcmpInMsgs, basIpEntry=basIpEntry, basIcmpOutDestUnreachs=basIcmpOutDestUnreachs, basIcmpOutSrcQuenchs=basIcmpOutSrcQuenchs, basIcmpInAddrMasks=basIcmpInAddrMasks, PYSNMP_MODULE_ID=basAliasIpMib, basIpOutRequests=basIpOutRequests, basIcmpEntry=basIcmpEntry, basIpAlias=basIpAlias, basIpForwDatagrams=basIpForwDatagrams, basIcmpOutTimeExcds=basIcmpOutTimeExcds, basIpOutNoRoutes=basIpOutNoRoutes, basIpOutDiscards=basIpOutDiscards, basIpFragFails=basIpFragFails, basIcmpTable=basIcmpTable, basIcmpInErrors=basIcmpInErrors, basIcmpInEchos=basIcmpInEchos, basIpInDiscards=basIpInDiscards, basIcmpInTimestamps=basIcmpInTimestamps, basIcmpInTimeExcds=basIcmpInTimeExcds, basIpForwarding=basIpForwarding, basIcmpOutEchoReps=basIcmpOutEchoReps, basIpSlot=basIpSlot, basIcmp=basIcmp, basIcmpOutTimestamps=basIcmpOutTimestamps, basIpInDelivers=basIpInDelivers, basIpReasmFails=basIpReasmFails, basIpIf=basIpIf, basIcmpOutRedirects=basIcmpOutRedirects, basIcmpOutTimestampReps=basIcmpOutTimestampReps, basIpInUnknownProtos=basIpInUnknownProtos, basIpDefaultTTL=basIpDefaultTTL, basIcmpOutMsgs=basIcmpOutMsgs, basIpInHdrErrors=basIpInHdrErrors, basIpTable=basIpTable, basIcmpInSrcQuenchs=basIcmpInSrcQuenchs, basIcmpOutEchos=basIcmpOutEchos)
