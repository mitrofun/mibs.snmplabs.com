#
# PySNMP MIB module TIARA-NETWORKS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, NotificationType, IpAddress, TimeTicks, NotificationType, iso, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "Integer32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 1))
tiaraSystemMib.setRevisions(('1900-08-18 00:00',))
if mibBuilder.loadTexts: tiaraSystemMib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: tiaraSystemMib.setOrganization('Tiara Networks, Inc.')
systemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1))
dnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2))
systemEnableNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 3))
systemNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 4))
userAdminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 5))
ethernetFailOverGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6))
failOverEnableNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 7))
failOverNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 8))
vlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9))
sysIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysIpAddr.setStatus('current')
sysNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNetMask.setStatus('current')
sysBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysBroadcast.setStatus('current')
sysVersion = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysVersion.setStatus('current')
sysHostName = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysHostName.setStatus('current')
sysDomainName = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDomainName.setStatus('current')
sysAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("minor", 2), ("major", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAlarmStatus.setStatus('current')
sysReset = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysReset.setStatus('current')
sysDateTime = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDateTime.setStatus('current')
arpClearAtTable = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arpClearAtTable.setStatus('current')
ipClearRouteTable = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipClearRouteTable.setStatus('current')
dnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsEnable.setStatus('current')
dnsServerTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2), )
if mibBuilder.loadTexts: dnsServerTable.setStatus('current')
dnsServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1), ).setIndexNames((0, "TIARA-NETWORKS-SYSTEM-MIB", "dnsServerAddr"))
if mibBuilder.loadTexts: dnsServerEntry.setStatus('current')
dnsServerEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("primary", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServerEntryType.setStatus('current')
dnsServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServerAddr.setStatus('current')
userName = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: userName.setStatus('current')
tiaraEthernetFailOverTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1), )
if mibBuilder.loadTexts: tiaraEthernetFailOverTable.setStatus('current')
tiaraEthernetFailOverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1), ).setIndexNames((0, "TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex"))
if mibBuilder.loadTexts: tiaraEthernetFailOverEntry.setStatus('current')
tiaraFailOverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: tiaraFailOverIndex.setStatus('current')
tiaraFailOverEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraFailOverEnable.setStatus('current')
tiaraHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraHoldDownTime.setStatus('current')
enableFailOverNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 7, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableFailOverNotification.setStatus('current')
enableFailOverFailNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 7, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableFailOverFailNotification.setStatus('current')
failOverNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 8) + (0,1)).setObjects(("TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex"))
failOverFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 8) + (0,2)).setObjects(("TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex"))
vlanType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanType.setStatus('current')
vlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2), )
if mibBuilder.loadTexts: vlanStatsTable.setStatus('current')
vlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1), ).setIndexNames((0, "TIARA-NETWORKS-SYSTEM-MIB", "vlanTag"))
if mibBuilder.loadTexts: vlanStatsEntry.setStatus('current')
vlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTag.setStatus('current')
vlanInterfaceList = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanInterfaceList.setStatus('current')
vlanTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTxPkts.setStatus('current')
vlanRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanRxPkts.setStatus('current')
vlanDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanDroppedPkts.setStatus('current')
enableSysShutDownNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSysShutDownNotification.setStatus('current')
enableUserLoginNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableUserLoginNotification.setStatus('current')
enableUserLogOffNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableUserLogOffNotification.setStatus('current')
enableUserLoginFailNotification = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableUserLoginFailNotification.setStatus('current')
shutDownNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 4) + (0,1))
userLoginNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 4) + (0,2)).setObjects(("TIARA-NETWORKS-SYSTEM-MIB", "userName"))
userLogOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 4) + (0,3)).setObjects(("TIARA-NETWORKS-SYSTEM-MIB", "userName"))
userLoginFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 1, 4) + (0,4)).setObjects(("TIARA-NETWORKS-SYSTEM-MIB", "userName"))
mibBuilder.exportSymbols("TIARA-NETWORKS-SYSTEM-MIB", vlanTag=vlanTag, userName=userName, enableUserLoginFailNotification=enableUserLoginFailNotification, systemEnableNotification=systemEnableNotification, failOverFailNotification=failOverFailNotification, vlanStatsTable=vlanStatsTable, userLoginNotification=userLoginNotification, vlanDroppedPkts=vlanDroppedPkts, shutDownNotification=shutDownNotification, sysAlarmStatus=sysAlarmStatus, failOverEnableNotifications=failOverEnableNotifications, enableSysShutDownNotification=enableSysShutDownNotification, sysDomainName=sysDomainName, dnsServerAddr=dnsServerAddr, userLoginFailNotification=userLoginFailNotification, sysIpAddr=sysIpAddr, systemNotifications=systemNotifications, tiaraFailOverIndex=tiaraFailOverIndex, sysHostName=sysHostName, enableUserLoginNotification=enableUserLoginNotification, sysBroadcast=sysBroadcast, tiaraFailOverEnable=tiaraFailOverEnable, tiaraEthernetFailOverEntry=tiaraEthernetFailOverEntry, tiaraSystemMib=tiaraSystemMib, dnsServerTable=dnsServerTable, dnsServerEntry=dnsServerEntry, dnsServerEntryType=dnsServerEntryType, dnsEnable=dnsEnable, tiaraHoldDownTime=tiaraHoldDownTime, sysVersion=sysVersion, vlanRxPkts=vlanRxPkts, arpClearAtTable=arpClearAtTable, enableUserLogOffNotification=enableUserLogOffNotification, sysNetMask=sysNetMask, sysReset=sysReset, failOverNotifications=failOverNotifications, userLogOffNotification=userLogOffNotification, dnsGroup=dnsGroup, vlanGroup=vlanGroup, tiaraEthernetFailOverTable=tiaraEthernetFailOverTable, vlanInterfaceList=vlanInterfaceList, enableFailOverNotification=enableFailOverNotification, ethernetFailOverGroup=ethernetFailOverGroup, vlanStatsEntry=vlanStatsEntry, enableFailOverFailNotification=enableFailOverFailNotification, PYSNMP_MODULE_ID=tiaraSystemMib, sysDateTime=sysDateTime, systemObjects=systemObjects, failOverNotification=failOverNotification, vlanTxPkts=vlanTxPkts, ipClearRouteTable=ipClearRouteTable, userAdminGroup=userAdminGroup, vlanType=vlanType)