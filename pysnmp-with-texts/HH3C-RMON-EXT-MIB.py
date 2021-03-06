#
# PySNMP MIB module HH3C-RMON-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RMON-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hh3crmonExtend, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3crmonExtend")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
EntryStatus, = mibBuilder.importSymbols("RMON-MIB", "EntryStatus")
trapDestEntry, trapDestIndex = mibBuilder.importSymbols("RMON2-MIB", "trapDestEntry", "trapDestIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, MibIdentifier, iso, TimeTicks, Counter32, Integer32, IpAddress, Counter64, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "MibIdentifier", "iso", "TimeTicks", "Counter32", "Integer32", "IpAddress", "Counter64", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cperformance = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4))
hh3cperformance.setRevisions(('2003-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cperformance.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cperformance.setLastUpdated('200303150000Z')
if mibBuilder.loadTexts: hh3cperformance.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cperformance.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cperformance.setDescription(' ')
hh3cprialarmTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1), )
if mibBuilder.loadTexts: hh3cprialarmTable.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmTable.setDescription('A list of alarm entries.')
hh3cprialarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1), ).setIndexNames((0, "HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"))
if mibBuilder.loadTexts: hh3cprialarmEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmEntry.setDescription('A list of parameters that set up a periodic checking for alarm conditions. For example, an instance of the alarmValue object might be named alarmValue.8')
hh3cprialarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cprialarmIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmIndex.setDescription('An index that uniquely identifies an entry in the alarm table. Each such entry defines a diagnostic sample at a particular interval for an object on the device.')
hh3cprialarmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmInterval.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmInterval.setDescription('The interval in seconds over which the data is sampled and compared with the rising and falling thresholds. When setting this variable, care should be taken in the case of deltaValue sampling - the interval should be set short enough that the sampled variable is very unlikely to increase or decrease by more than 2^31 - 1 during a single sampling interval. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmVariable.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmVariable.setDescription('The object identifier of the particular variable to be sampled. Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge, or TimeTicks) may be sampled. Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view. Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe. During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned. If at any time the variable name of an established alarmEntry is no longer available in the selected MIB view, the probe must change the status of this alarmEntry to invalid(4). This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmSympol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmSympol.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmSympol.setDescription('')
hh3cprialarmSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("speedValue", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmSampleType.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmSampleType.setDescription('The method of sampling the selected variable and calculating the value to be compared against the thresholds. If the value of this object is absoluteValue(1), the value of the selected variable will be compared directly with the thresholds at the end of the sampling interval. If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference compared with the thresholds. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cprialarmValue.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmValue.setDescription('The value of the statistic during the last sampling period. For example, if the sample type is deltaValue, this value will be the difference between the samples at the beginning and end of the period. If the sample type is absoluteValue, this value will be the sampled value at the end of the period. This is the value that is compared with the rising and falling thresholds. The value during the current sampling period is not made available until the period is completed and will remain available until the next period completes.')
hh3cprialarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStartupAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmStartupAlarm.setDescription('The alarm that may be sent when this entry is first set to valid. If the first sample after this entry becomes valid is greater than or equal to the risingThreshold and alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single rising alarm will be generated. If the first sample after this entry becomes valid is less than or equal to the fallingThreshold and alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single falling alarm will be generated. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmRisingThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmRisingThreshold.setDescription('A threshold for the sampled statistic. When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is greater than or equal to this threshold and the associated alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3). After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the alarmFallingThreshold. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmFallingThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmFallingThreshold.setDescription('A threshold for the sampled statistic. When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is less than or equal to this threshold and the associated alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3). After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the alarmRisingThreshold. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmRisingEventIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmRisingEventIndex.setDescription('The index of the eventEntry that is used when a rising threshold is crossed. The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object. If there is no corresponding entry in the eventTable, then no association exists. In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmFallingEventIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmFallingEventIndex.setDescription('The index of the eventEntry that is used when a falling threshold is crossed. The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object. If there is no corresponding entry in the eventTable, then no association exists. In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index. This object may not be modified if the associated alarmStatus object is equal to valid(1).')
hh3cprialarmStatCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatCycle.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmStatCycle.setDescription('')
hh3cprialarmStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forever", 1), ("during", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatType.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmStatType.setDescription('')
hh3cprialarmOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 14), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmOwner.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmOwner.setDescription('The entity that configured this entry and is therefore using the resources assigned to it.')
hh3cprialarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 15), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cprialarmStatus.setDescription('The status of this alarm entry.')
hh3crmonEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5), )
if mibBuilder.loadTexts: hh3crmonEnableTable.setStatus('current')
if mibBuilder.loadTexts: hh3crmonEnableTable.setDescription('A list of enable rmon entries.')
hh3crmonEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1), ).setIndexNames((0, "HH3C-RMON-EXT-MIB", "hh3crmonEnableIfIndex"))
if mibBuilder.loadTexts: hh3crmonEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hh3crmonEnableEntry.setDescription('A list of parameters that set up a hh3crmonEnableTable')
hh3crmonEnableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3crmonEnableIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3crmonEnableIfIndex.setDescription('Specify an interface to enable rmon.')
hh3crmonEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3crmonEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hh3crmonEnableStatus.setDescription('Specify an interface to enable rmon.')
hh3cTrapDestTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6), )
if mibBuilder.loadTexts: hh3cTrapDestTable.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapDestTable.setDescription('Defines the trap destination Extend Table for providing, via SNMP, the capability of configure a trap dest.')
hh3cTrapDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1), )
trapDestEntry.registerAugmentions(("HH3C-RMON-EXT-MIB", "hh3cTrapDestEntry"))
hh3cTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cTrapDestEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapDestEntry.setDescription('Defines an entry in the hh3cTrapDestTable.')
hh3cTrapDestVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("snmpv1", 1), ("snmpv2", 2), ("snmpv3andauthen", 3), ("snmpv3andnoauthen", 4), ("snmpv3andpriv", 5))).clone('snmpv1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cTrapDestVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapDestVersion.setDescription('The version for trap destination. This object may not be modified if the associated trapDestStatus object is equal to active(1).')
hh3crmonExtendEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0))
if mibBuilder.loadTexts: hh3crmonExtendEventsV2.setStatus('current')
if mibBuilder.loadTexts: hh3crmonExtendEventsV2.setDescription('Definition point for pri RMON notifications.')
hh3cpririsingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 1)).setObjects(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmRisingThreshold"))
if mibBuilder.loadTexts: hh3cpririsingAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cpririsingAlarm.setDescription('The SNMP trap that is generated when an alarm entry crosses its rising threshold and generates an event that is configured for sending SNMP traps.')
hh3cprifallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 2)).setObjects(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmFallingThreshold"))
if mibBuilder.loadTexts: hh3cprifallingAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cprifallingAlarm.setDescription('The SNMP trap that is generated when an alarm entry crosses its falling threshold and generates an event that is configured for sending SNMP traps.')
mibBuilder.exportSymbols("HH3C-RMON-EXT-MIB", hh3cprialarmSympol=hh3cprialarmSympol, hh3cprifallingAlarm=hh3cprifallingAlarm, hh3cprialarmSampleType=hh3cprialarmSampleType, hh3cpririsingAlarm=hh3cpririsingAlarm, hh3crmonEnableIfIndex=hh3crmonEnableIfIndex, hh3cprialarmFallingEventIndex=hh3cprialarmFallingEventIndex, hh3cprialarmInterval=hh3cprialarmInterval, hh3cTrapDestTable=hh3cTrapDestTable, hh3crmonExtendEventsV2=hh3crmonExtendEventsV2, hh3cprialarmTable=hh3cprialarmTable, hh3cprialarmOwner=hh3cprialarmOwner, PYSNMP_MODULE_ID=hh3cperformance, hh3crmonEnableStatus=hh3crmonEnableStatus, hh3cprialarmStatType=hh3cprialarmStatType, hh3crmonEnableEntry=hh3crmonEnableEntry, hh3cTrapDestEntry=hh3cTrapDestEntry, hh3cperformance=hh3cperformance, hh3cprialarmEntry=hh3cprialarmEntry, hh3cprialarmIndex=hh3cprialarmIndex, hh3cprialarmRisingThreshold=hh3cprialarmRisingThreshold, hh3cprialarmStatus=hh3cprialarmStatus, hh3cprialarmVariable=hh3cprialarmVariable, hh3cprialarmStartupAlarm=hh3cprialarmStartupAlarm, hh3cTrapDestVersion=hh3cTrapDestVersion, hh3crmonEnableTable=hh3crmonEnableTable, hh3cprialarmStatCycle=hh3cprialarmStatCycle, hh3cprialarmRisingEventIndex=hh3cprialarmRisingEventIndex, hh3cprialarmValue=hh3cprialarmValue, hh3cprialarmFallingThreshold=hh3cprialarmFallingThreshold)
