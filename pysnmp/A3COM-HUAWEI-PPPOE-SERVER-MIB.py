#
# PySNMP MIB module A3COM-HUAWEI-PPPOE-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-PPPOE-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks, Gauge32, IpAddress, Integer32, Unsigned32, NotificationType, iso, ModuleIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "Integer32", "Unsigned32", "NotificationType", "iso", "ModuleIdentity", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cPPPoEServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102))
h3cPPPoEServer.setRevisions(('2009-05-06 00:00',))
if mibBuilder.loadTexts: h3cPPPoEServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: h3cPPPoEServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cPPPoEServerObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1))
h3cPPPoEServerMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPPPoEServerMaxSessions.setStatus('current')
h3cPPPoEServerCurrSessions = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPPPoEServerCurrSessions.setStatus('current')
h3cPPPoEServerAuthRequests = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPPPoEServerAuthRequests.setStatus('current')
h3cPPPoEServerAuthSuccesses = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPPPoEServerAuthSuccesses.setStatus('current')
h3cPPPoEServerAuthFailures = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPPPoEServerAuthFailures.setStatus('current')
h3cPPPoESAbnormOffsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPPPoESAbnormOffsThreshold.setStatus('current')
h3cPPPoESAbnormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPPPoESAbnormOffPerThreshold.setStatus('current')
h3cPPPoESNormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPPPoESNormOffPerThreshold.setStatus('current')
h3cPPPoEServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 2))
h3cPPPoeServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 2, 0))
h3cPPPoESAbnormOffsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 2, 0, 1))
if mibBuilder.loadTexts: h3cPPPoESAbnormOffsAlarm.setStatus('current')
h3cPPPoESAbnormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 2, 0, 2))
if mibBuilder.loadTexts: h3cPPPoESAbnormOffPerAlarm.setStatus('current')
h3cPPPoESNormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 102, 2, 0, 3))
if mibBuilder.loadTexts: h3cPPPoESNormOffPerAlarm.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-PPPOE-SERVER-MIB", h3cPPPoESAbnormOffsThreshold=h3cPPPoESAbnormOffsThreshold, h3cPPPoEServerObject=h3cPPPoEServerObject, h3cPPPoESNormOffPerThreshold=h3cPPPoESNormOffPerThreshold, PYSNMP_MODULE_ID=h3cPPPoEServer, h3cPPPoEServerMaxSessions=h3cPPPoEServerMaxSessions, h3cPPPoESNormOffPerAlarm=h3cPPPoESNormOffPerAlarm, h3cPPPoESAbnormOffsAlarm=h3cPPPoESAbnormOffsAlarm, h3cPPPoEServerAuthFailures=h3cPPPoEServerAuthFailures, h3cPPPoEServer=h3cPPPoEServer, h3cPPPoESAbnormOffPerAlarm=h3cPPPoESAbnormOffPerAlarm, h3cPPPoEServerAuthSuccesses=h3cPPPoEServerAuthSuccesses, h3cPPPoESAbnormOffPerThreshold=h3cPPPoESAbnormOffPerThreshold, h3cPPPoeServerTrapPrefix=h3cPPPoeServerTrapPrefix, h3cPPPoEServerTraps=h3cPPPoEServerTraps, h3cPPPoEServerAuthRequests=h3cPPPoEServerAuthRequests, h3cPPPoEServerCurrSessions=h3cPPPoEServerCurrSessions)
