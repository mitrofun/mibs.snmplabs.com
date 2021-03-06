#
# PySNMP MIB module ZXR10-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-POE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, MibIdentifier, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Gauge32, ModuleIdentity, iso, NotificationType, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibIdentifier", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Gauge32", "ModuleIdentity", "iso", "NotificationType", "Integer32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10POE = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 319))
class DisplayString(OctetString):
    pass

pseTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1), )
if mibBuilder.loadTexts: pseTable.setStatus('current')
if mibBuilder.loadTexts: pseTable.setDescription('A table of objects that display and control attributes of the main power source in a PSE device. Ethernet switches are one example of boxes that would support these objects. Values of all read-write objects in this table are persistent at restart/reboot.')
pseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1), ).setIndexNames((0, "ZXR10-POE-MIB", "pseGroupIndex"))
if mibBuilder.loadTexts: pseEntry.setStatus('current')
if mibBuilder.loadTexts: pseEntry.setDescription('A set of objects that display and control the Main power of a PSE.')
pseGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pseGroupIndex.setStatus('current')
if mibBuilder.loadTexts: pseGroupIndex.setDescription('This variable uniquely identifies the group containing the port to which a power Ethernet PSE is connected. Group means box in the stack, module in a rack and the value 1 MUST be used for non-modular devices. Furthermore, the same value MUST be used in this variable, pethMainPseGroupIndex, and pethNotificationControlGroupIndex to refer to a given box in a stack or module in the rack.')
overTemperatureAutoRecovery = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: overTemperatureAutoRecovery.setStatus('current')
if mibBuilder.loadTexts: overTemperatureAutoRecovery.setDescription('disable (0) An group which can not provide the overtemperature auto-recovery functions. enable(1) An group which can provide the overtemperature auto-recovery functions.')
psePeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 3), DisplayString()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: psePeakPower.setStatus('current')
if mibBuilder.loadTexts: psePeakPower.setDescription('Poe peak-power.')
psePeakPowerTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psePeakPowerTime.setStatus('current')
if mibBuilder.loadTexts: psePeakPowerTime.setDescription('peak-power time.')
pseCurrentTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pseCurrentTemperature.setStatus('current')
if mibBuilder.loadTexts: pseCurrentTemperature.setDescription('Poe current temperature.')
pseFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pseFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: pseFirmwareVersion.setDescription('Poe firmware version.')
pseCriticalPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 7), DisplayString()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pseCriticalPower.setStatus('current')
if mibBuilder.loadTexts: pseCriticalPower.setDescription('Poe critical-power.')
portTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2), )
if mibBuilder.loadTexts: portTable.setStatus('current')
if mibBuilder.loadTexts: portTable.setDescription('A table of objects that display and control the power characteristics of power Ethernet ports on a Power Source Entity (PSE) device. This group will be implemented in managed power Ethernet switches and mid-span devices. Values of all read-write objects in this table are persistent at restart/reboot.')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1), ).setIndexNames((0, "ZXR10-POE-MIB", "portEntryGroupIndex"), (0, "ZXR10-POE-MIB", "portEntryPortIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('current')
if mibBuilder.loadTexts: portEntry.setDescription('A set of objects that display and control the power characteristics of a power Ethernet PSE port. ')
portEntryGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: portEntryGroupIndex.setStatus('current')
if mibBuilder.loadTexts: portEntryGroupIndex.setDescription('This variable uniquely identifies the group to which power Ethernet PSE is connected. Group means (box in the stack, module in a rack) and the value 1 MUST be used for non-modular devices. Furthermore, the same value MUST be used in this variable, pethPsePortGroupIndex, and pethNotificationControlGroupIndex to refer to a given box in a stack or module in a rack.')
portEntryPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: portEntryPortIndex.setStatus('current')
if mibBuilder.loadTexts: portEntryPortIndex.setDescription('This variable uniquely identifies the power Ethernet PSE port within group pethPsePortGroupIndex to which the power Ethernet PSE entry is connected.')
interfaceCurrentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 3), DisplayString()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceCurrentPower.setStatus('current')
if mibBuilder.loadTexts: interfaceCurrentPower.setDescription('The current power of the PSE port expressed in Watts.')
interfaceAvgPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 4), DisplayString()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceAvgPower.setStatus('current')
if mibBuilder.loadTexts: interfaceAvgPower.setDescription('The average power of the PSE port expressed in Watts.')
interfacePeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 5), DisplayString()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: interfacePeakPower.setStatus('current')
if mibBuilder.loadTexts: interfacePeakPower.setDescription('The peak power of the PSE port expressed in Watts.')
interfacepeakPowerTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfacepeakPowerTime.setStatus('current')
if mibBuilder.loadTexts: interfacepeakPowerTime.setDescription('The interface peak Power Time.')
enhancedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enhancedMode.setStatus('current')
if mibBuilder.loadTexts: enhancedMode.setDescription('enable (0) An interface which can provide the enhanced mode. disable(1) An interface which can not provide the enhanced mode.')
pdMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fifteen-point-four", 0), ("four", 1), ("seven", 2), ("eighteen", 3), ("twenty-seven", 4), ("thirty", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdMaxPower.setStatus('current')
if mibBuilder.loadTexts: pdMaxPower.setDescription('The max poe pd power: 15.4(0) 15.4W 4.0(1), 4.0W 7.0(2), 7.0W ext.18(3), 18W ext.27(4), 27W ext.30(5) 30W ')
mibBuilder.exportSymbols("ZXR10-POE-MIB", psePeakPower=psePeakPower, enhancedMode=enhancedMode, pseFirmwareVersion=pseFirmwareVersion, pseCurrentTemperature=pseCurrentTemperature, interfacepeakPowerTime=interfacepeakPowerTime, interfaceCurrentPower=interfaceCurrentPower, pseGroupIndex=pseGroupIndex, psePeakPowerTime=psePeakPowerTime, interfaceAvgPower=interfaceAvgPower, portEntryGroupIndex=portEntryGroupIndex, pseCriticalPower=pseCriticalPower, pseEntry=pseEntry, portEntry=portEntry, pdMaxPower=pdMaxPower, zxr10=zxr10, zxr10POE=zxr10POE, interfacePeakPower=interfacePeakPower, portEntryPortIndex=portEntryPortIndex, pseTable=pseTable, zte=zte, overTemperatureAutoRecovery=overTemperatureAutoRecovery, portTable=portTable, DisplayString=DisplayString)
