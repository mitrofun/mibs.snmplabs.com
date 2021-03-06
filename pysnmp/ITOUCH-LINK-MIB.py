#
# PySNMP MIB module ITOUCH-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-LINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Gauge32, Counter32, Bits, Counter64, TimeTicks, NotificationType, ModuleIdentity, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Gauge32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xLink = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 24))
xLinkBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 24, 1))
xWan = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 24, 3))
linkTable = MibTable((1, 3, 6, 1, 4, 1, 33, 24, 1, 1), )
if mibBuilder.loadTexts: linkTable.setStatus('mandatory')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkEntry.setStatus('mandatory')
linkNoBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkNoBuffers.setStatus('mandatory')
linkDelayExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDelayExceeded.setStatus('mandatory')
linkOutputQFull = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkOutputQFull.setStatus('mandatory')
linkDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDownTime.setStatus('mandatory')
linkDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDownCount.setStatus('mandatory')
linkDownLastStart = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDownLastStart.setStatus('mandatory')
linkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7, 128, 129, 130, 131, 132, 133, 138, 139, 140, 141, 143, 145, 146))).clone(namedValues=NamedValues(("running1", 7), ("initWaitDsr", 128), ("initWait", 129), ("running2", 130), ("purgeWait", 131), ("down", 132), ("purging", 133), ("loop", 138), ("testSend", 139), ("testReceive", 140), ("testLoop", 141), ("speedChange", 143), ("disabled", 145), ("badQuality", 146)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkStatus.setStatus('mandatory')
linkLostBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkLostBuffers.setStatus('mandatory')
linkResourceTable = MibTable((1, 3, 6, 1, 4, 1, 33, 24, 1, 2), )
if mibBuilder.loadTexts: linkResourceTable.setStatus('mandatory')
linkResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1), ).setIndexNames((0, "ITOUCH-LINK-MIB", "linkResourceType"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkResourceEntry.setStatus('mandatory')
linkResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("utilization", 1), ("outputQueue", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkResourceType.setStatus('mandatory')
linkResourceCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkResourceCurrent.setStatus('mandatory')
linkResourceHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkResourceHigh.setStatus('mandatory')
linkResourceAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkResourceAverage.setStatus('mandatory')
wanTable = MibTable((1, 3, 6, 1, 4, 1, 33, 24, 3, 1), )
if mibBuilder.loadTexts: wanTable.setStatus('mandatory')
wanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: wanEntry.setStatus('mandatory')
wanProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("xcp", 2), ("fr", 3), ("ppp", 4), ("frlmi", 5), ("fransi", 6), ("frdcelmi", 7), ("frdceansi", 8), ("x25", 9))).clone('xcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanProtocol.setStatus('mandatory')
wanCompressionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 256))).clone(namedValues=NamedValues(("noCompression", 1), ("compress", 2), ("auto", 256))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanCompressionAdminStatus.setStatus('mandatory')
wanMaxForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanMaxForwardDelay.setStatus('mandatory')
wanMaxMultiForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000)).clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanMaxMultiForwardDelay.setStatus('mandatory')
wanAdminSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanAdminSpeed.setStatus('mandatory')
wanCompressionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notCompressing", 1), ("compressing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanCompressionOperStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ITOUCH-LINK-MIB", linkDownCount=linkDownCount, linkResourceEntry=linkResourceEntry, wanMaxForwardDelay=wanMaxForwardDelay, linkResourceType=linkResourceType, linkResourceCurrent=linkResourceCurrent, wanCompressionAdminStatus=wanCompressionAdminStatus, linkStatus=linkStatus, linkResourceHigh=linkResourceHigh, xLink=xLink, linkNoBuffers=linkNoBuffers, wanMaxMultiForwardDelay=wanMaxMultiForwardDelay, linkDownTime=linkDownTime, linkLostBuffers=linkLostBuffers, linkDelayExceeded=linkDelayExceeded, linkResourceTable=linkResourceTable, wanCompressionOperStatus=wanCompressionOperStatus, xWan=xWan, linkDownLastStart=linkDownLastStart, wanProtocol=wanProtocol, xLinkBasic=xLinkBasic, linkOutputQFull=linkOutputQFull, wanAdminSpeed=wanAdminSpeed, linkTable=linkTable, wanTable=wanTable, linkResourceAverage=linkResourceAverage, wanEntry=wanEntry, linkEntry=linkEntry)
