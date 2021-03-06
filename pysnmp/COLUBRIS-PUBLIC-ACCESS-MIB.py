#
# PySNMP MIB module COLUBRIS-PUBLIC-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-PUBLIC-ACCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSecurity, ColubrisPriorityQueue, ColubrisUsersAuthenticationType, ColubrisProfileIndexOrZero, ColubrisNotificationEnable, ColubrisUsersAuthenticationMode, ColubrisSSIDOrNone = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSecurity", "ColubrisPriorityQueue", "ColubrisUsersAuthenticationType", "ColubrisProfileIndexOrZero", "ColubrisNotificationEnable", "ColubrisUsersAuthenticationMode", "ColubrisSSIDOrNone")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter64, Bits, ModuleIdentity, MibIdentifier, iso, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Bits", "ModuleIdentity", "MibIdentifier", "iso", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Counter32", "ObjectIdentity")
TextualConvention, DateAndTime, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "TruthValue", "DisplayString", "MacAddress")
colubrisPublicAccessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 1))
if mibBuilder.loadTexts: colubrisPublicAccessMIB.setLastUpdated('200511040000Z')
if mibBuilder.loadTexts: colubrisPublicAccessMIB.setOrganization('Colubris Networks, Inc.')
colubrisPublicAccessMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1))
publicAccessGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1))
publicAccessDeviceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2))
publicAccessUsersGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3))
publicAccessNASPortsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4))
publicAccessStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessStatus.setStatus('current')
publicAccessStatusChangedCause = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessStatusChangedCause.setStatus('current')
publicAccessDeviceUserName = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 253))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessDeviceUserName.setStatus('current')
publicAccessDeviceUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 230))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessDeviceUserPassword.setStatus('current')
publicAccessDeviceSessionTimeoutAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessDeviceSessionTimeoutAdminStatus.setStatus('current')
publicAccessDeviceSessionTimeoutOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessDeviceSessionTimeoutOperStatus.setStatus('current')
publicAccessDeviceConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 5), ColubrisUsersAuthenticationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessDeviceConfigMode.setStatus('current')
publicAccessDeviceAuthenProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 6), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessDeviceAuthenProfileIndex.setStatus('current')
publicAccessDeviceAccountingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessDeviceAccountingEnabled.setStatus('current')
publicAccessDeviceAccountingProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 8), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessDeviceAccountingProfileIndex.setStatus('current')
publicAccessDeviceForceReconfiguration = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("forceReconfiguration", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessDeviceForceReconfiguration.setStatus('current')
publicAccessUsersMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersMaxCount.setStatus('current')
publicAccessUsersCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersCount.setStatus('current')
publicAccessUsersThreshold = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessUsersThreshold.setStatus('current')
publicAccessUsersSessionTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 4), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessUsersSessionTrapEnabled.setStatus('current')
publicAccessUsersConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5), )
if mibBuilder.loadTexts: publicAccessUsersConfigTable.setStatus('current')
publicAccessUsersConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigIndex"))
if mibBuilder.loadTexts: publicAccessUsersConfigEntry.setStatus('current')
publicAccessUsersConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessUsersConfigIndex.setStatus('current')
publicAccessUsersConfigAuthenType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 2), ColubrisUsersAuthenticationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAuthenType.setStatus('current')
publicAccessUsersConfigAuthenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 3), ColubrisUsersAuthenticationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAuthenMode.setStatus('current')
publicAccessUsersConfigAuthenProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 4), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAuthenProfileIndex.setStatus('current')
publicAccessUsersConfigAuthenTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAuthenTimeout.setStatus('current')
publicAccessUsersConfigAccountingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAccountingEnabled.setStatus('current')
publicAccessUsersConfigAccountingProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 7), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigAccountingProfileIndex.setStatus('current')
publicAccessUsersConfigInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 8), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigInterfaceIndex.setStatus('current')
publicAccessUsersConfigVirtualApProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 5, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUsersConfigVirtualApProfileIndex.setStatus('current')
publicAccessUserTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6), )
if mibBuilder.loadTexts: publicAccessUserTable.setStatus('current')
publicAccessUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserIndex"))
if mibBuilder.loadTexts: publicAccessUserEntry.setStatus('current')
publicAccessUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessUserIndex.setStatus('current')
publicAccessUserAuthenType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 2), ColubrisUsersAuthenticationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserAuthenType.setStatus('current')
publicAccessUserAuthenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 3), ColubrisUsersAuthenticationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserAuthenMode.setStatus('current')
publicAccessUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unassigned", 0), ("connecting", 1), ("connected", 2), ("reconnecting", 3), ("disconnecting", 4), ("disconnected", 5), ("disconnectingAdministrative", 6), ("disconnectedAdministrative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserState.setStatus('current')
publicAccessUserStationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserStationIpAddress.setStatus('current')
publicAccessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserName.setStatus('current')
publicAccessUserSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserSessionStartTime.setStatus('current')
publicAccessUserSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 8), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserSessionDuration.setStatus('current')
publicAccessUserIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 9), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserIdleTime.setStatus('current')
publicAccessUserBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserBytesSent.setStatus('current')
publicAccessUserBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserBytesReceived.setStatus('current')
publicAccessUserPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserPacketsSent.setStatus('current')
publicAccessUserPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserPacketsReceived.setStatus('current')
publicAccessUserForceDisconnection = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("adminReset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessUserForceDisconnection.setStatus('current')
publicAccessUserStationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 15), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserStationMacAddress.setStatus('current')
publicAccessUserApMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 16), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserApMacAddress.setStatus('current')
publicAccessUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserGroupName.setStatus('current')
publicAccessUserSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 18), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserSSID.setStatus('current')
publicAccessUserSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 19), ColubrisSecurity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserSecurity.setStatus('current')
publicAccessUserPHYType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3), ("ieee802dot11n", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserPHYType.setStatus('current')
publicAccessUserVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserVLAN.setStatus('current')
publicAccessUserApRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserApRadioIndex.setStatus('current')
publicAccessUserConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserConfigIndex.setStatus('current')
publicAccessUserConnectedInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: publicAccessUserConnectedInterface.setStatus('current')
publicAccessUserBytesSentDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserBytesSentDropped.setStatus('current')
publicAccessUserBytesReceivedDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserBytesReceivedDropped.setStatus('current')
publicAccessUserPacketsSentDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserPacketsSentDropped.setStatus('current')
publicAccessUserPacketsReceivedDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserPacketsReceivedDropped.setStatus('current')
publicAccessUserRateLimitationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 29), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserRateLimitationEnabled.setStatus('current')
publicAccessUserMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserMaxTransmitRate.setStatus('current')
publicAccessUserMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserMaxReceiveRate.setStatus('current')
publicAccessUserBandwidthControlLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 32), ColubrisPriorityQueue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserBandwidthControlLevel.setStatus('current')
publicAccessUserNASPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 6, 1, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessUserNASPort.setStatus('current')
publicAccessUsersLoggedInTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 7), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessUsersLoggedInTrapEnabled.setStatus('current')
publicAccessUsersLoggedInTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 3, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessUsersLoggedInTrapInterval.setStatus('current')
publicAccessNASPortCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessNASPortCount.setStatus('current')
publicAccessNASPortTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2), )
if mibBuilder.loadTexts: publicAccessNASPortTable.setStatus('current')
publicAccessNASPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortIndex"))
if mibBuilder.loadTexts: publicAccessNASPortEntry.setStatus('current')
publicAccessNASPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessNASPortIndex.setStatus('current')
publicAccessNASPortUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 1, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessNASPortUserName.setStatus('current')
publicAccessMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2))
publicAccessMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0))
publicAccessStatusChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatus"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedCause"))
if mibBuilder.loadTexts: publicAccessStatusChangedTrap.setStatus('current')
publicAccessUsersThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 2)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount"))
if mibBuilder.loadTexts: publicAccessUsersThresholdTrap.setStatus('current')
publicAccessUsersSessionStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 3)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"))
if mibBuilder.loadTexts: publicAccessUsersSessionStartTrap.setStatus('current')
publicAccessUsersSessionStopTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 4)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"))
if mibBuilder.loadTexts: publicAccessUsersSessionStopTrap.setStatus('current')
publicAccessUsersSessionFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 5)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"))
if mibBuilder.loadTexts: publicAccessUsersSessionFailTrap.setStatus('current')
publicAccessUsersLoggedInTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 1, 2, 0, 6)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationIpAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationMacAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApMacAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConnectedInterface"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionDuration"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceived"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSent"))
if mibBuilder.loadTexts: publicAccessUsersLoggedInTrap.setStatus('current')
colubrisPublicAccessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3))
colubrisPublicAccessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 1))
colubrisPublicAccessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2))
colubrisPublicAccessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 1, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "colubrisPublicAccessMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "colubrisPublicAccessUserMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "colubrisPublicAccessUserConfigMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "colubrisPublicAccessNotificationGroup"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "colubrisPublicAccessNASPortsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessMIBCompliance = colubrisPublicAccessMIBCompliance.setStatus('current')
colubrisPublicAccessMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatus"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedCause"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceUserName"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceUserPassword"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceSessionTimeoutAdminStatus"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceSessionTimeoutOperStatus"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceConfigMode"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAuthenProfileIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAccountingEnabled"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceAccountingProfileIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessDeviceForceReconfiguration"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersCount"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersThreshold"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionTrapEnabled"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrapEnabled"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrapInterval"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessMIBGroup = colubrisPublicAccessMIBGroup.setStatus('current')
colubrisPublicAccessUserMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 2)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserAuthenType"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserAuthenMode"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserState"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationIpAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserName"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionStartTime"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSessionDuration"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserIdleTime"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSent"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceived"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsSent"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsReceived"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserForceDisconnection"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserStationMacAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApMacAddress"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserGroupName"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSSID"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserSecurity"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPHYType"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserVLAN"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserApRadioIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConfigIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserConnectedInterface"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesSentDropped"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBytesReceivedDropped"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsSentDropped"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserPacketsReceivedDropped"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserRateLimitationEnabled"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserMaxTransmitRate"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserMaxReceiveRate"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserBandwidthControlLevel"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUserNASPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessUserMIBGroup = colubrisPublicAccessUserMIBGroup.setStatus('current')
colubrisPublicAccessUserConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 3)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenType"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenMode"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenProfileIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAuthenTimeout"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAccountingEnabled"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigAccountingProfileIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigInterfaceIndex"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersConfigVirtualApProfileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessUserConfigMIBGroup = colubrisPublicAccessUserConfigMIBGroup.setStatus('current')
colubrisPublicAccessNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 4)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessStatusChangedTrap"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersThresholdTrap"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionStartTrap"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionStopTrap"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersSessionFailTrap"), ("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessUsersLoggedInTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessNotificationGroup = colubrisPublicAccessNotificationGroup.setStatus('current')
colubrisPublicAccessNASPortsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 1, 3, 2, 5)).setObjects(("COLUBRIS-PUBLIC-ACCESS-MIB", "publicAccessNASPortUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessNASPortsMIBGroup = colubrisPublicAccessNASPortsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-PUBLIC-ACCESS-MIB", publicAccessDeviceSessionTimeoutOperStatus=publicAccessDeviceSessionTimeoutOperStatus, publicAccessUserPacketsReceived=publicAccessUserPacketsReceived, publicAccessUsersConfigVirtualApProfileIndex=publicAccessUsersConfigVirtualApProfileIndex, publicAccessDeviceConfigMode=publicAccessDeviceConfigMode, publicAccessUserConfigIndex=publicAccessUserConfigIndex, publicAccessUserBandwidthControlLevel=publicAccessUserBandwidthControlLevel, colubrisPublicAccessMIBConformance=colubrisPublicAccessMIBConformance, publicAccessUserSecurity=publicAccessUserSecurity, publicAccessDeviceGroup=publicAccessDeviceGroup, publicAccessUserBytesReceived=publicAccessUserBytesReceived, publicAccessUsersThresholdTrap=publicAccessUsersThresholdTrap, publicAccessDeviceForceReconfiguration=publicAccessDeviceForceReconfiguration, publicAccessUserPacketsSent=publicAccessUserPacketsSent, publicAccessUserPacketsSentDropped=publicAccessUserPacketsSentDropped, publicAccessUsersSessionTrapEnabled=publicAccessUsersSessionTrapEnabled, publicAccessUserBytesReceivedDropped=publicAccessUserBytesReceivedDropped, publicAccessUserIdleTime=publicAccessUserIdleTime, colubrisPublicAccessNASPortsMIBGroup=colubrisPublicAccessNASPortsMIBGroup, publicAccessDeviceUserName=publicAccessDeviceUserName, publicAccessDeviceSessionTimeoutAdminStatus=publicAccessDeviceSessionTimeoutAdminStatus, publicAccessUserGroupName=publicAccessUserGroupName, publicAccessUsersLoggedInTrapEnabled=publicAccessUsersLoggedInTrapEnabled, colubrisPublicAccessNotificationGroup=colubrisPublicAccessNotificationGroup, publicAccessNASPortUserName=publicAccessNASPortUserName, publicAccessNASPortEntry=publicAccessNASPortEntry, publicAccessUsersCount=publicAccessUsersCount, publicAccessUserSSID=publicAccessUserSSID, publicAccessDeviceUserPassword=publicAccessDeviceUserPassword, publicAccessUserPacketsReceivedDropped=publicAccessUserPacketsReceivedDropped, publicAccessUserBytesSent=publicAccessUserBytesSent, publicAccessMIBNotifications=publicAccessMIBNotifications, publicAccessUserSessionDuration=publicAccessUserSessionDuration, colubrisPublicAccessMIB=colubrisPublicAccessMIB, publicAccessUserStationMacAddress=publicAccessUserStationMacAddress, publicAccessUserForceDisconnection=publicAccessUserForceDisconnection, publicAccessNASPortsGroup=publicAccessNASPortsGroup, publicAccessNASPortIndex=publicAccessNASPortIndex, publicAccessUsersConfigIndex=publicAccessUsersConfigIndex, publicAccessStatusChangedCause=publicAccessStatusChangedCause, PYSNMP_MODULE_ID=colubrisPublicAccessMIB, publicAccessUserMaxTransmitRate=publicAccessUserMaxTransmitRate, publicAccessUserBytesSentDropped=publicAccessUserBytesSentDropped, publicAccessUsersConfigAccountingProfileIndex=publicAccessUsersConfigAccountingProfileIndex, colubrisPublicAccessMIBGroups=colubrisPublicAccessMIBGroups, publicAccessUsersConfigAuthenTimeout=publicAccessUsersConfigAuthenTimeout, colubrisPublicAccessMIBObjects=colubrisPublicAccessMIBObjects, publicAccessUsersLoggedInTrapInterval=publicAccessUsersLoggedInTrapInterval, publicAccessDeviceAccountingProfileIndex=publicAccessDeviceAccountingProfileIndex, publicAccessUserStationIpAddress=publicAccessUserStationIpAddress, publicAccessUserState=publicAccessUserState, publicAccessUsersThreshold=publicAccessUsersThreshold, publicAccessUsersConfigAuthenMode=publicAccessUsersConfigAuthenMode, publicAccessUserIndex=publicAccessUserIndex, publicAccessUserMaxReceiveRate=publicAccessUserMaxReceiveRate, publicAccessNASPortCount=publicAccessNASPortCount, publicAccessStatusChangedTrap=publicAccessStatusChangedTrap, publicAccessUserApMacAddress=publicAccessUserApMacAddress, publicAccessUsersConfigEntry=publicAccessUsersConfigEntry, publicAccessNASPortTable=publicAccessNASPortTable, publicAccessUsersMaxCount=publicAccessUsersMaxCount, publicAccessUsersSessionStopTrap=publicAccessUsersSessionStopTrap, publicAccessUsersConfigTable=publicAccessUsersConfigTable, publicAccessStatus=publicAccessStatus, publicAccessUsersConfigInterfaceIndex=publicAccessUsersConfigInterfaceIndex, publicAccessUsersSessionFailTrap=publicAccessUsersSessionFailTrap, publicAccessUserEntry=publicAccessUserEntry, publicAccessUsersConfigAccountingEnabled=publicAccessUsersConfigAccountingEnabled, publicAccessGroup=publicAccessGroup, publicAccessUserTable=publicAccessUserTable, publicAccessUserNASPort=publicAccessUserNASPort, colubrisPublicAccessMIBCompliances=colubrisPublicAccessMIBCompliances, publicAccessUserName=publicAccessUserName, publicAccessUsersLoggedInTrap=publicAccessUsersLoggedInTrap, publicAccessUserApRadioIndex=publicAccessUserApRadioIndex, publicAccessDeviceAuthenProfileIndex=publicAccessDeviceAuthenProfileIndex, publicAccessUserAuthenMode=publicAccessUserAuthenMode, colubrisPublicAccessUserConfigMIBGroup=colubrisPublicAccessUserConfigMIBGroup, publicAccessUserPHYType=publicAccessUserPHYType, publicAccessUsersGroup=publicAccessUsersGroup, publicAccessUserConnectedInterface=publicAccessUserConnectedInterface, publicAccessDeviceAccountingEnabled=publicAccessDeviceAccountingEnabled, publicAccessUsersConfigAuthenType=publicAccessUsersConfigAuthenType, publicAccessMIBNotificationPrefix=publicAccessMIBNotificationPrefix, colubrisPublicAccessMIBCompliance=colubrisPublicAccessMIBCompliance, colubrisPublicAccessMIBGroup=colubrisPublicAccessMIBGroup, publicAccessUserSessionStartTime=publicAccessUserSessionStartTime, publicAccessUsersSessionStartTrap=publicAccessUsersSessionStartTrap, publicAccessUserAuthenType=publicAccessUserAuthenType, colubrisPublicAccessUserMIBGroup=colubrisPublicAccessUserMIBGroup, publicAccessUserVLAN=publicAccessUserVLAN, publicAccessUserRateLimitationEnabled=publicAccessUserRateLimitationEnabled, publicAccessUsersConfigAuthenProfileIndex=publicAccessUsersConfigAuthenProfileIndex)
