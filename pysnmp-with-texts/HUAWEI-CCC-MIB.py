#
# PySNMP MIB module HUAWEI-CCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-CCC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
HWL2VpnStateChangeReason, HWEnableValue, HWL2VpnVcEncapsType = mibBuilder.importSymbols("HUAWEI-VPLS-EXT-MIB", "HWL2VpnStateChangeReason", "HWEnableValue", "HWL2VpnVcEncapsType")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, NotificationType, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, Bits, TimeTicks, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "TimeTicks", "Integer32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwL2VpnCCC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3))
if mibBuilder.loadTexts: hwL2VpnCCC.setLastUpdated('200605110900Z')
if mibBuilder.loadTexts: hwL2VpnCCC.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwL2VpnCCC.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwL2VpnCCC.setDescription('The HUAWEI-CCC-MIB contains objects to manage KOMPELLA.')
hwL2Vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119))
hwCCCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1))
hwCCCVcTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1), )
if mibBuilder.loadTexts: hwCCCVcTable.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcTable.setDescription("This table is the CCC's configuration table. Users can create or delete the CCC by it.")
hwCCCVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1), ).setIndexNames((0, "HUAWEI-CCC-MIB", "hwCCCVcName"))
if mibBuilder.loadTexts: hwCCCVcEntry.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcEntry.setDescription('Provides the information of a CCC entry.')
hwCCCVcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: hwCCCVcName.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcName.setDescription('The human-readable name of this CCC.')
hwCCCVcConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcConnectionType.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcConnectionType.setDescription('This object indicates the VC connection type.')
hwCCCVcEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 3), HWL2VpnVcEncapsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcEncapType.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcEncapType.setDescription('This object indicates the service to be carried.')
hwCCCVcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcIfIndex.setDescription('This object indicates the AC ifIndex. 0 is invalid ifIndex.')
hwCCCVcInboundlabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcInboundlabel.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcInboundlabel.setDescription('This object indicates the static inbound label. This value need not be designated if the CCC is local.')
hwCCCVcOutboundlabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcOutboundlabel.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcOutboundlabel.setDescription('This object indicates the static outbound label. This value need not be designated if the CCC is local.')
hwCCCVcOutIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcOutIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcOutIfIndex.setDescription('This object indicates the ifIndex of the out interface in the side of PSN, or the ifIndex of the out interface in the side of AC if the CCC is local cross. 0 is invalid ifIndex.')
hwCCCVcNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcNextHop.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcNextHop.setDescription("This object indicates the next hop IP address of the out interface in the side of PSN. For the interface of ATM or FR or Ethernet, the next hop address must be used. Don't use the out interface in this case.")
hwCCCVcCtrlWord = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 9), HWEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcCtrlWord.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcCtrlWord.setDescription('This object indicates the control word capability. This value need not be designated if the CCC is local.')
hwCCCVcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcOperStatus.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcOperStatus.setDescription('This object indicates the operation status.')
hwCCCVcUpStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcUpStartTime.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcUpStartTime.setDescription('Specifies the time this VC status was Up(1).')
hwCCCVcUpSumTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcUpSumTime.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcUpSumTime.setDescription('Specifies the cumulate time this VC status has been Up(1).')
hwCCCVcMaxAtmCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcMaxAtmCells.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcMaxAtmCells.setDescription('Specifies the MaxAtmCells.')
hwCCCVcAtmPackOvertime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcAtmPackOvertime.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcAtmPackOvertime.setDescription('Specifies the AtmPackOvertime.')
hwCCCVcPwJitterBufferDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcPwJitterBufferDepth.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcPwJitterBufferDepth.setDescription('Specifies the PwJitterBufferDepth.')
hwCCCVcPwTdmEncapsulationNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcPwTdmEncapsulationNum.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcPwTdmEncapsulationNum.setDescription('Specifies the PwTdmEncapsulationNum.')
hwCCCVcPwIdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcPwIdleCode.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcPwIdleCode.setDescription('Specifies the PwIdleCode.')
hwCCCVcPwRtpHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcPwRtpHeader.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcPwRtpHeader.setDescription('Specifies the PwRtpHeader.')
hwCCCVcIpInterworking = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 19), HWEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcIpInterworking.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcIpInterworking.setDescription('This object indicates the enable sign of the IP interworking.')
hwCCCVcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCCCVcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcRowStatus.setDescription('RowStatus for this Table.')
hwCCCVcStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2), )
if mibBuilder.loadTexts: hwCCCVcStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsTable.setDescription("This table contains the CCC's VC packets statistics.")
hwCCCVcStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1), ).setIndexNames((0, "HUAWEI-CCC-MIB", "hwCCCVcName"), (0, "HUAWEI-CCC-MIB", "hwCCCVcStatisticsIfIndex"))
if mibBuilder.loadTexts: hwCCCVcStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsEntry.setDescription("Provides the information of the CCC's VC packets Statistics.")
hwCCCVcStatisticsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwCCCVcStatisticsIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsIfIndex.setDescription('This object indicates the AC ifIndex. The CCC will have two AC which need to be displayed if the CCC is local cross.')
hwCCCVcStatisticsRcvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcStatisticsRcvPkts.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsRcvPkts.setDescription('The total number of packets received on this VC.')
hwCCCVcStatisticsRcvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcStatisticsRcvBytes.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsRcvBytes.setDescription('The total number of bytes received on this VC.')
hwCCCVcStatisticsSndPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcStatisticsSndPkts.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsSndPkts.setDescription('The total number of packets sent on this VC.')
hwCCCVcStatisticsSndBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCCCVcStatisticsSndBytes.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsSndBytes.setDescription('The total number of bytes sent on the VC.')
hwCCCVcUpDownNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 3), HWEnableValue().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCCCVcUpDownNotifEnable.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcUpDownNotifEnable.setDescription('This object indicates the enable sign of CCC VC state change notification.')
hwCCCVcDeletedNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 4), HWEnableValue().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCCCVcDeletedNotifEnable.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcDeletedNotifEnable.setDescription('This object indicates the enable sign of CCC VC deletion notification.')
hwCCCVcStateChangeReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 1, 5), HWL2VpnStateChangeReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwCCCVcStateChangeReason.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStateChangeReason.setDescription('This object indicates the reason of CCC VC state change.')
hwCCCMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2))
hwCCCVcDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 1)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"), ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason"))
if mibBuilder.loadTexts: hwCCCVcDown.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcDown.setDescription("This notification indicates the VC's state changes to down.")
hwCCCVcUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 2)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"), ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason"))
if mibBuilder.loadTexts: hwCCCVcUp.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcUp.setDescription("This notification indicates the VC's state changes to up.")
hwCCCVcDeleted = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 2, 3)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"))
if mibBuilder.loadTexts: hwCCCVcDeleted.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcDeleted.setDescription('This notification indicates the VC is deleted.')
hwCCCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3))
hwCCCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 1))
hwCCCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 1, 1)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcGroup"), ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsGroup"), ("HUAWEI-CCC-MIB", "hwCCCNotificationControlGroup"), ("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReasonGroup"), ("HUAWEI-CCC-MIB", "hwCCCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCMIBCompliance = hwCCCMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwCCCMIBCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-KOMPELLA-MIB.')
hwCCCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2))
hwCCCVcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 1)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcConnectionType"), ("HUAWEI-CCC-MIB", "hwCCCVcEncapType"), ("HUAWEI-CCC-MIB", "hwCCCVcIfIndex"), ("HUAWEI-CCC-MIB", "hwCCCVcInboundlabel"), ("HUAWEI-CCC-MIB", "hwCCCVcOutboundlabel"), ("HUAWEI-CCC-MIB", "hwCCCVcOutIfIndex"), ("HUAWEI-CCC-MIB", "hwCCCVcNextHop"), ("HUAWEI-CCC-MIB", "hwCCCVcCtrlWord"), ("HUAWEI-CCC-MIB", "hwCCCVcOperStatus"), ("HUAWEI-CCC-MIB", "hwCCCVcUpStartTime"), ("HUAWEI-CCC-MIB", "hwCCCVcUpSumTime"), ("HUAWEI-CCC-MIB", "hwCCCVcMaxAtmCells"), ("HUAWEI-CCC-MIB", "hwCCCVcAtmPackOvertime"), ("HUAWEI-CCC-MIB", "hwCCCVcPwJitterBufferDepth"), ("HUAWEI-CCC-MIB", "hwCCCVcPwTdmEncapsulationNum"), ("HUAWEI-CCC-MIB", "hwCCCVcPwIdleCode"), ("HUAWEI-CCC-MIB", "hwCCCVcPwRtpHeader"), ("HUAWEI-CCC-MIB", "hwCCCVcIpInterworking"), ("HUAWEI-CCC-MIB", "hwCCCVcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCVcGroup = hwCCCVcGroup.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcGroup.setDescription("The CCC's VC group.")
hwCCCVcStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 2)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcStatisticsRcvPkts"), ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsRcvBytes"), ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsSndPkts"), ("HUAWEI-CCC-MIB", "hwCCCVcStatisticsSndBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCVcStatisticsGroup = hwCCCVcStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStatisticsGroup.setDescription("The CCC's VC Statistics group.")
hwCCCNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 3)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcUpDownNotifEnable"), ("HUAWEI-CCC-MIB", "hwCCCVcDeletedNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCNotificationControlGroup = hwCCCNotificationControlGroup.setStatus('current')
if mibBuilder.loadTexts: hwCCCNotificationControlGroup.setDescription("The CCC's Notification Control group.")
hwCCCVcStateChangeReasonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 4)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcStateChangeReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCVcStateChangeReasonGroup = hwCCCVcStateChangeReasonGroup.setStatus('current')
if mibBuilder.loadTexts: hwCCCVcStateChangeReasonGroup.setDescription("The CCC's Vc State Change Reason group.")
hwCCCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 3, 3, 2, 5)).setObjects(("HUAWEI-CCC-MIB", "hwCCCVcDown"), ("HUAWEI-CCC-MIB", "hwCCCVcUp"), ("HUAWEI-CCC-MIB", "hwCCCVcDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCCCNotificationGroup = hwCCCNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwCCCNotificationGroup.setDescription('The CCC Notification group.')
mibBuilder.exportSymbols("HUAWEI-CCC-MIB", hwCCCMIBGroups=hwCCCMIBGroups, hwCCCMIBCompliance=hwCCCMIBCompliance, hwCCCVcMaxAtmCells=hwCCCVcMaxAtmCells, PYSNMP_MODULE_ID=hwL2VpnCCC, hwCCCVcDeletedNotifEnable=hwCCCVcDeletedNotifEnable, hwCCCVcGroup=hwCCCVcGroup, hwCCCVcEntry=hwCCCVcEntry, hwCCCVcTable=hwCCCVcTable, hwCCCVcStatisticsIfIndex=hwCCCVcStatisticsIfIndex, hwCCCVcStatisticsRcvPkts=hwCCCVcStatisticsRcvPkts, hwCCCVcConnectionType=hwCCCVcConnectionType, hwCCCVcStatisticsTable=hwCCCVcStatisticsTable, hwCCCVcDeleted=hwCCCVcDeleted, hwCCCVcStatisticsSndPkts=hwCCCVcStatisticsSndPkts, hwL2Vpn=hwL2Vpn, hwCCCVcPwJitterBufferDepth=hwCCCVcPwJitterBufferDepth, hwCCCVcStateChangeReason=hwCCCVcStateChangeReason, hwCCCMIBConformance=hwCCCMIBConformance, hwCCCVcStatisticsGroup=hwCCCVcStatisticsGroup, hwCCCVcStatisticsEntry=hwCCCVcStatisticsEntry, hwCCCVcPwRtpHeader=hwCCCVcPwRtpHeader, hwCCCVcDown=hwCCCVcDown, hwCCCMIBCompliances=hwCCCMIBCompliances, hwCCCVcPwIdleCode=hwCCCVcPwIdleCode, hwCCCNotificationControlGroup=hwCCCNotificationControlGroup, hwCCCVcStatisticsSndBytes=hwCCCVcStatisticsSndBytes, hwCCCMIBObjects=hwCCCMIBObjects, hwCCCVcNextHop=hwCCCVcNextHop, hwCCCVcIpInterworking=hwCCCVcIpInterworking, hwCCCVcName=hwCCCVcName, hwCCCVcInboundlabel=hwCCCVcInboundlabel, hwCCCVcUpSumTime=hwCCCVcUpSumTime, hwCCCNotificationGroup=hwCCCNotificationGroup, hwCCCVcUpStartTime=hwCCCVcUpStartTime, hwCCCVcPwTdmEncapsulationNum=hwCCCVcPwTdmEncapsulationNum, hwCCCVcOperStatus=hwCCCVcOperStatus, hwCCCVcOutIfIndex=hwCCCVcOutIfIndex, hwCCCVcUp=hwCCCVcUp, hwCCCVcAtmPackOvertime=hwCCCVcAtmPackOvertime, hwL2VpnCCC=hwL2VpnCCC, hwCCCVcEncapType=hwCCCVcEncapType, hwCCCVcStatisticsRcvBytes=hwCCCVcStatisticsRcvBytes, hwCCCVcIfIndex=hwCCCVcIfIndex, hwCCCVcRowStatus=hwCCCVcRowStatus, hwCCCVcUpDownNotifEnable=hwCCCVcUpDownNotifEnable, hwCCCMIBTraps=hwCCCMIBTraps, hwCCCVcOutboundlabel=hwCCCVcOutboundlabel, hwCCCVcCtrlWord=hwCCCVcCtrlWord, hwCCCVcStateChangeReasonGroup=hwCCCVcStateChangeReasonGroup)
