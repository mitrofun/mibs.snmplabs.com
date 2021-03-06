#
# PySNMP MIB module HH3C-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-SESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, MibIdentifier, Integer32, ObjectIdentity, Bits, ModuleIdentity, Counter32, IpAddress, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter32", "IpAddress", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cSession = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 149))
hh3cSession.setRevisions(('2013-12-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cSession.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hh3cSession.setLastUpdated('201312200000Z')
if mibBuilder.loadTexts: hh3cSession.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cSession.setContactInfo('Platform Team Hangzhou H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cSession.setDescription('The MIB is designed to manage sessions.')
hh3cSessionTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1))
hh3cSessionStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1), )
if mibBuilder.loadTexts: hh3cSessionStatTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatTable.setDescription('The statistics of sessions.')
hh3cSessionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1), ).setIndexNames((0, "HH3C-SESSION-MIB", "hh3cSessionStatChassis"), (0, "HH3C-SESSION-MIB", "hh3cSessionStatSlot"), (0, "HH3C-SESSION-MIB", "hh3cSessionStatCPUID"))
if mibBuilder.loadTexts: hh3cSessionStatEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatEntry.setDescription('An entry (conceptual row) representing session statistics information.')
hh3cSessionStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hh3cSessionStatChassis.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatChassis.setDescription('An IRF member device ID.')
hh3cSessionStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hh3cSessionStatSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatSlot.setDescription('The slot where the card resides.')
hh3cSessionStatCPUID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: hh3cSessionStatCPUID.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatCPUID.setDescription('CPU ID.')
hh3cSessionStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSessionStatCount.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatCount.setDescription('The number of current sessions.')
hh3cSessionStatCreateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSessionStatCreateRate.setStatus('current')
if mibBuilder.loadTexts: hh3cSessionStatCreateRate.setDescription('The number of sessions per second.')
mibBuilder.exportSymbols("HH3C-SESSION-MIB", hh3cSessionStatCPUID=hh3cSessionStatCPUID, hh3cSessionStatTable=hh3cSessionStatTable, hh3cSessionStatSlot=hh3cSessionStatSlot, hh3cSessionStatCreateRate=hh3cSessionStatCreateRate, hh3cSessionTables=hh3cSessionTables, hh3cSessionStatEntry=hh3cSessionStatEntry, PYSNMP_MODULE_ID=hh3cSession, hh3cSession=hh3cSession, hh3cSessionStatChassis=hh3cSessionStatChassis, hh3cSessionStatCount=hh3cSessionStatCount)
