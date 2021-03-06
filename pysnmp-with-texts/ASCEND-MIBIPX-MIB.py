#
# PySNMP MIB module ASCEND-MIBIPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, Gauge32, Unsigned32, iso, Bits, IpAddress, Integer32, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Unsigned32", "iso", "Bits", "IpAddress", "Integer32", "ObjectIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibipxGlobalProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 87))
mibipxInterfaceProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 86))
mibipxGlobalProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 87, 1), )
if mibBuilder.loadTexts: mibipxGlobalProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxGlobalProfileTable.setDescription('A list of mibipxGlobalProfile profile entries.')
mibipxGlobalProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPX-MIB", "ipxGlobalProfile-Index-o"))
if mibBuilder.loadTexts: mibipxGlobalProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxGlobalProfileEntry.setDescription('A mibipxGlobalProfile entry containing objects that maps to the parameters of mibipxGlobalProfile profile.')
ipxGlobalProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 1), Integer32()).setLabel("ipxGlobalProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxGlobalProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_Index_o.setDescription('')
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("ipxGlobalProfile-InterfaceAddress-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ipxGlobalProfile-InterfaceAddress-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 4), Integer32()).setLabel("ipxGlobalProfile-InterfaceAddress-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
ipxGlobalProfile_InterfaceAddress_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 5), Integer32()).setLabel("ipxGlobalProfile-InterfaceAddress-LogicalItem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_LogicalItem.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_InterfaceAddress_LogicalItem.setDescription('A number that specifies an addressable logical entity within the context of a physical address.')
ipxGlobalProfile_IpxRoutingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxGlobalProfile-IpxRoutingEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_IpxRoutingEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_IpxRoutingEnabled.setDescription("TRUE if this box is currently routing IPX. We don't do IPX routing protocols or packet forwarding if FALSE. Spoofing is independent, not affected by this.")
ipxGlobalProfile_IpxDialinPool = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 7), DisplayString()).setLabel("ipxGlobalProfile-IpxDialinPool").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_IpxDialinPool.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_IpxDialinPool.setDescription('Dialin Pool Numbers to be shared by the ipx wan interfaces')
ipxGlobalProfile_GlobalVrouter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 8), DisplayString()).setLabel("ipxGlobalProfile-GlobalVrouter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_GlobalVrouter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_GlobalVrouter.setDescription('Specifies the global VRouter.')
ipxGlobalProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ipxGlobalProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxGlobalProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxGlobalProfile_Action_o.setDescription('')
mibipxInterfaceProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 86, 1), )
if mibBuilder.loadTexts: mibipxInterfaceProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxInterfaceProfileTable.setDescription('A list of mibipxInterfaceProfile profile entries.')
mibipxInterfaceProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Shelf-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Slot-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Item-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-LogicalItem-o"))
if mibBuilder.loadTexts: mibipxInterfaceProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxInterfaceProfileEntry.setDescription('A mibipxInterfaceProfile entry containing objects that maps to the parameters of mibipxInterfaceProfile profile.')
ipxInterfaceProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 1), Integer32()).setLabel("ipxInterfaceProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_Shelf_o.setDescription('')
ipxInterfaceProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 2), Integer32()).setLabel("ipxInterfaceProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_Slot_o.setDescription('')
ipxInterfaceProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 3), Integer32()).setLabel("ipxInterfaceProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_Item_o.setDescription('')
ipxInterfaceProfile_LogicalItem_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 4), Integer32()).setLabel("ipxInterfaceProfile-LogicalItem-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_LogicalItem_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_LogicalItem_o.setDescription('')
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 7), Integer32()).setLabel("ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
ipxInterfaceProfile_InterfaceAddress_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 8), Integer32()).setLabel("ipxInterfaceProfile-InterfaceAddress-LogicalItem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_LogicalItem.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_InterfaceAddress_LogicalItem.setDescription('A number that specifies an addressable logical entity within the context of a physical address.')
ipxInterfaceProfile_IpxRoutingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxInterfaceProfile-IpxRoutingEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxRoutingEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxRoutingEnabled.setDescription("TRUE if this box is currently routing IPX. We don't do IPX routing protocols or packet forwarding if FALSE. Spoofing is not affected by this.")
ipxInterfaceProfile_IpxFrame = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("n-8023", 2), ("n-8022", 3), ("sNAP", 4), ("enetII", 5)))).setLabel("ipxInterfaceProfile-IpxFrame").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxFrame.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxFrame.setDescription('The IPX Frame Type supported in this interface.')
ipxInterfaceProfile_IpxNetNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 11), DisplayString()).setLabel("ipxInterfaceProfile-IpxNetNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxNetNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxNetNumber.setDescription('The network number of the ipx router.')
ipxInterfaceProfile_IpxType20 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxInterfaceProfile-IpxType20").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxType20.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxType20.setDescription('Propogate IPX Type 20 packets (NetBIOS).')
ipxInterfaceProfile_IpxSapFilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 13), DisplayString()).setLabel("ipxInterfaceProfile-IpxSapFilterName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapFilterName.setDescription('The name of this filter. All filters are referenced by name so a name must be assigned to active filters.')
ipxInterfaceProfile_oIPXSAPFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 14), Integer32()).setLabel("ipxInterfaceProfile-oIPXSAPFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_oIPXSAPFilter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_oIPXSAPFilter.setDescription('The number of the IPX SAP Filter assigned to this interface.')
ipxInterfaceProfile_IpxSapProxy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxInterfaceProfile-IpxSapProxy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxy.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxy.setDescription('Use IPX SAP Proxy.')
ipxInterfaceProfile_Vrouter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 16), DisplayString()).setLabel("ipxInterfaceProfile-Vrouter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_Vrouter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_Vrouter.setDescription('Specifies the VRouter in which this IPX interface profile belongs.')
ipxInterfaceProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ipxInterfaceProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_Action_o.setDescription('')
mibipxInterfaceProfile_IpxSapProxyNetTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 86, 2), ).setLabel("mibipxInterfaceProfile-IpxSapProxyNetTable")
if mibBuilder.loadTexts: mibipxInterfaceProfile_IpxSapProxyNetTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxInterfaceProfile_IpxSapProxyNetTable.setDescription('A list of mibipxInterfaceProfile__ipx_sap_proxy_net profile entries.')
mibipxInterfaceProfile_IpxSapProxyNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1), ).setLabel("mibipxInterfaceProfile-IpxSapProxyNetEntry").setIndexNames((0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Shelf-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Slot-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Item-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-LogicalItem-o"), (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Index-o"))
if mibBuilder.loadTexts: mibipxInterfaceProfile_IpxSapProxyNetEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxInterfaceProfile_IpxSapProxyNetEntry.setDescription('A mibipxInterfaceProfile__ipx_sap_proxy_net entry containing objects that maps to the parameters of mibipxInterfaceProfile__ipx_sap_proxy_net profile.')
ipxInterfaceProfile_IpxSapProxyNet_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 1), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Shelf_o.setDescription('')
ipxInterfaceProfile_IpxSapProxyNet_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 2), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Slot_o.setDescription('')
ipxInterfaceProfile_IpxSapProxyNet_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 3), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Item_o.setDescription('')
ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 4), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet-LogicalItem-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o.setDescription('')
ipxInterfaceProfile_IpxSapProxyNet_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 5), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet_Index_o.setDescription('')
ipxInterfaceProfile_IpxSapProxyNet = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 6), Integer32()).setLabel("ipxInterfaceProfile-IpxSapProxyNet").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet.setStatus('mandatory')
if mibBuilder.loadTexts: ipxInterfaceProfile_IpxSapProxyNet.setDescription('The Network# for IPX SAP Proxy.')
mibBuilder.exportSymbols("ASCEND-MIBIPX-MIB", ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf=ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf, ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber=ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber, ipxGlobalProfile_IpxRoutingEnabled=ipxGlobalProfile_IpxRoutingEnabled, ipxGlobalProfile_Action_o=ipxGlobalProfile_Action_o, ipxInterfaceProfile_IpxSapProxyNet=ipxInterfaceProfile_IpxSapProxyNet, ipxInterfaceProfile_IpxSapProxyNet_Slot_o=ipxInterfaceProfile_IpxSapProxyNet_Slot_o, ipxInterfaceProfile_IpxSapProxyNet_Index_o=ipxInterfaceProfile_IpxSapProxyNet_Index_o, ipxGlobalProfile_GlobalVrouter=ipxGlobalProfile_GlobalVrouter, mibipxInterfaceProfile=mibipxInterfaceProfile, ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber=ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber, mibipxInterfaceProfile_IpxSapProxyNetEntry=mibipxInterfaceProfile_IpxSapProxyNetEntry, ipxInterfaceProfile_Slot_o=ipxInterfaceProfile_Slot_o, ipxInterfaceProfile_oIPXSAPFilter=ipxInterfaceProfile_oIPXSAPFilter, ipxInterfaceProfile_IpxSapProxy=ipxInterfaceProfile_IpxSapProxy, ipxInterfaceProfile_Shelf_o=ipxInterfaceProfile_Shelf_o, mibipxInterfaceProfile_IpxSapProxyNetTable=mibipxInterfaceProfile_IpxSapProxyNetTable, ipxInterfaceProfile_IpxSapProxyNet_Shelf_o=ipxInterfaceProfile_IpxSapProxyNet_Shelf_o, ipxInterfaceProfile_Item_o=ipxInterfaceProfile_Item_o, ipxInterfaceProfile_IpxType20=ipxInterfaceProfile_IpxType20, ipxInterfaceProfile_LogicalItem_o=ipxInterfaceProfile_LogicalItem_o, mibipxGlobalProfileEntry=mibipxGlobalProfileEntry, mibipxInterfaceProfileTable=mibipxInterfaceProfileTable, DisplayString=DisplayString, ipxGlobalProfile_Index_o=ipxGlobalProfile_Index_o, ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot=ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot, mibipxGlobalProfile=mibipxGlobalProfile, mibipxGlobalProfileTable=mibipxGlobalProfileTable, ipxInterfaceProfile_IpxSapProxyNet_Item_o=ipxInterfaceProfile_IpxSapProxyNet_Item_o, ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o=ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o, ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf=ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf, ipxInterfaceProfile_IpxRoutingEnabled=ipxInterfaceProfile_IpxRoutingEnabled, ipxGlobalProfile_InterfaceAddress_LogicalItem=ipxGlobalProfile_InterfaceAddress_LogicalItem, ipxInterfaceProfile_Action_o=ipxInterfaceProfile_Action_o, ipxInterfaceProfile_Vrouter=ipxInterfaceProfile_Vrouter, ipxInterfaceProfile_IpxFrame=ipxInterfaceProfile_IpxFrame, mibipxInterfaceProfileEntry=mibipxInterfaceProfileEntry, ipxGlobalProfile_IpxDialinPool=ipxGlobalProfile_IpxDialinPool, ipxInterfaceProfile_InterfaceAddress_LogicalItem=ipxInterfaceProfile_InterfaceAddress_LogicalItem, ipxInterfaceProfile_IpxSapFilterName=ipxInterfaceProfile_IpxSapFilterName, ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot=ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot, ipxInterfaceProfile_IpxNetNumber=ipxInterfaceProfile_IpxNetNumber)
