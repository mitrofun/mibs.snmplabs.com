#
# PySNMP MIB module CPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dialaccess, = mibBuilder.importSymbols("CPM-NORTEL-MIB", "dialaccess")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Bits, IpAddress, Counter64, NotificationType, ModuleIdentity, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpm = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3))
if mibBuilder.loadTexts: cpm.setLastUpdated('0002170000Z')
if mibBuilder.loadTexts: cpm.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: cpm.setContactInfo(' Jim Wimberley Nortel Networks 3500 Carling Avenue Nepean, Ontario, Canada K2H 8E9 phone: 613-765-2582 email: rrjames@nortelnetworks.com')
if mibBuilder.loadTexts: cpm.setDescription('CVX Policy Manager MIB')
cpm_conf = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3, 1)).setLabel("cpm-conf")
if mibBuilder.loadTexts: cpm_conf.setStatus('current')
if mibBuilder.loadTexts: cpm_conf.setDescription('Sub-tree for configuration objects')
cpm_performance = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3, 2)).setLabel("cpm-performance")
if mibBuilder.loadTexts: cpm_performance.setStatus('current')
if mibBuilder.loadTexts: cpm_performance.setDescription('Sub-tree for performance and operational metrics objects')
cpm_surv = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3, 3)).setLabel("cpm-surv")
if mibBuilder.loadTexts: cpm_surv.setStatus('current')
if mibBuilder.loadTexts: cpm_surv.setDescription('Sub-tree for surveillance related objects')
cpm_sysconf = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1)).setLabel("cpm-sysconf")
if mibBuilder.loadTexts: cpm_sysconf.setStatus('current')
if mibBuilder.loadTexts: cpm_sysconf.setDescription('sub-tree for cpm system related objects')
sysAbsStartTime = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAbsStartTime.setStatus('current')
if mibBuilder.loadTexts: sysAbsStartTime.setDescription('time of last system startup in seconds since epoch (Jan 1, 1970 GMT)')
sysMibRevision = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMibRevision.setStatus('current')
if mibBuilder.loadTexts: sysMibRevision.setDescription('major and minor version number of MIB (vX.X)')
sysSoftwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareRevision.setStatus('current')
if mibBuilder.loadTexts: sysSoftwareRevision.setDescription('major and minor version number of cpm software (vX.X)')
sysConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysConfigFile.setStatus('current')
if mibBuilder.loadTexts: sysConfigFile.setDescription('current configuration file name')
sysLogFile = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLogFile.setStatus('current')
if mibBuilder.loadTexts: sysLogFile.setDescription('current log file')
sysLogFileMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLogFileMaxSize.setStatus('current')
if mibBuilder.loadTexts: sysLogFileMaxSize.setDescription('max number of lines in log file')
sysTraceLevel = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTraceLevel.setStatus('current')
if mibBuilder.loadTexts: sysTraceLevel.setDescription('current logging/trace level')
sysOperationalState = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("initializing", 0), ("discovering", 1), ("ready", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysOperationalState.setStatus('current')
if mibBuilder.loadTexts: sysOperationalState.setDescription('current operating state of CPM')
cpmVpopOMTable = MibTable((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1), )
if mibBuilder.loadTexts: cpmVpopOMTable.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMTable.setDescription('table of current OMs, per VPOP')
cpmVpopOMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1), ).setIndexNames((0, "CPM-MIB", "cpmVpopOMVpopId"))
if mibBuilder.loadTexts: cpmVpopOMEntry.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMEntry.setDescription('a VPOP entry in the table of current OMs')
cpmVpopOMVpopId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMVpopId.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMVpopId.setDescription('a unique number that identifies the VPOP')
cpmVpopOMPortLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMPortLimit.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMPortLimit.setDescription('(by VPOP) the current portlimit')
cpmVpopOMOverflowPortLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMOverflowPortLimit.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMOverflowPortLimit.setDescription('(by VPOP) the current overflow portlimit')
cpmVpopOMActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMActiveCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMActiveCalls.setDescription('(by VPOP) the current number of active calls')
cpmVpopOMActivePortLimitCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMActivePortLimitCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMActivePortLimitCalls.setDescription('(by VPOP) the current number of active port limit calls')
cpmVpopOMAcceptedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMAcceptedCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMAcceptedCalls.setDescription('(by VPOP) the total number of calls accepted during the uptime of this CPM server')
cpmVpopOMAcceptedOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMAcceptedOverflowCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMAcceptedOverflowCalls.setDescription('(by VPOP) the total number of calls accepted as overflow calls during the uptime of this CPM server')
cpmVpopOMReleasedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMReleasedCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMReleasedCalls.setDescription('(by VPOP) the total number of released calls during the uptime of this CPM server')
cpmVpopOMPortLimitReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMPortLimitReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMPortLimitReject.setDescription('(by VPOP) the total number of call attempts that were rejected by the portlimit during the uptime of this server')
cpmVpopOMOverflowPortLimitReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMOverflowPortLimitReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMOverflowPortLimitReject.setDescription('(by VPOP) the total number of call attempts that were rejected by the overflow portlimit during the uptime of this server')
cpmVpopOMClidFilterReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMClidFilterReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMClidFilterReject.setDescription('(by VPOP) the total number of call attempts that were rejected by CLID filters during the uptime of this server')
cpmVpopOMProxyReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMProxyReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMProxyReject.setDescription('N/A')
cpmVpopOMIPAddressReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMIPAddressReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMIPAddressReject.setDescription('(by VPOP) the total number of call attempts that were rejected during the uptime of this server because CPM was unable to assign an IP Address')
cpmVpopOMGatewayReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMGatewayReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMGatewayReject.setDescription('(by VPOP) the total number of call attempts that were rejected during the uptime of this server because CPM was unable to assign a call to a gateway (or LNS)')
cpmVpopOMGuaranteeReject = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMGuaranteeReject.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMGuaranteeReject.setDescription('(by VPOP) the total number of call attempts that were rejected by the port guarantees.')
cpmVpopOMSnapshotTable = MibTable((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2), )
if mibBuilder.loadTexts: cpmVpopOMSnapshotTable.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotTable.setDescription('a table of OM snapshots per VPOP')
cpmVpopOMSnapshotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1), ).setIndexNames((0, "CPM-MIB", "cpmVpopOMSnapshotVpopId"), (0, "CPM-MIB", "cpmVpopOMSnapshotTimeStamp"))
if mibBuilder.loadTexts: cpmVpopOMSnapshotEntry.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotEntry.setDescription('an entry in the table of OM snapshots per VPOP')
cpmVpopOMSnapshotVpopId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMSnapshotVpopId.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotVpopId.setDescription('a unique number that identifies the VPOP')
cpmVpopOMSnapshotTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMSnapshotTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotTimeStamp.setDescription('the time of of the snapshot in seconds since epoch (Jan 1, 1970 GMT)')
cpmVpopOMSnapshotMinCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMSnapshotMinCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotMinCalls.setDescription('(by VPOP) the minimum number of active calls during reporting period')
cpmVpopOMSnapshotMaxCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmVpopOMSnapshotMaxCalls.setStatus('current')
if mibBuilder.loadTexts: cpmVpopOMSnapshotMaxCalls.setDescription('(by VPOP) the maximum number of active calls during reporting period')
cpmAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2), )
if mibBuilder.loadTexts: cpmAlarmTable.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTable.setDescription('a table of active traps')
cpmAlarmTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1), ).setIndexNames((0, "CPM-MIB", "cpmAlarmTableTrapGenNum"))
if mibBuilder.loadTexts: cpmAlarmTableEntry.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableEntry.setDescription('an entry in the table of alarms')
cpmAlarmTableTrapGenNum = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapGenNum.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapGenNum.setDescription('a unique number that identifies the trap')
cpmAlarmTableTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 6, 8, 10, 12, 14))).clone(namedValues=NamedValues(("nasNotResponding", 2), ("gatewayRemovedFromService", 4), ("gatewaysUnavailable", 6), ("mpGatewaysUnavailable", 8), ("ipAddressExhausted", 10), ("portsUnavailable", 12), ("overflowPortsInUse", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapType.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapType.setDescription('type of the trap')
cpmAlarmTableTrapSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4))).clone(namedValues=NamedValues(("warning", 1), ("critical", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapSeverity.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapSeverity.setDescription('severity of the trap')
cpmAlarmTableTrapTimeTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapTimeTicks.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapTimeTicks.setDescription('the time that the trap was raised')
cpmAlarmTableTrapArg1 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapArg1.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapArg1.setDescription('trap raise arguement')
cpmAlarmTableTrapArg2 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapArg2.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapArg2.setDescription('trap raise arguement')
cpmAlarmTableTrapArg3 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmAlarmTableTrapArg3.setStatus('current')
if mibBuilder.loadTexts: cpmAlarmTableTrapArg3.setDescription('trap raise arguement')
cpm_trapVariables = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1)).setLabel("cpm-trapVariables")
if mibBuilder.loadTexts: cpm_trapVariables.setStatus('current')
if mibBuilder.loadTexts: cpm_trapVariables.setDescription('The subtree of information related to Traps')
trap_severity = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 0), ("warning", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setLabel("trap-severity")
if mibBuilder.loadTexts: trap_severity.setStatus('current')
if mibBuilder.loadTexts: trap_severity.setDescription('The trap severity.')
trap_nasIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 2), IpAddress()).setLabel("trap-nasIPAddress")
if mibBuilder.loadTexts: trap_nasIPAddress.setStatus('current')
if mibBuilder.loadTexts: trap_nasIPAddress.setDescription('The ip address of a NAS.')
trap_gatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 3), IpAddress()).setLabel("trap-gatewayIPAddress")
if mibBuilder.loadTexts: trap_gatewayIPAddress.setStatus('current')
if mibBuilder.loadTexts: trap_gatewayIPAddress.setDescription('The ip address of a gateway.')
trap_vpopId = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 4), Integer32()).setLabel("trap-vpopId")
if mibBuilder.loadTexts: trap_vpopId.setStatus('current')
if mibBuilder.loadTexts: trap_vpopId.setDescription('The VPOP id.')
trap_gennum = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 5), Integer32()).setLabel("trap-gennum")
if mibBuilder.loadTexts: trap_gennum.setStatus('current')
if mibBuilder.loadTexts: trap_gennum.setDescription('Unique identifier for the trap.')
trap_AAAServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 6), IpAddress()).setLabel("trap-AAAServerIPAddress")
if mibBuilder.loadTexts: trap_AAAServerIPAddress.setStatus('current')
if mibBuilder.loadTexts: trap_AAAServerIPAddress.setDescription('The ip address of a AAA server.')
cpmStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,1)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "sysOperationalState"))
if mibBuilder.loadTexts: cpmStateChangeTrap.setDescription('The Trap generated when CPM changes states.')
nasNotRespondingTrap = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,2)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_nasIPAddress"))
if mibBuilder.loadTexts: nasNotRespondingTrap.setDescription('The Trap generated when a nas stops responding.')
nasNowRespondingTrap = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,3)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_nasIPAddress"))
if mibBuilder.loadTexts: nasNowRespondingTrap.setDescription('The Trap generated when a nas starts responding.')
gatewayRemovedFromService = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,4)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_gatewayIPAddress"))
if mibBuilder.loadTexts: gatewayRemovedFromService.setDescription('The Trap generated when a gateway is removed from service.')
gatewayReturnedToService = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,5)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_gatewayIPAddress"))
if mibBuilder.loadTexts: gatewayReturnedToService.setDescription('The Trap generated when a gateway is returned to service.')
gatewaysUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,6)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: gatewaysUnavailable.setDescription('The Trap generated when a call is rejected because all gateways are at capacity or administratively locked.')
gatewaysAvailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,7)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: gatewaysAvailable.setDescription('The Trap generated when a call is accepted after the above trap was generated.')
mpGatewaysUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,8)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: mpGatewaysUnavailable.setDescription('The Trap generated when a call is rejected because all multilink PPP gateways are at capacity or administratively locked.')
mpGatewaysAvailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,9)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: mpGatewaysAvailable.setDescription('The Trap generated when a call is accepted after the above trap was generated.')
ipAddressesExhausted = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,10)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"), ("CPM-MIB", "trap_nasIPAddress"))
if mibBuilder.loadTexts: ipAddressesExhausted.setDescription('The Trap is generated when a call is rejected because an IP address could not be assigned from the available pools.')
ipAddressesAvailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,11)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"), ("CPM-MIB", "trap_nasIPAddress"))
if mibBuilder.loadTexts: ipAddressesAvailable.setDescription('The Trap generated when a call is accepted after the above trap was generated.')
portsUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,12)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: portsUnavailable.setDescription('The Trap generated when a call is rejected because all ports, including overflow, are used up.')
portsAvailable = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,13)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: portsAvailable.setDescription('The Trap generated when a call is accepted after the above trap was generated.')
overflowPortsInUse = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,14)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: overflowPortsInUse.setDescription('The trap generated when a call is accepted as an overflow port.')
overflowPortsNotInUse = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,15)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_vpopId"))
if mibBuilder.loadTexts: overflowPortsNotInUse.setDescription('The trap generated when a call is accepted not as an overflow after the above trap was generated.')
disconnectRequestDiscarded = NotificationType((1, 3, 6, 1, 4, 1, 562, 14, 3) + (0,16)).setObjects(("CPM-MIB", "trap_gennum"), ("CPM-MIB", "trap_severity"), ("CPM-MIB", "trap_AAAServerIPAddress"))
if mibBuilder.loadTexts: disconnectRequestDiscarded.setDescription('The trap generated when a RADIUS disconnect request is discarded.')
mibBuilder.exportSymbols("CPM-MIB", cpmAlarmTable=cpmAlarmTable, cpmVpopOMVpopId=cpmVpopOMVpopId, cpmVpopOMIPAddressReject=cpmVpopOMIPAddressReject, ipAddressesExhausted=ipAddressesExhausted, cpmVpopOMReleasedCalls=cpmVpopOMReleasedCalls, cpmVpopOMPortLimit=cpmVpopOMPortLimit, cpmVpopOMActivePortLimitCalls=cpmVpopOMActivePortLimitCalls, sysSoftwareRevision=sysSoftwareRevision, sysLogFileMaxSize=sysLogFileMaxSize, cpmAlarmTableTrapTimeTicks=cpmAlarmTableTrapTimeTicks, cpm_performance=cpm_performance, trap_gennum=trap_gennum, gatewayReturnedToService=gatewayReturnedToService, cpmVpopOMEntry=cpmVpopOMEntry, gatewaysUnavailable=gatewaysUnavailable, cpmVpopOMSnapshotVpopId=cpmVpopOMSnapshotVpopId, cpmVpopOMAcceptedOverflowCalls=cpmVpopOMAcceptedOverflowCalls, sysTraceLevel=sysTraceLevel, cpmAlarmTableTrapArg3=cpmAlarmTableTrapArg3, cpmAlarmTableTrapType=cpmAlarmTableTrapType, nasNowRespondingTrap=nasNowRespondingTrap, overflowPortsNotInUse=overflowPortsNotInUse, cpmAlarmTableTrapSeverity=cpmAlarmTableTrapSeverity, cpmVpopOMClidFilterReject=cpmVpopOMClidFilterReject, trap_gatewayIPAddress=trap_gatewayIPAddress, cpm_trapVariables=cpm_trapVariables, cpmVpopOMSnapshotEntry=cpmVpopOMSnapshotEntry, cpmVpopOMPortLimitReject=cpmVpopOMPortLimitReject, trap_nasIPAddress=trap_nasIPAddress, trap_vpopId=trap_vpopId, cpm=cpm, cpm_surv=cpm_surv, cpmVpopOMOverflowPortLimit=cpmVpopOMOverflowPortLimit, cpmVpopOMSnapshotMaxCalls=cpmVpopOMSnapshotMaxCalls, cpmAlarmTableEntry=cpmAlarmTableEntry, disconnectRequestDiscarded=disconnectRequestDiscarded, overflowPortsInUse=overflowPortsInUse, sysConfigFile=sysConfigFile, gatewaysAvailable=gatewaysAvailable, sysAbsStartTime=sysAbsStartTime, cpmVpopOMGuaranteeReject=cpmVpopOMGuaranteeReject, cpmVpopOMSnapshotTimeStamp=cpmVpopOMSnapshotTimeStamp, portsAvailable=portsAvailable, sysLogFile=sysLogFile, cpmVpopOMProxyReject=cpmVpopOMProxyReject, PYSNMP_MODULE_ID=cpm, sysOperationalState=sysOperationalState, cpmVpopOMSnapshotTable=cpmVpopOMSnapshotTable, trap_AAAServerIPAddress=trap_AAAServerIPAddress, cpmVpopOMAcceptedCalls=cpmVpopOMAcceptedCalls, mpGatewaysAvailable=mpGatewaysAvailable, cpm_sysconf=cpm_sysconf, ipAddressesAvailable=ipAddressesAvailable, cpmVpopOMTable=cpmVpopOMTable, portsUnavailable=portsUnavailable, nasNotRespondingTrap=nasNotRespondingTrap, sysMibRevision=sysMibRevision, cpmVpopOMActiveCalls=cpmVpopOMActiveCalls, mpGatewaysUnavailable=mpGatewaysUnavailable, gatewayRemovedFromService=gatewayRemovedFromService, cpmVpopOMGatewayReject=cpmVpopOMGatewayReject, cpmVpopOMOverflowPortLimitReject=cpmVpopOMOverflowPortLimitReject, cpmVpopOMSnapshotMinCalls=cpmVpopOMSnapshotMinCalls, cpmAlarmTableTrapArg2=cpmAlarmTableTrapArg2, cpmStateChangeTrap=cpmStateChangeTrap, cpmAlarmTableTrapArg1=cpmAlarmTableTrapArg1, trap_severity=trap_severity, cpm_conf=cpm_conf, cpmAlarmTableTrapGenNum=cpmAlarmTableTrapGenNum)