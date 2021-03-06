#
# PySNMP MIB module ChrComPmOpticsOMS-SRC-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOMS-SRC-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Bits, Counter32, iso, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Bits", "Counter32", "iso", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmOpticsOMS_SRC_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11), ).setLabel("chrComPmOpticsOMS-SRC-IntervalTable")
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalTable.setStatus('current')
chrComPmOpticsOMS_SRC_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1), ).setLabel("chrComPmOpticsOMS-SRC-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmOpticsOMS-SRC-Interval-MIB", "chrComPmOpticsIntervalNumber"))
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalEntry.setStatus('current')
chrComPmOpticsIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsIntervalNumber.setStatus('current')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
chrComPmOpticsORS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS.setStatus('current')
chrComPmOpticsSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES.setStatus('current')
chrComPmOpticsUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS.setStatus('current')
chrComPmOpticsMean = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean.setStatus('current')
chrComPmOpticsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax.setStatus('current')
chrComPmOpticsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin.setStatus('current')
chrComPmOpticsSD = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD.setStatus('current')
mibBuilder.exportSymbols("ChrComPmOpticsOMS-SRC-Interval-MIB", chrComPmOpticsSES=chrComPmOpticsSES, chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl, chrComPmOpticsMean=chrComPmOpticsMean, chrComPmOpticsMin=chrComPmOpticsMin, chrComPmOpticsORS=chrComPmOpticsORS, chrComPmOpticsOMS_SRC_IntervalEntry=chrComPmOpticsOMS_SRC_IntervalEntry, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsUAS=chrComPmOpticsUAS, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsMax=chrComPmOpticsMax, chrComPmOpticsOMS_SRC_IntervalTable=chrComPmOpticsOMS_SRC_IntervalTable, chrComPmOpticsIntervalNumber=chrComPmOpticsIntervalNumber, chrComPmOpticsSD=chrComPmOpticsSD)
