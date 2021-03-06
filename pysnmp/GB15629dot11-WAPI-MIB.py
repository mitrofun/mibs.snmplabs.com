#
# PySNMP MIB module GB15629dot11-WAPI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GB15629dot11-WAPI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, Counter64, Gauge32, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, TimeTicks, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "TimeTicks", "Integer32", "iso")
MacAddress, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "DisplayString")
gb15629dot11wapiMIB = ModuleIdentity((1, 2, 156, 11235, 15629, 11, 1, 1))
if mibBuilder.loadTexts: gb15629dot11wapiMIB.setLastUpdated('200705211757Z')
if mibBuilder.loadTexts: gb15629dot11wapiMIB.setOrganization('China Broadband Wireless IP Standard Group.')
member_body = MibIdentifier((1, 2)).setLabel("member-body")
cn = MibIdentifier((1, 2, 156))
bwips = MibIdentifier((1, 2, 156, 11235))
gb15629 = MibIdentifier((1, 2, 156, 11235, 15629))
gb15629_11 = MibIdentifier((1, 2, 156, 11235, 15629, 11)).setLabel("gb15629-11")
gb15629_11_mibs = MibIdentifier((1, 2, 156, 11235, 15629, 11, 1)).setLabel("gb15629-11-mibs")
wapiMIBObjects = MibIdentifier((1, 2, 156, 11235, 15629, 11, 1, 1, 1))
gb15629dot11wapiConfigTable = MibTable((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1), )
if mibBuilder.loadTexts: gb15629dot11wapiConfigTable.setStatus('current')
gb15629dot11wapiConfigEntry = MibTableRow((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gb15629dot11wapiConfigEntry.setStatus('current')
gb15629dot11wapiConfigVersion = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigVersion.setStatus('current')
gb15629dot11wapiControlledAuthControl = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiControlledAuthControl.setStatus('current')
gb15629dot11wapiControlledPortControl = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiControlledPortControl.setStatus('current')
gb15629dot11wapiOptionImplemented = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiOptionImplemented.setStatus('current')
gb15629dot11wapiPreauthenticationImplemented = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiPreauthenticationImplemented.setStatus('current')
gb15629dot11wapiEnabled = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiEnabled.setStatus('current')
gb15629dot11wapiPreauthenticationEnabled = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiPreauthenticationEnabled.setStatus('current')
gb15629dot11wapiConfigUnicastKeysSupported = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastKeysSupported.setStatus('current')
gb15629dot11wapiConfigUnicastRekeyMethod = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("timeBased", 2), ("packetBased", 3), ("timepacket-Based", 4))).clone('timeBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastRekeyMethod.setStatus('current')
gb15629dot11wapiConfigUnicastRekeyTime = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastRekeyTime.setStatus('current')
gb15629dot11wapiConfigUnicastRekeyPackets = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('1000 packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastRekeyPackets.setStatus('current')
gb15629dot11wapiConfigMulticastCipher = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastCipher.setStatus('current')
gb15629dot11wapiConfigMulticastRekeyMethod = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("timeBased", 2), ("packetBased", 3), ("timepacket-Based", 4))).clone('timeBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastRekeyMethod.setStatus('current')
gb15629dot11wapiConfigMulticastRekeyTime = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastRekeyTime.setStatus('current')
gb15629dot11wapiConfigMulticastRekeyPackets = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('1000 packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastRekeyPackets.setStatus('current')
gb15629dot11wapiConfigMulticastRekeyStrict = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastRekeyStrict.setStatus('current')
gb15629dot11wapiConfigPSKValue = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigPSKValue.setStatus('current')
gb15629dot11wapiConfigPSKPassPhrase = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigPSKPassPhrase.setStatus('current')
gb15629dot11wapiConfigCertificateUpdateCount = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigCertificateUpdateCount.setStatus('current')
gb15629dot11wapiConfigMulticastUpdateCount = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastUpdateCount.setStatus('current')
gb15629dot11wapiConfigUnicastUpdateCount = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastUpdateCount.setStatus('current')
gb15629dot11wapiConfigMulticastCipherSize = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigMulticastCipherSize.setStatus('current')
gb15629dot11wapiConfigBKLifetime = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(43200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigBKLifetime.setStatus('current')
gb15629dot11wapiConfigBKReauthThreshold = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(70)).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigBKReauthThreshold.setStatus('current')
gb15629dot11wapiConfigSATimeout = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigSATimeout.setStatus('current')
gb15629dot11wapiAuthenticationSuiteSelected = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiAuthenticationSuiteSelected.setStatus('current')
gb15629dot11wapiUnicastCipherSelected = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 27), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiUnicastCipherSelected.setStatus('current')
gb15629dot11wapiMulticastCipherSelected = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 28), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiMulticastCipherSelected.setStatus('current')
gb15629dot11wapiBKIDUsed = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiBKIDUsed.setStatus('current')
gb15629dot11wapiAuthenticationSuiteRequested = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiAuthenticationSuiteRequested.setStatus('current')
gb15629dot11wapiUnicastCipherRequested = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiUnicastCipherRequested.setStatus('current')
gb15629dot11wapiMulticastCipherRequested = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 1, 1, 32), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiMulticastCipherRequested.setStatus('current')
gb15629dot11wapiConfigUnicastCiphersTable = MibTable((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2), )
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCiphersTable.setStatus('current')
gb15629dot11wapiConfigUnicastCiphersEntry = MibTableRow((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherIndex"))
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCiphersEntry.setStatus('current')
gb15629dot11wapiConfigUnicastCipherIndex = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCipherIndex.setStatus('current')
gb15629dot11wapiConfigUnicastCipher = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCipher.setStatus('current')
gb15629dot11wapiConfigUnicastCipherEnabled = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCipherEnabled.setStatus('current')
gb15629dot11wapiConfigUnicastCipherSize = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigUnicastCipherSize.setStatus('current')
gb15629dot11wapiConfigAuthenticationSuitesTable = MibTable((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3), )
if mibBuilder.loadTexts: gb15629dot11wapiConfigAuthenticationSuitesTable.setStatus('current')
gb15629dot11wapiConfigAuthenticationSuitesEntry = MibTableRow((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1), ).setIndexNames((0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuiteIndex"))
if mibBuilder.loadTexts: gb15629dot11wapiConfigAuthenticationSuitesEntry.setStatus('current')
gb15629dot11wapiConfigAuthenticationSuiteIndex = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: gb15629dot11wapiConfigAuthenticationSuiteIndex.setStatus('current')
gb15629dot11wapiConfigAuthenticationSuite = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiConfigAuthenticationSuite.setStatus('current')
gb15629dot11wapiConfigAuthenticationSuiteEnabled = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gb15629dot11wapiConfigAuthenticationSuiteEnabled.setStatus('current')
gb15629dot11wapiStatsTable = MibTable((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4), )
if mibBuilder.loadTexts: gb15629dot11wapiStatsTable.setStatus('current')
gb15629dot11wapiStatsEntry = MibTableRow((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsIndex"))
if mibBuilder.loadTexts: gb15629dot11wapiStatsEntry.setStatus('current')
gb15629dot11wapiStatsIndex = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: gb15629dot11wapiStatsIndex.setStatus('current')
gb15629dot11wapiStatsSTAAddress = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsSTAAddress.setStatus('current')
gb15629dot11wapiStatsVersion = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsVersion.setStatus('current')
gb15629dot11wapiStatsControlledPortStatus = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsControlledPortStatus.setStatus('current')
gb15629dot11wapiStatsSelectedUnicastCipher = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsSelectedUnicastCipher.setStatus('current')
gb15629dot11wapiStatsWPIReplayCounters = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWPIReplayCounters.setStatus('current')
gb15629dot11wapiStatsWPIDecryptableErrors = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWPIDecryptableErrors.setStatus('current')
gb15629dot11wapiStatsWPIMICErrors = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWPIMICErrors.setStatus('current')
gb15629dot11wapiStatsWAISignatureErrors = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAISignatureErrors.setStatus('current')
gb15629dot11wapiStatsWAIHMACErrors = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIHMACErrors.setStatus('current')
gb15629dot11wapiStatsWAIAuthenticationResultFailures = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIAuthenticationResultFailures.setStatus('current')
gb15629dot11wapiStatsWAIDiscardCounters = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIDiscardCounters.setStatus('current')
gb15629dot11wapiStatsWAITimeoutCounters = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAITimeoutCounters.setStatus('current')
gb15629dot11wapiStatsWAIFormatErrors = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIFormatErrors.setStatus('current')
gb15629dot11wapiStatsWAICertificateHandshakeFailures = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAICertificateHandshakeFailures.setStatus('current')
gb15629dot11wapiStatsWAIUnicastHandshakeFailures = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIUnicastHandshakeFailures.setStatus('current')
gb15629dot11wapiStatsWAIMulticastHandshakeFailures = MibTableColumn((1, 2, 156, 11235, 15629, 11, 1, 1, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gb15629dot11wapiStatsWAIMulticastHandshakeFailures.setStatus('current')
wapiMIBConformance = MibIdentifier((1, 2, 156, 11235, 15629, 11, 1, 1, 2))
gb15629dot11wapiGroups = MibIdentifier((1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1))
gb15629wapiCompliances = MibIdentifier((1, 2, 156, 11235, 15629, 11, 1, 1, 2, 2))
gb15629dot11wapiBase = ObjectGroup((1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1, 1)).setObjects(("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigVersion"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiControlledAuthControl"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiControlledPortControl"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiOptionImplemented"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiPreauthenticationImplemented"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiEnabled"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiPreauthenticationEnabled"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastKeysSupported"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyMethod"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyTime"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastRekeyPackets"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastCipher"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyMethod"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyTime"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyPackets"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastRekeyStrict"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigPSKValue"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigPSKPassPhrase"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigCertificateUpdateCount"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastUpdateCount"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastUpdateCount"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigMulticastCipherSize"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipher"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherEnabled"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigUnicastCipherSize"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuite"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigAuthenticationSuiteEnabled"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigSATimeout"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiAuthenticationSuiteSelected"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiUnicastCipherSelected"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiMulticastCipherSelected"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiBKIDUsed"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiAuthenticationSuiteRequested"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiUnicastCipherRequested"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiMulticastCipherRequested"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsSTAAddress"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsVersion"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsControlledPortStatus"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsSelectedUnicastCipher"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIReplayCounters"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIDecryptableErrors"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWPIMICErrors"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAISignatureErrors"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIHMACErrors"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIAuthenticationResultFailures"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIDiscardCounters"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAITimeoutCounters"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIFormatErrors"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAICertificateHandshakeFailures"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIUnicastHandshakeFailures"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiStatsWAIMulticastHandshakeFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gb15629dot11wapiBase = gb15629dot11wapiBase.setStatus('current')
gb15629dot11wapiBKcachingGroup = ObjectGroup((1, 2, 156, 11235, 15629, 11, 1, 1, 2, 1, 2)).setObjects(("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigBKLifetime"), ("GB15629dot11-WAPI-MIB", "gb15629dot11wapiConfigBKReauthThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gb15629dot11wapiBKcachingGroup = gb15629dot11wapiBKcachingGroup.setStatus('current')
gb15629dot11wapiCompliance = ModuleCompliance((1, 2, 156, 11235, 15629, 11, 1, 1, 2, 2, 1)).setObjects(("GB15629dot11-WAPI-MIB", "gb15629dot11wapiBase"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gb15629dot11wapiCompliance = gb15629dot11wapiCompliance.setStatus('current')
mibBuilder.exportSymbols("GB15629dot11-WAPI-MIB", gb15629dot11wapiConfigMulticastRekeyMethod=gb15629dot11wapiConfigMulticastRekeyMethod, member_body=member_body, gb15629dot11wapiConfigUnicastUpdateCount=gb15629dot11wapiConfigUnicastUpdateCount, gb15629dot11wapiConfigUnicastRekeyTime=gb15629dot11wapiConfigUnicastRekeyTime, gb15629dot11wapiConfigUnicastKeysSupported=gb15629dot11wapiConfigUnicastKeysSupported, gb15629dot11wapiConfigBKReauthThreshold=gb15629dot11wapiConfigBKReauthThreshold, gb15629dot11wapiStatsWAISignatureErrors=gb15629dot11wapiStatsWAISignatureErrors, gb15629dot11wapiStatsWAIHMACErrors=gb15629dot11wapiStatsWAIHMACErrors, gb15629dot11wapiStatsWAIUnicastHandshakeFailures=gb15629dot11wapiStatsWAIUnicastHandshakeFailures, gb15629dot11wapiGroups=gb15629dot11wapiGroups, gb15629dot11wapiConfigBKLifetime=gb15629dot11wapiConfigBKLifetime, gb15629dot11wapiStatsTable=gb15629dot11wapiStatsTable, gb15629dot11wapiBKIDUsed=gb15629dot11wapiBKIDUsed, gb15629wapiCompliances=gb15629wapiCompliances, gb15629dot11wapiPreauthenticationEnabled=gb15629dot11wapiPreauthenticationEnabled, gb15629dot11wapiStatsIndex=gb15629dot11wapiStatsIndex, gb15629dot11wapiConfigMulticastRekeyStrict=gb15629dot11wapiConfigMulticastRekeyStrict, gb15629dot11wapiUnicastCipherSelected=gb15629dot11wapiUnicastCipherSelected, gb15629dot11wapiConfigEntry=gb15629dot11wapiConfigEntry, gb15629dot11wapiAuthenticationSuiteRequested=gb15629dot11wapiAuthenticationSuiteRequested, gb15629dot11wapiStatsWPIReplayCounters=gb15629dot11wapiStatsWPIReplayCounters, gb15629dot11wapiStatsWAICertificateHandshakeFailures=gb15629dot11wapiStatsWAICertificateHandshakeFailures, wapiMIBObjects=wapiMIBObjects, gb15629dot11wapiConfigUnicastCiphersTable=gb15629dot11wapiConfigUnicastCiphersTable, gb15629_11=gb15629_11, gb15629dot11wapiConfigUnicastCipherSize=gb15629dot11wapiConfigUnicastCipherSize, gb15629dot11wapiControlledPortControl=gb15629dot11wapiControlledPortControl, gb15629dot11wapiConfigMulticastRekeyTime=gb15629dot11wapiConfigMulticastRekeyTime, gb15629dot11wapiConfigUnicastCipher=gb15629dot11wapiConfigUnicastCipher, gb15629dot11wapiStatsWAIFormatErrors=gb15629dot11wapiStatsWAIFormatErrors, bwips=bwips, gb15629dot11wapiConfigMulticastCipherSize=gb15629dot11wapiConfigMulticastCipherSize, gb15629_11_mibs=gb15629_11_mibs, gb15629dot11wapiConfigAuthenticationSuitesTable=gb15629dot11wapiConfigAuthenticationSuitesTable, gb15629dot11wapiStatsWAIAuthenticationResultFailures=gb15629dot11wapiStatsWAIAuthenticationResultFailures, gb15629dot11wapiConfigMulticastCipher=gb15629dot11wapiConfigMulticastCipher, gb15629dot11wapiConfigAuthenticationSuitesEntry=gb15629dot11wapiConfigAuthenticationSuitesEntry, gb15629dot11wapiConfigAuthenticationSuite=gb15629dot11wapiConfigAuthenticationSuite, gb15629dot11wapiStatsSelectedUnicastCipher=gb15629dot11wapiStatsSelectedUnicastCipher, gb15629dot11wapiConfigVersion=gb15629dot11wapiConfigVersion, gb15629dot11wapiAuthenticationSuiteSelected=gb15629dot11wapiAuthenticationSuiteSelected, gb15629dot11wapiStatsControlledPortStatus=gb15629dot11wapiStatsControlledPortStatus, gb15629dot11wapiBKcachingGroup=gb15629dot11wapiBKcachingGroup, gb15629dot11wapiStatsSTAAddress=gb15629dot11wapiStatsSTAAddress, gb15629dot11wapiConfigUnicastRekeyPackets=gb15629dot11wapiConfigUnicastRekeyPackets, gb15629dot11wapiConfigUnicastCipherIndex=gb15629dot11wapiConfigUnicastCipherIndex, gb15629dot11wapiOptionImplemented=gb15629dot11wapiOptionImplemented, gb15629dot11wapiUnicastCipherRequested=gb15629dot11wapiUnicastCipherRequested, gb15629dot11wapiConfigAuthenticationSuiteEnabled=gb15629dot11wapiConfigAuthenticationSuiteEnabled, gb15629dot11wapiConfigPSKPassPhrase=gb15629dot11wapiConfigPSKPassPhrase, gb15629dot11wapiConfigUnicastCiphersEntry=gb15629dot11wapiConfigUnicastCiphersEntry, gb15629dot11wapiStatsWPIMICErrors=gb15629dot11wapiStatsWPIMICErrors, gb15629dot11wapiBase=gb15629dot11wapiBase, gb15629dot11wapiConfigMulticastRekeyPackets=gb15629dot11wapiConfigMulticastRekeyPackets, gb15629dot11wapiStatsWAIDiscardCounters=gb15629dot11wapiStatsWAIDiscardCounters, gb15629dot11wapiMIB=gb15629dot11wapiMIB, gb15629dot11wapiStatsVersion=gb15629dot11wapiStatsVersion, gb15629dot11wapiControlledAuthControl=gb15629dot11wapiControlledAuthControl, gb15629dot11wapiStatsEntry=gb15629dot11wapiStatsEntry, gb15629dot11wapiConfigUnicastCipherEnabled=gb15629dot11wapiConfigUnicastCipherEnabled, gb15629=gb15629, gb15629dot11wapiConfigSATimeout=gb15629dot11wapiConfigSATimeout, wapiMIBConformance=wapiMIBConformance, gb15629dot11wapiStatsWPIDecryptableErrors=gb15629dot11wapiStatsWPIDecryptableErrors, gb15629dot11wapiConfigTable=gb15629dot11wapiConfigTable, gb15629dot11wapiConfigPSKValue=gb15629dot11wapiConfigPSKValue, gb15629dot11wapiMulticastCipherSelected=gb15629dot11wapiMulticastCipherSelected, gb15629dot11wapiStatsWAITimeoutCounters=gb15629dot11wapiStatsWAITimeoutCounters, gb15629dot11wapiStatsWAIMulticastHandshakeFailures=gb15629dot11wapiStatsWAIMulticastHandshakeFailures, gb15629dot11wapiPreauthenticationImplemented=gb15629dot11wapiPreauthenticationImplemented, gb15629dot11wapiConfigUnicastRekeyMethod=gb15629dot11wapiConfigUnicastRekeyMethod, cn=cn, gb15629dot11wapiConfigMulticastUpdateCount=gb15629dot11wapiConfigMulticastUpdateCount, gb15629dot11wapiConfigCertificateUpdateCount=gb15629dot11wapiConfigCertificateUpdateCount, gb15629dot11wapiMulticastCipherRequested=gb15629dot11wapiMulticastCipherRequested, PYSNMP_MODULE_ID=gb15629dot11wapiMIB, gb15629dot11wapiCompliance=gb15629dot11wapiCompliance, gb15629dot11wapiEnabled=gb15629dot11wapiEnabled, gb15629dot11wapiConfigAuthenticationSuiteIndex=gb15629dot11wapiConfigAuthenticationSuiteIndex)
