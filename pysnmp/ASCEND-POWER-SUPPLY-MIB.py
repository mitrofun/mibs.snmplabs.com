#
# PySNMP MIB module ASCEND-POWER-SUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-POWER-SUPPLY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
powerSupply, = mibBuilder.importSymbols("ASCEND-MIB", "powerSupply")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, Unsigned32, Integer32, IpAddress, TimeTicks, Counter32, Counter64, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
powerSupplyCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 18, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyCount.setStatus('mandatory')
powerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 529, 18, 2), )
if mibBuilder.loadTexts: powerSupplyTable.setStatus('mandatory')
powerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 18, 2, 1), ).setIndexNames((0, "ASCEND-POWER-SUPPLY-MIB", "powerSupplyIndex"))
if mibBuilder.loadTexts: powerSupplyEntry.setStatus('mandatory')
powerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyIndex.setStatus('mandatory')
powerSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("present", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyState.setStatus('mandatory')
powerSupplyOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("noFailure", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyOperationalState.setStatus('mandatory')
powerSupplySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplySerialNumber.setStatus('mandatory')
powerSupplyStateTrapState = MibScalar((1, 3, 6, 1, 4, 1, 529, 18, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: powerSupplyStateTrapState.setStatus('mandatory')
powerSupplyOperationalStateTrapState = MibScalar((1, 3, 6, 1, 4, 1, 529, 18, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: powerSupplyOperationalStateTrapState.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-POWER-SUPPLY-MIB", powerSupplyState=powerSupplyState, powerSupplySerialNumber=powerSupplySerialNumber, powerSupplyIndex=powerSupplyIndex, powerSupplyCount=powerSupplyCount, powerSupplyEntry=powerSupplyEntry, powerSupplyOperationalState=powerSupplyOperationalState, powerSupplyOperationalStateTrapState=powerSupplyOperationalStateTrapState, powerSupplyTable=powerSupplyTable, powerSupplyStateTrapState=powerSupplyStateTrapState)
