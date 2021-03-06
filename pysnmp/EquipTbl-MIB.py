#
# PySNMP MIB module EquipTbl-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EquipTbl-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:57:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
chrComHwNe, = mibBuilder.importSymbols("Chromatis-MIB", "chrComHwNe")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, IpAddress, NotificationType, Counter64, Gauge32, MibIdentifier, ObjectIdentity, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "Counter64", "Gauge32", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
chrComHwNeId = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeId.setStatus('current')
chrComHwNeType = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("metropolis2000", 1), ("metropolis2500", 2), ("metropolis4000", 3), ("metropolis4500", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeType.setStatus('current')
chrComHwNeRunningSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeRunningSwVersion.setStatus('current')
chrComHwNeAvailableSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeAvailableSwVersion.setStatus('current')
chrComHwNeNextSessionSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeNextSessionSwVersion.setStatus('current')
chrComHwNeRunningConfigurationSet = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeRunningConfigurationSet.setStatus('current')
chrComHwNeAvailableConfigurationSets = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeAvailableConfigurationSets.setStatus('current')
chrComHwNeNextSessionConfigurationSet = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeNextSessionConfigurationSet.setStatus('current')
chrComHwNeTimeofDay = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 9), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeTimeofDay.setStatus('current')
chrComHwNeDailyPMStartOfTime = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeDailyPMStartOfTime.setStatus('current')
chrComHwNeCriticalAlarmCounter = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeCriticalAlarmCounter.setStatus('current')
chrComHwNeMajorAlarmCounter = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeMajorAlarmCounter.setStatus('current')
chrComHwNeMinorAlarmCounter = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeMinorAlarmCounter.setStatus('current')
chrComHwNeDetectionFaultStabilizationTime = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeDetectionFaultStabilizationTime.setStatus('current')
chrComHwNeRemovalFaultStabilizationTime = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 150))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeRemovalFaultStabilizationTime.setStatus('current')
chrComHwNeAlarmCutOffStatus = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeAlarmCutOffStatus.setStatus('current')
chrComHwNeAtmfM4NeSuppressZeroStats = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeAtmfM4NeSuppressZeroStats.setStatus('current')
chrComHwNeResetPMCountersAction = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeResetPMCountersAction.setStatus('current')
chrComHwNeACOActivationAction = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeACOActivationAction.setStatus('current')
chrComHwNeAtmCbrRatesList = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeAtmCbrRatesList.setStatus('current')
chrComHwNeAtmRtVbrRatesList = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeAtmRtVbrRatesList.setStatus('current')
chrComHwNeMaxPathPM = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeMaxPathPM.setStatus('current')
chrComHwNeCurrentPathPM = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComHwNeCurrentPathPM.setStatus('current')
chrComHwNeGlobalSubnetID = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComHwNeGlobalSubnetID.setStatus('current')
mibBuilder.exportSymbols("EquipTbl-MIB", chrComHwNeAvailableSwVersion=chrComHwNeAvailableSwVersion, chrComHwNeRunningConfigurationSet=chrComHwNeRunningConfigurationSet, chrComHwNeAtmCbrRatesList=chrComHwNeAtmCbrRatesList, chrComHwNeAlarmCutOffStatus=chrComHwNeAlarmCutOffStatus, chrComHwNeResetPMCountersAction=chrComHwNeResetPMCountersAction, chrComHwNeAvailableConfigurationSets=chrComHwNeAvailableConfigurationSets, chrComHwNeType=chrComHwNeType, chrComHwNeId=chrComHwNeId, chrComHwNeAtmfM4NeSuppressZeroStats=chrComHwNeAtmfM4NeSuppressZeroStats, chrComHwNeACOActivationAction=chrComHwNeACOActivationAction, chrComHwNeCurrentPathPM=chrComHwNeCurrentPathPM, chrComHwNeRunningSwVersion=chrComHwNeRunningSwVersion, chrComHwNeGlobalSubnetID=chrComHwNeGlobalSubnetID, chrComHwNeMajorAlarmCounter=chrComHwNeMajorAlarmCounter, chrComHwNeRemovalFaultStabilizationTime=chrComHwNeRemovalFaultStabilizationTime, chrComHwNeAtmRtVbrRatesList=chrComHwNeAtmRtVbrRatesList, chrComHwNeNextSessionSwVersion=chrComHwNeNextSessionSwVersion, chrComHwNeCriticalAlarmCounter=chrComHwNeCriticalAlarmCounter, chrComHwNeMaxPathPM=chrComHwNeMaxPathPM, chrComHwNeDailyPMStartOfTime=chrComHwNeDailyPMStartOfTime, chrComHwNeTimeofDay=chrComHwNeTimeofDay, chrComHwNeMinorAlarmCounter=chrComHwNeMinorAlarmCounter, chrComHwNeNextSessionConfigurationSet=chrComHwNeNextSessionConfigurationSet, chrComHwNeDetectionFaultStabilizationTime=chrComHwNeDetectionFaultStabilizationTime)
