#
# PySNMP MIB module ALCATEL-IND1-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Dot3Oam, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Dot3Oam")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
dot3OamEventLogValue, dot3OamEventLogLocation, dot3OamEventLogThresholdLo, dot3OamEventLogWindowHi, dot3OamEventLogEventTotal, dot3OamLoopbackEntry, dot3OamStatsEntry, dot3OamEventLogWindowLo, dot3OamEventLogType, dot3OamEventLogTimestamp, dot3OamEventLogThresholdHi, dot3OamEntry, dot3OamEventLogOui, dot3OamEventLogRunningTotal = mibBuilder.importSymbols("DOT3-OAM-MIB", "dot3OamEventLogValue", "dot3OamEventLogLocation", "dot3OamEventLogThresholdLo", "dot3OamEventLogWindowHi", "dot3OamEventLogEventTotal", "dot3OamLoopbackEntry", "dot3OamStatsEntry", "dot3OamEventLogWindowLo", "dot3OamEventLogType", "dot3OamEventLogTimestamp", "dot3OamEventLogThresholdHi", "dot3OamEntry", "dot3OamEventLogOui", "dot3OamEventLogRunningTotal")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, iso, IpAddress, Gauge32, enterprises, NotificationType, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Counter32, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "Gauge32", "enterprises", "NotificationType", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Counter32", "TimeTicks", "MibIdentifier", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1Dot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1))
alcatelIND1Dot3OamMIB.setRevisions(('2009-02-25 00:00',))
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIB.setLastUpdated('200902250000Z')
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1Dot3OamNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0))
if mibBuilder.loadTexts: alcatelIND1Dot3OamNotifications.setStatus('current')
alcatelIND1Dot3OamMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1))
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIBObjects.setStatus('current')
alcatelIND1Dot3OamMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2))
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIBConformance.setStatus('current')
alcatelIND1Dot3OamMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIBGroups.setStatus('current')
alcatelIND1Dot3OamMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1Dot3OamMIBCompliances.setStatus('current')
alaDot3OamStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamStatus.setStatus('current')
alaDot3OamGlobalClearStats = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamGlobalClearStats.setStatus('current')
alaDot3OamGlobalClearEventLogs = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamGlobalClearEventLogs.setStatus('current')
alaDot3OamGlobalClearVariableTransactions = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamGlobalClearVariableTransactions.setStatus('current')
alaDot3OamMultiplePduCount = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamMultiplePduCount.setStatus('current')
alaDot3OamPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8))
alaDot3OamTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1), )
if mibBuilder.loadTexts: alaDot3OamTable.setStatus('current')
alaDot3OamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1), )
dot3OamEntry.registerAugmentions(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamEntry"))
alaDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
if mibBuilder.loadTexts: alaDot3OamEntry.setStatus('current')
alaDot3OamKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 120)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamKeepAliveInterval.setStatus('current')
alaDot3OamHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamHelloInterval.setStatus('current')
alaDot3OamNextTransactionId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamNextTransactionId.setStatus('current')
alaDot3OamPortLoopbackControl = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9))
alaDot3OamLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1), )
if mibBuilder.loadTexts: alaDot3OamLoopbackTable.setStatus('current')
alaDot3OamLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1), )
dot3OamLoopbackEntry.registerAugmentions(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamLoopbackEntry"))
alaDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
if mibBuilder.loadTexts: alaDot3OamLoopbackEntry.setStatus('current')
alaDot3OamPortL1PingFramesConf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamPortL1PingFramesConf.setStatus('current')
alaDot3OamPortL1PingFramesDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamPortL1PingFramesDelay.setStatus('current')
alaDot3OamPortL1PingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 0), ("start", 1), ("running", 2), ("operationSuccessful", 3), ("operationUnsuccessful", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamPortL1PingStatus.setStatus('current')
alaDot3OamPortL1PingFramesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamPortL1PingFramesSent.setStatus('current')
alaDot3OamPortL1PingFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamPortL1PingFramesReceived.setStatus('current')
alaDot3OamPortL1PingAverageRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 9, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamPortL1PingAverageRoundTripDelay.setStatus('current')
alaDot3OamPortStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10))
alaDot3OamStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1), )
if mibBuilder.loadTexts: alaDot3OamStatsTable.setStatus('current')
alaDot3OamStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1, 1), )
dot3OamStatsEntry.registerAugmentions(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamStatsEntry"))
alaDot3OamStatsEntry.setIndexNames(*dot3OamStatsEntry.getIndexNames())
if mibBuilder.loadTexts: alaDot3OamStatsEntry.setStatus('current')
alaDot3OamPortClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamPortClearStats.setStatus('current')
alaDot3OamPortEventLogs = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11))
alaDot3OamEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1), )
if mibBuilder.loadTexts: alaDot3OamEventLogTable.setStatus('current')
alaDot3OamEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: alaDot3OamEventLogEntry.setStatus('current')
alaDot3OamPortClearEventLogs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDot3OamPortClearEventLogs.setStatus('current')
alaDot3OamRetrieveRequest = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12))
alaDot3OamRetrieveRequestTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1), )
if mibBuilder.loadTexts: alaDot3OamRetrieveRequestTable.setStatus('current')
alaDot3OamRetrieveRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamTransactionId"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestBranch"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestLeaf"))
if mibBuilder.loadTexts: alaDot3OamRetrieveRequestEntry.setStatus('current')
alaDot3OamTransactionId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: alaDot3OamTransactionId.setStatus('current')
alaDot3OamVariableRequestBranch = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 7))).clone(namedValues=NamedValues(("object", 3), ("package", 4), ("attribute", 7))).clone('attribute'))
if mibBuilder.loadTexts: alaDot3OamVariableRequestBranch.setStatus('current')
alaDot3OamVariableRequestLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: alaDot3OamVariableRequestLeaf.setStatus('current')
alaDot3OamVariableRequestRetrieveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("failed", 2), ("success", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamVariableRequestRetrieveStatus.setStatus('current')
alaDot3OamVariableRequestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDot3OamVariableRequestRowStatus.setStatus('current')
alaDot3OamPortClearVariableTransactions = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDot3OamPortClearVariableTransactions.setStatus('current')
alaDot3OamRetrieveResponse = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13))
alaDot3OamRetrieveResponseTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1), )
if mibBuilder.loadTexts: alaDot3OamRetrieveResponseTable.setStatus('current')
alaDot3OamRetrieveResponseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamTransactionId"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseBranch"), (0, "ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseLeaf"))
if mibBuilder.loadTexts: alaDot3OamRetrieveResponseEntry.setStatus('current')
alaDot3OamVariableResponseBranch = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 7))).clone(namedValues=NamedValues(("object", 3), ("package", 4), ("attribute", 7))))
if mibBuilder.loadTexts: alaDot3OamVariableResponseBranch.setStatus('current')
alaDot3OamVariableResponseLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: alaDot3OamVariableResponseLeaf.setStatus('current')
alaDot3OamVariableResponseValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 1, 13, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDot3OamVariableResponseValue.setStatus('current')
alaDot3OamThresholdEventClear = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0, 1)).setObjects(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"), ("DOT3-OAM-MIB", "dot3OamEventLogOui"), ("DOT3-OAM-MIB", "dot3OamEventLogType"), ("DOT3-OAM-MIB", "dot3OamEventLogLocation"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowHi"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowLo"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdHi"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdLo"), ("DOT3-OAM-MIB", "dot3OamEventLogValue"), ("DOT3-OAM-MIB", "dot3OamEventLogRunningTotal"), ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: alaDot3OamThresholdEventClear.setStatus('current')
alaDot3OamNonThresholdEventClear = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 0, 2)).setObjects(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"), ("DOT3-OAM-MIB", "dot3OamEventLogOui"), ("DOT3-OAM-MIB", "dot3OamEventLogType"), ("DOT3-OAM-MIB", "dot3OamEventLogLocation"), ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: alaDot3OamNonThresholdEventClear.setStatus('current')
alcatelIND1Dot3OamMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamBaseGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortConfigGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortLoopbackControlGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortStatsGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortEventLogsGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamRetrieveRequestGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamRetrieveResponseGroup"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1Dot3OamMIBCompliance = alcatelIND1Dot3OamMIBCompliance.setStatus('current')
alaDot3OamBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamStatus"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearStats"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearEventLogs"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamGlobalClearVariableTransactions"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamMultiplePduCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamBaseGroup = alaDot3OamBaseGroup.setStatus('current')
alaDot3OamPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamKeepAliveInterval"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamHelloInterval"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamNextTransactionId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamPortConfigGroup = alaDot3OamPortConfigGroup.setStatus('current')
alaDot3OamPortLoopbackControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesConf"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesDelay"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingStatus"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesSent"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingFramesReceived"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortL1PingAverageRoundTripDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamPortLoopbackControlGroup = alaDot3OamPortLoopbackControlGroup.setStatus('current')
alaDot3OamPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamPortStatsGroup = alaDot3OamPortStatsGroup.setStatus('current')
alaDot3OamPortEventLogsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearEventLogs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamPortEventLogsGroup = alaDot3OamPortEventLogsGroup.setStatus('current')
alaDot3OamRetrieveRequestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestRetrieveStatus"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableRequestRowStatus"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamPortClearVariableTransactions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamRetrieveRequestGroup = alaDot3OamRetrieveRequestGroup.setStatus('current')
alaDot3OamRetrieveResponseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamVariableResponseValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamRetrieveResponseGroup = alaDot3OamRetrieveResponseGroup.setStatus('current')
alaDot3OamNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52, 1, 2, 1, 8)).setObjects(("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamThresholdEventClear"), ("ALCATEL-IND1-DOT3-OAM-MIB", "alaDot3OamNonThresholdEventClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDot3OamNotificationGroup = alaDot3OamNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-DOT3-OAM-MIB", alaDot3OamRetrieveRequestTable=alaDot3OamRetrieveRequestTable, alaDot3OamPortL1PingFramesSent=alaDot3OamPortL1PingFramesSent, alaDot3OamPortL1PingFramesReceived=alaDot3OamPortL1PingFramesReceived, alaDot3OamPortClearStats=alaDot3OamPortClearStats, alaDot3OamPortL1PingFramesConf=alaDot3OamPortL1PingFramesConf, alcatelIND1Dot3OamNotifications=alcatelIND1Dot3OamNotifications, alaDot3OamRetrieveResponseEntry=alaDot3OamRetrieveResponseEntry, alaDot3OamPortEventLogs=alaDot3OamPortEventLogs, alcatelIND1Dot3OamMIBObjects=alcatelIND1Dot3OamMIBObjects, alaDot3OamPortConfig=alaDot3OamPortConfig, alaDot3OamPortLoopbackControl=alaDot3OamPortLoopbackControl, alaDot3OamRetrieveResponse=alaDot3OamRetrieveResponse, alaDot3OamPortL1PingFramesDelay=alaDot3OamPortL1PingFramesDelay, alcatelIND1Dot3OamMIBCompliances=alcatelIND1Dot3OamMIBCompliances, alaDot3OamPortL1PingAverageRoundTripDelay=alaDot3OamPortL1PingAverageRoundTripDelay, alaDot3OamBaseGroup=alaDot3OamBaseGroup, alaDot3OamVariableRequestRowStatus=alaDot3OamVariableRequestRowStatus, alaDot3OamTransactionId=alaDot3OamTransactionId, alcatelIND1Dot3OamMIBCompliance=alcatelIND1Dot3OamMIBCompliance, alaDot3OamStatus=alaDot3OamStatus, alaDot3OamPortStats=alaDot3OamPortStats, PYSNMP_MODULE_ID=alcatelIND1Dot3OamMIB, alaDot3OamVariableRequestRetrieveStatus=alaDot3OamVariableRequestRetrieveStatus, alaDot3OamVariableResponseValue=alaDot3OamVariableResponseValue, alaDot3OamPortLoopbackControlGroup=alaDot3OamPortLoopbackControlGroup, alaDot3OamRetrieveRequestEntry=alaDot3OamRetrieveRequestEntry, alaDot3OamNotificationGroup=alaDot3OamNotificationGroup, alaDot3OamVariableRequestBranch=alaDot3OamVariableRequestBranch, alaDot3OamPortL1PingStatus=alaDot3OamPortL1PingStatus, alcatelIND1Dot3OamMIBGroups=alcatelIND1Dot3OamMIBGroups, alaDot3OamKeepAliveInterval=alaDot3OamKeepAliveInterval, alaDot3OamHelloInterval=alaDot3OamHelloInterval, alaDot3OamEventLogTable=alaDot3OamEventLogTable, alaDot3OamLoopbackTable=alaDot3OamLoopbackTable, alaDot3OamRetrieveResponseTable=alaDot3OamRetrieveResponseTable, alaDot3OamGlobalClearVariableTransactions=alaDot3OamGlobalClearVariableTransactions, alaDot3OamVariableResponseLeaf=alaDot3OamVariableResponseLeaf, alaDot3OamGlobalClearStats=alaDot3OamGlobalClearStats, alaDot3OamPortClearVariableTransactions=alaDot3OamPortClearVariableTransactions, alaDot3OamTable=alaDot3OamTable, alaDot3OamStatsTable=alaDot3OamStatsTable, alcatelIND1Dot3OamMIB=alcatelIND1Dot3OamMIB, alaDot3OamStatsEntry=alaDot3OamStatsEntry, alaDot3OamPortClearEventLogs=alaDot3OamPortClearEventLogs, alaDot3OamMultiplePduCount=alaDot3OamMultiplePduCount, alaDot3OamThresholdEventClear=alaDot3OamThresholdEventClear, alaDot3OamPortStatsGroup=alaDot3OamPortStatsGroup, alaDot3OamRetrieveRequest=alaDot3OamRetrieveRequest, alaDot3OamRetrieveResponseGroup=alaDot3OamRetrieveResponseGroup, alaDot3OamVariableRequestLeaf=alaDot3OamVariableRequestLeaf, alaDot3OamPortEventLogsGroup=alaDot3OamPortEventLogsGroup, alaDot3OamRetrieveRequestGroup=alaDot3OamRetrieveRequestGroup, alaDot3OamEventLogEntry=alaDot3OamEventLogEntry, alaDot3OamGlobalClearEventLogs=alaDot3OamGlobalClearEventLogs, alaDot3OamNextTransactionId=alaDot3OamNextTransactionId, alaDot3OamNonThresholdEventClear=alaDot3OamNonThresholdEventClear, alaDot3OamPortConfigGroup=alaDot3OamPortConfigGroup, alaDot3OamVariableResponseBranch=alaDot3OamVariableResponseBranch, alcatelIND1Dot3OamMIBConformance=alcatelIND1Dot3OamMIBConformance, alaDot3OamEntry=alaDot3OamEntry, alaDot3OamLoopbackEntry=alaDot3OamLoopbackEntry)
