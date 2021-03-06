#
# PySNMP MIB module A3COM-HUAWEI-IPA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-IPA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, TimeTicks, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress, Bits, Counter64, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "TimeTicks", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress", "Bits", "Counter64", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
h3cIpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25))
if mibBuilder.loadTexts: h3cIpa.setLastUpdated('200411010000Z')
if mibBuilder.loadTexts: h3cIpa.setOrganization('Huawei 3Com Technologies Co., Ltd.')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

h3cIpaGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1))
h3cIpaGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaGlobalEnable.setStatus('current')
h3cIpaTimeOutSeconds = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 2), Integer32().clone(43200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaTimeOutSeconds.setStatus('current')
h3cIpaIntListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 3), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaIntListMaxItemNum.setStatus('current')
h3cIpaExtListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaExtListMaxItemNum.setStatus('current')
h3cIpaFWListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaFWListMaxItemNum.setStatus('current')
h3cIpaAccountListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaAccountListMaxItemNum.setStatus('current')
h3cIpaAccountListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaAccountListNextIndex.setStatus('current')
h3cIpaListCleaningFlag = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("cleaningAll", 2), ("cleaningIntList", 3), ("cleaningExtList", 4), ("cleaningFWList", 5))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaListCleaningFlag.setStatus('current')
h3cIpaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2), )
if mibBuilder.loadTexts: h3cIpaIfConfigTable.setStatus('current')
h3cIpaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIfConfigIfIndex"))
if mibBuilder.loadTexts: h3cIpaIfConfigEntry.setStatus('current')
h3cIpaIfConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: h3cIpaIfConfigIfIndex.setStatus('current')
h3cIpaIfConfigInEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaIfConfigInEnable.setStatus('current')
h3cIpaIfConfigOutEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaIfConfigOutEnable.setStatus('current')
h3cIpaIfConfigFWEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nodirection", 1), ("inbound", 2), ("outbound", 3), ("bidirection", 4))).clone('nodirection')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpaIfConfigFWEnable.setStatus('current')
h3cIpaAccountListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3), )
if mibBuilder.loadTexts: h3cIpaAccountListTable.setStatus('current')
h3cIpaAccountListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaAccountListIndex"))
if mibBuilder.loadTexts: h3cIpaAccountListEntry.setStatus('current')
h3cIpaAccountListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cIpaAccountListIndex.setStatus('current')
h3cIpaAccountListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpaAccountListIpAddr.setStatus('current')
h3cIpaAccountListIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpaAccountListIpMask.setStatus('current')
h3cIpaAccountListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cIpaAccountListRowStatus.setStatus('current')
h3cIpaIntListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4), )
if mibBuilder.loadTexts: h3cIpaIntListTable.setStatus('current')
h3cIpaIntListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListIpSrc"), (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListIpDst"), (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListProtocol"))
if mibBuilder.loadTexts: h3cIpaIntListEntry.setStatus('current')
h3cIpaIntListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cIpaIntListIpSrc.setStatus('current')
h3cIpaIntListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: h3cIpaIntListIpDst.setStatus('current')
h3cIpaIntListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cIpaIntListProtocol.setStatus('current')
h3cIpaIntListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaIntListInPackets.setStatus('current')
h3cIpaIntListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaIntListInBytes.setStatus('current')
h3cIpaIntListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaIntListOutPackets.setStatus('current')
h3cIpaIntListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaIntListOutBytes.setStatus('current')
h3cIpaExtListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5), )
if mibBuilder.loadTexts: h3cIpaExtListTable.setStatus('current')
h3cIpaExtListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListIpSrc"), (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListIpDst"), (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListProtocol"))
if mibBuilder.loadTexts: h3cIpaExtListEntry.setStatus('current')
h3cIpaExtListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cIpaExtListIpSrc.setStatus('current')
h3cIpaExtListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: h3cIpaExtListIpDst.setStatus('current')
h3cIpaExtListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cIpaExtListProtocol.setStatus('current')
h3cIpaExtListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaExtListInPackets.setStatus('current')
h3cIpaExtListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaExtListInBytes.setStatus('current')
h3cIpaExtListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaExtListOutPackets.setStatus('current')
h3cIpaExtListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaExtListOutBytes.setStatus('current')
h3cIpaFWListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6), )
if mibBuilder.loadTexts: h3cIpaFWListTable.setStatus('current')
h3cIpaFWListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaFWListIpSrc"), (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaFWListIpDst"))
if mibBuilder.loadTexts: h3cIpaFWListEntry.setStatus('current')
h3cIpaFWListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: h3cIpaFWListIpSrc.setStatus('current')
h3cIpaFWListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: h3cIpaFWListIpDst.setStatus('current')
h3cIpaFWListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaFWListInPackets.setStatus('current')
h3cIpaFWListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaFWListInBytes.setStatus('current')
h3cIpaFWListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaFWListOutPackets.setStatus('current')
h3cIpaFWListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIpaFWListOutBytes.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-IPA-MIB", h3cIpaExtListIpDst=h3cIpaExtListIpDst, h3cIpaFWListIpSrc=h3cIpaFWListIpSrc, h3cIpaIfConfigTable=h3cIpaIfConfigTable, h3cIpaIntListIpDst=h3cIpaIntListIpDst, h3cIpaAccountListIpMask=h3cIpaAccountListIpMask, h3cIpaAccountListNextIndex=h3cIpaAccountListNextIndex, h3cIpaExtListMaxItemNum=h3cIpaExtListMaxItemNum, h3cIpaListCleaningFlag=h3cIpaListCleaningFlag, h3cIpaIntListProtocol=h3cIpaIntListProtocol, h3cIpaAccountListMaxItemNum=h3cIpaAccountListMaxItemNum, h3cIpaFWListMaxItemNum=h3cIpaFWListMaxItemNum, h3cIpaAccountListIpAddr=h3cIpaAccountListIpAddr, h3cIpaIntListInPackets=h3cIpaIntListInPackets, h3cIpaExtListEntry=h3cIpaExtListEntry, h3cIpaIfConfigOutEnable=h3cIpaIfConfigOutEnable, h3cIpaIfConfigFWEnable=h3cIpaIfConfigFWEnable, h3cIpaExtListIpSrc=h3cIpaExtListIpSrc, PYSNMP_MODULE_ID=h3cIpa, h3cIpaExtListInPackets=h3cIpaExtListInPackets, h3cIpaTimeOutSeconds=h3cIpaTimeOutSeconds, h3cIpaIntListIpSrc=h3cIpaIntListIpSrc, h3cIpaGlobalStats=h3cIpaGlobalStats, h3cIpa=h3cIpa, h3cIpaIntListOutPackets=h3cIpaIntListOutPackets, h3cIpaFWListOutBytes=h3cIpaFWListOutBytes, h3cIpaIfConfigEntry=h3cIpaIfConfigEntry, h3cIpaAccountListRowStatus=h3cIpaAccountListRowStatus, h3cIpaExtListOutPackets=h3cIpaExtListOutPackets, h3cIpaIntListInBytes=h3cIpaIntListInBytes, h3cIpaIfConfigInEnable=h3cIpaIfConfigInEnable, h3cIpaAccountListTable=h3cIpaAccountListTable, h3cIpaFWListInBytes=h3cIpaFWListInBytes, h3cIpaIntListOutBytes=h3cIpaIntListOutBytes, h3cIpaFWListOutPackets=h3cIpaFWListOutPackets, h3cIpaAccountListIndex=h3cIpaAccountListIndex, h3cIpaFWListEntry=h3cIpaFWListEntry, h3cIpaExtListInBytes=h3cIpaExtListInBytes, h3cIpaFWListTable=h3cIpaFWListTable, h3cIpaFWListInPackets=h3cIpaFWListInPackets, h3cIpaIntListMaxItemNum=h3cIpaIntListMaxItemNum, h3cIpaAccountListEntry=h3cIpaAccountListEntry, h3cIpaExtListOutBytes=h3cIpaExtListOutBytes, h3cIpaFWListIpDst=h3cIpaFWListIpDst, h3cIpaIntListTable=h3cIpaIntListTable, h3cIpaExtListTable=h3cIpaExtListTable, h3cIpaIfConfigIfIndex=h3cIpaIfConfigIfIndex, h3cIpaIntListEntry=h3cIpaIntListEntry, h3cIpaExtListProtocol=h3cIpaExtListProtocol, h3cIpaGlobalEnable=h3cIpaGlobalEnable, InterfaceIndex=InterfaceIndex)
