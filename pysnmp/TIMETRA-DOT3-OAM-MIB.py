#
# PySNMP MIB module TIMETRA-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
dot3OamEntry, dot3OamLoopbackEntry, dot3OamPeerMacAddress = mibBuilder.importSymbols("DOT3-OAM-MIB", "dot3OamEntry", "dot3OamLoopbackEntry", "dot3OamPeerMacAddress")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Counter32, iso, Bits, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "iso", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter64", "Integer32")
TruthValue, TextualConvention, RowStatus, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "TimeStamp", "DisplayString")
tmnxSRConfs, tmnxSRNotifyPrefix, timetraSRMIBModules, tmnxSRObjs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRConfs", "tmnxSRNotifyPrefix", "timetraSRMIBModules", "tmnxSRObjs")
timetraDOT3OAMMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 42))
timetraDOT3OAMMIBModule.setRevisions(('1908-07-01 00:00', '1908-01-01 00:00', '2006-08-01 00:00',))
if mibBuilder.loadTexts: timetraDOT3OAMMIBModule.setLastUpdated('0807010000Z')
if mibBuilder.loadTexts: timetraDOT3OAMMIBModule.setOrganization('Alcatel-Lucent')
tmnxDot3OamObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42))
tmnxDot3OamMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42))
tmnxDot3OamEntryObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1))
tmnxDot3OamLoopbackObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2))
tmnxDot3OamNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42))
tmnxDot3OamNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42))
tmnxDot3OamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0))
tmnxDot3OamTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1), )
if mibBuilder.loadTexts: tmnxDot3OamTable.setStatus('current')
tmnxDot3OamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1), )
dot3OamEntry.registerAugmentions(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamEntry"))
tmnxDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
if mibBuilder.loadTexts: tmnxDot3OamEntry.setStatus('current')
tmnxDot3OamLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxDot3OamLastChanged.setStatus('current')
tmnxDot3OamInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(10)).setUnits('100s of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxDot3OamInterval.setStatus('current')
tmnxDot3OamMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxDot3OamMultiplier.setStatus('current')
tmnxDot3OamTunneling = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxDot3OamTunneling.setStatus('current')
tmnxDot3OamLooped = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxDot3OamLooped.setStatus('current')
tmnxDot3OamHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxDot3OamHoldTime.setStatus('current')
tmnxDot3OamLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1), )
if mibBuilder.loadTexts: tmnxDot3OamLoopbackTable.setStatus('current')
tmnxDot3OamLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1), )
dot3OamLoopbackEntry.registerAugmentions(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackEntry"))
tmnxDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
if mibBuilder.loadTexts: tmnxDot3OamLoopbackEntry.setStatus('current')
tmnxDot3OamLoopbackLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxDot3OamLoopbackLastChanged.setStatus('current')
tmnxDot3OamLoopbackLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noLoopback", 1), ("localLoopback", 2))).clone('noLoopback')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxDot3OamLoopbackLocalStatus.setStatus('current')
tmnxDot3OamPeerChanged = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 1)).setObjects(("DOT3-OAM-MIB", "dot3OamPeerMacAddress"))
if mibBuilder.loadTexts: tmnxDot3OamPeerChanged.setStatus('current')
tmnxDot3OamLoopDetected = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tmnxDot3OamLoopDetected.setStatus('current')
tmnxDot3OamLoopCleared = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tmnxDot3OamLoopCleared.setStatus('current')
tmnxDot3OamMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1))
tmnxDot3OamMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2))
tmnxDot3OamMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 1)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGroup"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamMIBCompliance = tmnxDot3OamMIBCompliance.setStatus('obsolete')
tmnxDot3OamMIBV6v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 2)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamMIBV6v0Compliance = tmnxDot3OamMIBV6v0Compliance.setStatus('obsolete')
tmnxDot3OamMIBV6v1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 3)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v1Group"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamMIBV6v1Compliance = tmnxDot3OamMIBV6v1Compliance.setStatus('current')
tmnxDot3OamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 1)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamGroup = tmnxDot3OamGroup.setStatus('obsolete')
tmnxDot3OamLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 2)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLastChanged"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLocalStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamLoopbackGroup = tmnxDot3OamLoopbackGroup.setStatus('current')
tmnxDot3OamNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 3)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamNotificationGroup = tmnxDot3OamNotificationGroup.setStatus('obsolete')
tmnxDot3OamNotificationV6v0Group = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 4)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopDetected"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamNotificationV6v0Group = tmnxDot3OamNotificationV6v0Group.setStatus('current')
tmnxDot3OamV6v0Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 5)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"), ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLooped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamV6v0Group = tmnxDot3OamV6v0Group.setStatus('current')
tmnxDot3OamV6v1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 6)).setObjects(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxDot3OamV6v1Group = tmnxDot3OamV6v1Group.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-DOT3-OAM-MIB", PYSNMP_MODULE_ID=timetraDOT3OAMMIBModule, tmnxDot3OamLoopbackLocalStatus=tmnxDot3OamLoopbackLocalStatus, tmnxDot3OamPeerChanged=tmnxDot3OamPeerChanged, tmnxDot3OamMIBV6v0Compliance=tmnxDot3OamMIBV6v0Compliance, tmnxDot3OamTable=tmnxDot3OamTable, tmnxDot3OamMultiplier=tmnxDot3OamMultiplier, tmnxDot3OamNotificationGroup=tmnxDot3OamNotificationGroup, tmnxDot3OamLoopbackObjs=tmnxDot3OamLoopbackObjs, timetraDOT3OAMMIBModule=timetraDOT3OAMMIBModule, tmnxDot3OamLoopbackGroup=tmnxDot3OamLoopbackGroup, tmnxDot3OamInterval=tmnxDot3OamInterval, tmnxDot3OamV6v1Group=tmnxDot3OamV6v1Group, tmnxDot3OamLoopbackEntry=tmnxDot3OamLoopbackEntry, tmnxDot3OamEntry=tmnxDot3OamEntry, tmnxDot3OamLoopCleared=tmnxDot3OamLoopCleared, tmnxDot3OamMIBConformance=tmnxDot3OamMIBConformance, tmnxDot3OamNotificationsPrefix=tmnxDot3OamNotificationsPrefix, tmnxDot3OamLoopbackLastChanged=tmnxDot3OamLoopbackLastChanged, tmnxDot3OamLoopDetected=tmnxDot3OamLoopDetected, tmnxDot3OamNotifyPrefix=tmnxDot3OamNotifyPrefix, tmnxDot3OamMIBCompliance=tmnxDot3OamMIBCompliance, tmnxDot3OamNotificationV6v0Group=tmnxDot3OamNotificationV6v0Group, tmnxDot3OamLoopbackTable=tmnxDot3OamLoopbackTable, tmnxDot3OamGroup=tmnxDot3OamGroup, tmnxDot3OamEntryObjs=tmnxDot3OamEntryObjs, tmnxDot3OamMIBGroups=tmnxDot3OamMIBGroups, tmnxDot3OamTunneling=tmnxDot3OamTunneling, tmnxDot3OamObjs=tmnxDot3OamObjs, tmnxDot3OamHoldTime=tmnxDot3OamHoldTime, tmnxDot3OamV6v0Group=tmnxDot3OamV6v0Group, tmnxDot3OamLooped=tmnxDot3OamLooped, tmnxDot3OamNotifications=tmnxDot3OamNotifications, tmnxDot3OamMIBCompliances=tmnxDot3OamMIBCompliances, tmnxDot3OamLastChanged=tmnxDot3OamLastChanged, tmnxDot3OamMIBV6v1Compliance=tmnxDot3OamMIBV6v1Compliance)