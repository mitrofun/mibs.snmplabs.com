#
# PySNMP MIB module HUAWEI-SUPERLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SUPERLAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
huaweiMgmt, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Unsigned32, ObjectIdentity, TimeTicks, iso, IpAddress, Bits, Integer32, Counter32, NotificationType, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Unsigned32", "ObjectIdentity", "TimeTicks", "iso", "IpAddress", "Bits", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "ModuleIdentity")
DisplayString, TimeStamp, RowStatus, TextualConvention, PhysAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TextualConvention", "PhysAddress", "TruthValue")
hwSuperLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178))
if mibBuilder.loadTexts: hwSuperLagMIB.setLastUpdated('200810211010Z')
if mibBuilder.loadTexts: hwSuperLagMIB.setOrganization('Organization.')
if mibBuilder.loadTexts: hwSuperLagMIB.setContactInfo('Contact-info.')
if mibBuilder.loadTexts: hwSuperLagMIB.setDescription('Description.')
hwDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwSuperLagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1))
hwSuperLagTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1), )
if mibBuilder.loadTexts: hwSuperLagTable.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagTable.setDescription('The super LAG table.')
hwSuperLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1), ).setIndexNames((0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagId"))
if mibBuilder.loadTexts: hwSuperLagEntry.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagEntry.setDescription('Super LAG entry.')
hwSuperLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSuperLagId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagId.setDescription('The ID of the super LAG, it is the index of the super LAG.')
hwSuperLagSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagSystemId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagSystemId.setDescription('The system ID of the super LAG, it is a physical address.')
hwSuperLagPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagPri.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPri.setDescription('The priority of the super LAG. The default is 100.')
hwSuperLagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagStatus.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagStatus.setDescription('The status of the super LAG. 1:initialize 2:backup 3:master')
hwSuperLagStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("pri", 1), ("timeout", 2), ("bfdDown", 3), ("peerTimeout", 4), ("peerBfdDown", 5), ("allMemberDown", 6), ("init", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagStatusReason.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagStatusReason.setDescription('The reason for the super LAG is in the current status. pri(1):Priority calculation timeout(2):Receiving timer timeout bfdDown(3):BFD detected the control link between the PE and peer down peerTimeout(4):Receiving timer of the peer timeout peerBfdDown(5):BFD of the peer detected the control link between the PE and peer down allMemberDown(6):All SuperLagMembers of the superlag down init(7):The initial superlag. ')
hwSuperLagPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagPeerIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPeerIpAddr.setDescription('The IP address of the peer super LAG.')
hwSuperLagSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSourceIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagSourceIpAddr.setDescription('The source IP address of the super LAG.')
hwSuperLagReceiveFailTimeMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagReceiveFailTimeMultiple.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagReceiveFailTimeMultiple.setDescription('The fail time of the super LAG for receiving packets. It is the multiple of sending period.')
hwSuperLagSendPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSendPeriod.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagSendPeriod.setDescription('The period for sending packets of the super LAG. The unit is 100ms')
hwSuperLagPacketReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketReceive.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPacketReceive.setDescription('The number of the received packets.')
hwSuperLagPacketSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketSend.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPacketSend.setDescription('The number of the sending packets.')
hwSuperLagPacketRecDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketRecDrop.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPacketRecDrop.setDescription('The number of the droped packets when the packets are received.')
hwSuperLagPacketSndDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPacketSndDrop.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPacketSndDrop.setDescription('The number of the droped packets when the packets are send out.')
hwSuperLagPeerSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerSystemId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPeerSystemId.setDescription('The system ID of peer super LAG,it is a physical address.')
hwSuperLagPeerPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerPri.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPeerPri.setDescription('The priority of the peer super LAG.')
hwSuperLagPeerReceiveFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagPeerReceiveFailTime.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagPeerReceiveFailTime.setDescription('The fail time of the peer super LAG for receiving packets.The unit is 100ms')
hwSuperLagSecurityKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSecurityKeyType.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagSecurityKeyType.setDescription('The mode of the security key. 1:The simple encrypt mode; 2:The cipher encrypt mode.')
hwSuperLagSecurityKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagSecurityKey.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagSecurityKey.setDescription('This is the security key. It is must be hex number and the most number is 16. If hwSuperLagSecurityKeyType is simple, you can get the key. If hwSuperLagSecurityKeyType is cipher, the system returns a random character string with 24 bytes.')
hwSuperLagBfdSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagBfdSessId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagBfdSessId.setDescription('The ID of BFD session which is bind to a super LAG. When the status of the link is changed, BFD will notify super LAG.')
hwSuperLagResetCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagResetCounter.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagResetCounter.setDescription('Reset hwSuperLagPacketReceive,hwSuperLagPacketSend,hwSuperLagPacketRecDrop,hwSuperLagPacketSndDrop.')
hwSuperLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagRowStatus.setDescription('Current operation status of the row.Used to manage the creation and deletion of conceptual rows.')
hwSuperLagMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2), )
if mibBuilder.loadTexts: hwSuperLagMemberTable.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberTable.setDescription('The member table of a super LAG.')
hwSuperLagMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1), ).setIndexNames((0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberParentSuperLagId"), (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberType"), (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberId"))
if mibBuilder.loadTexts: hwSuperLagMemberEntry.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberEntry.setDescription('Member Entry.')
hwSuperLagMemberParentSuperLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSuperLagMemberParentSuperLagId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberParentSuperLagId.setDescription('The ID of the super LAG which the member is belonged to.')
hwSuperLagMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwSuperLagMemberType.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberType.setDescription('The type of the member. Now is EthTrunk only. 1:EthTrunk')
hwSuperLagMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwSuperLagMemberId.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberId.setDescription('The ID of the member.')
hwSuperLagMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberStatus.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberStatus.setDescription('The member status. 1:backup 2:master.')
hwSuperLagMemberStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("forceBackup", 1), ("forceMaster", 2), ("suplagInit", 3), ("suplagBackup", 4), ("suplagMaster", 5), ("peerMemberDown", 6), ("peerMemberUp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberStatusReason.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberStatusReason.setDescription('The reason for the member is in the current status. forceBackup(1):The work mode of the member is force-backup forceMaster(2):The work mode of the member is force-master suplagInit(3):The work mode of the member is auto, the status of parent super LAG is INITIALIZE suplagBackup(4):The work mode of the member is auto, the status of parent super LAG is BACKUP suplagMaster(5):The work mode of the member is auto, the status of parent super LAG is MASTER peerMemberDown(6):The status of the members belonged to the peer super LAG is down peerMemberUp(7):The status of the members belonged to the peer super LAG is up')
hwSuperLagMemberWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("forceBackup", 2), ("forceMaster", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagMemberWorkMode.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberWorkMode.setDescription('The work mode of the member. 1:auto 2:forceBackup 3:forceMaster')
hwSuperLagMemberLocaPhylLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSuperLagMemberLocaPhylLinkStatus.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberLocaPhylLinkStatus.setDescription('The local physical link status of the member. 1:up 2:down')
hwSuperLagMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSuperLagMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberRowStatus.setDescription('Current operation status of the row.Used to manage the creation and deletion of conceptual rows.')
hwSuperLagTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2))
hwSuperLagStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"))
if mibBuilder.loadTexts: hwSuperLagStatusChange.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagStatusChange.setDescription('The event is generated when the status of the super LAG is changed or the status reason of the super LAG is changed.')
hwSuperLagMemberStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"))
if mibBuilder.loadTexts: hwSuperLagMemberStatusChange.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberStatusChange.setDescription('The event is generated when the status of the memeber is changed or the status reason of the memeber is changed.')
hwSuperLagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3))
hwSuperLagCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1))
hwSuperLagFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagGroup"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberGroup"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagFullCompliance = hwSuperLagFullCompliance.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagFullCompliance.setDescription('Description.')
hwSuperLagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2))
hwSuperLagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagSystemId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPri"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerIpAddr"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSourceIpAddr"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagReceiveFailTimeMultiple"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSendPeriod"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketReceive"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSend"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketRecDrop"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSndDrop"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerSystemId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerPri"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerReceiveFailTime"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKeyType"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKey"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagBfdSessId"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagResetCounter"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagGroup = hwSuperLagGroup.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagGroup.setDescription('Description.')
hwSuperLagMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberWorkMode"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberLocaPhylLinkStatus"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagMemberGroup = hwSuperLagMemberGroup.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagMemberGroup.setDescription('Description.')
hwSuperLagNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)).setObjects(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusChange"), ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSuperLagNotificationGroup = hwSuperLagNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwSuperLagNotificationGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-SUPERLAG-MIB", hwSuperLagMIB=hwSuperLagMIB, hwSuperLagResetCounter=hwSuperLagResetCounter, hwSuperLagMemberGroup=hwSuperLagMemberGroup, hwSuperLagGroups=hwSuperLagGroups, hwSuperLagConformance=hwSuperLagConformance, hwSuperLagStatusReason=hwSuperLagStatusReason, hwSuperLagPacketSndDrop=hwSuperLagPacketSndDrop, hwSuperLagMemberType=hwSuperLagMemberType, hwSuperLagStatusChange=hwSuperLagStatusChange, hwSuperLagCompliances=hwSuperLagCompliances, hwSuperLagMemberStatusReason=hwSuperLagMemberStatusReason, hwSuperLagBfdSessId=hwSuperLagBfdSessId, hwSuperLagRowStatus=hwSuperLagRowStatus, hwSuperLagMemberTable=hwSuperLagMemberTable, hwSuperLagMemberRowStatus=hwSuperLagMemberRowStatus, hwSuperLagSendPeriod=hwSuperLagSendPeriod, hwSuperLagPacketReceive=hwSuperLagPacketReceive, hwSuperLagMemberLocaPhylLinkStatus=hwSuperLagMemberLocaPhylLinkStatus, hwSuperLagGroup=hwSuperLagGroup, hwSuperLagId=hwSuperLagId, hwSuperLagPri=hwSuperLagPri, hwSuperLagPeerIpAddr=hwSuperLagPeerIpAddr, hwSuperLagStatus=hwSuperLagStatus, hwSuperLagEntry=hwSuperLagEntry, hwSuperLagMemberParentSuperLagId=hwSuperLagMemberParentSuperLagId, hwSuperLagFullCompliance=hwSuperLagFullCompliance, hwSuperLagNotificationGroup=hwSuperLagNotificationGroup, hwSuperLagSecurityKey=hwSuperLagSecurityKey, hwSuperLagMemberStatusChange=hwSuperLagMemberStatusChange, hwSuperLagPeerPri=hwSuperLagPeerPri, hwSuperLagTable=hwSuperLagTable, hwSuperLagReceiveFailTimeMultiple=hwSuperLagReceiveFailTimeMultiple, hwSuperLagPeerReceiveFailTime=hwSuperLagPeerReceiveFailTime, hwDatacomm=hwDatacomm, hwSuperLagSourceIpAddr=hwSuperLagSourceIpAddr, hwSuperLagPacketRecDrop=hwSuperLagPacketRecDrop, hwSuperLagSystemId=hwSuperLagSystemId, hwSuperLagPeerSystemId=hwSuperLagPeerSystemId, hwSuperLagMemberStatus=hwSuperLagMemberStatus, hwSuperLagTraps=hwSuperLagTraps, hwSuperLagMemberId=hwSuperLagMemberId, hwSuperLagSecurityKeyType=hwSuperLagSecurityKeyType, PYSNMP_MODULE_ID=hwSuperLagMIB, hwSuperLagMemberEntry=hwSuperLagMemberEntry, hwSuperLagObjects=hwSuperLagObjects, hwSuperLagMemberWorkMode=hwSuperLagMemberWorkMode, hwSuperLagPacketSend=hwSuperLagPacketSend)
