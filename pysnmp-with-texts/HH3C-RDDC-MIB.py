#
# PySNMP MIB module HH3C-RDDC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RDDC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Gauge32, ModuleIdentity, MibIdentifier, iso, Integer32, TimeTicks, Bits, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso", "Integer32", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cRddc = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 151))
hh3cRddc.setRevisions(('2014-01-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cRddc.setRevisionsDescriptions(('Creation Date.',))
if mibBuilder.loadTexts: hh3cRddc.setLastUpdated('201401030000Z')
if mibBuilder.loadTexts: hh3cRddc.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cRddc.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cRddc.setDescription('Redundancy group is concerned with ensuring minimal disruption to data and control planes in case of a failover. If one of the group-node in an IRF fails, the other group-node in the IRF takes over the function of the failed group-node with minimal service interruption. This module defines the objects pertaining to redundancy group(RDDC).')
hh3cRddcNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 151, 0))
hh3cRddcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1))
hh3cRddcInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1))
hh3cRddcTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2))
hh3cRddcTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cRddcTable.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcTable.setDescription('This table describes the current status of redundancy groups.')
hh3cRddcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-RDDC-MIB", "hh3cRddcGroupIdx"))
if mibBuilder.loadTexts: hh3cRddcEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcEntry.setDescription('The entry of hh3cRddcEntry.')
hh3cRddcGroupIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cRddcGroupIdx.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcGroupIdx.setDescription('Unique identifier of this redundancy group. 0 is an invalid value.')
hh3cRddcGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcGroupName.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcGroupName.setDescription('Unique identifier of this redundancy group.')
hh3cRddcPreempTimeRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 3), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcPreempTimeRemain.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcPreempTimeRemain.setDescription('The redundancy group should not switch back immediately when a failover is recovered. The preempt delay timer is started for waiting the failover became believable. This object contains the current preempt delay time remained when a failover is recovered.')
hh3cRddcPreempTimeConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 4), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcPreempTimeConfig.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcPreempTimeConfig.setDescription('The current preempt delay time.')
hh3cRddcHoldTimeRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcHoldTimeRemain.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcHoldTimeRemain.setDescription('To prevent frequent switchovers of the redundancy group, the hold-down timer started to keeping in a state for a fixed time. This object contains the current remained hold-down time when a switchover or a failover recovery occurred.')
hh3cRddcHoldTimeConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcHoldTimeConfig.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcHoldTimeConfig.setDescription('The current hold-down time.')
hh3cRddcNodeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cRddcNodeTable.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeTable.setDescription('This table describes the current status of a redundancy group node.')
hh3cRddcNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1), ).setIndexNames((0, "HH3C-RDDC-MIB", "hh3cRddcNodeGroupIdx"), (0, "HH3C-RDDC-MIB", "hh3cRddcNodeId"))
if mibBuilder.loadTexts: hh3cRddcNodeEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeEntry.setDescription('The entry of hh3cRddcNodeEntry.')
hh3cRddcNodeGroupIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cRddcNodeGroupIdx.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeGroupIdx.setDescription('Unique identifier of this redundancy group. 0 is an invalid value.')
hh3cRddcNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hh3cRddcNodeId.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeId.setDescription('Unique identifier of this redundancy group node. 0 is an invalid value.')
hh3cRddcNodeBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("chassis", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcNodeBindType.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeBindType.setDescription('The bind type of this redundancy group node. The current version only supports binding chassis of an IRF device.')
hh3cRddcNodeBindInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcNodeBindInfo.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeBindInfo.setDescription('The bind information of this redundancy group node. The current version only supports binding chassis of an IRF device. If the value of hh3cRddcNodeBindType is invalid, the value of hh3cRddcNodeBindInfo is 65535.')
hh3cRddcNodePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcNodePriority.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodePriority.setDescription('The priority of this redundancy group node. The higher the value, the greater the priority.')
hh3cRddcNodeWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcNodeWeight.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeWeight.setDescription('The current weight of this redundancy group node. The max value is 255.')
hh3cRddcNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("master", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRddcNodeStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeStatus.setDescription('The current status of this redundancy group node.')
hh3cRddcNodeInfo = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cRddcNodeInfo.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcNodeInfo.setDescription('This object contains node identification information where the switchover occurred.')
hh3cRddcSwitchReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 151, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cRddcSwitchReason.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcSwitchReason.setDescription('This object contains the cause for switchover.')
hh3cRddcSwitchoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 1)).setObjects(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"), ("HH3C-RDDC-MIB", "hh3cRddcGroupName"), ("HH3C-RDDC-MIB", "hh3cRddcNodeInfo"), ("HH3C-RDDC-MIB", "hh3cRddcSwitchReason"))
if mibBuilder.loadTexts: hh3cRddcSwitchoverTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcSwitchoverTrap.setDescription('Notification to signal switchover/failover.')
hh3cRddcFailIfRecoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 2)).setObjects(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"), ("HH3C-RDDC-MIB", "hh3cRddcGroupName"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cRddcFailIfRecoverTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcFailIfRecoverTrap.setDescription('Notification to signal the failed interface recovered.')
hh3cRddcFailIfGenerateTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 151, 0, 3)).setObjects(("HH3C-RDDC-MIB", "hh3cRddcGroupIdx"), ("HH3C-RDDC-MIB", "hh3cRddcGroupName"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cRddcFailIfGenerateTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cRddcFailIfGenerateTrap.setDescription('Notification to signal the failed interface generated.')
mibBuilder.exportSymbols("HH3C-RDDC-MIB", hh3cRddcNodeInfo=hh3cRddcNodeInfo, hh3cRddcNotifications=hh3cRddcNotifications, hh3cRddcPreempTimeConfig=hh3cRddcPreempTimeConfig, hh3cRddcNodeBindInfo=hh3cRddcNodeBindInfo, hh3cRddc=hh3cRddc, PYSNMP_MODULE_ID=hh3cRddc, hh3cRddcSwitchoverTrap=hh3cRddcSwitchoverTrap, hh3cRddcNodeTable=hh3cRddcNodeTable, hh3cRddcFailIfRecoverTrap=hh3cRddcFailIfRecoverTrap, hh3cRddcHoldTimeRemain=hh3cRddcHoldTimeRemain, hh3cRddcFailIfGenerateTrap=hh3cRddcFailIfGenerateTrap, hh3cRddcNodeEntry=hh3cRddcNodeEntry, hh3cRddcHoldTimeConfig=hh3cRddcHoldTimeConfig, hh3cRddcNodePriority=hh3cRddcNodePriority, hh3cRddcInfo=hh3cRddcInfo, hh3cRddcPreempTimeRemain=hh3cRddcPreempTimeRemain, hh3cRddcTrapObjects=hh3cRddcTrapObjects, hh3cRddcObjects=hh3cRddcObjects, hh3cRddcNodeWeight=hh3cRddcNodeWeight, hh3cRddcGroupIdx=hh3cRddcGroupIdx, hh3cRddcTable=hh3cRddcTable, hh3cRddcNodeStatus=hh3cRddcNodeStatus, hh3cRddcEntry=hh3cRddcEntry, hh3cRddcNodeId=hh3cRddcNodeId, hh3cRddcNodeBindType=hh3cRddcNodeBindType, hh3cRddcGroupName=hh3cRddcGroupName, hh3cRddcSwitchReason=hh3cRddcSwitchReason, hh3cRddcNodeGroupIdx=hh3cRddcNodeGroupIdx)
