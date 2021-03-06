#
# PySNMP MIB module H3C-LOGIC-VOLUME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-LOGIC-VOLUME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
H3cStorageActionType, H3cStorageEnableState, h3cStorageRef, H3cLvIDType, H3cSessionIDType, H3cStorageLedStateType, H3cRaidIDType, H3cWwpnListType = mibBuilder.importSymbols("H3C-STORAGE-REF-MIB", "H3cStorageActionType", "H3cStorageEnableState", "h3cStorageRef", "H3cLvIDType", "H3cSessionIDType", "H3cStorageLedStateType", "H3cRaidIDType", "H3cWwpnListType")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Counter64, ObjectIdentity, NotificationType, Counter32, Bits, Unsigned32, TimeTicks, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "NotificationType", "Counter32", "Bits", "Unsigned32", "TimeTicks", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
DisplayString, TextualConvention, RowStatus, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue", "DateAndTime")
h3cLogicVolume = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5))
if mibBuilder.loadTexts: h3cLogicVolume.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: h3cLogicVolume.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cLogicVolume.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cLogicVolume.setDescription('This MIB describes the general information of disk device.')
h3cLvMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1))
h3cLogicResourceCapacityObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1))
h3cLvCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvCount.setStatus('current')
if mibBuilder.loadTexts: h3cLvCount.setDescription('This object identifies the maximal number of logic volumes supported.')
h3cLvMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 2), Integer32()).setUnits('TB').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvMaxSize.setStatus('current')
if mibBuilder.loadTexts: h3cLvMaxSize.setDescription('This object identifies the maximal size of logic volumes supported.')
h3cTargetCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTargetCount.setStatus('current')
if mibBuilder.loadTexts: h3cTargetCount.setDescription('This object identifies the maximal number of targets supported.')
h3cInitiatorCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cInitiatorCount.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorCount.setDescription('This object identifies the maximal number of initiators supported.')
h3cSanClientCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSanClientCount.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientCount.setDescription('This object identifies the maximal number of SAN client supported.')
h3cLogicVolumeResource = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2))
h3cLvCreateIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 1), H3cLvIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvCreateIndex.setStatus('current')
if mibBuilder.loadTexts: h3cLvCreateIndex.setDescription('This object supplys an valid index which uses to create a new entry for the h3cLvTable object. Reference to h3cLvRowStatus object for more information. Note that if an entry of the associated table has been created or deleted, the historical value of this object may be an invalid index to create a new entry for the associated table.')
h3cLvTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2), )
if mibBuilder.loadTexts: h3cLvTable.setStatus('current')
if mibBuilder.loadTexts: h3cLvTable.setDescription('This table describes the logic resource information of a logic volume.')
h3cLvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"))
if mibBuilder.loadTexts: h3cLvEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLvEntry.setDescription('An entry containing management information applicable to a particular logic resource.')
h3cLvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 1), H3cLvIDType())
if mibBuilder.loadTexts: h3cLvIndex.setStatus('current')
if mibBuilder.loadTexts: h3cLvIndex.setDescription('This object describes the symbol of a logic volume.')
h3cLvName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvName.setStatus('current')
if mibBuilder.loadTexts: h3cLvName.setDescription('This object identifies the name of a logic volume.')
h3cLvTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 3), Integer32()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvTotalSize.setStatus('current')
if mibBuilder.loadTexts: h3cLvTotalSize.setDescription('This object describes the total size of a logic volume. The units is million bytes.')
h3cLvCreateRaidUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 4), H3cRaidIDType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvCreateRaidUuid.setStatus('current')
if mibBuilder.loadTexts: h3cLvCreateRaidUuid.setDescription('This object describes the ID of array where a logic volume build on.')
h3cLvCreateRaidSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 5), Integer32()).setUnits('MB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvCreateRaidSize.setStatus('current')
if mibBuilder.loadTexts: h3cLvCreateRaidSize.setDescription('This object describes the size of a logic volume when create it. The units is million bytes.')
h3cLvSedInquiryStringKeep = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvSedInquiryStringKeep.setStatus('current')
if mibBuilder.loadTexts: h3cLvSedInquiryStringKeep.setDescription("This object identifies if the inquiry string of the logic volume should be reserved. This value of this object is valid only when the associated h3cLvType is equal to 'serviceEnabled'.")
h3cLvSedRaidUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 7), H3cRaidIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvSedRaidUuid.setStatus('current')
if mibBuilder.loadTexts: h3cLvSedRaidUuid.setDescription('This object describes the location where the SED infomation is build on.')
h3cLvState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("usable", 1), ("unusable", 2), ("conflict", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvState.setStatus('current')
if mibBuilder.loadTexts: h3cLvState.setDescription("This object identifies the state of a logic volume. The value 'conflict' means the names of two or more logic volume are reduplicate.")
h3cLvAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("use", 1), ("unused", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvAssigned.setStatus('current')
if mibBuilder.loadTexts: h3cLvAssigned.setDescription('This object identifies if the logic volume has be designated for target or SAN client.')
h3cLvType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("virtual", 1), ("direct", 2), ("serviceEnabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvType.setStatus('current')
if mibBuilder.loadTexts: h3cLvType.setDescription("This object describes the type of a logic volume. The value 'virtual' means virtual devices are defined as sets of storage blocks from one or more physical array. This allows the creation of virtual devices that can be a portion of a larger physical array, or an aggregation of multiple physical array. The value 'direct' means direct devices are directly mapped SCSI devices. Because they are not virtualized, direct devices cannot take advantage of advanced storage options, such as mirroring, failover, replication, or snapshot copy. The value 'serviceEnabled' means service enabled devices are all maintained in a one-to-one mapping relationship(one physical array equals one logical device).")
h3cLvExtendTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvExtendTimes.setStatus('current')
if mibBuilder.loadTexts: h3cLvExtendTimes.setDescription('This object describes the times the logic volume has been extended.')
h3cLvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLvRowStatus.setDescription('This object describes the actions to create or delete a logic volume.')
h3cLvExtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3), )
if mibBuilder.loadTexts: h3cLvExtTable.setStatus('current')
if mibBuilder.loadTexts: h3cLvExtTable.setDescription('This table contains the extend resource information of the logic volume.')
h3cLvExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvRaidUuid"))
if mibBuilder.loadTexts: h3cLvExtEntry.setStatus('current')
if mibBuilder.loadTexts: h3cLvExtEntry.setDescription('An entry containing management information applicable to extend resource of logic volume.')
h3cLvRaidUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 1), H3cRaidIDType())
if mibBuilder.loadTexts: h3cLvRaidUuid.setStatus('current')
if mibBuilder.loadTexts: h3cLvRaidUuid.setDescription('This index is identical to h3cRaidUuid in H3C-RAID-MIB.')
h3cLvExtSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('MB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvExtSize.setStatus('current')
if mibBuilder.loadTexts: h3cLvExtSize.setDescription('This object describes the extend size of the logic volume in a specific raid. The units is million bytes. This object will always return zero when read.')
h3cLvRaidSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 3), Integer32()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cLvRaidSize.setStatus('current')
if mibBuilder.loadTexts: h3cLvRaidSize.setDescription('This object describes the size of logic volume on the specific raid. The units is million bytes.')
h3cLvExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cLvExtRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cLvExtRowStatus.setDescription('This object describes the action to extend the logic volume.')
h3cTargetResource = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4))
h3cTargetCreateIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTargetCreateIndex.setStatus('current')
if mibBuilder.loadTexts: h3cTargetCreateIndex.setDescription('This object supplys an valid index which uses to create a new entry for the h3cTargetTable object. Note that if an entry of the associated table has been created or deleted, the historical value of this object may be an invalid index to create a new entry for the associated table.')
h3cTargetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2), )
if mibBuilder.loadTexts: h3cTargetTable.setStatus('current')
if mibBuilder.loadTexts: h3cTargetTable.setDescription('This table describes some information when creating a target.')
h3cTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"))
if mibBuilder.loadTexts: h3cTargetEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTargetEntry.setDescription('An entry containing management information applicable to a target when create it.')
h3cTargetId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cTargetId.setStatus('current')
if mibBuilder.loadTexts: h3cTargetId.setDescription('This object identifies the ID of a target.')
h3cTargetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 223))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTargetName.setStatus('current')
if mibBuilder.loadTexts: h3cTargetName.setDescription('This object describes the name of a target.')
h3cTargetMinLun = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTargetMinLun.setStatus('current')
if mibBuilder.loadTexts: h3cTargetMinLun.setDescription('This object describes the mini LUN(logical unit number) number of a target.')
h3cTargetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTargetRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cTargetRowStatus.setDescription('This object describes the actions to add or delete the target.')
h3cTargetAddressTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5), )
if mibBuilder.loadTexts: h3cTargetAddressTable.setStatus('current')
if mibBuilder.loadTexts: h3cTargetAddressTable.setDescription('This table described some address information of a target.')
h3cTargetAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetIpAddrType"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetIpAddress"))
if mibBuilder.loadTexts: h3cTargetAddressEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTargetAddressEntry.setDescription('An entry containing management information applicable to the address of a target.')
h3cTargetIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 1), InetAddress())
if mibBuilder.loadTexts: h3cTargetIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cTargetIpAddress.setDescription('This object describes the IP address of a target.')
h3cTargetIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 2), InetAddressType())
if mibBuilder.loadTexts: h3cTargetIpAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cTargetIpAddrType.setDescription('This object describes the type of IP address.')
h3cTargetIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTargetIpRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cTargetIpRowStatus.setDescription('This object describes the actions to add or delete a IP address of a target.')
h3cTargetLvAssignTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6), )
if mibBuilder.loadTexts: h3cTargetLvAssignTable.setStatus('current')
if mibBuilder.loadTexts: h3cTargetLvAssignTable.setDescription('This table describes logic resource information of a target.')
h3cTargetLvAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"))
if mibBuilder.loadTexts: h3cTargetLvAssignEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTargetLvAssignEntry.setDescription('An entry containing management information applicable to the logic resource of a target.')
h3cTargetLvLun = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTargetLvLun.setStatus('current')
if mibBuilder.loadTexts: h3cTargetLvLun.setDescription('This object identifies the init LUN number of a target.')
h3cTargetLvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTargetLvRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cTargetLvRowStatus.setDescription('This object describes the actions to add or delete the logic resource of a target.')
h3cInitiatorResource = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7))
h3cInitiatorCreateIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cInitiatorCreateIndex.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorCreateIndex.setDescription('This object supplys an valid index which uses to create a new entry for the h3cInitiatorTable object. Note that if an entry of the associated table has been created or deleted, the historical value of this object may be an invalid index to create a new entry for the associated table.')
h3cInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2), )
if mibBuilder.loadTexts: h3cInitiatorTable.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorTable.setDescription('This table describes the creation information of initiators.')
h3cInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cInitiatorId"))
if mibBuilder.loadTexts: h3cInitiatorEntry.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorEntry.setDescription('An entry containing management information applicable to the creation of initiator.')
h3cInitiatorId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cInitiatorId.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorId.setDescription('This object identifies the ID of the initiator.')
h3cInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 223))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cInitiatorName.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorName.setDescription('This object describes the name of the initiator.')
h3cInitiatorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cInitiatorRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cInitiatorRowStatus.setDescription('This object describes the actions to add or delete initiators.')
h3cTargetInitiatorAssociateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8), )
if mibBuilder.loadTexts: h3cTargetInitiatorAssociateTable.setStatus('current')
if mibBuilder.loadTexts: h3cTargetInitiatorAssociateTable.setDescription('This table describes the associate information between the target and initiator.')
h3cTargetInitiatorAssociateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cInitiatorId"))
if mibBuilder.loadTexts: h3cTargetInitiatorAssociateEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTargetInitiatorAssociateEntry.setDescription('An entry containing management information applicable to association between the target and initiator.')
h3cTIAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("nonexclusive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTIAccessMode.setStatus('current')
if mibBuilder.loadTexts: h3cTIAccessMode.setDescription("This object identifies the mode of accessing between the target and initiator. The value 'read' means read available. The value 'write' means read/write available, and write available only for one association. The value 'nonexclusive' means read/write available for multi-association.")
h3cTIChap = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 2), H3cStorageEnableState().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTIChap.setStatus('current')
if mibBuilder.loadTexts: h3cTIChap.setDescription('This object identifies the state of the chap attestation.')
h3cTIUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTIUserName.setStatus('current')
if mibBuilder.loadTexts: h3cTIUserName.setDescription('This object identifies the user name for the chap attestation.')
h3cTIPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTIPassword.setStatus('current')
if mibBuilder.loadTexts: h3cTIPassword.setDescription('This object identifies the password for the chap attestation. It is proclaimed and can be modified.')
h3cTIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTIRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cTIRowStatus.setDescription('This object describes the actions to add or delete the association.')
h3cTISessionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9), )
if mibBuilder.loadTexts: h3cTISessionTable.setStatus('current')
if mibBuilder.loadTexts: h3cTISessionTable.setDescription('This table described the information of the sessions.')
h3cTISessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cTISessionId"))
if mibBuilder.loadTexts: h3cTISessionEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTISessionEntry.setDescription('An entry containing management information applicable to the sessions.')
h3cTISessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 1), H3cSessionIDType())
if mibBuilder.loadTexts: h3cTISessionId.setStatus('current')
if mibBuilder.loadTexts: h3cTISessionId.setDescription('This object identifies the ID of a session.')
h3cTISessionConnectionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTISessionConnectionCount.setStatus('current')
if mibBuilder.loadTexts: h3cTISessionConnectionCount.setDescription('This object describes the number of connections between the targets and initiators.')
h3cTISessionInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTISessionInitiatorName.setStatus('current')
if mibBuilder.loadTexts: h3cTISessionInitiatorName.setDescription("This object identifies the initiator's name of a session.")
h3cSanClientResource = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10))
h3cSanClientCreateIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSanClientCreateIndex.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientCreateIndex.setDescription('This object supplys an valid index which uses to create a new entry for the h3cSanClientTable object. Note that if an entry of the associated table has been created or deleted, the historical value of this object may be an invalid index to create a new entry for the associated table.')
h3cSanClientTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2), )
if mibBuilder.loadTexts: h3cSanClientTable.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientTable.setDescription('This table described the information of SAN(Storage Area Network) clients.')
h3cSanClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"))
if mibBuilder.loadTexts: h3cSanClientEntry.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientEntry.setDescription('An entry containing management information applicable to the SAN clients.')
h3cSanClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSanClientId.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientId.setDescription('This object identifies the index of a SAN client.')
h3cSanClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSanClientName.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientName.setDescription('This object identifies the name of a SAN client.')
h3cSanClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("iscsi", 1), ("fc", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSanClientType.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientType.setDescription('This object identifies the type of a SAN client.')
h3cFcInitiatorWwpnList = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 4), H3cWwpnListType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFcInitiatorWwpnList.setStatus('current')
if mibBuilder.loadTexts: h3cFcInitiatorWwpnList.setDescription("This object identifies the name list of FC Initiator WWPN(World Wide Port Name). The value of this object is invalid and should be ignored when the value of associated h3cSanClientType object is not equal to 'fc'.")
h3cFcAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("nonexclusive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFcAccessMode.setStatus('current')
if mibBuilder.loadTexts: h3cFcAccessMode.setDescription("This object identifies the mode of access. The value of this object is invalid and should be ignored when the value of associated h3cSanClientType object is not equal to 'fc'. The value 'read' means read available. The value 'write' means read/write available, and write available only for one association. The value 'nonexclusive' means read/write available for multi-association.")
h3cSanClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSanClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cSanClientRowStatus.setDescription('This object describes the action to create or delete a SAN client.')
h3cFcLogicResourceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11), )
if mibBuilder.loadTexts: h3cFcLogicResourceTable.setStatus('current')
if mibBuilder.loadTexts: h3cFcLogicResourceTable.setDescription('This table describes logic resource information of a FC.')
h3cFcLogicResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1), ).setIndexNames((0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"), (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"))
if mibBuilder.loadTexts: h3cFcLogicResourceEntry.setStatus('current')
if mibBuilder.loadTexts: h3cFcLogicResourceEntry.setDescription('An entry containing management information applicable to the logic resource of a FC.')
h3cFcLvLun = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcLvLun.setStatus('current')
if mibBuilder.loadTexts: h3cFcLvLun.setDescription('This object identifies the init LUN number of a FC.')
h3cFcTargetWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 2), H3cWwpnListType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFcTargetWwpnName.setStatus('current')
if mibBuilder.loadTexts: h3cFcTargetWwpnName.setDescription('This object identifies the name list of FC Target WWPN(World Wide Port Name). ')
h3cFcInitiatorWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 3), H3cWwpnListType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFcInitiatorWwpnName.setStatus('current')
if mibBuilder.loadTexts: h3cFcInitiatorWwpnName.setDescription('This object identifies the name list of FC Initiator WWPN(World Wide Port Name). ')
h3cFcLvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFcLvRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cFcLvRowStatus.setDescription('This object describes the actions to add or delete the logic resource of a FC.')
mibBuilder.exportSymbols("H3C-LOGIC-VOLUME-MIB", h3cTargetLvRowStatus=h3cTargetLvRowStatus, h3cLvIndex=h3cLvIndex, h3cTISessionTable=h3cTISessionTable, h3cLvMibObjects=h3cLvMibObjects, h3cTargetEntry=h3cTargetEntry, h3cTargetLvAssignEntry=h3cTargetLvAssignEntry, h3cFcLvRowStatus=h3cFcLvRowStatus, h3cTIChap=h3cTIChap, h3cLvExtSize=h3cLvExtSize, h3cTargetResource=h3cTargetResource, h3cTargetAddressEntry=h3cTargetAddressEntry, h3cLvType=h3cLvType, h3cTISessionConnectionCount=h3cTISessionConnectionCount, PYSNMP_MODULE_ID=h3cLogicVolume, h3cTISessionInitiatorName=h3cTISessionInitiatorName, h3cFcLogicResourceTable=h3cFcLogicResourceTable, h3cTargetTable=h3cTargetTable, h3cInitiatorRowStatus=h3cInitiatorRowStatus, h3cInitiatorTable=h3cInitiatorTable, h3cSanClientEntry=h3cSanClientEntry, h3cLvTotalSize=h3cLvTotalSize, h3cTIRowStatus=h3cTIRowStatus, h3cSanClientName=h3cSanClientName, h3cInitiatorCreateIndex=h3cInitiatorCreateIndex, h3cTargetIpRowStatus=h3cTargetIpRowStatus, h3cTIPassword=h3cTIPassword, h3cTargetIpAddress=h3cTargetIpAddress, h3cLvRowStatus=h3cLvRowStatus, h3cTIAccessMode=h3cTIAccessMode, h3cTISessionEntry=h3cTISessionEntry, h3cSanClientResource=h3cSanClientResource, h3cTargetAddressTable=h3cTargetAddressTable, h3cFcAccessMode=h3cFcAccessMode, h3cLvName=h3cLvName, h3cTargetId=h3cTargetId, h3cInitiatorName=h3cInitiatorName, h3cInitiatorEntry=h3cInitiatorEntry, h3cInitiatorResource=h3cInitiatorResource, h3cTargetInitiatorAssociateEntry=h3cTargetInitiatorAssociateEntry, h3cLvCreateIndex=h3cLvCreateIndex, h3cLvExtRowStatus=h3cLvExtRowStatus, h3cTargetLvLun=h3cTargetLvLun, h3cTargetMinLun=h3cTargetMinLun, h3cSanClientRowStatus=h3cSanClientRowStatus, h3cSanClientCount=h3cSanClientCount, h3cTIUserName=h3cTIUserName, h3cFcLogicResourceEntry=h3cFcLogicResourceEntry, h3cTISessionId=h3cTISessionId, h3cLogicResourceCapacityObject=h3cLogicResourceCapacityObject, h3cInitiatorId=h3cInitiatorId, h3cLogicVolume=h3cLogicVolume, h3cLogicVolumeResource=h3cLogicVolumeResource, h3cLvState=h3cLvState, h3cLvEntry=h3cLvEntry, h3cLvExtendTimes=h3cLvExtendTimes, h3cTargetInitiatorAssociateTable=h3cTargetInitiatorAssociateTable, h3cLvSedRaidUuid=h3cLvSedRaidUuid, h3cInitiatorCount=h3cInitiatorCount, h3cLvExtEntry=h3cLvExtEntry, h3cLvCount=h3cLvCount, h3cSanClientId=h3cSanClientId, h3cFcTargetWwpnName=h3cFcTargetWwpnName, h3cSanClientType=h3cSanClientType, h3cLvCreateRaidUuid=h3cLvCreateRaidUuid, h3cFcInitiatorWwpnList=h3cFcInitiatorWwpnList, h3cLvCreateRaidSize=h3cLvCreateRaidSize, h3cLvSedInquiryStringKeep=h3cLvSedInquiryStringKeep, h3cLvRaidSize=h3cLvRaidSize, h3cTargetRowStatus=h3cTargetRowStatus, h3cTargetLvAssignTable=h3cTargetLvAssignTable, h3cFcLvLun=h3cFcLvLun, h3cLvMaxSize=h3cLvMaxSize, h3cLvAssigned=h3cLvAssigned, h3cTargetCount=h3cTargetCount, h3cLvExtTable=h3cLvExtTable, h3cLvRaidUuid=h3cLvRaidUuid, h3cLvTable=h3cLvTable, h3cTargetName=h3cTargetName, h3cSanClientCreateIndex=h3cSanClientCreateIndex, h3cTargetCreateIndex=h3cTargetCreateIndex, h3cSanClientTable=h3cSanClientTable, h3cFcInitiatorWwpnName=h3cFcInitiatorWwpnName, h3cTargetIpAddrType=h3cTargetIpAddrType)
