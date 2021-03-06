#
# PySNMP MIB module IEEE8021-MIRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-MIRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:40:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
ieee8021PbbBackboneEdgeBridgeObjects, = mibBuilder.importSymbols("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeObjects")
IEEE8021BridgePortNumberOrZero, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumberOrZero")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32, Gauge32, ObjectIdentity, iso, Counter64, Bits, IpAddress, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32", "Gauge32", "ObjectIdentity", "iso", "Counter64", "Bits", "IpAddress", "Unsigned32", "TimeTicks", "Integer32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ieee8021MirpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 23))
ieee8021MirpMib.setRevisions(('2011-04-05 00:00',))
if mibBuilder.loadTexts: ieee8021MirpMib.setLastUpdated('201104050000Z')
if mibBuilder.loadTexts: ieee8021MirpMib.setOrganization('IEEE 802.1 Working Group')
ieee8021MirpMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 1))
ieee8021MirpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2))
ieee8021MirpPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 23, 1, 1), )
if mibBuilder.loadTexts: ieee8021MirpPortTable.setStatus('current')
ieee8021MirpPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-MIRP-MIB", "ieee8021MirpPortEntry"))
ieee8021MirpPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MirpPortEntry.setStatus('current')
ieee8021MirpPortEnabledStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MirpPortEnabledStatus.setStatus('current')
ieee8021PbbMirpEnableStatus = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpEnableStatus.setStatus('current')
ieee8021PbbMirpBvid = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 8), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpBvid.setStatus('current')
ieee8021PbbMirpDestSelector = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cbpMirpGroup", 1), ("cbpMirpVlan", 2), ("cbpMirpTable", 3))).clone('cbpMirpGroup')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpDestSelector.setStatus('current')
ieee8021PbbMirpPnpEnable = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpPnpEnable.setStatus('current')
ieee8021PbbMirpPnpPortNumber = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 11), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbMirpPnpPortNumber.setStatus('current')
ieee8021MirpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2, 1))
ieee8021MirpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2, 2))
ieee8021MirpReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 23, 2, 2, 1)).setObjects(("IEEE8021-MIRP-MIB", "ieee8021MirpPortEnabledStatus"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpEnableStatus"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpBvid"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpDestSelector"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpEnable"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpPortNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MirpReqdGroup = ieee8021MirpReqdGroup.setStatus('current')
ieee8021MirpBridgeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 23, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IEEE8021-MIRP-MIB", "ieee8021MirpReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MirpBridgeCompliance = ieee8021MirpBridgeCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-MIRP-MIB", ieee8021MirpMIBObjects=ieee8021MirpMIBObjects, ieee8021MirpPortEnabledStatus=ieee8021MirpPortEnabledStatus, ieee8021PbbMirpPnpPortNumber=ieee8021PbbMirpPnpPortNumber, ieee8021MirpPortEntry=ieee8021MirpPortEntry, ieee8021PbbMirpBvid=ieee8021PbbMirpBvid, ieee8021MirpConformance=ieee8021MirpConformance, ieee8021PbbMirpPnpEnable=ieee8021PbbMirpPnpEnable, ieee8021MirpCompliances=ieee8021MirpCompliances, ieee8021MirpMib=ieee8021MirpMib, ieee8021MirpReqdGroup=ieee8021MirpReqdGroup, ieee8021MirpPortTable=ieee8021MirpPortTable, ieee8021MirpBridgeCompliance=ieee8021MirpBridgeCompliance, ieee8021PbbMirpDestSelector=ieee8021PbbMirpDestSelector, PYSNMP_MODULE_ID=ieee8021MirpMib, ieee8021MirpGroups=ieee8021MirpGroups, ieee8021PbbMirpEnableStatus=ieee8021PbbMirpEnableStatus)
