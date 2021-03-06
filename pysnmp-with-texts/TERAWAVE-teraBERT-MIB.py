#
# PySNMP MIB module TERAWAVE-teraBERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraBERT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, Bits, Integer32, TimeTicks, Counter64, MibIdentifier, enterprises, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "Integer32", "TimeTicks", "Counter64", "MibIdentifier", "enterprises", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraBERTGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 16))
teraBERTConfigureTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 16, 1), )
if mibBuilder.loadTexts: teraBERTConfigureTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTConfigureTable.setDescription(' table teraBERTConfigureTable')
teraBERTConfigureTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1), ).setIndexNames((0, "TERAWAVE-teraBERT-MIB", "ifIndex"))
if mibBuilder.loadTexts: teraBERTConfigureTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTConfigureTableEntry.setDescription(' table entry teraBERTConfigureTableEntry ')
teraBERTCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("start", 1), ("stop", 2), ("clear", 3), ("insert-err", 4), ("timer", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTCommand.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCommand.setDescription('')
teraBERTTestTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTTestTime.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTTestTime.setDescription('')
teraBERTSynThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTSynThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTSynThreshold.setDescription('')
teraBERTSESThresholdMantissa = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTSESThresholdMantissa.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTSESThresholdMantissa.setDescription('')
teraBERTSESThresholdExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTSESThresholdExponent.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTSESThresholdExponent.setDescription('')
teraBERTSynStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("yes", 0), ("no", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTSynStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTSynStatus.setDescription('')
teraBERTElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTElapsedTime.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTElapsedTime.setDescription('')
teraBERTPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("twoE11MinusOne", 1), ("twoE15MinusOne", 2), ("twoE20MinusOne", 3), ("twoE23MinusOne", 4), ("allOnes", 5), ("allZeroes", 6), ("alternatingOneZero", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraBERTPattern.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTPattern.setDescription('')
teraBERTCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 16, 2), )
if mibBuilder.loadTexts: teraBERTCurrentTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentTable.setDescription(' table teraBERTCurrentTable')
teraBERTCurrentTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1), ).setIndexNames((0, "TERAWAVE-teraBERT-MIB", "ifIndex"))
if mibBuilder.loadTexts: teraBERTCurrentTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentTableEntry.setDescription(' table entry teraBERTCurrentTableEntry ')
teraBERTCurrentCountInSync = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentCountInSync.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentCountInSync.setDescription('')
teraBERTCurrentRateInSync = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentRateInSync.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentRateInSync.setDescription('')
teraBERTCurrentESCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentESCount.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentESCount.setDescription('')
teraBERTCurrentSESCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentSESCount.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentSESCount.setDescription('')
teraBERTCurrentCSESCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentCSESCount.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentCSESCount.setDescription('')
teraBERTCurrentUASCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraBERTCurrentUASCount.setStatus('mandatory')
if mibBuilder.loadTexts: teraBERTCurrentUASCount.setDescription('')
mibBuilder.exportSymbols("TERAWAVE-teraBERT-MIB", teraBERTCurrentRateInSync=teraBERTCurrentRateInSync, terawave=terawave, teraBERTSynStatus=teraBERTSynStatus, teraBERTCommand=teraBERTCommand, teraBERTTestTime=teraBERTTestTime, teraBERTCurrentCountInSync=teraBERTCurrentCountInSync, teraBERTElapsedTime=teraBERTElapsedTime, teraBERTGroup=teraBERTGroup, teraBERTSynThreshold=teraBERTSynThreshold, teraBERTCurrentUASCount=teraBERTCurrentUASCount, teraBERTPattern=teraBERTPattern, teraBERTCurrentESCount=teraBERTCurrentESCount, teraBERTCurrentTableEntry=teraBERTCurrentTableEntry, teraBERTConfigureTable=teraBERTConfigureTable, teraBERTSESThresholdMantissa=teraBERTSESThresholdMantissa, teraBERTCurrentCSESCount=teraBERTCurrentCSESCount, teraBERTCurrentTable=teraBERTCurrentTable, teraBERTSESThresholdExponent=teraBERTSESThresholdExponent, teraBERTCurrentSESCount=teraBERTCurrentSESCount, teraBERTConfigureTableEntry=teraBERTConfigureTableEntry)
