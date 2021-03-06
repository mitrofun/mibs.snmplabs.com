#
# PySNMP MIB module HUAWEI-SMARTLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SMARTLINK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Counter32, NotificationType, Integer32, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "NotificationType", "Integer32", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "iso", "Gauge32")
TextualConvention, DateAndTime, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "RowStatus", "DisplayString")
hwSmartLinkMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5))
if mibBuilder.loadTexts: hwSmartLinkMib.setLastUpdated('200803111355Z')
if mibBuilder.loadTexts: hwSmartLinkMib.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwSmartLinkMib.setContactInfo('CX Team Huawei Technologies Co.,Ltd. Shouchuang Bld.,NO.8 Dongbeiwang West Rd., Zhongguancun Software Park, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100094')
if mibBuilder.loadTexts: hwSmartLinkMib.setDescription('This module includes the information about smart link. The information can be read and some of them can be set.')
hwL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42))
hwSmartLinkMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1))
hwSmartLinkRevFlushTotal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkRevFlushTotal.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevFlushTotal.setDescription('The total of received flush packets.')
hwSmartLinkRevLastFlushIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushIfIndex.setDescription('The interface index of port which received flush packet lastly.')
hwSmartLinkRevLastFlushTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 3), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushTime.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushTime.setDescription('The time when received flush packet lastly. field octets contents range ----- ------ -------- ----- 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9')
hwSmartLinkRevLastFlushSourceMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushSourceMacAddr.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushSourceMacAddr.setDescription('The SMAC of flush packet which arrived this device lastly.')
hwSmartLinkRevLastFlushVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 5), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushVlan.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevLastFlushVlan.setDescription('The control VLAN of flush packet which arrived this device lastly.')
hwSmartLinkResetFlushStatistics = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("unused", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSmartLinkResetFlushStatistics.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkResetFlushStatistics.setDescription('Reset the statistics of flush packets.')
hwSmartLinkRevPortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7), )
if mibBuilder.loadTexts: hwSmartLinkRevPortCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevPortCfgTable.setDescription('This is port configuration table which received flush packet, and configuration relation of port received flush packet was described. The index of table is hwSmartLinkRpcIfIndex.')
hwSmartLinkRevPortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcIfIndex"))
if mibBuilder.loadTexts: hwSmartLinkRevPortCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevPortCfgEntry.setDescription('The table includes the information of the received flush packet port configuration information. The index of the table is hwSmartLinkRpcIfIndex.')
hwSmartLinkRpcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwSmartLinkRpcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRpcIfIndex.setDescription('The index of port from which received flush packets.')
hwSmartLinkRpcRevVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 2), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSmartLinkRpcRevVlan.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRpcRevVlan.setDescription('Set the VLAN ID to verify the validity of flush packets received. Ranging from 1 to 4094.')
hwSmartLinkRpcRevPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSmartLinkRpcRevPassword.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRpcRevPassword.setDescription('Set the password to verify the validity of flush packets received.')
hwSmartLinkGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8), )
if mibBuilder.loadTexts: hwSmartLinkGroupCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupCfgTable.setDescription('The table includes the information of the smart link group configuration information, and include the mode of smart link group, working status of group, control vlan of group etc.')
hwSmartLinkGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupId"))
if mibBuilder.loadTexts: hwSmartLinkGroupCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupCfgEntry.setDescription('The table includes the information of the smart link group configuration information. The index of the table is hwSmartLinkGcGroupId.')
hwSmartLinkGcGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSmartLinkGcGroupId.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcGroupId.setDescription('Smart link group index.')
hwSmartLinkGcMasterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkGcMasterIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcMasterIfIndex.setDescription('The master interface index of smart link group.')
hwSmartLinkGcSlaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkGcSlaveIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcSlaveIfIndex.setDescription('The slave interface index of smart link group.')
hwSmartLinkGcGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("master", 2), ("slave", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkGcGroupStatus.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcGroupStatus.setDescription('Working status of smart link group, include none, master and slave. none: all ports in group are inactive. Master: master port is active, and slave port is inactive. Slave: master port is inactive, and slave port is active.')
hwSmartLinkGcEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 5), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcEnable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcEnable.setDescription('Startup or close the smart link group. Before startup the smart link group, the group must be created.')
hwSmartLinkGcSendControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 6), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcSendControlVlan.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcSendControlVlan.setDescription('Set the tag of flush packets which send from this smart link group.')
hwSmartLinkGcSendPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcSendPassword.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcSendPassword.setDescription('Set password of flush packets which send from this smart link group.')
hwSmartLinkGcLock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 8), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcLock.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcLock.setDescription('Active port was locked on master port')
hwSmartLinkGcForce = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 9), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcForce.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcForce.setDescription('Active port was locked on slave port.')
hwSmartLinkGcRevertWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 1200)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcRevertWtrTime.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcRevertWtrTime.setDescription('Set wait-to-restore time.')
hwSmartLinkGcRevertEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 11), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcRevertEnable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcRevertEnable.setDescription('When wait-to-restore timer is over, the smart link group link will be switched.')
hwSmartLinkGcManual = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switch", 1), ("unused", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcManual.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcManual.setDescription('The link was switched every setting manual command.')
hwSmartLinkGcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 8, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkGcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGcRowStatus.setDescription('Status of smart link group row.')
hwSmartLinkPortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9), )
if mibBuilder.loadTexts: hwSmartLinkPortCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPortCfgTable.setDescription('This table is the configuration table of member port of smart link group. This table described that configuration relation of member port of smart link group. This table index is hwSmartLinkPcGroupId and hwSmartLinkPcPortType.')
hwSmartLinkPortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcGroupId"), (0, "HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcPortType"))
if mibBuilder.loadTexts: hwSmartLinkPortCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPortCfgEntry.setDescription('This table described that configuration relation of member port of smart link group. This table index is hwSmartLinkPcGroupId and hwSmartLinkPcPortType.')
hwSmartLinkPcGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSmartLinkPcGroupId.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcGroupId.setDescription('Smart link group index.')
hwSmartLinkPcPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))))
if mibBuilder.loadTexts: hwSmartLinkPcPortType.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcPortType.setDescription('The role of smart link group member port.')
hwSmartLinkPcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkPcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcIfIndex.setDescription('Interface index of member port of smart link group.')
hwSmartLinkPcPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkPcPortStatus.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcPortStatus.setDescription('The status of member port, include unknown, active and inactive.')
hwSmartLinkPcSendFlushNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkPcSendFlushNum.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcSendFlushNum.setDescription('The total of flush packets send from this port.')
hwSmartLinkPcSendFlushTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmartLinkPcSendFlushTime.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcSendFlushTime.setDescription('The time when send flush packet lastly. field octets contents range ----- ------ -------- ----- 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9')
hwSmartLinkPcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 9, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmartLinkPcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPcRowStatus.setDescription('Status of monitor link group row.')
hwMonitorLinkGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10), )
if mibBuilder.loadTexts: hwMonitorLinkGroupCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGroupCfgTable.setDescription('This is status information table of monitor link group, and index is hwMonitorLinkGcGroupId.')
hwMonitorLinkGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcGroupId"))
if mibBuilder.loadTexts: hwMonitorLinkGroupCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGroupCfgEntry.setDescription('This is status information table of monitor link group, and index is hwMonitorLinkGcGroupId.')
hwMonitorLinkGcGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwMonitorLinkGcGroupId.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGcGroupId.setDescription('Monitor link group index.')
hwMonitorLinkGcRecoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 60)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkGcRecoverTime.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGcRecoverTime.setDescription('Set recover time, when uplink port turn to UP and over the recover time, all downlink port will be undo shutdown.')
hwMonitorLinkGcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 10, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkGcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGcRowStatus.setDescription('Status of monitor link group row.')
hwMonitorLinkUpLinkPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11), )
if mibBuilder.loadTexts: hwMonitorLinkUpLinkPortTable.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUpLinkPortTable.setDescription('This is the information table of member port in monitor link group upink, The table indexes are hwMonitorLinkUlGroupId, hwMonitorLinkUlPortType.')
hwMonitorLinkUpLinkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlGroupId"), (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortType"))
if mibBuilder.loadTexts: hwMonitorLinkUpLinkPortEntry.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUpLinkPortEntry.setDescription('This is the information table of member port in monitor link group upink, The table indexes are hwMonitorLinkUlGroupId and hwMonitorLinkUlPortType.')
hwMonitorLinkUlGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwMonitorLinkUlGroupId.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlGroupId.setDescription('Monitor link group index.')
hwMonitorLinkUlPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("smartLink", 1), ("switchPort", 2))))
if mibBuilder.loadTexts: hwMonitorLinkUlPortType.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlPortType.setDescription('Type of uplink port in monitor link group, include smart link group and switch port.')
hwMonitorLinkUlPortValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkUlPortValue.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlPortValue.setDescription('When port type is smart link, the value is smart link group index. When port type is switch port, the value is ifindex of switch port.')
hwMonitorLinkUlPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkUlPortStatus.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlPortStatus.setDescription('State of member port in monitor group, include UP and DOWN.')
hwMonitorLinkUlPortUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 5), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkUlPortUpTime.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlPortUpTime.setDescription('Show the time when the port state turn to UP recently.')
hwMonitorLinkUlPortDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkUlPortDownTime.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlPortDownTime.setDescription('Show the time when the port state turn to DOWN recently.')
hwMonitorLinkUlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 11, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkUlRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUlRowStatus.setDescription('Status of monitor link group row.')
hwMonitorLinkDownLinkPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12), )
if mibBuilder.loadTexts: hwMonitorLinkDownLinkPortTable.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDownLinkPortTable.setDescription('This is the information table of member port in monitor link group downlink, The table indexes are hwMonitorLinkDlGroupId and hwMonitorLinkDlArrayIndex.')
hwMonitorLinkDownLinkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1), ).setIndexNames((0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlGroupId"), (0, "HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlArrayIndex"))
if mibBuilder.loadTexts: hwMonitorLinkDownLinkPortEntry.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDownLinkPortEntry.setDescription('This is the information table of member port in monitor link group downlink, The table indexes are hwMonitorLinkDlGroupId and hwMonitorLinkDlArrayIndex.')
hwMonitorLinkDlGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwMonitorLinkDlGroupId.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlGroupId.setDescription('Monitor link group index.')
hwMonitorLinkDlArrayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwMonitorLinkDlArrayIndex.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlArrayIndex.setDescription('The downlink array index of Monitor link group.')
hwMonitorLinkDlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkDlIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlIfIndex.setDescription('Member interface index of monitor link group downlink.')
hwMonitorLinkDlPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkDlPortStatus.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlPortStatus.setDescription('State of member port in monitor group, include UP and DOWN.')
hwMonitorLinkDlPortUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 5), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkDlPortUpTime.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlPortUpTime.setDescription('Show the time when the port state turn to UP recently.')
hwMonitorLinkDlPortDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMonitorLinkDlPortDownTime.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlPortDownTime.setDescription('Show the time when the port state turn to DOWN recently.')
hwMonitorLinkDlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 1, 12, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMonitorLinkDlRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDlRowStatus.setDescription('Status of monitor link group row.')
hwSmartLinkMibTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2))
if mibBuilder.loadTexts: hwSmartLinkMibTraps.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkMibTraps.setDescription('Definition point for smart link group notifications.')
hwSmartLinkLinkSwitch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 1)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"))
if mibBuilder.loadTexts: hwSmartLinkLinkSwitch.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkLinkSwitch.setDescription('The SNMP trap that is generated when smart link group link status switches.')
hwSmartLinkInactiveLinkFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 2)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex"))
if mibBuilder.loadTexts: hwSmartLinkInactiveLinkFail.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkInactiveLinkFail.setDescription('The SNMP trap that is generated when detect the link change to abnormal status.')
hwSmartLinkInactiveLinkResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 3)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex"))
if mibBuilder.loadTexts: hwSmartLinkInactiveLinkResume.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkInactiveLinkResume.setDescription('The SNMP trap that is generated when detect the link change to normal status from abnormal status.')
hwSmartLinkGroupEnable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 4)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable"))
if mibBuilder.loadTexts: hwSmartLinkGroupEnable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupEnable.setDescription('The SNMP trap that is generated when smart link group was enabled.')
hwSmartLinkGroupDisable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 5)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable"))
if mibBuilder.loadTexts: hwSmartLinkGroupDisable.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupDisable.setDescription('The SNMP trap that is generated when smart link group was disabled.')
hwSmartLinkLinkSwitchToMaster = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 6)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"))
if mibBuilder.loadTexts: hwSmartLinkLinkSwitchToMaster.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkLinkSwitchToMaster.setDescription('The SNMP trap that is generated when detect the link change to master from slave.')
hwSmartLinkLinkSwitchToSlave = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 7)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"))
if mibBuilder.loadTexts: hwSmartLinkLinkSwitchToSlave.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkLinkSwitchToSlave.setDescription('The SNMP trap that is generated when detect the link change to slave from master.')
hwSmartLinkGroupUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 8)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"))
if mibBuilder.loadTexts: hwSmartLinkGroupUp.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupUp.setDescription('The SNMP trap that is generated when detect the group turn to up.')
hwSmartLinkGroupDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 2, 9)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"))
if mibBuilder.loadTexts: hwSmartLinkGroupDown.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupDown.setDescription('The SNMP trap that is generated when detect the group turn to down.')
hwSmartLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3))
hwSmartLinkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1))
hwSmartLinkInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 1)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevFlushTotal"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushIfIndex"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushTime"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushSourceMacAddr"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRevLastFlushVlan"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkResetFlushStatistics"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmartLinkInfoGroup = hwSmartLinkInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkInfoGroup.setDescription('A collection of objects providing smart link information.')
hwSmartLinkRevPortCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 2)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcRevVlan"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkRpcRevPassword"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmartLinkRevPortCfgGroup = hwSmartLinkRevPortCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkRevPortCfgGroup.setDescription('A collection of objects providing port configuration which received flush packet.')
hwSmartLinkGroupCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 3)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcMasterIfIndex"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSlaveIfIndex"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcGroupStatus"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcEnable"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSendControlVlan"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcSendPassword"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcLock"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcForce"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRevertWtrTime"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRevertEnable"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcManual"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmartLinkGroupCfgGroup = hwSmartLinkGroupCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkGroupCfgGroup.setDescription('A collection of objects providing smart link group status information.')
hwSmartLinkPortCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 4)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcIfIndex"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcPortStatus"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcSendFlushNum"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcSendFlushTime"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkPcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmartLinkPortCfgGroup = hwSmartLinkPortCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkPortCfgGroup.setDescription('A collection of objects providing smart link port configuration.')
hwMonitorLinkGroupCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 5)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcRecoverTime"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkGcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMonitorLinkGroupCfgGroup = hwMonitorLinkGroupCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkGroupCfgGroup.setDescription('A collection of objects provding monitor link group information. ')
hwMonitorLinkUpLinkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 6)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortValue"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortStatus"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortUpTime"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlPortDownTime"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkUlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMonitorLinkUpLinkPortGroup = hwMonitorLinkUpLinkPortGroup.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkUpLinkPortGroup.setDescription('A collection of objects providing monitor link group uplink port configuration.')
hwMonitorLinkDownLinkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 1, 7)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlIfIndex"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortStatus"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortUpTime"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlPortDownTime"), ("HUAWEI-SMARTLINK-MIB", "hwMonitorLinkDlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMonitorLinkDownLinkPortGroup = hwMonitorLinkDownLinkPortGroup.setStatus('current')
if mibBuilder.loadTexts: hwMonitorLinkDownLinkPortGroup.setDescription('A collection of objects providing monitor link group downlink port configuration.')
hwSmartLinkTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 2))
hwSmartLinkTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 2, 1)).setObjects(("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitch"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkInactiveLinkFail"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkInactiveLinkResume"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupEnable"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupDisable"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitchToMaster"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkLinkSwitchToSlave"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupUp"), ("HUAWEI-SMARTLINK-MIB", "hwSmartLinkGroupDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmartLinkTrapsGroup = hwSmartLinkTrapsGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmartLinkTrapsGroup.setDescription('The Group of smart link Trap.')
hwSmartLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 5, 3, 3))
mibBuilder.exportSymbols("HUAWEI-SMARTLINK-MIB", hwSmartLinkGroupUp=hwSmartLinkGroupUp, hwSmartLinkPcGroupId=hwSmartLinkPcGroupId, hwSmartLinkGcLock=hwSmartLinkGcLock, hwMonitorLinkUpLinkPortTable=hwMonitorLinkUpLinkPortTable, hwSmartLinkGcSendControlVlan=hwSmartLinkGcSendControlVlan, hwMonitorLinkDlPortStatus=hwMonitorLinkDlPortStatus, hwSmartLinkRpcRevPassword=hwSmartLinkRpcRevPassword, hwSmartLinkTrapGroups=hwSmartLinkTrapGroups, hwSmartLinkConformance=hwSmartLinkConformance, hwSmartLinkPcPortType=hwSmartLinkPcPortType, hwSmartLinkTrapsGroup=hwSmartLinkTrapsGroup, hwSmartLinkRpcIfIndex=hwSmartLinkRpcIfIndex, PYSNMP_MODULE_ID=hwSmartLinkMib, hwSmartLinkInfoGroup=hwSmartLinkInfoGroup, hwSmartLinkGcSlaveIfIndex=hwSmartLinkGcSlaveIfIndex, hwSmartLinkGroupCfgEntry=hwSmartLinkGroupCfgEntry, hwSmartLinkGcForce=hwSmartLinkGcForce, hwSmartLinkPortCfgEntry=hwSmartLinkPortCfgEntry, hwSmartLinkMib=hwSmartLinkMib, hwSmartLinkGroupCfgGroup=hwSmartLinkGroupCfgGroup, hwMonitorLinkGcGroupId=hwMonitorLinkGcGroupId, hwMonitorLinkGcRowStatus=hwMonitorLinkGcRowStatus, hwMonitorLinkUlPortDownTime=hwMonitorLinkUlPortDownTime, hwMonitorLinkUpLinkPortGroup=hwMonitorLinkUpLinkPortGroup, hwMonitorLinkUlPortType=hwMonitorLinkUlPortType, hwMonitorLinkUlPortValue=hwMonitorLinkUlPortValue, hwSmartLinkPcSendFlushTime=hwSmartLinkPcSendFlushTime, hwSmartLinkGcMasterIfIndex=hwSmartLinkGcMasterIfIndex, hwMonitorLinkDlPortDownTime=hwMonitorLinkDlPortDownTime, hwMonitorLinkUlPortUpTime=hwMonitorLinkUlPortUpTime, hwSmartLinkGcManual=hwSmartLinkGcManual, hwSmartLinkCompliances=hwSmartLinkCompliances, hwMonitorLinkUlRowStatus=hwMonitorLinkUlRowStatus, hwSmartLinkGcSendPassword=hwSmartLinkGcSendPassword, hwMonitorLinkDlGroupId=hwMonitorLinkDlGroupId, hwSmartLinkRevLastFlushIfIndex=hwSmartLinkRevLastFlushIfIndex, hwMonitorLinkDownLinkPortTable=hwMonitorLinkDownLinkPortTable, hwSmartLinkMibTraps=hwSmartLinkMibTraps, hwSmartLinkPortCfgGroup=hwSmartLinkPortCfgGroup, hwMonitorLinkUpLinkPortEntry=hwMonitorLinkUpLinkPortEntry, hwSmartLinkLinkSwitchToMaster=hwSmartLinkLinkSwitchToMaster, hwMonitorLinkUlPortStatus=hwMonitorLinkUlPortStatus, hwSmartLinkRevLastFlushVlan=hwSmartLinkRevLastFlushVlan, hwSmartLinkRevPortCfgEntry=hwSmartLinkRevPortCfgEntry, hwMonitorLinkGroupCfgEntry=hwMonitorLinkGroupCfgEntry, hwSmartLinkGcRevertWtrTime=hwSmartLinkGcRevertWtrTime, hwSmartLinkRpcRevVlan=hwSmartLinkRpcRevVlan, hwSmartLinkGcEnable=hwSmartLinkGcEnable, hwSmartLinkPcIfIndex=hwSmartLinkPcIfIndex, hwSmartLinkRevPortCfgGroup=hwSmartLinkRevPortCfgGroup, hwSmartLinkGroupEnable=hwSmartLinkGroupEnable, hwMonitorLinkGcRecoverTime=hwMonitorLinkGcRecoverTime, hwSmartLinkGcGroupStatus=hwSmartLinkGcGroupStatus, hwSmartLinkPcPortStatus=hwSmartLinkPcPortStatus, hwSmartLinkGroupDown=hwSmartLinkGroupDown, hwSmartLinkLinkSwitchToSlave=hwSmartLinkLinkSwitchToSlave, hwSmartLinkGroupCfgTable=hwSmartLinkGroupCfgTable, hwSmartLinkMibObjects=hwSmartLinkMibObjects, hwMonitorLinkDownLinkPortEntry=hwMonitorLinkDownLinkPortEntry, hwSmartLinkGcRowStatus=hwSmartLinkGcRowStatus, hwSmartLinkRevFlushTotal=hwSmartLinkRevFlushTotal, hwMonitorLinkDlPortUpTime=hwMonitorLinkDlPortUpTime, hwSmartLinkLinkSwitch=hwSmartLinkLinkSwitch, hwMonitorLinkUlGroupId=hwMonitorLinkUlGroupId, hwSmartLinkPortCfgTable=hwSmartLinkPortCfgTable, hwSmartLinkPcSendFlushNum=hwSmartLinkPcSendFlushNum, hwMonitorLinkDownLinkPortGroup=hwMonitorLinkDownLinkPortGroup, hwSmartLinkRevPortCfgTable=hwSmartLinkRevPortCfgTable, hwL2Mgmt=hwL2Mgmt, hwMonitorLinkGroupCfgTable=hwMonitorLinkGroupCfgTable, hwSmartLinkGroupDisable=hwSmartLinkGroupDisable, hwSmartLinkRevLastFlushSourceMacAddr=hwSmartLinkRevLastFlushSourceMacAddr, hwSmartLinkGcRevertEnable=hwSmartLinkGcRevertEnable, hwMonitorLinkDlRowStatus=hwMonitorLinkDlRowStatus, hwSmartLinkGroups=hwSmartLinkGroups, hwMonitorLinkDlArrayIndex=hwMonitorLinkDlArrayIndex, hwSmartLinkGcGroupId=hwSmartLinkGcGroupId, hwSmartLinkInactiveLinkResume=hwSmartLinkInactiveLinkResume, hwSmartLinkResetFlushStatistics=hwSmartLinkResetFlushStatistics, hwSmartLinkRevLastFlushTime=hwSmartLinkRevLastFlushTime, hwMonitorLinkDlIfIndex=hwMonitorLinkDlIfIndex, hwSmartLinkPcRowStatus=hwSmartLinkPcRowStatus, hwMonitorLinkGroupCfgGroup=hwMonitorLinkGroupCfgGroup, hwSmartLinkInactiveLinkFail=hwSmartLinkInactiveLinkFail)
