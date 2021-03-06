#
# PySNMP MIB module RAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
MmEndpointID, MmAliasAddress, MmGlobalIdentifier, mmH323Root, MmH225Crv, MmCallType, MmGatekeeperID, MmAliasTag, MmTAddressTag = mibBuilder.importSymbols("MULTI-MEDIA-MIB-TC", "MmEndpointID", "MmAliasAddress", "MmGlobalIdentifier", "mmH323Root", "MmH225Crv", "MmCallType", "MmGatekeeperID", "MmAliasTag", "MmTAddressTag")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, ObjectIdentity, MibIdentifier, Bits, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter64, TimeTicks, NotificationType, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "Bits", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "iso")
DateAndTime, TextualConvention, DisplayString, TruthValue, TAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString", "TruthValue", "TAddress", "RowStatus")
ras = ModuleIdentity((0, 0, 8, 341, 1, 1, 2))
if mibBuilder.loadTexts: ras.setLastUpdated('9812162253Z')
if mibBuilder.loadTexts: ras.setOrganization('ITU-T')
rasConfiguration = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 1))
rasRegistration = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 2))
rasAdmission = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 3))
rasStats = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 4))
rasEvents = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 5, 0))
rasConfigurationTable = MibTable((0, 0, 8, 341, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: rasConfigurationTable.setStatus('current')
rasConfigurationTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rasConfigurationTableEntry.setStatus('current')
rasConfigurationGatekeeperIdentifier = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 1), MmGatekeeperID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasConfigurationGatekeeperIdentifier.setStatus('current')
rasConfigurationTimer = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 2), Integer32().clone(3)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rasConfigurationTimer.setStatus('current')
rasConfigurationMaxNumberOfRetries = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 3), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rasConfigurationMaxNumberOfRetries.setStatus('current')
rasConfigurationGatekeeperDiscoveryAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 4), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasConfigurationGatekeeperDiscoveryAddressTag.setStatus('current')
rasConfigurationGatekeeperDiscoveryAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 5), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasConfigurationGatekeeperDiscoveryAddress.setStatus('current')
rasRegistrationTable = MibTable((0, 0, 8, 341, 1, 1, 2, 2, 1), )
if mibBuilder.loadTexts: rasRegistrationTable.setStatus('current')
rasRegistrationTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"), (0, "RAS-MIB", "rasRegistrationSrcRasAddressTag"), (0, "RAS-MIB", "rasRegistrationSrcRasAddress"))
if mibBuilder.loadTexts: rasRegistrationTableEntry.setStatus('current')
rasRegistrationCallSignallingAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 1), MmTAddressTag())
if mibBuilder.loadTexts: rasRegistrationCallSignallingAddressTag.setStatus('current')
rasRegistrationCallSignallingAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 2), TAddress())
if mibBuilder.loadTexts: rasRegistrationCallSignallingAddress.setStatus('current')
rasRegistrationSrcRasAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 3), MmTAddressTag())
if mibBuilder.loadTexts: rasRegistrationSrcRasAddressTag.setStatus('current')
rasRegistrationSrcRasAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 4), TAddress())
if mibBuilder.loadTexts: rasRegistrationSrcRasAddress.setStatus('current')
rasRegistrationIsGatekeeper = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationIsGatekeeper.setStatus('current')
rasRegistrationGatekeeperId = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 6), MmGatekeeperID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationGatekeeperId.setStatus('current')
rasRegistrationEndpointId = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 7), MmEndpointID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationEndpointId.setStatus('current')
rasRegistrationEncryption = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationEncryption.setStatus('current')
rasRegistrationWillSupplyUUIE = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationWillSupplyUUIE.setStatus('current')
rasRegistrationIntegrityCheckValue = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationIntegrityCheckValue.setStatus('current')
rasRegistrationTableNumberOfAliases = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationTableNumberOfAliases.setStatus('current')
rasRegistrationTableRowStatus = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rasRegistrationTableRowStatus.setStatus('current')
rasRegistrationEndpointType = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationEndpointType.setStatus('current')
rasRegistrationPregrantedARQ = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationPregrantedARQ.setStatus('current')
rasRegistrationIsregisteredByRRQ = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationIsregisteredByRRQ.setStatus('current')
rasRegistrationAliasTable = MibTable((0, 0, 8, 341, 1, 1, 2, 2, 2), )
if mibBuilder.loadTexts: rasRegistrationAliasTable.setStatus('current')
rasRegistrationAliasTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"), (0, "RAS-MIB", "rasRegistrationAliasTableIndex"))
if mibBuilder.loadTexts: rasRegistrationAliasTableEntry.setStatus('current')
rasRegistrationAliasTableIndex = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rasRegistrationAliasTableIndex.setStatus('current')
rasRegistrationAliasTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 2), MmAliasTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAliasTag.setStatus('current')
rasRegistrationAlias = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 3), MmAliasAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAlias.setStatus('current')
rasRegistrationRasAddressTable = MibTable((0, 0, 8, 341, 1, 1, 2, 2, 3), )
if mibBuilder.loadTexts: rasRegistrationRasAddressTable.setStatus('current')
rasRegistrationRasAddressTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"), (0, "RAS-MIB", "rasRegistrationRasAddressTableIndex"))
if mibBuilder.loadTexts: rasRegistrationRasAddressTableEntry.setStatus('current')
rasRegistrationRasAddressTableIndex = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rasRegistrationRasAddressTableIndex.setStatus('current')
rasRegistrationAdditionalSrcRasAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 2), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAdditionalSrcRasAddressTag.setStatus('current')
rasRegistrationAdditionalSrcRasAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 3), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAdditionalSrcRasAddress.setStatus('current')
rasRegistrationCallSignalingAddressTable = MibTable((0, 0, 8, 341, 1, 1, 2, 2, 4), )
if mibBuilder.loadTexts: rasRegistrationCallSignalingAddressTable.setStatus('current')
rasRegistrationCallSignalingAddressTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"), (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"), (0, "RAS-MIB", "rasRegistrationCallSignalingAddressTableIndex"))
if mibBuilder.loadTexts: rasRegistrationCallSignalingAddressTableEntry.setStatus('current')
rasRegistrationCallSignalingAddressTableIndex = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: rasRegistrationCallSignalingAddressTableIndex.setStatus('current')
rasRegistrationAdditionalCallSignalingAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 2), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAdditionalCallSignalingAddressTag.setStatus('current')
rasRegistrationAdditionalCallSignalingAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 3), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasRegistrationAdditionalCallSignalingAddress.setStatus('current')
rasAdmissionTable = MibTable((0, 0, 8, 341, 1, 1, 2, 3, 1), )
if mibBuilder.loadTexts: rasAdmissionTable.setStatus('current')
rasAdmissionTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAS-MIB", "rasAdmissionSrcCallSignallingAddress"), (0, "RAS-MIB", "rasAdmissionRasAddress"), (0, "RAS-MIB", "rasAdmissionCallIdentifier"))
if mibBuilder.loadTexts: rasAdmissionTableEntry.setStatus('current')
rasAdmissionSrcCallSignallingAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 1), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSrcCallSignallingAddressTag.setStatus('current')
rasAdmissionSrcCallSignallingAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 2), TAddress())
if mibBuilder.loadTexts: rasAdmissionSrcCallSignallingAddress.setStatus('current')
rasAdmissionDestCallSignallingAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 3), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestCallSignallingAddressTag.setStatus('current')
rasAdmissionDestCallSignallingAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestCallSignallingAddress.setStatus('current')
rasAdmissionCallIdentifier = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 5), MmGlobalIdentifier())
if mibBuilder.loadTexts: rasAdmissionCallIdentifier.setStatus('current')
rasAdmissionConferenceId = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 6), MmGlobalIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionConferenceId.setStatus('current')
rasAdmissionRasAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 7), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionRasAddressTag.setStatus('current')
rasAdmissionRasAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 8), TAddress())
if mibBuilder.loadTexts: rasAdmissionRasAddress.setStatus('current')
rasAdmissionCRV = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 9), MmH225Crv()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionCRV.setStatus('current')
rasAdmissionIsGatekeeper = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionIsGatekeeper.setStatus('current')
rasAdmissionSrcAliasAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 11), MmAliasTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSrcAliasAddressTag.setStatus('current')
rasAdmissionSrcAliasAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 12), MmAliasAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSrcAliasAddress.setStatus('current')
rasAdmissionDestAliasAddressTag = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 13), MmAliasTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestAliasAddressTag.setStatus('current')
rasAdmissionDestAliasAddress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 14), MmAliasAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestAliasAddress.setStatus('current')
rasAdmissionAnswerCallIndicator = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("caller", 1), ("callee", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionAnswerCallIndicator.setStatus('current')
rasAdmissionTime = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 16), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionTime.setStatus('current')
rasAdmissionEndpointId = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 17), MmEndpointID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionEndpointId.setStatus('current')
rasAdmissionBandwidth = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionBandwidth.setStatus('current')
rasAdmissionIRRFrequency = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionIRRFrequency.setStatus('current')
rasAdmissionCallType = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 20), MmCallType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionCallType.setStatus('current')
rasAdmissionCallModel = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("direct", 1), ("gatekeeperRouted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionCallModel.setStatus('current')
rasAdmissionSrcHandlesBandwidth = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 22), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSrcHandlesBandwidth.setStatus('current')
rasAdmissionDestHandlesBandwidth = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestHandlesBandwidth.setStatus('current')
rasAdmissionSecurity = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSecurity.setStatus('current')
rasAdmissionSrcWillSupplyUUIE = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionSrcWillSupplyUUIE.setStatus('current')
rasAdmissionDestWillSupplyUUIE = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 26), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasAdmissionDestWillSupplyUUIE.setStatus('current')
rasAdmissionTableRowStatus = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rasAdmissionTableRowStatus.setStatus('current')
rasStatsTable = MibTable((0, 0, 8, 341, 1, 1, 2, 4, 1), )
if mibBuilder.loadTexts: rasStatsTable.setStatus('current')
rasStatsTableEntry = MibTableRow((0, 0, 8, 341, 1, 1, 2, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rasStatsTableEntry.setStatus('current')
rasStatsGatekeeperConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsGatekeeperConfirms.setStatus('current')
rasStatsGatekeeperRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsGatekeeperRejects.setStatus('current')
rasStatsRegistrationConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsRegistrationConfirms.setStatus('current')
rasStatsRegistrationRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsRegistrationRejects.setStatus('current')
rasStatsUnregistrationConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsUnregistrationConfirms.setStatus('current')
rasStatsUnregistrationRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsUnregistrationRejects.setStatus('current')
rasStatsAdmissionConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsAdmissionConfirms.setStatus('current')
rasStatsAdmissionRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsAdmissionRejects.setStatus('current')
rasStatsBandwidthConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsBandwidthConfirms.setStatus('current')
rasStatsBandwidthRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsBandwidthRejects.setStatus('current')
rasStatsDisengageConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsDisengageConfirms.setStatus('current')
rasStatsDisengageRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsDisengageRejects.setStatus('current')
rasStatsLocationConfirms = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsLocationConfirms.setStatus('current')
rasStatsLocationRejects = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsLocationRejects.setStatus('current')
rasStatsInfoRequests = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsInfoRequests.setStatus('current')
rasStatsInfoRequestResponses = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsInfoRequestResponses.setStatus('current')
rasStatsnonStandardMessages = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsnonStandardMessages.setStatus('current')
rasStatsUnknownMessages = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsUnknownMessages.setStatus('current')
rasStatsRequestInProgress = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsRequestInProgress.setStatus('current')
rasStatsResourceAvailabilityIndicator = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsResourceAvailabilityIndicator.setStatus('current')
rasStatsResourceAvailabilityConfirm = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsResourceAvailabilityConfirm.setStatus('current')
rasStatsRegisteredEndpointsNo = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsRegisteredEndpointsNo.setStatus('current')
rasStatsAdmittedEndpointsNo = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsAdmittedEndpointsNo.setStatus('current')
rasStatsINAKs = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsINAKs.setStatus('current')
rasStatsIACKs = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsIACKs.setStatus('current')
rasStatsGkRoutedCalls = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsGkRoutedCalls.setStatus('current')
rasStatsResourceAvailabilityIndications = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsResourceAvailabilityIndications.setStatus('current')
rasStatsResourceAvailabilityConfirmations = MibTableColumn((0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rasStatsResourceAvailabilityConfirmations.setStatus('current')
lastArjReason = MibScalar((0, 0, 8, 341, 1, 1, 2, 5, 0, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("calledPartyNotRegistered", 1), ("invalidPermission", 2), ("requestDenied", 3), ("undefinedReason", 4), ("callerNotRegistered", 5), ("routeCallToGatekeeper", 6), ("invalidEndpointIdentifier", 7), ("resourceUnavailable", 8), ("securityDenial", 9), ("qosControlNotSupported", 10), ("incompleteAddress", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastArjReason.setStatus('current')
lastArjRasAddressTag = MibScalar((0, 0, 8, 341, 1, 1, 2, 5, 0, 2), MmTAddressTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastArjRasAddressTag.setStatus('current')
lastArjRasAddress = MibScalar((0, 0, 8, 341, 1, 1, 2, 5, 0, 3), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastArjRasAddress.setStatus('current')
admissionReject = NotificationType((0, 0, 8, 341, 1, 1, 2, 5, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("RAS-MIB", "lastArjReason"), ("RAS-MIB", "lastArjRasAddressTag"), ("RAS-MIB", "lastArjRasAddress"))
if mibBuilder.loadTexts: admissionReject.setStatus('current')
rasMIBConformance = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 6))
rasMIBGroups = MibIdentifier((0, 0, 8, 341, 1, 1, 2, 6, 1))
rasConfigurationGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 2, 6, 1, 1)).setObjects(("RAS-MIB", "rasConfigurationTimer"), ("RAS-MIB", "rasConfigurationMaxNumberOfRetries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasConfigurationGroup = rasConfigurationGroup.setStatus('current')
rasRegistrationGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 2, 6, 1, 2)).setObjects(("RAS-MIB", "rasRegistrationIsGatekeeper"), ("RAS-MIB", "rasRegistrationGatekeeperId"), ("RAS-MIB", "rasRegistrationEndpointId"), ("RAS-MIB", "rasRegistrationEncryption"), ("RAS-MIB", "rasRegistrationWillSupplyUUIE"), ("RAS-MIB", "rasRegistrationIntegrityCheckValue"), ("RAS-MIB", "rasRegistrationTableNumberOfAliases"), ("RAS-MIB", "rasRegistrationEndpointType"), ("RAS-MIB", "rasRegistrationPregrantedARQ"), ("RAS-MIB", "rasRegistrationAlias"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasRegistrationGroup = rasRegistrationGroup.setStatus('current')
rasAdmissionGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 2, 6, 1, 3)).setObjects(("RAS-MIB", "rasAdmissionConferenceId"), ("RAS-MIB", "rasAdmissionRasAddressTag"), ("RAS-MIB", "rasAdmissionCRV"), ("RAS-MIB", "rasAdmissionIsGatekeeper"), ("RAS-MIB", "rasAdmissionSrcCallSignallingAddressTag"), ("RAS-MIB", "rasAdmissionDestCallSignallingAddressTag"), ("RAS-MIB", "rasAdmissionDestCallSignallingAddress"), ("RAS-MIB", "rasAdmissionSrcAliasAddressTag"), ("RAS-MIB", "rasAdmissionSrcAliasAddress"), ("RAS-MIB", "rasAdmissionDestAliasAddressTag"), ("RAS-MIB", "rasAdmissionDestAliasAddress"), ("RAS-MIB", "rasAdmissionAnswerCallIndicator"), ("RAS-MIB", "rasAdmissionTime"), ("RAS-MIB", "rasAdmissionEndpointId"), ("RAS-MIB", "rasAdmissionBandwidth"), ("RAS-MIB", "rasAdmissionIRRFrequency"), ("RAS-MIB", "rasAdmissionCallType"), ("RAS-MIB", "rasAdmissionCallModel"), ("RAS-MIB", "rasAdmissionSrcHandlesBandwidth"), ("RAS-MIB", "rasAdmissionDestHandlesBandwidth"), ("RAS-MIB", "rasAdmissionSecurity"), ("RAS-MIB", "rasAdmissionSrcWillSupplyUUIE"), ("RAS-MIB", "rasAdmissionDestWillSupplyUUIE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasAdmissionGroup = rasAdmissionGroup.setStatus('current')
rasStatsGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 2, 6, 1, 4)).setObjects(("RAS-MIB", "rasStatsGatekeeperConfirms"), ("RAS-MIB", "rasStatsGatekeeperRejects"), ("RAS-MIB", "rasStatsRegistrationConfirms"), ("RAS-MIB", "rasStatsRegistrationRejects"), ("RAS-MIB", "rasStatsUnregistrationConfirms"), ("RAS-MIB", "rasStatsUnregistrationRejects"), ("RAS-MIB", "rasStatsAdmissionConfirms"), ("RAS-MIB", "rasStatsAdmissionRejects"), ("RAS-MIB", "rasStatsBandwidthConfirms"), ("RAS-MIB", "rasStatsBandwidthRejects"), ("RAS-MIB", "rasStatsDisengageConfirms"), ("RAS-MIB", "rasStatsDisengageRejects"), ("RAS-MIB", "rasStatsLocationConfirms"), ("RAS-MIB", "rasStatsLocationRejects"), ("RAS-MIB", "rasStatsInfoRequests"), ("RAS-MIB", "rasStatsInfoRequestResponses"), ("RAS-MIB", "rasStatsnonStandardMessages"), ("RAS-MIB", "rasStatsUnknownMessages"), ("RAS-MIB", "rasStatsRequestInProgress"), ("RAS-MIB", "rasStatsResourceAvailabilityIndicator"), ("RAS-MIB", "rasStatsResourceAvailabilityConfirm"), ("RAS-MIB", "rasStatsRegisteredEndpointsNo"), ("RAS-MIB", "rasStatsAdmittedEndpointsNo"), ("RAS-MIB", "rasStatsINAKs"), ("RAS-MIB", "rasStatsIACKs"), ("RAS-MIB", "rasStatsGkRoutedCalls"), ("RAS-MIB", "rasStatsResourceAvailabilityIndications"), ("RAS-MIB", "rasStatsResourceAvailabilityConfirmations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasStatsGroup = rasStatsGroup.setStatus('current')
rasEventsGroup = ObjectGroup((0, 0, 8, 341, 1, 1, 2, 6, 1, 5)).setObjects(("RAS-MIB", "lastArjReason"), ("RAS-MIB", "lastArjRasAddressTag"), ("RAS-MIB", "lastArjRasAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasEventsGroup = rasEventsGroup.setStatus('current')
rasMIBCompliance = ModuleCompliance((0, 0, 8, 341, 1, 1, 2, 6, 2)).setObjects(("RAS-MIB", "rasRegistrationGroup"), ("RAS-MIB", "rasAdmissionGroup"), ("RAS-MIB", "rasStatsGroup"), ("RAS-MIB", "rasEventsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rasMIBCompliance = rasMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("RAS-MIB", rasStatsBandwidthRejects=rasStatsBandwidthRejects, PYSNMP_MODULE_ID=ras, rasRegistrationAdditionalCallSignalingAddressTag=rasRegistrationAdditionalCallSignalingAddressTag, rasRegistrationSrcRasAddressTag=rasRegistrationSrcRasAddressTag, rasRegistrationAdditionalSrcRasAddressTag=rasRegistrationAdditionalSrcRasAddressTag, rasRegistrationCallSignallingAddress=rasRegistrationCallSignallingAddress, rasRegistrationEndpointType=rasRegistrationEndpointType, rasStatsGatekeeperRejects=rasStatsGatekeeperRejects, rasRegistration=rasRegistration, rasRegistrationCallSignalingAddressTable=rasRegistrationCallSignalingAddressTable, rasRegistrationAdditionalSrcRasAddress=rasRegistrationAdditionalSrcRasAddress, rasRegistrationRasAddressTableIndex=rasRegistrationRasAddressTableIndex, rasStatsAdmissionRejects=rasStatsAdmissionRejects, rasRegistrationCallSignalingAddressTableIndex=rasRegistrationCallSignalingAddressTableIndex, rasAdmissionDestAliasAddress=rasAdmissionDestAliasAddress, rasStatsDisengageRejects=rasStatsDisengageRejects, rasRegistrationCallSignallingAddressTag=rasRegistrationCallSignallingAddressTag, rasMIBCompliance=rasMIBCompliance, rasStatsAdmittedEndpointsNo=rasStatsAdmittedEndpointsNo, rasAdmissionDestCallSignallingAddressTag=rasAdmissionDestCallSignallingAddressTag, rasAdmissionConferenceId=rasAdmissionConferenceId, rasMIBConformance=rasMIBConformance, rasStatsGatekeeperConfirms=rasStatsGatekeeperConfirms, rasConfigurationMaxNumberOfRetries=rasConfigurationMaxNumberOfRetries, rasRegistrationPregrantedARQ=rasRegistrationPregrantedARQ, rasRegistrationGatekeeperId=rasRegistrationGatekeeperId, rasStatsTableEntry=rasStatsTableEntry, rasRegistrationAlias=rasRegistrationAlias, rasAdmissionTime=rasAdmissionTime, rasRegistrationAliasTag=rasRegistrationAliasTag, rasRegistrationAliasTableEntry=rasRegistrationAliasTableEntry, rasRegistrationRasAddressTableEntry=rasRegistrationRasAddressTableEntry, rasAdmissionSrcAliasAddress=rasAdmissionSrcAliasAddress, rasAdmissionRasAddressTag=rasAdmissionRasAddressTag, lastArjRasAddress=lastArjRasAddress, rasStatsGroup=rasStatsGroup, rasStatsGkRoutedCalls=rasStatsGkRoutedCalls, rasAdmissionAnswerCallIndicator=rasAdmissionAnswerCallIndicator, rasConfigurationGatekeeperIdentifier=rasConfigurationGatekeeperIdentifier, rasConfigurationTimer=rasConfigurationTimer, rasRegistrationTableEntry=rasRegistrationTableEntry, rasStatsRegisteredEndpointsNo=rasStatsRegisteredEndpointsNo, rasAdmissionCallIdentifier=rasAdmissionCallIdentifier, rasStatsResourceAvailabilityConfirmations=rasStatsResourceAvailabilityConfirmations, ras=ras, rasAdmissionDestWillSupplyUUIE=rasAdmissionDestWillSupplyUUIE, rasConfigurationTableEntry=rasConfigurationTableEntry, rasAdmissionSrcCallSignallingAddressTag=rasAdmissionSrcCallSignallingAddressTag, rasAdmissionSrcWillSupplyUUIE=rasAdmissionSrcWillSupplyUUIE, rasConfigurationGatekeeperDiscoveryAddressTag=rasConfigurationGatekeeperDiscoveryAddressTag, rasAdmissionTable=rasAdmissionTable, rasRegistrationEncryption=rasRegistrationEncryption, rasStatsUnregistrationRejects=rasStatsUnregistrationRejects, rasStatsnonStandardMessages=rasStatsnonStandardMessages, rasConfigurationTable=rasConfigurationTable, rasAdmissionCRV=rasAdmissionCRV, rasRegistrationGroup=rasRegistrationGroup, rasAdmissionCallModel=rasAdmissionCallModel, rasStatsRegistrationRejects=rasStatsRegistrationRejects, lastArjReason=lastArjReason, rasAdmission=rasAdmission, rasStatsResourceAvailabilityIndicator=rasStatsResourceAvailabilityIndicator, rasRegistrationAliasTableIndex=rasRegistrationAliasTableIndex, rasRegistrationAliasTable=rasRegistrationAliasTable, rasConfigurationGatekeeperDiscoveryAddress=rasConfigurationGatekeeperDiscoveryAddress, rasStatsAdmissionConfirms=rasStatsAdmissionConfirms, rasRegistrationIsGatekeeper=rasRegistrationIsGatekeeper, rasAdmissionTableRowStatus=rasAdmissionTableRowStatus, rasAdmissionSrcCallSignallingAddress=rasAdmissionSrcCallSignallingAddress, rasAdmissionSrcHandlesBandwidth=rasAdmissionSrcHandlesBandwidth, rasStatsTable=rasStatsTable, rasRegistrationSrcRasAddress=rasRegistrationSrcRasAddress, rasAdmissionSecurity=rasAdmissionSecurity, rasStatsResourceAvailabilityIndications=rasStatsResourceAvailabilityIndications, rasStatsResourceAvailabilityConfirm=rasStatsResourceAvailabilityConfirm, rasAdmissionCallType=rasAdmissionCallType, rasAdmissionDestCallSignallingAddress=rasAdmissionDestCallSignallingAddress, rasAdmissionBandwidth=rasAdmissionBandwidth, rasConfigurationGroup=rasConfigurationGroup, rasStatsINAKs=rasStatsINAKs, admissionReject=admissionReject, rasAdmissionDestAliasAddressTag=rasAdmissionDestAliasAddressTag, rasStatsIACKs=rasStatsIACKs, rasStatsRegistrationConfirms=rasStatsRegistrationConfirms, rasRegistrationCallSignalingAddressTableEntry=rasRegistrationCallSignalingAddressTableEntry, rasStatsDisengageConfirms=rasStatsDisengageConfirms, lastArjRasAddressTag=lastArjRasAddressTag, rasStatsLocationConfirms=rasStatsLocationConfirms, rasRegistrationWillSupplyUUIE=rasRegistrationWillSupplyUUIE, rasEventsGroup=rasEventsGroup, rasRegistrationIsregisteredByRRQ=rasRegistrationIsregisteredByRRQ, rasRegistrationRasAddressTable=rasRegistrationRasAddressTable, rasStatsUnregistrationConfirms=rasStatsUnregistrationConfirms, rasStatsInfoRequests=rasStatsInfoRequests, rasStatsLocationRejects=rasStatsLocationRejects, rasAdmissionIsGatekeeper=rasAdmissionIsGatekeeper, rasStatsInfoRequestResponses=rasStatsInfoRequestResponses, rasStatsBandwidthConfirms=rasStatsBandwidthConfirms, rasStatsRequestInProgress=rasStatsRequestInProgress, rasRegistrationIntegrityCheckValue=rasRegistrationIntegrityCheckValue, rasAdmissionSrcAliasAddressTag=rasAdmissionSrcAliasAddressTag, rasRegistrationTable=rasRegistrationTable, rasStats=rasStats, rasAdmissionRasAddress=rasAdmissionRasAddress, rasAdmissionIRRFrequency=rasAdmissionIRRFrequency, rasRegistrationTableRowStatus=rasRegistrationTableRowStatus, rasRegistrationAdditionalCallSignalingAddress=rasRegistrationAdditionalCallSignalingAddress, rasRegistrationTableNumberOfAliases=rasRegistrationTableNumberOfAliases, rasStatsUnknownMessages=rasStatsUnknownMessages, rasAdmissionTableEntry=rasAdmissionTableEntry, rasAdmissionGroup=rasAdmissionGroup, rasAdmissionEndpointId=rasAdmissionEndpointId, rasAdmissionDestHandlesBandwidth=rasAdmissionDestHandlesBandwidth, rasConfiguration=rasConfiguration, rasEvents=rasEvents, rasRegistrationEndpointId=rasRegistrationEndpointId, rasMIBGroups=rasMIBGroups)
