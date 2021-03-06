#
# PySNMP MIB module EdgeSwitch-RADIUS-AUTH-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Gauge32, MibIdentifier, Counter64, Unsigned32, iso, ModuleIdentity, ObjectIdentity, Bits, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Gauge32", "MibIdentifier", "Counter64", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathRadius = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8))
fastPathRadius.setRevisions(('2014-04-21 00:00', '2011-12-14 00:00', '2011-09-26 00:00', '2011-01-26 00:00', '2007-05-23 00:00', '2003-11-21 00:00', '2003-05-07 00:00',))
if mibBuilder.loadTexts: fastPathRadius.setLastUpdated('201404210000Z')
if mibBuilder.loadTexts: fastPathRadius.setOrganization('Broadcom Inc')
agentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1))
agentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setStatus('current')
agentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusTimeout.setStatus('current')
agentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingMode.setStatus('current')
agentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusStatsClear.setStatus('current')
agentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setStatus('current')
agentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6), )
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setStatus('current')
agentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1), ).setIndexNames((0, "EdgeSwitch-RADIUS-AUTH-CLIENT-MIB", "agentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setStatus('current')
agentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setStatus('current')
agentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setStatus('current')
agentRadiusAccountingServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddressType.setStatus('current')
agentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingPort.setStatus('current')
agentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setStatus('current')
agentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setStatus('current')
agentRadiusAccountingServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerName.setStatus('current')
agentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setStatus('current')
agentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8), )
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setStatus('current')
agentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1), ).setIndexNames((0, "EdgeSwitch-RADIUS-AUTH-CLIENT-MIB", "agentRadiusServerIndex"))
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setStatus('current')
agentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusServerIndex.setStatus('current')
agentRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddress.setStatus('obsolete')
agentRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddressType.setStatus('current')
agentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPort.setStatus('current')
agentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSecret.setStatus('current')
agentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setStatus('current')
agentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setStatus('current')
agentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setStatus('current')
agentRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerRowStatus.setStatus('current')
agentRadiusServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerName.setStatus('current')
agentRadiusServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerInetAddress.setStatus('current')
agentRadiusServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerTimeout.setStatus('current')
agentRadiusServerRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerRetransmit.setStatus('current')
agentRadiusServerDeadtime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerDeadtime.setStatus('current')
agentRadiusServerSourceIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSourceIPAddr.setStatus('current')
agentRadiusServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPriority.setStatus('current')
agentRadiusServerUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("login", 2), ("dot1x", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerUsageType.setStatus('current')
agentRadiusAuthenticationServers = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAuthenticationServers.setStatus('current')
agentRadiusAccountingServers = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingServers.setStatus('current')
agentRadiusNamedAuthenticationServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusNamedAuthenticationServerGroups.setStatus('current')
agentRadiusNamedAccountingServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusNamedAccountingServerGroups.setStatus('current')
agentRadiusDeadTime = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusDeadTime.setStatus('current')
agentRadiusServerKey = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerKey.setStatus('obsolete')
agentRadiusSourceIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusSourceIPAddr.setStatus('current')
agentRadiusNasIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusNasIpAddress.setStatus('current')
agentAuthorizationNetworkRadiusMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAuthorizationNetworkRadiusMode.setStatus('current')
agentRadiusSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 8, 1, 18), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusSourceInterface.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-RADIUS-AUTH-CLIENT-MIB", agentRadiusStatsClear=agentRadiusStatsClear, agentRadiusConfigGroup=agentRadiusConfigGroup, agentRadiusServerInetAddress=agentRadiusServerInetAddress, agentRadiusMaxTransmit=agentRadiusMaxTransmit, agentRadiusAccountingSecret=agentRadiusAccountingSecret, agentRadiusNamedAccountingServerGroups=agentRadiusNamedAccountingServerGroups, agentRadiusServerTimeout=agentRadiusServerTimeout, agentRadiusServerSourceIPAddr=agentRadiusServerSourceIPAddr, agentRadiusAccountingConfigEntry=agentRadiusAccountingConfigEntry, agentRadiusAccountingPort=agentRadiusAccountingPort, agentRadiusServerIndexNextValid=agentRadiusServerIndexNextValid, agentRadiusServerDeadtime=agentRadiusServerDeadtime, agentRadiusAccountingMode=agentRadiusAccountingMode, agentRadiusDeadTime=agentRadiusDeadTime, agentRadiusAccountingServerAddress=agentRadiusAccountingServerAddress, agentRadiusTimeout=agentRadiusTimeout, agentRadiusServerPort=agentRadiusServerPort, agentRadiusServerConfigEntry=agentRadiusServerConfigEntry, agentRadiusAuthenticationServers=agentRadiusAuthenticationServers, agentRadiusServerRowStatus=agentRadiusServerRowStatus, agentRadiusSourceIPAddr=agentRadiusSourceIPAddr, agentRadiusServerUsageType=agentRadiusServerUsageType, agentRadiusAccountingServers=agentRadiusAccountingServers, agentRadiusServerRetransmit=agentRadiusServerRetransmit, agentRadiusSourceInterface=agentRadiusSourceInterface, PYSNMP_MODULE_ID=fastPathRadius, agentRadiusAccountingStatus=agentRadiusAccountingStatus, agentRadiusServerPriority=agentRadiusServerPriority, agentRadiusAccountingServerIndex=agentRadiusAccountingServerIndex, agentRadiusAccountingServerName=agentRadiusAccountingServerName, fastPathRadius=fastPathRadius, agentRadiusAccountingIndexNextValid=agentRadiusAccountingIndexNextValid, agentRadiusServerAddress=agentRadiusServerAddress, agentRadiusServerName=agentRadiusServerName, agentRadiusNasIpAddress=agentRadiusNasIpAddress, agentRadiusNamedAuthenticationServerGroups=agentRadiusNamedAuthenticationServerGroups, agentRadiusAccountingConfigTable=agentRadiusAccountingConfigTable, agentRadiusServerSecret=agentRadiusServerSecret, agentRadiusServerPrimaryMode=agentRadiusServerPrimaryMode, agentRadiusServerIndex=agentRadiusServerIndex, agentRadiusServerKey=agentRadiusServerKey, agentAuthorizationNetworkRadiusMode=agentAuthorizationNetworkRadiusMode, agentRadiusServerMsgAuth=agentRadiusServerMsgAuth, agentRadiusServerCurrentMode=agentRadiusServerCurrentMode, agentRadiusAccountingServerAddressType=agentRadiusAccountingServerAddressType, agentRadiusServerAddressType=agentRadiusServerAddressType, agentRadiusServerConfigTable=agentRadiusServerConfigTable)
