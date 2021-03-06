#
# PySNMP MIB module MRV-IR-HDAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MRV-IR-HDAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:15:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
TrapSeverity, = mibBuilder.importSymbols("MRV-IR-SYSTEM-MIB", "TrapSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Integer32, Counter32, NotificationType, ObjectIdentity, TimeTicks, iso, Bits, enterprises, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Integer32", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "iso", "Bits", "enterprises", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mrvBpd = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
mrvLx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 100))
irHdamMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 33, 100, 4))
if mibBuilder.loadTexts: irHdamMib.setLastUpdated('200703220000Z')
if mibBuilder.loadTexts: irHdamMib.setOrganization('MRV Communications - BPD Division')
if mibBuilder.loadTexts: irHdamMib.setContactInfo('Postal: MRV Communications, Inc. 295 Foster Street Littleton, MA 01460 E-mail: support@mrv.com')
if mibBuilder.loadTexts: irHdamMib.setDescription('This is the MRV LX HDAM Alarm MIB module.')
irHdam = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 100, 4, 1))
irHdamAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 100, 4, 2))
irHdamControl = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 100, 4, 3))
irHdamAnalog = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 100, 4, 4))
class IrHdamModuleType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("empty", 1), ("alarmModule", 2), ("controlModule", 3), ("analoglModule", 4))

class IrContactState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("closed", 2))

class IrAnalogStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

irHdamUnitTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1), )
if mibBuilder.loadTexts: irHdamUnitTable.setStatus('current')
if mibBuilder.loadTexts: irHdamUnitTable.setDescription('A list of hdam unit entries.')
irHdamUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irHdamUnitPortIndex"))
if mibBuilder.loadTexts: irHdamUnitEntry.setStatus('current')
if mibBuilder.loadTexts: irHdamUnitEntry.setDescription('An hdam unit entry.')
irHdamUnitPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamUnitPortIndex.setStatus('current')
if mibBuilder.loadTexts: irHdamUnitPortIndex.setDescription('The port index to which this hdam unit is connected.')
irHdamFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamFwVersion.setStatus('current')
if mibBuilder.loadTexts: irHdamFwVersion.setDescription('The HDAM unit firmware version string.')
irHdamConnectStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamConnectStatus.setStatus('current')
if mibBuilder.loadTexts: irHdamConnectStatus.setDescription('The HDAM unit connection status.')
irHdamPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerAC", 1), ("powerDC", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerType.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerType.setDescription('The type of power used by the hdam device.')
irHdamAction = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irHdamAction.setStatus('current')
if mibBuilder.loadTexts: irHdamAction.setDescription('This object is used to perform an action on the HDAM unit. A read of this object always returns the value other(1). Setting this object to reset(2) causes the unit to be reset.')
irHdamModuleTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2), )
if mibBuilder.loadTexts: irHdamModuleTable.setStatus('current')
if mibBuilder.loadTexts: irHdamModuleTable.setDescription('A list of hdam module entries.')
irHdamModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irHdamPortIndex"), (0, "MRV-IR-HDAM-MIB", "irHdamSlotIndex"))
if mibBuilder.loadTexts: irHdamModuleEntry.setStatus('current')
if mibBuilder.loadTexts: irHdamModuleEntry.setDescription('An hdam module entry.')
irHdamPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPortIndex.setStatus('current')
if mibBuilder.loadTexts: irHdamPortIndex.setDescription('The port index to which this hdam unit is connected.')
irHdamSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamSlotIndex.setStatus('current')
if mibBuilder.loadTexts: irHdamSlotIndex.setDescription('The slot index for this module entry.')
irHdamModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 3), IrHdamModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamModuleType.setStatus('current')
if mibBuilder.loadTexts: irHdamModuleType.setDescription('The type of module in the slot.')
irHdamPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3), )
if mibBuilder.loadTexts: irHdamPowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerSupplyTable.setDescription('A list of hdam power supply entries.')
irHdamPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irHdamPortIndex"), (0, "MRV-IR-HDAM-MIB", "irHdamPowerIndex"))
if mibBuilder.loadTexts: irHdamPowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerSupplyEntry.setDescription('An hdam power supply entry.')
irHdamPowerPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerPortIndex.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerPortIndex.setDescription('The index of the port to which the hdam unit is attached.')
irHdamPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerIndex.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerIndex.setDescription('The index of the hdam power unit.')
irHdamPowerUnitPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerUnitPresent.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerUnitPresent.setDescription('This indicates if the power unit is present or not.')
irHdamPowerInputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerInputStatus.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerInputStatus.setDescription('This indicates if the power unit is plugged into a power source.')
irHdamPowerOutputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerOutputStatus.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerOutputStatus.setDescription('This indicates the status of the internal power feed to the device components.')
irHdamPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irHdamPowerStatus.setStatus('current')
if mibBuilder.loadTexts: irHdamPowerStatus.setDescription('The overall status of the power unit.')
irAlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1), )
if mibBuilder.loadTexts: irAlarmConfigTable.setStatus('current')
if mibBuilder.loadTexts: irAlarmConfigTable.setDescription('A list of alarm config entries.')
irAlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irAlarmPortIndex"), (0, "MRV-IR-HDAM-MIB", "irAlarmSlotIndex"), (0, "MRV-IR-HDAM-MIB", "irAlarmPointIndex"))
if mibBuilder.loadTexts: irAlarmConfigEntry.setStatus('current')
if mibBuilder.loadTexts: irAlarmConfigEntry.setDescription('An hdam alarm config entry.')
irAlarmPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmPortIndex.setStatus('current')
if mibBuilder.loadTexts: irAlarmPortIndex.setDescription('The port index on which the alarm unit is attached.')
irAlarmSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmSlotIndex.setStatus('current')
if mibBuilder.loadTexts: irAlarmSlotIndex.setDescription('The slot in the alarm unit which identifies this module.')
irAlarmPointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmPointIndex.setStatus('current')
if mibBuilder.loadTexts: irAlarmPointIndex.setDescription('An integer which uniquely identifies an alarm on this module.')
irAlarmName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmName.setStatus('current')
if mibBuilder.loadTexts: irAlarmName.setDescription('The name assigned to the alarm.')
irAlarmContactState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 5), IrContactState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmContactState.setStatus('current')
if mibBuilder.loadTexts: irAlarmContactState.setDescription('The current state of the alarm contacts.')
irAlarmContactFaultState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 6), IrContactState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmContactFaultState.setStatus('current')
if mibBuilder.loadTexts: irAlarmContactFaultState.setDescription('The contact state (open or closed) which indicates the fault condition. If the value of this object and irAlarmContactState is the same, then the alarm has been triggered.')
irAlarmDebounceInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmDebounceInterval.setStatus('current')
if mibBuilder.loadTexts: irAlarmDebounceInterval.setDescription('The number of seconds the alarm must be in the fault state before it is considered valid.')
irAlarmAudibleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmAudibleStatus.setStatus('current')
if mibBuilder.loadTexts: irAlarmAudibleStatus.setDescription('This indicates whether the audible alarm on the unit will sound when this alarm is generated.')
irAlarmTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmTrapStatus.setStatus('current')
if mibBuilder.loadTexts: irAlarmTrapStatus.setDescription('This indicates whether an snmp trap will be generated when this alarm is generated.')
irAlarmTrapSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 10), TrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmTrapSeverity.setStatus('current')
if mibBuilder.loadTexts: irAlarmTrapSeverity.setDescription('The trap severity assigned to this alarm. This value will be sent when an alarm fires and an snmp trap is generated.')
irAlarmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmCount.setStatus('current')
if mibBuilder.loadTexts: irAlarmCount.setDescription('The number of times the alarm has been generated since the unit was started.')
irAlarmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAlarmTimestamp.setStatus('current')
if mibBuilder.loadTexts: irAlarmTimestamp.setDescription('A timestamp string indicating the time the last alarm was generated. A null string indicates that the alarm has not been generated.')
irAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAlarmDescription.setStatus('current')
if mibBuilder.loadTexts: irAlarmDescription.setDescription('A user configurable alarm description string.')
irControlConfigTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1), )
if mibBuilder.loadTexts: irControlConfigTable.setStatus('current')
if mibBuilder.loadTexts: irControlConfigTable.setDescription('A list of control config entries.')
irControlConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irControlPortIndex"), (0, "MRV-IR-HDAM-MIB", "irControlSlotIndex"), (0, "MRV-IR-HDAM-MIB", "irControlPointIndex"))
if mibBuilder.loadTexts: irControlConfigEntry.setStatus('current')
if mibBuilder.loadTexts: irControlConfigEntry.setDescription('A control config entry.')
irControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irControlPortIndex.setStatus('current')
if mibBuilder.loadTexts: irControlPortIndex.setDescription('The port index on which the control unit is attached.')
irControlSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irControlSlotIndex.setStatus('current')
if mibBuilder.loadTexts: irControlSlotIndex.setDescription('The slot in the control unit which identifies this module.')
irControlPointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irControlPointIndex.setStatus('current')
if mibBuilder.loadTexts: irControlPointIndex.setDescription('An integer which uniquely identifies a control on this module.')
irControlName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irControlName.setStatus('current')
if mibBuilder.loadTexts: irControlName.setDescription('The name assigned to the control.')
irControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 5), IrContactState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irControlState.setStatus('current')
if mibBuilder.loadTexts: irControlState.setDescription('The current value of the control state.')
irControlActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 6), IrContactState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irControlActiveState.setStatus('current')
if mibBuilder.loadTexts: irControlActiveState.setDescription('The value of the control state that activates the attached device.')
irControlDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irControlDescription.setStatus('current')
if mibBuilder.loadTexts: irControlDescription.setDescription('A user configurable control description string.')
irAnalogConfigTable = MibTable((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1), )
if mibBuilder.loadTexts: irAnalogConfigTable.setStatus('current')
if mibBuilder.loadTexts: irAnalogConfigTable.setDescription('A list of analog loop config entries.')
irAnalogConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1), ).setIndexNames((0, "MRV-IR-HDAM-MIB", "irAnalogPortIndex"), (0, "MRV-IR-HDAM-MIB", "irAnalogSlotIndex"), (0, "MRV-IR-HDAM-MIB", "irAnalogPointIndex"))
if mibBuilder.loadTexts: irAnalogConfigEntry.setStatus('current')
if mibBuilder.loadTexts: irAnalogConfigEntry.setDescription('An analog loop config entry.')
irAnalogPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogPortIndex.setStatus('current')
if mibBuilder.loadTexts: irAnalogPortIndex.setDescription('The port index on which the analog unit is attached.')
irAnalogSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogSlotIndex.setStatus('current')
if mibBuilder.loadTexts: irAnalogSlotIndex.setDescription('The slot in the analog unit which identifies this module.')
irAnalogPointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogPointIndex.setStatus('current')
if mibBuilder.loadTexts: irAnalogPointIndex.setDescription('An integer which uniquely identifies an analog point on this module.')
irAnalogName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogName.setStatus('current')
if mibBuilder.loadTexts: irAnalogName.setDescription('The name assigned to the analog.')
irAnalogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogDescription.setStatus('current')
if mibBuilder.loadTexts: irAnalogDescription.setDescription('A user configurable analog description string.')
irAnalogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 6), IrAnalogStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogStatus.setStatus('current')
if mibBuilder.loadTexts: irAnalogStatus.setDescription('The status of the analog point.')
irAnalogValue = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogValue.setStatus('current')
if mibBuilder.loadTexts: irAnalogValue.setDescription('The current analog sensor reading in milliAmps.')
irAnalogCalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogCalValue.setStatus('current')
if mibBuilder.loadTexts: irAnalogCalValue.setDescription('The current analog sensor calibrated value.')
irAnalogCalMinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogCalMinValue.setStatus('current')
if mibBuilder.loadTexts: irAnalogCalMinValue.setDescription('The calibration value assigned to the minimum sensor reading.')
irAnalogCalMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogCalMaxValue.setStatus('current')
if mibBuilder.loadTexts: irAnalogCalMaxValue.setDescription('The calibration value assigned to the maximum analog sensor reading.')
irAnalogCalMargin = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogCalMargin.setStatus('current')
if mibBuilder.loadTexts: irAnalogCalMargin.setDescription('The calibration margin value. This will be added to the calibrated analog sensor value.')
irAnalogCalUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogCalUnits.setStatus('current')
if mibBuilder.loadTexts: irAnalogCalUnits.setDescription('A user defined string describing the calibrated units for the analog sensor.')
irAnalogThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogThresholdHigh.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdHigh.setDescription('The analog sensor high threshold value. A value of -0 indicates threshold is not configured.')
irAnalogThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogThresholdLow.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdLow.setDescription('The analog sensor low threshold value. A value of -0 indicates threshold is not configured.')
irAnalogThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 15), TrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogThresholdSeverity.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdSeverity.setDescription('The severity value of the analog sensor assigned to the low threshold. This value will be sent in the threshold trap.')
irAnalogThresholdHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irAnalogThresholdHysteresis.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdHysteresis.setDescription('After crossing a threshold, the delta by which the caliberated value must drop within the normal range before the alarm condition is cleared (i.e. a cleared alarm is generated).')
irAnalogThresholdHighAlarmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogThresholdHighAlarmCount.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdHighAlarmCount.setDescription('The number of times the analog sensor high threshold has been crossed since the unit was started.')
irAnalogThresholdLowAlarmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogThresholdLowAlarmCount.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdLowAlarmCount.setDescription('The number of times the analog sensor low threshold has been crossed since the unit was started.')
irAnalogThresholdHighTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogThresholdHighTimestamp.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdHighTimestamp.setDescription('A timestamp string indicating the time the analog sensor last crossed the high threshold. A null string indicates that the alarm has not been crossed.')
irAnalogThresholdLowTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irAnalogThresholdLowTimestamp.setStatus('current')
if mibBuilder.loadTexts: irAnalogThresholdLowTimestamp.setDescription('A timestamp string indicating the time the analog sensor last crossed the low threshold. A null string indicates that the alarm has not been crossed.')
mibBuilder.exportSymbols("MRV-IR-HDAM-MIB", irAlarmPointIndex=irAlarmPointIndex, irAnalogDescription=irAnalogDescription, irHdamPowerType=irHdamPowerType, mrvBpd=mrvBpd, irAnalogPointIndex=irAnalogPointIndex, IrAnalogStatus=IrAnalogStatus, irHdamPowerInputStatus=irHdamPowerInputStatus, irAlarmConfigEntry=irAlarmConfigEntry, irAnalogThresholdHighTimestamp=irAnalogThresholdHighTimestamp, irHdamPowerStatus=irHdamPowerStatus, irAnalogThresholdHigh=irAnalogThresholdHigh, irHdamUnitPortIndex=irHdamUnitPortIndex, irAnalogThresholdLow=irAnalogThresholdLow, irAnalogCalMaxValue=irAnalogCalMaxValue, irHdam=irHdam, irHdamModuleEntry=irHdamModuleEntry, irAnalogName=irAnalogName, irAlarmContactFaultState=irAlarmContactFaultState, irControlConfigEntry=irControlConfigEntry, irControlName=irControlName, irControlDescription=irControlDescription, irHdamAction=irHdamAction, IrContactState=IrContactState, irAlarmCount=irAlarmCount, irAnalogThresholdHighAlarmCount=irAnalogThresholdHighAlarmCount, irHdamFwVersion=irHdamFwVersion, irAlarmConfigTable=irAlarmConfigTable, irHdamPortIndex=irHdamPortIndex, irAnalogConfigEntry=irAnalogConfigEntry, irAlarmPortIndex=irAlarmPortIndex, irAlarmDebounceInterval=irAlarmDebounceInterval, irAlarmContactState=irAlarmContactState, irAlarmSlotIndex=irAlarmSlotIndex, irHdamPowerSupplyTable=irHdamPowerSupplyTable, irControlPointIndex=irControlPointIndex, irControlSlotIndex=irControlSlotIndex, irHdamAnalog=irHdamAnalog, mrvLx=mrvLx, irHdamPowerIndex=irHdamPowerIndex, irAlarmTrapSeverity=irAlarmTrapSeverity, irControlPortIndex=irControlPortIndex, irControlConfigTable=irControlConfigTable, irAnalogThresholdLowAlarmCount=irAnalogThresholdLowAlarmCount, irAnalogThresholdHysteresis=irAnalogThresholdHysteresis, IrHdamModuleType=IrHdamModuleType, irHdamMib=irHdamMib, irAnalogThresholdLowTimestamp=irAnalogThresholdLowTimestamp, irHdamPowerPortIndex=irHdamPowerPortIndex, irControlState=irControlState, irAnalogSlotIndex=irAnalogSlotIndex, PYSNMP_MODULE_ID=irHdamMib, irHdamSlotIndex=irHdamSlotIndex, irAnalogCalValue=irAnalogCalValue, irControlActiveState=irControlActiveState, irAlarmTrapStatus=irAlarmTrapStatus, irAnalogConfigTable=irAnalogConfigTable, irAnalogCalMargin=irAnalogCalMargin, irAnalogCalUnits=irAnalogCalUnits, irAnalogValue=irAnalogValue, irHdamConnectStatus=irHdamConnectStatus, irAlarmDescription=irAlarmDescription, irHdamPowerUnitPresent=irHdamPowerUnitPresent, irAlarmAudibleStatus=irAlarmAudibleStatus, irHdamUnitTable=irHdamUnitTable, irHdamPowerSupplyEntry=irHdamPowerSupplyEntry, irAnalogStatus=irAnalogStatus, irHdamPowerOutputStatus=irHdamPowerOutputStatus, irHdamUnitEntry=irHdamUnitEntry, irAnalogCalMinValue=irAnalogCalMinValue, irHdamAlarm=irHdamAlarm, irAlarmTimestamp=irAlarmTimestamp, irAnalogPortIndex=irAnalogPortIndex, irHdamModuleType=irHdamModuleType, irHdamModuleTable=irHdamModuleTable, irHdamControl=irHdamControl, irAnalogThresholdSeverity=irAnalogThresholdSeverity, irAlarmName=irAlarmName)
