#
# PySNMP MIB module ORANAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ORANAMES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Counter32, IpAddress, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ModuleIdentity, NotificationType, Unsigned32, Bits, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter32", "IpAddress", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ModuleIdentity", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 11)

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

oracle = MibIdentifier((1, 3, 6, 1, 4, 1, 111))
oraNamesMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 6))
oraNamesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 6, 1))
oraNamesTNSTable = MibTable((1, 3, 6, 1, 4, 1, 111, 6, 1, 1), )
if mibBuilder.loadTexts: oraNamesTNSTable.setStatus('mandatory')
oraNamesTNSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraNamesTNSEntry.setStatus('mandatory')
oraNamesTNSstartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNSstartDate.setStatus('mandatory')
oraNamesTNStraceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNStraceLevel.setStatus('mandatory')
oraNamesTNSsecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNSsecurityLevel.setStatus('mandatory')
oraNamesTNSparameterFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNSparameterFile.setStatus('mandatory')
oraNamesTNSlogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNSlogFile.setStatus('mandatory')
oraNamesTNStraceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNStraceFile.setStatus('mandatory')
oraNamesTNSstate = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNSstate.setStatus('mandatory')
oraNamesTNScontact = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNScontact.setStatus('mandatory')
oraNamesTNSlistenAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNSlistenAddresses.setStatus('mandatory')
oraNamesTNSfailedListenAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNSfailedListenAddresses.setStatus('mandatory')
oraNamesTNSreload = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesTNSreload.setStatus('mandatory')
oraNamesTNSrunningTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesTNSrunningTime.setStatus('mandatory')
oraNamesConfigTable = MibTable((1, 3, 6, 1, 4, 1, 111, 6, 1, 2), )
if mibBuilder.loadTexts: oraNamesConfigTable.setStatus('mandatory')
oraNamesConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraNamesConfigEntry.setStatus('mandatory')
oraNamesConfigAdminRegion = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigAdminRegion.setStatus('mandatory')
oraNamesConfigAuthorityRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigAuthorityRequired.setStatus('mandatory')
oraNamesConfigAutoRefreshExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigAutoRefreshExpire.setStatus('mandatory')
oraNamesConfigAutoRefreshRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 4), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigAutoRefreshRetry.setStatus('mandatory')
oraNamesConfigCacheCheckpointFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigCacheCheckpointFile.setStatus('mandatory')
oraNamesConfigCacheCheckpointInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigCacheCheckpointInterval.setStatus('mandatory')
oraNamesConfigConfigCheckpointFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigConfigCheckpointFile.setStatus('mandatory')
oraNamesConfigDefaultForwarders = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigDefaultForwarders.setStatus('mandatory')
oraNamesConfigDefaultForwardersOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigDefaultForwardersOnly.setStatus('mandatory')
oraNamesConfigDomainCheckpointFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigDomainCheckpointFile.setStatus('mandatory')
oraNamesConfigDomainHints = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigDomainHints.setStatus('mandatory')
oraNamesConfigDomains = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigDomains.setStatus('mandatory')
oraNamesConfigForwardingAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigForwardingAvailable.setStatus('mandatory')
oraNamesConfigForwardingDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigForwardingDesired.setStatus('mandatory')
oraNamesConfigLogDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigLogDirectory.setStatus('mandatory')
oraNamesConfigLogStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 16), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigLogStatsInterval.setStatus('mandatory')
oraNamesConfigLogUnique = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigLogUnique.setStatus('mandatory')
oraNamesConfigMaxOpenConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigMaxOpenConnections.setStatus('mandatory')
oraNamesConfigMaxReforwards = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigMaxReforwards.setStatus('mandatory')
oraNamesConfigMessagePoolStartSize = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigMessagePoolStartSize.setStatus('mandatory')
oraNamesConfigNoModifyRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 21), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigNoModifyRequests.setStatus('mandatory')
oraNamesConfigNoRegionDatabase = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 22), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigNoRegionDatabase.setStatus('mandatory')
oraNamesConfigResetStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 23), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigResetStatsInterval.setStatus('mandatory')
oraNamesConfigServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigServerName.setStatus('mandatory')
oraNamesConfigTopologyCheckpointFile = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 25), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigTopologyCheckpointFile.setStatus('mandatory')
oraNamesConfigTraceDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 26), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigTraceDirectory.setStatus('mandatory')
oraNamesConfigTraceFunc = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 27), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigTraceFunc.setStatus('mandatory')
oraNamesConfigTraceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigTraceMask.setStatus('mandatory')
oraNamesConfigTraceUnique = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 2, 1, 29), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oraNamesConfigTraceUnique.setStatus('mandatory')
oraNamesServerTable = MibTable((1, 3, 6, 1, 4, 1, 111, 6, 1, 3), )
if mibBuilder.loadTexts: oraNamesServerTable.setStatus('mandatory')
oraNamesServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: oraNamesServerEntry.setStatus('mandatory')
oraNamesServerQueriesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerQueriesReceived.setStatus('mandatory')
oraNamesServerLastNnamesNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerLastNnamesNotFound.setStatus('mandatory')
oraNamesServerQueriesTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerQueriesTotalTime.setStatus('mandatory')
oraNamesServerDeletesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerDeletesReceived.setStatus('mandatory')
oraNamesServerDeletesRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerDeletesRefused.setStatus('mandatory')
oraNamesServerDeletesTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerDeletesTotalTime.setStatus('mandatory')
oraNamesServerRenamesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerRenamesReceived.setStatus('mandatory')
oraNamesServerRenamesRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerRenamesRefused.setStatus('mandatory')
oraNamesServerRenamesTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerRenamesTotalTime.setStatus('mandatory')
oraNamesServerUpdatesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerUpdatesReceived.setStatus('mandatory')
oraNamesServerUpdatesRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerUpdatesRefused.setStatus('mandatory')
oraNamesServerUpdatesTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerUpdatesTotalTime.setStatus('mandatory')
oraNamesServerCorruptMessagesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerCorruptMessagesReceived.setStatus('mandatory')
oraNamesServerResponsesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerResponsesSent.setStatus('mandatory')
oraNamesServerErrorResponsesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerErrorResponsesSent.setStatus('mandatory')
oraNamesServerAliasLoopsDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerAliasLoopsDetected.setStatus('mandatory')
oraNamesServerLookupsAttempted = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerLookupsAttempted.setStatus('mandatory')
oraNamesServerCreatedOnLookup = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerCreatedOnLookup.setStatus('mandatory')
oraNamesServerLookupFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerLookupFailures.setStatus('mandatory')
oraNamesServerExactMatches = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerExactMatches.setStatus('mandatory')
oraNamesServerForwardFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerForwardFailures.setStatus('mandatory')
oraNamesServerForwardTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerForwardTimeouts.setStatus('mandatory')
oraNamesServerResponsesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerResponsesReceived.setStatus('mandatory')
oraNamesServerErrorResponsesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerErrorResponsesReceived.setStatus('mandatory')
oraNamesServerRequestsForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerRequestsForwarded.setStatus('mandatory')
oraNamesServerLastReload = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 26), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerLastReload.setStatus('mandatory')
oraNamesServerReloadCheckFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerReloadCheckFailures.setStatus('mandatory')
oraNamesServerLastCheckpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 28), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerLastCheckpoint.setStatus('mandatory')
oraNamesServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerName.setStatus('mandatory')
oraNamesServerAdminRegion = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 6, 1, 3, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraNamesServerAdminRegion.setStatus('mandatory')
mibBuilder.exportSymbols("ORANAMES-MIB", oraNamesObjects=oraNamesObjects, oraNamesServerRenamesRefused=oraNamesServerRenamesRefused, oraNamesServerCreatedOnLookup=oraNamesServerCreatedOnLookup, oraNamesServerResponsesReceived=oraNamesServerResponsesReceived, oraNamesTNSfailedListenAddresses=oraNamesTNSfailedListenAddresses, oracle=oracle, oraNamesConfigTraceUnique=oraNamesConfigTraceUnique, oraNamesTNSsecurityLevel=oraNamesTNSsecurityLevel, oraNamesConfigNoRegionDatabase=oraNamesConfigNoRegionDatabase, oraNamesConfigLogDirectory=oraNamesConfigLogDirectory, oraNamesServerErrorResponsesSent=oraNamesServerErrorResponsesSent, oraNamesConfigAdminRegion=oraNamesConfigAdminRegion, oraNamesServerLookupFailures=oraNamesServerLookupFailures, oraNamesServerLastReload=oraNamesServerLastReload, oraNamesConfigForwardingDesired=oraNamesConfigForwardingDesired, oraNamesConfigCacheCheckpointFile=oraNamesConfigCacheCheckpointFile, oraNamesServerUpdatesReceived=oraNamesServerUpdatesReceived, oraNamesServerLastCheckpoint=oraNamesServerLastCheckpoint, oraNamesServerErrorResponsesReceived=oraNamesServerErrorResponsesReceived, oraNamesConfigNoModifyRequests=oraNamesConfigNoModifyRequests, oraNamesServerForwardFailures=oraNamesServerForwardFailures, oraNamesTNScontact=oraNamesTNScontact, oraNamesServerLookupsAttempted=oraNamesServerLookupsAttempted, oraNamesConfigAutoRefreshRetry=oraNamesConfigAutoRefreshRetry, oraNamesTNSlistenAddresses=oraNamesTNSlistenAddresses, oraNamesServerRequestsForwarded=oraNamesServerRequestsForwarded, oraNamesConfigDefaultForwarders=oraNamesConfigDefaultForwarders, oraNamesConfigDomainCheckpointFile=oraNamesConfigDomainCheckpointFile, oraNamesConfigCacheCheckpointInterval=oraNamesConfigCacheCheckpointInterval, oraNamesServerCorruptMessagesReceived=oraNamesServerCorruptMessagesReceived, oraNamesTNSlogFile=oraNamesTNSlogFile, oraNamesConfigDefaultForwardersOnly=oraNamesConfigDefaultForwardersOnly, oraNamesServerDeletesTotalTime=oraNamesServerDeletesTotalTime, oraNamesTNSTable=oraNamesTNSTable, oraNamesServerQueriesTotalTime=oraNamesServerQueriesTotalTime, oraNamesServerTable=oraNamesServerTable, oraNamesConfigAutoRefreshExpire=oraNamesConfigAutoRefreshExpire, oraNamesTNSEntry=oraNamesTNSEntry, oraNamesTNSreload=oraNamesTNSreload, oraNamesServerQueriesReceived=oraNamesServerQueriesReceived, oraNamesTNSparameterFile=oraNamesTNSparameterFile, oraNamesConfigMaxReforwards=oraNamesConfigMaxReforwards, oraNamesServerExactMatches=oraNamesServerExactMatches, oraNamesServerUpdatesRefused=oraNamesServerUpdatesRefused, oraNamesConfigTable=oraNamesConfigTable, oraNamesServerReloadCheckFailures=oraNamesServerReloadCheckFailures, oraNamesServerAliasLoopsDetected=oraNamesServerAliasLoopsDetected, oraNamesConfigMaxOpenConnections=oraNamesConfigMaxOpenConnections, oraNamesServerForwardTimeouts=oraNamesServerForwardTimeouts, oraNamesConfigConfigCheckpointFile=oraNamesConfigConfigCheckpointFile, oraNamesConfigForwardingAvailable=oraNamesConfigForwardingAvailable, oraNamesConfigResetStatsInterval=oraNamesConfigResetStatsInterval, oraNamesServerRenamesTotalTime=oraNamesServerRenamesTotalTime, oraNamesConfigDomainHints=oraNamesConfigDomainHints, oraNamesConfigLogStatsInterval=oraNamesConfigLogStatsInterval, oraNamesConfigTraceDirectory=oraNamesConfigTraceDirectory, oraNamesConfigLogUnique=oraNamesConfigLogUnique, oraNamesConfigServerName=oraNamesConfigServerName, oraNamesServerRenamesReceived=oraNamesServerRenamesReceived, oraNamesConfigAuthorityRequired=oraNamesConfigAuthorityRequired, oraNamesConfigMessagePoolStartSize=oraNamesConfigMessagePoolStartSize, oraNamesServerDeletesRefused=oraNamesServerDeletesRefused, oraNamesTNSrunningTime=oraNamesTNSrunningTime, oraNamesConfigEntry=oraNamesConfigEntry, oraNamesTNSstartDate=oraNamesTNSstartDate, oraNamesConfigDomains=oraNamesConfigDomains, oraNamesMIB=oraNamesMIB, oraNamesTNSstate=oraNamesTNSstate, oraNamesConfigTopologyCheckpointFile=oraNamesConfigTopologyCheckpointFile, oraNamesServerEntry=oraNamesServerEntry, TruthValue=TruthValue, DateAndTime=DateAndTime, oraNamesServerName=oraNamesServerName, oraNamesServerAdminRegion=oraNamesServerAdminRegion, oraNamesConfigTraceMask=oraNamesConfigTraceMask, oraNamesTNStraceFile=oraNamesTNStraceFile, oraNamesServerUpdatesTotalTime=oraNamesServerUpdatesTotalTime, oraNamesConfigTraceFunc=oraNamesConfigTraceFunc, oraNamesServerResponsesSent=oraNamesServerResponsesSent, oraNamesTNStraceLevel=oraNamesTNStraceLevel, oraNamesServerLastNnamesNotFound=oraNamesServerLastNnamesNotFound, oraNamesServerDeletesReceived=oraNamesServerDeletesReceived)
