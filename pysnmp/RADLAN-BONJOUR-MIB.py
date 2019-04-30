#
# PySNMP MIB module RADLAN-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-BONJOUR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:36:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks, Bits, Integer32, MibIdentifier, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks", "Bits", "Integer32", "MibIdentifier", "iso", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rlBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 114))
rlBonjour.setRevisions(('2009-04-23 00:00', '2015-05-12 00:00',))
if mibBuilder.loadTexts: rlBonjour.setLastUpdated('201505120000Z')
if mibBuilder.loadTexts: rlBonjour.setOrganization('Marvell Computer Communications Ltd.')
rlBonjourPublish = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourPublish.setStatus('current')
class RlBonjourServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlBonjourNotPublished", 0), ("rlBonjourInactive", 1), ("rlBonjourRegistering", 2), ("rlBonjourRunning", 3))

class RlBonjourOperationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class RlBonjourOperationReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notExclude", 0), ("include", 1), ("notInclude", 2), ("exclude", 3), ("bonjourDisabled", 4), ("serviceDisabled", 5), ("noIPaddress", 6), ("l2InterfaceDown", 7), ("notPresent", 8), ("unknown", 9))

rlBonjourStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 2), )
if mibBuilder.loadTexts: rlBonjourStatusTable.setStatus('current')
rlBonjourStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 2, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusServiceName"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusIPInterfaceType"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusIPInterfaceAddr"))
if mibBuilder.loadTexts: rlBonjourStatusEntry.setStatus('current')
rlBonjourStatusServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setStatus('current')
rlBonjourStatusIPInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setStatus('current')
rlBonjourStatusIPInterfaceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setStatus('current')
rlBonjourStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 4), RlBonjourServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStatusState.setStatus('current')
rlBonjourStateTable = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 3), )
if mibBuilder.loadTexts: rlBonjourStateTable.setStatus('current')
rlBonjourStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 3, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourStateServiceName"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStateL2Interface"))
if mibBuilder.loadTexts: rlBonjourStateEntry.setStatus('current')
rlBonjourStateServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStateServiceName.setStatus('current')
rlBonjourStateL2Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setStatus('current')
rlBonjourStateOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 3), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setStatus('current')
rlBonjourStateOperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 4), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setStatus('current')
rlBonjourStateIPv6OperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 5), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationMode.setStatus('current')
rlBonjourStateIPv6OperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 6), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationReason.setStatus('current')
rlBonjourL2Table = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 4), )
if mibBuilder.loadTexts: rlBonjourL2Table.setStatus('current')
rlBonjourL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 4, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourL2Ifindex"))
if mibBuilder.loadTexts: rlBonjourL2Entry.setStatus('current')
rlBonjourL2Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setStatus('current')
rlBonjourL2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setStatus('current')
rlBonjourL2Mode = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2Mode.setStatus('current')
rlBonjourInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourInstanceName.setStatus('current')
rlBonjourHostName = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourHostName.setStatus('current')
mibBuilder.exportSymbols("RADLAN-BONJOUR-MIB", rlBonjourStateIPv6OperationReason=rlBonjourStateIPv6OperationReason, rlBonjourStatusTable=rlBonjourStatusTable, rlBonjourInstanceName=rlBonjourInstanceName, RlBonjourOperationState=RlBonjourOperationState, RlBonjourServiceState=RlBonjourServiceState, rlBonjourStateOperationMode=rlBonjourStateOperationMode, rlBonjourStatusState=rlBonjourStatusState, rlBonjourL2RowStatus=rlBonjourL2RowStatus, rlBonjourStateEntry=rlBonjourStateEntry, rlBonjourStateOperationReason=rlBonjourStateOperationReason, rlBonjourPublish=rlBonjourPublish, rlBonjourL2Table=rlBonjourL2Table, rlBonjourStateServiceName=rlBonjourStateServiceName, rlBonjourL2Ifindex=rlBonjourL2Ifindex, rlBonjourStatusServiceName=rlBonjourStatusServiceName, PYSNMP_MODULE_ID=rlBonjour, rlBonjourStateL2Interface=rlBonjourStateL2Interface, rlBonjourL2Mode=rlBonjourL2Mode, rlBonjourHostName=rlBonjourHostName, rlBonjourStatusIPInterfaceType=rlBonjourStatusIPInterfaceType, rlBonjourStateTable=rlBonjourStateTable, RlBonjourOperationReason=RlBonjourOperationReason, rlBonjour=rlBonjour, rlBonjourL2Entry=rlBonjourL2Entry, rlBonjourStateIPv6OperationMode=rlBonjourStateIPv6OperationMode, rlBonjourStatusIPInterfaceAddr=rlBonjourStatusIPInterfaceAddr, rlBonjourStatusEntry=rlBonjourStatusEntry)