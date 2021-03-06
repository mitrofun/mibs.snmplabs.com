#
# PySNMP MIB module RBN-SYS-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-SYS-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
rbnModules, = mibBuilder.importSymbols("RBN-SMI", "rbnModules")
RbnUnsigned64, = mibBuilder.importSymbols("RBN-TC", "RbnUnsigned64")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, ModuleIdentity, Bits, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, iso, Unsigned32, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "iso", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
rbnSysSecurityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 5, 54))
rbnSysSecurityMib.setRevisions(('2009-11-09 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnSysSecurityMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: rbnSysSecurityMib.setLastUpdated('200911091800Z')
if mibBuilder.loadTexts: rbnSysSecurityMib.setOrganization('Ericsson Inc.')
if mibBuilder.loadTexts: rbnSysSecurityMib.setContactInfo(' Ericsson Inc. 100 Headquarters Drive San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 ')
if mibBuilder.loadTexts: rbnSysSecurityMib.setDescription('This MIB module defines attributes and notifications related to system and network level security issues. All mib objects defined in the module are viewed within the context identified in the SNMP protocol (i.e. the community string in v1/v2c or the contextName in v3). ')
rbnSysSecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 0))
rbnSysSecObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1))
rbnSysSecConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2))
rbnSysSecThresholdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1))
rbnSysSecNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 1), Bits().clone(namedValues=NamedValues(("maliciousPkt", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnSysSecNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: rbnSysSecNotifyEnable.setDescription('The bit mask to enable/disable notifications for crossing specific threshold.')
rbnMeasurementInterval = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnMeasurementInterval.setStatus('current')
if mibBuilder.loadTexts: rbnMeasurementInterval.setDescription('Data is sampled at the start and end of a specified interval. The difference between the start and end values |end - start| is called the delta value. When setting the interval, care should be taken that the interval should be short enough that the sampled variable is very unlikely to increase or decrease by more than range of the variable. ')
rbnMaliciousPktsThresholdHi = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 3), RbnUnsigned64()).setUnits('Packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnMaliciousPktsThresholdHi.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktsThresholdHi.setDescription('When the current sampling interval delta value of the malicious packets counter is greater than or equal to this threshold, and the delta value at the last sampling interval was less than this threshold, a single high threshold exceeded event will be generated. A single high threshold exceeded event will also be generated if the first sampling interval delta value of the malicious IP packets counter is greater than or equal to this threshold. After a high threshold exceeded event is generated, another such event will not be generated until the delta value falls below this threshold and reaches the rbnMaliciousPktsThresholdLow, generating a low threshold exceeded event. In other words there cannot be successive high threshold events without an intervening low threshold event. ')
rbnMaliciousPktsThresholdLow = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 4), RbnUnsigned64()).setUnits('Packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnMaliciousPktsThresholdLow.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktsThresholdLow.setDescription('When the current sampling interval delta value of the malicious packets counter is less than or equal to this threshold, and the delta value at the last sampling interval was greater than this threshold, a single low threshold exceeded event will be generated. In addition, a high threshold exceeded event must occur before a low threshold exceeded event can be generated. ')
rbnSysSecStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2))
rbnMaliciousPktsCounter = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnMaliciousPktsCounter.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktsCounter.setDescription('A count of all malicious pkts. This includes but is not limited to malformed IP packets, malformed layer 4 IP, packets filtered by ACLs for specific faults, IP packets identified as attempting to spoof a system, and IP packets which failed reassembly.')
rbnMaliciousPktsDelta = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2, 2), CounterBasedGauge64()).setUnits('packets').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMaliciousPktsDelta.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktsDelta.setDescription('The delta value of rbnMaliciousPktsCounter at the most recently completed measurement interval.')
rbnSysSecNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 4))
rbnThresholdNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 4, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnThresholdNotifyTime.setStatus('current')
if mibBuilder.loadTexts: rbnThresholdNotifyTime.setDescription('The DateAndTime of the notification.')
rbnMaliciousPktThresholdHiExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2352, 5, 54, 0, 1))
if mibBuilder.loadTexts: rbnMaliciousPktThresholdHiExceeded.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktThresholdHiExceeded.setDescription('This notification signifies that one of the delta values is equal to or greater than the corresponding high threshold value. The specific delta value is the last object in the notification varbind list. ')
rbnMaliciousPktThresholdLowExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2352, 5, 54, 0, 2)).setObjects(("RBN-SYS-SECURITY-MIB", "rbnThresholdNotifyTime"))
if mibBuilder.loadTexts: rbnMaliciousPktThresholdLowExceeded.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktThresholdLowExceeded.setDescription('This notification signifies that one of the delta values is less than or equal to the corresponding low threshold value. The specific delta value is the last object in the notification varbind list. ')
rbnSysSecCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 1))
rbnSysSecGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2))
rbnMaliciousPktGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 1)).setObjects(("RBN-SYS-SECURITY-MIB", "rbnSysSecNotifyEnable"), ("RBN-SYS-SECURITY-MIB", "rbnMeasurementInterval"), ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsThresholdHi"), ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsThresholdLow"), ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMaliciousPktGroup = rbnMaliciousPktGroup.setStatus('current')
if mibBuilder.loadTexts: rbnMaliciousPktGroup.setDescription('Set of objects for the group.')
rbnSysSecNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 4)).setObjects(("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsDelta"), ("RBN-SYS-SECURITY-MIB", "rbnThresholdNotifyTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSysSecNotifyObjectsGroup = rbnSysSecNotifyObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: rbnSysSecNotifyObjectsGroup.setDescription('Set of objects for the group.')
rbnSysSecNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 5)).setObjects(("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktThresholdHiExceeded"), ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktThresholdLowExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSysSecNotificationGroup = rbnSysSecNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: rbnSysSecNotificationGroup.setDescription('Set of notifications for the group.')
rbnSysSecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 1, 1)).setObjects(("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktGroup"), ("RBN-SYS-SECURITY-MIB", "rbnSysSecNotifyObjectsGroup"), ("RBN-SYS-SECURITY-MIB", "rbnSysSecNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSysSecCompliance = rbnSysSecCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnSysSecCompliance.setDescription('The compliance statement for support of this mib module.')
mibBuilder.exportSymbols("RBN-SYS-SECURITY-MIB", rbnMeasurementInterval=rbnMeasurementInterval, rbnSysSecConformance=rbnSysSecConformance, rbnMaliciousPktThresholdHiExceeded=rbnMaliciousPktThresholdHiExceeded, rbnSysSecNotifications=rbnSysSecNotifications, rbnSysSecCompliances=rbnSysSecCompliances, rbnSysSecGroups=rbnSysSecGroups, rbnSysSecNotifyObjectsGroup=rbnSysSecNotifyObjectsGroup, rbnMaliciousPktGroup=rbnMaliciousPktGroup, rbnSysSecObjects=rbnSysSecObjects, rbnMaliciousPktsThresholdHi=rbnMaliciousPktsThresholdHi, rbnSysSecCompliance=rbnSysSecCompliance, rbnSysSecNotifyObjects=rbnSysSecNotifyObjects, rbnSysSecThresholdObjects=rbnSysSecThresholdObjects, rbnSysSecNotificationGroup=rbnSysSecNotificationGroup, PYSNMP_MODULE_ID=rbnSysSecurityMib, rbnSysSecNotifyEnable=rbnSysSecNotifyEnable, rbnMaliciousPktsCounter=rbnMaliciousPktsCounter, rbnMaliciousPktsThresholdLow=rbnMaliciousPktsThresholdLow, rbnSysSecStatsObjects=rbnSysSecStatsObjects, rbnMaliciousPktThresholdLowExceeded=rbnMaliciousPktThresholdLowExceeded, rbnThresholdNotifyTime=rbnThresholdNotifyTime, rbnSysSecurityMib=rbnSysSecurityMib, rbnMaliciousPktsDelta=rbnMaliciousPktsDelta)
