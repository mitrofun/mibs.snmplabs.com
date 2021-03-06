#
# PySNMP MIB module HUAWEI-SZONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SZONE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
mplsVpnVrfName, = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfName")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, ObjectIdentity, Unsigned32, ModuleIdentity, Counter64, Bits, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Integer32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Integer32", "MibIdentifier", "IpAddress")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
hwSZONE = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15))
if mibBuilder.loadTexts: hwSZONE.setLastUpdated('200304080900Z')
if mibBuilder.loadTexts: hwSZONE.setOrganization('Huawei Technologies co.,Ltd.')
hwSZoneZoneCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1))
hwSZoneZoneTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1), )
if mibBuilder.loadTexts: hwSZoneZoneTable.setStatus('current')
hwSZoneZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "HUAWEI-SZONE-MIB", "hwSZoneZoneID"))
if mibBuilder.loadTexts: hwSZoneZoneEntry.setStatus('current')
hwSZoneZoneID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSZoneZoneID.setStatus('current')
hwSZoneZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneZoneName.setStatus('current')
hwSZoneSecPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneSecPriority.setStatus('current')
hwSZoneZoneStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneZoneStatus.setStatus('current')
hwSZoneZoneIFTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2), )
if mibBuilder.loadTexts: hwSZoneZoneIFTable.setStatus('current')
hwSZoneZoneIFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1), ).setIndexNames((0, "HUAWEI-SZONE-MIB", "hwSZoneIFZoneID"), (0, "HUAWEI-SZONE-MIB", "hwSZoneZoneIFIndex"))
if mibBuilder.loadTexts: hwSZoneZoneIFEntry.setStatus('current')
hwSZoneIFZoneID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSZoneIFZoneID.setStatus('current')
hwSZoneZoneIFIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSZoneZoneIFIndex.setStatus('current')
hwSZoneZoneIFStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneZoneIFStatus.setStatus('current')
hwSZoneInterZoneCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2))
hwSZoneInterZoneTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1), )
if mibBuilder.loadTexts: hwSZoneInterZoneTable.setStatus('current')
hwSZoneInterZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID1"), (0, "HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID2"))
if mibBuilder.loadTexts: hwSZoneInterZoneEntry.setStatus('current')
hwSZoneInterZoneZoneID1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSZoneInterZoneZoneID1.setStatus('current')
hwSZoneInterZoneZoneID2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSZoneInterZoneZoneID2.setStatus('current')
hwSZoneInterZoneEnableFW = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneInterZoneEnableFW.setStatus('current')
hwSZoneInterZoneStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSZoneInterZoneStatus.setStatus('current')
hwSZoneConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3))
hwSZoneCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 1))
hwSZoneMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2))
hwSZoneZoneCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2, 1)).setObjects(("HUAWEI-SZONE-MIB", "hwSZoneZoneName"), ("HUAWEI-SZONE-MIB", "hwSZoneSecPriority"), ("HUAWEI-SZONE-MIB", "hwSZoneZoneStatus"), ("HUAWEI-SZONE-MIB", "hwSZoneZoneIFIndex"), ("HUAWEI-SZONE-MIB", "hwSZoneZoneIFStatus"), ("HUAWEI-SZONE-MIB", "hwSZoneZoneID"), ("HUAWEI-SZONE-MIB", "hwSZoneIFZoneID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSZoneZoneCfgGroup = hwSZoneZoneCfgGroup.setStatus('current')
hwSZoneInterZoneCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2, 2)).setObjects(("HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID1"), ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID2"), ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneEnableFW"), ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSZoneInterZoneCfgGroup = hwSZoneInterZoneCfgGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SZONE-MIB", hwSZoneZoneCfg=hwSZoneZoneCfg, hwSZoneInterZoneZoneID1=hwSZoneInterZoneZoneID1, hwSZoneCompliance=hwSZoneCompliance, hwSZoneZoneIFStatus=hwSZoneZoneIFStatus, hwSZoneZoneCfgGroup=hwSZoneZoneCfgGroup, hwSZoneIFZoneID=hwSZoneIFZoneID, hwSZoneZoneTable=hwSZoneZoneTable, hwSZoneInterZoneCfgGroup=hwSZoneInterZoneCfgGroup, hwSZoneInterZoneEntry=hwSZoneInterZoneEntry, hwSZoneMibGroups=hwSZoneMibGroups, hwSZoneZoneEntry=hwSZoneZoneEntry, hwSZoneZoneName=hwSZoneZoneName, hwSZoneZoneIFTable=hwSZoneZoneIFTable, hwSZoneInterZoneEnableFW=hwSZoneInterZoneEnableFW, hwSZoneZoneID=hwSZoneZoneID, hwSZoneConformance=hwSZoneConformance, hwSZoneZoneIFIndex=hwSZoneZoneIFIndex, hwSZoneInterZoneTable=hwSZoneInterZoneTable, hwSZoneZoneIFEntry=hwSZoneZoneIFEntry, PYSNMP_MODULE_ID=hwSZONE, hwSZoneInterZoneZoneID2=hwSZoneInterZoneZoneID2, hwSZONE=hwSZONE, hwSZoneInterZoneCfg=hwSZoneInterZoneCfg, hwSZoneSecPriority=hwSZoneSecPriority, hwSZoneZoneStatus=hwSZoneZoneStatus, hwSZoneInterZoneStatus=hwSZoneInterZoneStatus)
