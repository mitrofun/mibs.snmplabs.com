#
# PySNMP MIB module S5-ETH-MULTISEG-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-ETH-MULTISEG-TOPOLOGY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
s5EnMsTop, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5EnMsTop")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, ModuleIdentity, Integer32, Counter32, MibIdentifier, IpAddress, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Unsigned32", "NotificationType")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
SnpxChassisType, SnpxBackplaneType = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "SnpxChassisType", "SnpxBackplaneType")
s5EthMultisegTopologyMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 0))
s5EthMultisegTopologyMib.setRevisions(('2009-08-18 00:00', '2006-09-13 00:00', '2006-09-12 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: s5EthMultisegTopologyMib.setLastUpdated('200908180000Z')
if mibBuilder.loadTexts: s5EthMultisegTopologyMib.setOrganization('Nortel Networks')
s5EnMsTopInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1))
s5EnMsTopNmm = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2))
s5EnMsTopBdg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3))
s5EnMsTopSrcMac = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4))
s5EnMsTopPort = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5))
s5EnMsTopIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopIpAddr.setStatus('current')
s5EnMsTopStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("topOn", 1), ("topOff", 2))).clone('topOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5EnMsTopStatus.setStatus('current')
s5EnMsTopNmmLstChg = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmLstChg.setStatus('current')
s5EnMsTopBdgLstChg = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgLstChg.setStatus('deprecated')
s5EnMsTopNmmMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmMaxNum.setStatus('current')
s5EnMsTopNmmCurNum = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmCurNum.setStatus('current')
s5EnMsTopBdgMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgMaxNum.setStatus('deprecated')
s5EnMsTopBdgCurNum = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgCurNum.setStatus('deprecated')
s5EnMsTopNmmTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1), )
if mibBuilder.loadTexts: s5EnMsTopNmmTable.setStatus('current')
s5EnMsTopNmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSlot"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmPort"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmIpAddr"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSegId"))
if mibBuilder.loadTexts: s5EnMsTopNmmEntry.setStatus('current')
s5EnMsTopNmmSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmSlot.setStatus('current')
s5EnMsTopNmmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmPort.setStatus('current')
s5EnMsTopNmmIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmIpAddr.setStatus('current')
s5EnMsTopNmmSegId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmSegId.setStatus('current')
s5EnMsTopNmmMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmMacAddr.setStatus('current')
s5EnMsTopNmmChassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 6), SnpxChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmChassisType.setStatus('current')
s5EnMsTopNmmBkplType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 7), SnpxBackplaneType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmBkplType.setStatus('current')
s5EnMsTopNmmLocalSeg = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmLocalSeg.setStatus('current')
s5EnMsTopNmmCurState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("topChanged", 1), ("heartbeat", 2), ("new", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmCurState.setStatus('current')
s5EnMsTopNmmEosSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmEosSize.setStatus('current')
s5EnMsTopNmmEosTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3), )
if mibBuilder.loadTexts: s5EnMsTopNmmEosTable.setStatus('current')
s5EnMsTopNmmEosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSlot"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmPort"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmIpAddr"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSegId"))
if mibBuilder.loadTexts: s5EnMsTopNmmEosEntry.setStatus('current')
s5EnMsTopNmmEos = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopNmmEos.setStatus('current')
s5EnMsTopBdgTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1), )
if mibBuilder.loadTexts: s5EnMsTopBdgTable.setStatus('deprecated')
s5EnMsTopBdgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgSlotNum"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgPortNum"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgIpAddr"))
if mibBuilder.loadTexts: s5EnMsTopBdgEntry.setStatus('deprecated')
s5EnMsTopBdgSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgSlotNum.setStatus('deprecated')
s5EnMsTopBdgPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgPortNum.setStatus('deprecated')
s5EnMsTopBdgIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgIpAddr.setStatus('deprecated')
s5EnMsTopBdgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgNumber.setStatus('deprecated')
s5EnMsTopBdgMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgMacAddr.setStatus('deprecated')
s5EnMsTopBdgType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("localSyn", 2), ("remoteSyn", 3), ("kalpana", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgType.setStatus('deprecated')
s5EnMsTopBdgNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgNumPorts.setStatus('deprecated')
s5EnMsTopBdgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgStatus.setStatus('deprecated')
s5EnMsTopBdgHelloPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgHelloPortNum.setStatus('deprecated')
s5EnMsTopBdgHelloPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("eth", 2), ("tok4", 3), ("tok16", 4), ("fddi", 5), ("t1", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgHelloPortType.setStatus('deprecated')
s5EnMsTopBdgHelloPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgHelloPortStatus.setStatus('deprecated')
s5EnMsTopBdgCompBdgMac1 = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgCompBdgMac1.setStatus('deprecated')
s5EnMsTopBdgCompBdgMac2 = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgCompBdgMac2.setStatus('deprecated')
s5EnMsTopBdgEosSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgEosSize.setStatus('deprecated')
s5EnMsTopBdgEosTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3), )
if mibBuilder.loadTexts: s5EnMsTopBdgEosTable.setStatus('deprecated')
s5EnMsTopBdgEosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgSlotNum"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgPortNum"), (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgIpAddr"))
if mibBuilder.loadTexts: s5EnMsTopBdgEosEntry.setStatus('deprecated')
s5EnMsTopBdgEos = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopBdgEos.setStatus('deprecated')
s5EnMsTopSrcMacAddrTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1), )
if mibBuilder.loadTexts: s5EnMsTopSrcMacAddrTable.setStatus('deprecated')
s5EnMsTopSrcMacAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopSrcMacAddr"))
if mibBuilder.loadTexts: s5EnMsTopSrcMacAddrEntry.setStatus('deprecated')
s5EnMsTopSrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopSrcMacAddr.setStatus('deprecated')
s5EnMsTopSrcMacSegId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopSrcMacSegId.setStatus('deprecated')
s5EnMsTopSrcMacAddrLstChg = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5EnMsTopSrcMacAddrLstChg.setStatus('deprecated')
s5EnMsTopPortTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1), )
if mibBuilder.loadTexts: s5EnMsTopPortTable.setStatus('current')
s5EnMsTopPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1), ).setIndexNames((0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopPortIfIndex"))
if mibBuilder.loadTexts: s5EnMsTopPortEntry.setStatus('current')
s5EnMsTopPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: s5EnMsTopPortIfIndex.setStatus('current')
s5EnMsTopPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("topActive", 1), ("topPassthru", 2))).clone('topActive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5EnMsTopPortState.setStatus('current')
mibBuilder.exportSymbols("S5-ETH-MULTISEG-TOPOLOGY-MIB", PYSNMP_MODULE_ID=s5EthMultisegTopologyMib, s5EnMsTopBdgNumber=s5EnMsTopBdgNumber, s5EnMsTopBdgEosEntry=s5EnMsTopBdgEosEntry, s5EnMsTopNmmMaxNum=s5EnMsTopNmmMaxNum, s5EnMsTopNmmEosTable=s5EnMsTopNmmEosTable, s5EnMsTopNmmChassisType=s5EnMsTopNmmChassisType, s5EnMsTopBdgLstChg=s5EnMsTopBdgLstChg, s5EnMsTopNmmCurNum=s5EnMsTopNmmCurNum, s5EnMsTopNmmIpAddr=s5EnMsTopNmmIpAddr, s5EnMsTopSrcMacSegId=s5EnMsTopSrcMacSegId, s5EnMsTopNmmSegId=s5EnMsTopNmmSegId, s5EnMsTopNmmEos=s5EnMsTopNmmEos, s5EnMsTopPortIfIndex=s5EnMsTopPortIfIndex, s5EnMsTopNmmPort=s5EnMsTopNmmPort, s5EthMultisegTopologyMib=s5EthMultisegTopologyMib, s5EnMsTopBdgEosSize=s5EnMsTopBdgEosSize, s5EnMsTopBdgType=s5EnMsTopBdgType, s5EnMsTopNmmMacAddr=s5EnMsTopNmmMacAddr, s5EnMsTopBdgStatus=s5EnMsTopBdgStatus, s5EnMsTopNmmSlot=s5EnMsTopNmmSlot, s5EnMsTopSrcMacAddrEntry=s5EnMsTopSrcMacAddrEntry, s5EnMsTopSrcMacAddrLstChg=s5EnMsTopSrcMacAddrLstChg, s5EnMsTopNmmLstChg=s5EnMsTopNmmLstChg, s5EnMsTopNmmEosSize=s5EnMsTopNmmEosSize, s5EnMsTopBdgSlotNum=s5EnMsTopBdgSlotNum, s5EnMsTopBdgCurNum=s5EnMsTopBdgCurNum, s5EnMsTopInfo=s5EnMsTopInfo, s5EnMsTopBdgMacAddr=s5EnMsTopBdgMacAddr, s5EnMsTopBdgPortNum=s5EnMsTopBdgPortNum, s5EnMsTopPortState=s5EnMsTopPortState, s5EnMsTopNmmLocalSeg=s5EnMsTopNmmLocalSeg, s5EnMsTopBdgHelloPortNum=s5EnMsTopBdgHelloPortNum, s5EnMsTopBdg=s5EnMsTopBdg, s5EnMsTopBdgTable=s5EnMsTopBdgTable, s5EnMsTopBdgHelloPortStatus=s5EnMsTopBdgHelloPortStatus, s5EnMsTopIpAddr=s5EnMsTopIpAddr, s5EnMsTopBdgNumPorts=s5EnMsTopBdgNumPorts, s5EnMsTopPortTable=s5EnMsTopPortTable, s5EnMsTopSrcMac=s5EnMsTopSrcMac, s5EnMsTopNmmTable=s5EnMsTopNmmTable, s5EnMsTopBdgEos=s5EnMsTopBdgEos, s5EnMsTopNmmEosEntry=s5EnMsTopNmmEosEntry, s5EnMsTopBdgMaxNum=s5EnMsTopBdgMaxNum, s5EnMsTopPort=s5EnMsTopPort, s5EnMsTopBdgHelloPortType=s5EnMsTopBdgHelloPortType, s5EnMsTopBdgEosTable=s5EnMsTopBdgEosTable, s5EnMsTopBdgCompBdgMac2=s5EnMsTopBdgCompBdgMac2, s5EnMsTopPortEntry=s5EnMsTopPortEntry, s5EnMsTopNmm=s5EnMsTopNmm, s5EnMsTopBdgEntry=s5EnMsTopBdgEntry, s5EnMsTopSrcMacAddr=s5EnMsTopSrcMacAddr, s5EnMsTopSrcMacAddrTable=s5EnMsTopSrcMacAddrTable, s5EnMsTopStatus=s5EnMsTopStatus, s5EnMsTopNmmEntry=s5EnMsTopNmmEntry, s5EnMsTopNmmCurState=s5EnMsTopNmmCurState, s5EnMsTopNmmBkplType=s5EnMsTopNmmBkplType, s5EnMsTopBdgCompBdgMac1=s5EnMsTopBdgCompBdgMac1, s5EnMsTopBdgIpAddr=s5EnMsTopBdgIpAddr)