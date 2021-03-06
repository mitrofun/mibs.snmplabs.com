#
# PySNMP MIB module COLUBRIS-VIRTUAL-AP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-VIRTUAL-AP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisUsersAuthenticationMode, ColubrisSSID, ColubrisPriorityQueue, ColubrisSecurity, ColubrisProfileIndexOrZero = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisUsersAuthenticationMode", "ColubrisSSID", "ColubrisPriorityQueue", "ColubrisSecurity", "ColubrisProfileIndexOrZero")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Bits, iso, ObjectIdentity, IpAddress, NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
colubrisVirtualApMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 11))
if mibBuilder.loadTexts: colubrisVirtualApMIB.setLastUpdated('200607250000Z')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisVirtualApMIB.setDescription('Colubris Networks Virtual Access Point MIB.')
colubrisVirtualApMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1))
coVirtualApConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1))
coVirtualAccessPointConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1), )
if mibBuilder.loadTexts: coVirtualAccessPointConfigTable.setStatus('current')
if mibBuilder.loadTexts: coVirtualAccessPointConfigTable.setDescription('VSC configuration attributes. In tabular form to allow for multiple instances.')
coVirtualAccessPointConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApWlanProfileIndex"))
if mibBuilder.loadTexts: coVirtualAccessPointConfigEntry.setStatus('current')
if mibBuilder.loadTexts: coVirtualAccessPointConfigEntry.setDescription('An entry in the coVirtualAccessPointConfigTable. ifIndex - Each 802.11 interface is represented by an ifEntry. Interface tables in this MIB module are indexed by ifIndex. coVirtualWlanProfileIndex - Uniquely access a profile for this particular 802.11 interface.')
coVirtualApWlanProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVirtualApWlanProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApWlanProfileIndex.setDescription('Specifies the index of the VSC profile.')
coVirtualApSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 2), ColubrisSSID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApSSID.setStatus('current')
if mibBuilder.loadTexts: coVirtualApSSID.setDescription('Service Set ID assigned to the VSC. This value must be unique per radio interface.')
coVirtualApBroadcastSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApBroadcastSSID.setStatus('current')
if mibBuilder.loadTexts: coVirtualApBroadcastSSID.setDescription('Specifies if the SSID is included in beacon frames.')
coVirtualApMaximumNumberOfUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApMaximumNumberOfUsers.setStatus('current')
if mibBuilder.loadTexts: coVirtualApMaximumNumberOfUsers.setDescription('Specifies the maximum number of concurrent users that this profile can accept.')
coVirtualApDefaultVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApDefaultVLAN.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultVLAN.setDescription('Specifies the default VLAN to use for this profile when no RADIUS authentication has taken place. The value 0 is used when no VLAN has been assigned to this profile. Writing to this object is only available on APs.')
coVirtualApSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 6), ColubrisSecurity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApSecurity.setStatus('current')
if mibBuilder.loadTexts: coVirtualApSecurity.setDescription('Identifies all supported authentication/encryption algorithms.')
coVirtualApAuthenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 7), ColubrisUsersAuthenticationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApAuthenMode.setStatus('current')
if mibBuilder.loadTexts: coVirtualApAuthenMode.setDescription('Identifies if user authentication is performed locally or via an external authentication server.')
coVirtualApAuthenProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 8), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApAuthenProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApAuthenProfileIndex.setDescription("Specifies the authentication server profile to use for user authentication. This parameter only applies when the coVirtualApSecurity is set to 'wpa' or 'ieee802dot1x' and coVirtualApAuthenMode is set to 'profile' or 'localAndProfile'. When set to zero, no authentication server profile is selected or on a AP it could represent a pre-configured authentication profile.")
coVirtualApUserAccountingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApUserAccountingEnabled.setStatus('current')
if mibBuilder.loadTexts: coVirtualApUserAccountingEnabled.setDescription('Indicates if accounting information is generated by the device and sent to the authentication server for connected users. Accounting information will be generated only if a valid authentication server profile is configured for the coVirtualApAccountingProfileIndex attribute.')
coVirtualApUserAccountingProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 10), ColubrisProfileIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApUserAccountingProfileIndex.setStatus('current')
if mibBuilder.loadTexts: coVirtualApUserAccountingProfileIndex.setDescription('Identifies the authentication server profile to be used for accounting information. The special value Zero indicates that no accounting profile is selected.')
coVirtualApDefaultUserRateLimitationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserRateLimitationEnabled.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserRateLimitationEnabled.setDescription('Indicates if the default user rate limitation is enabled.')
coVirtualApDefaultUserMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxTransmitRate.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxTransmitRate.setDescription('Identifies the default user maximum transmit rate.')
coVirtualApDefaultUserMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxReceiveRate.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserMaxReceiveRate.setDescription('Identifies the default user maximum receive rate.')
coVirtualApDefaultUserBandwidthLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 14), ColubrisPriorityQueue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVirtualApDefaultUserBandwidthLevel.setStatus('current')
if mibBuilder.loadTexts: coVirtualApDefaultUserBandwidthLevel.setDescription('Identifies the default user bandwidth level.')
coVirtualApOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 11, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coVirtualApOperState.setStatus('current')
if mibBuilder.loadTexts: coVirtualApOperState.setDescription('Activate/Deactivate the VSC on the radio.')
colubrisVirtualApMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2))
colubrisVirtualApMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 1))
colubrisVirtualApMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 2))
colubrisVirtualApMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 1, 1)).setObjects(("COLUBRIS-VIRTUAL-AP-MIB", "colubrisVirtualApMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVirtualApMIBCompliance = colubrisVirtualApMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisVirtualApMIBCompliance.setDescription('The compliance statement for the Virtual Access Point MIB.')
colubrisVirtualApMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 11, 2, 2, 1)).setObjects(("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApSSID"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApBroadcastSSID"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApMaximumNumberOfUsers"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultVLAN"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApSecurity"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApAuthenMode"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApAuthenProfileIndex"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApUserAccountingEnabled"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApUserAccountingProfileIndex"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserRateLimitationEnabled"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxTransmitRate"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxReceiveRate"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApDefaultUserBandwidthLevel"), ("COLUBRIS-VIRTUAL-AP-MIB", "coVirtualApOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVirtualApMIBGroup = colubrisVirtualApMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisVirtualApMIBGroup.setDescription('A collection of objects for use with Virtual Access Points.')
mibBuilder.exportSymbols("COLUBRIS-VIRTUAL-AP-MIB", PYSNMP_MODULE_ID=colubrisVirtualApMIB, coVirtualApSecurity=coVirtualApSecurity, colubrisVirtualApMIBCompliance=colubrisVirtualApMIBCompliance, coVirtualApUserAccountingEnabled=coVirtualApUserAccountingEnabled, coVirtualApDefaultUserRateLimitationEnabled=coVirtualApDefaultUserRateLimitationEnabled, colubrisVirtualApMIBObjects=colubrisVirtualApMIBObjects, colubrisVirtualApMIBGroup=colubrisVirtualApMIBGroup, colubrisVirtualApMIBCompliances=colubrisVirtualApMIBCompliances, coVirtualApMaximumNumberOfUsers=coVirtualApMaximumNumberOfUsers, coVirtualApWlanProfileIndex=coVirtualApWlanProfileIndex, colubrisVirtualApMIBGroups=colubrisVirtualApMIBGroups, coVirtualApSSID=coVirtualApSSID, coVirtualAccessPointConfigEntry=coVirtualAccessPointConfigEntry, colubrisVirtualApMIB=colubrisVirtualApMIB, coVirtualApDefaultUserBandwidthLevel=coVirtualApDefaultUserBandwidthLevel, coVirtualApBroadcastSSID=coVirtualApBroadcastSSID, coVirtualApOperState=coVirtualApOperState, coVirtualApConfig=coVirtualApConfig, coVirtualApDefaultUserMaxTransmitRate=coVirtualApDefaultUserMaxTransmitRate, colubrisVirtualApMIBConformance=colubrisVirtualApMIBConformance, coVirtualAccessPointConfigTable=coVirtualAccessPointConfigTable, coVirtualApUserAccountingProfileIndex=coVirtualApUserAccountingProfileIndex, coVirtualApAuthenProfileIndex=coVirtualApAuthenProfileIndex, coVirtualApAuthenMode=coVirtualApAuthenMode, coVirtualApDefaultVLAN=coVirtualApDefaultVLAN, coVirtualApDefaultUserMaxReceiveRate=coVirtualApDefaultUserMaxReceiveRate)
