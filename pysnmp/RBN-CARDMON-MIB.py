#
# PySNMP MIB module RBN-CARDMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-CARDMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
RbnAlarmPerceivedSeverity, RbnAlarmType, RbnAlarmServiceAffecting, RbnAlarmId, RbnAlarmProbableCause = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmPerceivedSeverity", "RbnAlarmType", "RbnAlarmServiceAffecting", "RbnAlarmId", "RbnAlarmProbableCause")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnSlot, = mibBuilder.importSymbols("RBN-TC", "RbnSlot")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Gauge32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, Counter64, Unsigned32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "Unsigned32", "iso", "TimeTicks")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rbnCardMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 31))
rbnCardMonMIB.setRevisions(('2006-10-02 00:00', '2005-05-09 00:00', '2004-09-27 00:00', '2004-06-29 00:00',))
if mibBuilder.loadTexts: rbnCardMonMIB.setLastUpdated('200610020000Z')
if mibBuilder.loadTexts: rbnCardMonMIB.setOrganization('RedBack Networks, Inc.')
rbnCardMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 31, 0))
rbnCardMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1))
rbnCardMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2))
rbnCardAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1), )
if mibBuilder.loadTexts: rbnCardAlarmActiveTable.setStatus('current')
rbnCardAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1), ).setIndexNames((0, "RBN-CARDMON-MIB", "rbnCardAlarmSlot"), (0, "RBN-CARDMON-MIB", "rbnCardAlarmActiveIndex"))
if mibBuilder.loadTexts: rbnCardAlarmActiveEntry.setStatus('current')
rbnCardAlarmSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnCardAlarmSlot.setStatus('current')
rbnCardAlarmActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rbnCardAlarmActiveIndex.setStatus('current')
rbnCardAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 3), RbnAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmId.setStatus('current')
rbnCardAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 4), RbnAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmType.setStatus('current')
rbnCardAlarmDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmDateAndTime.setStatus('current')
rbnCardAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmDescription.setStatus('current')
rbnCardAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 7), RbnAlarmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmProbableCause.setStatus('current')
rbnCardAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 8), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmSeverity.setStatus('current')
rbnCardAlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 9), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardAlarmServiceAffecting.setStatus('current')
rbnCardStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2), )
if mibBuilder.loadTexts: rbnCardStatsTable.setStatus('current')
rbnCardStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1), ).setIndexNames((0, "RBN-CARDMON-MIB", "rbnCardStatsSlot"))
if mibBuilder.loadTexts: rbnCardStatsEntry.setStatus('current')
rbnCardStatsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnCardStatsSlot.setStatus('current')
rbnCardStatsTotalCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsTotalCircuits.setStatus('current')
rbnCardStatsUpCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsUpCircuits.setStatus('current')
rbnCardStatsDownCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsDownCircuits.setStatus('current')
rbnCardStatsUnboundCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsUnboundCircuits.setStatus('current')
rbnCardStatsNoBindCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsNoBindCircuits.setStatus('current')
rbnCardStatsBindTotalCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsBindTotalCircuits.setStatus('current')
rbnCardStatsBindIfCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsBindIfCircuits.setStatus('current')
rbnCardStatsBindAuthCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsBindAuthCircuits.setStatus('current')
rbnCardStatsBindSubCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsBindSubCircuits.setStatus('current')
rbnCardStatsAtmCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsAtmCircuits.setStatus('current')
rbnCardStatsEthCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsEthCircuits.setStatus('current')
rbnCardStatsPppCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsPppCircuits.setStatus('current')
rbnCardStatsPppoeCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsPppoeCircuits.setStatus('current')
rbnCardStatsDot1qCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsDot1qCircuits.setStatus('current')
rbnCardStatsFrCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsFrCircuits.setStatus('current')
rbnCardStatsChdlcCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsChdlcCircuits.setStatus('current')
rbnCardStatsGreCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsGreCircuits.setStatus('current')
rbnCardStatsMplsCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsMplsCircuits.setStatus('current')
rbnCardStatsClipsCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsClipsCircuits.setStatus('current')
rbnCardStatsVplsCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsVplsCircuits.setStatus('current')
rbnCardStatsIpipCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsIpipCircuits.setStatus('current')
rbnCardStatsIpv6v4ManualCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsIpv6v4ManualCircuits.setStatus('current')
rbnCardStatsIpv6v4AutoCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCardStatsIpv6v4AutoCircuits.setStatus('current')
rbnCardAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 31, 0, 1)).setObjects(("RBN-CARDMON-MIB", "rbnCardAlarmId"), ("RBN-CARDMON-MIB", "rbnCardAlarmType"), ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"), ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"), ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"), ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"))
if mibBuilder.loadTexts: rbnCardAlarm.setStatus('current')
rbnCardMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1))
rbnCardMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2))
rbnCardMonMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 1)).setObjects(("RBN-CARDMON-MIB", "rbnCardAlarmId"), ("RBN-CARDMON-MIB", "rbnCardAlarmType"), ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"), ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"), ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"), ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBObjectGroup = rbnCardMonMIBObjectGroup.setStatus('current')
rbnCardMonMIBObjectGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 4)).setObjects(("RBN-CARDMON-MIB", "rbnCardAlarmId"), ("RBN-CARDMON-MIB", "rbnCardAlarmType"), ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"), ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"), ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"), ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"), ("RBN-CARDMON-MIB", "rbnCardAlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBObjectGroup2 = rbnCardMonMIBObjectGroup2.setStatus('current')
rbnCardMonMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 2)).setObjects(("RBN-CARDMON-MIB", "rbnCardAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBNotificationGroup = rbnCardMonMIBNotificationGroup.setStatus('current')
rbnCardStatsMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 3)).setObjects(("RBN-CARDMON-MIB", "rbnCardStatsTotalCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsUpCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsDownCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsUnboundCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsNoBindCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindTotalCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindIfCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindAuthCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindSubCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsAtmCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsEthCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsPppCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsPppoeCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsDot1qCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsFrCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsChdlcCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsGreCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsMplsCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsClipsCircuits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardStatsMIBObjectGroup = rbnCardStatsMIBObjectGroup.setStatus('current')
rbnCardStatsMIBObjectGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 5)).setObjects(("RBN-CARDMON-MIB", "rbnCardStatsTotalCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsUpCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsDownCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsUnboundCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsNoBindCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindTotalCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindIfCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindAuthCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsBindSubCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsAtmCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsEthCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsPppCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsPppoeCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsDot1qCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsFrCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsChdlcCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsGreCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsMplsCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsClipsCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsVplsCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsIpipCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsIpv6v4ManualCircuits"), ("RBN-CARDMON-MIB", "rbnCardStatsIpv6v4AutoCircuits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardStatsMIBObjectGroup2 = rbnCardStatsMIBObjectGroup2.setStatus('current')
rbnCardMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 1)).setObjects(("RBN-CARDMON-MIB", "rbnCardMonMIBObjectGroup"), ("RBN-CARDMON-MIB", "rbnCardMonMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBCompliance = rbnCardMonMIBCompliance.setStatus('current')
rbnCardMonMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 2)).setObjects(("RBN-CARDMON-MIB", "rbnCardMonMIBObjectGroup"), ("RBN-CARDMON-MIB", "rbnCardMonMIBNotificationGroup"), ("RBN-CARDMON-MIB", "rbnCardStatsMIBObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBCompliance2 = rbnCardMonMIBCompliance2.setStatus('current')
rbnCardMonMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 3)).setObjects(("RBN-CARDMON-MIB", "rbnCardMonMIBObjectGroup2"), ("RBN-CARDMON-MIB", "rbnCardMonMIBNotificationGroup"), ("RBN-CARDMON-MIB", "rbnCardStatsMIBObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBCompliance3 = rbnCardMonMIBCompliance3.setStatus('current')
rbnCardMonMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 4)).setObjects(("RBN-CARDMON-MIB", "rbnCardMonMIBObjectGroup2"), ("RBN-CARDMON-MIB", "rbnCardMonMIBNotificationGroup"), ("RBN-CARDMON-MIB", "rbnCardStatsMIBObjectGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCardMonMIBCompliance4 = rbnCardMonMIBCompliance4.setStatus('current')
mibBuilder.exportSymbols("RBN-CARDMON-MIB", rbnCardAlarmSlot=rbnCardAlarmSlot, rbnCardStatsEntry=rbnCardStatsEntry, rbnCardStatsBindIfCircuits=rbnCardStatsBindIfCircuits, rbnCardAlarmServiceAffecting=rbnCardAlarmServiceAffecting, rbnCardStatsMIBObjectGroup2=rbnCardStatsMIBObjectGroup2, rbnCardStatsDownCircuits=rbnCardStatsDownCircuits, rbnCardStatsSlot=rbnCardStatsSlot, rbnCardStatsEthCircuits=rbnCardStatsEthCircuits, rbnCardMonMIBObjectGroup2=rbnCardMonMIBObjectGroup2, rbnCardMonMIBCompliance4=rbnCardMonMIBCompliance4, rbnCardStatsBindAuthCircuits=rbnCardStatsBindAuthCircuits, rbnCardStatsAtmCircuits=rbnCardStatsAtmCircuits, rbnCardMonMIBNotifications=rbnCardMonMIBNotifications, rbnCardStatsClipsCircuits=rbnCardStatsClipsCircuits, rbnCardMonMIBObjectGroup=rbnCardMonMIBObjectGroup, rbnCardStatsGreCircuits=rbnCardStatsGreCircuits, rbnCardStatsChdlcCircuits=rbnCardStatsChdlcCircuits, rbnCardStatsBindTotalCircuits=rbnCardStatsBindTotalCircuits, rbnCardStatsFrCircuits=rbnCardStatsFrCircuits, rbnCardAlarmActiveEntry=rbnCardAlarmActiveEntry, rbnCardStatsUpCircuits=rbnCardStatsUpCircuits, rbnCardAlarm=rbnCardAlarm, rbnCardStatsDot1qCircuits=rbnCardStatsDot1qCircuits, rbnCardAlarmActiveTable=rbnCardAlarmActiveTable, rbnCardStatsBindSubCircuits=rbnCardStatsBindSubCircuits, rbnCardMonMIBNotificationGroup=rbnCardMonMIBNotificationGroup, rbnCardStatsTotalCircuits=rbnCardStatsTotalCircuits, rbnCardAlarmProbableCause=rbnCardAlarmProbableCause, PYSNMP_MODULE_ID=rbnCardMonMIB, rbnCardStatsPppoeCircuits=rbnCardStatsPppoeCircuits, rbnCardStatsTable=rbnCardStatsTable, rbnCardMonMIBCompliance2=rbnCardMonMIBCompliance2, rbnCardStatsUnboundCircuits=rbnCardStatsUnboundCircuits, rbnCardStatsIpv6v4ManualCircuits=rbnCardStatsIpv6v4ManualCircuits, rbnCardAlarmType=rbnCardAlarmType, rbnCardStatsNoBindCircuits=rbnCardStatsNoBindCircuits, rbnCardStatsVplsCircuits=rbnCardStatsVplsCircuits, rbnCardMonMIB=rbnCardMonMIB, rbnCardMonMIBCompliances=rbnCardMonMIBCompliances, rbnCardAlarmSeverity=rbnCardAlarmSeverity, rbnCardMonMIBObjects=rbnCardMonMIBObjects, rbnCardMonMIBCompliance=rbnCardMonMIBCompliance, rbnCardAlarmDateAndTime=rbnCardAlarmDateAndTime, rbnCardStatsPppCircuits=rbnCardStatsPppCircuits, rbnCardStatsIpipCircuits=rbnCardStatsIpipCircuits, rbnCardAlarmDescription=rbnCardAlarmDescription, rbnCardMonMIBGroups=rbnCardMonMIBGroups, rbnCardAlarmId=rbnCardAlarmId, rbnCardStatsMplsCircuits=rbnCardStatsMplsCircuits, rbnCardStatsMIBObjectGroup=rbnCardStatsMIBObjectGroup, rbnCardStatsIpv6v4AutoCircuits=rbnCardStatsIpv6v4AutoCircuits, rbnCardMonMIBConformance=rbnCardMonMIBConformance, rbnCardMonMIBCompliance3=rbnCardMonMIBCompliance3, rbnCardAlarmActiveIndex=rbnCardAlarmActiveIndex)
