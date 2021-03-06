#
# PySNMP MIB module HM2-USERMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-USERMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hm2ConfigurationMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs", "HmEnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter64, ModuleIdentity, iso, Gauge32, Unsigned32, NotificationType, IpAddress, Integer32, Counter32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "iso", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "Integer32", "Counter32", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hm2UserMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24))
hm2UserMgmtMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2UserMgmtMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2UserMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
class Hm2UserAccessRoles(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 6, 7, 13, 15))
    namedValues = NamedValues(("unauthorized", 0), ("guest", 1), ("auditor", 2), ("custom1", 5), ("custom2", 6), ("custom3", 7), ("operator", 13), ("administrator", 15))

class Hm2UserAuthList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 5, 7, 9, 10, 248, 300))
    namedValues = NamedValues(("local", 3), ("radius", 5), ("ias", 7), ("cam", 9), ("ldap", 10), ("reject", 248), ("none", 300))

class Hm2UserCustomAccessRoles(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 6, 7))
    namedValues = NamedValues(("custom1", 5), ("custom2", 6), ("custom3", 7))

class Hm2UserCliExecModes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 10))
    namedValues = NamedValues(("user-exec-mode", 1), ("priv-exec-mode", 2), ("global-config-exec-mode", 3), ("vlan-database-exec-mode", 4), ("interface-exec-mode", 5), ("all-modes", 10))

hm2UserMgmtMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 0))
hm2UserMgmtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1))
hm2UserConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1))
hm2PwdMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2))
hm2UserApplicationListGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3))
hm2UserAuthListGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4))
hm2UserIasGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5))
hm2UserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1), )
if mibBuilder.loadTexts: hm2UserConfigTable.setStatus('current')
hm2UserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1), ).setIndexNames((1, "HM2-USERMGMT-MIB", "hm2UserName"))
if mibBuilder.loadTexts: hm2UserConfigEntry.setStatus('current')
hm2UserName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hm2UserName.setStatus('current')
hm2UserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserPassword.setStatus('current')
hm2UserAccessRole = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 3), Hm2UserAccessRoles().clone('guest')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAccessRole.setStatus('current')
hm2UserLockoutStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserLockoutStatus.setStatus('current')
hm2UserPwdChangePerm = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserPwdChangePerm.setStatus('current')
hm2UserPwdPolicyChk = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 6), HmEnabledStatus().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserPwdPolicyChk.setStatus('current')
hm2UserSnmpAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hmacmd5", 1), ("hmacsha", 2))).clone('hmacmd5')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserSnmpAuthType.setStatus('current')
hm2UserSnmpEncType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("des", 1), ("aesCfb128", 2))).clone('des')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserSnmpEncType.setStatus('current')
hm2UserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserStatus.setStatus('current')
hm2UserStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10))
hm2UserLastUserCreated = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10, 1), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2UserLastUserCreated.setStatus('current')
hm2UserLastUserDeleted = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 10, 2), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2UserLastUserDeleted.setStatus('current')
hm2UserCustomGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20))
hm2UserCustomAccessRole2NameTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1), )
if mibBuilder.loadTexts: hm2UserCustomAccessRole2NameTable.setStatus('current')
hm2UserCustomAccessRole2NameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1), ).setIndexNames((0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"))
if mibBuilder.loadTexts: hm2UserCustomAccessRole2NameEntry.setStatus('current')
hm2UserCustomAccessRole = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 1), Hm2UserCustomAccessRoles())
if mibBuilder.loadTexts: hm2UserCustomAccessRole.setStatus('current')
hm2UserCustomAccessRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2UserCustomAccessRoleName.setStatus('current')
hm2UserCustomAccessRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomAccessRoleStatus.setStatus('current')
hm2UserCustomCliCmdInheritTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2), )
if mibBuilder.loadTexts: hm2UserCustomCliCmdInheritTable.setStatus('current')
hm2UserCustomCliCmdInheritEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1), ).setIndexNames((0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"))
if mibBuilder.loadTexts: hm2UserCustomCliCmdInheritEntry.setStatus('current')
hm2UserCustomCliBaseAccessRole = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1, 1), Hm2UserAccessRoles().clone('guest')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomCliBaseAccessRole.setStatus('current')
hm2UserCustomCliBaseAccessRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomCliBaseAccessRoleStatus.setStatus('current')
hm2UserCustomCliCmdTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3), )
if mibBuilder.loadTexts: hm2UserCustomCliCmdTable.setStatus('current')
hm2UserCustomCliCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1), ).setIndexNames((0, "HM2-USERMGMT-MIB", "hm2UserCustomAccessRole"), (0, "HM2-USERMGMT-MIB", "hm2UserCustomCliExecMode"), (0, "HM2-USERMGMT-MIB", "hm2UserCustomCliIndex"))
if mibBuilder.loadTexts: hm2UserCustomCliCmdEntry.setStatus('current')
hm2UserCustomCliExecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 1), Hm2UserCliExecModes())
if mibBuilder.loadTexts: hm2UserCustomCliExecMode.setStatus('current')
hm2UserCustomCliIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hm2UserCustomCliIndex.setStatus('current')
hm2UserCustomCliCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomCliCommand.setStatus('current')
hm2UserCustomCliType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomCliType.setStatus('current')
hm2UserCustomCliStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 1, 20, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserCustomCliStatus.setStatus('current')
hm2PwdMgmtMinLength = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtMinLength.setStatus('current')
hm2PwdMgmtLoginAttempts = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtLoginAttempts.setStatus('current')
hm2PwdMgmtMinUpperCase = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtMinUpperCase.setStatus('current')
hm2PwdMgmtMinLowerCase = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtMinLowerCase.setStatus('current')
hm2PwdMgmtMinNumericNumbers = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtMinNumericNumbers.setStatus('current')
hm2PwdMgmtMinSpecialCharacters = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PwdMgmtMinSpecialCharacters.setStatus('current')
hm2PwdMgmtDefaultPwdStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100))
hm2PwdMgmtDefaultPwdActive = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PwdMgmtDefaultPwdActive.setStatus('current')
hm2PwdMgmtDefaultPwdStatusTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100), )
if mibBuilder.loadTexts: hm2PwdMgmtDefaultPwdStatusTable.setStatus('current')
hm2PwdMgmtDefaultPwdStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1), ).setIndexNames((0, "HM2-USERMGMT-MIB", "hm2PwdMgmtDefaultPwdStatusIndex"))
if mibBuilder.loadTexts: hm2PwdMgmtDefaultPwdStatusEntry.setStatus('current')
hm2PwdMgmtDefaultPwdStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2PwdMgmtDefaultPwdStatusIndex.setStatus('current')
hm2PwdMgmtDefaultPwdStatusUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 2, 100, 100, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PwdMgmtDefaultPwdStatusUserName.setStatus('current')
hm2UserApplicationListTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1), )
if mibBuilder.loadTexts: hm2UserApplicationListTable.setStatus('current')
hm2UserApplicationListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1), ).setIndexNames((1, "HM2-USERMGMT-MIB", "hm2UserApplicationListName"))
if mibBuilder.loadTexts: hm2UserApplicationListEntry.setStatus('current')
hm2UserApplicationListName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hm2UserApplicationListName.setStatus('current')
hm2UserApplicationListAuthListName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserApplicationListAuthListName.setStatus('current')
hm2UserApplicationListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserApplicationListStatus.setStatus('current')
hm2UserAuthListTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1), )
if mibBuilder.loadTexts: hm2UserAuthListTable.setStatus('current')
hm2UserAuthListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1), ).setIndexNames((1, "HM2-USERMGMT-MIB", "hm2UserAuthListName"))
if mibBuilder.loadTexts: hm2UserAuthListEntry.setStatus('current')
hm2UserAuthListName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hm2UserAuthListName.setStatus('current')
hm2UserAuthListPolicy1 = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 2), Hm2UserAuthList().clone('local')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListPolicy1.setStatus('current')
hm2UserAuthListPolicy2 = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 3), Hm2UserAuthList().clone('reject')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListPolicy2.setStatus('current')
hm2UserAuthListPolicy3 = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 4), Hm2UserAuthList().clone('reject')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListPolicy3.setStatus('current')
hm2UserAuthListPolicy4 = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 5), Hm2UserAuthList().clone('reject')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListPolicy4.setStatus('current')
hm2UserAuthListPolicy5 = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 6), Hm2UserAuthList().clone('reject')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListPolicy5.setStatus('current')
hm2UserAuthListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 4, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserAuthListStatus.setStatus('current')
hm2UserIasTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1), )
if mibBuilder.loadTexts: hm2UserIasTable.setStatus('current')
hm2UserIasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1), ).setIndexNames((1, "HM2-USERMGMT-MIB", "hm2UserIasUserName"))
if mibBuilder.loadTexts: hm2UserIasEntry.setStatus('current')
hm2UserIasUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hm2UserIasUserName.setStatus('current')
hm2UserIasUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserIasUserPassword.setStatus('current')
hm2UserIasUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 24, 1, 5, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2UserIasUserStatus.setStatus('current')
hm2UserCreatedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 1)).setObjects(("HM2-USERMGMT-MIB", "hm2UserLastUserCreated"))
if mibBuilder.loadTexts: hm2UserCreatedTrap.setStatus('current')
hm2UserDeletedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 2)).setObjects(("HM2-USERMGMT-MIB", "hm2UserLastUserDeleted"))
if mibBuilder.loadTexts: hm2UserDeletedTrap.setStatus('current')
hm2UserLockedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 3)).setObjects(("HM2-USERMGMT-MIB", "hm2UserName"), ("HM2-USERMGMT-MIB", "hm2UserLockoutStatus"))
if mibBuilder.loadTexts: hm2UserLockedTrap.setStatus('current')
hm2UserPwdChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 4)).setObjects(("HM2-USERMGMT-MIB", "hm2UserName"))
if mibBuilder.loadTexts: hm2UserPwdChangedTrap.setStatus('current')
hm2UserPwdPolicyChkChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 24, 0, 5)).setObjects(("HM2-USERMGMT-MIB", "hm2UserName"), ("HM2-USERMGMT-MIB", "hm2UserPwdPolicyChk"))
if mibBuilder.loadTexts: hm2UserPwdPolicyChkChangedTrap.setStatus('current')
hm2UserMgmtMibSNMPExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 3))
hm2UserMgmtGlobalSESGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1))
hm2UserMgmtUserSESGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2))
hm2UserMgmtApplSESGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3))
hm2UserMgmtAuthSESGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4))
hm2UserMgmtGlobalSESLenCharset = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1, 1))
if mibBuilder.loadTexts: hm2UserMgmtGlobalSESLenCharset.setStatus('current')
hm2UserMgmtGlobalSESPwdLenCharset = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 1, 2))
if mibBuilder.loadTexts: hm2UserMgmtGlobalSESPwdLenCharset.setStatus('current')
hm2UserMgmtUserSESActivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2, 1))
if mibBuilder.loadTexts: hm2UserMgmtUserSESActivate.setStatus('current')
hm2UserMgmtUserSESDeactivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 2, 2))
if mibBuilder.loadTexts: hm2UserMgmtUserSESDeactivate.setStatus('current')
hm2UserMgmtApplSESAddDel = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3, 1))
if mibBuilder.loadTexts: hm2UserMgmtApplSESAddDel.setStatus('current')
hm2UserMgmtApplSESDeactivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 3, 2))
if mibBuilder.loadTexts: hm2UserMgmtApplSESDeactivate.setStatus('current')
hm2UserMgmtAuthSESDuplPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4, 1))
if mibBuilder.loadTexts: hm2UserMgmtAuthSESDuplPolicy.setStatus('current')
hm2UserMgmtAuthSESDeactivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 24, 3, 4, 2))
if mibBuilder.loadTexts: hm2UserMgmtAuthSESDeactivate.setStatus('current')
mibBuilder.exportSymbols("HM2-USERMGMT-MIB", hm2UserLockoutStatus=hm2UserLockoutStatus, hm2UserAuthListName=hm2UserAuthListName, hm2UserMgmtApplSESAddDel=hm2UserMgmtApplSESAddDel, hm2UserMgmtApplSESDeactivate=hm2UserMgmtApplSESDeactivate, hm2PwdMgmtDefaultPwdStatusGroup=hm2PwdMgmtDefaultPwdStatusGroup, hm2PwdMgmtDefaultPwdStatusEntry=hm2PwdMgmtDefaultPwdStatusEntry, hm2UserAuthListPolicy2=hm2UserAuthListPolicy2, hm2UserAuthListStatus=hm2UserAuthListStatus, hm2UserCustomAccessRole2NameEntry=hm2UserCustomAccessRole2NameEntry, hm2UserApplicationListName=hm2UserApplicationListName, hm2UserDeletedTrap=hm2UserDeletedTrap, hm2PwdMgmtDefaultPwdStatusTable=hm2PwdMgmtDefaultPwdStatusTable, hm2UserCustomGroup=hm2UserCustomGroup, hm2UserSnmpAuthType=hm2UserSnmpAuthType, hm2UserAuthListPolicy1=hm2UserAuthListPolicy1, hm2PwdMgmtGroup=hm2PwdMgmtGroup, hm2UserMgmtGlobalSESPwdLenCharset=hm2UserMgmtGlobalSESPwdLenCharset, hm2UserApplicationListGroup=hm2UserApplicationListGroup, hm2UserCreatedTrap=hm2UserCreatedTrap, hm2PwdMgmtMinSpecialCharacters=hm2PwdMgmtMinSpecialCharacters, hm2PwdMgmtMinNumericNumbers=hm2PwdMgmtMinNumericNumbers, hm2PwdMgmtLoginAttempts=hm2PwdMgmtLoginAttempts, hm2UserLastUserCreated=hm2UserLastUserCreated, hm2UserCustomCliStatus=hm2UserCustomCliStatus, hm2UserMgmtMibNotifications=hm2UserMgmtMibNotifications, hm2UserIasUserStatus=hm2UserIasUserStatus, hm2UserAuthListPolicy4=hm2UserAuthListPolicy4, hm2PwdMgmtMinUpperCase=hm2PwdMgmtMinUpperCase, hm2UserCustomCliCommand=hm2UserCustomCliCommand, hm2UserMgmtMib=hm2UserMgmtMib, hm2UserCustomCliCmdInheritTable=hm2UserCustomCliCmdInheritTable, hm2UserPwdChangedTrap=hm2UserPwdChangedTrap, hm2UserPwdPolicyChkChangedTrap=hm2UserPwdPolicyChkChangedTrap, hm2UserMgmtAuthSESDeactivate=hm2UserMgmtAuthSESDeactivate, hm2UserApplicationListEntry=hm2UserApplicationListEntry, hm2UserCustomCliCmdInheritEntry=hm2UserCustomCliCmdInheritEntry, hm2UserIasUserName=hm2UserIasUserName, hm2UserLockedTrap=hm2UserLockedTrap, hm2UserCustomCliCmdEntry=hm2UserCustomCliCmdEntry, hm2UserCustomCliCmdTable=hm2UserCustomCliCmdTable, hm2UserMgmtUserSESGroup=hm2UserMgmtUserSESGroup, hm2PwdMgmtMinLowerCase=hm2PwdMgmtMinLowerCase, hm2UserConfigEntry=hm2UserConfigEntry, hm2UserMgmtUserSESDeactivate=hm2UserMgmtUserSESDeactivate, hm2UserCustomCliIndex=hm2UserCustomCliIndex, hm2UserStatusGroup=hm2UserStatusGroup, hm2UserMgmtUserSESActivate=hm2UserMgmtUserSESActivate, hm2UserIasTable=hm2UserIasTable, hm2UserAuthListGroup=hm2UserAuthListGroup, hm2UserCustomCliBaseAccessRoleStatus=hm2UserCustomCliBaseAccessRoleStatus, hm2UserCustomAccessRole=hm2UserCustomAccessRole, hm2UserApplicationListAuthListName=hm2UserApplicationListAuthListName, hm2UserConfigTable=hm2UserConfigTable, hm2UserCustomCliExecMode=hm2UserCustomCliExecMode, Hm2UserCustomAccessRoles=Hm2UserCustomAccessRoles, hm2PwdMgmtDefaultPwdStatusIndex=hm2PwdMgmtDefaultPwdStatusIndex, hm2UserMgmtGlobalSESGroup=hm2UserMgmtGlobalSESGroup, hm2UserAuthListEntry=hm2UserAuthListEntry, hm2UserAccessRole=hm2UserAccessRole, hm2PwdMgmtMinLength=hm2PwdMgmtMinLength, hm2UserIasEntry=hm2UserIasEntry, Hm2UserCliExecModes=Hm2UserCliExecModes, hm2UserAuthListTable=hm2UserAuthListTable, hm2UserApplicationListStatus=hm2UserApplicationListStatus, hm2PwdMgmtDefaultPwdStatusUserName=hm2PwdMgmtDefaultPwdStatusUserName, hm2UserMgmtMibObjects=hm2UserMgmtMibObjects, hm2UserPwdChangePerm=hm2UserPwdChangePerm, hm2UserIasGroup=hm2UserIasGroup, hm2UserMgmtGlobalSESLenCharset=hm2UserMgmtGlobalSESLenCharset, hm2UserCustomAccessRoleStatus=hm2UserCustomAccessRoleStatus, hm2UserConfigGroup=hm2UserConfigGroup, hm2UserApplicationListTable=hm2UserApplicationListTable, hm2UserIasUserPassword=hm2UserIasUserPassword, hm2UserMgmtAuthSESDuplPolicy=hm2UserMgmtAuthSESDuplPolicy, PYSNMP_MODULE_ID=hm2UserMgmtMib, hm2UserMgmtMibSNMPExtensionGroup=hm2UserMgmtMibSNMPExtensionGroup, hm2UserCustomAccessRoleName=hm2UserCustomAccessRoleName, hm2PwdMgmtDefaultPwdActive=hm2PwdMgmtDefaultPwdActive, hm2UserMgmtApplSESGroup=hm2UserMgmtApplSESGroup, hm2UserCustomCliType=hm2UserCustomCliType, hm2UserPassword=hm2UserPassword, hm2UserCustomCliBaseAccessRole=hm2UserCustomCliBaseAccessRole, hm2UserLastUserDeleted=hm2UserLastUserDeleted, hm2UserCustomAccessRole2NameTable=hm2UserCustomAccessRole2NameTable, hm2UserName=hm2UserName, hm2UserSnmpEncType=hm2UserSnmpEncType, Hm2UserAuthList=Hm2UserAuthList, hm2UserStatus=hm2UserStatus, hm2UserAuthListPolicy5=hm2UserAuthListPolicy5, Hm2UserAccessRoles=Hm2UserAccessRoles, hm2UserPwdPolicyChk=hm2UserPwdPolicyChk, hm2UserAuthListPolicy3=hm2UserAuthListPolicy3, hm2UserMgmtAuthSESGroup=hm2UserMgmtAuthSESGroup)
