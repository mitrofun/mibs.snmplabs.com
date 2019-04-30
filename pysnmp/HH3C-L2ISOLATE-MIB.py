#
# PySNMP MIB module HH3C-L2ISOLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-L2ISOLATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso, Counter32, ObjectIdentity, Unsigned32, Integer32, MibIdentifier, Bits, Counter64, ModuleIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "Integer32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "IpAddress", "Gauge32")
MacAddress, TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
hh3cL2Isolate = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 103))
hh3cL2Isolate.setRevisions(('2009-05-06 00:00',))
if mibBuilder.loadTexts: hh3cL2Isolate.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hh3cL2Isolate.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cL2IsolateObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1))
hh3cL2IsolateEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 1), )
if mibBuilder.loadTexts: hh3cL2IsolateEnableTable.setStatus('current')
hh3cL2IsolateEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 1, 1), ).setIndexNames((0, "HH3C-L2ISOLATE-MIB", "hh3cL2IsolateVLANIndex"))
if mibBuilder.loadTexts: hh3cL2IsolateEnableEntry.setStatus('current')
hh3cL2IsolateVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cL2IsolateVLANIndex.setStatus('current')
hh3cL2IsolateEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cL2IsolateEnable.setStatus('current')
hh3cL2IsolatePermitMACTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 2), )
if mibBuilder.loadTexts: hh3cL2IsolatePermitMACTable.setStatus('current')
hh3cL2IsolatePermitMACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 2, 1), ).setIndexNames((0, "HH3C-L2ISOLATE-MIB", "hh3cL2IsolateVLANIndex"), (0, "HH3C-L2ISOLATE-MIB", "hh3cL2IsoLatePermitMAC"))
if mibBuilder.loadTexts: hh3cL2IsolatePermitMACEntry.setStatus('current')
hh3cL2IsoLatePermitMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cL2IsoLatePermitMAC.setStatus('current')
hh3cL2IsoLatePermitMACRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 103, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cL2IsoLatePermitMACRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-L2ISOLATE-MIB", hh3cL2IsolateEnableEntry=hh3cL2IsolateEnableEntry, PYSNMP_MODULE_ID=hh3cL2Isolate, hh3cL2IsolateObject=hh3cL2IsolateObject, hh3cL2IsoLatePermitMACRowStatus=hh3cL2IsoLatePermitMACRowStatus, hh3cL2IsolatePermitMACTable=hh3cL2IsolatePermitMACTable, hh3cL2IsolatePermitMACEntry=hh3cL2IsolatePermitMACEntry, hh3cL2IsoLatePermitMAC=hh3cL2IsoLatePermitMAC, hh3cL2IsolateVLANIndex=hh3cL2IsolateVLANIndex, hh3cL2Isolate=hh3cL2Isolate, hh3cL2IsolateEnable=hh3cL2IsolateEnable, hh3cL2IsolateEnableTable=hh3cL2IsolateEnableTable)