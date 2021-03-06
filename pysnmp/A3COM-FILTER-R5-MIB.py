#
# PySNMP MIB module A3COM-FILTER-R5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-FILTER-R5-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:19 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
MacAddress, = mibBuilder.importSymbols("RFC1286-MIB", "MacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, ModuleIdentity, Unsigned32, Integer32, NotificationType, ObjectIdentity, iso, Bits, IpAddress, MibIdentifier, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "ObjectIdentity", "iso", "Bits", "IpAddress", "MibIdentifier", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 10))
a3ComFilterCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 10, 1))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3filterControl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableMatchOne", 1), ("enableCheckAll", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterControl.setStatus('mandatory')
a3filterDefaultAction = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterDefaultAction.setStatus('mandatory')
a3filterBridgeSelect = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("noFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterBridgeSelect.setStatus('mandatory')
a3filterIpSelect = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("noFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterIpSelect.setStatus('mandatory')
a3filterIpxSelect = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("noFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterIpxSelect.setStatus('mandatory')
a3filterAppleTalkSelect = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("noFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterAppleTalkSelect.setStatus('mandatory')
a3filterDecSelect = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("noFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterDecSelect.setStatus('mandatory')
a3filterUserMaskTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 10, 2), )
if mibBuilder.loadTexts: a3filterUserMaskTable.setStatus('mandatory')
a3filterUserMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1), ).setIndexNames((0, "A3COM-FILTER-R5-MIB", "a3filterUserMaskIndex"))
if mibBuilder.loadTexts: a3filterUserMaskEntry.setStatus('mandatory')
a3filterUserMaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterUserMaskIndex.setStatus('mandatory')
a3filterUserMaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskName.setStatus('mandatory')
a3filterUserMaskLocType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("protocolFieldSemantics", 1), ("offsetLengthSemantics", 2), ("dataLinkOffsetLengthSemantics", 3), ("ipOffsetLengthSemantics", 4), ("ipxOffsetLengthSemantics", 5), ("appleTalkOffsetLengthSemantics", 6), ("decNetOffsetLengthSemantics", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskLocType.setStatus('mandatory')
a3filterUserMaskLocField = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47))).clone(namedValues=NamedValues(("dlDestinationAddress", 1), ("dlSourceAddress", 2), ("dlAddress", 3), ("dlProtocol", 4), ("dlLength", 5), ("dlDSAP", 6), ("dlSSAP", 7), ("dlLSAP", 8), ("dlOUI", 9), ("dlLanID", 10), ("ipDestAddress", 11), ("ipSourceAddress", 12), ("ipAddress", 13), ("ipProtocol", 14), ("ipDestinationPort", 15), ("ipSourcePort", 16), ("ipPort", 17), ("ipOptions", 18), ("ipTOS", 19), ("ipxDestNetwork", 20), ("ipxSourceNetwork", 21), ("ipxNetwork", 22), ("ipxDestAddress", 23), ("ipxSourceAddress", 24), ("ipxAddress", 25), ("ipxDestSocket", 26), ("ipxSourceSocket", 27), ("ipxSocket", 28), ("atDestinationNetwork", 29), ("atSourceNetwork", 30), ("atNetwork", 31), ("atDestinationNodeID", 32), ("atSourceNodeID", 33), ("atNodeID", 34), ("atDestinationSocket", 35), ("atSourceSocket", 36), ("atSocket", 37), ("atDDPType", 38), ("decDestinationArea", 39), ("decSourceArea", 40), ("decArea", 41), ("decDestAddress", 42), ("decSourceAddress", 43), ("decAddress", 44), ("ipxPktLength", 45), ("ipxPktType", 46), ("ipxTransportCtl", 47)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskLocField.setStatus('mandatory')
a3filterUserMaskLocOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskLocOffset.setStatus('mandatory')
a3filterUserMaskLocLength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("reserved", 3), ("four", 4), ("rsvd", 5), ("six", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskLocLength.setStatus('mandatory')
a3filterUserMaskOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("or", 2), ("and", 3), ("xor", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskOperator.setStatus('mandatory')
a3filterUserMaskOperand = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskOperand.setStatus('mandatory')
a3filterUserMaskComparison = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("equal", 1), ("notEqual", 2), ("greaterThan", 3), ("greaterThanOrEqual", 4), ("lessThan", 5), ("lessThanOrEqual", 6), ("inclusiveRange", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskComparison.setStatus('mandatory')
a3filterUserMaskMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("all", 1), ("bits", 2), ("value", 3), ("valueRange", 4), ("userGroup", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskMatchType.setStatus('mandatory')
a3filterUserMaskMatchBits = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskMatchBits.setStatus('mandatory')
a3filterUserMaskMatchValue1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskMatchValue1.setStatus('mandatory')
a3filterUserMaskMatchValue2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskMatchValue2.setStatus('mandatory')
a3filterUserMaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 14), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserMaskStatus.setStatus('mandatory')
a3filterBuiltInMaskTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 10, 3), )
if mibBuilder.loadTexts: a3filterBuiltInMaskTable.setStatus('mandatory')
a3filterBuiltInMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1), ).setIndexNames((0, "A3COM-FILTER-R5-MIB", "a3filterBuiltInMaskIndex"))
if mibBuilder.loadTexts: a3filterBuiltInMaskEntry.setStatus('mandatory')
a3filterBuiltInMaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(257, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterBuiltInMaskIndex.setStatus('mandatory')
a3filterBuiltInMaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterBuiltInMaskName.setStatus('mandatory')
a3filterBuiltInMaskFieldValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60))).clone(namedValues=NamedValues(("dlBroadCast", 1), ("dlMultiCast", 2), ("appleTalkII", 3), ("aarp", 4), ("arp", 5), ("clnp", 6), ("decPhaseIV", 7), ("dlTest", 8), ("ip", 9), ("ipx", 10), ("lat", 11), ("ipNetMap", 12), ("xnsNetMap", 13), ("stp", 14), ("vip", 15), ("xns", 16), ("specificRoute", 17), ("singleRouteExp", 18), ("allRouteExp", 19), ("allRouteType", 20), ("icmp", 21), ("tcp", 22), ("udp", 23), ("dns", 24), ("finger", 25), ("ftp", 26), ("whois", 27), ("simpleMailTrans", 28), ("snmp", 29), ("sunRPC", 30), ("telnet", 31), ("tftp", 32), ("x400", 33), ("zero", 34), ("one", 35), ("two", 36), ("three", 37), ("four", 38), ("five", 39), ("six", 40), ("seven", 41), ("ipxBroadCast", 42), ("fileServicePkt", 43), ("sap", 44), ("rip", 45), ("netBIOS", 46), ("diag", 47), ("rtmps", 48), ("nis", 49), ("zis", 50), ("rtmprs", 51), ("nbp", 52), ("atp", 53), ("aep", 54), ("rtmprq", 55), ("zip", 56), ("adsp", 57), ("ipxTraceRt", 58), ("ipxPing", 59), ("ipxNwSec", 60)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterBuiltInMaskFieldValue.setStatus('mandatory')
a3filterUserGrpTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 10, 4), )
if mibBuilder.loadTexts: a3filterUserGrpTable.setStatus('mandatory')
a3filterUserGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1), ).setIndexNames((0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpIndex"))
if mibBuilder.loadTexts: a3filterUserGrpEntry.setStatus('mandatory')
a3filterUserGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterUserGrpIndex.setStatus('mandatory')
a3filterUserGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserGrpName.setStatus('mandatory')
a3filterUserGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserGrpStatus.setStatus('mandatory')
a3filterUserGrpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 10, 5), )
if mibBuilder.loadTexts: a3filterUserGrpAddrTable.setStatus('mandatory')
a3filterUserGrpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1), ).setIndexNames((0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpAddrIndex"), (0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpAddress"))
if mibBuilder.loadTexts: a3filterUserGrpAddrEntry.setStatus('mandatory')
a3filterUserGrpAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterUserGrpAddrIndex.setStatus('mandatory')
a3filterUserGrpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterUserGrpAddress.setStatus('mandatory')
a3filterUserGrpAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterUserGrpAddrStatus.setStatus('mandatory')
a3filterPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 10, 6), )
if mibBuilder.loadTexts: a3filterPolicyTable.setStatus('mandatory')
a3filterPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1), ).setIndexNames((0, "A3COM-FILTER-R5-MIB", "a3filterPolicyIndex"))
if mibBuilder.loadTexts: a3filterPolicyEntry.setStatus('mandatory')
a3filterPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterPolicyIndex.setStatus('mandatory')
a3filterPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyName.setStatus('mandatory')
a3filterPolicyAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2), ("count", 3), ("sequence", 4), ("prioritizeHigh", 5), ("prioritizeMed", 6), ("prioritizeLow", 7), ("doddiscard", 8), ("x25ProfId", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyAction.setStatus('mandatory')
a3filterPolicyMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyMask1.setStatus('mandatory')
a3filterPolicyMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyMask2.setStatus('mandatory')
a3filterPolicyMask3 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyMask3.setStatus('mandatory')
a3filterPolicyMask4 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyMask4.setStatus('mandatory')
a3filterPolicyContext = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("all", 1), ("atPorts1", 2), ("fromPorts1", 3), ("fromPorts1ToPorts2", 4), ("toPorts1", 5), ("betweenPorts1AndPorts2", 6), ("amongPorts1", 7))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyContext.setStatus('mandatory')
a3filterPolicyPorts1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyPorts1.setStatus('mandatory')
a3filterPolicyPorts2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyPorts2.setStatus('mandatory')
a3filterPolicyPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterPolicyPackets.setStatus('mandatory')
a3filterPolicyBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3filterPolicyBytes.setStatus('mandatory')
a3filterPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyStatus.setStatus('mandatory')
a3filterPolicyX25ProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3filterPolicyX25ProfId.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-FILTER-R5-MIB", a3filterUserMaskLocLength=a3filterUserMaskLocLength, a3filterPolicyAction=a3filterPolicyAction, a3filterIpxSelect=a3filterIpxSelect, a3filterUserMaskStatus=a3filterUserMaskStatus, a3filterPolicyName=a3filterPolicyName, a3filterBuiltInMaskTable=a3filterBuiltInMaskTable, a3filterUserGrpName=a3filterUserGrpName, a3filterPolicyEntry=a3filterPolicyEntry, a3filterDefaultAction=a3filterDefaultAction, a3filterUserMaskOperand=a3filterUserMaskOperand, a3filterPolicyX25ProfId=a3filterPolicyX25ProfId, a3filterUserMaskMatchValue1=a3filterUserMaskMatchValue1, a3filterUserMaskMatchValue2=a3filterUserMaskMatchValue2, a3filterUserMaskName=a3filterUserMaskName, a3filterPolicyTable=a3filterPolicyTable, a3filterPolicyContext=a3filterPolicyContext, a3filterUserGrpIndex=a3filterUserGrpIndex, a3Com=a3Com, a3filterUserGrpTable=a3filterUserGrpTable, a3filterUserGrpAddrIndex=a3filterUserGrpAddrIndex, RowStatus=RowStatus, a3filterIpSelect=a3filterIpSelect, a3filterUserMaskTable=a3filterUserMaskTable, a3filterUserMaskIndex=a3filterUserMaskIndex, a3filterUserMaskMatchType=a3filterUserMaskMatchType, a3filterPolicyMask2=a3filterPolicyMask2, a3filterPolicyPackets=a3filterPolicyPackets, a3filterUserGrpAddrTable=a3filterUserGrpAddrTable, a3filterBridgeSelect=a3filterBridgeSelect, a3filterPolicyStatus=a3filterPolicyStatus, a3filterAppleTalkSelect=a3filterAppleTalkSelect, a3filterBuiltInMaskName=a3filterBuiltInMaskName, a3filterPolicyIndex=a3filterPolicyIndex, a3filterUserMaskLocOffset=a3filterUserMaskLocOffset, a3filterPolicyMask1=a3filterPolicyMask1, a3filterControl=a3filterControl, a3ComFilterCtl=a3ComFilterCtl, a3filterUserGrpAddrEntry=a3filterUserGrpAddrEntry, a3filterUserMaskLocField=a3filterUserMaskLocField, a3filterBuiltInMaskEntry=a3filterBuiltInMaskEntry, a3filterUserGrpAddress=a3filterUserGrpAddress, a3filterPolicyBytes=a3filterPolicyBytes, a3filterUserMaskMatchBits=a3filterUserMaskMatchBits, a3filterUserGrpEntry=a3filterUserGrpEntry, a3filterPolicyPorts2=a3filterPolicyPorts2, a3filterPolicyMask3=a3filterPolicyMask3, a3filterDecSelect=a3filterDecSelect, a3filterUserGrpStatus=a3filterUserGrpStatus, a3filterUserMaskOperator=a3filterUserMaskOperator, a3filterPolicyPorts1=a3filterPolicyPorts1, a3filterBuiltInMaskIndex=a3filterBuiltInMaskIndex, a3filterUserGrpAddrStatus=a3filterUserGrpAddrStatus, a3filterPolicyMask4=a3filterPolicyMask4, a3filterBuiltInMaskFieldValue=a3filterBuiltInMaskFieldValue, a3filterUserMaskComparison=a3filterUserMaskComparison, a3ComFilter=a3ComFilter, a3filterUserMaskLocType=a3filterUserMaskLocType, brouterMIB=brouterMIB, a3filterUserMaskEntry=a3filterUserMaskEntry)
