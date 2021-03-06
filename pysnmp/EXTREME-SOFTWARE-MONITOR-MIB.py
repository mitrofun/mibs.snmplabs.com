#
# PySNMP MIB module EXTREME-SOFTWARE-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-SOFTWARE-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:55:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, PortList = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "PortList")
extremeImageDescription, = mibBuilder.importSymbols("EXTREME-SYSTEM-MIB", "extremeImageDescription")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, TimeTicks, Counter32, NotificationType, IpAddress, Gauge32, Integer32, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Gauge32", "Integer32", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
extremeSwMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 32))
if mibBuilder.loadTexts: extremeSwMonitor.setLastUpdated('200402140000Z')
if mibBuilder.loadTexts: extremeSwMonitor.setOrganization('Extreme Networks, Inc.')
extremeSwMonitorCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1))
extremeSwMonitorMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2))
extremeSwMonitorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 3))
extremeServiceLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 4))
extremeTrialLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 5))
extremeSwMonitorNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0))
extremeCpuMonitorInterval = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorInterval.setStatus('current')
extremeCpuMonitorTotalUtilization = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorTotalUtilization.setStatus('current')
extremeCpuMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3), )
if mibBuilder.loadTexts: extremeCpuMonitorTable.setStatus('current')
extremeCpuMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1), ).setIndexNames((0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSlotId"), (1, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorProcessName"))
if mibBuilder.loadTexts: extremeCpuMonitorEntry.setStatus('current')
extremeCpuMonitorSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSlotId.setStatus('current')
extremeCpuMonitorProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: extremeCpuMonitorProcessName.setStatus('current')
extremeCpuMonitorProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorProcessId.setStatus('current')
extremeCpuMonitorProcessState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorProcessState.setStatus('current')
extremeCpuMonitorUtilization5secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization5secs.setStatus('current')
extremeCpuMonitorUtilization10secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization10secs.setStatus('current')
extremeCpuMonitorUtilization30secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization30secs.setStatus('current')
extremeCpuMonitorUtilization1min = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization1min.setStatus('current')
extremeCpuMonitorUtilization5mins = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization5mins.setStatus('current')
extremeCpuMonitorUtilization30mins = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization30mins.setStatus('current')
extremeCpuMonitorUtilization1hour = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUtilization1hour.setStatus('current')
extremeCpuMonitorMaxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorMaxUtilization.setStatus('current')
extremeCpuMonitorUserTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorUserTime.setStatus('current')
extremeCpuMonitorSystemTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemTime.setStatus('current')
extremeCpuMonitorSystemTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4), )
if mibBuilder.loadTexts: extremeCpuMonitorSystemTable.setStatus('current')
extremeCpuMonitorSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1), ).setIndexNames((0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSystemSlotId"))
if mibBuilder.loadTexts: extremeCpuMonitorSystemEntry.setStatus('current')
extremeCpuMonitorSystemSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemSlotId.setStatus('current')
extremeCpuMonitorSystemUtilization5secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization5secs.setStatus('current')
extremeCpuMonitorSystemUtilization10secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization10secs.setStatus('current')
extremeCpuMonitorSystemUtilization30secs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization30secs.setStatus('current')
extremeCpuMonitorSystemUtilization1min = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization1min.setStatus('current')
extremeCpuMonitorSystemUtilization5mins = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization5mins.setStatus('current')
extremeCpuMonitorSystemUtilization30mins = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization30mins.setStatus('current')
extremeCpuMonitorSystemUtilization1hour = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemUtilization1hour.setStatus('current')
extremeCpuMonitorSystemMaxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeCpuMonitorSystemMaxUtilization.setStatus('current')
extremeMemoryMonitorSystemTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2), )
if mibBuilder.loadTexts: extremeMemoryMonitorSystemTable.setStatus('current')
extremeMemoryMonitorSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1), ).setIndexNames((0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorSystemSlotId"))
if mibBuilder.loadTexts: extremeMemoryMonitorSystemEntry.setStatus('current')
extremeMemoryMonitorSystemSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorSystemSlotId.setStatus('current')
extremeMemoryMonitorSystemTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorSystemTotal.setStatus('current')
extremeMemoryMonitorSystemFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorSystemFree.setStatus('current')
extremeMemoryMonitorSystemUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorSystemUsage.setStatus('current')
extremeMemoryMonitorUserUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorUserUsage.setStatus('current')
extremeMemoryMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3), )
if mibBuilder.loadTexts: extremeMemoryMonitorTable.setStatus('current')
extremeMemoryMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1), ).setIndexNames((0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorSlotId"), (1, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorProcessName"))
if mibBuilder.loadTexts: extremeMemoryMonitorEntry.setStatus('current')
extremeMemoryMonitorSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorSlotId.setStatus('current')
extremeMemoryMonitorProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: extremeMemoryMonitorProcessName.setStatus('current')
extremeMemoryMonitorUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorUsage.setStatus('current')
extremeMemoryMonitorLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorLimit.setStatus('current')
extremeMemoryMonitorZone = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorZone.setStatus('current')
extremeMemoryMonitorGreenZoneCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorGreenZoneCount.setStatus('current')
extremeMemoryMonitorYellowZoneCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorYellowZoneCount.setStatus('current')
extremeMemoryMonitorOrangeZoneCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorOrangeZoneCount.setStatus('current')
extremeMemoryMonitorRedZoneCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorRedZoneCount.setStatus('current')
extremeMemoryMonitorGreenZoneThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorGreenZoneThreshold.setStatus('current')
extremeMemoryMonitorYellowZoneThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorYellowZoneThreshold.setStatus('current')
extremeMemoryMonitorOrangeZoneThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorOrangeZoneThreshold.setStatus('current')
extremeMemoryMonitorRedZoneThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeMemoryMonitorRedZoneThreshold.setStatus('current')
extremeCpuMonitorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeCpuMonitorThreshold.setStatus('current')
extremeCpuMonitorCurrentUtilization = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeCpuMonitorCurrentUtilization.setStatus('current')
extremeSwMonitorCpuUtilization = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 1)).setObjects(("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSlotId"), ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorProcessName"), ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorCurrentUtilization"), ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorThreshold"))
if mibBuilder.loadTexts: extremeSwMonitorCpuUtilization.setStatus('current')
extremeServiceLicenseExpiryDate = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeServiceLicenseExpiryDate.setStatus('current')
extremeServiceLicenseType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeServiceLicenseType.setStatus('current')
imageDescription = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: imageDescription.setStatus('current')
noOfDaysLeft = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 90))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: noOfDaysLeft.setStatus('current')
trialPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 32, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 90))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: trialPeriod.setStatus('current')
extremeServiceLicenseExpiration = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 2)).setObjects(("EXTREME-SOFTWARE-MONITOR-MIB", "extremeServiceLicenseExpiryDate"), ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeServiceLicenseType"), ("EXTREME-SOFTWARE-MONITOR-MIB", "imageDescription"), ("EXTREME-SOFTWARE-MONITOR-MIB", "noOfDaysLeft"))
if mibBuilder.loadTexts: extremeServiceLicenseExpiration.setStatus('current')
extremeTrialLicenseExpiration = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 3)).setObjects(("EXTREME-SOFTWARE-MONITOR-MIB", "trialPeriod"), ("EXTREME-SOFTWARE-MONITOR-MIB", "imageDescription"), ("EXTREME-SOFTWARE-MONITOR-MIB", "noOfDaysLeft"))
if mibBuilder.loadTexts: extremeTrialLicenseExpiration.setStatus('current')
mibBuilder.exportSymbols("EXTREME-SOFTWARE-MONITOR-MIB", extremeMemoryMonitorYellowZoneThreshold=extremeMemoryMonitorYellowZoneThreshold, extremeMemoryMonitorSystemTotal=extremeMemoryMonitorSystemTotal, extremeMemoryMonitorYellowZoneCount=extremeMemoryMonitorYellowZoneCount, extremeMemoryMonitorEntry=extremeMemoryMonitorEntry, extremeMemoryMonitorTable=extremeMemoryMonitorTable, extremeMemoryMonitorZone=extremeMemoryMonitorZone, extremeCpuMonitorSlotId=extremeCpuMonitorSlotId, extremeMemoryMonitorGreenZoneCount=extremeMemoryMonitorGreenZoneCount, extremeCpuMonitorSystemUtilization1min=extremeCpuMonitorSystemUtilization1min, extremeCpuMonitorTable=extremeCpuMonitorTable, extremeSwMonitorCpu=extremeSwMonitorCpu, extremeCpuMonitorSystemEntry=extremeCpuMonitorSystemEntry, extremeCpuMonitorSystemUtilization10secs=extremeCpuMonitorSystemUtilization10secs, extremeMemoryMonitorOrangeZoneCount=extremeMemoryMonitorOrangeZoneCount, extremeMemoryMonitorOrangeZoneThreshold=extremeMemoryMonitorOrangeZoneThreshold, extremeCpuMonitorProcessState=extremeCpuMonitorProcessState, noOfDaysLeft=noOfDaysLeft, extremeTrialLicenseExpiration=extremeTrialLicenseExpiration, extremeCpuMonitorSystemTable=extremeCpuMonitorSystemTable, extremeMemoryMonitorUserUsage=extremeMemoryMonitorUserUsage, imageDescription=imageDescription, extremeMemoryMonitorSystemSlotId=extremeMemoryMonitorSystemSlotId, extremeServiceLicenseExpiration=extremeServiceLicenseExpiration, extremeServiceLicenseExpiryDate=extremeServiceLicenseExpiryDate, extremeCpuMonitorUtilization30secs=extremeCpuMonitorUtilization30secs, extremeCpuMonitorUtilization5mins=extremeCpuMonitorUtilization5mins, extremeMemoryMonitorUsage=extremeMemoryMonitorUsage, extremeCpuMonitorUtilization30mins=extremeCpuMonitorUtilization30mins, extremeCpuMonitorSystemUtilization5secs=extremeCpuMonitorSystemUtilization5secs, extremeTrialLicense=extremeTrialLicense, extremeSwMonitorNotificationsPrefix=extremeSwMonitorNotificationsPrefix, extremeCpuMonitorInterval=extremeCpuMonitorInterval, extremeMemoryMonitorLimit=extremeMemoryMonitorLimit, extremeCpuMonitorSystemUtilization30mins=extremeCpuMonitorSystemUtilization30mins, extremeCpuMonitorTotalUtilization=extremeCpuMonitorTotalUtilization, extremeMemoryMonitorSystemFree=extremeMemoryMonitorSystemFree, extremeCpuMonitorProcessId=extremeCpuMonitorProcessId, extremeCpuMonitorProcessName=extremeCpuMonitorProcessName, extremeCpuMonitorUserTime=extremeCpuMonitorUserTime, extremeMemoryMonitorRedZoneThreshold=extremeMemoryMonitorRedZoneThreshold, extremeCpuMonitorCurrentUtilization=extremeCpuMonitorCurrentUtilization, extremeSwMonitorNotifications=extremeSwMonitorNotifications, extremeCpuMonitorSystemMaxUtilization=extremeCpuMonitorSystemMaxUtilization, extremeServiceLicenseType=extremeServiceLicenseType, extremeMemoryMonitorGreenZoneThreshold=extremeMemoryMonitorGreenZoneThreshold, extremeServiceLicense=extremeServiceLicense, extremeSwMonitorMemory=extremeSwMonitorMemory, extremeCpuMonitorSystemUtilization30secs=extremeCpuMonitorSystemUtilization30secs, extremeCpuMonitorSystemUtilization5mins=extremeCpuMonitorSystemUtilization5mins, extremeMemoryMonitorProcessName=extremeMemoryMonitorProcessName, extremeCpuMonitorUtilization1min=extremeCpuMonitorUtilization1min, trialPeriod=trialPeriod, extremeCpuMonitorUtilization10secs=extremeCpuMonitorUtilization10secs, extremeCpuMonitorSystemSlotId=extremeCpuMonitorSystemSlotId, extremeMemoryMonitorSystemTable=extremeMemoryMonitorSystemTable, extremeSwMonitorCpuUtilization=extremeSwMonitorCpuUtilization, extremeMemoryMonitorRedZoneCount=extremeMemoryMonitorRedZoneCount, extremeSwMonitor=extremeSwMonitor, extremeCpuMonitorSystemUtilization1hour=extremeCpuMonitorSystemUtilization1hour, PYSNMP_MODULE_ID=extremeSwMonitor, extremeMemoryMonitorSlotId=extremeMemoryMonitorSlotId, extremeCpuMonitorSystemTime=extremeCpuMonitorSystemTime, extremeCpuMonitorEntry=extremeCpuMonitorEntry, extremeMemoryMonitorSystemUsage=extremeMemoryMonitorSystemUsage, extremeMemoryMonitorSystemEntry=extremeMemoryMonitorSystemEntry, extremeCpuMonitorUtilization1hour=extremeCpuMonitorUtilization1hour, extremeCpuMonitorUtilization5secs=extremeCpuMonitorUtilization5secs, extremeCpuMonitorMaxUtilization=extremeCpuMonitorMaxUtilization, extremeCpuMonitorThreshold=extremeCpuMonitorThreshold)
