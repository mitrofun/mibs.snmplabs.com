#
# PySNMP MIB module S5-SWITCH-BAYSECURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-SWITCH-BAYSECURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:59:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
s5Com, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Com")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, MibIdentifier, Counter64, Counter32, Bits, NotificationType, ObjectIdentity, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity", "iso")
DisplayString, TimeInterval, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "MacAddress", "TextualConvention", "TruthValue")
s5SbsAuth = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3))
s5SbsAuth.setRevisions(('2012-09-13 00:00', '2011-01-10 00:00', '2009-05-28 00:00', '2009-02-24 00:00', '2006-09-18 00:00', '2005-03-09 00:00', '2004-09-03 00:00', '2004-07-22 00:00', '2004-07-20 00:00', '2003-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: s5SbsAuth.setRevisionsDescriptions(('Version 114: Changed s5SbsAutoLearningAgingTime.', 'Version 113: Added s5SbsAuthCfgTrunk.', 'Version 112: Added support for port lock-out feature.', "Version 111: Added support for 'sticky-mac' feature. Made some SMIv2 compliance fixes.", 'Version 110: Fix DESCRIPTIONS', 'Version 109: Expanded range of s5SbsAutoLearningConfigMaxMacs.', 'Version 108: Added s5SbsAutoLearningPorts.', 'Version 107: Added auto-learning enhancements.', 'Version 106: Added version info', 'v104: 1. Added s5SbsMacViolationTable 2. Converted to SMIv2',))
if mibBuilder.loadTexts: s5SbsAuth.setLastUpdated('201209130000Z')
if mibBuilder.loadTexts: s5SbsAuth.setOrganization('Avaya')
if mibBuilder.loadTexts: s5SbsAuth.setContactInfo('Avaya')
if mibBuilder.loadTexts: s5SbsAuth.setDescription("BaySecure MIB - MAC-based Security MIB Copyright 1999-2012 Avaya All rights reserved. This Avaya SNMP Management Information Base Specification (Specification) embodies Avaya's confidential and proprietary intellectual property. Avaya retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class PortSet(TextualConvention, OctetString):
    description = 'The string is a variable length string which may vary from 0 to 256 octets long. The user must use the OCTET STRING length field in order to convey/determine how many octets are being used. Each bit corresponds to a port, as represented by its ifIndex value . When a bit has the value one(1), the corresponding port is a member of the set. When a bit has the value zero(0), the corresponding port is not a member of the set. The encoding is such that the most significant bit of octet #1 corresponds to ifIndex 0, while the least significant bit of the last octet corresponds to ifIndex ((octet_string_length * 8) - 1). For example, the least significant bit of octet #64 corresponds to ifIndex 511.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

s5SbsAuthSecurityLock = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("locked", 2), ("notlocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthSecurityLock.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthSecurityLock.setDescription("If s5SbsAuthSecurityLock is locked(2), the agent will refuse all requests to modify the 'security configuration'. Objects in s5SbsAuth, the Switch BaySecure MIB Group that are part of the 'security configuration', includes s5SbsAuthCtlPartTime, objects in s5SbsAuthCfgTable, Set requests for all read/write objects in s5SbsAuth group excluding this object will result in a BadValue return value.")
s5SbsAuthCtlPartTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAuthCtlPartTime.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCtlPartTime.setDescription('If the value of s5SbsAuthCfgActionMode is partitionPort or partitionPortAndSendTrap, time partition will be done if this value is greater than 0. The value indicates the duration of the time for port partitioning in seconds. The default value is zero. When this value is zero, port remians partitioned until manually re-enabled.')
s5SbsSecurityStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityStatus.setDescription('Indicates whether the switch security feature is enabled or not.')
s5SbsSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("singleMACperPort", 1), ("macList", 2), ("autoLearn", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityMode.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityMode.setDescription('The mode of switch security. singleMACperPort(1) indicates that the switch is in single-MAC-per-port mode which means it allows to configure only one MAC address per port. macList(2) indicates that the switch is in MAC-List mode, user can configure more than one MAC address per port, the maximum numbers of MAC address per port vary from switch to switch. autoLearn(3) indicates that the switch will learn the first MAC address on each port as an allowed address of that port. Change made between singleMACperPort(1), macList(2) and autoLearn(3) will erase all the data in s5SbsAuthCfgTable.')
s5SbsSecurityAction = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noAction", 1), ("trap", 2), ("partitionPort", 3), ("partitionPortAndsendTrap", 4), ("daFiltering", 5), ("daFilteringAndsendTrap", 6), ("partitionPortAnddaFiltering", 7), ("partitionPortdaFilteringAndsendTrap", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityAction.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityAction.setDescription('Action performed by software when a violation occurs (if s5SbsSecurityStatus is enabled). The security action specified here applies to all ports of the switch. NOTE: da means destination address. A blocked address will always cause the port to be partitioned when unauthorized access is attempted. See s5SbsAuthCfgAccessCtrlType for more information on allowed and blocked addresses.')
s5SbsCurrNodesAllowed = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrNodesAllowed.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrNodesAllowed.setDescription('The current number of entries of the nodes allowed in the s5SbsAuthCfgTable.')
s5SbsMaxNodesAllowed = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMaxNodesAllowed.setStatus('current')
if mibBuilder.loadTexts: s5SbsMaxNodesAllowed.setDescription('The maximum number of entries of the nodes allowed in the s5SbsAuthCfgTable.')
s5SbsCurrNodesBlocked = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrNodesBlocked.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrNodesBlocked.setDescription('The current number of entries of the nodes blocked in the s5SbsAuthCfgTable.')
s5SbsMaxNodesBlocked = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMaxNodesBlocked.setStatus('current')
if mibBuilder.loadTexts: s5SbsMaxNodesBlocked.setDescription('The maximum number of entries of the nodes blocked in the s5SbsAuthCfgTable.')
s5SbsAuthCfgTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10), )
if mibBuilder.loadTexts: s5SbsAuthCfgTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgTable.setDescription('A table containing a list of boards and ports and MAC addresses that constitute the security configuration.')
s5SbsAuthCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgBrdIndx"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgPortIndx"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthCfgMACIndx"))
if mibBuilder.loadTexts: s5SbsAuthCfgEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgEntry.setDescription('An entry in this table indicates the security configuration for a specified MAC address and a specified port and a specified board. A SNMP SET PDU for a row of the s5SbsAuthCfgTable requires the entired sequence of the MIB Objects in each s5SbsAuthCfgEntry stored in one PDU. Otherwise, GENERR return-value will be returned.')
s5SbsAuthCfgBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthCfgBrdIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgBrdIndx.setDescription('The index of the slot containing the board on which the port is located. This value is meaningful --NEW only if s5SbsAuthCfgSecureList value is zero. --NEW For other SecureList values it should have the value of zero. ')
s5SbsAuthCfgPortIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthCfgPortIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgPortIndx.setDescription('The index of the port on the board. This value is meaningful only if s5SbsAuthCfgSecureList value is zero. --NEW For other SecureList values it should have the value of zero. ')
s5SbsAuthCfgMACIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthCfgMACIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgMACIndx.setDescription('The index of source MAC address of allowed station or not-allowed station.')
s5SbsAuthCfgAccessCtrlType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("blocked", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAuthCfgAccessCtrlType.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgAccessCtrlType.setDescription('This Node Access Control Type represents whether the node entry is node allowed or node blocked type. A MAC address may be allowed on multiple ports.')
s5SbsAuthCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("valid", 1), ("create", 2), ("delete", 3), ("modify", 4), ("createSticky", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAuthCfgStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgStatus.setDescription('The status of the AuthCfg entry. The primary use of this object is for modifying the AuthCfg table. Values that can be written create(2), delete(3), modify(4). Values that can be read: valid(1). Setting this entry to delete(3) causes the entry to be deleted from the table. Setting a new entry with create(2) causes the entry to be created in the table. Setting an entry with modify(4) causes the entry to be modified. The response to a get request or get-next request will always indicate a status of valid (1), since invalid entries are removed from the table. This object cannot be modified for entries whose value of s5SbsAuthCfgSource is autoLearn(2) if the value of s5SbsAutoLearningSticky is false(2). Any such attempt will generate an inconsistentValue error.')
s5SbsAuthCfgSecureList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAuthCfgSecureList.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgSecureList.setDescription('The index of the security list. This value is meaningful only if s5SbsAuthCfgBrdIndx and s5SbsAuthCfgPortIndx values are zero. For other board and port index values it should have the value of zero. This value is used as an index into s5SbsSecurityListTable. The corresponding MAC Address of this entry is allowed or blocked on all the ports of that port list. Note that this value must be 0 for entries where the value of s5SbsAuthCfgSource is either autoLearn(2) or sticky(3).')
s5SbsAuthCfgSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("autoLearn", 2), ("sticky", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthCfgSource.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgSource.setDescription('This object indicates the source of an entry. A value of static(1) indicates that the entry was manually created by a user. A value of autoLearn(2) indicates that the entry was auto-learned. Note that if the value of s5SbsAutoLearningSticky is false(2), then an auto-learned entry cannot be directly deleted, though disabling auto-learning for a port will delete all auto-learned MAC addresses for the port. However, if the value of s5SbsAutoLearningSticky is true(1), then auto-learned addresses can be deleted normally.')
s5SbsAuthCfgLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 8), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthCfgLifetime.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgLifetime.setDescription('This object indicates the lifetime of an auto-learned entry. This is the time until the entry is automatically deleted by the system. This object does not apply to entries whose value of s5SbsAuthCfgSource is static(1), and for such entries, the value of this object will always be 0.')
s5SbsAuthCfgTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 10, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAuthCfgTrunk.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthCfgTrunk.setDescription('The trunk on which a MAC address is allowed or disallowed. This value must be 0 if the value of any of these objects is non-zero: s5SbsAuthCfgBrdIndx s5SbsAuthCfgPortIndx s5SbsAuthCfgSecureList The value of this object is only used if the above objects all have zero values. The value of this object must also be 0 if the value of s5SbsAuthCfgSource is either autoLearn(2) or sticky(3).')
s5SbsAuthStatusTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11), )
if mibBuilder.loadTexts: s5SbsAuthStatusTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthStatusTable.setDescription('A table containing a snapshot of the authorized boards and ports status data collection. Port security information consists of an action to be performed when an unAuthorized station is detected and the current security status of a port.')
s5SbsAuthStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusBrdIndx"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusPortIndx"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAuthStatusMACIndx"))
if mibBuilder.loadTexts: s5SbsAuthStatusEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthStatusEntry.setDescription('An entry in this table may represent a single MAC address, all MAC addresses on a single port, a single port, all the ports on a single board, a particuler port on all the boards, or all the ports on all the boards.')
s5SbsAuthStatusBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthStatusBrdIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthStatusBrdIndx.setDescription('The index of the board. This corresponds to the index of the slot containing the board if the index is greater than zero. A zero index is a wild card.')
s5SbsAuthStatusPortIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthStatusPortIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthStatusPortIndx.setDescription('The index of the port on the board. This corresponds to the index of the last manageable port on the board if the index is greater than zero. A zero index is a wild card.')
s5SbsAuthStatusMACIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsAuthStatusMACIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsAuthStatusMACIndx.setDescription('The index of MAC address on the port. This corresponds to the index of the MAC address on the port if the index is greater than zero. A zero index is a wild card.')
s5SbsCurrentAccessCtrlType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allow", 1), ("block", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrentAccessCtrlType.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrentAccessCtrlType.setDescription('This Node Access Control Type represents whether the node entry is node allowed or node blocked type.')
s5SbsCurrentActionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noAction", 1), ("partitionPort", 2), ("partitionPortAndsendTrap", 3), ("daFiltering", 4), ("daFilteringAndsendTrap", 5), ("sendTrap", 6), ("partitionPortAnddaFiltering", 7), ("partitionPortdaFilteringAndsendTrap", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrentActionMode.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrentActionMode.setDescription('An integer value representing the type of information contained in this s5SbsAuthStatusEntry. noAction(1) represents that port does not have any security assigned or the security is turned off. partitionPort(2) represents port is partitioned. partitionPortAndsendTrap(3) represents port is partitioned and a trap will be sent to trap receive station(s). daFiltering(4) represents port will filter out the frames with the desitnation address field is the MAC address of unauthorized station. daFilteringAndsendTrap(5) represents port will filter out the frames with the desitnation address field is the MAC address of unauthorized station and a trap will be sent to trap receive station(s). sendtrap(6) represents a trap will be sent to trap receive station(s). partitionPortAnddaFiltering(7) represents port is partitioned and port will filter out the frames with the destination address field is the MAC address of unauthorized station. partitionPortdaFilteringAndsendTrap(8) represents port is partitioned, port will filter out the frames with the destination address field is the MAC address of unauthorized station and a trap will be sent to trap receive station(s).')
s5SbsCurrentPortSecurStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("portSecure", 2), ("portPartition", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrentPortSecurStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrentPortSecurStatus.setDescription('This represents the current port security status. If s5SbsSecurityStatus is disable, notApplicable(1) will be returned. The port in a normal situation returns the status with portSecure(2). portPartition(3) will be returned only if the port is partitioned.')
s5SbsViolationStatusTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12), )
if mibBuilder.loadTexts: s5SbsViolationStatusTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsViolationStatusTable.setDescription('A table containing a list of boards, ports where network access violations have occurred. Information also contains the offending MAC addrersses.')
s5SbsViolationStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"))
if mibBuilder.loadTexts: s5SbsViolationStatusEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsViolationStatusEntry.setDescription('An entry in this table ')
s5SbsViolationStatusBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsViolationStatusBrdIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsViolationStatusBrdIndx.setDescription('The index of the board. This corresponds to the slot containing the board. This index will be 1 where it is not applicable, e.g., ByaStack 303/304.')
s5SbsViolationStatusPortIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsViolationStatusPortIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsViolationStatusPortIndx.setDescription('The index of the port on the board. This corresponds to the port on which a security violation was seen.')
s5SbsViolationStatusMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 12, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsViolationStatusMACAddress.setStatus('current')
if mibBuilder.loadTexts: s5SbsViolationStatusMACAddress.setDescription('The MAC address of the device attempting unauthorized network access. (MAC addrees-based security)')
s5SbsMgmViolationType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snmp", 1), ("web", 2), ("telnet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMgmViolationType.setStatus('current')
if mibBuilder.loadTexts: s5SbsMgmViolationType.setDescription('Type of management access attempted when the violation occurred.')
s5SbsMgmViolationIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMgmViolationIpAddress.setStatus('current')
if mibBuilder.loadTexts: s5SbsMgmViolationIpAddress.setDescription('IP Address of the station attempting unauthorized management access.')
s5SbsPortSecurityStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 15), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsPortSecurityStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsPortSecurityStatus.setDescription('The set of ports for which security is enabled. The bitwise AND of s5SbsPortSecurityStatus and s5SbsPortLearnStatus must be the empty set.')
s5SbsPortLearnStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 16), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsPortLearnStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsPortLearnStatus.setDescription("The set of ports for which auto learning is enabled. Note that a port's bit in this object may not be turned on if the port's value of s5SbsAutoLearningConfigEnabled is true(1).")
s5SbsCurrSecurityLists = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsCurrSecurityLists.setStatus('current')
if mibBuilder.loadTexts: s5SbsCurrSecurityLists.setDescription('The current number of entries of the Security lists in the s5SbsSecurityListTable.')
s5SbsMaxSecurityLists = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMaxSecurityLists.setStatus('current')
if mibBuilder.loadTexts: s5SbsMaxSecurityLists.setDescription('The maximum number of entries of the Security lists in the s5SbsSecurityListTable.')
s5SbsSecurityListTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19), )
if mibBuilder.loadTexts: s5SbsSecurityListTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityListTable.setDescription('A table containing a list of Security port lists.')
s5SbsSecurityListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsSecurityListIndx"))
if mibBuilder.loadTexts: s5SbsSecurityListEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityListEntry.setDescription('An entry in this table ')
s5SbsSecurityListIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsSecurityListIndx.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityListIndx.setDescription('The index of the security list. This corresponds to the Security port list which can be used as index into s5SbsAuthCfgTable. ')
s5SbsSecurityListMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 2), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityListMembers.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityListMembers.setDescription('The set of ports that are currently members in this Port list.')
s5SbsSecurityListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 19, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("create", 2), ("delete", 3), ("modify", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityListStatus.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityListStatus.setDescription('The status of the SecurityList entry. The primary use of this object is for modifying the SecurityList table. Values that can be written create(2), delete(3), modify(4). Values that can be read: valid(1). Setting this entry to delete(3) causes the entry to be deleted from the table. Setting a new entry with create(2) causes the entry to be created in the table. Setting an entry with modify(4) causes the entry to be modified. The response to a get request or get-next request will always indicate a status of valid (1), since invalid entries are removed from the table. ')
s5SbsMacViolation = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20))
s5SbsMacViolationClear = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsMacViolationClear.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationClear.setDescription('This object is used to clear all entries in the s5SbsMacViolationTable. Setting it to clear(2) will clear all entries in that table. Setting it to other(1) has no effect. This object always returns a value of other(1).')
s5SbsMacViolationTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2), )
if mibBuilder.loadTexts: s5SbsMacViolationTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationTable.setDescription('A table containing a list of Security port lists.')
s5SbsMacViolationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsMacViolationAddress"))
if mibBuilder.loadTexts: s5SbsMacViolationEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationEntry.setDescription('An entry in this table ')
s5SbsMacViolationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMacViolationAddress.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationAddress.setDescription('The MAC address that caused an access violation.')
s5SbsMacViolationBrd = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMacViolationBrd.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationBrd.setDescription('The last board/slot/unit number on which the MAC address caused an access violation.')
s5SbsMacViolationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 20, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5SbsMacViolationPort.setStatus('current')
if mibBuilder.loadTexts: s5SbsMacViolationPort.setDescription('The last port number on which the MAC address caused an access violation.')
s5SbsAutoLearningAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAutoLearningAgingTime.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningAgingTime.setDescription('The lifetime for MAC addresses which are auto-learned. This is measured in minutes. A value of 0 means addresses are not aged out.')
s5SbsAutoLearningConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22), )
if mibBuilder.loadTexts: s5SbsAutoLearningConfigTable.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigTable.setDescription('A table containing per-port configuration for auto-learning. Entries exist in the table for each ethernet port in the system.')
s5SbsAutoLearningConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1), ).setIndexNames((0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAutoLearningConfigBrd"), (0, "S5-SWITCH-BAYSECURE-MIB", "s5SbsAutoLearningConfigPort"))
if mibBuilder.loadTexts: s5SbsAutoLearningConfigEntry.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigEntry.setDescription('An entry in this table ')
s5SbsAutoLearningConfigBrd = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: s5SbsAutoLearningConfigBrd.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigBrd.setDescription('The board/slot/unit number.')
s5SbsAutoLearningConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: s5SbsAutoLearningConfigPort.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigPort.setDescription('The port number.')
s5SbsAutoLearningConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAutoLearningConfigEnabled.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigEnabled.setDescription("This object indicates whether auto-learning is enabled on the port. Note that this object may not be set to true(1) for a port whose bit is turned on in s5SbsPortLearnStatus. Likewise, a port's bit in s5SbsPortLearnStatus may not be turned on if the port's value of s5SbsAutoLearningConfigEnabled is true(1). Note that if this object is changed from true(1) to false(2), all auto-learned MAC addresses for the port will be removed.")
s5SbsAutoLearningConfigMaxMacs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAutoLearningConfigMaxMacs.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningConfigMaxMacs.setDescription('This object indicates the maximum number of MAC addresses that may be learned on the port.')
s5SbsAutoLearningPorts = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 23), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAutoLearningPorts.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningPorts.setDescription('This object specifies the set of ports for which auto- learning is enabled. It is an alternative to s5SbsAutoLearningConfigEnabled.')
s5SbsAutoLearningSticky = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 24), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsAutoLearningSticky.setStatus('current')
if mibBuilder.loadTexts: s5SbsAutoLearningSticky.setDescription("This object controls whether the 'sticky-mac' feature is enabled.")
s5SbsSecurityLockoutPortList = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 5, 3, 25), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5SbsSecurityLockoutPortList.setStatus('current')
if mibBuilder.loadTexts: s5SbsSecurityLockoutPortList.setDescription('This object controls the set of ports that are locked such that they cannot have mac-security enabled.')
mibBuilder.exportSymbols("S5-SWITCH-BAYSECURE-MIB", s5SbsSecurityListMembers=s5SbsSecurityListMembers, s5SbsAutoLearningAgingTime=s5SbsAutoLearningAgingTime, s5SbsAuthCfgTrunk=s5SbsAuthCfgTrunk, s5SbsAuthStatusPortIndx=s5SbsAuthStatusPortIndx, s5SbsSecurityLockoutPortList=s5SbsSecurityLockoutPortList, PYSNMP_MODULE_ID=s5SbsAuth, s5SbsAuthCfgSource=s5SbsAuthCfgSource, s5SbsMaxNodesAllowed=s5SbsMaxNodesAllowed, s5SbsAuthCfgAccessCtrlType=s5SbsAuthCfgAccessCtrlType, s5SbsAuthStatusTable=s5SbsAuthStatusTable, s5SbsAuth=s5SbsAuth, s5SbsCurrentAccessCtrlType=s5SbsCurrentAccessCtrlType, s5SbsSecurityListStatus=s5SbsSecurityListStatus, s5SbsAuthCfgBrdIndx=s5SbsAuthCfgBrdIndx, s5SbsMacViolationClear=s5SbsMacViolationClear, s5SbsAutoLearningConfigBrd=s5SbsAutoLearningConfigBrd, s5SbsAuthCfgTable=s5SbsAuthCfgTable, s5SbsAuthStatusBrdIndx=s5SbsAuthStatusBrdIndx, s5SbsMaxNodesBlocked=s5SbsMaxNodesBlocked, s5SbsSecurityStatus=s5SbsSecurityStatus, s5SbsAuthCtlPartTime=s5SbsAuthCtlPartTime, s5SbsSecurityListEntry=s5SbsSecurityListEntry, s5SbsMacViolationPort=s5SbsMacViolationPort, s5SbsAutoLearningConfigTable=s5SbsAutoLearningConfigTable, s5SbsAutoLearningConfigEnabled=s5SbsAutoLearningConfigEnabled, s5SbsAuthStatusEntry=s5SbsAuthStatusEntry, s5SbsMgmViolationIpAddress=s5SbsMgmViolationIpAddress, s5SbsCurrentPortSecurStatus=s5SbsCurrentPortSecurStatus, s5SbsViolationStatusEntry=s5SbsViolationStatusEntry, s5SbsPortLearnStatus=s5SbsPortLearnStatus, s5SbsSecurityListIndx=s5SbsSecurityListIndx, s5SbsMacViolationBrd=s5SbsMacViolationBrd, s5SbsAutoLearningPorts=s5SbsAutoLearningPorts, s5SbsCurrSecurityLists=s5SbsCurrSecurityLists, s5SbsMacViolationEntry=s5SbsMacViolationEntry, s5SbsAuthStatusMACIndx=s5SbsAuthStatusMACIndx, s5SbsMgmViolationType=s5SbsMgmViolationType, s5SbsMaxSecurityLists=s5SbsMaxSecurityLists, s5SbsViolationStatusTable=s5SbsViolationStatusTable, s5SbsAuthCfgSecureList=s5SbsAuthCfgSecureList, s5SbsAuthCfgLifetime=s5SbsAuthCfgLifetime, s5SbsViolationStatusBrdIndx=s5SbsViolationStatusBrdIndx, s5SbsMacViolationAddress=s5SbsMacViolationAddress, PortSet=PortSet, s5SbsCurrentActionMode=s5SbsCurrentActionMode, s5SbsAuthCfgEntry=s5SbsAuthCfgEntry, s5SbsCurrNodesAllowed=s5SbsCurrNodesAllowed, s5SbsMacViolation=s5SbsMacViolation, s5SbsSecurityListTable=s5SbsSecurityListTable, s5SbsMacViolationTable=s5SbsMacViolationTable, s5SbsAutoLearningConfigMaxMacs=s5SbsAutoLearningConfigMaxMacs, s5SbsAuthCfgPortIndx=s5SbsAuthCfgPortIndx, s5SbsAuthSecurityLock=s5SbsAuthSecurityLock, s5SbsAuthCfgMACIndx=s5SbsAuthCfgMACIndx, s5SbsAutoLearningConfigEntry=s5SbsAutoLearningConfigEntry, s5SbsViolationStatusPortIndx=s5SbsViolationStatusPortIndx, s5SbsSecurityMode=s5SbsSecurityMode, s5SbsSecurityAction=s5SbsSecurityAction, s5SbsAuthCfgStatus=s5SbsAuthCfgStatus, s5SbsAutoLearningSticky=s5SbsAutoLearningSticky, s5SbsPortSecurityStatus=s5SbsPortSecurityStatus, s5SbsAutoLearningConfigPort=s5SbsAutoLearningConfigPort, s5SbsViolationStatusMACAddress=s5SbsViolationStatusMACAddress, s5SbsCurrNodesBlocked=s5SbsCurrNodesBlocked)
