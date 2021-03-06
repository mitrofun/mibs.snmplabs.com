#
# PySNMP MIB module FECLIENT827x-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FECLIENT827x-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
proElsSubSysEventMsg, = mibBuilder.importSymbols("PROTEON-MIB", "proElsSubSysEventMsg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, iso, Gauge32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, NotificationType, NotificationType, TimeTicks, MibIdentifier, ObjectIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "Gauge32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "NotificationType", "NotificationType", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibmMSSClientMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
fe827xNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 0))
fe827xMIBObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1))
fe827xMIBConformanceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2))
fe827xProdGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1))
fe827xPCIAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2))
fe827xStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3))
fe827xSwitchGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4))
feMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 1))
feMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 2))
fe827xResetFlag = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noreset", 1), ("reboot", 2))).clone('noreset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fe827xResetFlag.setStatus('mandatory')
fe827xDRAMInstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xDRAMInstalled.setStatus('mandatory')
fe827xCacheInstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xCacheInstalled.setStatus('mandatory')
fe827xFlashInstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xFlashInstalled.setStatus('mandatory')
fe827xSRAMInstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xSRAMInstalled.setStatus('mandatory')
fe827xNotifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fe827xNotifyStatus.setStatus('mandatory')
fe827xSwitchIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xSwitchIPAddr.setStatus('mandatory')
fe827xSwitchSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xSwitchSlotNum.setStatus('mandatory')
fe827xSwitchPortNum = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xSwitchPortNum.setStatus('mandatory')
fe827xPCINumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCINumSlot.setStatus('mandatory')
fe827xPCIAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2), )
if mibBuilder.loadTexts: fe827xPCIAdapTable.setStatus('mandatory')
fe827xPCIAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1), ).setIndexNames((0, "FECLIENT827x-MIB", "fe827xPCIAdapSlotNum"))
if mibBuilder.loadTexts: fe827xPCIAdapEntry.setStatus('mandatory')
fe827xPCIAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: fe827xPCIAdapSlotNum.setStatus('mandatory')
fe827xPCIAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("atm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapType.setStatus('mandatory')
fe827xPCIAdapConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notConfigured", 1), ("atm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapConfigType.setStatus('mandatory')
fe827xPCIAdapATMMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("smf", 2), ("mmf", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapATMMediaType.setStatus('mandatory')
fe827xPCIAdapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("unknown", 1), ("notConfigured", 2), ("notPresent", 3), ("unavailable", 4), ("doesNotApply", 5), ("enablePending", 6), ("enabled", 7), ("disablePending", 8), ("disabled", 9), ("missConfigured", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapOperStatus.setStatus('mandatory')
fe827xPCIAdapDiagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("inactive", 2), ("idle", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapDiagStatus.setStatus('mandatory')
fe827xPCIAdapNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("testing", 4), ("doesNotApply", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapNetworkStatus.setStatus('mandatory')
fe827xPCIAdapFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("noFault", 2), ("isolated", 3), ("nonIsolated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xPCIAdapFaultStatus.setStatus('mandatory')
fe827xStatTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1), )
if mibBuilder.loadTexts: fe827xStatTable.setStatus('mandatory')
fe827xStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1), ).setIndexNames((0, "FECLIENT827x-MIB", "fe827xStatQueueNum"))
if mibBuilder.loadTexts: fe827xStatEntry.setStatus('mandatory')
fe827xStatQueueNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: fe827xStatQueueNum.setStatus('mandatory')
fe827xStatFramesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xStatFramesSent.setStatus('mandatory')
fe827xStatFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xStatFramesReceived.setStatus('mandatory')
fe827xDomainIfTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1), )
if mibBuilder.loadTexts: fe827xDomainIfTable.setStatus('mandatory')
fe827xDomainIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fe827xDomainIfEntry.setStatus('mandatory')
fe827xSwitchDomainNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fe827xSwitchDomainNum.setStatus('mandatory')
fe827xPCIAdapStatusChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 4) + (0,1)).setObjects(("FECLIENT827x-MIB", "fe827xPCIAdapConfigType"), ("FECLIENT827x-MIB", "fe827xPCIAdapOperStatus"), ("FECLIENT827x-MIB", "fe827xPCIAdapDiagStatus"), ("FECLIENT827x-MIB", "fe827xPCIAdapNetworkStatus"), ("FECLIENT827x-MIB", "fe827xPCIAdapFaultStatus"))
feGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 1, 1))
feMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 2, 1))
mibBuilder.exportSymbols("FECLIENT827x-MIB", fe827xPCINumSlot=fe827xPCINumSlot, fe827xPCIAdapNetworkStatus=fe827xPCIAdapNetworkStatus, ibmProd=ibmProd, fe827xDomainIfTable=fe827xDomainIfTable, fe827xStatGroup=fe827xStatGroup, fe827xPCIAdapEntry=fe827xPCIAdapEntry, fe827xNotifyStatus=fe827xNotifyStatus, fe827xSwitchSlotNum=fe827xSwitchSlotNum, fe827xSwitchIPAddr=fe827xSwitchIPAddr, ibm=ibm, fe827xPCIAdapOperStatus=fe827xPCIAdapOperStatus, fe827xFlashInstalled=fe827xFlashInstalled, fe827xPCIAdapConfigType=fe827xPCIAdapConfigType, fe827xProdGroup=fe827xProdGroup, fe827xSwitchGroup=fe827xSwitchGroup, fe827xStatQueueNum=fe827xStatQueueNum, fe827xPCIAdapDiagStatus=fe827xPCIAdapDiagStatus, fe827xStatTable=fe827xStatTable, ibmMSSClientMIB=ibmMSSClientMIB, nwaysMSS=nwaysMSS, feMIBCompliance=feMIBCompliance, feMIBCompliances=feMIBCompliances, fe827xSRAMInstalled=fe827xSRAMInstalled, fe827xSwitchPortNum=fe827xSwitchPortNum, fe827xResetFlag=fe827xResetFlag, fe827xPCIAdapFaultStatus=fe827xPCIAdapFaultStatus, fe827xPCIAdapSlotNum=fe827xPCIAdapSlotNum, fe827xStatEntry=fe827xStatEntry, fe827xSwitchDomainNum=fe827xSwitchDomainNum, feGroup=feGroup, fe827xPCIAdapStatusChg=fe827xPCIAdapStatusChg, fe827xDomainIfEntry=fe827xDomainIfEntry, fe827xPCIAdapterGroup=fe827xPCIAdapterGroup, fe827xMIBConformanceGroup=fe827xMIBConformanceGroup, fe827xPCIAdapATMMediaType=fe827xPCIAdapATMMediaType, fe827xDRAMInstalled=fe827xDRAMInstalled, fe827xPCIAdapType=fe827xPCIAdapType, fe827xStatFramesSent=fe827xStatFramesSent, fe827xPCIAdapTable=fe827xPCIAdapTable, fe827xMIBObjectGroup=fe827xMIBObjectGroup, fe827xCacheInstalled=fe827xCacheInstalled, fe827xStatFramesReceived=fe827xStatFramesReceived, fe827xNotificationGroup=fe827xNotificationGroup, feMIBGroups=feMIBGroups)
