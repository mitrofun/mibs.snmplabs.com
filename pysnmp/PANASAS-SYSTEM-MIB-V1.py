#
# PySNMP MIB module PANASAS-SYSTEM-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-SYSTEM-MIB-V1
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
panFs, = mibBuilder.importSymbols("PANASAS-PANFS-MIB-V1", "panFs")
PanSerialNumber, = mibBuilder.importSymbols("PANASAS-TC-MIB", "PanSerialNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, NotificationType, ModuleIdentity, IpAddress, Integer32, Counter64, MibIdentifier, ObjectIdentity, TimeTicks, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter32", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2))
panSystem.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panSystem.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panSystem.setOrganization('Panasas, Inc')
panSystemCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1))
panSystemClusterName = MibScalar((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemClusterName.setStatus('current')
panSystemClusterManagementAddress = MibScalar((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemClusterManagementAddress.setStatus('current')
panSystemClusterRepsetTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3), )
if mibBuilder.loadTexts: panSystemClusterRepsetTable.setStatus('current')
panSystemClusterRepsetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1), ).setIndexNames((0, "PANASAS-SYSTEM-MIB-V1", "panSystemClusterRepsetEntryIndex"))
if mibBuilder.loadTexts: panSystemClusterRepsetEntry.setStatus('current')
panSystemClusterRepsetEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemClusterRepsetEntryIndex.setStatus('current')
panSystemClusterRepsetEntryIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemClusterRepsetEntryIpAddr.setStatus('current')
panSystemClusterRepsetEntryBladeHwSN = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 1, 3, 1, 3), PanSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemClusterRepsetEntryBladeHwSN.setStatus('current')
panSystemServicesTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2), )
if mibBuilder.loadTexts: panSystemServicesTable.setStatus('current')
panSystemServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1), ).setIndexNames((0, "PANASAS-SYSTEM-MIB-V1", "panSystemServicesId"))
if mibBuilder.loadTexts: panSystemServicesEntry.setStatus('current')
panSystemServicesId = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 1), PanSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemServicesId.setStatus('current')
panSystemServicesBladeHwSN = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 2), PanSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemServicesBladeHwSN.setStatus('current')
panSystemServicesType = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemServicesType.setStatus('current')
panSystemServicesInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemServicesInfo.setStatus('current')
panSystemServicesBackupBladeHwSN = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 2, 1, 5), PanSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemServicesBackupBladeHwSN.setStatus('current')
panSystemVolServiceTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3), )
if mibBuilder.loadTexts: panSystemVolServiceTable.setStatus('current')
panSystemVolServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1), ).setIndexNames((0, "PANASAS-SYSTEM-MIB-V1", "panSystemServicesId"), (0, "PANASAS-SYSTEM-MIB-V1", "panSystemVolServiceVolIndex"))
if mibBuilder.loadTexts: panSystemVolServiceEntry.setStatus('current')
panSystemVolServiceVolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemVolServiceVolIndex.setStatus('current')
panSystemVolServiceVolPath = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panSystemVolServiceVolPath.setStatus('current')
mibBuilder.exportSymbols("PANASAS-SYSTEM-MIB-V1", panSystemVolServiceVolPath=panSystemVolServiceVolPath, panSystemClusterName=panSystemClusterName, panSystemVolServiceTable=panSystemVolServiceTable, panSystemClusterManagementAddress=panSystemClusterManagementAddress, panSystemClusterRepsetEntryBladeHwSN=panSystemClusterRepsetEntryBladeHwSN, panSystemVolServiceEntry=panSystemVolServiceEntry, panSystemClusterRepsetEntryIpAddr=panSystemClusterRepsetEntryIpAddr, panSystemServicesBackupBladeHwSN=panSystemServicesBackupBladeHwSN, panSystemClusterRepsetTable=panSystemClusterRepsetTable, panSystemServicesInfo=panSystemServicesInfo, panSystemServicesBladeHwSN=panSystemServicesBladeHwSN, panSystemServicesType=panSystemServicesType, panSystemClusterRepsetEntryIndex=panSystemClusterRepsetEntryIndex, panSystemCluster=panSystemCluster, panSystemVolServiceVolIndex=panSystemVolServiceVolIndex, panSystemServicesTable=panSystemServicesTable, PYSNMP_MODULE_ID=panSystem, panSystemServicesEntry=panSystemServicesEntry, panSystemClusterRepsetEntry=panSystemClusterRepsetEntry, panSystem=panSystem, panSystemServicesId=panSystemServicesId)