#
# PySNMP MIB module D5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/D5-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipAdEntAddr, = mibBuilder.importSymbols("IP-MIB", "ipAdEntAddr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmp, sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "snmp", "sysUpTime", "sysDescr")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, Bits, Counter64, Counter32, NotificationType, MibIdentifier, NotificationType, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Bits", "Counter64", "Counter32", "NotificationType", "MibIdentifier", "NotificationType", "enterprises", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

symplex = MibIdentifier((1, 3, 6, 1, 4, 1, 385))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1))
datamizerHseries = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 1))
directrouteSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 2))
directroute4Series = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 3))
datamizerVseries = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 4))
drcalldata = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 4, 1))
callDataTrapAddr = MibScalar((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataTrapAddr.setStatus('mandatory')
callDataTotalActiveCalls = MibScalar((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataTotalActiveCalls.setStatus('mandatory')
callDataActvTable = MibTable((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3), )
if mibBuilder.loadTexts: callDataActvTable.setStatus('mandatory')
callDataActvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1), ).setIndexNames((0, "D5-MIB", "callDataActvIndex"))
if mibBuilder.loadTexts: callDataActvEntry.setStatus('mandatory')
callDataActvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvIndex.setStatus('mandatory')
callDataActvReqTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvReqTime.setStatus('mandatory')
callDataActvEstTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvEstTime.setStatus('mandatory')
callDataActvCurrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvCurrTime.setStatus('mandatory')
callDataActvSourceSys = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvSourceSys.setStatus('mandatory')
callDataActvDestSys = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvDestSys.setStatus('mandatory')
callDataActvPhoneNum = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvPhoneNum.setStatus('mandatory')
callDataActvBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvBandwidth.setStatus('mandatory')
callDataActvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("requested", 2), ("active", 3), ("complete", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataActvStatus.setStatus('mandatory')
callDataCompTable = MibTable((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4), )
if mibBuilder.loadTexts: callDataCompTable.setStatus('mandatory')
callDataCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1), ).setIndexNames((0, "D5-MIB", "callDataCompIndex"))
if mibBuilder.loadTexts: callDataCompEntry.setStatus('mandatory')
callDataCompIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompIndex.setStatus('mandatory')
callDataCompReqTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompReqTime.setStatus('mandatory')
callDataCompEstTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompEstTime.setStatus('mandatory')
callDataCompRelTime = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompRelTime.setStatus('mandatory')
callDataCompSourceSys = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompSourceSys.setStatus('mandatory')
callDataCompDestSys = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompDestSys.setStatus('mandatory')
callDataCompPhoneNum = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompPhoneNum.setStatus('mandatory')
callDataCompBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompBandwidth.setStatus('mandatory')
callDataCompStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("requested", 2), ("active", 3), ("complete", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callDataCompStatus.setStatus('mandatory')
d5system = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 4, 2))
drProdType = MibScalar((1, 3, 6, 1, 4, 1, 385, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("datamizer-5", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: drProdType.setStatus('mandatory')
drSoftVersion = MibScalar((1, 3, 6, 1, 4, 1, 385, 1, 4, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: drSoftVersion.setStatus('mandatory')
d5stats = MibIdentifier((1, 3, 6, 1, 4, 1, 385, 1, 4, 3))
d5PortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1), )
if mibBuilder.loadTexts: d5PortStatsTable.setStatus('mandatory')
d5PortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1), ).setIndexNames((0, "D5-MIB", "d5StatsPortIndex"))
if mibBuilder.loadTexts: d5PortStatsEntry.setStatus('mandatory')
d5StatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("briA", 1), ("briB", 2), ("briC", 3), ("briD", 4), ("lanE", 5), ("serialHostF", 6), ("serialTrunkG", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortIndex.setStatus('mandatory')
d5StatsPortPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortPacketsIn.setStatus('mandatory')
d5StatsPortPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortPacketsOut.setStatus('mandatory')
d5StatsPortPPSIn = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortPPSIn.setStatus('mandatory')
d5StatsPortPPSOut = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortPPSOut.setStatus('mandatory')
d5StatsPortBPSIn = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortBPSIn.setStatus('mandatory')
d5StatsPortBPSOut = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5StatsPortBPSOut.setStatus('mandatory')
d5PortStatsInterval = MibScalar((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one-minute", 1), ("fifteen-minutes", 2), ("thirty-minutes", 3), ("sixty-minutes", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d5PortStatsInterval.setStatus('mandatory')
d5SystemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3), )
if mibBuilder.loadTexts: d5SystemStatsTable.setStatus('mandatory')
d5SystemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1), ).setIndexNames((0, "D5-MIB", "d5SystemStatsIndex"))
if mibBuilder.loadTexts: d5SystemStatsEntry.setStatus('mandatory')
d5SystemStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("wanDataErrors", 1), ("serialHostDataErrors", 2), ("lanDataErrors", 3), ("congestionDetection", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5SystemStatsIndex.setStatus('mandatory')
d5SystemStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d5SystemStatsCount.setStatus('mandatory')
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"))
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4)).setObjects(("IP-MIB", "ipAdEntAddr"))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("SNMPv2-MIB", "sysUpTime"))
unspecifiedTrap = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,1)).setObjects(("SNMPv2-MIB", "sysDescr"))
startDisasterRecovery = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,2)).setObjects(("SNMPv2-MIB", "sysDescr"))
stopDisasterRecovery = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,3)).setObjects(("SNMPv2-MIB", "sysDescr"))
noBChannel = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,4)).setObjects(("SNMPv2-MIB", "sysDescr"))
dailyConnLimit = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,5)).setObjects(("SNMPv2-MIB", "sysDescr"))
monthlyConnLimit = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,6)).setObjects(("SNMPv2-MIB", "sysDescr"))
dataErrorBChannel = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,7)).setObjects(("SNMPv2-MIB", "sysDescr"))
pppVersion = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,8)).setObjects(("SNMPv2-MIB", "sysDescr"))
ipTableFull = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,9)).setObjects(("SNMPv2-MIB", "sysDescr"))
macTableFull = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,10)).setObjects(("SNMPv2-MIB", "sysDescr"))
routeTableFull = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,11)).setObjects(("SNMPv2-MIB", "sysDescr"))
duplicateItem = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,12)).setObjects(("SNMPv2-MIB", "sysDescr"))
noDChannel = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,13)).setObjects(("SNMPv2-MIB", "sysDescr"))
lostDedicated = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,14)).setObjects(("SNMPv2-MIB", "sysDescr"))
compCallData = NotificationType((1, 3, 6, 1, 4, 1, 385) + (0,15)).setObjects(("SNMPv2-MIB", "sysDescr"))
mibBuilder.exportSymbols("D5-MIB", callDataCompSourceSys=callDataCompSourceSys, d5StatsPortBPSOut=d5StatsPortBPSOut, datamizerHseries=datamizerHseries, authenticationFailure=authenticationFailure, macTableFull=macTableFull, callDataActvEstTime=callDataActvEstTime, callDataCompDestSys=callDataCompDestSys, products=products, d5PortStatsEntry=d5PortStatsEntry, d5PortStatsInterval=d5PortStatsInterval, ipTableFull=ipTableFull, routeTableFull=routeTableFull, drcalldata=drcalldata, callDataCompStatus=callDataCompStatus, callDataCompIndex=callDataCompIndex, callDataCompEstTime=callDataCompEstTime, d5StatsPortPPSOut=d5StatsPortPPSOut, compCallData=compCallData, callDataCompBandwidth=callDataCompBandwidth, d5StatsPortPacketsOut=d5StatsPortPacketsOut, callDataActvTable=callDataActvTable, callDataActvPhoneNum=callDataActvPhoneNum, d5SystemStatsIndex=d5SystemStatsIndex, coldStart=coldStart, callDataTrapAddr=callDataTrapAddr, directroute4Series=directroute4Series, callDataActvCurrTime=callDataActvCurrTime, symplex=symplex, callDataCompTable=callDataCompTable, callDataCompPhoneNum=callDataCompPhoneNum, linkUp=linkUp, d5SystemStatsCount=d5SystemStatsCount, lostDedicated=lostDedicated, d5system=d5system, linkDown=linkDown, callDataActvReqTime=callDataActvReqTime, d5stats=d5stats, duplicateItem=duplicateItem, d5PortStatsTable=d5PortStatsTable, callDataActvStatus=callDataActvStatus, d5StatsPortPacketsIn=d5StatsPortPacketsIn, callDataCompReqTime=callDataCompReqTime, stopDisasterRecovery=stopDisasterRecovery, d5SystemStatsTable=d5SystemStatsTable, drProdType=drProdType, startDisasterRecovery=startDisasterRecovery, callDataActvEntry=callDataActvEntry, callDataActvIndex=callDataActvIndex, callDataActvDestSys=callDataActvDestSys, noDChannel=noDChannel, datamizerVseries=datamizerVseries, directrouteSeries=directrouteSeries, callDataActvSourceSys=callDataActvSourceSys, callDataCompRelTime=callDataCompRelTime, d5StatsPortIndex=d5StatsPortIndex, dailyConnLimit=dailyConnLimit, DisplayString=DisplayString, warmStart=warmStart, callDataTotalActiveCalls=callDataTotalActiveCalls, egpNeighborLoss=egpNeighborLoss, monthlyConnLimit=monthlyConnLimit, pppVersion=pppVersion, callDataActvBandwidth=callDataActvBandwidth, dataErrorBChannel=dataErrorBChannel, unspecifiedTrap=unspecifiedTrap, d5SystemStatsEntry=d5SystemStatsEntry, drSoftVersion=drSoftVersion, d5StatsPortPPSIn=d5StatsPortPPSIn, d5StatsPortBPSIn=d5StatsPortBPSIn, callDataCompEntry=callDataCompEntry, noBChannel=noBChannel)
