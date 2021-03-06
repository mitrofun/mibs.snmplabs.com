#
# PySNMP MIB module QLASP-Config-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QLASP-Config-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:43:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, TimeTicks, MibIdentifier, NotificationType, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Gauge32, Bits, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "MibIdentifier", "NotificationType", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Gauge32", "Bits", "enterprises", "Unsigned32")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
qlaspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1))
qlaspTeam = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1))
qlaspPhyAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2))
qlaspVirAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3))
btTeamNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btTeamNumber.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamNumber.setDescription('The number of loadbalance teams present on this system.')
btTeamTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2), )
if mibBuilder.loadTexts: btTeamTable.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamTable.setDescription('A list of team entries. The number of teams is given by the value of teamNumber.')
btTeamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1), ).setIndexNames((0, "QLASP-Config-MIB", "btTeamIndex"))
if mibBuilder.loadTexts: btTeamEntry.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamEntry.setDescription('An entry containing team objects at the target system.')
btTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btTeamIndex.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamIndex.setDescription("An unique value for each team. The value for each team must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
btTeamName = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btTeamName.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamName.setDescription('A textual string containing name of the team')
btTeamType = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(100, 101, 102, 104))).clone(namedValues=NamedValues(("team-SLB", 100), ("team-FEC-GEC", 101), ("team-802-3-AD", 102), ("team-SLB-AFD", 104)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btTeamType.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamType.setDescription('The type of team, distinguished according to the attribute assigned. When team has only one physical member, the team type is ignored')
btTeamMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btTeamMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: btTeamMacAddress.setDescription('Mac address of the team. Mac address is assigned to a team when the team type is team-FEC-GEC(101) or team-802-3-AD(102)')
btPhyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btPhyNumber.setStatus('mandatory')
if mibBuilder.loadTexts: btPhyNumber.setDescription('Number of physical adapters in the team')
btVirNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btVirNumber.setStatus('mandatory')
if mibBuilder.loadTexts: btVirNumber.setDescription('Number of virtual adapters in the team ')
btMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primaryMode", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btMode.setStatus('mandatory')
if mibBuilder.loadTexts: btMode.setDescription('mode of this team, PrimaryMode(0) or Standby(1). For team type other than team-SLB(100), this should always be PrimaryMode(0).')
btLiveLinkEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLiveLinkEnable.setStatus('mandatory')
if mibBuilder.loadTexts: btLiveLinkEnable.setDescription('LiveLink is enabled or not. Probe packet can be enabled only for team-SLB(100) and team-SLB-AFD(104).')
btLinkPacketFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkPacketFrequency.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkPacketFrequency.setDescription('For LiveLink feature: The frequency in milliseconds that a link packet is to be sent.')
btLinkMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkMaxRetry.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkMaxRetry.setDescription('For LiveLink feature: The maximum number of retries before failing a team member.')
btLinkRetryFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkRetryFrequency.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkRetryFrequency.setDescription('For LiveLink feature: The frequency (milliseconds) a link packet is to be sent after a dropped link packet is detected.')
btLinkTargetIpAddress1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkTargetIpAddress1.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkTargetIpAddress1.setDescription('For LiveLink feature: The target IP address that a link packet is sent to. A DNS name cannot be specified since there is no reliable method to resolve the DNS name without introducing unacceptable risk. Only the first one is mandatory for LiveLink. All 0 is not available.')
btLinkTargetIpAddress2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkTargetIpAddress2.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkTargetIpAddress2.setDescription('For LiveLink feature: The target IP address that a link packet is sent to. A DNS name cannot be specified since there is no reliable method to resolve the DNS name without introducing unacceptable risk. This one is optional for LiveLink. All 0 is not available.')
btLinkTargetIpAddress3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkTargetIpAddress3.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkTargetIpAddress3.setDescription('For LiveLink feature: The target IP address that a link packet is sent to. A DNS name cannot be specified since there is no reliable method to resolve the DNS name without introducing unacceptable risk. This one is optional for LiveLink. All 0 is not available.')
btLinkTargetIpAddress4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 1, 2, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btLinkTargetIpAddress4.setStatus('mandatory')
if mibBuilder.loadTexts: btLinkTargetIpAddress4.setDescription('For LiveLink feature: The target IP address that a link packet is sent to. A DNS name cannot be specified since there is no reliable method to resolve the DNS name without introducing unacceptable risk. This one is optional for LiveLink. All 0 is not available.')
btPhyAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btPhyAdapterNumber.setStatus('mandatory')
if mibBuilder.loadTexts: btPhyAdapterNumber.setDescription('Number of physical adapters presented in the physical adapter table.')
btPhyAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2), )
if mibBuilder.loadTexts: btPhyAdapterTable.setStatus('mandatory')
if mibBuilder.loadTexts: btPhyAdapterTable.setDescription('The phyMember tables contain the physical adapter members of loadbalance teams.')
btPhyAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1), ).setIndexNames((0, "QLASP-Config-MIB", "btpTeamIndex"), (0, "QLASP-Config-MIB", "btpAdapterIndex"))
if mibBuilder.loadTexts: btPhyAdapterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: btPhyAdapterEntry.setDescription('A team entry containing objects at the target system.')
btpTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btpTeamIndex.setStatus('mandatory')
if mibBuilder.loadTexts: btpTeamIndex.setDescription('An unique value for each team.')
btpAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btpAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: btpAdapterIndex.setDescription('A value for each adapter within a team.')
btpAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btpAdapterDesc.setStatus('mandatory')
if mibBuilder.loadTexts: btpAdapterDesc.setDescription(' A textual string containing name of the adapter')
btpMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(100, 101))).clone(namedValues=NamedValues(("load-balance", 100), ("standby", 101)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btpMemberType.setStatus('mandatory')
if mibBuilder.loadTexts: btpMemberType.setDescription('The type of adapter member.')
btpMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btpMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: btpMacAddress.setDescription('Mac address of the adapter.')
btpMemberState = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("link-up-not-join-traffic", 2), ("disable-not-join-traffic", 3), ("join-traffic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btpMemberState.setStatus('mandatory')
if mibBuilder.loadTexts: btpMemberState.setDescription('State of the interface in the team.')
btpLiveLinkIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btpLiveLinkIp.setStatus('mandatory')
if mibBuilder.loadTexts: btpLiveLinkIp.setDescription('IP address for LiveLink.')
btVirAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btVirAdapterNumber.setStatus('mandatory')
if mibBuilder.loadTexts: btVirAdapterNumber.setDescription('Number of virtual adapters presented in the virtual adapter table.')
btVirAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2), )
if mibBuilder.loadTexts: btVirAdapterTable.setStatus('mandatory')
if mibBuilder.loadTexts: btVirAdapterTable.setDescription('The virMember tables contain the VLAN members of loadbalance teams.')
btVirAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1), ).setIndexNames((0, "QLASP-Config-MIB", "btvTeamIndex"), (0, "QLASP-Config-MIB", "btvAdapterIndex"))
if mibBuilder.loadTexts: btVirAdapterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: btVirAdapterEntry.setDescription('A team entry containing objects at the target system.')
btvTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btvTeamIndex.setStatus('mandatory')
if mibBuilder.loadTexts: btvTeamIndex.setDescription('An unique value for each team.')
btvAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btvAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: btvAdapterIndex.setDescription('A unique value for each virtual adapter in a team.')
btvAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvAdapterDesc.setStatus('mandatory')
if mibBuilder.loadTexts: btvAdapterDesc.setDescription(' A textual string containing name of the VLAN')
btvVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: btvVlanId.setDescription('802.1Q VLAN ID of the virtual adapter.')
btvLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: btvLinkStatus.setDescription('Virtual adapter link status')
btvIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: btvIPAddress.setDescription('IP address of the virtual adapter.')
btvSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: btvSubnetMask.setDescription('IP subnet Mask of the virtual adapter.')
btvPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 8), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: btvPhysAddress.setDescription('MAC address of the virtual adapter.')
btvLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1, 3, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btvLineSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: btvLineSpeed.setDescription('A textual string displays the operating speed of the virtual adapter.')
mibBuilder.exportSymbols("QLASP-Config-MIB", btvPhysAddress=btvPhysAddress, qlaspTeam=qlaspTeam, btTeamEntry=btTeamEntry, btpAdapterDesc=btpAdapterDesc, btPhyNumber=btPhyNumber, btvAdapterDesc=btvAdapterDesc, btLinkTargetIpAddress4=btLinkTargetIpAddress4, btLinkTargetIpAddress1=btLinkTargetIpAddress1, btVirNumber=btVirNumber, qlaspConfig=qlaspConfig, btTeamTable=btTeamTable, btpLiveLinkIp=btpLiveLinkIp, btTeamNumber=btTeamNumber, qlaspVirAdapter=qlaspVirAdapter, btPhyAdapterNumber=btPhyAdapterNumber, enet=enet, btLiveLinkEnable=btLiveLinkEnable, btvAdapterIndex=btvAdapterIndex, btpMemberType=btpMemberType, qlaspPhyAdapter=qlaspPhyAdapter, btPhyAdapterEntry=btPhyAdapterEntry, btLinkMaxRetry=btLinkMaxRetry, btTeamName=btTeamName, btvSubnetMask=btvSubnetMask, qlasp=qlasp, btTeamType=btTeamType, btvTeamIndex=btvTeamIndex, btMode=btMode, btTeamIndex=btTeamIndex, btLinkTargetIpAddress3=btLinkTargetIpAddress3, btVirAdapterNumber=btVirAdapterNumber, btLinkTargetIpAddress2=btLinkTargetIpAddress2, btvLinkStatus=btvLinkStatus, btpTeamIndex=btpTeamIndex, btpAdapterIndex=btpAdapterIndex, btLinkRetryFrequency=btLinkRetryFrequency, btTeamMacAddress=btTeamMacAddress, btvIPAddress=btvIPAddress, btVirAdapterTable=btVirAdapterTable, qlogic=qlogic, btPhyAdapterTable=btPhyAdapterTable, btpMemberState=btpMemberState, btvLineSpeed=btvLineSpeed, btvVlanId=btvVlanId, btpMacAddress=btpMacAddress, btVirAdapterEntry=btVirAdapterEntry, btLinkPacketFrequency=btLinkPacketFrequency)
