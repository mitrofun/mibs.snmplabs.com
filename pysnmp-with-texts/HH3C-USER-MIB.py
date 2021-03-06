#
# PySNMP MIB module HH3C-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-USER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Gauge32, Bits, MibIdentifier, ObjectIdentity, Counter64, iso, ModuleIdentity, NotificationType, Integer32, Unsigned32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "MibIdentifier", "ObjectIdentity", "Counter64", "iso", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DateAndTime, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "DisplayString", "MacAddress")
hh3cUser = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 12))
if mibBuilder.loadTexts: hh3cUser.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hh3cUser.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cUser.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cUser.setDescription(' This MIB contains objects to Manage configuration and Monitor running state for userlog feature. ')
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ServiceType(TextualConvention, Integer32):
    description = 'enable (1) disable (2) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

hh3cUserObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1))
hh3cUserInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1), )
if mibBuilder.loadTexts: hh3cUserInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserInfoTable.setDescription(' Local User Info Table ')
hh3cUserInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1), ).setIndexNames((0, "HH3C-USER-MIB", "hh3cUserIndex"))
if mibBuilder.loadTexts: hh3cUserInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserInfoEntry.setDescription(' The entry of hh3cUserInfoTable ')
hh3cUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserName.setStatus('current')
if mibBuilder.loadTexts: hh3cUserName.setDescription(' The name of local user, it must be unique. ')
hh3cUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserPassword.setStatus('current')
if mibBuilder.loadTexts: hh3cUserPassword.setDescription(' The password of local user, default is null. ')
hh3cAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cAuthMode.setStatus('current')
if mibBuilder.loadTexts: hh3cAuthMode.setDescription(' The encrypting type of password: 0 : password simple, means password is clean text. 7 : password cipher, means password is encrypted text. default is 0. ')
hh3cUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cUserLevel.setDescription(' The privilege of local user the value range is from 0 to 3, and 0 is minimum, 3 is maximum. default is 0. ')
hh3cUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("block", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserState.setStatus('current')
if mibBuilder.loadTexts: hh3cUserState.setDescription(' The state of local user 0: active, means local user can execute any operations that he has privilege to do. 1: block, means local user can not execute any operations. default is active. ')
hh3cUserInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserInfoRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cUserInfoRowStatus.setDescription(' The status of this conceptual row. Now only support CreateAndGo and Destroy and Active. ')
hh3cUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 1, 1, 7), Integer32())
if mibBuilder.loadTexts: hh3cUserIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cUserIndex.setDescription(' The index of local user ')
hh3cUserAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2), )
if mibBuilder.loadTexts: hh3cUserAttributeTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserAttributeTable.setDescription(' Local User Attribute Table. if there are data in hh3cUserInfoTable, this table should have the relevant data. this table only support query and modify, but not support create and delete operations. ')
hh3cUserAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1), ).setIndexNames((0, "HH3C-USER-MIB", "hh3cUserIndex"))
if mibBuilder.loadTexts: hh3cUserAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserAttributeEntry.setDescription('The entry of hh3cUserAttributeTable ')
hh3cAccessLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cAccessLimit.setStatus('current')
if mibBuilder.loadTexts: hh3cAccessLimit.setDescription(' The maximum user number of current user who can access devices. default is 0, means no limit. ')
hh3cIdleCut = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIdleCut.setStatus('current')
if mibBuilder.loadTexts: hh3cIdleCut.setDescription(' Valid idle time out(second): 60..7200, default is 0, means disable idle time out. ')
hh3cIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIPAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cIPAddress.setDescription(" Set local user's ip address. default is 0.0.0.0 ")
hh3cNasIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNasIPAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cNasIPAddress.setDescription(" Set local user's ip address of network access server. default is 127.0.0.1, means local machine. ")
hh3cSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSlotNum.setStatus('current')
if mibBuilder.loadTexts: hh3cSlotNum.setDescription(" Set local user's slot. default is 0. ")
hh3cSubSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSubSlotNum.setStatus('current')
if mibBuilder.loadTexts: hh3cSubSlotNum.setDescription(" Set local user's sub-slot. default is 0. ")
hh3cPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortNum.setStatus('current')
if mibBuilder.loadTexts: hh3cPortNum.setDescription(" Set local user's port number. 0 is an insignificant value for initial status. ")
hh3cMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMacAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cMacAddress.setDescription(" Set local user's mac address. default is 0-0-0, means the local user do not bind any mac address. ")
hh3cVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVlan.setStatus('current')
if mibBuilder.loadTexts: hh3cVlan.setDescription(" Set local user's vlan id. the value range is from 0 to 4094. default is 0, means the local user is not in any vlan. ")
hh3cFtpService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 10), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFtpService.setStatus('current')
if mibBuilder.loadTexts: hh3cFtpService.setDescription(' FTP service: enable Setting this object to the value enable has the effect of enabling the FTP service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the FTP service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cFtpDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFtpDirectory.setStatus('current')
if mibBuilder.loadTexts: hh3cFtpDirectory.setDescription(' Directory of FTP user. default is null, means if local user has the privilege of ftp service. ')
hh3cLanAccessService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 12), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLanAccessService.setStatus('current')
if mibBuilder.loadTexts: hh3cLanAccessService.setDescription(' Lan Access service: enable Setting this object to the value enable has the effect of enabling the lan access service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the lan access service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cSshService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 13), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSshService.setStatus('current')
if mibBuilder.loadTexts: hh3cSshService.setDescription(' SSH service: enable Setting this object to the value enable has the effect of enabling the SSH service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the SSH service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cTelnetService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 14), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cTelnetService.setStatus('current')
if mibBuilder.loadTexts: hh3cTelnetService.setDescription(' Telnet service: enable Setting this object to the value enable has the effect of enabling the TELNET service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the TELNET service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cTerminalService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 15), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cTerminalService.setStatus('current')
if mibBuilder.loadTexts: hh3cTerminalService.setDescription(' Terminal service: enable Setting this object to the value enable has the effect of enabling the terminal service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the terminal service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 16), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExpirationDate.setStatus('current')
if mibBuilder.loadTexts: hh3cExpirationDate.setDescription(" Expired date of user. The default value is 0-0-0,0:0:0.0, and means it doesn't expire for ever. ")
hh3cUserGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cUserGroup.setDescription(" The user group that user belongs to. Any user must belong to a user group. The default group is the 'system' group. The maximum length of the group name is 80. ")
hh3cPortalService = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 2, 1, 18), ServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortalService.setStatus('current')
if mibBuilder.loadTexts: hh3cPortalService.setDescription(' Portal service: enable Setting this object to the value enable has the effect of enabling the portal service for the corresponding entry in the hh3cUserAttributeTable. disable Setting this object to the value disable has the effect of disabling the portal service for the corresponding entry in the hh3cUserAttributeTable. The default value is disable. ')
hh3cUserMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserMaxNum.setStatus('current')
if mibBuilder.loadTexts: hh3cUserMaxNum.setDescription(' This object contains the maximum number of local users. ')
hh3cUserCurrNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserCurrNum.setStatus('current')
if mibBuilder.loadTexts: hh3cUserCurrNum.setDescription(' This object contains the current number of local users. ')
hh3cUserIndexIndicator = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserIndexIndicator.setStatus('current')
if mibBuilder.loadTexts: hh3cUserIndexIndicator.setDescription(' This object contains an appropriate value to be used for hh3cUserIndex when creating entries in the hh3cUserInfoTable. The value 0 indicates that no unassigned entries are available. To obtain the hh3cUserIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object. After each retrieval, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse. ')
hh3cUserGroupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 12, 2))
hh3cUserGroupInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1), )
if mibBuilder.loadTexts: hh3cUserGroupInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserGroupInfoTable.setDescription(' User group information table. ')
hh3cUserGroupInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1), ).setIndexNames((0, "HH3C-USER-MIB", "hh3cUserGroupName"))
if mibBuilder.loadTexts: hh3cUserGroupInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserGroupInfoEntry.setDescription(' The entry of hh3cUserGroupInfoTable. ')
hh3cUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: hh3cUserGroupName.setStatus('current')
if mibBuilder.loadTexts: hh3cUserGroupName.setDescription(' The index of user group. ')
hh3cUserGroupInfoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 12, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cUserGroupInfoRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cUserGroupInfoRowStatus.setDescription(' The status of this conceptual row. Only support createAndGo, destroy and active. ')
mibBuilder.exportSymbols("HH3C-USER-MIB", hh3cUserGroupInfoEntry=hh3cUserGroupInfoEntry, hh3cNasIPAddress=hh3cNasIPAddress, hh3cPortNum=hh3cPortNum, hh3cFtpService=hh3cFtpService, hh3cUserGroupInfoTable=hh3cUserGroupInfoTable, hh3cMacAddress=hh3cMacAddress, hh3cSshService=hh3cSshService, hh3cPortalService=hh3cPortalService, hh3cSlotNum=hh3cSlotNum, hh3cUserMaxNum=hh3cUserMaxNum, hh3cIPAddress=hh3cIPAddress, hh3cUserInfoTable=hh3cUserInfoTable, hh3cUserAttributeTable=hh3cUserAttributeTable, hh3cIdleCut=hh3cIdleCut, hh3cUserObjects=hh3cUserObjects, hh3cExpirationDate=hh3cExpirationDate, hh3cUserInfoRowStatus=hh3cUserInfoRowStatus, hh3cFtpDirectory=hh3cFtpDirectory, hh3cUserLevel=hh3cUserLevel, hh3cAuthMode=hh3cAuthMode, hh3cUserGroup=hh3cUserGroup, hh3cUserPassword=hh3cUserPassword, hh3cTelnetService=hh3cTelnetService, ServiceType=ServiceType, hh3cVlan=hh3cVlan, hh3cSubSlotNum=hh3cSubSlotNum, hh3cAccessLimit=hh3cAccessLimit, PYSNMP_MODULE_ID=hh3cUser, hh3cUserGroupObjects=hh3cUserGroupObjects, hh3cUserGroupName=hh3cUserGroupName, hh3cUserIndex=hh3cUserIndex, hh3cUserState=hh3cUserState, hh3cUserCurrNum=hh3cUserCurrNum, hh3cUserName=hh3cUserName, hh3cUserAttributeEntry=hh3cUserAttributeEntry, hh3cUserIndexIndicator=hh3cUserIndexIndicator, DisplayString=DisplayString, hh3cLanAccessService=hh3cLanAccessService, hh3cUser=hh3cUser, hh3cUserInfoEntry=hh3cUserInfoEntry, hh3cTerminalService=hh3cTerminalService, hh3cUserGroupInfoRowStatus=hh3cUserGroupInfoRowStatus)
