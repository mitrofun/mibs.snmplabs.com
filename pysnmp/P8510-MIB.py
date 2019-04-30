#
# PySNMP MIB module P8510-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/P8510-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, ObjectIdentity, iso, Counter32, Unsigned32, Integer32, MibIdentifier, Gauge32, Counter64, Bits, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "Integer32", "MibIdentifier", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
p8510 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 1))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2))
channel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 3))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4))
sensorName = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorName.setStatus('mandatory')
ch1Name = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Name.setStatus('mandatory')
ch1Val = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Val.setStatus('mandatory')
ch1IntVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-550, 1250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1IntVal.setStatus('mandatory')
ch1Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Alarm.setStatus('mandatory')
ch1LimHi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimHi.setStatus('mandatory')
ch1LimLo = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimLo.setStatus('mandatory')
ch1LimHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1LimHyst.setStatus('mandatory')
ch1Delay = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Delay.setStatus('mandatory')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 5, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1), ).setIndexNames((0, "P8510-MIB", "ch1temperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
ch1temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1temperature.setStatus('mandatory')
mibBuilder.exportSymbols("P8510-MIB", messageString=messageString, comet=comet, DisplayString=DisplayString, channels=channels, ch1Val=ch1Val, ch1Delay=ch1Delay, historyTable=historyTable, historyEntry=historyEntry, p8510=p8510, channel1=channel1, ch1LimHi=ch1LimHi, ch1LimLo=ch1LimLo, tables=tables, ch1Name=ch1Name, ch1IntVal=ch1IntVal, ch1Alarm=ch1Alarm, traps=traps, sensorName=sensorName, products=products, ch1temperature=ch1temperature, settings=settings, ch1LimHyst=ch1LimHyst)