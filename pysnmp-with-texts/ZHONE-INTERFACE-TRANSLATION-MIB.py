#
# PySNMP MIB module ZHONE-INTERFACE-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-INTERFACE-TRANSLATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InterfaceIndex, ifEntry = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Unsigned32, Integer32, Counter64, Gauge32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Unsigned32", "Integer32", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "TimeTicks")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
zhoneShelfIndex, zhoneModules, zhoneInterfaceTranslation, zhoneSlotIndex = mibBuilder.importSymbols("Zhone", "zhoneShelfIndex", "zhoneModules", "zhoneInterfaceTranslation", "zhoneSlotIndex")
ZhoneIfType, ZhoneSlotValue, ZhoneRowStatus, ZhoneShelfValue = mibBuilder.importSymbols("Zhone-TC", "ZhoneIfType", "ZhoneSlotValue", "ZhoneRowStatus", "ZhoneShelfValue")
zhoneInterfaceTrans = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 6))
zhoneInterfaceTrans.setRevisions(('2011-02-24 01:38', '2010-04-09 15:04', '2010-04-02 14:29', '2010-03-10 11:19', '2008-09-28 23:15', '2007-01-26 18:23', '2004-05-26 15:53', '2001-06-28 13:07', '2001-05-23 11:02', '2001-05-11 15:25', '2000-09-20 12:00', '2000-09-12 11:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhoneInterfaceTrans.setRevisionsDescriptions(('Changed the range of field redundancyParam1 -2147483648 to 2147483647', 'Add lineRedTraps', "Renamed 'ifType' to 'xxxifTypexxx' since ZMS can accidentaly compile in this deprecated object instead of MIB2 'ifType' object.", 'Add zhoneLineRedStatusTable Document redundancyParam1', 'V01.01.05 - Add zhoneDescriptionTable. Add zhoneIfXDescriptionIndex. Add zhoneIfXDescriptionIndexNext.', 'V01.01.04 - add shelf, slot, port and subport aliases to zhoneIfXEntry to allow user to create physical if-translate record.', 'V01.01.03 - add redundancyParam1.', 'V01.01.02 - fix the 17 slot limit problem', 'V01.01.01 - Deprecated physicalToIfIndexTable and replaced it with zhonePhysicalToIfIndexTable.', 'V01.01.00 - Added physicalFlag and ifTypeExtension records', 'V01.00.01 - Added markup for Physical-to-IfIndex Record', 'V01.00.00 - Initial Release',))
if mibBuilder.loadTexts: zhoneInterfaceTrans.setLastUpdated('201102241138Z')
if mibBuilder.loadTexts: zhoneInterfaceTrans.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: zhoneInterfaceTrans.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: zhoneInterfaceTrans.setDescription('Defines translation tables that provide the translation to and from shelf/slot/port/subport <-> interface number. Both table are created whenever an ifIndex is created. The ifStackDefaultTable is used to provide a roadmap of stack bindings, and to supply default ifAdminStatus values for new rows of the ifTable.')
ifIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 5, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndexNext.setStatus('current')
if mibBuilder.loadTexts: ifIndexNext.setDescription('Contains the next available ifIndex.')
physicalToIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2), )
if mibBuilder.loadTexts: physicalToIfIndexTable.setStatus('deprecated')
if mibBuilder.loadTexts: physicalToIfIndexTable.setDescription('Table to translate from shelf/slot/physical port/subport to the interface number (zhoneIfIndex). The physical port is the port number on the card selected by shelf/slot. The role of subport may vary depending on the card type, but is included to allow maximum flexibility and future exhancements. This table has been replaced by a zhonePhysicalToIfIndexTable. The objects in this table have been replaced by zhonePortIndex, zhoneSubPortIndex, zhonePhysicalIfIndex, zhoneIfType, and zhoneIfTypeExtension.')
physicalToIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1), ).setIndexNames((0, "Zhone", "zhoneShelfIndex"), (0, "Zhone", "zhoneSlotIndex"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "pportIndex"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "subPortIndex"))
if mibBuilder.loadTexts: physicalToIfIndexEntry.setStatus('deprecated')
if mibBuilder.loadTexts: physicalToIfIndexEntry.setDescription('The physical table is indexed by shelf/slot/physical port /subport. In instances where there is no subport the value of subport should be set to zero. This entry has been replaced by zhonePhysicalToIfIndexEntry.')
pportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: pportIndex.setStatus('deprecated')
if mibBuilder.loadTexts: pportIndex.setDescription('The port number of the physical port on the card or device. The numbering should start at 1 for the first port on the device and proceed sequentially. This object has been replaced by zhonePortIndex.')
subPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: subPortIndex.setStatus('deprecated')
if mibBuilder.loadTexts: subPortIndex.setDescription('This entry provides flexibility to define more than one interface on a port. The most common use of subport will be to handle structured TDM lines allowing for example an interface number to be assign to each DS1 in a DS3. Subport may also be used to handle other situations where a physical port contains more than one inetrface. This object has replaced by zhoneSubPortIndex.')
zhoneIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneIfIndex.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: zhoneIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: zhoneIfIndex.setDescription('The interface number of the pport or pport/subport that uniquely identifies the interface across the system. This object has been replaced by zhonePhysicalIfIndex.')
xxxifTypexxx = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xxxifTypexxx.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: xxxifTypexxx.setStatus('deprecated')
if mibBuilder.loadTexts: xxxifTypexxx.setDescription('The type of interface. Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention. This object has replaced by zhoneIfType. ')
ifIndexToPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3), )
if mibBuilder.loadTexts: ifIndexToPhysicalTable.setStatus('current')
if mibBuilder.loadTexts: ifIndexToPhysicalTable.setDescription('Table to translate from interface number (zhoneIfIndex) to the physical location and port (including subport where defined). zhoneShelfNumber is the number of the shelf on which the port is located and can have a value from 1-255, zhoneSlotNumber is the card slot on which card with the physical port is located and currently has a value of 1-18. The pportNumber identifies the specific physical port on the card beginning with port 1. subPortNumber issued to define multiple interfaces on a port as required, if the identified port has a single interface number, subport will be set to zero. ')
ifIndexToPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1), ).setIndexNames((0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfIndex"))
if mibBuilder.loadTexts: ifIndexToPhysicalEntry.setStatus('current')
if mibBuilder.loadTexts: ifIndexToPhysicalEntry.setDescription('The table is indexed by the zhoneIfidndex of the desired interface.')
zhoneShelfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 1), ZhoneShelfValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneShelfNumber.setStatus('current')
if mibBuilder.loadTexts: zhoneShelfNumber.setDescription('The zhoneShelfNumber is the physical address or number of the shelf for the desired interface. A Zhone system is limited to a maximum of 255 shelves. The first shelf in a system is shelf 1, ')
zhoneSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 2), ZhoneSlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneSlotNumber.setStatus('current')
if mibBuilder.loadTexts: zhoneSlotNumber.setDescription('The zhoneSlotNumber is the physical slot number on which the card containing the port or interface is located. Zhone shelves are currently limited to 30 slots numbered 1-30. Note that daughter boards do not have slot numbers.')
pportNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pportNumber.setStatus('current')
if mibBuilder.loadTexts: pportNumber.setDescription('The pportNumber defines the phyiscal port number on the selected shelf/slot (card). Port numbering begins with port 1 and ports are numbered sequentially. pportNumber 0 is invalid unless the ifIndex is for an interface that is not bound to a physical port.')
subPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: subPortNumber.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: subPortNumber.setStatus('current')
if mibBuilder.loadTexts: subPortNumber.setDescription('The subPortNumber is used to identify multiple logical ports on a physical that require their own interface number, e.g. DS1s on a DS3 port. Note that multiple protocol layers such as IP over ATM do not require unique interface numbers and are handled by the standard ifStackTable mechanism. Subport 0 is reserved to designate that a physical port has no subport and hence a single interface number. ')
ifaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 5), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaceType.setStatus('current')
if mibBuilder.loadTexts: ifaceType.setDescription('The type of interface. Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention.')
ifaceTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 6), ZhoneIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaceTypeExtension.setStatus('current')
if mibBuilder.loadTexts: ifaceTypeExtension.setDescription("This field is used to specify the zhone-proprietary interface type when necessary. For example, if the interface is a line-group, iftype is set to 'IANAIFTYPE_OTHER' and ifTypeExtension is set to 'ZHONEIFTYPE_LINEGROUP'. By default ifTypeExtension is set to 'ZHONEIFTYPE_NONE(0)'.")
ifStackDefaultTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4), )
if mibBuilder.loadTexts: ifStackDefaultTable.setStatus('current')
if mibBuilder.loadTexts: ifStackDefaultTable.setDescription('This table defines the default ifTable vales and stack arrangements (bindings) and unit numbers based on types of cards and ifTypes.')
ifStackDefaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1), ).setIndexNames((0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefUpperType"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefLowerType"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefCardType"))
if mibBuilder.loadTexts: ifStackDefaultEntry.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: ifStackDefaultEntry.setStatus('current')
if mibBuilder.loadTexts: ifStackDefaultEntry.setDescription("This table contains the unit/card type, the ifType of the 'from' layer (ifStkDefUpperIfType) and the ifType of the 'to' layer (ifStkDefLowerIfType) and the number of units for each association. Also the Default value ifAdminStatus in ifTable. A value must be supplied for all fields except ifStkDefAdminStatus to create a new row.")
ifStkDefCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ifStkDefCardType.setStatus('current')
if mibBuilder.loadTexts: ifStkDefCardType.setDescription('The numerical representation of unit/card type as specified in zhoneCardResourcesModule where cardZhoneType has the following defined values: unknownType(1), interShelf(2), infoServices(3), hdsl2(10),sechtor100(1001),zedge64(2001), and zplex10(3001). Other values may be used. ')
ifStkDefUpperType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 2), IANAifType())
if mibBuilder.loadTexts: ifStkDefUpperType.setStatus('current')
if mibBuilder.loadTexts: ifStkDefUpperType.setDescription('The value of ifType corresponding to the higher sublayer of the relationship, i.e., the sublayer that runs on top of the sublayer identified by the corresponding instance of ifStkDefLowerType.')
ifStkDefLowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 3), IANAifType())
if mibBuilder.loadTexts: ifStkDefLowerType.setStatus('current')
if mibBuilder.loadTexts: ifStkDefLowerType.setDescription('The value of ifType corresponding to the default lower sublayer of the relationship, i.e., the sublayer that runs under the sublayer identified by the corresponding instance of ifStkDefUpperType.')
ifStkDefUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('count').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifStkDefUnits.setStatus('current')
if mibBuilder.loadTexts: ifStkDefUnits.setDescription('Number of units for this association which indicates the number of ifindexes created for this particular iftype pair on this card type such as 48 creations for the initial version of the HDSL2 card. ')
ifStkDefAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifStkDefAdminStatus.setStatus('current')
if mibBuilder.loadTexts: ifStkDefAdminStatus.setDescription('Default value for ifAdminStatus in ifTable for the UPPPER ifindex associated with the ifStkDefUpperType.')
ifStkDefRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 6), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifStkDefRowStatus.setStatus('current')
if mibBuilder.loadTexts: ifStkDefRowStatus.setDescription('Row status used to create and/or remove rows from this table.')
ifInverseStackTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 5), )
if mibBuilder.loadTexts: ifInverseStackTable.setStatus('current')
if mibBuilder.loadTexts: ifInverseStackTable.setDescription(" This is the inverse ifstacktable in that the index scheme is lower.higher as opposed to higher.lower as defined in rfc2233. Comments and information is copied here for clarity. Information on a particular relationship between two sub-layers, specifying that one sub-layer runs on 'top' of the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable. Use of this table is solely for management stations to walk the table (getnext) from the lower physical port (ifindex) up the stack.")
ifInverseStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1), ).setIndexNames((0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifInverseStackLowerLayer"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifInverseStackHigherLayer"))
if mibBuilder.loadTexts: ifInverseStackEntry.setStatus('current')
if mibBuilder.loadTexts: ifInverseStackEntry.setDescription("The table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub- layers run 'on top of' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs over the sub-layer with ifIndex value y, then this table contains: ifStackStatus.y.x=active For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I. For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer. (If I is not involved in multiplexing, then these are the only two rows associated with I.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifStackStatus.0.x=active ifStackStatus.x.0=active A corresponding entry in this mib is made whenever an entry is made in the standard ifStackTable. Thus, deletion, creation, and modification is not possible on this table.")
ifInverseStackLowerLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ifInverseStackLowerLayer.setStatus('current')
if mibBuilder.loadTexts: ifInverseStackLowerLayer.setDescription("The value of ifIndex corresponding to the lower sub- layer of the relationship, i.e., the sub-layer which runs 'below' the sub-layer identified by the corresponding instance of ifInverseStackHigherLayer. If there is no lower sub-layer, then this object has the value 0. ")
ifInverseStackHigherLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: ifInverseStackHigherLayer.setStatus('current')
if mibBuilder.loadTexts: ifInverseStackHigherLayer.setDescription("The value of ifIndex corresponding to the higher sub-layer of the relationship, i.e., the sub-layer which runs on 'top' of the sub-layer identified by the corresponding instance of ifStackLowerLayer. If there is no higher sub-layer (below the internetwork layer), then this object has the value 0. ")
ifInverseStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInverseStackStatus.setStatus('current')
if mibBuilder.loadTexts: ifInverseStackStatus.setDescription('Status of this entry. If the entry exists, this value must be 1.')
zhoneIfXTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6), )
if mibBuilder.loadTexts: zhoneIfXTable.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXTable.setDescription('This table contains additional objects for the interface table. Each row corresponds to a conceptual row in the ifTable.')
zhoneIfXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1), )
ifEntry.registerAugmentions(("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfXEntry"))
zhoneIfXEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneIfXEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntry.setDescription('An entry containing additional management information applicable to a particular interface.')
physicalFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: physicalFlag.setStatus('current')
if mibBuilder.loadTexts: physicalFlag.setDescription("The flag is set to 'true(1)' if the ifIndex represents the physical layer. Otherwise the flag is set to 'false(2)'.")
ifTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 2), ZhoneIfType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifTypeExtension.setStatus('current')
if mibBuilder.loadTexts: ifTypeExtension.setDescription("This field is used to specify the zhone-proprietary interface type when necessary. For example, if the interface is a line-group, iftype is set to 'IANAIFTYPE_OTHER' and ifTypeExtension is set to 'ZHONEIFTYPE_LINEGROUP'. By default ifTypeExtension is set to 'ZHONEIFTYPE_NONE(0)'.")
redundancyParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: redundancyParam1.setStatus('current')
if mibBuilder.loadTexts: redundancyParam1.setDescription('For linegroups, this value contains information about line redundancy as follows: 0x8000 bit set => switchover on failure 0x7FFF number of seconds to wait before switchover 0x40000000 bit set => revert after switchover 0x3FFF0000 these 4 bits contains the number of seconds to wait before reverting 0x80000000 bit set => disable transmit on standby For physical interfaces: 0x00000001 bit set => secondary member of a protection pair bit clear => primary member, or standalone')
zhoneIfXEntryIfTypeAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 4), IANAifType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntryIfTypeAlias.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntryIfTypeAlias.setDescription('This object maps to ifType object within the ifEntry table. This object is used when creating a new row in the ifEntry table since ifType is read-only.')
zhoneIfXEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 5), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntryRowStatus.setDescription("This object is used to create and delete rows within the ifEntry table since ifEntry is standard and does not have a Row Status object. Currently, only ifType value of 'other' is allowed to be created via SNMP.")
zhoneIfXEntryShelfAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntryShelfAlias.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntryShelfAlias.setDescription('Writeable shelf number. This object maps to the read-only object zhoneShelfNumber.')
zhoneIfXEntrySlotAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 33))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntrySlotAlias.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntrySlotAlias.setDescription('Writeable slot number. This object maps to the read-only object zhoneSlotNumber.')
zhoneIfXEntryPortAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntryPortAlias.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntryPortAlias.setDescription('Writeable port number. This object maps to the read-only object zhonePortNumber.')
zhoneIfXEntrySubportAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXEntrySubportAlias.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXEntrySubportAlias.setDescription('Writeable subport number. This object maps to the read-only object zhoneSubPortNumber.')
zhoneIfXDescriptionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIfXDescriptionIndex.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXDescriptionIndex.setDescription('Index value of a zhoneDescriptionEntry. Zero indicates no reference to zhoneDescriptionEntry.')
zhonePhysicalToIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7), )
if mibBuilder.loadTexts: zhonePhysicalToIfIndexTable.setStatus('current')
if mibBuilder.loadTexts: zhonePhysicalToIfIndexTable.setDescription("Table to translate from shelf/slot/physical port/subport/ iftype/iftype-extension to the interface number (zhonePhysicalIfIndex). The physical port is the port number on the card selected by shelf/slot. The role of subport may vary depending on the card type, but is included to allow maximum flexibility and future exhancements. Iftype-extension is searched when iftype is set to 'ZHONEIFTYPE_NONE(0)'.")
zhonePhysicalToIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1), ).setIndexNames((0, "Zhone", "zhoneShelfIndex"), (0, "Zhone", "zhoneSlotIndex"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhonePortIndex"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSubPortIndex"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfType"), (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfTypeExtension"))
if mibBuilder.loadTexts: zhonePhysicalToIfIndexEntry.setStatus('current')
if mibBuilder.loadTexts: zhonePhysicalToIfIndexEntry.setDescription('The physical table is indexed by shelf/slot/physical port /subport/iftype/iftype-extension. In instances where there is no subport the value of subport should be set to zero.')
zhonePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: zhonePortIndex.setStatus('current')
if mibBuilder.loadTexts: zhonePortIndex.setDescription('The port number of the physical port on the card or device. The numbering should start at 1 for the first port on the device and proceed sequentially.')
zhoneSubPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: zhoneSubPortIndex.setStatus('current')
if mibBuilder.loadTexts: zhoneSubPortIndex.setDescription('This entry provides flexibility to define more than one interface on a port. The most common use of subport will be to handle structured TDM lines allowing for example an interface number to be assign to each DS1 in a DS3. Subport may also be used to handle other situations where a physical port contains more than one inetrface.')
zhoneIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 4), IANAifType())
if mibBuilder.loadTexts: zhoneIfType.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: zhoneIfType.setStatus('current')
if mibBuilder.loadTexts: zhoneIfType.setDescription('The type of interface. Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention. ')
zhoneIfTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 5), ZhoneIfType())
if mibBuilder.loadTexts: zhoneIfTypeExtension.setStatus('current')
if mibBuilder.loadTexts: zhoneIfTypeExtension.setDescription("This field is used to specify the zhone-proprietary interface type when necessary. For example, if the interface is a line-group, iftype is set to 'IANAIFTYPE_OTHER' and ifTypeExtension is set to 'ZHONEIFTYPE_LINEGROUP'. By default ifTypeExtension is set to 'ZHONEIFTYPE_NONE(0)'.")
zhonePhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhonePhysicalIfIndex.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2')
if mibBuilder.loadTexts: zhonePhysicalIfIndex.setStatus('current')
if mibBuilder.loadTexts: zhonePhysicalIfIndex.setDescription('The interface number of the pport or pport/subport that uniquely identifies the interface across the system.')
zhoneDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 8), )
if mibBuilder.loadTexts: zhoneDescriptionTable.setStatus('current')
if mibBuilder.loadTexts: zhoneDescriptionTable.setDescription('Table of description entries.')
zhoneDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1), ).setIndexNames((0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfXDescriptionIndex"))
if mibBuilder.loadTexts: zhoneDescriptionEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneDescriptionEntry.setDescription('Descritpion entry.')
zhoneDescriptionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1, 1), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDescriptionRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneDescriptionRowStatus.setDescription('Row status object.')
zhoneDescriptionText = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDescriptionText.setStatus('current')
if mibBuilder.loadTexts: zhoneDescriptionText.setDescription('Description object used as free format text description. Contains readable characters, with the following exclusions: 1. Double quotes 2. Carriage Returns 3. Line Feeds 4. Carat Maximum number of characters is 64, including any NULL terminator.')
zhoneIfXDescriptionIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 5, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneIfXDescriptionIndexNext.setStatus('current')
if mibBuilder.loadTexts: zhoneIfXDescriptionIndexNext.setDescription('Returns the next available zhoneIfXDescriptionIndex.')
zhoneLineRedStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 5, 10), )
if mibBuilder.loadTexts: zhoneLineRedStatusTable.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedStatusTable.setDescription('Line redundancy information')
zhoneLineRedStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1), ).setIndexNames((0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfIndex"))
if mibBuilder.loadTexts: zhoneLineRedStatusEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedStatusEntry.setDescription('Line redundancy information for on line')
zhoneLineRedStatusFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inactive", 1), ("standby", 2), ("active", 3), ("unavailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneLineRedStatusFunction.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedStatusFunction.setDescription('Current redundancy function as returned from LineRR. . inactive means registered but neither active nor standby . standby means this is the protection line in a pair. . active means either standalone or the working line in a protection pair. . unavailable means not registered with LineRR')
zhoneLineRedOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("oos", 2), ("trafficDisabled", 3), ("unavailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneLineRedOpStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedOpStatus.setDescription('Line status . active means line is up as standalone or the working line in a redundant pair. . oos means line is down . trafficDisabled means up as standby . unavailable means not registered with LineRR')
zhoneLineRedTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 5, 11))
if mibBuilder.loadTexts: zhoneLineRedTraps.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedTraps.setDescription('Traps for facility redundancy')
zhoneLineRedTrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0))
if mibBuilder.loadTexts: zhoneLineRedTrapsPrefix.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedTrapsPrefix.setDescription('Add zero in OID for traps.')
zhoneLineRedundancyUnsafe = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0, 1))
if mibBuilder.loadTexts: zhoneLineRedundancyUnsafe.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedundancyUnsafe.setDescription('Sent when configured peer is not traffic-disabled')
zhoneLineRedundancySafe = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0, 2))
if mibBuilder.loadTexts: zhoneLineRedundancySafe.setStatus('current')
if mibBuilder.loadTexts: zhoneLineRedundancySafe.setDescription('Sent when both lines in a facility-redundant pair have become redundancy ready.')
mibBuilder.exportSymbols("ZHONE-INTERFACE-TRANSLATION-MIB", zhoneDescriptionText=zhoneDescriptionText, ifInverseStackHigherLayer=ifInverseStackHigherLayer, zhoneIfXEntryPortAlias=zhoneIfXEntryPortAlias, ifTypeExtension=ifTypeExtension, zhoneLineRedundancySafe=zhoneLineRedundancySafe, ifInverseStackTable=ifInverseStackTable, zhoneShelfNumber=zhoneShelfNumber, ifStackDefaultTable=ifStackDefaultTable, PYSNMP_MODULE_ID=zhoneInterfaceTrans, ifIndexToPhysicalTable=ifIndexToPhysicalTable, zhoneIfTypeExtension=zhoneIfTypeExtension, ifStkDefUpperType=ifStkDefUpperType, zhoneDescriptionRowStatus=zhoneDescriptionRowStatus, zhoneIfXEntryRowStatus=zhoneIfXEntryRowStatus, zhoneLineRedTrapsPrefix=zhoneLineRedTrapsPrefix, zhoneIfXDescriptionIndex=zhoneIfXDescriptionIndex, zhoneIfXDescriptionIndexNext=zhoneIfXDescriptionIndexNext, pportIndex=pportIndex, zhoneLineRedOpStatus=zhoneLineRedOpStatus, zhoneDescriptionTable=zhoneDescriptionTable, zhoneDescriptionEntry=zhoneDescriptionEntry, ifInverseStackEntry=ifInverseStackEntry, subPortNumber=subPortNumber, physicalToIfIndexEntry=physicalToIfIndexEntry, zhoneIfXTable=zhoneIfXTable, zhoneIfXEntry=zhoneIfXEntry, ifStkDefRowStatus=ifStkDefRowStatus, zhoneLineRedStatusTable=zhoneLineRedStatusTable, ifStkDefCardType=ifStkDefCardType, ifIndexToPhysicalEntry=ifIndexToPhysicalEntry, pportNumber=pportNumber, zhoneSlotNumber=zhoneSlotNumber, zhoneIfType=zhoneIfType, zhonePhysicalIfIndex=zhonePhysicalIfIndex, ifInverseStackLowerLayer=ifInverseStackLowerLayer, ifaceType=ifaceType, zhonePortIndex=zhonePortIndex, zhonePhysicalToIfIndexEntry=zhonePhysicalToIfIndexEntry, ifStkDefAdminStatus=ifStkDefAdminStatus, zhoneSubPortIndex=zhoneSubPortIndex, zhoneIfIndex=zhoneIfIndex, redundancyParam1=redundancyParam1, ifStackDefaultEntry=ifStackDefaultEntry, zhoneInterfaceTrans=zhoneInterfaceTrans, physicalToIfIndexTable=physicalToIfIndexTable, zhoneIfXEntryIfTypeAlias=zhoneIfXEntryIfTypeAlias, ifInverseStackStatus=ifInverseStackStatus, zhonePhysicalToIfIndexTable=zhonePhysicalToIfIndexTable, ifStkDefUnits=ifStkDefUnits, ifIndexNext=ifIndexNext, physicalFlag=physicalFlag, zhoneIfXEntrySlotAlias=zhoneIfXEntrySlotAlias, zhoneIfXEntrySubportAlias=zhoneIfXEntrySubportAlias, xxxifTypexxx=xxxifTypexxx, subPortIndex=subPortIndex, zhoneIfXEntryShelfAlias=zhoneIfXEntryShelfAlias, zhoneLineRedTraps=zhoneLineRedTraps, ifStkDefLowerType=ifStkDefLowerType, zhoneLineRedStatusFunction=zhoneLineRedStatusFunction, ifaceTypeExtension=ifaceTypeExtension, zhoneLineRedundancyUnsafe=zhoneLineRedundancyUnsafe, zhoneLineRedStatusEntry=zhoneLineRedStatusEntry)
