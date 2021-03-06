#
# PySNMP MIB module CISCO-SSM-PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SSM-PROV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, MibIdentifier, Counter64, IpAddress, Integer32, ObjectIdentity, Bits, TimeTicks, Gauge32, NotificationType, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
ciscoSsmProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 448))
ciscoSsmProvMIB.setRevisions(('2005-02-15 00:00',))
if mibBuilder.loadTexts: ciscoSsmProvMIB.setLastUpdated('200502150000Z')
if mibBuilder.loadTexts: ciscoSsmProvMIB.setOrganization('Cisco Systems Inc.')
ciscoSsmProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 448, 1))
ciscoSsmProvMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 448, 2))
ssmProvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1))
ssmProvFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1), )
if mibBuilder.loadTexts: ssmProvFeatureTable.setStatus('current')
ssmProvFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureName"))
if mibBuilder.loadTexts: ssmProvFeatureEntry.setStatus('current')
ssmProvFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: ssmProvFeatureName.setStatus('current')
ssmProvFeatureNeedsImage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssmProvFeatureNeedsImage.setStatus('current')
ssmProvFeatureIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2), )
if mibBuilder.loadTexts: ssmProvFeatureIfTable.setStatus('current')
ssmProvFeatureIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfStartPort"), (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfEndPort"), (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfFeatureName"))
if mibBuilder.loadTexts: ssmProvFeatureIfEntry.setStatus('current')
ssmProvFeatureIfStartPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ssmProvFeatureIfStartPort.setStatus('current')
ssmProvFeatureIfEndPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: ssmProvFeatureIfEndPort.setStatus('current')
ssmProvFeatureIfFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: ssmProvFeatureIfFeatureName.setStatus('current')
ssmProvFeatureIfForceRemove = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forceReset", 1), ("noop", 2))).clone('noop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ssmProvFeatureIfForceRemove.setStatus('current')
ssmProvFeatureIfPartnerImageURI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ssmProvFeatureIfPartnerImageURI.setStatus('current')
ssmProvFeatureIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ssmProvFeatureIfRowStatus.setStatus('current')
ssmProvDppTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3), )
if mibBuilder.loadTexts: ssmProvDppTable.setStatus('current')
ssmProvDppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-SSM-PROV-MIB", "ssmProvDppStartPort"))
if mibBuilder.loadTexts: ssmProvDppEntry.setStatus('current')
ssmProvDppStartPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ssmProvDppStartPort.setStatus('current')
ssmProvDppEndPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssmProvDppEndPort.setStatus('current')
ssmProvDppName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssmProvDppName.setStatus('current')
ssmProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 1))
ssmProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2))
ssmProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 1, 1)).setObjects(("CISCO-SSM-PROV-MIB", "ssmProvFeatureGroup"), ("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfGroup"), ("CISCO-SSM-PROV-MIB", "ssmProvDppGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssmProvMIBCompliance = ssmProvMIBCompliance.setStatus('current')
ssmProvFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 1)).setObjects(("CISCO-SSM-PROV-MIB", "ssmProvFeatureNeedsImage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssmProvFeatureGroup = ssmProvFeatureGroup.setStatus('current')
ssmProvFeatureIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 2)).setObjects(("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfForceRemove"), ("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfPartnerImageURI"), ("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssmProvFeatureIfGroup = ssmProvFeatureIfGroup.setStatus('current')
ssmProvDppGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 3)).setObjects(("CISCO-SSM-PROV-MIB", "ssmProvDppEndPort"), ("CISCO-SSM-PROV-MIB", "ssmProvDppName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ssmProvDppGroup = ssmProvDppGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SSM-PROV-MIB", ssmProvFeatureIfStartPort=ssmProvFeatureIfStartPort, ssmProvDppName=ssmProvDppName, ssmProvMIBCompliances=ssmProvMIBCompliances, ssmProvFeatureEntry=ssmProvFeatureEntry, ciscoSsmProvMIB=ciscoSsmProvMIB, ssmProvDppTable=ssmProvDppTable, ssmProvConfiguration=ssmProvConfiguration, ssmProvFeatureIfRowStatus=ssmProvFeatureIfRowStatus, ssmProvFeatureIfEntry=ssmProvFeatureIfEntry, ssmProvDppGroup=ssmProvDppGroup, ssmProvFeatureGroup=ssmProvFeatureGroup, ssmProvFeatureName=ssmProvFeatureName, ssmProvFeatureIfFeatureName=ssmProvFeatureIfFeatureName, ssmProvFeatureIfGroup=ssmProvFeatureIfGroup, ssmProvDppEntry=ssmProvDppEntry, ssmProvDppStartPort=ssmProvDppStartPort, ciscoSsmProvMIBObjects=ciscoSsmProvMIBObjects, ssmProvFeatureIfPartnerImageURI=ssmProvFeatureIfPartnerImageURI, ssmProvFeatureNeedsImage=ssmProvFeatureNeedsImage, PYSNMP_MODULE_ID=ciscoSsmProvMIB, ciscoSsmProvMIBConform=ciscoSsmProvMIBConform, ssmProvMIBGroups=ssmProvMIBGroups, ssmProvFeatureIfTable=ssmProvFeatureIfTable, ssmProvDppEndPort=ssmProvDppEndPort, ssmProvFeatureTable=ssmProvFeatureTable, ssmProvMIBCompliance=ssmProvMIBCompliance, ssmProvFeatureIfForceRemove=ssmProvFeatureIfForceRemove, ssmProvFeatureIfEndPort=ssmProvFeatureIfEndPort)
