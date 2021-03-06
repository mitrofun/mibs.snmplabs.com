#
# PySNMP MIB module Dlink-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Gauge32, Bits, MibIdentifier, Integer32, Unsigned32, Counter64, iso, IpAddress, Counter32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Gauge32", "Bits", "MibIdentifier", "Integer32", "Unsigned32", "Counter64", "iso", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Dlink, Inc.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("sw-storm-control", 7))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 2, 1), ).setIndexNames((0, "Dlink-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
mibBuilder.exportSymbols("Dlink-ERRDISABLE-RECOVERY-MIB", PYSNMP_MODULE_ID=rlErrdisableRecovery, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval)
