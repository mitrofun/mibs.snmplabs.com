#
# PySNMP MIB module ChrComPmSonetSNT-P-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-P-Current-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Unsigned32, ModuleIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, MibIdentifier, NotificationType, IpAddress, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmSonetSNT_P_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10), ).setLabel("chrComPmSonetSNT-P-CurrentTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_P_CurrentTable.setStatus('current')
chrComPmSonetSNT_P_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1), ).setLabel("chrComPmSonetSNT-P-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmSonetSNT_P_CurrentEntry.setStatus('current')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
chrComPmSonetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetStatus.setStatus('current')
chrComPmSonetWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetWidth.setStatus('current')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
chrComPmSonetUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetUAS.setStatus('current')
chrComPmSonetPS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetPS.setStatus('current')
chrComPmSonetThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetThresholdProfIndex.setStatus('current')
chrComPmSonetResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 10, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmSonetResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmSonetSNT-P-Current-MIB", chrComPmSonetElapsedTime=chrComPmSonetElapsedTime, chrComPmSonetUAS=chrComPmSonetUAS, chrComPmSonetES=chrComPmSonetES, chrComPmSonetThresholdProfIndex=chrComPmSonetThresholdProfIndex, chrComPmSonetResetPmCountersAction=chrComPmSonetResetPmCountersAction, chrComPmSonetWidth=chrComPmSonetWidth, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetStatus=chrComPmSonetStatus, chrComPmSonetCV=chrComPmSonetCV, chrComPmSonetPS=chrComPmSonetPS, chrComPmSonetSNT_P_CurrentEntry=chrComPmSonetSNT_P_CurrentEntry, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetSNT_P_CurrentTable=chrComPmSonetSNT_P_CurrentTable, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls)