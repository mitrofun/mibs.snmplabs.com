#
# PySNMP MIB module CABH-CTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CABH-CTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
clabProjCableHome, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjCableHome")
InetAddressType, InetAddressIPv6, InetAddress, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressIPv6", "InetAddress", "InetAddressIPv4")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, ObjectIdentity, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, Counter32, Unsigned32, Counter64, Integer32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "Counter32", "Unsigned32", "Counter64", "Integer32", "Gauge32", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cabhCtpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5))
if mibBuilder.loadTexts: cabhCtpMib.setLastUpdated('200304110000Z')
if mibBuilder.loadTexts: cabhCtpMib.setOrganization('CableLabs Broadband Access Department')
cabhCtpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1))
cabhCtpBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 1))
cabhCtpConnSpeed = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2))
cabhCtpPing = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3))
cabhCtpSetToFactory = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpSetToFactory.setStatus('current')
cabhCtpConnSrcIpType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 1), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnSrcIpType.setStatus('current')
cabhCtpConnSrcIp = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 2), InetAddress().clone(hexValue="c0a80001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnSrcIp.setStatus('current')
cabhCtpConnDestIpType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnDestIpType.setStatus('current')
cabhCtpConnDestIp = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnDestIp.setStatus('current')
cabhCtpConnProto = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2))).clone('udp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnProto.setStatus('current')
cabhCtpConnNumPkts = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnNumPkts.setStatus('current')
cabhCtpConnPktSize = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1518)).clone(1518)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnPktSize.setStatus('current')
cabhCtpConnTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000)).clone(30000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnTimeOut.setStatus('current')
cabhCtpConnControl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("abort", 2))).clone('abort')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpConnControl.setStatus('current')
cabhCtpConnStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notRun", 1), ("running", 2), ("complete", 3), ("aborted", 4), ("timedOut", 5))).clone('notRun')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpConnStatus.setStatus('current')
cabhCtpConnPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpConnPktsSent.setStatus('current')
cabhCtpConnPktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpConnPktsRecv.setStatus('current')
cabhCtpConnRTT = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('millisec').setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpConnRTT.setStatus('current')
cabhCtpConnThroughput = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpConnThroughput.setStatus('current')
cabhCtpPingSrcIpType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 1), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingSrcIpType.setStatus('current')
cabhCtpPingSrcIp = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 2), InetAddress().clone(hexValue="c0a80001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingSrcIp.setStatus('current')
cabhCtpPingDestIpType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingDestIpType.setStatus('current')
cabhCtpPingDestIp = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingDestIp.setStatus('current')
cabhCtpPingNumPkts = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingNumPkts.setStatus('current')
cabhCtpPingPktSize = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1518)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingPktSize.setStatus('current')
cabhCtpPingTimeBetween = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingTimeBetween.setStatus('current')
cabhCtpPingTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingTimeOut.setStatus('current')
cabhCtpPingControl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("abort", 2))).clone('abort')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCtpPingControl.setStatus('current')
cabhCtpPingStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notRun", 1), ("running", 2), ("complete", 3), ("aborted", 4), ("timedOut", 5))).clone('notRun')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingStatus.setStatus('current')
cabhCtpPingNumSent = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingNumSent.setStatus('current')
cabhCtpPingNumRecv = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingNumRecv.setStatus('current')
cabhCtpPingAvgRTT = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('millisec').setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingAvgRTT.setStatus('current')
cabhCtpPingMaxRTT = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('millisec').setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingMaxRTT.setStatus('current')
cabhCtpPingMinRTT = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('millisec').setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingMinRTT.setStatus('current')
cabhCtpPingNumIcmpError = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingNumIcmpError.setStatus('current')
cabhCtpPingIcmpError = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCtpPingIcmpError.setStatus('current')
cabhCtpNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 2, 0))
cabhCtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3))
cabhCtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 1))
cabhCtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 2))
cabhCtpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 1, 3)).setObjects(("CABH-CTP-MIB", "cabhCtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhCtpBasicCompliance = cabhCtpBasicCompliance.setStatus('current')
cabhCtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 2, 1)).setObjects(("CABH-CTP-MIB", "cabhCtpSetToFactory"), ("CABH-CTP-MIB", "cabhCtpConnSrcIpType"), ("CABH-CTP-MIB", "cabhCtpConnSrcIp"), ("CABH-CTP-MIB", "cabhCtpConnDestIpType"), ("CABH-CTP-MIB", "cabhCtpConnDestIp"), ("CABH-CTP-MIB", "cabhCtpConnProto"), ("CABH-CTP-MIB", "cabhCtpConnNumPkts"), ("CABH-CTP-MIB", "cabhCtpConnPktSize"), ("CABH-CTP-MIB", "cabhCtpConnTimeOut"), ("CABH-CTP-MIB", "cabhCtpConnControl"), ("CABH-CTP-MIB", "cabhCtpConnStatus"), ("CABH-CTP-MIB", "cabhCtpConnPktsSent"), ("CABH-CTP-MIB", "cabhCtpConnPktsRecv"), ("CABH-CTP-MIB", "cabhCtpConnRTT"), ("CABH-CTP-MIB", "cabhCtpConnThroughput"), ("CABH-CTP-MIB", "cabhCtpPingSrcIpType"), ("CABH-CTP-MIB", "cabhCtpPingSrcIp"), ("CABH-CTP-MIB", "cabhCtpPingDestIpType"), ("CABH-CTP-MIB", "cabhCtpPingDestIp"), ("CABH-CTP-MIB", "cabhCtpPingNumPkts"), ("CABH-CTP-MIB", "cabhCtpPingPktSize"), ("CABH-CTP-MIB", "cabhCtpPingTimeBetween"), ("CABH-CTP-MIB", "cabhCtpPingTimeOut"), ("CABH-CTP-MIB", "cabhCtpPingControl"), ("CABH-CTP-MIB", "cabhCtpPingStatus"), ("CABH-CTP-MIB", "cabhCtpPingNumSent"), ("CABH-CTP-MIB", "cabhCtpPingNumRecv"), ("CABH-CTP-MIB", "cabhCtpPingAvgRTT"), ("CABH-CTP-MIB", "cabhCtpPingMinRTT"), ("CABH-CTP-MIB", "cabhCtpPingMaxRTT"), ("CABH-CTP-MIB", "cabhCtpPingNumIcmpError"), ("CABH-CTP-MIB", "cabhCtpPingIcmpError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhCtpGroup = cabhCtpGroup.setStatus('current')
mibBuilder.exportSymbols("CABH-CTP-MIB", cabhCtpConnPktSize=cabhCtpConnPktSize, cabhCtpConnControl=cabhCtpConnControl, cabhCtpPingTimeOut=cabhCtpPingTimeOut, cabhCtpPingSrcIp=cabhCtpPingSrcIp, cabhCtpConnRTT=cabhCtpConnRTT, cabhCtpConnDestIpType=cabhCtpConnDestIpType, cabhCtpConnPktsSent=cabhCtpConnPktsSent, cabhCtpGroup=cabhCtpGroup, cabhCtpPingControl=cabhCtpPingControl, cabhCtpPing=cabhCtpPing, cabhCtpConnTimeOut=cabhCtpConnTimeOut, cabhCtpConnProto=cabhCtpConnProto, cabhCtpPingPktSize=cabhCtpPingPktSize, cabhCtpConnSrcIp=cabhCtpConnSrcIp, cabhCtpPingNumSent=cabhCtpPingNumSent, cabhCtpConnNumPkts=cabhCtpConnNumPkts, cabhCtpConnPktsRecv=cabhCtpConnPktsRecv, cabhCtpPingTimeBetween=cabhCtpPingTimeBetween, cabhCtpPingMaxRTT=cabhCtpPingMaxRTT, cabhCtpPingAvgRTT=cabhCtpPingAvgRTT, cabhCtpPingNumIcmpError=cabhCtpPingNumIcmpError, cabhCtpPingDestIp=cabhCtpPingDestIp, cabhCtpPingMinRTT=cabhCtpPingMinRTT, cabhCtpObjects=cabhCtpObjects, cabhCtpConformance=cabhCtpConformance, cabhCtpPingIcmpError=cabhCtpPingIcmpError, cabhCtpMib=cabhCtpMib, cabhCtpBase=cabhCtpBase, cabhCtpPingDestIpType=cabhCtpPingDestIpType, cabhCtpConnSrcIpType=cabhCtpConnSrcIpType, cabhCtpPingNumPkts=cabhCtpPingNumPkts, cabhCtpPingSrcIpType=cabhCtpPingSrcIpType, cabhCtpBasicCompliance=cabhCtpBasicCompliance, PYSNMP_MODULE_ID=cabhCtpMib, cabhCtpSetToFactory=cabhCtpSetToFactory, cabhCtpConnSpeed=cabhCtpConnSpeed, cabhCtpConnStatus=cabhCtpConnStatus, cabhCtpPingStatus=cabhCtpPingStatus, cabhCtpConnDestIp=cabhCtpConnDestIp, cabhCtpPingNumRecv=cabhCtpPingNumRecv, cabhCtpNotification=cabhCtpNotification, cabhCtpConnThroughput=cabhCtpConnThroughput, cabhCtpCompliances=cabhCtpCompliances, cabhCtpGroups=cabhCtpGroups)
