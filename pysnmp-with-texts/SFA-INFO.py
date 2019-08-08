#
# PySNMP MIB module SFA-INFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SFA-INFO
# Produced by pysmi-0.3.4 at Wed May  1 15:01:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, ModuleIdentity, IpAddress, TimeTicks, Counter32, ObjectIdentity, Unsigned32, NotificationType, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
datadirect = MibIdentifier((1, 3, 6, 1, 4, 1, 6894))
unit = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2))
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2, 10))
class DisplayString(OctetString):
    pass

tempNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tempNumber.setDescription('The number of temperature sensors in the system.')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 2), )
if mibBuilder.loadTexts: tempTable.setStatus('mandatory')
if mibBuilder.loadTexts: tempTable.setDescription('A list of temperature sensor entries. The number of entries is given by the value of tempNumber.')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1), ).setIndexNames((0, "SFA-INFO", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tempEntry.setDescription('A temp entry containing temperature sensor status.')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempIndex.setStatus('mandatory')
if mibBuilder.loadTexts: tempIndex.setDescription('A unique value for each temperature sensor. Its value ranges between 1 and the value of tempNumber.')
tempEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncId.setStatus('mandatory')
if mibBuilder.loadTexts: tempEncId.setDescription('A unique value displaying the enclosure ID number of the temperature sensor.')
tempEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncPos.setStatus('mandatory')
if mibBuilder.loadTexts: tempEncPos.setDescription('A unique value displaying the position number of the temperature sensor.')
tempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempStatus.setStatus('mandatory')
if mibBuilder.loadTexts: tempStatus.setDescription('The current temperature status of the unit.')
fanNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNumber.setStatus('mandatory')
if mibBuilder.loadTexts: fanNumber.setDescription('The number of fans in the system.')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 4), )
if mibBuilder.loadTexts: fanTable.setStatus('mandatory')
if mibBuilder.loadTexts: fanTable.setDescription('A list of fan entries. The number of entries is given by the value of fanNumber.')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1), ).setIndexNames((0, "SFA-INFO", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fanEntry.setDescription('A fan entry containing fan status.')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fanIndex.setDescription('A unique value for each fan. Its value ranges between 1 and the value of fanNumber.')
fanEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncId.setStatus('mandatory')
if mibBuilder.loadTexts: fanEncId.setDescription('A unique value displaying the enclosure ID number of the fan.')
fanEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncPos.setStatus('mandatory')
if mibBuilder.loadTexts: fanEncPos.setDescription('A unique value displaying the position number of the fan.')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fanStatus.setDescription('The current fan status of the unit.')
powerNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNumber.setStatus('mandatory')
if mibBuilder.loadTexts: powerNumber.setDescription('The number of power supplies in the system.')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 6), )
if mibBuilder.loadTexts: powerTable.setStatus('mandatory')
if mibBuilder.loadTexts: powerTable.setDescription('A list of power supply entries. The number of entries is given by the value of powerNumber.')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1), ).setIndexNames((0, "SFA-INFO", "powerIndex"))
if mibBuilder.loadTexts: powerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: powerEntry.setDescription('A power entry containing power supply status.')
powerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: powerIndex.setDescription('A unique value for each power supply. Its value ranges between 1 and the value of powerNumber.')
powerEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncId.setStatus('mandatory')
if mibBuilder.loadTexts: powerEncId.setDescription('A unique value displaying the enclosure ID number of the power supply.')
powerEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncPos.setStatus('mandatory')
if mibBuilder.loadTexts: powerEncPos.setDescription('A unique value displaying the position number of the power supply.')
powerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: powerStatus.setDescription('The current power supply status of the unit.')
poolNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumber.setStatus('mandatory')
if mibBuilder.loadTexts: poolNumber.setDescription('The number of pools in system.')
poolTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 8), )
if mibBuilder.loadTexts: poolTable.setStatus('mandatory')
if mibBuilder.loadTexts: poolTable.setDescription('A list of pool entries. The number of entries is given by the value of poolNumber.')
poolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1), ).setIndexNames((0, "SFA-INFO", "poolIndex"))
if mibBuilder.loadTexts: poolEntry.setStatus('mandatory')
if mibBuilder.loadTexts: poolEntry.setDescription("A pool entry containing a pool's status.")
poolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: poolIndex.setDescription('A unique value for each pool. Its value ranges between 1 and the value of poolNumber.')
poolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolId.setStatus('mandatory')
if mibBuilder.loadTexts: poolId.setDescription('An integer which give the pool id as displayed in the OID.')
poolType = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("storage", 1), ("spare", 2), ("unassigned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolType.setStatus('mandatory')
if mibBuilder.loadTexts: poolType.setDescription('The type of pool.')
poolNumDisks = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumDisks.setStatus('mandatory')
if mibBuilder.loadTexts: poolNumDisks.setDescription('The number of disks in the corresponding pool.')
physicalDiskTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 9), )
if mibBuilder.loadTexts: physicalDiskTable.setStatus('mandatory')
if mibBuilder.loadTexts: physicalDiskTable.setDescription('A list of disk entries. The number of entries is given by the value of poolNumDisks.')
physicalDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1), ).setIndexNames((0, "SFA-INFO", "physDiskIndex"))
if mibBuilder.loadTexts: physicalDiskEntry.setStatus('mandatory')
if mibBuilder.loadTexts: physicalDiskEntry.setDescription("The information related to a disk's status.")
physDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskIndex.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskIndex.setDescription('A unique value for each physical disk within a pool.')
physDiskPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskPoolId.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskPoolId.setDescription('An integer which give the pool id as displayed in the OID.')
physDiskId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskId.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskId.setDescription('An integer which give the physical disk id as displayed in the OID.')
physDiskWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskWWN.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskWWN.setDescription('A string which gives the WWN of the physical disk.')
physDiskEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskEnc.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskEnc.setDescription('A string which gives the physical disk enclosure number.')
physDiskSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskSlot.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskSlot.setDescription('An integer which give the physical disk position number.')
physDiskState = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("failed", 2), ("predictedfailure", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskState.setStatus('mandatory')
if mibBuilder.loadTexts: physDiskState.setDescription('An integer which gives the state of a physical disk.')
systemName = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemName.setStatus('mandatory')
if mibBuilder.loadTexts: systemName.setDescription('The name that has been assigned to the system.')
eventLogTrapLevel = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTrapLevel.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogTrapLevel.setDescription("This object specifies the eventLogTrap level in conjunction with an event's severity level. When an event occurs and if its severity level is at or below the value specified by this object instance, the agent will send the associated eventLogTrap to configured recipients.")
eventLogNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogNumEntries.setDescription('The number of entries in the Event Table.')
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3), )
if mibBuilder.loadTexts: eventLogTable.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogTable.setDescription('The table of event entries.')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1), ).setIndexNames((0, "SFA-INFO", "eventLogIndex"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogEntry.setDescription('An entry of the event table.')
eventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogIndex.setDescription('This object identifies the event entry.')
eventLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogLevel.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogLevel.setDescription('This object identifies the severity level of this event entry.')
eventLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogDescr.setStatus('mandatory')
if mibBuilder.loadTexts: eventLogDescr.setDescription('This object identifies the textual description of the event.')
mibBuilder.exportSymbols("SFA-INFO", physDiskState=physDiskState, powerNumber=powerNumber, eventLogTable=eventLogTable, fanStatus=fanStatus, physDiskSlot=physDiskSlot, eventLogLevel=eventLogLevel, fanTable=fanTable, tempNumber=tempNumber, fanEntry=fanEntry, tempEncPos=tempEncPos, physDiskIndex=physDiskIndex, fanEncId=fanEncId, tempTable=tempTable, physDiskWWN=physDiskWWN, poolNumDisks=poolNumDisks, physicalDiskEntry=physicalDiskEntry, poolNumber=poolNumber, poolTable=poolTable, poolType=poolType, powerStatus=powerStatus, unit=unit, eventLogIndex=eventLogIndex, tempStatus=tempStatus, powerEncId=powerEncId, physDiskEnc=physDiskEnc, tempEntry=tempEntry, DisplayString=DisplayString, systemName=systemName, eventLogEntry=eventLogEntry, eventLogNumEntries=eventLogNumEntries, poolEntry=poolEntry, tempEncId=tempEncId, fanNumber=fanNumber, poolIndex=poolIndex, powerTable=powerTable, eventLogTrapLevel=eventLogTrapLevel, eventLog=eventLog, tempIndex=tempIndex, poolId=poolId, fanIndex=fanIndex, powerEntry=powerEntry, fanEncPos=fanEncPos, powerEncPos=powerEncPos, physicalDiskTable=physicalDiskTable, powerIndex=powerIndex, physDiskPoolId=physDiskPoolId, physDiskId=physDiskId, datadirect=datadirect, eventLogDescr=eventLogDescr)