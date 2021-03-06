#
# PySNMP MIB module CCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CCAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
PhysicalIndexOrZero, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndexOrZero")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpegInputProgEntry, mpegOutputTSIndex, mpegInputTSIndex, mpegOutputProgIndex, mpegInputProgIndex, mpegVideoSessionIndex, mpegOutputProgEntry = mibBuilder.importSymbols("SCTE-HMS-MPEG-MIB", "mpegInputProgEntry", "mpegOutputTSIndex", "mpegInputTSIndex", "mpegOutputProgIndex", "mpegInputProgIndex", "mpegVideoSessionIndex", "mpegOutputProgEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, ObjectIdentity, ModuleIdentity, TimeTicks, MibIdentifier, Unsigned32, Gauge32, Bits, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "Gauge32", "Bits", "IpAddress", "NotificationType", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ccapMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24))
ccapMib.setRevisions(('2013-04-04 00:00', '2012-08-09 00:00', '2011-08-05 00:00', '2011-05-17 00:00',))
if mibBuilder.loadTexts: ccapMib.setLastUpdated('201304040000Z')
if mibBuilder.loadTexts: ccapMib.setOrganization('Cable Television Laboratories, Inc.')
ccapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 0))
ccapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1))
ccapInterfacesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 1))
ccapInterfaceIndexMapTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 1, 1), )
if mibBuilder.loadTexts: ccapInterfaceIndexMapTable.setStatus('current')
ccapInterfaceIndexMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccapInterfaceIndexMapEntry.setStatus('current')
ccapInterfaceIndexMapPath = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapInterfaceIndexMapPath.setStatus('current')
ccapInterfaceIndexMapEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 1, 1, 1, 2), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapInterfaceIndexMapEntPhysicalIndex.setStatus('current')
ccapMpegObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2))
ccapMpegInputProgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 1), )
if mibBuilder.loadTexts: ccapMpegInputProgTable.setStatus('current')
ccapMpegInputProgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 1, 1), )
mpegInputProgEntry.registerAugmentions(("CCAP-MIB", "ccapMpegInputProgEntry"))
ccapMpegInputProgEntry.setIndexNames(*mpegInputProgEntry.getIndexNames())
if mibBuilder.loadTexts: ccapMpegInputProgEntry.setStatus('current')
ccapMpegInputProgBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 1, 1, 1), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegInputProgBitRate.setStatus('current')
ccapMpegInputProgRequestedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 1, 1, 2), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegInputProgRequestedBandwidth.setStatus('current')
ccapMpegOutputProgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 2), )
if mibBuilder.loadTexts: ccapMpegOutputProgTable.setStatus('current')
ccapMpegOutputProgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 2, 1), )
mpegOutputProgEntry.registerAugmentions(("CCAP-MIB", "ccapMpegOutputProgEntry"))
ccapMpegOutputProgEntry.setIndexNames(*mpegOutputProgEntry.getIndexNames())
if mibBuilder.loadTexts: ccapMpegOutputProgEntry.setStatus('current')
ccapMpegOutputProgBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 2, 1, 1), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegOutputProgBitRate.setStatus('current')
ccapMpegInputProgVideoSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 3), )
if mibBuilder.loadTexts: ccapMpegInputProgVideoSessionTable.setStatus('current')
ccapMpegInputProgVideoSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 3, 1), ).setIndexNames((0, "SCTE-HMS-MPEG-MIB", "mpegInputTSIndex"), (0, "SCTE-HMS-MPEG-MIB", "mpegInputProgIndex"), (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"))
if mibBuilder.loadTexts: ccapMpegInputProgVideoSessionEntry.setStatus('current')
ccapMpegInputProgVideoSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("closed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegInputProgVideoSessionStatus.setStatus('current')
ccapMpegOutputProgVideoSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 4), )
if mibBuilder.loadTexts: ccapMpegOutputProgVideoSessionTable.setStatus('current')
ccapMpegOutputProgVideoSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 4, 1), ).setIndexNames((0, "SCTE-HMS-MPEG-MIB", "mpegOutputTSIndex"), (0, "SCTE-HMS-MPEG-MIB", "mpegOutputProgIndex"), (0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"))
if mibBuilder.loadTexts: ccapMpegOutputProgVideoSessionEntry.setStatus('current')
ccapMpegOutputProgVideoSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("closed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegOutputProgVideoSessionStatus.setStatus('current')
ccapCryptoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3))
ccapEcmgStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 1), )
if mibBuilder.loadTexts: ccapEcmgStatusTable.setStatus('current')
ccapEcmgStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 1, 1), ).setIndexNames((0, "CCAP-MIB", "ccapEcmgIndex"))
if mibBuilder.loadTexts: ccapEcmgStatusEntry.setStatus('current')
ccapEcmgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ccapEcmgIndex.setStatus('current')
ccapEcmgNumActiveSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapEcmgNumActiveSessions.setStatus('current')
ccapEcmgCwMessageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapEcmgCwMessageCount.setStatus('current')
ccapEcmdStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 2), )
if mibBuilder.loadTexts: ccapEcmdStatusTable.setStatus('current')
ccapEcmdStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 2, 1), ).setIndexNames((0, "CCAP-MIB", "ccapEcmdIndex"))
if mibBuilder.loadTexts: ccapEcmdStatusEntry.setStatus('current')
ccapEcmdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ccapEcmdIndex.setStatus('current')
ccapEcmdNumActiveSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapEcmdNumActiveSessions.setStatus('current')
ccapEcmdCwMessageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapEcmdCwMessageCount.setStatus('current')
ccapMpegDecryptSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 3), )
if mibBuilder.loadTexts: ccapMpegDecryptSessionTable.setStatus('current')
ccapMpegDecryptSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 3, 1), ).setIndexNames((0, "SCTE-HMS-MPEG-MIB", "mpegVideoSessionIndex"))
if mibBuilder.loadTexts: ccapMpegDecryptSessionEntry.setStatus('current')
ccapMpegDecryptSessionDecrypted = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 1, 3, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccapMpegDecryptSessionDecrypted.setStatus('current')
ccapMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2))
ccapMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 1))
ccapMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 2))
ccapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 1, 1)).setObjects(("CCAP-MIB", "ccapInterfacesGroup"), ("CCAP-MIB", "ccapMpegGroup"), ("CCAP-MIB", "ccapCryptoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccapCompliance = ccapCompliance.setStatus('current')
ccapInterfacesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 2, 1)).setObjects(("CCAP-MIB", "ccapInterfaceIndexMapPath"), ("CCAP-MIB", "ccapInterfaceIndexMapEntPhysicalIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccapInterfacesGroup = ccapInterfacesGroup.setStatus('current')
ccapMpegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 2, 2)).setObjects(("CCAP-MIB", "ccapMpegInputProgBitRate"), ("CCAP-MIB", "ccapMpegInputProgRequestedBandwidth"), ("CCAP-MIB", "ccapMpegInputProgBitRate"), ("CCAP-MIB", "ccapMpegInputProgVideoSessionStatus"), ("CCAP-MIB", "ccapMpegOutputProgVideoSessionStatus"), ("CCAP-MIB", "ccapMpegOutputProgBitRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccapMpegGroup = ccapMpegGroup.setStatus('current')
ccapCryptoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 24, 2, 2, 3)).setObjects(("CCAP-MIB", "ccapEcmgNumActiveSessions"), ("CCAP-MIB", "ccapEcmgCwMessageCount"), ("CCAP-MIB", "ccapEcmdNumActiveSessions"), ("CCAP-MIB", "ccapEcmdCwMessageCount"), ("CCAP-MIB", "ccapMpegDecryptSessionDecrypted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccapCryptoGroup = ccapCryptoGroup.setStatus('current')
mibBuilder.exportSymbols("CCAP-MIB", ccapInterfacesObjects=ccapInterfacesObjects, ccapMibConformance=ccapMibConformance, ccapEcmdStatusEntry=ccapEcmdStatusEntry, ccapCompliance=ccapCompliance, ccapNotifications=ccapNotifications, ccapEcmdStatusTable=ccapEcmdStatusTable, ccapMpegGroup=ccapMpegGroup, ccapMpegInputProgTable=ccapMpegInputProgTable, ccapMpegOutputProgTable=ccapMpegOutputProgTable, ccapMpegOutputProgVideoSessionEntry=ccapMpegOutputProgVideoSessionEntry, PYSNMP_MODULE_ID=ccapMib, ccapMpegInputProgVideoSessionTable=ccapMpegInputProgVideoSessionTable, ccapMpegInputProgEntry=ccapMpegInputProgEntry, ccapMibCompliances=ccapMibCompliances, ccapCryptoGroup=ccapCryptoGroup, ccapMpegDecryptSessionTable=ccapMpegDecryptSessionTable, ccapEcmgIndex=ccapEcmgIndex, ccapEcmdNumActiveSessions=ccapEcmdNumActiveSessions, ccapInterfaceIndexMapEntPhysicalIndex=ccapInterfaceIndexMapEntPhysicalIndex, ccapObjects=ccapObjects, ccapMibGroups=ccapMibGroups, ccapMpegOutputProgVideoSessionStatus=ccapMpegOutputProgVideoSessionStatus, ccapMpegOutputProgEntry=ccapMpegOutputProgEntry, ccapMpegOutputProgVideoSessionTable=ccapMpegOutputProgVideoSessionTable, ccapInterfacesGroup=ccapInterfacesGroup, ccapMpegInputProgVideoSessionEntry=ccapMpegInputProgVideoSessionEntry, ccapMpegObjects=ccapMpegObjects, ccapEcmdIndex=ccapEcmdIndex, ccapEcmgStatusEntry=ccapEcmgStatusEntry, ccapMpegInputProgRequestedBandwidth=ccapMpegInputProgRequestedBandwidth, ccapInterfaceIndexMapEntry=ccapInterfaceIndexMapEntry, ccapInterfaceIndexMapTable=ccapInterfaceIndexMapTable, ccapInterfaceIndexMapPath=ccapInterfaceIndexMapPath, ccapEcmgStatusTable=ccapEcmgStatusTable, ccapMib=ccapMib, ccapMpegDecryptSessionDecrypted=ccapMpegDecryptSessionDecrypted, ccapMpegOutputProgBitRate=ccapMpegOutputProgBitRate, ccapEcmdCwMessageCount=ccapEcmdCwMessageCount, ccapMpegDecryptSessionEntry=ccapMpegDecryptSessionEntry, ccapCryptoObjects=ccapCryptoObjects, ccapEcmgNumActiveSessions=ccapEcmgNumActiveSessions, ccapMpegInputProgBitRate=ccapMpegInputProgBitRate, ccapEcmgCwMessageCount=ccapEcmgCwMessageCount, ccapMpegInputProgVideoSessionStatus=ccapMpegInputProgVideoSessionStatus)
