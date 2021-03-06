#
# PySNMP MIB module A3COM-HUAWEI-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, Bits, TimeTicks, Integer32, NotificationType, Counter32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "Integer32", "NotificationType", "Counter32", "iso", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cSSH = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22))
h3cSSH.setRevisions(('2007-11-19 00:00',))
if mibBuilder.loadTexts: h3cSSH.setLastUpdated('200711190000Z')
if mibBuilder.loadTexts: h3cSSH.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cSSHServerMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1))
h3cSSHServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1))
h3cSSHServerGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1))
h3cSSHServerVersion = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHServerVersion.setStatus('current')
h3cSSHServerCompatibleSSH1x = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableCompatibleSSH1x", 1), ("disableCompatibleSSH1x", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSSHServerCompatibleSSH1x.setStatus('current')
h3cSSHServerRekeyInterval = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSSHServerRekeyInterval.setStatus('current')
h3cSSHServerAuthRetries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSSHServerAuthRetries.setStatus('current')
h3cSSHServerAuthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSSHServerAuthTimeout.setStatus('current')
h3cSFTPServerIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSFTPServerIdleTimeout.setStatus('current')
h3cSSHServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSSHServer", 1), ("disableSSHServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSSHServerEnable.setStatus('current')
h3cSFTPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSFTPService", 1), ("disableSFTPService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSFTPServerEnable.setStatus('current')
h3cSSHUserConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2))
h3cSSHUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1), )
if mibBuilder.loadTexts: h3cSSHUserConfigTable.setStatus('current')
h3cSSHUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-SSH-MIB", "h3cSSHUserName"))
if mibBuilder.loadTexts: h3cSSHUserConfigEntry.setStatus('current')
h3cSSHUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: h3cSSHUserName.setStatus('current')
h3cSSHUserServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("all", 2), ("stelnet", 3), ("sftp", 4))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSSHUserServiceType.setStatus('current')
h3cSSHUserAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("password", 2), ("publicKey", 3), ("any", 4), ("publicKeyPassword", 5))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSSHUserAuthType.setStatus('current')
h3cSSHUserPublicKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSSHUserPublicKeyName.setStatus('current')
h3cSSHUserWorkDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSSHUserWorkDirectory.setStatus('current')
h3cSSHUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSSHUserRowStatus.setStatus('current')
h3cSSHSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3), )
if mibBuilder.loadTexts: h3cSSHSessionInfoTable.setStatus('current')
h3cSSHSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionID"))
if mibBuilder.loadTexts: h3cSSHSessionInfoEntry.setStatus('current')
h3cSSHSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSSHSessionID.setStatus('current')
h3cSSHSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionUserName.setStatus('current')
h3cSSHSessionUserIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionUserIpAddrType.setStatus('current')
h3cSSHSessionUserIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionUserIpAddr.setStatus('current')
h3cSSHSessionClientVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionClientVersion.setStatus('current')
h3cSSHSessionServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("stelnet", 2), ("sftp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionServiceType.setStatus('current')
h3cSSHSessionEncry = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("aes128CBC", 2), ("desCBC", 3), ("des3CBC", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionEncry.setStatus('current')
h3cSSHSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("init", 1), ("verExchange", 2), ("keysExchange", 3), ("authRequest", 4), ("serviceRequest", 5), ("established", 6), ("disconnect", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSSHSessionState.setStatus('current')
h3cSSHServerObjForTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2))
h3cSSHAttemptUserName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cSSHAttemptUserName.setStatus('current')
h3cSSHAttemptIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cSSHAttemptIpAddrType.setStatus('current')
h3cSSHAttemptIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cSSHAttemptIpAddr.setStatus('current')
h3cSSHUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cSSHUserAuthFailureReason.setStatus('current')
h3cSSHServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3))
h3cSSHServerNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0))
h3cSSHUserAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 1)).setObjects(("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptUserName"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddrType"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddr"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHUserAuthFailureReason"))
if mibBuilder.loadTexts: h3cSSHUserAuthFailure.setStatus('current')
h3cSSHVersionNegotiationFailure = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 2)).setObjects(("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddrType"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHAttemptIpAddr"))
if mibBuilder.loadTexts: h3cSSHVersionNegotiationFailure.setStatus('current')
h3cSSHUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 3)).setObjects(("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserName"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddrType"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: h3cSSHUserLogin.setStatus('current')
h3cSSHUserLogoff = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 22, 1, 3, 0, 4)).setObjects(("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserName"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddrType"), ("A3COM-HUAWEI-SSH-MIB", "h3cSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: h3cSSHUserLogoff.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-SSH-MIB", h3cSSHUserAuthType=h3cSSHUserAuthType, h3cSSHSessionID=h3cSSHSessionID, h3cSSHAttemptIpAddr=h3cSSHAttemptIpAddr, h3cSSHSessionUserIpAddrType=h3cSSHSessionUserIpAddrType, h3cSSHServerMIB=h3cSSHServerMIB, h3cSSHUserAuthFailure=h3cSSHUserAuthFailure, h3cSSHSessionServiceType=h3cSSHSessionServiceType, h3cSSHUserLogoff=h3cSSHUserLogoff, h3cSSHSessionEncry=h3cSSHSessionEncry, h3cSSHUserLogin=h3cSSHUserLogin, h3cSSHServerCompatibleSSH1x=h3cSSHServerCompatibleSSH1x, h3cSSHSessionUserName=h3cSSHSessionUserName, h3cSSHUserConfigTable=h3cSSHUserConfigTable, h3cSSHUserRowStatus=h3cSSHUserRowStatus, h3cSSHServerAuthTimeout=h3cSSHServerAuthTimeout, h3cSSHSessionInfoEntry=h3cSSHSessionInfoEntry, h3cSSHServerObjForTrap=h3cSSHServerObjForTrap, h3cSSHUserAuthFailureReason=h3cSSHUserAuthFailureReason, h3cSSHSessionUserIpAddr=h3cSSHSessionUserIpAddr, PYSNMP_MODULE_ID=h3cSSH, h3cSSHServerNotifications=h3cSSHServerNotifications, h3cSSHUserPublicKeyName=h3cSSHUserPublicKeyName, h3cSSHAttemptUserName=h3cSSHAttemptUserName, h3cSSHUserConfigEntry=h3cSSHUserConfigEntry, h3cSSHUserName=h3cSSHUserName, h3cSSHServerMIBObjects=h3cSSHServerMIBObjects, h3cSFTPServerEnable=h3cSFTPServerEnable, h3cSSHSessionState=h3cSSHSessionState, h3cSSHUserConfig=h3cSSHUserConfig, h3cSSHServerGlobalConfig=h3cSSHServerGlobalConfig, h3cSFTPServerIdleTimeout=h3cSFTPServerIdleTimeout, h3cSSHUserWorkDirectory=h3cSSHUserWorkDirectory, h3cSSHServerNotificationsPrefix=h3cSSHServerNotificationsPrefix, h3cSSHServerEnable=h3cSSHServerEnable, h3cSSHVersionNegotiationFailure=h3cSSHVersionNegotiationFailure, h3cSSHServerVersion=h3cSSHServerVersion, h3cSSHSessionClientVersion=h3cSSHSessionClientVersion, h3cSSHServerAuthRetries=h3cSSHServerAuthRetries, h3cSSH=h3cSSH, h3cSSHUserServiceType=h3cSSHUserServiceType, h3cSSHServerRekeyInterval=h3cSSHServerRekeyInterval, h3cSSHSessionInfoTable=h3cSSHSessionInfoTable, h3cSSHAttemptIpAddrType=h3cSSHAttemptIpAddrType)
