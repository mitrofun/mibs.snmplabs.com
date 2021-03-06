#
# PySNMP MIB module Unisphere-Data-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Integer32, Counter32, ObjectIdentity, ModuleIdentity, iso, Counter64, MibIdentifier, Unsigned32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Integer32", "Counter32", "ObjectIdentity", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "Unsigned32", "Gauge32", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, UsdEnable = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex", "UsdEnable")
usdPPPoEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18))
usdPPPoEMIB.setRevisions(('2002-08-16 21:46', '2001-06-19 14:27', '2001-03-21 15:00', '2001-02-12 00:00', '2000-10-25 00:00', '1999-05-13 00:00',))
if mibBuilder.loadTexts: usdPPPoEMIB.setLastUpdated('200208162146Z')
if mibBuilder.loadTexts: usdPPPoEMIB.setOrganization('Juniper Networks, Inc.')
usdPPPoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1))
usdPPPoEIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1))
usdPPPoESubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2))
usdPPPoEGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3))
usdPPPoEProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4))
usdPPPoESummary = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5))
usdPPPoENextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoENextIfIndex.setStatus('current')
usdPPPoEIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2), )
if mibBuilder.loadTexts: usdPPPoEIfTable.setStatus('current')
usdPPPoEIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"))
if mibBuilder.loadTexts: usdPPPoEIfEntry.setStatus('current')
usdPPPoEIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfIfIndex.setStatus('current')
usdPPPoEIfMaxNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65335))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfMaxNumSessions.setStatus('current')
usdPPPoEIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfRowStatus.setStatus('current')
usdPPPoEIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfLowerIfIndex.setStatus('current')
usdPPPoEIfAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfAcName.setStatus('current')
usdPPPoEIfDupProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 6), UsdEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfDupProtect.setStatus('current')
usdPPPoEIfPADIFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 7), UsdEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfPADIFlag.setStatus('current')
usdPPPoEIfAutoconfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 8), UsdEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEIfAutoconfig.setStatus('current')
usdPPPoEIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3), )
if mibBuilder.loadTexts: usdPPPoEIfStatsTable.setStatus('current')
usdPPPoEIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1), ).setIndexNames((0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"))
if mibBuilder.loadTexts: usdPPPoEIfStatsEntry.setStatus('current')
usdPPPoEIfStatsRxPADI = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxPADI.setStatus('current')
usdPPPoEIfStatsTxPADO = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsTxPADO.setStatus('current')
usdPPPoEIfStatsRxPADR = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxPADR.setStatus('current')
usdPPPoEIfStatsTxPADS = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsTxPADS.setStatus('current')
usdPPPoEIfStatsRxPADT = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxPADT.setStatus('current')
usdPPPoEIfStatsTxPADT = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsTxPADT.setStatus('current')
usdPPPoEIfStatsRxInvVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvVersion.setStatus('current')
usdPPPoEIfStatsRxInvCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvCode.setStatus('current')
usdPPPoEIfStatsRxInvTags = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvTags.setStatus('current')
usdPPPoEIfStatsRxInvSession = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvSession.setStatus('current')
usdPPPoEIfStatsRxInvTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvTypes.setStatus('current')
usdPPPoEIfStatsRxInvPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInvPackets.setStatus('current')
usdPPPoEIfStatsRxInsufficientResources = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsRxInsufficientResources.setStatus('current')
usdPPPoEIfStatsTxPADM = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEIfStatsTxPADM.setStatus('current')
usdPPPoESubIfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESubIfNextIfIndex.setStatus('current')
usdPPPoESubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2), )
if mibBuilder.loadTexts: usdPPPoESubIfTable.setStatus('current')
usdPPPoESubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfIndex"))
if mibBuilder.loadTexts: usdPPPoESubIfEntry.setStatus('current')
usdPPPoESubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdPPPoESubIfIndex.setStatus('current')
usdPPPoESubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoESubIfRowStatus.setStatus('current')
usdPPPoESubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoESubIfLowerIfIndex.setStatus('current')
usdPPPoESubIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoESubIfId.setStatus('current')
usdPPPoESubIfSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESubIfSessionId.setStatus('current')
usdPPPoESubIfMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoESubIfMotm.setStatus('current')
usdPPPoESubIfUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoESubIfUrl.setStatus('current')
usdPPPoEGlobalMotm = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPPPoEGlobalMotm.setStatus('current')
usdPPPoEProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1), )
if mibBuilder.loadTexts: usdPPPoEProfileTable.setStatus('deprecated')
usdPPPoEProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1), ).setIndexNames((0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileIndex"))
if mibBuilder.loadTexts: usdPPPoEProfileEntry.setStatus('deprecated')
usdPPPoEProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdPPPoEProfileIndex.setStatus('deprecated')
usdPPPoEProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEProfileRowStatus.setStatus('deprecated')
usdPPPoEProfileMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEProfileMotm.setStatus('deprecated')
usdPPPoEProfileUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdPPPoEProfileUrl.setStatus('deprecated')
usdPPPoEMajorInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoEMajorInterfaceCount.setStatus('current')
usdPPPoESummaryMajorIfAdminUp = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfAdminUp.setStatus('current')
usdPPPoESummaryMajorIfAdminDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfAdminDown.setStatus('current')
usdPPPoESummaryMajorIfOperUp = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfOperUp.setStatus('current')
usdPPPoESummaryMajorIfOperDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfOperDown.setStatus('current')
usdPPPoESummaryMajorIfLowerLayerDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfLowerLayerDown.setStatus('current')
usdPPPoESummaryMajorIfNotPresent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummaryMajorIfNotPresent.setStatus('current')
usdPPPoESummarySubInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubInterfaceCount.setStatus('current')
usdPPPoESummarySubIfAdminUp = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfAdminUp.setStatus('current')
usdPPPoESummarySubIfAdminDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfAdminDown.setStatus('current')
usdPPPoESummarySubIfOperUp = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfOperUp.setStatus('current')
usdPPPoESummarySubIfOperDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfOperDown.setStatus('current')
usdPPPoESummarySubIfLowerLayerDown = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfLowerLayerDown.setStatus('current')
usdPPPoESummarySubIfNotPresent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdPPPoESummarySubIfNotPresent.setStatus('current')
usdPPPoEConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4))
usdPPPoECompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5))
usdPPPoEGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4))
usdPPPoECompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 1)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance = usdPPPoECompliance.setStatus('obsolete')
usdPPPoECompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 2)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance2 = usdPPPoECompliance2.setStatus('obsolete')
usdPPPoECompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 3)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileGroup"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance3 = usdPPPoECompliance3.setStatus('obsolete')
usdPPPoECompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 4)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance4 = usdPPPoECompliance4.setStatus('obsolete')
usdPPPoECompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 5)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup3"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance5 = usdPPPoECompliance5.setStatus('obsolete')
usdPPPoECompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 6)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEGroup4"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoECompliance6 = usdPPPoECompliance6.setStatus('current')
usdPPPoEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 1)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoEGroup = usdPPPoEGroup.setStatus('obsolete')
usdPPPoESubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 2)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfNextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfId"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfSessionId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoESubIfGroup = usdPPPoESubIfGroup.setStatus('obsolete')
usdPPPoEProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 3)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileUrl"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileMotm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoEProfileGroup = usdPPPoEProfileGroup.setStatus('deprecated')
usdPPPoEGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 4)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoEGroup2 = usdPPPoEGroup2.setStatus('obsolete')
usdPPPoESubIfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 5)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfNextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfId"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfSessionId"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfUrl"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfMotm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoESubIfGroup2 = usdPPPoESubIfGroup2.setStatus('current')
usdPPPoESummaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 6)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoEMajorInterfaceCount"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfAdminUp"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfAdminDown"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfOperUp"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfOperDown"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfNotPresent"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfLowerLayerDown"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubInterfaceCount"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfAdminUp"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfAdminDown"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfOperUp"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfOperDown"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfNotPresent"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfLowerLayerDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoESummaryGroup = usdPPPoESummaryGroup.setStatus('current')
usdPPPoEGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 7)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAcName"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfDupProtect"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoEGroup3 = usdPPPoEGroup3.setStatus('obsolete')
usdPPPoEGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 8)).setObjects(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAcName"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfDupProtect"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfPADIFlag"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAutoconfig"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"), ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPPPoEGroup4 = usdPPPoEGroup4.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPPOE-MIB", usdPPPoEIfIfIndex=usdPPPoEIfIfIndex, usdPPPoEProfileUrl=usdPPPoEProfileUrl, usdPPPoESubIfNextIfIndex=usdPPPoESubIfNextIfIndex, usdPPPoEIfStatsRxInvCode=usdPPPoEIfStatsRxInvCode, usdPPPoESubIfTable=usdPPPoESubIfTable, usdPPPoEGroup2=usdPPPoEGroup2, usdPPPoECompliance5=usdPPPoECompliance5, usdPPPoESummaryMajorIfOperUp=usdPPPoESummaryMajorIfOperUp, usdPPPoEGlobalMotm=usdPPPoEGlobalMotm, usdPPPoESummaryMajorIfLowerLayerDown=usdPPPoESummaryMajorIfLowerLayerDown, usdPPPoESubIfRowStatus=usdPPPoESubIfRowStatus, usdPPPoEIfDupProtect=usdPPPoEIfDupProtect, usdPPPoESubIfGroup=usdPPPoESubIfGroup, usdPPPoEIfAcName=usdPPPoEIfAcName, usdPPPoECompliances=usdPPPoECompliances, usdPPPoEIfStatsRxPADI=usdPPPoEIfStatsRxPADI, usdPPPoEIfStatsTxPADS=usdPPPoEIfStatsTxPADS, usdPPPoEIfPADIFlag=usdPPPoEIfPADIFlag, usdPPPoESubIfLayer=usdPPPoESubIfLayer, usdPPPoESummarySubIfLowerLayerDown=usdPPPoESummarySubIfLowerLayerDown, PYSNMP_MODULE_ID=usdPPPoEMIB, usdPPPoEIfStatsRxInvPackets=usdPPPoEIfStatsRxInvPackets, usdPPPoESummarySubIfNotPresent=usdPPPoESummarySubIfNotPresent, usdPPPoEProfileEntry=usdPPPoEProfileEntry, usdPPPoESummarySubIfAdminDown=usdPPPoESummarySubIfAdminDown, usdPPPoESubIfLowerIfIndex=usdPPPoESubIfLowerIfIndex, usdPPPoEGroup3=usdPPPoEGroup3, usdPPPoEIfLowerIfIndex=usdPPPoEIfLowerIfIndex, usdPPPoEIfStatsTable=usdPPPoEIfStatsTable, usdPPPoEIfStatsRxInvVersion=usdPPPoEIfStatsRxInvVersion, usdPPPoEProfile=usdPPPoEProfile, usdPPPoEIfStatsEntry=usdPPPoEIfStatsEntry, usdPPPoESubIfIndex=usdPPPoESubIfIndex, usdPPPoEIfStatsRxInvSession=usdPPPoEIfStatsRxInvSession, usdPPPoEProfileMotm=usdPPPoEProfileMotm, usdPPPoEProfileGroup=usdPPPoEProfileGroup, usdPPPoEMIB=usdPPPoEMIB, usdPPPoECompliance6=usdPPPoECompliance6, usdPPPoEIfStatsRxInvTypes=usdPPPoEIfStatsRxInvTypes, usdPPPoEGlobal=usdPPPoEGlobal, usdPPPoEProfileIndex=usdPPPoEProfileIndex, usdPPPoEObjects=usdPPPoEObjects, usdPPPoESummaryGroup=usdPPPoESummaryGroup, usdPPPoEIfStatsRxInsufficientResources=usdPPPoEIfStatsRxInsufficientResources, usdPPPoEGroups=usdPPPoEGroups, usdPPPoECompliance3=usdPPPoECompliance3, usdPPPoESubIfUrl=usdPPPoESubIfUrl, usdPPPoESummaryMajorIfAdminDown=usdPPPoESummaryMajorIfAdminDown, usdPPPoEIfTable=usdPPPoEIfTable, usdPPPoESummaryMajorIfOperDown=usdPPPoESummaryMajorIfOperDown, usdPPPoESummarySubIfAdminUp=usdPPPoESummarySubIfAdminUp, usdPPPoESubIfSessionId=usdPPPoESubIfSessionId, usdPPPoECompliance2=usdPPPoECompliance2, usdPPPoEIfStatsTxPADO=usdPPPoEIfStatsTxPADO, usdPPPoEProfileRowStatus=usdPPPoEProfileRowStatus, usdPPPoESubIfMotm=usdPPPoESubIfMotm, usdPPPoEIfEntry=usdPPPoEIfEntry, usdPPPoENextIfIndex=usdPPPoENextIfIndex, usdPPPoEIfAutoconfig=usdPPPoEIfAutoconfig, usdPPPoESummary=usdPPPoESummary, usdPPPoEMajorInterfaceCount=usdPPPoEMajorInterfaceCount, usdPPPoEIfStatsTxPADT=usdPPPoEIfStatsTxPADT, usdPPPoEIfMaxNumSessions=usdPPPoEIfMaxNumSessions, usdPPPoESummarySubIfOperUp=usdPPPoESummarySubIfOperUp, usdPPPoEGroup4=usdPPPoEGroup4, usdPPPoECompliance=usdPPPoECompliance, usdPPPoESummaryMajorIfAdminUp=usdPPPoESummaryMajorIfAdminUp, usdPPPoECompliance4=usdPPPoECompliance4, usdPPPoEIfStatsRxPADR=usdPPPoEIfStatsRxPADR, usdPPPoESummarySubInterfaceCount=usdPPPoESummarySubInterfaceCount, usdPPPoEIfStatsTxPADM=usdPPPoEIfStatsTxPADM, usdPPPoESubIfGroup2=usdPPPoESubIfGroup2, usdPPPoEConformance=usdPPPoEConformance, usdPPPoEIfStatsRxInvTags=usdPPPoEIfStatsRxInvTags, usdPPPoEGroup=usdPPPoEGroup, usdPPPoESummaryMajorIfNotPresent=usdPPPoESummaryMajorIfNotPresent, usdPPPoESubIfEntry=usdPPPoESubIfEntry, usdPPPoESummarySubIfOperDown=usdPPPoESummarySubIfOperDown, usdPPPoEIfLayer=usdPPPoEIfLayer, usdPPPoEIfRowStatus=usdPPPoEIfRowStatus, usdPPPoEProfileTable=usdPPPoEProfileTable, usdPPPoESubIfId=usdPPPoESubIfId, usdPPPoEIfStatsRxPADT=usdPPPoEIfStatsRxPADT)
