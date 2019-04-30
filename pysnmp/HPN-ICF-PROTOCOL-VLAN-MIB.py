#
# PySNMP MIB module HPN-ICF-PROTOCOL-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-PROTOCOL-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Unsigned32, Counter32, TimeTicks, Counter64, Bits, NotificationType, ObjectIdentity, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter32", "TimeTicks", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpnicfProtocolVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16))
hpnicfProtocolVlan.setRevisions(('2004-08-31 19:38',))
if mibBuilder.loadTexts: hpnicfProtocolVlan.setLastUpdated('200408311800Z')
if mibBuilder.loadTexts: hpnicfProtocolVlan.setOrganization('')
class HpnicfvProtocolVlanProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 101, 102, 103, 201))
    namedValues = NamedValues(("ip", 1), ("ipx", 2), ("at", 3), ("ipv6", 4), ("mode-llc", 101), ("mode-snap", 102), ("mode-ethernetii", 103), ("notConfigure", 201))

class HpnicfvProtocolVlanProtocolSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notused", 1), ("ethernetii", 2), ("llc", 3), ("raw", 4), ("snap", 5), ("etype", 6))

hpnicfProtocolVlanOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1))
hpnicfProtocolNumAllVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolNumAllVlan.setStatus('current')
hpnicfProtocolNumPerVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolNumPerVlan.setStatus('current')
hpnicfProtocolNumAllPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolNumAllPort.setStatus('current')
hpnicfProtocolNumPerPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolNumPerPort.setStatus('current')
hpnicfProtocolVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5), )
if mibBuilder.loadTexts: hpnicfProtocolVlanTable.setStatus('current')
hpnicfProtocolVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanVlanId"), (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolIndex"))
if mibBuilder.loadTexts: hpnicfProtocolVlanEntry.setStatus('current')
hpnicfProtocolVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfProtocolVlanVlanId.setStatus('current')
hpnicfProtocolVlanProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfProtocolVlanProtocolIndex.setStatus('current')
hpnicfProtocolVlanProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 3), HpnicfvProtocolVlanProtocolType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfProtocolVlanProtocolType.setStatus('current')
hpnicfProtocolVlanProtocolSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 4), HpnicfvProtocolVlanProtocolSubType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfProtocolVlanProtocolSubType.setStatus('current')
hpnicfProtocolVlanProtocolTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfProtocolVlanProtocolTypeValue.setStatus('current')
hpnicfProtocolVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfProtocolVlanRowStatus.setStatus('current')
hpnicfProtocolVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6), )
if mibBuilder.loadTexts: hpnicfProtocolVlanPortTable.setStatus('current')
hpnicfProtocolVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortIndex"), (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortVlanId"), (0, "HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolId"))
if mibBuilder.loadTexts: hpnicfProtocolVlanPortEntry.setStatus('current')
hpnicfProtocolVlanPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfProtocolVlanPortIndex.setStatus('current')
hpnicfProtocolVlanPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfProtocolVlanPortVlanId.setStatus('current')
hpnicfProtocolVlanPortProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: hpnicfProtocolVlanPortProtocolId.setStatus('current')
hpnicfProtocolVlanPortProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 4), HpnicfvProtocolVlanProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolVlanPortProtocolType.setStatus('current')
hpnicfProtocolVlanPortProtocolSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 5), HpnicfvProtocolVlanProtocolSubType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolVlanPortProtocolSubType.setStatus('current')
hpnicfProtocolVlanPortTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolVlanPortTypeValue.setStatus('current')
hpnicfProtocolVlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfProtocolVlanPortRowStatus.setStatus('current')
hpnicfProtocolVlanPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfProtocolVlanPortStatus.setStatus('current')
hpnicfDifferentProtocolNumAllPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDifferentProtocolNumAllPort.setStatus('current')
hpnicfProtocolVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2))
hpnicfProtocolVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 1))
hpnicfProtocolVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 1, 1)).setObjects(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanOperateGroup"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolGroup"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfProtocolVlanCompliance = hpnicfProtocolVlanCompliance.setStatus('current')
hpnicfProtocolVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2))
hpnicfProtocolVlanOperateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 1)).setObjects(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumAllVlan"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumPerVlan"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumAllPort"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolNumPerPort"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfDifferentProtocolNumAllPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfProtocolVlanOperateGroup = hpnicfProtocolVlanOperateGroup.setStatus('current')
hpnicfProtocolVlanProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 2)).setObjects(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolType"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolSubType"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanProtocolTypeValue"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfProtocolVlanProtocolGroup = hpnicfProtocolVlanProtocolGroup.setStatus('current')
hpnicfProtocolVlanPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16, 2, 2, 3)).setObjects(("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolType"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortProtocolSubType"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortTypeValue"), ("HPN-ICF-PROTOCOL-VLAN-MIB", "hpnicfProtocolVlanPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfProtocolVlanPortGroup = hpnicfProtocolVlanPortGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-PROTOCOL-VLAN-MIB", hpnicfProtocolVlan=hpnicfProtocolVlan, hpnicfProtocolVlanPortRowStatus=hpnicfProtocolVlanPortRowStatus, hpnicfProtocolVlanGroups=hpnicfProtocolVlanGroups, hpnicfProtocolVlanPortVlanId=hpnicfProtocolVlanPortVlanId, hpnicfProtocolVlanPortStatus=hpnicfProtocolVlanPortStatus, hpnicfDifferentProtocolNumAllPort=hpnicfDifferentProtocolNumAllPort, hpnicfProtocolVlanPortTable=hpnicfProtocolVlanPortTable, hpnicfProtocolVlanPortEntry=hpnicfProtocolVlanPortEntry, hpnicfProtocolNumAllVlan=hpnicfProtocolNumAllVlan, hpnicfProtocolVlanVlanId=hpnicfProtocolVlanVlanId, hpnicfProtocolNumPerVlan=hpnicfProtocolNumPerVlan, HpnicfvProtocolVlanProtocolType=HpnicfvProtocolVlanProtocolType, hpnicfProtocolVlanEntry=hpnicfProtocolVlanEntry, hpnicfProtocolNumPerPort=hpnicfProtocolNumPerPort, PYSNMP_MODULE_ID=hpnicfProtocolVlan, hpnicfProtocolVlanProtocolType=hpnicfProtocolVlanProtocolType, hpnicfProtocolVlanProtocolSubType=hpnicfProtocolVlanProtocolSubType, hpnicfProtocolVlanPortProtocolId=hpnicfProtocolVlanPortProtocolId, hpnicfProtocolVlanPortProtocolType=hpnicfProtocolVlanPortProtocolType, HpnicfvProtocolVlanProtocolSubType=HpnicfvProtocolVlanProtocolSubType, hpnicfProtocolVlanTable=hpnicfProtocolVlanTable, hpnicfProtocolNumAllPort=hpnicfProtocolNumAllPort, hpnicfProtocolVlanProtocolIndex=hpnicfProtocolVlanProtocolIndex, hpnicfProtocolVlanPortIndex=hpnicfProtocolVlanPortIndex, hpnicfProtocolVlanOperateGroup=hpnicfProtocolVlanOperateGroup, hpnicfProtocolVlanPortGroup=hpnicfProtocolVlanPortGroup, hpnicfProtocolVlanConformance=hpnicfProtocolVlanConformance, hpnicfProtocolVlanPortProtocolSubType=hpnicfProtocolVlanPortProtocolSubType, hpnicfProtocolVlanProtocolGroup=hpnicfProtocolVlanProtocolGroup, hpnicfProtocolVlanPortTypeValue=hpnicfProtocolVlanPortTypeValue, hpnicfProtocolVlanOperate=hpnicfProtocolVlanOperate, hpnicfProtocolVlanCompliance=hpnicfProtocolVlanCompliance, hpnicfProtocolVlanRowStatus=hpnicfProtocolVlanRowStatus, hpnicfProtocolVlanCompliances=hpnicfProtocolVlanCompliances, hpnicfProtocolVlanProtocolTypeValue=hpnicfProtocolVlanProtocolTypeValue)