#
# PySNMP MIB module TIMETRA-CLEAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-CLEAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Bits, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, Unsigned32, Counter32, ObjectIdentity, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
tmnxSRNotifyPrefix, tmnxSRObjs, tmnxSRConfs, timetraSRMIBModules = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRNotifyPrefix", "tmnxSRObjs", "tmnxSRConfs", "timetraSRMIBModules")
tmnxEventAppIndex, = mibBuilder.importSymbols("TIMETRA-LOG-MIB", "tmnxEventAppIndex")
TmnxActionType, TNamedItem = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxActionType", "TNamedItem")
timetraClearMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 13))
timetraClearMIBModule.setRevisions(('1905-01-24 00:00', '1904-06-02 00:00', '1904-01-15 00:00', '1903-08-15 00:00', '1903-01-20 00:00', '1902-02-27 00:00',))
if mibBuilder.loadTexts: timetraClearMIBModule.setLastUpdated('0501240000Z')
if mibBuilder.loadTexts: timetraClearMIBModule.setOrganization('Alcatel-Lucent')
tmnxClearObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13))
tmnxClearNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13))
tmnxClearNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13, 0))
tmnxClearConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13))
tmnxClearTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1), )
if mibBuilder.loadTexts: tmnxClearTable.setStatus('current')
tmnxClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1), ).setIndexNames((0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"), (0, "TIMETRA-CLEAR-MIB", "tmnxClearIndex"))
if mibBuilder.loadTexts: tmnxClearEntry.setStatus('current')
tmnxClearIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: tmnxClearIndex.setStatus('current')
tmnxClearName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 2), TNamedItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxClearName.setStatus('current')
tmnxClearParams = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxClearParams.setStatus('current')
tmnxClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 4), TmnxActionType().clone('notApplicable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxClearAction.setStatus('current')
tmnxClearLastClearedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxClearLastClearedTime.setStatus('current')
tmnxClearResult = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxClearResult.setStatus('current')
tmnxClearErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxClearErrorText.setStatus('current')
tmnxClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13, 0, 1)).setObjects(("TIMETRA-CLEAR-MIB", "tmnxClearName"), ("TIMETRA-CLEAR-MIB", "tmnxClearParams"), ("TIMETRA-CLEAR-MIB", "tmnxClearLastClearedTime"), ("TIMETRA-CLEAR-MIB", "tmnxClearResult"), ("TIMETRA-CLEAR-MIB", "tmnxClearErrorText"))
if mibBuilder.loadTexts: tmnxClear.setStatus('current')
tmnxClearCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 1))
tmnxClearGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2))
tmnxClearCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 1, 1)).setObjects(("TIMETRA-CLEAR-MIB", "tmnxClearGroup"), ("TIMETRA-CLEAR-MIB", "tmnxClearNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxClearCompliance = tmnxClearCompliance.setStatus('current')
tmnxClearGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2, 1)).setObjects(("TIMETRA-CLEAR-MIB", "tmnxClearName"), ("TIMETRA-CLEAR-MIB", "tmnxClearParams"), ("TIMETRA-CLEAR-MIB", "tmnxClearAction"), ("TIMETRA-CLEAR-MIB", "tmnxClearLastClearedTime"), ("TIMETRA-CLEAR-MIB", "tmnxClearResult"), ("TIMETRA-CLEAR-MIB", "tmnxClearErrorText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxClearGroup = tmnxClearGroup.setStatus('current')
tmnxClearNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2, 2)).setObjects(("TIMETRA-CLEAR-MIB", "tmnxClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxClearNotificationGroup = tmnxClearNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-CLEAR-MIB", tmnxClearName=tmnxClearName, tmnxClearAction=tmnxClearAction, tmnxClearGroups=tmnxClearGroups, tmnxClearCompliance=tmnxClearCompliance, tmnxClearCompliances=tmnxClearCompliances, timetraClearMIBModule=timetraClearMIBModule, tmnxClearLastClearedTime=tmnxClearLastClearedTime, tmnxClear=tmnxClear, tmnxClearParams=tmnxClearParams, tmnxClearNotifications=tmnxClearNotifications, tmnxClearResult=tmnxClearResult, PYSNMP_MODULE_ID=timetraClearMIBModule, tmnxClearTable=tmnxClearTable, tmnxClearNotificationsPrefix=tmnxClearNotificationsPrefix, tmnxClearObjs=tmnxClearObjs, tmnxClearConformance=tmnxClearConformance, tmnxClearErrorText=tmnxClearErrorText, tmnxClearNotificationGroup=tmnxClearNotificationGroup, tmnxClearEntry=tmnxClearEntry, tmnxClearIndex=tmnxClearIndex, tmnxClearGroup=tmnxClearGroup)