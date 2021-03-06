#
# PySNMP MIB module VIDEOFRAME-SIGMON-VM0001-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VIDEOFRAME-SIGMON-VM0001-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, TimeTicks, Integer32, Counter32, IpAddress, Unsigned32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "TimeTicks", "Integer32", "Counter32", "IpAddress", "Unsigned32", "Bits", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
vfBoxId, = mibBuilder.importSymbols("VIDEOFRAME-GENERIC-MIB", "vfBoxId")
vfMIBModules, = mibBuilder.importSymbols("VIDEOFRAME-REGISTRATIONS-MIB", "vfMIBModules")
vfSigmonFrameModuleTypes, vfFrameSlotNumber, vfProductsVF200Reg = mibBuilder.importSymbols("VIDEOFRAME-SIGMON-MIB", "vfSigmonFrameModuleTypes", "vfFrameSlotNumber", "vfProductsVF200Reg")
videoframeSigmonVm0001MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 1, 4))
videoframeSigmonVm0001MIB.setRevisions(('1901-08-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setRevisionsDescriptions(('First release.',))
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setLastUpdated('0108300000Z')
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setOrganization('Videoframe Systems')
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setContactInfo('Videoframe Systems P.O. Box 1991, Grass Valley, CA 95945, USA. +1 (530) 477-2000 http://www.videoframesystems.com')
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setDescription('This MIB describes the device specific objects of the VM0001 Analog Audio Monitoring module, and augments MIB-2, VF-GENERIC, and VF-SIGMON in the identification of this Videoframe Systems managed device. This module will be extended or modified as required. Videoframe Systems reserves the right to make changes in specification and other information contained in this document without prior notice. The reader should consult Videoframe Systems to determine whether any such changes have been made. In no event shall Videoframe Systems be liable for any incidental, indirect, special, or consequential damages whatsoever (including but not limited to lost profits) arising out of or related to this document or the information contained in it. Videoframe Systems grants vendors, end users, and other interested parties a non-exclusive license to use this specification in connection with the management of Videoframe Systems products. Copyright 2001 Videoframe, Inc.')
vfProductsVM0001Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 1))
if mibBuilder.loadTexts: vfProductsVM0001Reg.setStatus('current')
if mibBuilder.loadTexts: vfProductsVM0001Reg.setDescription('Videoframe VM0001 Analog Audio Monitoring Module.')
vm0001AnalogAudio = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1))
vm0001Table = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1), )
if mibBuilder.loadTexts: vm0001Table.setStatus('current')
if mibBuilder.loadTexts: vm0001Table.setDescription('Each row contains information about one VM0001 Analog Audio module in the managed VF200 frame.')
vm0001Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"))
if mibBuilder.loadTexts: vm0001Entry.setStatus('current')
if mibBuilder.loadTexts: vm0001Entry.setDescription('An Analog Audio module entry.')
vm0001SlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SlotNumber.setStatus('current')
if mibBuilder.loadTexts: vm0001SlotNumber.setDescription('The slot that this entry represents.')
vm0001Active = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001Active.setStatus('current')
if mibBuilder.loadTexts: vm0001Active.setDescription('Indicates whether this entry is active (this module is in this slot).')
vm0001FirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001FirmwareRev.setStatus('current')
if mibBuilder.loadTexts: vm0001FirmwareRev.setDescription('The revision level of the firmware on this module.')
vm0001Locate = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flash", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001Locate.setStatus('current')
if mibBuilder.loadTexts: vm0001Locate.setDescription('Controls the locate indicator on the module and indicates its current state. Set to flash (1) to cause the locate LED on the front of the module to begin flashing. Set to off to stop flashing.')
vm0001SignalTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2), )
if mibBuilder.loadTexts: vm0001SignalTable.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalTable.setDescription('Each row contains information about one channel of one VM0001 Analog Audio module in the managed VF200 frame.')
vm0001SignalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"), (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"))
if mibBuilder.loadTexts: vm0001SignalEntry.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalEntry.setDescription('An Analog Audio module channel entry.')
vm0001SignalSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SignalSlotNumber.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalSlotNumber.setDescription('The frame slot number that this entry represents.')
vm0001SignalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SignalNumber.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalNumber.setDescription('The channel within the module to which this signal is connected.')
vm0001SignalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001SignalName.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalName.setDescription('The name of the signal connected to this channel.')
vm0001SignalDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001SignalDescription.setStatus('current')
if mibBuilder.loadTexts: vm0001SignalDescription.setDescription('Descriptive identification of the signal connected to this channel.')
vm0001CurrentAplRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131071))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001CurrentAplRaw.setStatus('current')
if mibBuilder.loadTexts: vm0001CurrentAplRaw.setDescription('The current average amplitude value on this channel, in raw sample units.')
vm0001ZerodBCalibrationSet = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("go", 2), ("notReady", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001ZerodBCalibrationSet.setStatus('current')
if mibBuilder.loadTexts: vm0001ZerodBCalibrationSet.setDescription("Set to 'go' (2) to set the value of the 0 dB channel calibration to the current average amplitude value on this channel.")
vm0001ZerodBCalibrationValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131071))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001ZerodBCalibrationValue.setStatus('current')
if mibBuilder.loadTexts: vm0001ZerodBCalibrationValue.setDescription('The current raw sample amplitude value used as the 0 dB reference on this channel.')
vm0001AplHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighThreshold.setStatus('current')
if mibBuilder.loadTexts: vm0001AplHighThreshold.setDescription('The high APL alarm threshold for this channel, in dB.')
vm0001AplHighDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighDuration.setStatus('current')
if mibBuilder.loadTexts: vm0001AplHighDuration.setDescription('The high APL duration, in milliseconds, at which to alarm, for this channel.')
vm0001AplHighAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001AplHighAlarmState.setStatus('current')
if mibBuilder.loadTexts: vm0001AplHighAlarmState.setDescription('The current state of the high APL alarm for this channel.')
vm0001AplHighAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighAlarmAck.setStatus('current')
if mibBuilder.loadTexts: vm0001AplHighAlarmAck.setDescription('Set to acknowledge (3) to acknowledge a triggered high APL alarm for this channel.')
vm0001AplHighTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vm0001AplHighTrapEnable.setDescription('Set to enabled (1) to enable the high APL alarm trap for this channel.')
vm0001AplLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowThreshold.setStatus('current')
if mibBuilder.loadTexts: vm0001AplLowThreshold.setDescription('The low APL alarm threshold for this channel, in dB.')
vm0001AplLowDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowDuration.setStatus('current')
if mibBuilder.loadTexts: vm0001AplLowDuration.setDescription('The low APL duration, in milliseconds, at which to alarm, for this channel.')
vm0001AplLowAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001AplLowAlarmState.setStatus('current')
if mibBuilder.loadTexts: vm0001AplLowAlarmState.setDescription('The current state of the low APL alarm for this channel.')
vm0001AplLowAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowAlarmAck.setStatus('current')
if mibBuilder.loadTexts: vm0001AplLowAlarmAck.setDescription('Set to acknowledge (3) to acknowledge a triggered low APL alarm for this channel.')
vm0001AplLowTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vm0001AplLowTrapEnable.setDescription('Set to enabled (1) to enable the low APL alarm trap for this channel.')
vm0001PeakThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakThreshold.setStatus('current')
if mibBuilder.loadTexts: vm0001PeakThreshold.setDescription('The peak level above which to alarm.')
vm0001PeakPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakPeriod.setStatus('current')
if mibBuilder.loadTexts: vm0001PeakPeriod.setDescription('The period, in milliseconds, over which the peak value is accumulated for this channel.')
vm0001PeakAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001PeakAlarmState.setStatus('current')
if mibBuilder.loadTexts: vm0001PeakAlarmState.setDescription('The current state of the peak-threshold-exceeded alarm for this channel.')
vm0001PeakAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakAlarmAck.setStatus('current')
if mibBuilder.loadTexts: vm0001PeakAlarmAck.setDescription('Set to acknowledge (3) to acknowledge a triggered peak alarm for this channel.')
vm0001PeakTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vm0001PeakTrapEnable.setDescription('Set to enabled (1) to enable the peak alarm trap for this channel.')
vm0001StereoPairTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3), )
if mibBuilder.loadTexts: vm0001StereoPairTable.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairTable.setDescription('Each row contains information about one stereo pair on one VM0001 Analog Audio module in the managed VF200 frame.')
vm0001StereoPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"))
if mibBuilder.loadTexts: vm0001StereoPairEntry.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairEntry.setDescription('An Analog Audio module channel entry.')
vm0001StereoPairSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001StereoPairSlotNumber.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairSlotNumber.setDescription('The slot that this entry represents.')
vm0001StereoPairNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairNumber.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairNumber.setDescription('The channel within the module to which this signal is connected.')
vm0001StereoPairName = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairName.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairName.setDescription('The name of the signal connected to this channel.')
vm0001StereoPairDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairDescription.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoPairDescription.setDescription('Descriptive identifier of the signal connected to this channel.')
vm0001MonoFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoFilter.setStatus('current')
if mibBuilder.loadTexts: vm0001MonoFilter.setDescription('The filter type currently selected for the mono alarm for this stereo pair.')
vm0001MonoDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoDuration.setStatus('current')
if mibBuilder.loadTexts: vm0001MonoDuration.setDescription('The mono duration, in milliseconds, at which to alarm, for this stereo pair.')
vm0001MonoAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoAlarmState.setStatus('current')
if mibBuilder.loadTexts: vm0001MonoAlarmState.setDescription('The current state of the mono alarm for this stereo pair.')
vm0001MonoAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoAlarmAck.setStatus('current')
if mibBuilder.loadTexts: vm0001MonoAlarmAck.setDescription('Set to acknowledge (3) to acknowledge a triggered mono alarm for this stereo pair.')
vm0001MonoTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoTrapEnable.setStatus('current')
if mibBuilder.loadTexts: vm0001MonoTrapEnable.setDescription('Set to enabled (1) to enable the high APL alarm trap for this stereo pair.')
vm0001StereoOutOfPhaseFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseFilter.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseFilter.setDescription('The filter type currently selected for the stereo out of phase alarm for this stereo pair.')
vm0001StereoOutOfPhaseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseDuration.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseDuration.setDescription('The stereo out of phase duration, in milliseconds, at which to alarm, for this stereo pair.')
vm0001StereoOutOfPhaseAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmState.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmState.setDescription('The current state of the stereo out of phase alarm for this stereo pair.')
vm0001StereoOutOfPhaseAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmAck.setStatus('current')
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmAck.setDescription('Set to acknowledge (3) to acknowledge a triggered stereo out of phase alarm for this stereo pair.')
vm0001AnalogAudioEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4))
vm0001AnalogAudioEventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0))
analogAudioAPLHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 1)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioAPLHighAlarm.setStatus('current')
if mibBuilder.loadTexts: analogAudioAPLHighAlarm.setDescription('An Analog Audio APL high alarm was triggered.')
analogAudioAPLLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 2)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioAPLLowAlarm.setStatus('current')
if mibBuilder.loadTexts: analogAudioAPLLowAlarm.setDescription('An Analog Audio APL low alarm was triggered.')
analogAudioPeakAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 3)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioPeakAlarm.setStatus('current')
if mibBuilder.loadTexts: analogAudioPeakAlarm.setDescription('An Analog Audio peak threshold exceeded alarm was triggered.')
analogAudioMonoAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 4)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
if mibBuilder.loadTexts: analogAudioMonoAlarm.setStatus('current')
if mibBuilder.loadTexts: analogAudioMonoAlarm.setDescription('An Analog Audio mono alarm was triggered.')
analogAudioStereoOutOfPhaseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 5)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
if mibBuilder.loadTexts: analogAudioStereoOutOfPhaseAlarm.setStatus('current')
if mibBuilder.loadTexts: analogAudioStereoOutOfPhaseAlarm.setDescription('An Analog Audio stereo out of phase alarm was triggered.')
mibBuilder.exportSymbols("VIDEOFRAME-SIGMON-VM0001-MIB", vm0001SlotNumber=vm0001SlotNumber, vm0001AplLowThreshold=vm0001AplLowThreshold, vm0001AnalogAudio=vm0001AnalogAudio, vm0001AplLowDuration=vm0001AplLowDuration, vm0001AnalogAudioEventsV2=vm0001AnalogAudioEventsV2, vm0001StereoPairDescription=vm0001StereoPairDescription, vm0001PeakThreshold=vm0001PeakThreshold, vm0001Active=vm0001Active, vfProductsVM0001Reg=vfProductsVM0001Reg, vm0001PeakTrapEnable=vm0001PeakTrapEnable, vm0001ZerodBCalibrationSet=vm0001ZerodBCalibrationSet, vm0001PeakPeriod=vm0001PeakPeriod, vm0001PeakAlarmState=vm0001PeakAlarmState, PYSNMP_MODULE_ID=videoframeSigmonVm0001MIB, vm0001FirmwareRev=vm0001FirmwareRev, vm0001StereoPairNumber=vm0001StereoPairNumber, analogAudioStereoOutOfPhaseAlarm=analogAudioStereoOutOfPhaseAlarm, analogAudioAPLHighAlarm=analogAudioAPLHighAlarm, vm0001StereoPairEntry=vm0001StereoPairEntry, vm0001AplLowAlarmState=vm0001AplLowAlarmState, vm0001AplHighDuration=vm0001AplHighDuration, vm0001AplHighAlarmAck=vm0001AplHighAlarmAck, vm0001AplLowAlarmAck=vm0001AplLowAlarmAck, vm0001StereoPairTable=vm0001StereoPairTable, vm0001StereoPairSlotNumber=vm0001StereoPairSlotNumber, vm0001MonoFilter=vm0001MonoFilter, vm0001MonoAlarmAck=vm0001MonoAlarmAck, vm0001AplHighTrapEnable=vm0001AplHighTrapEnable, analogAudioAPLLowAlarm=analogAudioAPLLowAlarm, vm0001AplHighAlarmState=vm0001AplHighAlarmState, vm0001AplLowTrapEnable=vm0001AplLowTrapEnable, vm0001SignalNumber=vm0001SignalNumber, vm0001StereoOutOfPhaseAlarmAck=vm0001StereoOutOfPhaseAlarmAck, vm0001MonoTrapEnable=vm0001MonoTrapEnable, vm0001StereoOutOfPhaseDuration=vm0001StereoOutOfPhaseDuration, analogAudioMonoAlarm=analogAudioMonoAlarm, vm0001Locate=vm0001Locate, vm0001SignalName=vm0001SignalName, vm0001AnalogAudioEvents=vm0001AnalogAudioEvents, vm0001SignalEntry=vm0001SignalEntry, vm0001AplHighThreshold=vm0001AplHighThreshold, vm0001Entry=vm0001Entry, analogAudioPeakAlarm=analogAudioPeakAlarm, vm0001ZerodBCalibrationValue=vm0001ZerodBCalibrationValue, vm0001Table=vm0001Table, videoframeSigmonVm0001MIB=videoframeSigmonVm0001MIB, vm0001SignalTable=vm0001SignalTable, vm0001StereoOutOfPhaseAlarmState=vm0001StereoOutOfPhaseAlarmState, vm0001SignalDescription=vm0001SignalDescription, vm0001SignalSlotNumber=vm0001SignalSlotNumber, vm0001CurrentAplRaw=vm0001CurrentAplRaw, vm0001MonoAlarmState=vm0001MonoAlarmState, vm0001StereoPairName=vm0001StereoPairName, vm0001StereoOutOfPhaseFilter=vm0001StereoOutOfPhaseFilter, vm0001PeakAlarmAck=vm0001PeakAlarmAck, vm0001MonoDuration=vm0001MonoDuration)
