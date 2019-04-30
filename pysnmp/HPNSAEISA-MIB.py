#
# PySNMP MIB module HPNSAEISA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSAEISA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, Counter64, MibIdentifier, ObjectIdentity, Gauge32, iso, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity", "Gauge32", "iso", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaEISA = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9))
hpnsaEISAMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1))
hpnsaEISAAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2))
hpnsaEISACfgUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3))
hpnsaEISASlotInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4))
hpnsaEISAMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMibRevMajor.setStatus('mandatory')
hpnsaEISAMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMibRevMinor.setStatus('mandatory')
hpnsaEISAAgentTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1), )
if mibBuilder.loadTexts: hpnsaEISAAgentTable.setStatus('mandatory')
hpnsaEISAAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAAgentIndex"))
if mibBuilder.loadTexts: hpnsaEISAAgentEntry.setStatus('mandatory')
hpnsaEISAAgentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentIndex.setStatus('mandatory')
hpnsaEISAAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentName.setStatus('mandatory')
hpnsaEISAAgentVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentVersion.setStatus('mandatory')
hpnsaEISAAgentDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAAgentDate.setStatus('mandatory')
hpnsaEISACfgUtilRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMajor.setStatus('mandatory')
hpnsaEISACfgUtilRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgUtilRevMinor.setStatus('mandatory')
hpnsaEISABoardTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1), )
if mibBuilder.loadTexts: hpnsaEISABoardTable.setStatus('mandatory')
hpnsaEISABoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISASlotIndex"))
if mibBuilder.loadTexts: hpnsaEISABoardEntry.setStatus('mandatory')
hpnsaEISASlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISASlotIndex.setStatus('mandatory')
hpnsaEISASlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("expansion", 0), ("embedded", 1), ("virtual", 2), ("reserved", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISASlotType.setStatus('mandatory')
hpnsaEISACfgRevMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgRevMajor.setStatus('mandatory')
hpnsaEISACfgRevMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISACfgRevMinor.setStatus('mandatory')
hpnsaEISABoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISABoardID.setStatus('mandatory')
hpnsaEISABoardDupCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISABoardDupCfg.setStatus('mandatory')
hpnsaEISANumFunctions = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISANumFunctions.setStatus('mandatory')
hpnsaEISAFunctTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2), )
if mibBuilder.loadTexts: hpnsaEISAFunctTable.setStatus('mandatory')
hpnsaEISAFunctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAFunctSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAFunctIndex"))
if mibBuilder.loadTexts: hpnsaEISAFunctEntry.setStatus('mandatory')
hpnsaEISAFunctSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctSlotIndex.setStatus('mandatory')
hpnsaEISAFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctIndex.setStatus('mandatory')
hpnsaEISAFunctStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctStatus.setStatus('mandatory')
hpnsaEISAFunctType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAFunctType.setStatus('mandatory')
hpnsaEISAMemTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3), )
if mibBuilder.loadTexts: hpnsaEISAMemTable.setStatus('mandatory')
hpnsaEISAMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAMemSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAMemFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAMemAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISAMemEntry.setStatus('mandatory')
hpnsaEISAMemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemSlotIndex.setStatus('mandatory')
hpnsaEISAMemFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemFunctIndex.setStatus('mandatory')
hpnsaEISAMemAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemAllocIndex.setStatus('mandatory')
hpnsaEISAMemStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemStartAddr.setStatus('mandatory')
hpnsaEISAMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemSize.setStatus('mandatory')
hpnsaEISAMemShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nonshareable", 0), ("shareable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemShare.setStatus('mandatory')
hpnsaEISAMemType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("systemBaseOrExtended", 1), ("expanded", 2), ("virtual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemType.setStatus('mandatory')
hpnsaEISAMemCache = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notCached", 1), ("writeThroughCached", 2), ("writeBackCached", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemCache.setStatus('mandatory')
hpnsaEISAMemAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAMemAccess.setStatus('mandatory')
hpnsaEISAIntTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4), )
if mibBuilder.loadTexts: hpnsaEISAIntTable.setStatus('mandatory')
hpnsaEISAIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAIntSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAIntFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAIntAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISAIntEntry.setStatus('mandatory')
hpnsaEISAIntSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntSlotIndex.setStatus('mandatory')
hpnsaEISAIntFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntFunctIndex.setStatus('mandatory')
hpnsaEISAIntAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntAllocIndex.setStatus('mandatory')
hpnsaEISAIntNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntNum.setStatus('mandatory')
hpnsaEISAIntShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntShare.setStatus('mandatory')
hpnsaEISAIntTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("edgeTriggered", 0), ("levelTriggered", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAIntTrigger.setStatus('mandatory')
hpnsaEISADmaTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5), )
if mibBuilder.loadTexts: hpnsaEISADmaTable.setStatus('mandatory')
hpnsaEISADmaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISADmaSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISADmaFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISADmaAllocIndex"))
if mibBuilder.loadTexts: hpnsaEISADmaEntry.setStatus('mandatory')
hpnsaEISADmaSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaSlotIndex.setStatus('mandatory')
hpnsaEISADmaFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaFunctIndex.setStatus('mandatory')
hpnsaEISADmaAllocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaAllocIndex.setStatus('mandatory')
hpnsaEISADmaChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaChannelNum.setStatus('mandatory')
hpnsaEISADmaShare = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaShare.setStatus('mandatory')
hpnsaEISADmaTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("defaultISACompat", 0), ("typeA", 1), ("typeB", 2), ("burstC", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaTiming.setStatus('mandatory')
hpnsaEISADmaXferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("eightBit", 0), ("sixteenBit", 1), ("thirtyTwoBit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISADmaXferSize.setStatus('mandatory')
hpnsaEISAPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6), )
if mibBuilder.loadTexts: hpnsaEISAPortTable.setStatus('mandatory')
hpnsaEISAPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAPortSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortEntryIndex"))
if mibBuilder.loadTexts: hpnsaEISAPortEntry.setStatus('mandatory')
hpnsaEISAPortSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortSlotIndex.setStatus('mandatory')
hpnsaEISAPortFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortFunctIndex.setStatus('mandatory')
hpnsaEISAPortEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortEntryIndex.setStatus('mandatory')
hpnsaEISAPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortAddress.setStatus('mandatory')
hpnsaEISAPortSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortSize.setStatus('mandatory')
hpnsaEISAPortShared = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notShared", 0), ("shared", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortShared.setStatus('mandatory')
hpnsaEISAPortInitTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7), )
if mibBuilder.loadTexts: hpnsaEISAPortInitTable.setStatus('mandatory')
hpnsaEISAPortInitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1), ).setIndexNames((0, "HPNSAEISA-MIB", "hpnsaEISAPortInitSlotIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitFunctIndex"), (0, "HPNSAEISA-MIB", "hpnsaEISAPortInitEntryIndex"))
if mibBuilder.loadTexts: hpnsaEISAPortInitEntry.setStatus('mandatory')
hpnsaEISAPortInitSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitSlotIndex.setStatus('mandatory')
hpnsaEISAPortInitFunctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitFunctIndex.setStatus('mandatory')
hpnsaEISAPortInitEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitEntryIndex.setStatus('mandatory')
hpnsaEISAPortInitData = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 9, 4, 7, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaEISAPortInitData.setStatus('mandatory')
mibBuilder.exportSymbols("HPNSAEISA-MIB", hpnsaEISAMibRevMajor=hpnsaEISAMibRevMajor, hpnsaEISASlotIndex=hpnsaEISASlotIndex, hpnsaEISACfgRevMinor=hpnsaEISACfgRevMinor, hpnsaEISAFunctSlotIndex=hpnsaEISAFunctSlotIndex, hpnsaEISAAgentDate=hpnsaEISAAgentDate, hpnsaEISAMemTable=hpnsaEISAMemTable, hpnsaEISAMemAllocIndex=hpnsaEISAMemAllocIndex, hpnsaEISAMemSize=hpnsaEISAMemSize, hpnsaEISABoardTable=hpnsaEISABoardTable, hpnsaEISAFunctTable=hpnsaEISAFunctTable, hpnsaEISAAgentName=hpnsaEISAAgentName, hpnsaEISAIntShare=hpnsaEISAIntShare, hpnsaEISAPortInitTable=hpnsaEISAPortInitTable, hpnsaEISAPortInitEntry=hpnsaEISAPortInitEntry, hpnsaEISAPortInitEntryIndex=hpnsaEISAPortInitEntryIndex, hpnsaEISAIntTrigger=hpnsaEISAIntTrigger, hpnsaEISAFunctEntry=hpnsaEISAFunctEntry, hpnsaEISAMemAccess=hpnsaEISAMemAccess, hpnsaEISAIntTable=hpnsaEISAIntTable, hpnsaEISAAgentEntry=hpnsaEISAAgentEntry, hpnsaEISAFunctType=hpnsaEISAFunctType, hpnsaEISAPortTable=hpnsaEISAPortTable, hpnsaEISAAgentVersion=hpnsaEISAAgentVersion, hpnsaEISABoardID=hpnsaEISABoardID, hpnsaEISADmaTiming=hpnsaEISADmaTiming, hpnsa=hpnsa, hpnsaEISACfgUtilRevMinor=hpnsaEISACfgUtilRevMinor, hpnsaEISAMemEntry=hpnsaEISAMemEntry, hpnsaEISADmaAllocIndex=hpnsaEISADmaAllocIndex, hpnsaEISADmaTable=hpnsaEISADmaTable, hpnsaEISABoardEntry=hpnsaEISABoardEntry, hpnsaEISAIntSlotIndex=hpnsaEISAIntSlotIndex, hpnsaEISAIntFunctIndex=hpnsaEISAIntFunctIndex, hpnsaEISANumFunctions=hpnsaEISANumFunctions, hpnsaEISACfgUtil=hpnsaEISACfgUtil, hpnsaEISAPortEntry=hpnsaEISAPortEntry, hpnsaEISAMemStartAddr=hpnsaEISAMemStartAddr, hpnsaEISAMemShare=hpnsaEISAMemShare, hpnsaEISAPortInitData=hpnsaEISAPortInitData, hpnsaEISACfgRevMajor=hpnsaEISACfgRevMajor, hpnsaEISAIntEntry=hpnsaEISAIntEntry, hpnsaEISADmaShare=hpnsaEISADmaShare, hpnsaEISAPortSlotIndex=hpnsaEISAPortSlotIndex, hpnsaEISAPortShared=hpnsaEISAPortShared, hpnsaEISAFunctStatus=hpnsaEISAFunctStatus, hpnsaEISAPortFunctIndex=hpnsaEISAPortFunctIndex, hpnsaEISAIntAllocIndex=hpnsaEISAIntAllocIndex, hpnsaEISAFunctIndex=hpnsaEISAFunctIndex, hpnsaEISADmaFunctIndex=hpnsaEISADmaFunctIndex, hpnsaEISAPortInitSlotIndex=hpnsaEISAPortInitSlotIndex, hpnsaEISASlotType=hpnsaEISASlotType, hpnsaEISAMemFunctIndex=hpnsaEISAMemFunctIndex, hpnsaEISAPortSize=hpnsaEISAPortSize, hpnsaEISAMibRevMinor=hpnsaEISAMibRevMinor, hpnsaEISADmaChannelNum=hpnsaEISADmaChannelNum, hpnsaEISABoardDupCfg=hpnsaEISABoardDupCfg, hpnsaEISAAgent=hpnsaEISAAgent, hpnsaEISAMemCache=hpnsaEISAMemCache, hpnsaEISASlotInfo=hpnsaEISASlotInfo, hpnsaEISADmaSlotIndex=hpnsaEISADmaSlotIndex, hp=hp, nm=nm, hpnsaEISACfgUtilRevMajor=hpnsaEISACfgUtilRevMajor, hpnsaEISAMemType=hpnsaEISAMemType, hpnsaEISAIntNum=hpnsaEISAIntNum, hpnsaEISADmaXferSize=hpnsaEISADmaXferSize, hpnsaEISAMemSlotIndex=hpnsaEISAMemSlotIndex, hpnsaEISAPortEntryIndex=hpnsaEISAPortEntryIndex, hpnsaEISADmaEntry=hpnsaEISADmaEntry, hpnsaEISAAgentTable=hpnsaEISAAgentTable, hpnsaEISA=hpnsaEISA, hpnsaEISAAgentIndex=hpnsaEISAAgentIndex, hpnsaEISAPortAddress=hpnsaEISAPortAddress, hpnsaEISAMibRev=hpnsaEISAMibRev, hpnsaEISAPortInitFunctIndex=hpnsaEISAPortInitFunctIndex)