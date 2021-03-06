#
# PySNMP MIB module RBN-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
radiusAccClientServerPortNumber, radiusAccServerEntry, radiusAccServerAddress = mibBuilder.importSymbols("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber", "radiusAccServerEntry", "radiusAccServerAddress")
radiusAuthClientServerPortNumber, radiusAuthServerEntry, radiusAuthServerAddress = mibBuilder.importSymbols("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber", "radiusAuthServerEntry", "radiusAuthServerAddress")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Gauge32, IpAddress, Bits, Integer32, iso, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "Integer32", "iso", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64")
TextualConvention, DisplayString, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue")
rbnRadiusMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 32))
rbnRadiusMib.setRevisions(('2005-03-29 17:00', '2003-12-16 00:00',))
if mibBuilder.loadTexts: rbnRadiusMib.setLastUpdated('200503291700Z')
if mibBuilder.loadTexts: rbnRadiusMib.setOrganization('RedBack Networks, Inc.')
rbnRadiusMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 0))
rbnRadiusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1))
rbnRadiusMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2))
rbnRadiusAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1))
rbnRadiusAcctObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2))
rbnRadiusNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3))
class RbnRadiusServerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("down", 3))

class RbnRadiusServerReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("responding", 1), ("packetTimeout", 2), ("serverTimeout", 3), ("portDown", 4))

rbnRadiusAuthPktTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAuthPktTimeout.setStatus('current')
rbnRadiusAuthSrvTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAuthSrvTimeout.setStatus('current')
rbnRadiusAuthDeadtime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAuthDeadtime.setStatus('current')
rbnRadiusAuthTries = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('tries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAuthTries.setStatus('current')
rbnRadiusAuthStripDomain = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAuthStripDomain.setStatus('current')
rbnRadiusAuthSrvTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5), )
if mibBuilder.loadTexts: rbnRadiusAuthSrvTable.setStatus('current')
rbnRadiusAuthSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1), )
radiusAuthServerEntry.registerAugmentions(("RBN-RADIUS-MIB", "rbnRadiusAuthSrvEntry"))
rbnRadiusAuthSrvEntry.setIndexNames(*radiusAuthServerEntry.getIndexNames())
if mibBuilder.loadTexts: rbnRadiusAuthSrvEntry.setStatus('current')
rbnRadiusAuthSrvState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 1), RbnRadiusServerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAuthSrvState.setStatus('current')
rbnRadiusAuthSrvLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAuthSrvLastChange.setStatus('current')
rbnRadiusAuthSrvCounterResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAuthSrvCounterResetTime.setStatus('current')
rbnRadiusAuthSrvSendErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAuthSrvSendErrors.setStatus('current')
rbnRadiusAcctPktTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAcctPktTimeout.setStatus('current')
rbnRadiusAcctSrvTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAcctSrvTimeout.setStatus('current')
rbnRadiusAcctDeadtime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAcctDeadtime.setStatus('current')
rbnRadiusAcctTries = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('retries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAcctTries.setStatus('current')
rbnRadiusAcctStripDomain = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnRadiusAcctStripDomain.setStatus('current')
rbnRadiusAcctSrvTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5), )
if mibBuilder.loadTexts: rbnRadiusAcctSrvTable.setStatus('current')
rbnRadiusAcctSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1), )
radiusAccServerEntry.registerAugmentions(("RBN-RADIUS-MIB", "rbnRadiusAcctSrvEntry"))
rbnRadiusAcctSrvEntry.setIndexNames(*radiusAccServerEntry.getIndexNames())
if mibBuilder.loadTexts: rbnRadiusAcctSrvEntry.setStatus('current')
rbnRadiusAcctSrvState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 1), RbnRadiusServerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAcctSrvState.setStatus('current')
rbnRadiusAcctSrvLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAcctSrvLastChange.setStatus('current')
rbnRadiusAcctSrvCounterResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAcctSrvCounterResetTime.setStatus('current')
rbnRadiusAcctSrvSendErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnRadiusAcctSrvSendErrors.setStatus('current')
rbnRadiusClientPort = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1024, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnRadiusClientPort.setStatus('current')
rbnRadiusContext = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnRadiusContext.setStatus('current')
rbnRadiusReason = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 3), RbnRadiusServerReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnRadiusReason.setStatus('current')
rbnRadiusUsername = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnRadiusUsername.setStatus('current')
rbnRadiusAuthStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 32, 0, 1)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RBN-RADIUS-MIB", "rbnRadiusClientPort"), ("RBN-RADIUS-MIB", "rbnRadiusContext"), ("RBN-RADIUS-MIB", "rbnRadiusReason"), ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
if mibBuilder.loadTexts: rbnRadiusAuthStateChange.setStatus('current')
rbnRadiusAcctStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 32, 0, 2)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("RBN-RADIUS-MIB", "rbnRadiusClientPort"), ("RBN-RADIUS-MIB", "rbnRadiusContext"), ("RBN-RADIUS-MIB", "rbnRadiusReason"), ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
if mibBuilder.loadTexts: rbnRadiusAcctStateChange.setStatus('current')
rbnRadiusCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1))
rbnRadiusGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2))
rbnRadiusCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1, 2)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthGroup2"), ("RBN-RADIUS-MIB", "rbnRadiusAcctGroup2"), ("RBN-RADIUS-MIB", "rbnRadiusNotifyGroup"), ("RBN-RADIUS-MIB", "rbnRadiusAuthNotifyGroup"), ("RBN-RADIUS-MIB", "rbnRadiusAcctNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusCompliance2 = rbnRadiusCompliance2.setStatus('current')
rbnRadiusAuthGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 6)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthPktTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAuthDeadtime"), ("RBN-RADIUS-MIB", "rbnRadiusAuthTries"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvLastChange"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvCounterResetTime"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvSendErrors"), ("RBN-RADIUS-MIB", "rbnRadiusAuthStripDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAuthGroup2 = rbnRadiusAuthGroup2.setStatus('current')
rbnRadiusAcctGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 7)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAcctPktTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAcctDeadtime"), ("RBN-RADIUS-MIB", "rbnRadiusAcctTries"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvLastChange"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvCounterResetTime"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvSendErrors"), ("RBN-RADIUS-MIB", "rbnRadiusAcctStripDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAcctGroup2 = rbnRadiusAcctGroup2.setStatus('current')
rbnRadiusNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 3)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusClientPort"), ("RBN-RADIUS-MIB", "rbnRadiusContext"), ("RBN-RADIUS-MIB", "rbnRadiusReason"), ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusNotifyGroup = rbnRadiusNotifyGroup.setStatus('current')
rbnRadiusAuthNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 4)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAuthNotifyGroup = rbnRadiusAuthNotifyGroup.setStatus('current')
rbnRadiusAcctNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 5)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAcctStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAcctNotifyGroup = rbnRadiusAcctNotifyGroup.setStatus('current')
rbnRadiusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1, 1)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthGroup"), ("RBN-RADIUS-MIB", "rbnRadiusAcctGroup"), ("RBN-RADIUS-MIB", "rbnRadiusNotifyGroup"), ("RBN-RADIUS-MIB", "rbnRadiusAuthNotifyGroup"), ("RBN-RADIUS-MIB", "rbnRadiusAcctNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusCompliance = rbnRadiusCompliance.setStatus('deprecated')
rbnRadiusAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 1)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAuthPktTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAuthDeadtime"), ("RBN-RADIUS-MIB", "rbnRadiusAuthTries"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvLastChange"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvCounterResetTime"), ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvSendErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAuthGroup = rbnRadiusAuthGroup.setStatus('deprecated')
rbnRadiusAcctGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 2)).setObjects(("RBN-RADIUS-MIB", "rbnRadiusAcctPktTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvTimeout"), ("RBN-RADIUS-MIB", "rbnRadiusAcctDeadtime"), ("RBN-RADIUS-MIB", "rbnRadiusAcctTries"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvLastChange"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvCounterResetTime"), ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvSendErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnRadiusAcctGroup = rbnRadiusAcctGroup.setStatus('deprecated')
mibBuilder.exportSymbols("RBN-RADIUS-MIB", rbnRadiusAuthSrvLastChange=rbnRadiusAuthSrvLastChange, rbnRadiusAcctSrvEntry=rbnRadiusAcctSrvEntry, rbnRadiusAcctSrvTimeout=rbnRadiusAcctSrvTimeout, rbnRadiusAuthNotifyGroup=rbnRadiusAuthNotifyGroup, rbnRadiusAuthTries=rbnRadiusAuthTries, rbnRadiusAcctStripDomain=rbnRadiusAcctStripDomain, rbnRadiusAcctTries=rbnRadiusAcctTries, rbnRadiusContext=rbnRadiusContext, rbnRadiusAcctPktTimeout=rbnRadiusAcctPktTimeout, rbnRadiusAcctGroup2=rbnRadiusAcctGroup2, rbnRadiusGroups=rbnRadiusGroups, rbnRadiusAuthObjects=rbnRadiusAuthObjects, rbnRadiusAcctObjects=rbnRadiusAcctObjects, rbnRadiusCompliance=rbnRadiusCompliance, rbnRadiusNotifyGroup=rbnRadiusNotifyGroup, rbnRadiusAuthSrvTimeout=rbnRadiusAuthSrvTimeout, rbnRadiusAcctDeadtime=rbnRadiusAcctDeadtime, rbnRadiusAuthGroup2=rbnRadiusAuthGroup2, rbnRadiusAcctNotifyGroup=rbnRadiusAcctNotifyGroup, rbnRadiusAcctStateChange=rbnRadiusAcctStateChange, rbnRadiusAcctSrvState=rbnRadiusAcctSrvState, rbnRadiusCompliance2=rbnRadiusCompliance2, rbnRadiusAcctSrvTable=rbnRadiusAcctSrvTable, rbnRadiusAuthSrvState=rbnRadiusAuthSrvState, rbnRadiusNotifyObjects=rbnRadiusNotifyObjects, rbnRadiusAcctGroup=rbnRadiusAcctGroup, rbnRadiusAuthSrvCounterResetTime=rbnRadiusAuthSrvCounterResetTime, rbnRadiusAcctSrvLastChange=rbnRadiusAcctSrvLastChange, rbnRadiusClientPort=rbnRadiusClientPort, rbnRadiusUsername=rbnRadiusUsername, rbnRadiusAuthSrvSendErrors=rbnRadiusAuthSrvSendErrors, rbnRadiusAuthGroup=rbnRadiusAuthGroup, rbnRadiusAuthPktTimeout=rbnRadiusAuthPktTimeout, rbnRadiusMib=rbnRadiusMib, rbnRadiusAcctSrvCounterResetTime=rbnRadiusAcctSrvCounterResetTime, rbnRadiusCompliances=rbnRadiusCompliances, rbnRadiusAuthStripDomain=rbnRadiusAuthStripDomain, rbnRadiusMIBNotifications=rbnRadiusMIBNotifications, rbnRadiusAuthDeadtime=rbnRadiusAuthDeadtime, PYSNMP_MODULE_ID=rbnRadiusMib, rbnRadiusMIBConformance=rbnRadiusMIBConformance, RbnRadiusServerReason=RbnRadiusServerReason, rbnRadiusReason=rbnRadiusReason, rbnRadiusAuthStateChange=rbnRadiusAuthStateChange, RbnRadiusServerState=RbnRadiusServerState, rbnRadiusMIBObjects=rbnRadiusMIBObjects, rbnRadiusAuthSrvEntry=rbnRadiusAuthSrvEntry, rbnRadiusAuthSrvTable=rbnRadiusAuthSrvTable, rbnRadiusAcctSrvSendErrors=rbnRadiusAcctSrvSendErrors)
