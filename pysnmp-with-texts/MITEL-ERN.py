#
# PySNMP MIB module MITEL-ERN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-ERN
# Produced by pysmi-0.3.4 at Wed May  1 14:13:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
mitelAppCallServer, = mibBuilder.importSymbols("MITEL-MIB", "mitelAppCallServer")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, IpAddress, NotificationType, Counter32, Unsigned32, Gauge32, iso, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "NotificationType", "Counter32", "Unsigned32", "Gauge32", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Integer32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
mitelCsEmergencyResponse = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3))
mitelCsErSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 1), Integer32())
if mibBuilder.loadTexts: mitelCsErSeqNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErSeqNumber.setDescription('Same number used in the Emergency Call logs.')
mitelCsErCallType = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 2), Integer32())
if mibBuilder.loadTexts: mitelCsErCallType.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErCallType.setDescription('Type of Emergency Call.')
mitelCsErDetectTime = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 3), DateAndTime())
if mibBuilder.loadTexts: mitelCsErDetectTime.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErDetectTime.setDescription('The time that the emergency call occurred on the Call Server.')
mitelCsErCallingDN = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 4), DisplayString())
if mibBuilder.loadTexts: mitelCsErCallingDN.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErCallingDN.setDescription('The directory number dialed for the emergency call.')
mitelCsErCallingPNI = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 5), DisplayString())
if mibBuilder.loadTexts: mitelCsErCallingPNI.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErCallingPNI.setDescription('The PNI dialed for the emergency call.')
mitelCsErCesidDigits = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 6), DisplayString())
if mibBuilder.loadTexts: mitelCsErCesidDigits.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErCesidDigits.setDescription('The CESID assigned to the Dialing Number. May also be the default system CESID value or empty if the CESID is unknown.')
mitelCsErDialledDigits = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 7), DisplayString())
if mibBuilder.loadTexts: mitelCsErDialledDigits.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErDialledDigits.setDescription('The number dialed for the emergency call.')
mitelCsErRegistrationDN = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 8), DisplayString())
if mibBuilder.loadTexts: mitelCsErRegistrationDN.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErRegistrationDN.setDescription('The directory number dialed for the emergency call. This could be empty, the directory number of the device making the call, an incoming caller ID or remote CESID.')
mitelCsErUnackTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9), )
if mibBuilder.loadTexts: mitelCsErUnackTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErUnackTable.setDescription("A list of notifications sent from this agent that are expected to be acknowledged, but have not yet received the acknowledgement. One entry is created for each acknowledgeable notification transmitted from this agent. Managers are expected to delete the rows in this table to acknowledge receipt of the notification. To do so, the index is provided in the notification sent to the manager. Any unacknowledged notifications are removed at the agent's discretion. This table is kept in volatile memory.")
mitelCsErUnackTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1), ).setIndexNames((0, "MITEL-ERN", "mitelCsErUnackTableIndex"))
if mibBuilder.loadTexts: mitelCsErUnackTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErUnackTableEntry.setDescription('An entry containing unacknowledged notification information.')
mitelCsErUnackTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: mitelCsErUnackTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErUnackTableIndex.setDescription('The index of the row for the Manager to acknowledge the notification. If no acknowledgement is required, this will be 0. For require acknowledgement this is a unique value, greater than zero, for each row. The values are assigned contiguously starting from 1, and are not re-used (to allow for duplicated Set Requests for destruction of the row).')
mitelCsErUnackTableToken = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 9, 1, 2), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mitelCsErUnackTableToken.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCsErUnackTableToken.setDescription('The status of this row. A status of active indicates that an acknowledgement is still expected. Write a destroy(6) here to acknowledge this notification. A status of notInService indicates that no acknowledgement is expected.')
mitelCsErNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3, 10))
mitelCsErNotification = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 3) + (0,401)).setObjects(("SNMPv2-MIB", "sysName"), ("MITEL-ERN", "mitelCsErSeqNumber"), ("MITEL-ERN", "mitelCsErCallType"), ("MITEL-ERN", "mitelCsErDetectTime"), ("MITEL-ERN", "mitelCsErCallingDN"), ("MITEL-ERN", "mitelCsErCallingPNI"), ("MITEL-ERN", "mitelCsErCesidDigits"), ("MITEL-ERN", "mitelCsErDialledDigits"), ("MITEL-ERN", "mitelCsErRegistrationDN"), ("MITEL-ERN", "mitelCsErUnackTableIndex"), ("MITEL-ERN", "mitelCsErUnackTableToken"))
if mibBuilder.loadTexts: mitelCsErNotification.setDescription('This notification is generated whenever an emergency call condition is detected. The manager is expected to ....')
mibBuilder.exportSymbols("MITEL-ERN", mitelCsErCallingDN=mitelCsErCallingDN, mitelCsErRegistrationDN=mitelCsErRegistrationDN, Integer32=Integer32, DateAndTime=DateAndTime, mitelCsErUnackTableToken=mitelCsErUnackTableToken, mitelCsEmergencyResponse=mitelCsEmergencyResponse, mitelCsErDetectTime=mitelCsErDetectTime, mitelCsErCallingPNI=mitelCsErCallingPNI, mitelCsErNotification=mitelCsErNotification, mitelCsErCesidDigits=mitelCsErCesidDigits, mitelCsErDialledDigits=mitelCsErDialledDigits, mitelCsErUnackTableEntry=mitelCsErUnackTableEntry, mitelCsErUnackTable=mitelCsErUnackTable, mitelCsErCallType=mitelCsErCallType, mitelCsErUnackTableIndex=mitelCsErUnackTableIndex, mitelCsErSeqNumber=mitelCsErSeqNumber, mitelCsErNotifications=mitelCsErNotifications)
