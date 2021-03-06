#
# PySNMP MIB module DKSF-54-1-X-X-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-54-1-X-X-1
# Produced by pysmi-0.3.4 at Wed May  1 12:47:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Unsigned32, Gauge32, Bits, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, iso, Integer32, Counter32, Counter64, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "iso", "Integer32", "Counter32", "Counter64", "NotificationType", "enterprises")
TextualConvention, DisplayString, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "TimeStamp")
netPing4Pwr = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 54))
netPing4Pwr.setRevisions(('2015-03-02 00:00', '2014-06-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netPing4Pwr.setRevisionsDescriptions(('npRelHumidity branch added npGsmSendSms variable added npRelayMode values redefined', 'Initial release',))
if mibBuilder.loadTexts: netPing4Pwr.setLastUpdated('201503020000Z')
if mibBuilder.loadTexts: netPing4Pwr.setOrganization('Alentis Electronics')
if mibBuilder.loadTexts: netPing4Pwr.setContactInfo('developers@netping.ru')
if mibBuilder.loadTexts: netPing4Pwr.setDescription('MIB for NetPing 4PWR-220/SMS remote sensing and control')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5500))
npRelayTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5500, 5), )
if mibBuilder.loadTexts: npRelayTable.setStatus('current')
if mibBuilder.loadTexts: npRelayTable.setDescription('Watchdog and outlet/relay control table')
npRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1), ).setIndexNames((0, "DKSF-54-1-X-X-1", "npRelayN"))
if mibBuilder.loadTexts: npRelayEntry.setStatus('current')
if mibBuilder.loadTexts: npRelayEntry.setDescription('Relay/outlet table row')
npRelayN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayN.setStatus('current')
if mibBuilder.loadTexts: npRelayN.setDescription('The N of output relay')
npRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flip", -1), ("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayMode.setStatus('current')
if mibBuilder.loadTexts: npRelayMode.setDescription('Control of relay: -1 - flip between on(1) and off(0) 0 - manual off 1 - manual on 2 - watchdog 3 - schedule 4 - both schedule and watchdog (while switched on by schedule) 5 - logic')
npRelayStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayStartReset.setStatus('current')
if mibBuilder.loadTexts: npRelayStartReset.setDescription('Write 1 to start reset (switch relay off for some time)')
npRelayMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayMemo.setStatus('current')
if mibBuilder.loadTexts: npRelayMemo.setDescription('Relay memo')
npRelayFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("flip", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayFlip.setStatus('current')
if mibBuilder.loadTexts: npRelayFlip.setDescription('Write -1 to flip between manual on and manual off states of relay')
npRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayState.setStatus('current')
if mibBuilder.loadTexts: npRelayState.setDescription('Actual relay state at the moment, regardless of source of control. 0 - relay is off 1 - relay is on')
npRelayPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayPowered.setStatus('current')
if mibBuilder.loadTexts: npRelayPowered.setDescription('AC presence on output (relay operation check) 0 - no AC on output socket 1 - AC is present on oputput')
npPwr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5800))
npPwrTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5800, 3), )
if mibBuilder.loadTexts: npPwrTable.setStatus('current')
if mibBuilder.loadTexts: npPwrTable.setDescription('Watchdog and outlet/relay control table')
npPwrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1), ).setIndexNames((0, "DKSF-54-1-X-X-1", "npPwrChannelN"))
if mibBuilder.loadTexts: npPwrEntry.setStatus('current')
if mibBuilder.loadTexts: npPwrEntry.setDescription('Watchdog control table row')
npPwrChannelN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrChannelN.setStatus('current')
if mibBuilder.loadTexts: npPwrChannelN.setDescription('The id of watchdog/power channel')
npPwrStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrStartReset.setStatus('obsolete')
if mibBuilder.loadTexts: npPwrStartReset.setDescription('Deprecated in current FW version: Write 1 to start forced reset. On read: 0 - normal operation 1 - reset is active 2 - reboot pause is active or watchdog is inactive')
npPwrResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrResetsCounter.setStatus('current')
if mibBuilder.loadTexts: npPwrResetsCounter.setDescription('Counter of watchdog resets Write 0 to clear.')
npPwrRepeatingResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrRepeatingResetsCounter.setStatus('current')
if mibBuilder.loadTexts: npPwrRepeatingResetsCounter.setDescription('Counter of continous failed watchdog resets')
npPwrMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrMemo.setStatus('current')
if mibBuilder.loadTexts: npPwrMemo.setDescription('Watchdog channel memo')
npThermo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800))
npThermoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8800, 1), )
if mibBuilder.loadTexts: npThermoTable.setStatus('current')
if mibBuilder.loadTexts: npThermoTable.setDescription('Thermo Sensors Table')
npThermoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1), ).setIndexNames((0, "DKSF-54-1-X-X-1", "npThermoSensorN"))
if mibBuilder.loadTexts: npThermoEntry.setStatus('current')
if mibBuilder.loadTexts: npThermoEntry.setDescription('Thermo Sensors Table Row')
npThermoSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoSensorN.setStatus('current')
if mibBuilder.loadTexts: npThermoSensorN.setDescription('The id of temperature sensor, 1 to 8')
npThermoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValue.setStatus('current')
if mibBuilder.loadTexts: npThermoValue.setDescription('Temperature, deg.C')
npThermoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoStatus.setStatus('current')
if mibBuilder.loadTexts: npThermoStatus.setDescription('Temperature status (0=fault, 1=underheat, 2=normal, 3=overheat)')
npThermoLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoLow.setStatus('current')
if mibBuilder.loadTexts: npThermoLow.setDescription('Bottom margin of normal temperature range, deg.C')
npThermoHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoHigh.setStatus('current')
if mibBuilder.loadTexts: npThermoHigh.setDescription('Top margin of normal temperature range, deg.C')
npThermoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoMemo.setStatus('current')
if mibBuilder.loadTexts: npThermoMemo.setDescription('T channel memo')
npThermoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2))
npThermoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0))
npThermoTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapSensorN.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapSensorN.setDescription('The id of temperature sensor, 1 to 8')
npThermoTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapValue.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapValue.setDescription('Temperature, deg.C')
npThermoTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapStatus.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapStatus.setDescription('Temperature status (0=fault, 1=underheat, 2=normal, 3=overheat)')
npThermoTrapLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapLow.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapLow.setDescription('Bottom margin of normal temperature range, deg.C')
npThermoTrapHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapHigh.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapHigh.setDescription('Top margin of normal temperature range, deg.C')
npThermoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapMemo.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapMemo.setDescription('T channel memo')
npThermoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)).setObjects(("DKSF-54-1-X-X-1", "npThermoTrapSensorN"), ("DKSF-54-1-X-X-1", "npThermoTrapValue"), ("DKSF-54-1-X-X-1", "npThermoTrapStatus"), ("DKSF-54-1-X-X-1", "npThermoTrapLow"), ("DKSF-54-1-X-X-1", "npThermoTrapHigh"), ("DKSF-54-1-X-X-1", "npThermoTrapMemo"))
if mibBuilder.loadTexts: npThermoTrap.setStatus('current')
if mibBuilder.loadTexts: npThermoTrap.setDescription('Status of Thermo sensor is changed (crossing of normal temp. range)')
npRelHumidity = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400))
npRelHumSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 2))
npRelHumSensorStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("error", 0), ("ok", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatus.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorStatus.setDescription("Status of the Rel.Humidity Sensor One 1=Normal, 0=Error or Sensor isn't connected")
npRelHumSensorValueH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueH.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueH.setDescription('Relative humidity value, %')
npRelHumSensorValueT = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueT.setDescription('Sensor temperature, deg.C')
npRelHumSensorStatusH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatusH.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorStatusH.setDescription('Status of Relative Humiduty')
npRelHumSafeRangeHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setStatus('current')
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setDescription('Relative Humidity safe range, top margin, %RH')
npRelHumSafeRangeLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setStatus('current')
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setDescription('Relative Humidity safe range, bottom margin, %RH')
npRelHumSensorValueT100 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT100.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueT100.setDescription('Sensor temperature, deg.C * 100 (fixed point two decimal places) Used to get access to the fractional part of T value')
npRelHumTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9))
npRelHumTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0))
npRelHumTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0, 1)).setObjects(("DKSF-54-1-X-X-1", "npRelHumSensorStatusH"), ("DKSF-54-1-X-X-1", "npRelHumSensorValueH"), ("DKSF-54-1-X-X-1", "npRelHumSafeRangeHigh"), ("DKSF-54-1-X-X-1", "npRelHumSafeRangeLow"))
if mibBuilder.loadTexts: npRelHumTrap.setStatus('current')
if mibBuilder.loadTexts: npRelHumTrap.setDescription('Status of Relative Humidity RH sensor has changed!')
npGsm = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800))
npGsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 1))
npGsmFailed = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ok", 0), ("failed", 1), ("fatalError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmFailed.setStatus('current')
if mibBuilder.loadTexts: npGsmFailed.setDescription("Firmware's GSM module status")
npGsmRegistration = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))).clone(namedValues=NamedValues(("impossible", 0), ("homeNetwork", 1), ("searching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5), ("infoUpdate", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmRegistration.setStatus('current')
if mibBuilder.loadTexts: npGsmRegistration.setDescription('Status of modem registration in GSM network (AT+CREG? result)')
npGsmStrength = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmStrength.setStatus('current')
if mibBuilder.loadTexts: npGsmStrength.setDescription('GSM signal strength. 0..31 = 0..100%, 99 = unknown or n/a, 255 = updating info')
npGsmSendSms = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npGsmSendSms.setStatus('current')
if mibBuilder.loadTexts: npGsmSendSms.setDescription('Send arbitrary SMS. Format: [phone_number,phone_number,...] Message One to four destination phone numbers If [] and numbers omitted, mesagge will be sent to preset numbers from SMS setup Only Latin characters allowed in message body')
npGsmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2))
npGsmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0))
npGsmTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)).setObjects(("DKSF-54-1-X-X-1", "npGsmFailed"), ("DKSF-54-1-X-X-1", "npGsmRegistration"), ("DKSF-54-1-X-X-1", "npGsmStrength"))
if mibBuilder.loadTexts: npGsmTrap.setStatus('current')
if mibBuilder.loadTexts: npGsmTrap.setDescription('GSM modem or SMS firmware problems')
npBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3900))
npBatteryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3900, 1))
npBatteryPok = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3900, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("batteryPower", 0), ("externalPower", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npBatteryPok.setStatus('current')
if mibBuilder.loadTexts: npBatteryPok.setDescription('Power source')
npBatteryLevel = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3900, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npBatteryLevel.setStatus('current')
if mibBuilder.loadTexts: npBatteryLevel.setDescription('Battery charge, approximate value, in percent. Valid only if npBatteryPok = 0')
npBatteryChg = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3900, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("batteryChargingSuspended", 0), ("batteryFastCharging", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npBatteryChg.setStatus('current')
if mibBuilder.loadTexts: npBatteryChg.setDescription('Battery chargeing status. 0 if charging suspended or battery is full, 1 while LiPo fast charging.')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
if mibBuilder.loadTexts: npSoftReboot.setDescription('Write 1 to reboot device after current operations completition')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
if mibBuilder.loadTexts: npResetStack.setDescription('Write 1 to re-initialize network stack')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
if mibBuilder.loadTexts: npForcedReboot.setDescription('Write 1 to immediate forced reboot')
mibBuilder.exportSymbols("DKSF-54-1-X-X-1", npThermoSensorN=npThermoSensorN, npBatteryLevel=npBatteryLevel, npPwrTable=npPwrTable, npThermoTrapPrefix=npThermoTrapPrefix, netPing4Pwr=netPing4Pwr, npThermo=npThermo, npThermoTrapSensorN=npThermoTrapSensorN, npPwrRepeatingResetsCounter=npPwrRepeatingResetsCounter, npRelHumidity=npRelHumidity, npBattery=npBattery, npSoftReboot=npSoftReboot, npGsmSendSms=npGsmSendSms, npRelayTable=npRelayTable, PYSNMP_MODULE_ID=netPing4Pwr, npRelayStartReset=npRelayStartReset, npResetStack=npResetStack, npThermoTrap=npThermoTrap, npGsmStrength=npGsmStrength, npThermoTraps=npThermoTraps, npThermoStatus=npThermoStatus, npThermoTrapHigh=npThermoTrapHigh, npPwrResetsCounter=npPwrResetsCounter, npThermoTrapLow=npThermoTrapLow, npRelHumSensorValueT100=npRelHumSensorValueT100, npForcedReboot=npForcedReboot, npRelHumTraps=npRelHumTraps, npPwr=npPwr, npRelHumSafeRangeLow=npRelHumSafeRangeLow, npThermoLow=npThermoLow, npThermoTrapStatus=npThermoTrapStatus, npPwrChannelN=npPwrChannelN, npRelayMode=npRelayMode, npThermoHigh=npThermoHigh, npGsm=npGsm, npReboot=npReboot, npBatteryPok=npBatteryPok, lightcom=lightcom, npGsmTraps=npGsmTraps, npThermoMemo=npThermoMemo, npBatteryChg=npBatteryChg, npRelayState=npRelayState, npRelHumTrap=npRelHumTrap, npThermoTrapMemo=npThermoTrapMemo, npBatteryInfo=npBatteryInfo, npGsmRegistration=npGsmRegistration, npGsmInfo=npGsmInfo, npRelHumSensorStatusH=npRelHumSensorStatusH, npThermoTable=npThermoTable, npRelayFlip=npRelayFlip, npRelay=npRelay, npRelHumSensorValueT=npRelHumSensorValueT, npRelHumSensorValueH=npRelHumSensorValueH, npRelHumSafeRangeHigh=npRelHumSafeRangeHigh, npRelayPowered=npRelayPowered, npPwrStartReset=npPwrStartReset, npPwrMemo=npPwrMemo, npRelHumSensor=npRelHumSensor, npThermoEntry=npThermoEntry, npRelayEntry=npRelayEntry, npRelHumSensorStatus=npRelHumSensorStatus, npThermoTrapValue=npThermoTrapValue, npGsmFailed=npGsmFailed, npGsmTrapPrefix=npGsmTrapPrefix, npRelayN=npRelayN, npGsmTrap=npGsmTrap, npPwrEntry=npPwrEntry, npRelayMemo=npRelayMemo, npThermoValue=npThermoValue, npRelHumTrapPrefix=npRelHumTrapPrefix)
