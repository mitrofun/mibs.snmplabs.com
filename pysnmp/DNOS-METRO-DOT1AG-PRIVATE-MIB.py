#
# PySNMP MIB module DNOS-METRO-DOT1AG-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-METRO-DOT1AG-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, iso, Integer32, Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, Bits, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "iso", "Integer32", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
StorageType, RowStatus, RowPointer, TruthValue, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "RowPointer", "TruthValue", "DisplayString", "TextualConvention", "MacAddress")
fastPathDot1agPrivateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45))
fastPathDot1agPrivateMIB.setRevisions(('2011-01-26 00:00', '2008-05-27 00:00',))
if mibBuilder.loadTexts: fastPathDot1agPrivateMIB.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathDot1agPrivateMIB.setOrganization('Dell, Inc.')
dot1agGlobalConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1))
dot1agMipConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2))
dot1agRMepConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3))
agentDot1agGlobalConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1))
agentDot1agCfmStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agCfmStatus.setStatus('current')
agentDot1agCfmArchieveHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agCfmArchieveHoldTime.setStatus('current')
agentDot1agCfmClearRemoteMEPs = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agCfmClearRemoteMEPs.setStatus('current')
agentDot1agCfmClearTraceRouteCache = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agCfmClearTraceRouteCache.setStatus('current')
agentDot1agMipConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1))
agentDot1agMipTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1), )
if mibBuilder.loadTexts: agentDot1agMipTable.setStatus('current')
agentDot1agMipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1), ).setIndexNames((0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agMipMdIndex"), (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agMipIfIndex"))
if mibBuilder.loadTexts: agentDot1agMipEntry.setStatus('current')
agentDot1agMipMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: agentDot1agMipMdIndex.setStatus('current')
agentDot1agMipIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: agentDot1agMipIfIndex.setStatus('current')
agentDot1agMipMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDot1agMipMode.setStatus('current')
agentDot1agRMepConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1))
agentDot1agRMepTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1), )
if mibBuilder.loadTexts: agentDot1agRMepTable.setStatus('current')
agentDot1agRMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1), ).setIndexNames((0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMdIndex"), (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMaIndex"), (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMepIdIndex"), (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepIdentifier"))
if mibBuilder.loadTexts: agentDot1agRMepEntry.setStatus('current')
agentDot1agRMepMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentDot1agRMepMdIndex.setStatus('current')
agentDot1agRMepMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: agentDot1agRMepMaIndex.setStatus('current')
agentDot1agRMepMepIdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), )))
if mibBuilder.loadTexts: agentDot1agRMepMepIdIndex.setStatus('current')
agentDot1agRMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDot1agRMepIdentifier.setStatus('current')
agentDot1agRMepIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agRMepIfIndex.setStatus('current')
agentDot1agRMepMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1agRMepMacAddress.setStatus('current')
agentDot1agRMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDot1agRMepRowStatus.setStatus('current')
mibBuilder.exportSymbols("DNOS-METRO-DOT1AG-PRIVATE-MIB", dot1agMipConfigGroup=dot1agMipConfigGroup, agentDot1agGlobalConfigGroup=agentDot1agGlobalConfigGroup, agentDot1agRMepMepIdIndex=agentDot1agRMepMepIdIndex, dot1agRMepConfigGroup=dot1agRMepConfigGroup, agentDot1agRMepRowStatus=agentDot1agRMepRowStatus, fastPathDot1agPrivateMIB=fastPathDot1agPrivateMIB, agentDot1agRMepEntry=agentDot1agRMepEntry, agentDot1agRMepMaIndex=agentDot1agRMepMaIndex, agentDot1agCfmClearTraceRouteCache=agentDot1agCfmClearTraceRouteCache, dot1agGlobalConfigGroup=dot1agGlobalConfigGroup, agentDot1agRMepTable=agentDot1agRMepTable, agentDot1agRMepMdIndex=agentDot1agRMepMdIndex, agentDot1agMipTable=agentDot1agMipTable, agentDot1agMipEntry=agentDot1agMipEntry, agentDot1agRMepMacAddress=agentDot1agRMepMacAddress, agentDot1agMipMdIndex=agentDot1agMipMdIndex, agentDot1agRMepConfigGroup=agentDot1agRMepConfigGroup, agentDot1agMipMode=agentDot1agMipMode, agentDot1agCfmArchieveHoldTime=agentDot1agCfmArchieveHoldTime, agentDot1agRMepIfIndex=agentDot1agRMepIfIndex, agentDot1agMipConfigGroup=agentDot1agMipConfigGroup, agentDot1agMipIfIndex=agentDot1agMipIfIndex, PYSNMP_MODULE_ID=fastPathDot1agPrivateMIB, agentDot1agCfmStatus=agentDot1agCfmStatus, agentDot1agRMepIdentifier=agentDot1agRMepIdentifier, agentDot1agCfmClearRemoteMEPs=agentDot1agCfmClearRemoteMEPs)
