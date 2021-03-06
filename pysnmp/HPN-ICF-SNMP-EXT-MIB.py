#
# PySNMP MIB module HPN-ICF-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
SnmpAdminString, SnmpSecurityModel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpSecurityModel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Counter32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Counter32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "Integer32", "Counter64")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
hpnicfSnmpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104))
hpnicfSnmpExt.setRevisions(('2009-04-07 17:00',))
if mibBuilder.loadTexts: hpnicfSnmpExt.setLastUpdated('200904071700Z')
if mibBuilder.loadTexts: hpnicfSnmpExt.setOrganization('')
hpnicfSnmpExtScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1))
hpnicfSnmpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2))
hpnicfSnmpExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 3))
hpnicfSnmpExtSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSnmpExtSnmpChannel.setStatus('current')
hpnicfSnmpExtReadCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSnmpExtReadCommunitySingle.setStatus('current')
hpnicfSnmpExtWriteCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSnmpExtWriteCommunitySingle.setStatus('current')
hpnicfSnmpExtMaxContextNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSnmpExtMaxContextNum.setStatus('current')
hpnicfSnmpExtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1), )
if mibBuilder.loadTexts: hpnicfSnmpExtCommunityTable.setStatus('current')
hpnicfSnmpExtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtCommunitySecurityLevel"), (0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtCommunitySecurityName"))
if mibBuilder.loadTexts: hpnicfSnmpExtCommunityEntry.setStatus('current')
hpnicfSnmpExtCommunitySecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 1), SnmpSecurityModel())
if mibBuilder.loadTexts: hpnicfSnmpExtCommunitySecurityLevel.setStatus('current')
hpnicfSnmpExtCommunitySecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpnicfSnmpExtCommunitySecurityName.setStatus('current')
hpnicfSnmpExtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSnmpExtCommunityName.setStatus('current')
hpnicfSnmpExtCommunityAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSnmpExtCommunityAclNum.setStatus('current')
hpnicfSnmpCommunityExTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2), )
if mibBuilder.loadTexts: hpnicfSnmpCommunityExTable.setStatus('current')
hpnicfSnmpCommunityExEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpCommunityExName"))
if mibBuilder.loadTexts: hpnicfSnmpCommunityExEntry.setStatus('current')
hpnicfSnmpCommunityExName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSnmpCommunityExName.setStatus('current')
hpnicfSnmpCommunityExWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSnmpCommunityExWrite.setStatus('current')
hpnicfSnmpCommunityExViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSnmpCommunityExViewName.setStatus('current')
hpnicfSnmpCommunityExAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSnmpCommunityExAclNum.setStatus('current')
hpnicfSnmpCommunityExRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSnmpCommunityExRowStatus.setStatus('current')
hpnicfSnmpExtContextTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3), )
if mibBuilder.loadTexts: hpnicfSnmpExtContextTable.setStatus('current')
hpnicfSnmpExtContextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtContextName"))
if mibBuilder.loadTexts: hpnicfSnmpExtContextEntry.setStatus('current')
hpnicfSnmpExtContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpnicfSnmpExtContextName.setStatus('current')
hpnicfSnmpExtContextRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSnmpExtContextRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-SNMP-EXT-MIB", PYSNMP_MODULE_ID=hpnicfSnmpExt, hpnicfSnmpExtContextTable=hpnicfSnmpExtContextTable, hpnicfSnmpExtWriteCommunitySingle=hpnicfSnmpExtWriteCommunitySingle, hpnicfSnmpExtSnmpChannel=hpnicfSnmpExtSnmpChannel, hpnicfSnmpExtCommunitySecurityName=hpnicfSnmpExtCommunitySecurityName, hpnicfSnmpExtTables=hpnicfSnmpExtTables, hpnicfSnmpExtCommunityTable=hpnicfSnmpExtCommunityTable, hpnicfSnmpCommunityExViewName=hpnicfSnmpCommunityExViewName, hpnicfSnmpExtCommunityEntry=hpnicfSnmpExtCommunityEntry, hpnicfSnmpCommunityExEntry=hpnicfSnmpCommunityExEntry, hpnicfSnmpCommunityExAclNum=hpnicfSnmpCommunityExAclNum, hpnicfSnmpCommunityExTable=hpnicfSnmpCommunityExTable, hpnicfSnmpExt=hpnicfSnmpExt, hpnicfSnmpExtCommunityAclNum=hpnicfSnmpExtCommunityAclNum, hpnicfSnmpExtContextName=hpnicfSnmpExtContextName, hpnicfSnmpExtCommunityName=hpnicfSnmpExtCommunityName, hpnicfSnmpExtReadCommunitySingle=hpnicfSnmpExtReadCommunitySingle, hpnicfSnmpExtCommunitySecurityLevel=hpnicfSnmpExtCommunitySecurityLevel, hpnicfSnmpCommunityExName=hpnicfSnmpCommunityExName, hpnicfSnmpExtNotifications=hpnicfSnmpExtNotifications, hpnicfSnmpCommunityExRowStatus=hpnicfSnmpCommunityExRowStatus, hpnicfSnmpExtContextEntry=hpnicfSnmpExtContextEntry, hpnicfSnmpCommunityExWrite=hpnicfSnmpCommunityExWrite, hpnicfSnmpExtMaxContextNum=hpnicfSnmpExtMaxContextNum, hpnicfSnmpExtContextRowStatus=hpnicfSnmpExtContextRowStatus, hpnicfSnmpExtScalarObjects=hpnicfSnmpExtScalarObjects)
