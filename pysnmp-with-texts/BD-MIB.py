#
# PySNMP MIB module BD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
fcSwitch, bcsiModules = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch", "bcsiModules")
SwPortIndex, = mibBuilder.importSymbols("Brocade-TC", "SwPortIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, Integer32, NotificationType, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, Counter64, Gauge32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Integer32", "NotificationType", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
swVfId, = mibBuilder.importSymbols("SW-MIB", "swVfId")
bd = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51))
if mibBuilder.loadTexts: bd.setLastUpdated('200907281830Z')
if mibBuilder.loadTexts: bd.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: bd.setContactInfo('Customer Support Group Brocade Communications Systems, 1745 Technology Drive, San Jose, CA 95110 U.S.A Tel: +1-408-392-6061 Fax: +1-408-392-6656 Email: support@Brocade.COM WEB: www.brocade.com')
if mibBuilder.loadTexts: bd.setDescription("The MIB module is for Brocade's Bottleneck detection feature.Copyright (c) 1996-2003 Brocade Communications Systems, Inc. All rights reserved.")
class BdType(TextualConvention, Integer32):
    description = 'BD type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("congestion", 1), ("latency", 2))

bdTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0))
if mibBuilder.loadTexts: bdTraps.setStatus('current')
if mibBuilder.loadTexts: bdTraps.setDescription('The OID represents the BD Traps.')
bdConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1))
if mibBuilder.loadTexts: bdConfig.setStatus('current')
if mibBuilder.loadTexts: bdConfig.setDescription('The OID represents the BD config.')
bdStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2))
if mibBuilder.loadTexts: bdStats.setStatus('current')
if mibBuilder.loadTexts: bdStats.setDescription('This OID represents the BD stats.')
bdStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdStatus.setStatus('current')
if mibBuilder.loadTexts: bdStatus.setDescription('This object gives the status of bottleneck detection feature if enabled in the switch. The value of this OID if true(1) or false(2).')
bdLThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdLThreshold.setStatus('current')
if mibBuilder.loadTexts: bdLThreshold.setDescription('This object is the severity threshold for latency bottleneck. This threshold indicates the percentage of one-second intervals affected by latency conditions within a specified time window. The value of this OID is between 0 and 1.')
bdCThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdCThreshold.setStatus('current')
if mibBuilder.loadTexts: bdCThreshold.setDescription('This object is the severity threshold for congestion bottleneck. This threshold indicates the percentage of one-second intervals affected by congestion conditions within a specified time window. The value of this OID is between 0 and 1')
bdQTime = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdQTime.setStatus('current')
if mibBuilder.loadTexts: bdQTime.setDescription('The minimum number of seconds between consecutive alerts. The value assigned to this parameter applies to both latency and congestion monitoring. In this duration, there will not be any traps sent.')
bdWinAvgTime = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdWinAvgTime.setStatus('current')
if mibBuilder.loadTexts: bdWinAvgTime.setDescription('The time window in seconds over which the percentage of seconds affected by bottleneck conditions is computed and compared with the threshold.')
bdThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bdThreshold.setStatus('current')
if mibBuilder.loadTexts: bdThreshold.setDescription('This is the severity threshold for latency or congestion bottleneck. This is accessible only for traps. This object is one of the variable binding in bdTrap and bdClearTrap.')
nBdType = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 7), BdType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nBdType.setStatus('current')
if mibBuilder.loadTexts: nBdType.setDescription('This is the type of bottleneck.This is accessible only for traps. This object is one of the variable binding in bdTrap and bdClearTrap. This can have a value of congestion(1) or latency(2).')
bdNumOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdNumOfEntries.setStatus('current')
if mibBuilder.loadTexts: bdNumOfEntries.setDescription('Number of rows in the stats table.')
bdStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2), )
if mibBuilder.loadTexts: bdStatsTable.setStatus('current')
if mibBuilder.loadTexts: bdStatsTable.setDescription('The table of stats entries represents both types of bottleneck. Each sample in the stats is taken every 10 seconds.The maximum number of entries for each port, each type [congestion/latency] is 30.')
bdStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1), ).setIndexNames((0, "BD-MIB", "userPortNumber"), (0, "BD-MIB", "bdType"), (0, "BD-MIB", "bdSampleTime"))
if mibBuilder.loadTexts: bdStatsEntry.setStatus('current')
if mibBuilder.loadTexts: bdStatsEntry.setDescription('An entry of BD stats information.')
userPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 1), SwPortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userPortNumber.setStatus('current')
if mibBuilder.loadTexts: userPortNumber.setDescription('This object represents the user port indices of bottleneck monitored ports like F-port, E-port, L-port, FCOE-port.')
bdSampleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdSampleTime.setStatus('current')
if mibBuilder.loadTexts: bdSampleTime.setDescription('This object represents the sample time in Unix time format. Ex:1265259069 The above Unix time is equal to Thu, 04 Feb 2010 04:51:09 GMT .')
bdType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 3), BdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdType.setStatus('current')
if mibBuilder.loadTexts: bdType.setDescription('This object represents the bottleneck type. The value of this object can be congestion(1) or latency(2).')
bdStatsValue10SecsSample = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdStatsValue10SecsSample.setStatus('current')
if mibBuilder.loadTexts: bdStatsValue10SecsSample.setDescription('This sample is average of 10 samples collected every second. If the sample has not been taken yet then bdStatsValue10SecsSample return -1.')
bdStatsValue60SecsSample = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdStatsValue60SecsSample.setStatus('current')
if mibBuilder.loadTexts: bdStatsValue60SecsSample.setDescription('This sample is average of 60 samples collected every second. If the sample has not been taken yet then bdStatsValue60SecsSample return -1.')
bdStatsValue300SecsSample = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdStatsValue300SecsSample.setStatus('current')
if mibBuilder.loadTexts: bdStatsValue300SecsSample.setDescription('This sample is average of 300 samples collected every second. If the sample has not been taken yet then bdStatsValue300SecsSample return -1.')
bdAggrStats = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bdAggrStats.setStatus('current')
if mibBuilder.loadTexts: bdAggrStats.setDescription('This object represents the aggregrate stats value. This value is the sum of all the samples divided by average window and multiplied by 100.This is accessible only for traps. This obejct is one of the variable binding in bdTrap and bdClearTrap.')
bdAbsoluteValue = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bdAbsoluteValue.setStatus('current')
if mibBuilder.loadTexts: bdAbsoluteValue.setDescription('This object represents the absolute value of bdAggrStats. It is the number of affected seconds. This object is accessible only for traps and it is one of the variable binding in bdTrap and bdClearTrap.')
bdAvgFrameSize = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bdAvgFrameSize.setStatus('current')
if mibBuilder.loadTexts: bdAvgFrameSize.setDescription('This object represents the average size in bytes of all frames that were transmitted on the ports during the averaging window. This object is accessible only for traps and it is one of the variable binding in bdTrap and bdClearTrap.')
bdTrap = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0, 1)).setObjects(("BD-MIB", "userPortNumber"), ("BD-MIB", "bdWinAvgTime"), ("BD-MIB", "nBdType"), ("BD-MIB", "bdThreshold"), ("BD-MIB", "bdAggrStats"), ("BD-MIB", "bdAbsoluteValue"), ("SW-MIB", "swVfId"), ("BD-MIB", "bdAvgFrameSize"))
if mibBuilder.loadTexts: bdTrap.setStatus('current')
if mibBuilder.loadTexts: bdTrap.setDescription('trap to be send for bottleneck detection.')
bdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0, 2)).setObjects(("BD-MIB", "userPortNumber"), ("BD-MIB", "bdWinAvgTime"), ("BD-MIB", "nBdType"), ("BD-MIB", "bdThreshold"), ("BD-MIB", "bdAggrStats"), ("BD-MIB", "bdAbsoluteValue"), ("SW-MIB", "swVfId"), ("BD-MIB", "bdAvgFrameSize"))
if mibBuilder.loadTexts: bdClearTrap.setStatus('current')
if mibBuilder.loadTexts: bdClearTrap.setDescription('trap to be send for bottleneck clearance.')
mibBuilder.exportSymbols("BD-MIB", bd=bd, bdStatsValue60SecsSample=bdStatsValue60SecsSample, bdStatsTable=bdStatsTable, bdWinAvgTime=bdWinAvgTime, BdType=BdType, bdStatsValue10SecsSample=bdStatsValue10SecsSample, userPortNumber=userPortNumber, PYSNMP_MODULE_ID=bd, bdNumOfEntries=bdNumOfEntries, bdClearTrap=bdClearTrap, bdAggrStats=bdAggrStats, bdThreshold=bdThreshold, bdLThreshold=bdLThreshold, bdSampleTime=bdSampleTime, bdAvgFrameSize=bdAvgFrameSize, bdType=bdType, bdStatus=bdStatus, bdStatsValue300SecsSample=bdStatsValue300SecsSample, bdAbsoluteValue=bdAbsoluteValue, bdTrap=bdTrap, bdConfig=bdConfig, bdStats=bdStats, bdTraps=bdTraps, bdQTime=bdQTime, nBdType=nBdType, bdStatsEntry=bdStatsEntry, bdCThreshold=bdCThreshold)
