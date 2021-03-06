#
# PySNMP MIB module BCS-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BCS-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcs, = mibBuilder.importSymbols("BCS-IDENT-MIB", "bcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter64, Counter32, MibIdentifier, Bits, ObjectIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter64", "Counter32", "MibIdentifier", "Bits", "ObjectIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcsTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1166, 7, 3))
if mibBuilder.loadTexts: bcsTraps.setLastUpdated('200603280000Z')
if mibBuilder.loadTexts: bcsTraps.setOrganization('Motorola Connected Home Solutions')
bcsTrapElements = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1))
bcsTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2))
class ConfigChangeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("staged", 1), ("applied", 2), ("saved", 3))

class ConfigChangeAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("waitingRetune", 1), ("waitingSave", 2), ("waitingReboot", 3))

trapIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIdentifier.setStatus('current')
trapSequenceId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSequenceId.setStatus('current')
trapNetworkElemModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemModelNumber.setStatus('current')
trapNetworkElemSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemSerialNum.setStatus('current')
trapPerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cleared", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPerceivedSeverity.setStatus('current')
trapNetworkElemOperState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemOperState.setStatus('current')
trapNetworkElemAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAlarmStatus.setStatus('current')
trapNetworkElemAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2), ("shuttingDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAdminState.setStatus('current')
trapNetworkElemAvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inTest", 1), ("failed", 2), ("powerOff", 3), ("offLine", 4), ("offDuty", 5), ("dependency", 6), ("degraded", 7), ("notInstalled", 8), ("logFull", 9), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAvailStatus.setStatus('current')
trapText = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapText.setStatus('current')
trapNETrapLastTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNETrapLastTrapTimeStamp.setStatus('current')
trapChangedObjectId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 12), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedObjectId.setStatus('current')
trapAdditionalInfoInteger1 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger1.setStatus('current')
trapAdditionalInfoInteger2 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger2.setStatus('current')
trapAdditionalInfoInteger3 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger3.setStatus('current')
trapChangedValueDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueDisplayString.setStatus('current')
trapChangedValueOID = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueOID.setStatus('current')
trapChangedValueIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueIpAddress.setStatus('current')
trapChangedValueInteger = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueInteger.setStatus('current')
numberOfTrapReceivers = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfTrapReceivers.setStatus('current')
trapReceiversTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2), )
if mibBuilder.loadTexts: trapReceiversTable.setStatus('current')
trapReceiversEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1), ).setIndexNames((0, "BCS-TRAPS-MIB", "trapReceiversTableIndex"))
if mibBuilder.loadTexts: trapReceiversEntry.setStatus('current')
trapReceiversTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: trapReceiversTableIndex.setStatus('current')
trapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverAddr.setStatus('current')
trapReceiverCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverCommunityString.setStatus('current')
trapToBeSendQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 1000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapToBeSendQueueSize.setStatus('current')
trapSentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 300)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSentQueueSize.setStatus('current')
trapThrottlingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 6), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapThrottlingRate.setStatus('current')
trapLastSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLastSent.setStatus('current')
trapReceiversEntryOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiversEntryOperState.setStatus('current')
trapResendRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 9), Integer32().clone(2147483647)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapResendRequest.setStatus('current')
numberOfDiscriminators = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfDiscriminators.setStatus('current')
trapDiscrimTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4), )
if mibBuilder.loadTexts: trapDiscrimTable.setStatus('current')
trapDiscrimEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1), ).setIndexNames((0, "BCS-TRAPS-MIB", "trapDiscrimTableIndex"))
if mibBuilder.loadTexts: trapDiscrimEntry.setStatus('current')
trapDiscrimTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: trapDiscrimTableIndex.setStatus('current')
trapDiscrimReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimReceiverAddr.setStatus('current')
trapDiscrimAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10))).clone(namedValues=NamedValues(("offDuty", 5), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDiscrimAvailabilityStatus.setStatus('current')
trapDiscrimWeeklyMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimWeeklyMask.setStatus('current')
trapDiscrimDailyStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStartTime.setStatus('current')
trapDiscrimDailyStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStopTime.setStatus('current')
trapSeverityDiscrim = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSeverityDiscrim.setStatus('current')
trapDiscrimOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimOperationalState.setStatus('current')
trapDiscrimConfigChangeCntl = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimConfigChangeCntl.setStatus('current')
mibBuilder.exportSymbols("BCS-TRAPS-MIB", trapChangedValueIpAddress=trapChangedValueIpAddress, trapDiscrimConfigChangeCntl=trapDiscrimConfigChangeCntl, trapReceiverCommunityString=trapReceiverCommunityString, trapDiscrimAvailabilityStatus=trapDiscrimAvailabilityStatus, trapNETrapLastTrapTimeStamp=trapNETrapLastTrapTimeStamp, trapThrottlingRate=trapThrottlingRate, trapReceiversEntryOperState=trapReceiversEntryOperState, trapAdditionalInfoInteger2=trapAdditionalInfoInteger2, trapDiscrimDailyStartTime=trapDiscrimDailyStartTime, trapDiscrimEntry=trapDiscrimEntry, trapPerceivedSeverity=trapPerceivedSeverity, trapNetworkElemModelNumber=trapNetworkElemModelNumber, trapDiscrimDailyStopTime=trapDiscrimDailyStopTime, bcsTraps=bcsTraps, trapDiscrimTable=trapDiscrimTable, trapSeverityDiscrim=trapSeverityDiscrim, trapResendRequest=trapResendRequest, trapReceiversEntry=trapReceiversEntry, trapReceiverAddr=trapReceiverAddr, trapDiscrimTableIndex=trapDiscrimTableIndex, trapDiscrimOperationalState=trapDiscrimOperationalState, trapIdentifier=trapIdentifier, bcsTrapElements=bcsTrapElements, trapNetworkElemAdminState=trapNetworkElemAdminState, trapNetworkElemSerialNum=trapNetworkElemSerialNum, trapChangedValueInteger=trapChangedValueInteger, trapDiscrimWeeklyMask=trapDiscrimWeeklyMask, PYSNMP_MODULE_ID=bcsTraps, trapNetworkElemAlarmStatus=trapNetworkElemAlarmStatus, trapAdditionalInfoInteger1=trapAdditionalInfoInteger1, trapSequenceId=trapSequenceId, trapToBeSendQueueSize=trapToBeSendQueueSize, trapChangedValueDisplayString=trapChangedValueDisplayString, numberOfDiscriminators=numberOfDiscriminators, trapNetworkElemOperState=trapNetworkElemOperState, trapReceiversTable=trapReceiversTable, trapAdditionalInfoInteger3=trapAdditionalInfoInteger3, numberOfTrapReceivers=numberOfTrapReceivers, bcsTrapControl=bcsTrapControl, ConfigChangeAction=ConfigChangeAction, trapReceiversTableIndex=trapReceiversTableIndex, trapChangedObjectId=trapChangedObjectId, trapLastSent=trapLastSent, trapChangedValueOID=trapChangedValueOID, trapSentQueueSize=trapSentQueueSize, trapText=trapText, ConfigChangeState=ConfigChangeState, trapNetworkElemAvailStatus=trapNetworkElemAvailStatus, trapDiscrimReceiverAddr=trapDiscrimReceiverAddr)
