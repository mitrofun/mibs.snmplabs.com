#
# PySNMP MIB module TERAWAVE-terads1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-terads1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, NotificationType, Unsigned32, TimeTicks, Integer32, MibIdentifier, ModuleIdentity, ObjectIdentity, iso, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "NotificationType", "Unsigned32", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "iso", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraDs1Group = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 11))
teradsx1CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 11, 1), )
if mibBuilder.loadTexts: teradsx1CurrentTable.setStatus('mandatory')
teradsx1CurrentTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1), ).setIndexNames((0, "TERAWAVE-terads1-MIB", "teradsx1CurrentIndex"))
if mibBuilder.loadTexts: teradsx1CurrentTableEntry.setStatus('mandatory')
teradsx1CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentIndex.setStatus('mandatory')
teradsx1CurrentESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentESs.setStatus('mandatory')
teradsx1CurrentSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentSESs.setStatus('mandatory')
teradsx1CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentSEFSs.setStatus('mandatory')
teradsx1CurrentUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentUASs.setStatus('mandatory')
teradsx1CurrentCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentCSSs.setStatus('mandatory')
teradsx1CurrentPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentPCVs.setStatus('mandatory')
teradsx1CurrentLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentLESs.setStatus('mandatory')
teradsx1CurrentBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentBESs.setStatus('mandatory')
teradsx1CurrentDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentDMs.setStatus('mandatory')
teradsx1CurrentLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentLCVs.setStatus('mandatory')
teradsx1CurrentLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentLOF.setStatus('mandatory')
teradsx1CurrentYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentYELLOW.setStatus('mandatory')
teradsx1CurrentAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1CurrentAIS.setStatus('mandatory')
teraStandarddsx1CurrentLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1CurrentLOF.setStatus('mandatory')
teraStandarddsx1CurrentYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1CurrentYELLOW.setStatus('mandatory')
teraStandarddsx1CurrentAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1CurrentAIS.setStatus('mandatory')
teraStandarddsx1CurrentLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 1, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1CurrentLOSs.setStatus('mandatory')
teradsx1IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 11, 2), )
if mibBuilder.loadTexts: teradsx1IntervalTable.setStatus('mandatory')
teradsx1IntervalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1), ).setIndexNames((0, "TERAWAVE-terads1-MIB", "teradsx1IntervalIndex"), (0, "TERAWAVE-terads1-MIB", "teradsx1IntervalNumber"))
if mibBuilder.loadTexts: teradsx1IntervalTableEntry.setStatus('mandatory')
teradsx1IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalIndex.setStatus('mandatory')
teradsx1IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalNumber.setStatus('mandatory')
teradsx1IntervalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalESs.setStatus('mandatory')
teradsx1IntervalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalSESs.setStatus('mandatory')
teradsx1IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalSEFSs.setStatus('mandatory')
teradsx1IntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalUASs.setStatus('mandatory')
teradsx1IntervalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalCSSs.setStatus('mandatory')
teradsx1IntervalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalPCVs.setStatus('mandatory')
teradsx1IntervalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalLESs.setStatus('mandatory')
teradsx1IntervalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalBESs.setStatus('mandatory')
teradsx1IntervalDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalDMs.setStatus('mandatory')
teradsx1IntervalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalLCVs.setStatus('mandatory')
teradsx1IntervalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalLOF.setStatus('mandatory')
teradsx1IntervalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalYELLOW.setStatus('mandatory')
teradsx1IntervalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1IntervalAIS.setStatus('mandatory')
teraStandarddsx1IntervalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1IntervalLOF.setStatus('mandatory')
teraStandarddsx1IntervalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1IntervalYELLOW.setStatus('mandatory')
teraStandarddsx1IntervalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1IntervalAIS.setStatus('mandatory')
teraStandarddsx1IntervalLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1IntervalLOSs.setStatus('mandatory')
teradsx1TotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 11, 3), )
if mibBuilder.loadTexts: teradsx1TotalTable.setStatus('mandatory')
teradsx1TotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1), ).setIndexNames((0, "TERAWAVE-terads1-MIB", "teradsx1TotalIndex"))
if mibBuilder.loadTexts: teradsx1TotalTableEntry.setStatus('mandatory')
teradsx1TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalIndex.setStatus('mandatory')
teradsx1TotalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalESs.setStatus('mandatory')
teradsx1TotalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalSESs.setStatus('mandatory')
teradsx1TotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalSEFSs.setStatus('mandatory')
teradsx1TotalUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalUAS.setStatus('mandatory')
teradsx1TotalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalCSSs.setStatus('mandatory')
teradsx1TotalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalPCVs.setStatus('mandatory')
teradsx1TotalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalLESs.setStatus('mandatory')
teradsx1TotalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalBESs.setStatus('mandatory')
teradsx1TotalDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalDMs.setStatus('mandatory')
teradsx1TotalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalLCVs.setStatus('mandatory')
teradsx1TotalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalLOF.setStatus('mandatory')
teradsx1TotalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalYELLOW.setStatus('mandatory')
teradsx1TotalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TotalAIS.setStatus('mandatory')
teradsx1TotalPerfStat = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teradsx1TotalPerfStat.setStatus('mandatory')
teraStandarddsx1TotalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1TotalLOF.setStatus('mandatory')
teraStandarddsx1TotalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1TotalYELLOW.setStatus('mandatory')
teraStandarddsx1TotalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1TotalAIS.setStatus('mandatory')
teraStandarddsx1TotalLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 3, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1TotalLOSs.setStatus('mandatory')
teradsx1Standard7DayTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 11, 4), )
if mibBuilder.loadTexts: teradsx1Standard7DayTotalTable.setStatus('mandatory')
teradsx1Standard7DayTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1), ).setIndexNames((0, "TERAWAVE-terads1-MIB", "teradsx1Standard7DayTotalIndex"), (0, "TERAWAVE-terads1-MIB", "teradsx1Standard7DayTotalNumber"))
if mibBuilder.loadTexts: teradsx1Standard7DayTotalTableEntry.setStatus('mandatory')
teradsx1Standard7DayTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalIndex.setStatus('mandatory')
teradsx1Standard7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalNumber.setStatus('mandatory')
teradsx1Standard7DayTotalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalESs.setStatus('mandatory')
teradsx1Standard7DayTotalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalSESs.setStatus('mandatory')
teradsx1Standard7DayTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalSEFSs.setStatus('mandatory')
teradsx1Standard7DayTotalUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalUAS.setStatus('mandatory')
teradsx1Standard7DayTotalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalCSSs.setStatus('mandatory')
teradsx1Standard7DayTotalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalPCVs.setStatus('mandatory')
teradsx1Standard7DayTotalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalLESs.setStatus('mandatory')
teradsx1Standard7DayTotalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalBESs.setStatus('mandatory')
teradsx1Standard7DayTotalDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalDMs.setStatus('mandatory')
teradsx1Standard7DayTotalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalLCVs.setStatus('mandatory')
teradsx1Standard7DayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Standard7DayTotalValidData.setStatus('mandatory')
teradsx1Tera7DayTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 11, 5), )
if mibBuilder.loadTexts: teradsx1Tera7DayTotalTable.setStatus('mandatory')
teradsx1Tera7DayTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1), ).setIndexNames((0, "TERAWAVE-terads1-MIB", "teradsx1Tera7DayTotalIndex"), (0, "TERAWAVE-terads1-MIB", "teradsx1Tera7DayTotalNumber"))
if mibBuilder.loadTexts: teradsx1Tera7DayTotalTableEntry.setStatus('mandatory')
teradsx1Tera7DayTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalIndex.setStatus('mandatory')
teradsx1Tera7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalNumber.setStatus('mandatory')
teradsx1Tera7DayTotalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalESs.setStatus('mandatory')
teradsx1Tera7DayTotalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalSESs.setStatus('mandatory')
teradsx1Tera7DayTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalSEFSs.setStatus('mandatory')
teradsx1Tera7DayTotalUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalUAS.setStatus('mandatory')
teradsx1Tera7DayTotalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalCSSs.setStatus('mandatory')
teradsx1Tera7DayTotalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalPCVs.setStatus('mandatory')
teradsx1Tera7DayTotalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalLESs.setStatus('mandatory')
teradsx1Tera7DayTotalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalBESs.setStatus('mandatory')
teradsx1Tera7DayTotalDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalDMs.setStatus('mandatory')
teradsx1Tera7DayTotalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalLCVs.setStatus('mandatory')
teradsx1Tera7DayTotalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalLOF.setStatus('mandatory')
teradsx1Tera7DayTotalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalYELLOW.setStatus('mandatory')
teradsx1Tera7DayTotalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalAIS.setStatus('mandatory')
teradsx1TeraStandard7DayTotalLOF = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TeraStandard7DayTotalLOF.setStatus('mandatory')
teradsx1TeraStandard7DayTotalYELLOW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TeraStandard7DayTotalYELLOW.setStatus('mandatory')
teradsx1TeraStandard7DayTotalAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1TeraStandard7DayTotalAIS.setStatus('mandatory')
teradsx1Tera7DayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx1Tera7DayTotalValidData.setStatus('mandatory')
teraStandarddsx1Tera7DayTotalLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 11, 5, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStandarddsx1Tera7DayTotalLOSs.setStatus('mandatory')
mibBuilder.exportSymbols("TERAWAVE-terads1-MIB", teradsx1TotalSESs=teradsx1TotalSESs, teradsx1IntervalYELLOW=teradsx1IntervalYELLOW, teraStandarddsx1TotalLOF=teraStandarddsx1TotalLOF, teradsx1CurrentCSSs=teradsx1CurrentCSSs, teradsx1Standard7DayTotalCSSs=teradsx1Standard7DayTotalCSSs, teradsx1TotalTableEntry=teradsx1TotalTableEntry, teradsx1Tera7DayTotalLESs=teradsx1Tera7DayTotalLESs, teradsx1Tera7DayTotalDMs=teradsx1Tera7DayTotalDMs, teradsx1Tera7DayTotalSEFSs=teradsx1Tera7DayTotalSEFSs, teradsx1TotalDMs=teradsx1TotalDMs, teradsx1CurrentLCVs=teradsx1CurrentLCVs, teradsx1CurrentYELLOW=teradsx1CurrentYELLOW, teradsx1IntervalTable=teradsx1IntervalTable, teraStandarddsx1IntervalAIS=teraStandarddsx1IntervalAIS, teradsx1Standard7DayTotalNumber=teradsx1Standard7DayTotalNumber, teradsx1Standard7DayTotalLCVs=teradsx1Standard7DayTotalLCVs, teradsx1Tera7DayTotalYELLOW=teradsx1Tera7DayTotalYELLOW, teradsx1Tera7DayTotalSESs=teradsx1Tera7DayTotalSESs, teradsx1Standard7DayTotalESs=teradsx1Standard7DayTotalESs, teradsx1TotalIndex=teradsx1TotalIndex, teradsx1CurrentDMs=teradsx1CurrentDMs, teraStandarddsx1CurrentLOSs=teraStandarddsx1CurrentLOSs, teradsx1CurrentIndex=teradsx1CurrentIndex, teradsx1TotalCSSs=teradsx1TotalCSSs, teradsx1TotalPCVs=teradsx1TotalPCVs, teradsx1Tera7DayTotalBESs=teradsx1Tera7DayTotalBESs, teradsx1Standard7DayTotalSESs=teradsx1Standard7DayTotalSESs, teraStandarddsx1TotalYELLOW=teraStandarddsx1TotalYELLOW, teradsx1CurrentBESs=teradsx1CurrentBESs, teradsx1IntervalIndex=teradsx1IntervalIndex, teradsx1Tera7DayTotalNumber=teradsx1Tera7DayTotalNumber, teraStandarddsx1IntervalLOF=teraStandarddsx1IntervalLOF, teradsx1IntervalPCVs=teradsx1IntervalPCVs, teradsx1TotalPerfStat=teradsx1TotalPerfStat, teradsx1TeraStandard7DayTotalYELLOW=teradsx1TeraStandard7DayTotalYELLOW, teraStandarddsx1IntervalLOSs=teraStandarddsx1IntervalLOSs, teradsx1Standard7DayTotalPCVs=teradsx1Standard7DayTotalPCVs, teradsx1IntervalLESs=teradsx1IntervalLESs, teradsx1Standard7DayTotalDMs=teradsx1Standard7DayTotalDMs, teradsx1Standard7DayTotalUAS=teradsx1Standard7DayTotalUAS, teradsx1CurrentESs=teradsx1CurrentESs, teradsx1IntervalESs=teradsx1IntervalESs, teradsx1IntervalCSSs=teradsx1IntervalCSSs, teraStandarddsx1CurrentLOF=teraStandarddsx1CurrentLOF, teradsx1IntervalUASs=teradsx1IntervalUASs, teradsx1TotalLOF=teradsx1TotalLOF, teradsx1Standard7DayTotalLESs=teradsx1Standard7DayTotalLESs, teradsx1CurrentTable=teradsx1CurrentTable, teraStandarddsx1CurrentYELLOW=teraStandarddsx1CurrentYELLOW, teraStandarddsx1IntervalYELLOW=teraStandarddsx1IntervalYELLOW, teradsx1Tera7DayTotalValidData=teradsx1Tera7DayTotalValidData, teraStandarddsx1Tera7DayTotalLOSs=teraStandarddsx1Tera7DayTotalLOSs, teradsx1Standard7DayTotalSEFSs=teradsx1Standard7DayTotalSEFSs, teradsx1TotalLESs=teradsx1TotalLESs, teradsx1IntervalDMs=teradsx1IntervalDMs, teradsx1CurrentSEFSs=teradsx1CurrentSEFSs, teradsx1Standard7DayTotalIndex=teradsx1Standard7DayTotalIndex, teradsx1IntervalBESs=teradsx1IntervalBESs, teradsx1CurrentSESs=teradsx1CurrentSESs, teradsx1TotalLCVs=teradsx1TotalLCVs, teraStandarddsx1TotalLOSs=teraStandarddsx1TotalLOSs, teradsx1TeraStandard7DayTotalLOF=teradsx1TeraStandard7DayTotalLOF, teradsx1Tera7DayTotalPCVs=teradsx1Tera7DayTotalPCVs, teradsx1CurrentTableEntry=teradsx1CurrentTableEntry, teradsx1CurrentLOF=teradsx1CurrentLOF, teradsx1Tera7DayTotalTable=teradsx1Tera7DayTotalTable, teradsx1IntervalAIS=teradsx1IntervalAIS, teradsx1CurrentUASs=teradsx1CurrentUASs, teradsx1Standard7DayTotalValidData=teradsx1Standard7DayTotalValidData, teradsx1Tera7DayTotalCSSs=teradsx1Tera7DayTotalCSSs, teradsx1TotalSEFSs=teradsx1TotalSEFSs, terawave=terawave, teradsx1IntervalLCVs=teradsx1IntervalLCVs, teradsx1Tera7DayTotalESs=teradsx1Tera7DayTotalESs, teradsx1TotalESs=teradsx1TotalESs, teradsx1Standard7DayTotalTableEntry=teradsx1Standard7DayTotalTableEntry, teradsx1TotalTable=teradsx1TotalTable, teradsx1IntervalNumber=teradsx1IntervalNumber, teradsx1Tera7DayTotalLCVs=teradsx1Tera7DayTotalLCVs, teradsx1Tera7DayTotalLOF=teradsx1Tera7DayTotalLOF, teradsx1TotalAIS=teradsx1TotalAIS, teradsx1IntervalTableEntry=teradsx1IntervalTableEntry, teradsx1TotalYELLOW=teradsx1TotalYELLOW, teradsx1TeraStandard7DayTotalAIS=teradsx1TeraStandard7DayTotalAIS, teraDs1Group=teraDs1Group, teradsx1CurrentAIS=teradsx1CurrentAIS, teradsx1TotalBESs=teradsx1TotalBESs, teradsx1Tera7DayTotalUAS=teradsx1Tera7DayTotalUAS, teraStandarddsx1TotalAIS=teraStandarddsx1TotalAIS, teradsx1TotalUAS=teradsx1TotalUAS, teradsx1IntervalLOF=teradsx1IntervalLOF, teradsx1Tera7DayTotalTableEntry=teradsx1Tera7DayTotalTableEntry, teradsx1IntervalSESs=teradsx1IntervalSESs, teradsx1Tera7DayTotalIndex=teradsx1Tera7DayTotalIndex, teradsx1CurrentPCVs=teradsx1CurrentPCVs, teradsx1Standard7DayTotalBESs=teradsx1Standard7DayTotalBESs, teradsx1CurrentLESs=teradsx1CurrentLESs, teradsx1IntervalSEFSs=teradsx1IntervalSEFSs, teradsx1Standard7DayTotalTable=teradsx1Standard7DayTotalTable, teradsx1Tera7DayTotalAIS=teradsx1Tera7DayTotalAIS, teraStandarddsx1CurrentAIS=teraStandarddsx1CurrentAIS)
