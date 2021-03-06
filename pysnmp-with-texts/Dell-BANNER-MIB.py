#
# PySNMP MIB module Dell-BANNER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-BANNER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:55:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, NotificationType, MibIdentifier, Gauge32, IpAddress, Integer32, Counter64, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "NotificationType", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "Counter64", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlBanner = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 133))
rlBanner.setRevisions(('2007-12-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlBanner.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlBanner.setLastUpdated('200803160000Z')
if mibBuilder.loadTexts: rlBanner.setOrganization('Dell')
if mibBuilder.loadTexts: rlBanner.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlBanner.setDescription('The private MIB module definition for Banner displays messages in Dell switching devices. Banner allows users to configure display messages which are displayed on various authentication events. Banner Messages can hold dynamic data such as $(hostname) or $(domain) etc, and display instructions such as: bold, inverse, or blink. Banner Messages can be displayed or hidden with respect to the connection type: via Telnet, SSH or the Console.')
class BannerMessageType(TextualConvention, Integer32):
    description = 'Banner message type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlBannerMOTD", 1), ("rlBannerLogin", 2), ("rlBannerExec", 3))

rlBannerMessageTable = MibTable((1, 3, 6, 1, 4, 1, 89, 133, 1), )
if mibBuilder.loadTexts: rlBannerMessageTable.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageTable.setDescription('The table listing the Banner content.')
rlBannerMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 133, 1, 1), ).setIndexNames((0, "Dell-BANNER-MIB", "rlBannerMessageType"), (0, "Dell-BANNER-MIB", "rlBannerMessageIndex"))
if mibBuilder.loadTexts: rlBannerMessageEntry.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageEntry.setDescription('An entry in the rlBannerMessageTable.')
rlBannerMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 1), BannerMessageType())
if mibBuilder.loadTexts: rlBannerMessageType.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageType.setDescription('This variable identifies the Banner type. There are three types: MOTD, Login and Exec.')
rlBannerMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)))
if mibBuilder.loadTexts: rlBannerMessageIndex.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageIndex.setDescription('This variable identifies a Banner string section in the Banner content. The Banner content is limited to 2000 characters. Content is divided into 13 indexed sections. Each section contains 160 octets, except the last used section which can contain less than 160 octets. Once a section of the Banner string contains 160 octets of data, the user can write to the next index. Overwriting is not supported. To delete all Banner content, use the rlBannerMessageClear MIB.')
rlBannerMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageText.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageText.setDescription('This variable identifies the MIB which holds a section of the Banner content in the table.')
rlBannerManageTable = MibTable((1, 3, 6, 1, 4, 1, 89, 133, 2), )
if mibBuilder.loadTexts: rlBannerManageTable.setStatus('current')
if mibBuilder.loadTexts: rlBannerManageTable.setDescription('The table listing specifying for each connection type which Banner should, or should not be displayed.')
rlBannerManageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 133, 2, 1), ).setIndexNames((0, "Dell-BANNER-MIB", "rlBannerMessageType"))
if mibBuilder.loadTexts: rlBannerManageEntry.setStatus('current')
if mibBuilder.loadTexts: rlBannerManageEntry.setDescription(' An entry in the rlBannerManageTable.')
rlBannerManageSSH = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageSSH.setStatus('current')
if mibBuilder.loadTexts: rlBannerManageSSH.setDescription('This variable specifies whether the banner type specified in the key should or should not be displayed when a user accesses the device via SSH.')
rlBannerManageTelnet = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageTelnet.setStatus('current')
if mibBuilder.loadTexts: rlBannerManageTelnet.setDescription('This variable specifies whether the banner type specified in the key should or should not be displayed when a user accesses the device via Telnet.')
rlBannerManageConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageConsole.setStatus('current')
if mibBuilder.loadTexts: rlBannerManageConsole.setDescription('This variable specifies whether the banner type specified in the key should or should not be displayed when a user accesses the device via Console.')
rlBannerMessageClear = MibScalar((1, 3, 6, 1, 4, 1, 89, 133, 3), BannerMessageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageClear.setStatus('current')
if mibBuilder.loadTexts: rlBannerMessageClear.setDescription('This value, when set, clears the selected Banner type. Clearing the Banner type means that the related entry from rlBannerMessageTable is removed.')
mibBuilder.exportSymbols("Dell-BANNER-MIB", rlBannerManageTelnet=rlBannerManageTelnet, rlBanner=rlBanner, rlBannerMessageType=rlBannerMessageType, rlBannerMessageIndex=rlBannerMessageIndex, rlBannerMessageClear=rlBannerMessageClear, rlBannerManageTable=rlBannerManageTable, rlBannerMessageTable=rlBannerMessageTable, PYSNMP_MODULE_ID=rlBanner, rlBannerMessageText=rlBannerMessageText, rlBannerManageEntry=rlBannerManageEntry, BannerMessageType=BannerMessageType, rlBannerManageSSH=rlBannerManageSSH, rlBannerManageConsole=rlBannerManageConsole, rlBannerMessageEntry=rlBannerMessageEntry)
