#
# PySNMP MIB module Juniper-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, IpAddress, Counter32, MibIdentifier, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "iso", "Bits")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
juniEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34))
juniEthernetMIB.setRevisions(('2006-01-11 21:16', '2005-09-14 20:08', '2004-12-14 15:14', '2004-05-26 19:40', '2003-07-28 21:33', '2003-02-20 21:51', '2002-10-02 15:34', '2002-10-01 17:44', '2002-04-05 19:47', '2001-01-02 16:55', '2000-04-18 00:00', '2000-02-03 00:00',))
if mibBuilder.loadTexts: juniEthernetMIB.setLastUpdated('200601112116Z')
if mibBuilder.loadTexts: juniEthernetMIB.setOrganization('Juniper Networks, Inc.')
class JuniEthernetIfMauType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("mauNotPresent", 0), ("mauNotSupported", 1), ("mau10BaseT", 2), ("mau100BaseTx", 3), ("mau1000BaseT", 4), ("mau1000BaseCx", 5), ("mau1000BaseSx", 6), ("mau1000BaseLx", 7), ("mau1000BaseZx", 8), ("mauSfpUnknown", 9), ("mauSfpNotPresent", 10), ("mau100BaseFxSm", 11), ("mau100BaseFxMm", 12), ("mauSfpNotJnprCompliant", 13), ("mau10000BaseSr", 14), ("mau10000BaseLr", 15), ("mau10000BaseEr", 16), ("mauXfpUnknown", 17), ("mauXfpNotPresent", 18), ("mauXfpNotJnprCompliant", 19))

juniEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1))
juniEthernetIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1))
juniEthernetSubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2))
juniVlanMajorIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3))
juniVlanSubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4))
juniEthernetIfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5))
juniLagIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 6))
juniEthernetIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: juniEthernetIfTable.setStatus('current')
juniEthernetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-ETHERNET-MIB", "juniEthernetIfIndex"))
if mibBuilder.loadTexts: juniEthernetIfEntry.setStatus('current')
juniEthernetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniEthernetIfIndex.setStatus('current')
juniEthernetIfDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoDuplex", 1), ("halfDuplex", 2), ("fullDuplex", 3))).clone('autoDuplex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniEthernetIfDuplexMode.setStatus('current')
juniEthernetIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("autoNegotiate", 1), ("speed10Mbps", 2), ("speed100Mbps", 3), ("speed1000Mbps", 4), ("speed10000Mbps", 5))).clone('autoNegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniEthernetIfSpeed.setStatus('current')
juniEthernetIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9188)).clone(1518)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniEthernetIfMtu.setStatus('current')
juniEthernetIfOperDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoDuplex", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfOperDuplexMode.setStatus('current')
juniEthernetIfPrimaryMauType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 6), JuniEthernetIfMauType().clone('mauNotPresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfPrimaryMauType.setStatus('current')
juniEthernetIfSecondaryMauType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 7), JuniEthernetIfMauType().clone('mauNotSupported')).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfSecondaryMauType.setStatus('current')
juniEthernetIfPrimaryLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfPrimaryLength.setStatus('current')
juniEthernetIfSecondaryLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfSecondaryLength.setStatus('current')
juniEthernetSubIfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetSubIfNextIfIndex.setStatus('current')
juniEthernetSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2), )
if mibBuilder.loadTexts: juniEthernetSubIfTable.setStatus('current')
juniEthernetSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-ETHERNET-MIB", "juniEthernetSubIfIndex"))
if mibBuilder.loadTexts: juniEthernetSubIfEntry.setStatus('current')
juniEthernetSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniEthernetSubIfIndex.setStatus('current')
juniEthernetSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniEthernetSubIfRowStatus.setStatus('current')
juniEthernetSubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniEthernetSubIfLowerIfIndex.setStatus('current')
juniEthernetSubIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniEthernetSubIfId.setStatus('current')
juniVlanMajorNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniVlanMajorNextIfIndex.setStatus('current')
juniVlanMajorIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2), )
if mibBuilder.loadTexts: juniVlanMajorIfTable.setStatus('current')
juniVlanMajorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-ETHERNET-MIB", "juniVlanMajorIfIndex"))
if mibBuilder.loadTexts: juniVlanMajorIfEntry.setStatus('current')
juniVlanMajorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniVlanMajorIfIndex.setStatus('current')
juniVlanMajorIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanMajorIfLowerIfIndex.setStatus('current')
juniVlanMajorIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanMajorIfRowStatus.setStatus('current')
juniVlanSubNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniVlanSubNextIfIndex.setStatus('current')
juniVlanSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2), )
if mibBuilder.loadTexts: juniVlanSubIfTable.setStatus('current')
juniVlanSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1), ).setIndexNames((0, "Juniper-ETHERNET-MIB", "juniVlanSubIfIndex"))
if mibBuilder.loadTexts: juniVlanSubIfEntry.setStatus('current')
juniVlanSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniVlanSubIfIndex.setStatus('current')
juniVlanSubIfVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 4095), ValueRangeConstraint(5000, 5000), ValueRangeConstraint(5001, 5001), )).clone(5000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanId.setStatus('current')
juniVlanSubIfVlanUntagged = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanUntagged.setStatus('current')
juniVlanSubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfLowerIfIndex.setStatus('current')
juniVlanSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfRowStatus.setStatus('current')
juniVlanSubIfVlanStackId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 4095), ValueRangeConstraint(5000, 5000), )).clone(5000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanStackId.setStatus('current')
juniVlanSubIfVlanStackEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(33024, 34984, 37120))).clone(namedValues=NamedValues(("etherType8100h", 33024), ("etherType88a8h", 34984), ("etherType9100h", 37120))).clone('etherType9100h')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanStackEthertype.setStatus('current')
juniVlanSubIfVlanAdvisoryRxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanAdvisoryRxSpeed.setStatus('current')
juniVlanSubIfVlanAdvisoryTxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniVlanSubIfVlanAdvisoryTxSpeed.setStatus('current')
juniEthernetIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1), )
if mibBuilder.loadTexts: juniEthernetIfStatsTable.setStatus('current')
juniEthernetIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1), ).setIndexNames((0, "Juniper-ETHERNET-MIB", "juniEthernetIfStatsIndex"))
if mibBuilder.loadTexts: juniEthernetIfStatsEntry.setStatus('current')
juniEthernetIfStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniEthernetIfStatsIndex.setStatus('current')
juniEthernetIfIngressLineUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfIngressLineUtilization.setStatus('current')
juniEthernetIfEgressLineUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 5, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: juniEthernetIfEgressLineUtilization.setStatus('current')
juniLagNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 6, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLagNextIfIndex.setStatus('current')
juniEthernetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4))
juniEthernetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1))
juniEthernetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2))
juniEthernetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 1)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance = juniEthernetCompliance.setStatus('obsolete')
juniEthernetCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 2)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"), ("Juniper-ETHERNET-MIB", "juniVlanGroup"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance2 = juniEthernetCompliance2.setStatus('obsolete')
juniEthernetCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 3)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"), ("Juniper-ETHERNET-MIB", "juniVlanGroup"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance3 = juniEthernetCompliance3.setStatus('obsolete')
juniEthernetCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 4)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup2"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"), ("Juniper-ETHERNET-MIB", "juniVlanGroup"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance4 = juniEthernetCompliance4.setStatus('obsolete')
juniEthernetCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 5)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup2"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"), ("Juniper-ETHERNET-MIB", "juniEthernetIfStatsGroup"), ("Juniper-ETHERNET-MIB", "juniVlanGroup"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance5 = juniEthernetCompliance5.setStatus('obsolete')
juniEthernetCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 6)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetGroup2"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfGroup"), ("Juniper-ETHERNET-MIB", "juniEthernetIfStatsGroup"), ("Juniper-ETHERNET-MIB", "juniVlanGroup"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfGroup2"), ("Juniper-ETHERNET-MIB", "juniLagIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetCompliance6 = juniEthernetCompliance6.setStatus('current')
juniEthernetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 1)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetIfDuplexMode"), ("Juniper-ETHERNET-MIB", "juniEthernetIfSpeed"), ("Juniper-ETHERNET-MIB", "juniEthernetIfMtu"), ("Juniper-ETHERNET-MIB", "juniEthernetIfOperDuplexMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetGroup = juniEthernetGroup.setStatus('obsolete')
juniEthernetSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 2)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetSubIfNextIfIndex"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfRowStatus"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfLowerIfIndex"), ("Juniper-ETHERNET-MIB", "juniEthernetSubIfId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetSubIfGroup = juniEthernetSubIfGroup.setStatus('current')
juniVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 3)).setObjects(("Juniper-ETHERNET-MIB", "juniVlanMajorNextIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanMajorIfLowerIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanMajorIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVlanGroup = juniVlanGroup.setStatus('current')
juniVlanSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 4)).setObjects(("Juniper-ETHERNET-MIB", "juniVlanSubNextIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanId"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanUntagged"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfLowerIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVlanSubIfGroup = juniVlanSubIfGroup.setStatus('obsolete')
juniVlanSubIfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 5)).setObjects(("Juniper-ETHERNET-MIB", "juniVlanSubNextIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanId"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanUntagged"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanStackId"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfLowerIfIndex"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfRowStatus"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanStackEthertype"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanAdvisoryRxSpeed"), ("Juniper-ETHERNET-MIB", "juniVlanSubIfVlanAdvisoryTxSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniVlanSubIfGroup2 = juniVlanSubIfGroup2.setStatus('current')
juniEthernetGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 6)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetIfDuplexMode"), ("Juniper-ETHERNET-MIB", "juniEthernetIfSpeed"), ("Juniper-ETHERNET-MIB", "juniEthernetIfMtu"), ("Juniper-ETHERNET-MIB", "juniEthernetIfOperDuplexMode"), ("Juniper-ETHERNET-MIB", "juniEthernetIfPrimaryMauType"), ("Juniper-ETHERNET-MIB", "juniEthernetIfSecondaryMauType"), ("Juniper-ETHERNET-MIB", "juniEthernetIfPrimaryLength"), ("Juniper-ETHERNET-MIB", "juniEthernetIfSecondaryLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetGroup2 = juniEthernetGroup2.setStatus('current')
juniEthernetIfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 7)).setObjects(("Juniper-ETHERNET-MIB", "juniEthernetIfIngressLineUtilization"), ("Juniper-ETHERNET-MIB", "juniEthernetIfEgressLineUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEthernetIfStatsGroup = juniEthernetIfStatsGroup.setStatus('current')
juniLagIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 8)).setObjects(("Juniper-ETHERNET-MIB", "juniLagNextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLagIfGroup = juniLagIfGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-ETHERNET-MIB", juniEthernetIfDuplexMode=juniEthernetIfDuplexMode, juniVlanSubNextIfIndex=juniVlanSubNextIfIndex, juniEthernetConformance=juniEthernetConformance, JuniEthernetIfMauType=JuniEthernetIfMauType, juniEthernetCompliances=juniEthernetCompliances, juniEthernetSubIfTable=juniEthernetSubIfTable, PYSNMP_MODULE_ID=juniEthernetMIB, juniVlanSubIfLowerIfIndex=juniVlanSubIfLowerIfIndex, juniEthernetSubIfEntry=juniEthernetSubIfEntry, juniVlanSubIfVlanId=juniVlanSubIfVlanId, juniEthernetSubIfId=juniEthernetSubIfId, juniVlanSubIfLayer=juniVlanSubIfLayer, juniEthernetIfEntry=juniEthernetIfEntry, juniEthernetIfSecondaryLength=juniEthernetIfSecondaryLength, juniLagNextIfIndex=juniLagNextIfIndex, juniEthernetCompliance6=juniEthernetCompliance6, juniEthernetIfStatsIndex=juniEthernetIfStatsIndex, juniEthernetIfIngressLineUtilization=juniEthernetIfIngressLineUtilization, juniEthernetObjects=juniEthernetObjects, juniEthernetGroup2=juniEthernetGroup2, juniEthernetIfStats=juniEthernetIfStats, juniVlanSubIfIndex=juniVlanSubIfIndex, juniEthernetIfSecondaryMauType=juniEthernetIfSecondaryMauType, juniEthernetCompliance2=juniEthernetCompliance2, juniEthernetIfLayer=juniEthernetIfLayer, juniVlanSubIfTable=juniVlanSubIfTable, juniVlanMajorIfLayer=juniVlanMajorIfLayer, juniVlanSubIfVlanStackId=juniVlanSubIfVlanStackId, juniEthernetIfStatsEntry=juniEthernetIfStatsEntry, juniVlanSubIfGroup2=juniVlanSubIfGroup2, juniEthernetIfStatsGroup=juniEthernetIfStatsGroup, juniVlanSubIfGroup=juniVlanSubIfGroup, juniEthernetSubIfLowerIfIndex=juniEthernetSubIfLowerIfIndex, juniEthernetIfIndex=juniEthernetIfIndex, juniVlanMajorIfRowStatus=juniVlanMajorIfRowStatus, juniEthernetIfSpeed=juniEthernetIfSpeed, juniVlanMajorNextIfIndex=juniVlanMajorNextIfIndex, juniLagIfLayer=juniLagIfLayer, juniVlanSubIfEntry=juniVlanSubIfEntry, juniVlanSubIfVlanUntagged=juniVlanSubIfVlanUntagged, juniEthernetIfStatsTable=juniEthernetIfStatsTable, juniVlanGroup=juniVlanGroup, juniVlanSubIfVlanStackEthertype=juniVlanSubIfVlanStackEthertype, juniEthernetGroup=juniEthernetGroup, juniLagIfGroup=juniLagIfGroup, juniEthernetGroups=juniEthernetGroups, juniEthernetCompliance3=juniEthernetCompliance3, juniEthernetIfMtu=juniEthernetIfMtu, juniVlanSubIfVlanAdvisoryRxSpeed=juniVlanSubIfVlanAdvisoryRxSpeed, juniEthernetIfOperDuplexMode=juniEthernetIfOperDuplexMode, juniEthernetSubIfNextIfIndex=juniEthernetSubIfNextIfIndex, juniEthernetIfPrimaryLength=juniEthernetIfPrimaryLength, juniVlanMajorIfIndex=juniVlanMajorIfIndex, juniVlanMajorIfEntry=juniVlanMajorIfEntry, juniEthernetIfTable=juniEthernetIfTable, juniEthernetSubIfGroup=juniEthernetSubIfGroup, juniEthernetMIB=juniEthernetMIB, juniVlanSubIfVlanAdvisoryTxSpeed=juniVlanSubIfVlanAdvisoryTxSpeed, juniEthernetSubIfRowStatus=juniEthernetSubIfRowStatus, juniEthernetCompliance4=juniEthernetCompliance4, juniVlanSubIfRowStatus=juniVlanSubIfRowStatus, juniEthernetSubIfIndex=juniEthernetSubIfIndex, juniEthernetIfPrimaryMauType=juniEthernetIfPrimaryMauType, juniEthernetCompliance=juniEthernetCompliance, juniEthernetCompliance5=juniEthernetCompliance5, juniEthernetSubIfLayer=juniEthernetSubIfLayer, juniEthernetIfEgressLineUtilization=juniEthernetIfEgressLineUtilization, juniVlanMajorIfTable=juniVlanMajorIfTable, juniVlanMajorIfLowerIfIndex=juniVlanMajorIfLowerIfIndex)
