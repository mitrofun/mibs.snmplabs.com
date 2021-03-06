#
# PySNMP MIB module WBSN-APPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WBSN-APPLIANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Unsigned32, iso, Integer32, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, Bits, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "iso", "Integer32", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "IpAddress")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
dskPath, memShared, memCached, ssCpuIdle, memSwapErrorMsg, dskErrorMsg, fileErrorMsg, ssCpuSystem, memAvailReal, memAvailSwap, memTotalSwap, memTotalFree, memErrorName, fileName, memTotalReal, ssCpuUser, memBuffer, ssErrorName = mibBuilder.importSymbols("UCD-SNMP-MIB", "dskPath", "memShared", "memCached", "ssCpuIdle", "memSwapErrorMsg", "dskErrorMsg", "fileErrorMsg", "ssCpuSystem", "memAvailReal", "memAvailSwap", "memTotalSwap", "memTotalFree", "memErrorName", "fileName", "memTotalReal", "ssCpuUser", "memBuffer", "ssErrorName")
websense = ModuleIdentity((1, 3, 6, 1, 4, 1, 23365))
if mibBuilder.loadTexts: websense.setLastUpdated('201202200000Z')
if mibBuilder.loadTexts: websense.setOrganization('Websense, Inc.')
appliance = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000))
moduleName = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleName.setStatus('current')
memUsageFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memUsageFlag.setStatus('current')
vmTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 3), )
if mibBuilder.loadTexts: vmTable.setStatus('current')
vmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "vmName"))
if mibBuilder.loadTexts: vmEntry.setStatus('current')
vmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("online", 0), ("offline", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStatus.setStatus('current')
vmName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmName.setStatus('current')
hostname = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 4))
hostnameChangeFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostnameChangeFlag.setStatus('current')
prevHostname = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prevHostname.setStatus('current')
currHostname = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currHostname.setStatus('current')
ifaTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 5), )
if mibBuilder.loadTexts: ifaTable.setStatus('current')
ifaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "ifaName"))
if mibBuilder.loadTexts: ifaEntry.setStatus('current')
ifaChangeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaChangeFlag.setStatus('current')
ifaName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaName.setStatus('current')
ifaPrevAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPrevAddress.setStatus('current')
ifaCurrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaCurrAddress.setStatus('current')
ifaSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaSpeed.setStatus('current')
ifaInboundExceedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaInboundExceedFlag.setStatus('current')
ifaOutboundExceedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaOutboundExceedFlag.setStatus('current')
ifaPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPhysAddress.setStatus('current')
ifaChangeFlagv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaChangeFlagv6.setStatus('current')
ifaPrevAddressv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPrevAddressv6.setStatus('current')
ifaCurrAddressv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaCurrAddressv6.setStatus('current')
raidStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 6))
raidErrorFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidErrorFlag.setStatus('current')
dskPhysicalNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPhysicalNr.setStatus('current')
dskCriticalNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskCriticalNr.setStatus('current')
dskFailedNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskFailedNr.setStatus('current')
dskPhysErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPhysErrMsg.setStatus('current')
dskVirtualNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskVirtualNr.setStatus('current')
dskDegradedNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskDegradedNr.setStatus('current')
dskOfflineNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskOfflineNr.setStatus('current')
svcTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 7), )
if mibBuilder.loadTexts: svcTable.setStatus('current')
svcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "svcName"))
if mibBuilder.loadTexts: svcEntry.setStatus('current')
svcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 0), ("down", 1), ("yellow", 2), ("resetting", 3), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcStatus.setStatus('current')
svcName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcName.setStatus('current')
loadAvg = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 8))
loadErrorFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadErrorFlag.setStatus('current')
loadName = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadName.setStatus('current')
loadErrorMessage = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadErrorMessage.setStatus('current')
wsAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 9))
wsAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 9, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsAlertMessage.setStatus('current')
evtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 10))
evtTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtTimestamp.setStatus('current')
evtDir = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("assertion", 0), ("deassertion", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtDir.setStatus('current')
evtSensor = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtSensor.setStatus('current')
evtDesc = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtDesc.setStatus('current')
triggerReading = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerReading.setStatus('current')
triggerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerThreshold.setStatus('current')
errorClear = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 10000))
testEvent = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,10))
cpuMaxUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1000)).setObjects(("UCD-SNMP-MIB", "ssErrorName"), ("UCD-SNMP-MIB", "ssCpuUser"), ("UCD-SNMP-MIB", "ssCpuSystem"), ("UCD-SNMP-MIB", "ssCpuIdle"))
cpuMaxUsageExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1000)).setObjects(("UCD-SNMP-MIB", "ssErrorName"), ("UCD-SNMP-MIB", "ssCpuUser"), ("UCD-SNMP-MIB", "ssCpuSystem"), ("UCD-SNMP-MIB", "ssCpuIdle"))
memMaxUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1001)).setObjects(("UCD-SNMP-MIB", "memTotalReal"), ("UCD-SNMP-MIB", "memAvailReal"), ("UCD-SNMP-MIB", "memTotalFree"), ("UCD-SNMP-MIB", "memShared"), ("UCD-SNMP-MIB", "memBuffer"), ("UCD-SNMP-MIB", "memCached"), ("UCD-SNMP-MIB", "memTotalSwap"), ("UCD-SNMP-MIB", "memAvailSwap"))
memMaxUsageExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1001)).setObjects(("UCD-SNMP-MIB", "memTotalReal"), ("UCD-SNMP-MIB", "memAvailReal"), ("UCD-SNMP-MIB", "memTotalFree"), ("UCD-SNMP-MIB", "memShared"), ("UCD-SNMP-MIB", "memBuffer"), ("UCD-SNMP-MIB", "memCached"), ("UCD-SNMP-MIB", "memTotalSwap"), ("UCD-SNMP-MIB", "memAvailSwap"))
networkMaxBandwidthExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1002)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaSpeed"), ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
networkMaxBandwidthExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1002)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaSpeed"), ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
diskFreeMinSizeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1003)).setObjects(("UCD-SNMP-MIB", "dskPath"), ("UCD-SNMP-MIB", "dskErrorMsg"))
diskFreeMinSizeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1003)).setObjects(("UCD-SNMP-MIB", "dskPath"), ("UCD-SNMP-MIB", "dskErrorMsg"))
swapMinFreeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1004)).setObjects(("UCD-SNMP-MIB", "memErrorName"), ("UCD-SNMP-MIB", "memSwapErrorMsg"))
swapMinFreeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1004)).setObjects(("UCD-SNMP-MIB", "memErrorName"), ("UCD-SNMP-MIB", "memSwapErrorMsg"))
systemLoad = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1005)).setObjects(("WBSN-APPLIANCE-MIB", "loadName"), ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
systemLoadClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1005)).setObjects(("WBSN-APPLIANCE-MIB", "loadName"), ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
logFileMaxSizeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1006)).setObjects(("UCD-SNMP-MIB", "fileName"), ("UCD-SNMP-MIB", "fileErrorMsg"))
logFileMaxSizeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1006)).setObjects(("UCD-SNMP-MIB", "fileName"), ("UCD-SNMP-MIB", "fileErrorMsg"))
logCacheMinFreeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1007)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
logCacheMinFreeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1007)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
moduleDown = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1050)).setObjects(("WBSN-APPLIANCE-MIB", "vmName"))
moduleDownClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1050)).setObjects(("WBSN-APPLIANCE-MIB", "vmName"))
serviceDown = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1051)).setObjects(("WBSN-APPLIANCE-MIB", "svcStatus"), ("WBSN-APPLIANCE-MIB", "svcName"))
serviceDownClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1051)).setObjects(("WBSN-APPLIANCE-MIB", "svcStatus"), ("WBSN-APPLIANCE-MIB", "svcName"))
backupFailure = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1052)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
logServerConnectionLost = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1053)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
logServerConnectionLostClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1053)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
hostnameChange = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1061)).setObjects(("WBSN-APPLIANCE-MIB", "prevHostname"), ("WBSN-APPLIANCE-MIB", "currHostname"))
ipAddressChange = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1062)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaPrevAddress"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaPrevAddressv6"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddressv6"))
powerSupply = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2001)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
powerSupplyClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2001)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
redundancy = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2002)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
redundancyClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2002)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
temps = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2003)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
tempsClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2003)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
fans = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2004)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
fansClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2004)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
volt = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2005)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
voltClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2005)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
logs = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2006)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
logsClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2006)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
mem = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2007)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
memClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2007)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
intrusion = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2008)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
intrusionClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2008)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
battery = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2009)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
batteryClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2009)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
raid = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2010)).setObjects(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"), ("WBSN-APPLIANCE-MIB", "dskCriticalNr"), ("WBSN-APPLIANCE-MIB", "dskFailedNr"), ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"), ("WBSN-APPLIANCE-MIB", "dskVirtualNr"), ("WBSN-APPLIANCE-MIB", "dskDegradedNr"), ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
raidClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2010)).setObjects(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"), ("WBSN-APPLIANCE-MIB", "dskCriticalNr"), ("WBSN-APPLIANCE-MIB", "dskFailedNr"), ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"), ("WBSN-APPLIANCE-MIB", "dskVirtualNr"), ("WBSN-APPLIANCE-MIB", "dskDegradedNr"), ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
mibBuilder.exportSymbols("WBSN-APPLIANCE-MIB", ifaOutboundExceedFlag=ifaOutboundExceedFlag, battery=battery, logCacheMinFreeExceed=logCacheMinFreeExceed, redundancyClear=redundancyClear, vmEntry=vmEntry, evtDir=evtDir, ifaPrevAddress=ifaPrevAddress, memMaxUsageExceed=memMaxUsageExceed, fansClear=fansClear, moduleDown=moduleDown, wsAlert=wsAlert, svcTable=svcTable, memUsageFlag=memUsageFlag, diskFreeMinSizeExceedClear=diskFreeMinSizeExceedClear, ifaName=ifaName, svcStatus=svcStatus, redundancy=redundancy, ifaChangeFlag=ifaChangeFlag, PYSNMP_MODULE_ID=websense, ifaPhysAddress=ifaPhysAddress, moduleDownClear=moduleDownClear, intrusion=intrusion, dskFailedNr=dskFailedNr, loadName=loadName, dskVirtualNr=dskVirtualNr, ifaSpeed=ifaSpeed, swapMinFreeExceed=swapMinFreeExceed, diskFreeMinSizeExceed=diskFreeMinSizeExceed, memClear=memClear, cpuMaxUsageExceedClear=cpuMaxUsageExceedClear, vmStatus=vmStatus, moduleName=moduleName, intrusionClear=intrusionClear, triggerReading=triggerReading, ifaChangeFlagv6=ifaChangeFlagv6, logServerConnectionLost=logServerConnectionLost, logFileMaxSizeExceedClear=logFileMaxSizeExceedClear, prevHostname=prevHostname, currHostname=currHostname, raidErrorFlag=raidErrorFlag, dskPhysicalNr=dskPhysicalNr, evtInfo=evtInfo, voltClear=voltClear, temps=temps, logsClear=logsClear, wsAlertMessage=wsAlertMessage, systemLoadClear=systemLoadClear, swapMinFreeExceedClear=swapMinFreeExceedClear, hostnameChange=hostnameChange, powerSupply=powerSupply, raidClear=raidClear, backupFailure=backupFailure, networkMaxBandwidthExceedClear=networkMaxBandwidthExceedClear, errorClear=errorClear, powerSupplyClear=powerSupplyClear, fans=fans, evtSensor=evtSensor, loadErrorMessage=loadErrorMessage, tempsClear=tempsClear, mem=mem, ifaPrevAddressv6=ifaPrevAddressv6, raidStatus=raidStatus, ifaCurrAddressv6=ifaCurrAddressv6, cpuMaxUsageExceed=cpuMaxUsageExceed, dskPhysErrMsg=dskPhysErrMsg, vmTable=vmTable, evtDesc=evtDesc, evtTimestamp=evtTimestamp, vmName=vmName, serviceDownClear=serviceDownClear, ifaInboundExceedFlag=ifaInboundExceedFlag, appliance=appliance, volt=volt, systemLoad=systemLoad, batteryClear=batteryClear, logs=logs, ifaCurrAddress=ifaCurrAddress, dskOfflineNr=dskOfflineNr, networkMaxBandwidthExceed=networkMaxBandwidthExceed, dskDegradedNr=dskDegradedNr, triggerThreshold=triggerThreshold, hostnameChangeFlag=hostnameChangeFlag, svcName=svcName, serviceDown=serviceDown, memMaxUsageExceedClear=memMaxUsageExceedClear, loadAvg=loadAvg, ipAddressChange=ipAddressChange, ifaEntry=ifaEntry, logCacheMinFreeExceedClear=logCacheMinFreeExceedClear, raid=raid, logServerConnectionLostClear=logServerConnectionLostClear, websense=websense, ifaTable=ifaTable, dskCriticalNr=dskCriticalNr, loadErrorFlag=loadErrorFlag, logFileMaxSizeExceed=logFileMaxSizeExceed, hostname=hostname, svcEntry=svcEntry, testEvent=testEvent)
