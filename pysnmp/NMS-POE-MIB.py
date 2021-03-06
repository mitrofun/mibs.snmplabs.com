#
# PySNMP MIB module NMS-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-POE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Gauge32, Integer32, ModuleIdentity, iso, IpAddress, Bits, Counter64, NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Gauge32", "Integer32", "ModuleIdentity", "iso", "IpAddress", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
poe = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236))
powerEtherTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1), )
if mibBuilder.loadTexts: powerEtherTable.setStatus('mandatory')
powerEtherTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1), ).setIndexNames((0, "NMS-POE-MIB", "ifIndex"))
if mibBuilder.loadTexts: powerEtherTableEntry.setStatus('mandatory')
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('mandatory')
ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDescr.setStatus('mandatory')
ifPethPortControlAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPethPortControlAbility.setStatus('mandatory')
ifPethPortMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifPethPortMaxPower.setStatus('mandatory')
ifPethPortConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPethPortConsumptionPower.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-POE-MIB", ifPethPortControlAbility=ifPethPortControlAbility, ifPethPortConsumptionPower=ifPethPortConsumptionPower, powerEtherTable=powerEtherTable, ifPethPortMaxPower=ifPethPortMaxPower, powerEtherTableEntry=powerEtherTableEntry, ifDescr=ifDescr, ifIndex=ifIndex, poe=poe)
