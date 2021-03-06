#
# PySNMP MIB module V320-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/V320-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:33:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
mib_2, ModuleIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, ObjectIdentity, Integer32, Counter32, NotificationType, Counter64, MibIdentifier, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ModuleIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "enterprises", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sub10OID = ModuleIdentity((1, 3, 6, 1, 4, 1, 39003))
sub10OID.setRevisions(('2011-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sub10OID.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: sub10OID.setLastUpdated('201111290000Z')
if mibBuilder.loadTexts: sub10OID.setOrganization('Sub10 Systems Ltd')
if mibBuilder.loadTexts: sub10OID.setContactInfo('support@sub10systems.com')
if mibBuilder.loadTexts: sub10OID.setDescription('Sub10 MIB')
terminal2 = MibIdentifier((1, 3, 6, 1, 4, 1, 39003, 2))
terminalLinkQuality = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2), ("red", 3), ("unknown", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalLinkQuality.setStatus('current')
if mibBuilder.loadTexts: terminalLinkQuality.setDescription('A measure for quality of the microwave link. Green: good signal level to withstand heavy rain Yellow: sufficient signal level but no margin Red: insufficient signal level, link not available Unknown: no signal level data available')
terminalReceivePower = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalReceivePower.setStatus('current')
if mibBuilder.loadTexts: terminalReceivePower.setDescription('Receive signal level in dBm')
terminalTemperature = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalTemperature.setStatus('current')
if mibBuilder.loadTexts: terminalTemperature.setDescription('Temperature within the unit in degree Celsius')
terminalLockDetector = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalLockDetector.setStatus('current')
if mibBuilder.loadTexts: terminalLockDetector.setDescription('Lock detection signal level')
terminalLinkQualityImproved = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red2green", 1), ("red2yellow", 2), ("yellow2green", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalLinkQualityImproved.setStatus('current')
if mibBuilder.loadTexts: terminalLinkQualityImproved.setDescription('Indicates a positive change of the received microwave signal and the quality change from red to green or from red to yellow.')
terminalLinkQualityReduced = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("green2yellow", 1), ("green2red", 2), ("yellow2red", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalLinkQualityReduced.setStatus('current')
if mibBuilder.loadTexts: terminalLinkQualityReduced.setDescription('Indicates a negative change of the received microwave signal and the quality change from red to green or from red to yellow.')
terminalFirmwareversion = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalFirmwareversion.setStatus('current')
if mibBuilder.loadTexts: terminalFirmwareversion.setDescription('Installed Firmware Version.')
terminalAuxVoltage = MibScalar((1, 3, 6, 1, 4, 1, 39003, 2, 25), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terminalAuxVoltage.setStatus('current')
if mibBuilder.loadTexts: terminalAuxVoltage.setDescription('Actual Voltage at Auxilary Port')
terminalObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 39003, 2, 24)).setObjects(("V320-MIB", "terminalLinkQualityReduced"), ("V320-MIB", "terminalLinkQualityImproved"), ("V320-MIB", "terminalReceivePower"), ("V320-MIB", "terminalLinkQuality"), ("V320-MIB", "terminalTemperature"), ("V320-MIB", "terminalLockDetector"), ("V320-MIB", "terminalFirmwareversion"), ("V320-MIB", "terminalAuxVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    terminalObjectGroup = terminalObjectGroup.setStatus('current')
if mibBuilder.loadTexts: terminalObjectGroup.setDescription('Terminal object group')
terminalTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 39003, 2, 22))
terminalLinkQualityImprovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 39003, 2, 22, 1)).setObjects(("V320-MIB", "terminalLinkQualityImproved"))
if mibBuilder.loadTexts: terminalLinkQualityImprovedTrap.setStatus('current')
if mibBuilder.loadTexts: terminalLinkQualityImprovedTrap.setDescription('A trap indicating that the microwave signal quality did increase.')
terminalLinkQualityReducedTrap = NotificationType((1, 3, 6, 1, 4, 1, 39003, 2, 22, 2)).setObjects(("V320-MIB", "terminalLinkQualityReduced"))
if mibBuilder.loadTexts: terminalLinkQualityReducedTrap.setStatus('current')
if mibBuilder.loadTexts: terminalLinkQualityReducedTrap.setDescription('A trap indicating that the microwave signal quality did decrease.')
terminalTemperatureHighTrap = NotificationType((1, 3, 6, 1, 4, 1, 39003, 2, 22, 3)).setObjects(("V320-MIB", "terminalTemperature"))
if mibBuilder.loadTexts: terminalTemperatureHighTrap.setStatus('current')
if mibBuilder.loadTexts: terminalTemperatureHighTrap.setDescription('A trap indicating that the temperature within the unit is over or below 70 degree Celsius.')
terminalTemperatureLowTrap = NotificationType((1, 3, 6, 1, 4, 1, 39003, 2, 22, 4)).setObjects(("V320-MIB", "terminalTemperature"))
if mibBuilder.loadTexts: terminalTemperatureLowTrap.setStatus('current')
if mibBuilder.loadTexts: terminalTemperatureLowTrap.setDescription('A trap indicating that the temperature within the unit is over or below -40 degree Celsius.')
terminalNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 39003, 2, 23)).setObjects(("V320-MIB", "terminalLinkQualityImprovedTrap"), ("V320-MIB", "terminalLinkQualityReducedTrap"), ("V320-MIB", "terminalTemperatureHighTrap"), ("V320-MIB", "terminalTemperatureLowTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    terminalNotificationGroup = terminalNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: terminalNotificationGroup.setDescription('Terminal notification group')
mibBuilder.exportSymbols("V320-MIB", terminal2=terminal2, terminalFirmwareversion=terminalFirmwareversion, sub10OID=sub10OID, terminalTemperatureLowTrap=terminalTemperatureLowTrap, terminalLinkQualityReducedTrap=terminalLinkQualityReducedTrap, terminalLinkQualityReduced=terminalLinkQualityReduced, terminalReceivePower=terminalReceivePower, terminalNotificationGroup=terminalNotificationGroup, terminalTemperature=terminalTemperature, terminalLockDetector=terminalLockDetector, PYSNMP_MODULE_ID=sub10OID, terminalLinkQualityImproved=terminalLinkQualityImproved, terminalObjectGroup=terminalObjectGroup, terminalAuxVoltage=terminalAuxVoltage, terminalLinkQuality=terminalLinkQuality, terminalLinkQualityImprovedTrap=terminalLinkQualityImprovedTrap, terminalTemperatureHighTrap=terminalTemperatureHighTrap, terminalTraps=terminalTraps)
