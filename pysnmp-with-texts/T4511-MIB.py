#
# PySNMP MIB module T4511-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T4511-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Integer32, Counter64, Bits, Gauge32, NotificationType, ObjectIdentity, enterprises, MibIdentifier, Counter32, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Integer32", "Counter64", "Bits", "Gauge32", "NotificationType", "ObjectIdentity", "enterprises", "MibIdentifier", "Counter32", "ModuleIdentity", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t4511 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
readings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2))
readingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
if mibBuilder.loadTexts: temperature.setDescription('Temperature')
templow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: templow.setStatus('mandatory')
if mibBuilder.loadTexts: templow.setDescription('Temperature Limit Low')
temphigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temphigh.setStatus('mandatory')
if mibBuilder.loadTexts: temphigh.setDescription('Temperature Limit High')
temptime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temptime.setStatus('mandatory')
if mibBuilder.loadTexts: temptime.setDescription('Temperature alaram delay')
tempHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHyst.setStatus('mandatory')
if mibBuilder.loadTexts: tempHyst.setDescription('Temperature hysteresis')
temperaturei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperaturei.setStatus('mandatory')
if mibBuilder.loadTexts: temperaturei.setDescription('Temperature *10')
templowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: templowi.setStatus('mandatory')
if mibBuilder.loadTexts: templowi.setDescription('Temperature Limit Low *10')
temphighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temphighi.setStatus('mandatory')
if mibBuilder.loadTexts: temphighi.setDescription('Temperature Limit High *10')
humiditylowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humiditylowi.setStatus('mandatory')
if mibBuilder.loadTexts: humiditylowi.setDescription('Humidity Limit Low *10')
temptimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temptimei.setStatus('mandatory')
if mibBuilder.loadTexts: temptimei.setDescription('Temperature alaram delay')
tempHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempHysti.setStatus('mandatory')
if mibBuilder.loadTexts: tempHysti.setDescription('Temperature hysteresis *10')
humidityHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityHysti.setStatus('mandatory')
if mibBuilder.loadTexts: humidityHysti.setDescription('Humidity hysteresis *10')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
if mibBuilder.loadTexts: messageString.setDescription('Message giving more detailed information on alarms.')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: alarmTemperature.setDescription('Temperature alarm 0 = temperature OK 1 = temperature too high 2 = temperature too low')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
if mibBuilder.loadTexts: historyTable.setDescription('Table of the history values.')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T4511-MIB", "histtemperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
if mibBuilder.loadTexts: historyEntry.setDescription('History values entries.')
histtemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histtemperature.setStatus('mandatory')
if mibBuilder.loadTexts: histtemperature.setDescription('Temperature reading.')
mibBuilder.exportSymbols("T4511-MIB", templowi=templowi, settingsint=settingsint, tempHysti=tempHysti, DisplayString=DisplayString, messageString=messageString, tempHyst=tempHyst, readingsint=readingsint, humiditylowi=humiditylowi, alarmTemperature=alarmTemperature, temphighi=temphighi, historyEntry=historyEntry, historyTable=historyTable, settings=settings, traps=traps, tables=tables, comet=comet, products=products, temperature=temperature, temptimei=temptimei, temphigh=temphigh, readings=readings, t4511=t4511, temperaturei=temperaturei, templow=templow, temptime=temptime, humidityHysti=humidityHysti, histtemperature=histtemperature)
