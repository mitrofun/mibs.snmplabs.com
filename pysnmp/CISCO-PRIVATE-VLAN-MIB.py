#
# PySNMP MIB module CISCO-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRIVATE-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
vtpVlanEntry, vtpVlanEditEntry = mibBuilder.importSymbols("CISCO-VTP-MIB", "vtpVlanEntry", "vtpVlanEditEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Integer32, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Integer32", "Bits", "iso", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoPrivateVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 173))
ciscoPrivateVlanMIB.setRevisions(('2005-09-08 00:00', '2002-07-24 00:00', '2001-05-23 00:00', '2001-04-17 00:00',))
if mibBuilder.loadTexts: ciscoPrivateVlanMIB.setLastUpdated('200509080000Z')
if mibBuilder.loadTexts: ciscoPrivateVlanMIB.setOrganization('Cisco Systems, Inc.')
class PrivateVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("primary", 2), ("isolated", 3), ("community", 4), ("twoWayCommunity", 5))

class VlanIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanIndexBitmap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

cpvlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 1))
cpvlanVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1))
cpvlanPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2))
cpvlanSVIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3))
cpvlanVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1), )
if mibBuilder.loadTexts: cpvlanVlanTable.setStatus('current')
cpvlanVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1), )
vtpVlanEntry.registerAugmentions(("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEntry"))
cpvlanVlanEntry.setIndexNames(*vtpVlanEntry.getIndexNames())
if mibBuilder.loadTexts: cpvlanVlanEntry.setStatus('current')
cpvlanVlanPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1, 1), PrivateVlanType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanVlanPrivateVlanType.setStatus('current')
cpvlanVlanAssociatedPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanVlanAssociatedPrimaryVlan.setStatus('current')
cpvlanVlanEditTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2), )
if mibBuilder.loadTexts: cpvlanVlanEditTable.setStatus('current')
cpvlanVlanEditEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1), )
vtpVlanEditEntry.registerAugmentions(("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEditEntry"))
cpvlanVlanEditEntry.setIndexNames(*vtpVlanEditEntry.getIndexNames())
if mibBuilder.loadTexts: cpvlanVlanEditEntry.setStatus('current')
cpvlanVlanEditPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1, 1), PrivateVlanType().clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanVlanEditPrivateVlanType.setStatus('current')
cpvlanVlanEditAssocPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanVlanEditAssocPrimaryVlan.setStatus('current')
cpvlanPrivatePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1), )
if mibBuilder.loadTexts: cpvlanPrivatePortTable.setStatus('current')
cpvlanPrivatePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpvlanPrivatePortEntry.setStatus('current')
cpvlanPrivatePortSecondaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPrivatePortSecondaryVlan.setStatus('current')
cpvlanPromPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2), )
if mibBuilder.loadTexts: cpvlanPromPortTable.setStatus('current')
cpvlanPromPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpvlanPromPortEntry.setStatus('current')
cpvlanPromPortMultiPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanPromPortMultiPrimaryVlan.setStatus('current')
cpvlanPromPortSecondaryRemap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPromPortSecondaryRemap.setStatus('current')
cpvlanPromPortSecondaryRemap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPromPortSecondaryRemap2k.setStatus('current')
cpvlanPromPortSecondaryRemap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPromPortSecondaryRemap3k.setStatus('current')
cpvlanPromPortSecondaryRemap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPromPortSecondaryRemap4k.setStatus('current')
cpvlanPromPortTwoWayRemapCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanPromPortTwoWayRemapCapable.setStatus('current')
cpvlanPortModeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3), )
if mibBuilder.loadTexts: cpvlanPortModeTable.setStatus('current')
cpvlanPortModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpvlanPortModeEntry.setStatus('current')
cpvlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nonPrivateVlan", 1), ("host", 2), ("promiscuous", 3), ("secondaryTrunk", 4), ("promiscuousTrunk", 5))).clone('nonPrivateVlan')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanPortMode.setStatus('current')
cpvlanTrunkPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4), )
if mibBuilder.loadTexts: cpvlanTrunkPortTable.setStatus('current')
cpvlanTrunkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpvlanTrunkPortEntry.setStatus('current')
cpvlanTrunkPortDynamicState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("onNoNegotiate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortDynamicState.setStatus('current')
cpvlanTrunkPortEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1Q", 1), ("isl", 2), ("negotiate", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortEncapType.setStatus('current')
cpvlanTrunkPortNativeVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 3), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortNativeVlan.setStatus('current')
cpvlanTrunkPortSecondaryVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 4), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortSecondaryVlans.setStatus('current')
cpvlanTrunkPortSecondaryVlans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 5), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortSecondaryVlans2k.setStatus('current')
cpvlanTrunkPortSecondaryVlans3k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 6), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortSecondaryVlans3k.setStatus('current')
cpvlanTrunkPortSecondaryVlans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 7), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortSecondaryVlans4k.setStatus('current')
cpvlanTrunkPortNormalVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 8), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortNormalVlans.setStatus('current')
cpvlanTrunkPortNormalVlans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 9), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortNormalVlans2k.setStatus('current')
cpvlanTrunkPortNormalVlans3k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 10), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortNormalVlans3k.setStatus('current')
cpvlanTrunkPortNormalVlans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 11), VlanIndexBitmap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanTrunkPortNormalVlans4k.setStatus('current')
cpvlanTrunkPortDynamicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trunking", 1), ("notTrunking", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanTrunkPortDynamicStatus.setStatus('current')
cpvlanTrunkPortEncapOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1Q", 1), ("isl", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpvlanTrunkPortEncapOperType.setStatus('current')
cpvlanSVIMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1), )
if mibBuilder.loadTexts: cpvlanSVIMappingTable.setStatus('current')
cpvlanSVIMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-PRIVATE-VLAN-MIB", "cpvlanSVIMappingVlanIndex"))
if mibBuilder.loadTexts: cpvlanSVIMappingEntry.setStatus('current')
cpvlanSVIMappingVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1, 1), VlanIndexOrZero())
if mibBuilder.loadTexts: cpvlanSVIMappingVlanIndex.setStatus('current')
cpvlanSVIMappingPrimarySVI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpvlanSVIMappingPrimarySVI.setStatus('current')
cpvlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 2))
cpvlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 1))
cpvlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2))
cpvlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanMIBCompliance = cpvlanMIBCompliance.setStatus('current')
cpvlanVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 1)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanPrivateVlanType"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanAssociatedPrimaryVlan"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEditPrivateVlanType"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEditAssocPrimaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanVlanGroup = cpvlanVlanGroup.setStatus('current')
cpvlanPrivatePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 2)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPrivatePortSecondaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanPrivatePortGroup = cpvlanPrivatePortGroup.setStatus('current')
cpvlanPromPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 3)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortMultiPrimaryVlan"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortTwoWayRemapCapable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanPromPortGroup = cpvlanPromPortGroup.setStatus('current')
cpvlanPromPort4kGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 4)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap2k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap3k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanPromPort4kGroup = cpvlanPromPort4kGroup.setStatus('current')
cpvlanPortModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 5)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPortMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanPortModeGroup = cpvlanPortModeGroup.setStatus('current')
cpvlanSVIMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 6)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanSVIMappingPrimarySVI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanSVIMappingGroup = cpvlanSVIMappingGroup.setStatus('current')
cpvlanTrunkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 7)).setObjects(("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortDynamicState"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortEncapType"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNativeVlan"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans2k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans3k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans4k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans2k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans3k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans4k"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortDynamicStatus"), ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortEncapOperType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpvlanTrunkPortGroup = cpvlanTrunkPortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-MIB", cpvlanPromPortTwoWayRemapCapable=cpvlanPromPortTwoWayRemapCapable, cpvlanPortModeTable=cpvlanPortModeTable, cpvlanPromPort4kGroup=cpvlanPromPort4kGroup, VlanIndexBitmap=VlanIndexBitmap, cpvlanVlanTable=cpvlanVlanTable, cpvlanVlanEditAssocPrimaryVlan=cpvlanVlanEditAssocPrimaryVlan, cpvlanTrunkPortTable=cpvlanTrunkPortTable, cpvlanPortModeGroup=cpvlanPortModeGroup, cpvlanPromPortGroup=cpvlanPromPortGroup, cpvlanTrunkPortEncapOperType=cpvlanTrunkPortEncapOperType, cpvlanMIBConformance=cpvlanMIBConformance, cpvlanPrivatePortSecondaryVlan=cpvlanPrivatePortSecondaryVlan, cpvlanTrunkPortNormalVlans2k=cpvlanTrunkPortNormalVlans2k, cpvlanVlanPrivateVlanType=cpvlanVlanPrivateVlanType, cpvlanSVIObjects=cpvlanSVIObjects, PrivateVlanType=PrivateVlanType, cpvlanPortModeEntry=cpvlanPortModeEntry, cpvlanTrunkPortDynamicState=cpvlanTrunkPortDynamicState, cpvlanTrunkPortNativeVlan=cpvlanTrunkPortNativeVlan, VlanIndexOrZero=VlanIndexOrZero, cpvlanPromPortSecondaryRemap4k=cpvlanPromPortSecondaryRemap4k, cpvlanVlanObjects=cpvlanVlanObjects, cpvlanPromPortEntry=cpvlanPromPortEntry, cpvlanPromPortSecondaryRemap3k=cpvlanPromPortSecondaryRemap3k, cpvlanTrunkPortEncapType=cpvlanTrunkPortEncapType, cpvlanSVIMappingGroup=cpvlanSVIMappingGroup, cpvlanTrunkPortSecondaryVlans2k=cpvlanTrunkPortSecondaryVlans2k, cpvlanTrunkPortEntry=cpvlanTrunkPortEntry, cpvlanSVIMappingTable=cpvlanSVIMappingTable, cpvlanVlanGroup=cpvlanVlanGroup, cpvlanVlanEditPrivateVlanType=cpvlanVlanEditPrivateVlanType, cpvlanPortObjects=cpvlanPortObjects, cpvlanSVIMappingVlanIndex=cpvlanSVIMappingVlanIndex, PYSNMP_MODULE_ID=ciscoPrivateVlanMIB, cpvlanSVIMappingEntry=cpvlanSVIMappingEntry, cpvlanMIBCompliance=cpvlanMIBCompliance, cpvlanTrunkPortSecondaryVlans3k=cpvlanTrunkPortSecondaryVlans3k, cpvlanVlanEditTable=cpvlanVlanEditTable, cpvlanPrivatePortGroup=cpvlanPrivatePortGroup, cpvlanSVIMappingPrimarySVI=cpvlanSVIMappingPrimarySVI, cpvlanVlanEntry=cpvlanVlanEntry, cpvlanPrivatePortTable=cpvlanPrivatePortTable, cpvlanTrunkPortDynamicStatus=cpvlanTrunkPortDynamicStatus, cpvlanPromPortSecondaryRemap2k=cpvlanPromPortSecondaryRemap2k, cpvlanPromPortMultiPrimaryVlan=cpvlanPromPortMultiPrimaryVlan, cpvlanPortMode=cpvlanPortMode, cpvlanMIBCompliances=cpvlanMIBCompliances, cpvlanPromPortTable=cpvlanPromPortTable, cpvlanTrunkPortNormalVlans=cpvlanTrunkPortNormalVlans, ciscoPrivateVlanMIB=ciscoPrivateVlanMIB, cpvlanVlanAssociatedPrimaryVlan=cpvlanVlanAssociatedPrimaryVlan, cpvlanVlanEditEntry=cpvlanVlanEditEntry, cpvlanTrunkPortGroup=cpvlanTrunkPortGroup, cpvlanPromPortSecondaryRemap=cpvlanPromPortSecondaryRemap, cpvlanTrunkPortNormalVlans3k=cpvlanTrunkPortNormalVlans3k, cpvlanMIBObjects=cpvlanMIBObjects, cpvlanTrunkPortSecondaryVlans4k=cpvlanTrunkPortSecondaryVlans4k, cpvlanTrunkPortNormalVlans4k=cpvlanTrunkPortNormalVlans4k, cpvlanMIBGroups=cpvlanMIBGroups, cpvlanPrivatePortEntry=cpvlanPrivatePortEntry, cpvlanTrunkPortSecondaryVlans=cpvlanTrunkPortSecondaryVlans)
