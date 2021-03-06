#
# PySNMP MIB module PDN-MPE-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpe_bridge, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-bridge")
VnidRange, = mibBuilder.importSymbols("PDN-TC", "VnidRange")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, Integer32, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "Integer32", "TimeTicks", "Unsigned32", "iso")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
mpePdnBridgeGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1))
mpePdnBridgeMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 2))
mpePdnDot1dGenericBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1))
mpePdnDot1dTpFdb = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2))
mpePdnDot1dBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnDot1dBridgeTable.setStatus('mandatory')
mpePdnDot1dBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnDot1dBridgeEntry.setStatus('mandatory')
mpePdnDot1dBaseBridgeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseBridgeAddress.setStatus('mandatory')
mpePdnDot1dBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseNumPorts.setStatus('mandatory')
mpePdnDot1dBaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dBaseType.setStatus('mandatory')
mpePdnDot1dTpLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpLearnedEntryDiscards.setStatus('mandatory')
mpePdnDot1dTpAgeingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingTime.setStatus('mandatory')
mpePdnDot1dTpAgeingCleanupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 500000)).clone(150)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnDot1dTpAgeingCleanupTime.setStatus('mandatory')
mpePdnDot1dTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1), )
if mibBuilder.loadTexts: mpePdnDot1dTpFdbTable.setStatus('mandatory')
mpePdnDot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbAddress"), (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbVnidId"))
if mibBuilder.loadTexts: mpePdnDot1dTpFdbEntry.setStatus('mandatory')
mpePdnDot1dTpFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAddress.setStatus('mandatory')
mpePdnDot1dTpFdbVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 2), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbVnidId.setStatus('mandatory')
mpePdnDot1dTpFdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbIfIndex.setStatus('mandatory')
mpePdnDot1dTpFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbStatus.setStatus('mandatory')
mpePdnDot1dTpFdbAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbAgeTime.setStatus('mandatory')
mpePdnDot1dTpFdbFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("permanentDHCP", 2), ("permanentCONFIGURED", 3), ("dynamic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnDot1dTpFdbFlags.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-MPE-BRIDGE-MIB", mpePdnBridgeMIBTraps=mpePdnBridgeMIBTraps, mpePdnDot1dBaseNumPorts=mpePdnDot1dBaseNumPorts, mpePdnDot1dTpFdbVnidId=mpePdnDot1dTpFdbVnidId, mpePdnDot1dTpFdbIfIndex=mpePdnDot1dTpFdbIfIndex, mpePdnDot1dTpLearnedEntryDiscards=mpePdnDot1dTpLearnedEntryDiscards, mpePdnDot1dTpAgeingTime=mpePdnDot1dTpAgeingTime, mpePdnDot1dTpFdbTable=mpePdnDot1dTpFdbTable, mpePdnDot1dGenericBridge=mpePdnDot1dGenericBridge, mpePdnDot1dTpFdbAddress=mpePdnDot1dTpFdbAddress, mpePdnDot1dBridgeEntry=mpePdnDot1dBridgeEntry, mpePdnDot1dTpFdbEntry=mpePdnDot1dTpFdbEntry, mpePdnDot1dTpFdbStatus=mpePdnDot1dTpFdbStatus, mpePdnDot1dTpFdb=mpePdnDot1dTpFdb, mpePdnDot1dBaseType=mpePdnDot1dBaseType, mpePdnDot1dTpAgeingCleanupTime=mpePdnDot1dTpAgeingCleanupTime, mpePdnDot1dBaseBridgeAddress=mpePdnDot1dBaseBridgeAddress, mpePdnBridgeGenericMIBObjects=mpePdnBridgeGenericMIBObjects, mpePdnDot1dTpFdbFlags=mpePdnDot1dTpFdbFlags, mpePdnDot1dBridgeTable=mpePdnDot1dBridgeTable, mpePdnDot1dTpFdbAgeTime=mpePdnDot1dTpFdbAgeTime)
