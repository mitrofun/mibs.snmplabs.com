#
# PySNMP MIB module PDN-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_devConfig, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-devConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, NotificationType, Unsigned32, Gauge32, TimeTicks, IpAddress, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "Bits", "MibIdentifier")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
devConfigArea = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1))
devConfigAreaCopy = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))).clone(namedValues=NamedValues(("noOp", 1), ("active-to-customer1", 2), ("active-to-customer2", 3), ("customer1-to-active", 4), ("customer1-to-customer2", 5), ("customer2-to-active", 6), ("customer2-to-customer1", 7), ("factory1-to-active", 8), ("factory1-to-customer1", 9), ("factory1-to-customer2", 10), ("factory2-to-active", 11), ("factory2-to-customer1", 12), ("factory2-to-customer2", 13), ("factory3-to-active", 14), ("factory3-to-customer1", 15), ("factory3-to-customer2", 16), ("factory4-to-active", 17), ("factory4-to-customer1", 18), ("factory4-to-customer2", 19), ("factory5-to-active", 20), ("factory5-to-customer1", 21), ("factory5-to-customer2", 22), ("factory6-to-active", 23), ("factory6-to-customer1", 24), ("factory6-to-customer2", 25), ("factory7-to-active", 26), ("factory7-to-customer1", 27), ("factory7-to-customer2", 28), ("factory8-to-active", 29), ("factory8-to-customer1", 30), ("factory8-to-customer2", 31), ("factory9-to-active", 32), ("factory9-to-customer1", 33), ("factory9-to-customer2", 34)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigAreaCopy.setStatus('mandatory')
devConfigTestTimer = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2))
devConfigTestTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTestTimeout.setStatus('mandatory')
devConfigTestDuration = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTestDuration.setStatus('mandatory')
devConfigClockSrc = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3))
devConfigClockSrcTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1), )
if mibBuilder.loadTexts: devConfigClockSrcTable.setStatus('mandatory')
devConfigClockSrcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devCfgClkWhichSrc"))
if mibBuilder.loadTexts: devConfigClockSrcEntry.setStatus('mandatory')
devCfgClkWhichSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgClkWhichSrc.setStatus('mandatory')
devCfgClkSource = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("interface", 3), ("dbm", 4), ("external2", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkSource.setStatus('mandatory')
devCfgClkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkIfIndex.setStatus('mandatory')
devCfgClkRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rate400Hz", 1), ("rate8KHz", 2), ("rate64KHz", 3), ("rate1544KHz", 4), ("rate2048KHz", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkRate.setStatus('mandatory')
devConfigTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4))
devConfigTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTrapEnable.setStatus('mandatory')
cCNTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cCNTrapEnable.setStatus('mandatory')
devConfigAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5))
devConfigAlarmRelayCutoff = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigAlarmRelayCutoff.setStatus('mandatory')
devConfigCardType = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6))
devConfigCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7), )
if mibBuilder.loadTexts: devConfigCardTypeTable.setStatus('mandatory')
devConfigCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devCfgCardSlot"))
if mibBuilder.loadTexts: devConfigCardTypeEntry.setStatus('mandatory')
devCfgCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardSlot.setStatus('mandatory')
devCfgCardConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("emptySlot", 1), ("unsupportedAPM", 2), ("t1NAM", 3), ("syncDataAPM", 4), ("voiceFxsAPM", 5), ("voiceEmAPM", 6), ("voiceFxoAPM", 7), ("dsxAPM", 8), ("t1NoDsxNAM", 9), ("misconfiguredAPM", 10), ("ocu2APM", 11), ("ocu6APM", 12), ("dce6APM", 13), ("sruAPM", 14), ("ocu4APM", 15), ("pktVoiceAPM", 16), ("acceptingAPM", 17), ("failedAPM", 18), ("dpNAM", 19), ("stNAM", 20), ("ddsNAM", 21), ("dualDsxNniNAM", 22), ("t3NniNAM", 23), ("t3NAM", 24), ("dslNAM", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardConfig.setStatus('mandatory')
devCfgCardActual = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("emptySlot", 1), ("unsupportedAPM", 2), ("t1NAM", 3), ("syncDataAPM", 4), ("voiceFxsAPM", 5), ("voiceEmAPM", 6), ("voiceFxoAPM", 7), ("voiceDsxAPM", 8), ("t1NoDsxNAM", 9), ("misconfigured", 10), ("ocu2APM", 11), ("ocu6APM", 12), ("dce6APM", 13), ("sruAPM", 14), ("ocu4APM", 15), ("pktVoiceAPM", 16), ("acceptingAPM", 17), ("failedAPM", 18), ("dpNAM", 19), ("stNAM", 20), ("ddsNAM", 21), ("dualDsxNniNAM", 22), ("t3NniNAM", 23), ("t3NAM", 24), ("dslNAM", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardActual.setStatus('mandatory')
devCfgCardAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("accept", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgCardAction.setStatus('mandatory')
devConfigNetSync = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7))
devConfigNetSyncRole = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("tributary", 2), ("controller", 3))).clone('tributary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigNetSyncRole.setStatus('mandatory')
devConfigTime = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8))
devConfigTimeOfDay = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTimeOfDay.setStatus('mandatory')
devConfigChangeKeys = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9))
devConfigChangeKeysTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1), )
if mibBuilder.loadTexts: devConfigChangeKeysTable.setStatus('mandatory')
devConfigChangeKeysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devConfigChangeKeysDbType"))
if mibBuilder.loadTexts: devConfigChangeKeysEntry.setStatus('mandatory')
devConfigChangeKeysDbType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generalConfig", 1), ("rmonAlarm", 2), ("rmonUserHistory", 3), ("routerConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devConfigChangeKeysDbType.setStatus('mandatory')
devConfigChangeKeysDbKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devConfigChangeKeysDbKey.setStatus('mandatory')
devConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10))
devConfigComDiscTime = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigComDiscTime.setStatus('mandatory')
devConfigPortNumDisplayFormat = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sle", 1), ("unitport", 2), ("name", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigPortNumDisplayFormat.setStatus('mandatory')
devConfigDateDisplayFormat = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ddmmyy", 1), ("mmddyy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigDateDisplayFormat.setStatus('mandatory')
devAcceptRemoteResetFrame = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAcceptRemoteResetFrame.setStatus('mandatory')
cCN = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
mibBuilder.exportSymbols("PDN-CONFIG-MIB", devConfigPortNumDisplayFormat=devConfigPortNumDisplayFormat, devConfigChangeKeysDbType=devConfigChangeKeysDbType, devConfigDateDisplayFormat=devConfigDateDisplayFormat, cCNTrapEnable=cCNTrapEnable, devConfigChangeKeysTable=devConfigChangeKeysTable, devConfigClockSrc=devConfigClockSrc, devCfgClkSource=devCfgClkSource, devCfgCardConfig=devCfgCardConfig, devConfigTimeOfDay=devConfigTimeOfDay, devCfgCardAction=devCfgCardAction, devConfigTestDuration=devConfigTestDuration, devConfigTestTimer=devConfigTestTimer, devCfgClkWhichSrc=devCfgClkWhichSrc, devConfigCardTypeEntry=devConfigCardTypeEntry, devConfigChangeKeys=devConfigChangeKeys, devConfigTestTimeout=devConfigTestTimeout, devConfigTrap=devConfigTrap, devConfigArea=devConfigArea, devConfiguration=devConfiguration, devCfgCardSlot=devCfgCardSlot, devCfgCardActual=devCfgCardActual, devConfigClockSrcTable=devConfigClockSrcTable, devConfigAreaCopy=devConfigAreaCopy, devConfigNetSyncRole=devConfigNetSyncRole, cCN=cCN, devConfigAlarm=devConfigAlarm, devConfigNetSync=devConfigNetSync, devCfgClkRate=devCfgClkRate, devCfgClkIfIndex=devCfgClkIfIndex, devConfigComDiscTime=devConfigComDiscTime, devConfigChangeKeysDbKey=devConfigChangeKeysDbKey, devConfigCardTypeTable=devConfigCardTypeTable, devConfigClockSrcEntry=devConfigClockSrcEntry, devConfigTime=devConfigTime, devConfigAlarmRelayCutoff=devConfigAlarmRelayCutoff, devConfigTrapEnable=devConfigTrapEnable, devConfigCardType=devConfigCardType, devAcceptRemoteResetFrame=devAcceptRemoteResetFrame, devConfigChangeKeysEntry=devConfigChangeKeysEntry)
