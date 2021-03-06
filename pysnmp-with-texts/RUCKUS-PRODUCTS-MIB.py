#
# PySNMP MIB module RUCKUS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ruckusProducts, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusProducts")
RuckusCountryCode, = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusCountryCode")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, Bits, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, ModuleIdentity, Integer32, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "Bits", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32")
DisplayString, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "MacAddress")
ruckusProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 3, 1))
if mibBuilder.loadTexts: ruckusProductsMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusProductsMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusProductsMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusProductsMIB.setDescription('Ruckus product OID registration mib.')
ruckusWirelessRouterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1))
ruckusWirelessAdapterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2))
ruckusWirelessMetroProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3))
ruckusWirelessHotzoneProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4))
ruckusWirelessControllerProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5))
ruckusVF2825 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1))
ruckusVF2811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 2))
ruckusVF2821 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 3))
ruckusVF2835 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 4))
ruckusVF7811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 5))
ruckusVF2111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 1))
ruckusVF2121 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 2))
ruckusVF7111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 3))
ruckusMM2225 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 1))
ruckusMM2211 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 2))
ruckusMM2221 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 3))
ruckusZF2925 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 1))
ruckusZF2942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 2))
ruckusZF7942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 3))
ruckusZF7962 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 4))
ruckusZF2741 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 5))
ruckusZF7762 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 6))
ruckusZF7762S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 8))
ruckusZF7762T = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 9))
ruckusZF7762N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 10))
ruckusZF7343 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 12))
ruckusZF7363 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 13))
ruckusZF7341 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 14))
ruckusZF7731 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 16))
ruckusZF7025 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 20))
ruckusZF7321 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 22))
ruckusZF7321U = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 23))
ruckusZF2741EXT = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 24))
ruckusZF7982 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 25))
ruckusZF7782 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 28))
ruckusZF7782S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 29))
ruckusZF7782N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 30))
ruckusZF7782E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 31))
ruckusZF8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 32))
ruckusZF7762AC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 35))
ruckusZF7762SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 36))
ruckusZF7762TAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 37))
ruckusZF7372 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 40))
ruckusZF7372E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 41))
ruckusZF7352 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 45))
ruckusZF7351 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 48))
ruckusZF7742 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 50))
ruckusZF7055 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 52))
ruckusZF7781M = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 55))
ruckusZF7781CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 56))
ruckusZF7781CME = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 57))
ruckusZF7781CMS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 58))
ruckusZF7781FN = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 60))
ruckusZF7781FNE = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 61))
ruckusZF7781FNS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 62))
ruckusSC8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 65))
ruckusSC8800S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 66))
ruckusZF7761CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7))
ruckusZF7761CMControlLED = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("ledPerCM", 1), ("ledPerAP", 2), ("ledAlternateMode1Mode2OneHour", 3), ("ledAlternateMode1Mode2Mode6", 4), ("blueActive", 5), ("blueActiveCMOnlineLed", 6), ("ledAllOff", 7), ("heartbeatOffCM", 8), ("heartbeatOffAP", 9), ("softResetAP", 10), ("powerCycleAP", 11), ("factoryResetAP", 12), ("softResetCM", 13), ("powerCycleCM", 14), ("factoryResetCM", 15))).clone('ledPerCM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMControlLED.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMControlLED.setDescription('ledPerCM(1): LEDs enabled per Cable Modem definition, ledPerAP(2): LEDs configured per Access Point definition, ledAlternateMode1Mode2OneHour(3): Alternalte between modes 1 and 2 at a 30 second period then disabled after one hour, ledAlternateMode1Mode2Mode6(4): Alternalte between modes 1 and 2 at a 30 second period and then go to mode 6 blueActive(5): Blue Active Surge Protection Indicator, blueActiveCMOnlineLed(6): Blue Active Surge Protection Indicator and Cable Modem online Green LED enabled, ledAllOff(7): All LEDs disabled, heartbeatOffCM(8): Disable Cable Modem heartbeat monitoring, heartbeatOffAP(9): Disable Access Point heartbeat monitoring, softResetAP(10): Soft reset of Access Point, powerCycleAP(11): Power cycle Access Point, factoryResetAP(12): Reset Access Point to factory defaults, softResetCM(13): Soft reset of Cable Modem, powerCycleCM(14): Power cycle Cable Modem, factoryResetCM(15): Reset Cable Modem to factory defaults')
ruckusZF7761CMWanIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZF7761CMWanIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMWanIPAddr.setDescription('Specifies the IP address of the Cable Modem WAN interface.')
ruckusZF7761CMCustomization = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5))
ruckusZF7761CMHTTPService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHTTPService.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMHTTPService.setDescription('Enable/disable HTTP service.')
ruckusZF7761CMTelnetService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMTelnetService.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMTelnetService.setDescription('Enable/disable Telnet service.')
ruckusZF7761CMSSHService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMSSHService.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMSSHService.setDescription('Enable/disable SSH service.')
ruckusZF7761CMUsername = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMUsername.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMUsername.setDescription('Specifies username of cable modem. ')
ruckusZF7761CMPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMPassword.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMPassword.setDescription('Specifies password of cable modem. ')
ruckusZF7761CMLEDMode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ledAllOff", 0), ("blueActive", 1), ("blueActiveCMOnlineLed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMLEDMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMLEDMode.setDescription('ledAllOff(0): All LEDs disabled after 3 second delay, blueActive(1): Blue Active Surge Protection Indicator, blueActiveCMOnlineLed(2): Blue Active Surge Protection Indicator and Cable Modem online Green LED enabled')
ruckusZF7761CMHeartbeatMonitorCM = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorCM.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorCM.setDescription('Enable/disable Cable Modem heartbeat monitoring.')
ruckusZF7761CMHeartbeatMonitorAP = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorAP.setStatus('current')
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorAP.setDescription('Enable/disable Access Point heartbeat monitoring.')
ruckusZD1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1))
ruckusZD1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2))
ruckusZD3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3))
ruckusZD5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8))
ruckusZD1000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemName.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemName.setDescription('System name')
ruckusZD1000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemIPAddr.setDescription('IP Address')
ruckusZD1000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemMacAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemMacAddr.setDescription('MAC Address')
ruckusZD1000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemUptime.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemUptime.setDescription('Up time')
ruckusZD1000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemModel.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemModel.setDescription('Model')
ruckusZD1000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemLicensedAPs.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemLicensedAPs.setDescription('Licensed APs')
ruckusZD1000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemSerialNumber.setDescription('Serial number')
ruckusZD1000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000SystemVersion.setDescription('Software version')
ruckusZD1000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000CountryCode.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1000CountryCode.setDescription('Country code')
ruckusZD1100SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemName.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemName.setDescription('System name')
ruckusZD1100SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemIPAddr.setDescription('IP Address')
ruckusZD1100SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemMacAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemMacAddr.setDescription('MAC Address')
ruckusZD1100SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemUptime.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemUptime.setDescription('Up time')
ruckusZD1100SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemModel.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemModel.setDescription('Model')
ruckusZD1100SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemLicensedAPs.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemLicensedAPs.setDescription('Licensed APs')
ruckusZD1100SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemSerialNumber.setDescription('Serial number')
ruckusZD1100SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100SystemVersion.setDescription('Software version')
ruckusZD1100CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100CountryCode.setStatus('current')
if mibBuilder.loadTexts: ruckusZD1100CountryCode.setDescription('Country code')
ruckusZD3000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemName.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemName.setDescription('System name')
ruckusZD3000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemIPAddr.setDescription('IP Address')
ruckusZD3000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemMacAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemMacAddr.setDescription('MAC Address')
ruckusZD3000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemUptime.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemUptime.setDescription('Up time')
ruckusZD3000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemModel.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemModel.setDescription('Model')
ruckusZD3000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemLicensedAPs.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemLicensedAPs.setDescription('Licensed APs')
ruckusZD3000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemSerialNumber.setDescription('Serial number')
ruckusZD3000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000SystemVersion.setDescription('Software version')
ruckusZD3000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000CountryCode.setStatus('current')
if mibBuilder.loadTexts: ruckusZD3000CountryCode.setDescription('Country code')
ruckusZD5000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemName.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemName.setDescription('System name')
ruckusZD5000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemIPAddr.setDescription('IP Address')
ruckusZD5000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemMacAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemMacAddr.setDescription('MAC Address')
ruckusZD5000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemUptime.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemUptime.setDescription('Up time')
ruckusZD5000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemModel.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemModel.setDescription('Model')
ruckusZD5000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemLicensedAPs.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemLicensedAPs.setDescription('Licensed APs')
ruckusZD5000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemSerialNumber.setDescription('Serial number')
ruckusZD5000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000SystemVersion.setDescription('Software version')
ruckusZD5000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000CountryCode.setStatus('current')
if mibBuilder.loadTexts: ruckusZD5000CountryCode.setDescription('Country code')
mibBuilder.exportSymbols("RUCKUS-PRODUCTS-MIB", ruckusZD1000SystemIPAddr=ruckusZD1000SystemIPAddr, ruckusZF7781FN=ruckusZF7781FN, ruckusZD3000SystemSerialNumber=ruckusZD3000SystemSerialNumber, ruckusZD1000SystemName=ruckusZD1000SystemName, ruckusZF2942=ruckusZF2942, ruckusZF7962=ruckusZF7962, ruckusZF7781FNE=ruckusZF7781FNE, ruckusProductsMIB=ruckusProductsMIB, ruckusZF7762S=ruckusZF7762S, ruckusZF7781CM=ruckusZF7781CM, ruckusWirelessHotzoneProducts=ruckusWirelessHotzoneProducts, ruckusVF2821=ruckusVF2821, ruckusZF7782N=ruckusZF7782N, ruckusSC8800S=ruckusSC8800S, ruckusZD5000SystemMacAddr=ruckusZD5000SystemMacAddr, ruckusZF7761CM=ruckusZF7761CM, ruckusZF7762=ruckusZF7762, ruckusZD1000SystemUptime=ruckusZD1000SystemUptime, ruckusZD1000=ruckusZD1000, ruckusZD5000SystemName=ruckusZD5000SystemName, ruckusZD5000SystemIPAddr=ruckusZD5000SystemIPAddr, ruckusZF7761CMHeartbeatMonitorAP=ruckusZF7761CMHeartbeatMonitorAP, ruckusZD5000SystemUptime=ruckusZD5000SystemUptime, ruckusZD5000=ruckusZD5000, ruckusZD1100=ruckusZD1100, ruckusVF2825=ruckusVF2825, ruckusZD1100SystemName=ruckusZD1100SystemName, ruckusWirelessControllerProducts=ruckusWirelessControllerProducts, ruckusWirelessMetroProducts=ruckusWirelessMetroProducts, ruckusZF7363=ruckusZF7363, ruckusZF7761CMSSHService=ruckusZF7761CMSSHService, ruckusMM2221=ruckusMM2221, ruckusZF2741=ruckusZF2741, ruckusZF7761CMCustomization=ruckusZF7761CMCustomization, ruckusZF7762TAC=ruckusZF7762TAC, ruckusZF8800SAC=ruckusZF8800SAC, ruckusZD3000SystemModel=ruckusZD3000SystemModel, ruckusVF2811=ruckusVF2811, ruckusZF7982=ruckusZF7982, ruckusZD5000SystemSerialNumber=ruckusZD5000SystemSerialNumber, ruckusZD1100SystemModel=ruckusZD1100SystemModel, ruckusZF7761CMHTTPService=ruckusZF7761CMHTTPService, ruckusZD1100SystemIPAddr=ruckusZD1100SystemIPAddr, ruckusZF7781M=ruckusZF7781M, ruckusZD5000CountryCode=ruckusZD5000CountryCode, ruckusZF7742=ruckusZF7742, ruckusZF7781CME=ruckusZF7781CME, ruckusZF7942=ruckusZF7942, ruckusZF7761CMUsername=ruckusZF7761CMUsername, ruckusZD1100SystemLicensedAPs=ruckusZD1100SystemLicensedAPs, ruckusSC8800SAC=ruckusSC8800SAC, ruckusVF7811=ruckusVF7811, ruckusMM2225=ruckusMM2225, ruckusZD3000CountryCode=ruckusZD3000CountryCode, ruckusZD5000SystemModel=ruckusZD5000SystemModel, ruckusZF7055=ruckusZF7055, ruckusVF2111=ruckusVF2111, ruckusZF7782S=ruckusZF7782S, ruckusZF7782E=ruckusZF7782E, ruckusZD1000SystemModel=ruckusZD1000SystemModel, PYSNMP_MODULE_ID=ruckusProductsMIB, ruckusZF7343=ruckusZF7343, ruckusZF7731=ruckusZF7731, ruckusZD5000SystemLicensedAPs=ruckusZD5000SystemLicensedAPs, ruckusZF7761CMPassword=ruckusZF7761CMPassword, ruckusZD3000SystemMacAddr=ruckusZD3000SystemMacAddr, ruckusZF7321U=ruckusZF7321U, ruckusVF7111=ruckusVF7111, ruckusZF7025=ruckusZF7025, ruckusZD1000SystemSerialNumber=ruckusZD1000SystemSerialNumber, ruckusWirelessAdapterProducts=ruckusWirelessAdapterProducts, ruckusZF7351=ruckusZF7351, ruckusZF7761CMTelnetService=ruckusZF7761CMTelnetService, ruckusZF7761CMLEDMode=ruckusZF7761CMLEDMode, ruckusZD1100SystemSerialNumber=ruckusZD1100SystemSerialNumber, ruckusZD1000CountryCode=ruckusZD1000CountryCode, ruckusZF7782=ruckusZF7782, ruckusZD1100SystemMacAddr=ruckusZD1100SystemMacAddr, ruckusZF7352=ruckusZF7352, ruckusZF7762SAC=ruckusZF7762SAC, ruckusZF7761CMHeartbeatMonitorCM=ruckusZF7761CMHeartbeatMonitorCM, ruckusZF7762T=ruckusZF7762T, ruckusZF7781CMS=ruckusZF7781CMS, ruckusZD3000=ruckusZD3000, ruckusZD3000SystemUptime=ruckusZD3000SystemUptime, ruckusZD3000SystemVersion=ruckusZD3000SystemVersion, ruckusVF2835=ruckusVF2835, ruckusZF7761CMControlLED=ruckusZF7761CMControlLED, ruckusZF2925=ruckusZF2925, ruckusZD1100SystemUptime=ruckusZD1100SystemUptime, ruckusZD1100SystemVersion=ruckusZD1100SystemVersion, ruckusZD5000SystemVersion=ruckusZD5000SystemVersion, ruckusZD1000SystemMacAddr=ruckusZD1000SystemMacAddr, ruckusMM2211=ruckusMM2211, ruckusZD3000SystemLicensedAPs=ruckusZD3000SystemLicensedAPs, ruckusZD3000SystemName=ruckusZD3000SystemName, ruckusZF7321=ruckusZF7321, ruckusZF7762AC=ruckusZF7762AC, ruckusZF7762N=ruckusZF7762N, ruckusZF2741EXT=ruckusZF2741EXT, ruckusWirelessRouterProducts=ruckusWirelessRouterProducts, ruckusZF7372=ruckusZF7372, ruckusZF7372E=ruckusZF7372E, ruckusZF7761CMWanIPAddr=ruckusZF7761CMWanIPAddr, ruckusZD3000SystemIPAddr=ruckusZD3000SystemIPAddr, ruckusZD1100CountryCode=ruckusZD1100CountryCode, ruckusZF7781FNS=ruckusZF7781FNS, ruckusVF2121=ruckusVF2121, ruckusZF7341=ruckusZF7341, ruckusZD1000SystemVersion=ruckusZD1000SystemVersion, ruckusZD1000SystemLicensedAPs=ruckusZD1000SystemLicensedAPs)
