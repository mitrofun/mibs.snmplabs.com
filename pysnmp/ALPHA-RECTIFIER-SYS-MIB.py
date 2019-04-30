#
# PySNMP MIB module ALPHA-RECTIFIER-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALPHA-RECTIFIER-SYS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ScaledNumber, simple = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "ScaledNumber", "simple")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Integer32, ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, IpAddress, Counter32, NotificationType, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rectifierSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1))
rectifierSystem.setRevisions(('2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))
if mibBuilder.loadTexts: rectifierSystem.setLastUpdated('201507280000Z')
if mibBuilder.loadTexts: rectifierSystem.setOrganization('Alpha Technologies Ltd.')
rectSysTotalOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 1), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysTotalOutputCurrent.setStatus('current')
rectSysTotalOutputPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 2), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysTotalOutputPower.setStatus('current')
rectSysTotalCapacityInstalledAmps = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 3), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysTotalCapacityInstalledAmps.setStatus('current')
rectSysTotalCapacityInstalledPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 4), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysTotalCapacityInstalledPower.setStatus('current')
rectSysAverageRectifierOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 5), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysAverageRectifierOutputVoltage.setStatus('current')
rectSysAverageRectifierACInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 6), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysAverageRectifierACInputVoltage.setStatus('current')
rectSysAveragePhase1Voltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 7), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysAveragePhase1Voltage.setStatus('current')
rectSysAveragePhase2Voltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 8), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysAveragePhase2Voltage.setStatus('current')
rectSysAveragePhase3Voltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 9), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysAveragePhase3Voltage.setStatus('current')
rectSysSystemVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 10), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysSystemVoltage.setStatus('current')
rectSysTotalLoadCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 11), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysTotalLoadCurrent.setStatus('current')
rectSysBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 12), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysBatteryVoltage.setStatus('current')
rectSysBatteryCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 13), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysBatteryCurrent.setStatus('current')
rectSysBatteryTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 14), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysBatteryTemperature.setStatus('current')
rectSysSystemNumber = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 15), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rectSysSystemNumber.setStatus('current')
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1))
compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1, 1)).setObjects(("ALPHA-RECTIFIER-SYS-MIB", "rectifierGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    compliance = compliance.setStatus('current')
rectifierGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2))
rectifierGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2, 1)).setObjects(("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputCurrent"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputPower"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledAmps"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledPower"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierOutputVoltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierACInputVoltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase1Voltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase2Voltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase3Voltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemVoltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalLoadCurrent"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryVoltage"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryCurrent"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryTemperature"), ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rectifierGroup = rectifierGroup.setStatus('current')
mibBuilder.exportSymbols("ALPHA-RECTIFIER-SYS-MIB", rectSysAveragePhase1Voltage=rectSysAveragePhase1Voltage, rectSysBatteryVoltage=rectSysBatteryVoltage, rectSysTotalLoadCurrent=rectSysTotalLoadCurrent, rectSysAverageRectifierOutputVoltage=rectSysAverageRectifierOutputVoltage, rectifierSystem=rectifierSystem, rectSysSystemVoltage=rectSysSystemVoltage, conformance=conformance, rectSysBatteryCurrent=rectSysBatteryCurrent, rectSysSystemNumber=rectSysSystemNumber, rectifierGroup=rectifierGroup, rectSysTotalCapacityInstalledPower=rectSysTotalCapacityInstalledPower, rectSysAveragePhase3Voltage=rectSysAveragePhase3Voltage, compliance=compliance, rectSysAverageRectifierACInputVoltage=rectSysAverageRectifierACInputVoltage, rectSysTotalOutputCurrent=rectSysTotalOutputCurrent, rectSysTotalCapacityInstalledAmps=rectSysTotalCapacityInstalledAmps, rectSysTotalOutputPower=rectSysTotalOutputPower, rectifierGroups=rectifierGroups, rectSysAveragePhase2Voltage=rectSysAveragePhase2Voltage, compliances=compliances, PYSNMP_MODULE_ID=rectifierSystem, rectSysBatteryTemperature=rectSysBatteryTemperature)