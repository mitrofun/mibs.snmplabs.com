#
# PySNMP MIB module ITOUCH-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-IPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, ModuleIdentity, NotificationType, Gauge32, Integer32, IpAddress, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "ModuleIdentity", "NotificationType", "Gauge32", "Integer32", "IpAddress", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15))
xIpxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 1))
xIpxIf = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 2))
xIpxNetbios = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 3))
xIpxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 4))
xIpxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 5))
xIpxFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 6))
xIpxPrinter = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 8))
ipxRouting = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRouting.setStatus('mandatory')
ipxInternalNetwork = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxInternalNetwork.setStatus('mandatory')
ipxIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 2, 1), )
if mibBuilder.loadTexts: ipxIfTable.setStatus('mandatory')
ipxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxIfIndex"))
if mibBuilder.loadTexts: ipxIfEntry.setStatus('mandatory')
ipxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfIndex.setStatus('mandatory')
ipxIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfState.setStatus('mandatory')
ipxIfNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetwork.setStatus('mandatory')
ipxIfFrameStyle = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8023", 2), ("ieee8022", 3), ("ieee802Snap", 4))).clone('ieee8023')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfFrameStyle.setStatus('mandatory')
ipxIfFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesIn.setStatus('mandatory')
ipxIfFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesOut.setStatus('mandatory')
ipxIfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfErrors.setStatus('mandatory')
ipxIfTransitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfTransitDelay.setStatus('mandatory')
ipxIfTransitDelayActual = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfTransitDelayActual.setStatus('mandatory')
ipxIfProtocolPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5))).clone(namedValues=NamedValues(("low", 1), ("medium", 3), ("high", 5))).clone('medium')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfProtocolPriority.setStatus('mandatory')
ipxIfWatchdogSpoof = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfWatchdogSpoof.setStatus('mandatory')
ipxIfStatusNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfStatusNetwork.setStatus('mandatory')
ipxNetbiosHopLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxNetbiosHopLimit.setStatus('mandatory')
ipxNetbiosIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 3, 2), )
if mibBuilder.loadTexts: ipxNetbiosIfTable.setStatus('mandatory')
ipxNetbiosIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxNetbiosIfIndex"))
if mibBuilder.loadTexts: ipxNetbiosIfEntry.setStatus('mandatory')
ipxNetbiosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxNetbiosIfIndex.setStatus('mandatory')
ipxIfNetbiosForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetbiosForwarding.setStatus('mandatory')
ipxIfNetbiosIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosIn.setStatus('mandatory')
ipxIfNetbiosOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosOut.setStatus('mandatory')
ipxRipIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 1), )
if mibBuilder.loadTexts: ipxRipIfTable.setStatus('mandatory')
ipxRipIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxRipIfIndex"))
if mibBuilder.loadTexts: ipxRipIfEntry.setStatus('mandatory')
ipxRipIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipIfIndex.setStatus('mandatory')
ipxIfRipBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("propUpdateOnly", 3), ("demandCircuit", 4))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcst.setStatus('mandatory')
ipxIfRipBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstDiscardTimeout.setStatus('mandatory')
ipxIfRipBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstTimer.setStatus('mandatory')
ipxIfRipIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipIn.setStatus('mandatory')
ipxIfRipOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipOut.setStatus('mandatory')
ipxIfRipAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipAgedOut.setStatus('mandatory')
ipxRipTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 2), )
if mibBuilder.loadTexts: ipxRipTable.setStatus('mandatory')
ipxRipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxRipNetwork"))
if mibBuilder.loadTexts: ipxRipEntry.setStatus('mandatory')
ipxRipNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipNetwork.setStatus('mandatory')
ipxRipRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRouter.setStatus('mandatory')
ipxRipInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipInterface.setStatus('mandatory')
ipxRipHops = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipHops.setStatus('mandatory')
ipxRipTransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipTransTime.setStatus('mandatory')
ipxRipAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipAge.setStatus('mandatory')
ipxRipRtTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 3), )
if mibBuilder.loadTexts: ipxRipRtTable.setStatus('mandatory')
ipxRipRtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxRipRtNetwork"), (0, "ITOUCH-IPX-MIB", "ipxRipRtInterface"), (0, "ITOUCH-IPX-MIB", "ipxRipRtOrigin"), (0, "ITOUCH-IPX-MIB", "ipxRipRtRouter"))
if mibBuilder.loadTexts: ipxRipRtEntry.setStatus('mandatory')
ipxRipRtNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRtNetwork.setStatus('mandatory')
ipxRipRtRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRtRouter.setStatus('mandatory')
ipxRipRtInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRtInterface.setStatus('mandatory')
ipxRipRtHops = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRipRtHops.setStatus('mandatory')
ipxRipRtTransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRipRtTransTime.setStatus('mandatory')
ipxRipRtOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ripLearned", 1), ("static", 2), ("nlspLearned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRtOrigin.setStatus('mandatory')
ipxRipRtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRipRtRowStatus.setStatus('mandatory')
ipxSapIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 1), )
if mibBuilder.loadTexts: ipxSapIfTable.setStatus('mandatory')
ipxSapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxSapIfIndex"))
if mibBuilder.loadTexts: ipxSapIfEntry.setStatus('mandatory')
ipxSapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapIfIndex.setStatus('mandatory')
ipxIfSapBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("propUpdateOnly", 3), ("demandCircuit", 4))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcst.setStatus('mandatory')
ipxIfSapBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstDiscardTimeout.setStatus('mandatory')
ipxIfSapBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstTimer.setStatus('mandatory')
ipxIfSapIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapIn.setStatus('mandatory')
ipxIfSapOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapOut.setStatus('mandatory')
ipxIfSapAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapAgedOut.setStatus('mandatory')
ipxSapTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 2), )
if mibBuilder.loadTexts: ipxSapTable.setStatus('mandatory')
ipxSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxSapName"), (0, "ITOUCH-IPX-MIB", "ipxSapType"))
if mibBuilder.loadTexts: ipxSapEntry.setStatus('mandatory')
ipxSapName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(48, 48)).setFixedLength(48)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapName.setStatus('mandatory')
ipxSapNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapNetwork.setStatus('mandatory')
ipxSapHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapHost.setStatus('mandatory')
ipxSapSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSocket.setStatus('mandatory')
ipxSapInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapInterface.setStatus('mandatory')
ipxSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("user", 1), ("userGroup", 2), ("printQueue", 3), ("novellFileServer", 4), ("jobServer", 5), ("gateway1", 6), ("printServer", 7), ("archiveQueue", 8), ("archiveServer", 9), ("jobQueue", 10), ("administration", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapType.setStatus('mandatory')
ipxSapAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapAge.setStatus('mandatory')
ipxSapSvTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 3), )
if mibBuilder.loadTexts: ipxSapSvTable.setStatus('mandatory')
ipxSapSvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxSapSvName"), (0, "ITOUCH-IPX-MIB", "ipxSapSvType"), (0, "ITOUCH-IPX-MIB", "ipxSapSvOrigin"), (0, "ITOUCH-IPX-MIB", "ipxSapSvNetwork"), (0, "ITOUCH-IPX-MIB", "ipxSapSvSocket"), (0, "ITOUCH-IPX-MIB", "ipxSapSvHost"))
if mibBuilder.loadTexts: ipxSapSvEntry.setStatus('mandatory')
ipxSapSvName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvName.setStatus('mandatory')
ipxSapSvNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvNetwork.setStatus('mandatory')
ipxSapSvHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvHost.setStatus('mandatory')
ipxSapSvSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvSocket.setStatus('mandatory')
ipxSapSvInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvInterface.setStatus('mandatory')
ipxSapSvOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipxSapLearned", 1), ("ipxStatic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvOrigin.setStatus('mandatory')
ipxSapSvType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("user", 1), ("userGroup", 2), ("printQueue", 3), ("novellFileServer", 4), ("jobServer", 5), ("gateway1", 6), ("printServer", 7), ("archiveQueue", 8), ("archiveServer", 9), ("jobQueue", 10), ("administration", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvType.setStatus('mandatory')
ipxSapSvHops = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxSapSvHops.setStatus('mandatory')
ipxSapSvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxSapSvRowStatus.setStatus('mandatory')
ipxSapSvAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSvAge.setStatus('mandatory')
ipxIfFilterTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 6, 1), )
if mibBuilder.loadTexts: ipxIfFilterTable.setStatus('mandatory')
ipxIfFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxIfIndex"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterDestNetwork"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterDestNode"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterSourceNetwork"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterSourceNode"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterPacketType"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusDestNetworkAll"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusDestNodeAll"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusSourceNetworkAll"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusSourceNodeAll"), (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusPacketTypeAll"))
if mibBuilder.loadTexts: ipxIfFilterEntry.setStatus('mandatory')
ipxIfFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterIndex.setStatus('mandatory')
ipxIfFilterDestNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterDestNetwork.setStatus('mandatory')
ipxIfFilterDestNode = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterDestNode.setStatus('mandatory')
ipxIfFilterSourceNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterSourceNetwork.setStatus('mandatory')
ipxIfFilterSourceNode = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterSourceNode.setStatus('mandatory')
ipxIfFilterPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterPacketType.setStatus('mandatory')
ipxIfFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfFilterAction.setStatus('mandatory')
ipxIfFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfFilterRowStatus.setStatus('mandatory')
ipxIfFilterStatusDestNetworkAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterStatusDestNetworkAll.setStatus('mandatory')
ipxIfFilterStatusDestNodeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterStatusDestNodeAll.setStatus('mandatory')
ipxIfFilterStatusSourceNetworkAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterStatusSourceNetworkAll.setStatus('mandatory')
ipxIfFilterStatusSourceNodeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterStatusSourceNodeAll.setStatus('mandatory')
ipxIfFilterStatusPacketTypeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFilterStatusPacketTypeAll.setStatus('mandatory')
ipxIfRipFilterTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 6, 2), )
if mibBuilder.loadTexts: ipxIfRipFilterTable.setStatus('mandatory')
ipxIfRipFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxIfIndex"), (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterType"), (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterNetwork"), (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterNetworkAll"), (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterHost"))
if mibBuilder.loadTexts: ipxIfRipFilterEntry.setStatus('mandatory')
ipxIfRipFilterNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipFilterNetwork.setStatus('mandatory')
ipxIfRipFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("import", 1), ("export", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipFilterType.setStatus('mandatory')
ipxIfRipFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allow", 1), ("deny", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipFilterAction.setStatus('mandatory')
ipxIfRipFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipFilterRowStatus.setStatus('mandatory')
ipxIfRipFilterNetworkAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipFilterNetworkAll.setStatus('mandatory')
ipxIfRipFilterHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipFilterHost.setStatus('mandatory')
ipxIfSapFilterTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 6, 3), )
if mibBuilder.loadTexts: ipxIfSapFilterTable.setStatus('mandatory')
ipxIfSapFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxIfIndex"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterType"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterName"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterServiceType"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterServiceTypeAll"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterNetwork"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterNetworkAll"), (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterHost"))
if mibBuilder.loadTexts: ipxIfSapFilterEntry.setStatus('mandatory')
ipxIfSapFilterNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterNetwork.setStatus('mandatory')
ipxIfSapFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("import", 1), ("export", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterType.setStatus('mandatory')
ipxIfSapFilterServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterServiceType.setStatus('mandatory')
ipxIfSapFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allow", 1), ("deny", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapFilterAction.setStatus('mandatory')
ipxIfSapFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapFilterRowStatus.setStatus('mandatory')
ipxIfSapFilterNetworkAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterNetworkAll.setStatus('mandatory')
ipxIfSapFilterServiceTypeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterServiceTypeAll.setStatus('mandatory')
ipxIfSapFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterName.setStatus('mandatory')
ipxIfSapFilterHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapFilterHost.setStatus('mandatory')
ipxPrinterPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 8, 1), )
if mibBuilder.loadTexts: ipxPrinterPortTable.setStatus('mandatory')
ipxPrinterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1), ).setIndexNames((0, "ITOUCH-IPX-MIB", "ipxPrinterPortIndex"))
if mibBuilder.loadTexts: ipxPrinterPortEntry.setStatus('mandatory')
ipxPrinterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxPrinterPortIndex.setStatus('mandatory')
ipxPrinterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterPortStatus.setStatus('mandatory')
ipxPrinterPortServer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterPortServer.setStatus('mandatory')
ipxPrinterPortPrinter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterPortPrinter.setStatus('mandatory')
ipxTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 300)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxTimeout.setStatus('mandatory')
ipxPrinterEthernet = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterEthernet.setStatus('mandatory')
ipxPrinterMac = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterMac.setStatus('mandatory')
ipxPrinterMac802_2 = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 8, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setLabel("ipxPrinterMac802-2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterMac802_2.setStatus('mandatory')
ipxPrinterMac802_2_Snap = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setLabel("ipxPrinterMac802-2-Snap").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxPrinterMac802_2_Snap.setStatus('mandatory')
mibBuilder.exportSymbols("ITOUCH-IPX-MIB", ipxIfProtocolPriority=ipxIfProtocolPriority, ipxSapHost=ipxSapHost, ipxSapSvEntry=ipxSapSvEntry, ipxRipAge=ipxRipAge, ipxIfRipFilterNetworkAll=ipxIfRipFilterNetworkAll, ipxSapNetwork=ipxSapNetwork, xIpxIf=xIpxIf, ipxIfNetwork=ipxIfNetwork, ipxIfFilterEntry=ipxIfFilterEntry, ipxSapSvAge=ipxSapSvAge, ipxRipTable=ipxRipTable, ipxIfTransitDelay=ipxIfTransitDelay, ipxIfIndex=ipxIfIndex, ipxIfRipBcst=ipxIfRipBcst, xIpx=xIpx, xIpxRip=xIpxRip, ipxRipRtHops=ipxRipRtHops, ipxIfSapIn=ipxIfSapIn, ipxSapSocket=ipxSapSocket, ipxRouting=ipxRouting, ipxPrinterMac802_2_Snap=ipxPrinterMac802_2_Snap, ipxIfFramesOut=ipxIfFramesOut, ipxSapSvHost=ipxSapSvHost, ipxPrinterEthernet=ipxPrinterEthernet, ipxSapSvType=ipxSapSvType, ipxIfRipBcstDiscardTimeout=ipxIfRipBcstDiscardTimeout, ipxIfStatusNetwork=ipxIfStatusNetwork, ipxSapTable=ipxSapTable, ipxSapType=ipxSapType, ipxIfRipFilterRowStatus=ipxIfRipFilterRowStatus, ipxPrinterPortStatus=ipxPrinterPortStatus, ipxSapAge=ipxSapAge, ipxIfSapAgedOut=ipxIfSapAgedOut, ipxRipRtTransTime=ipxRipRtTransTime, ipxIfFilterDestNetwork=ipxIfFilterDestNetwork, ipxNetbiosIfIndex=ipxNetbiosIfIndex, ipxRipInterface=ipxRipInterface, ipxIfSapFilterRowStatus=ipxIfSapFilterRowStatus, ipxIfSapFilterNetworkAll=ipxIfSapFilterNetworkAll, ipxIfFilterStatusSourceNetworkAll=ipxIfFilterStatusSourceNetworkAll, ipxIfFilterStatusSourceNodeAll=ipxIfFilterStatusSourceNodeAll, ipxIfSapOut=ipxIfSapOut, ipxIfNetbiosOut=ipxIfNetbiosOut, ipxRipRtEntry=ipxRipRtEntry, ipxIfFilterStatusPacketTypeAll=ipxIfFilterStatusPacketTypeAll, ipxRipIfEntry=ipxRipIfEntry, ipxRipRtInterface=ipxRipRtInterface, ipxIfFilterSourceNode=ipxIfFilterSourceNode, ipxIfSapFilterName=ipxIfSapFilterName, ipxRipIfTable=ipxRipIfTable, ipxSapSvInterface=ipxSapSvInterface, ipxRipIfIndex=ipxRipIfIndex, ipxIfSapBcstDiscardTimeout=ipxIfSapBcstDiscardTimeout, ipxNetbiosIfEntry=ipxNetbiosIfEntry, xIpxNetbios=xIpxNetbios, ipxRipHops=ipxRipHops, ipxPrinterMac802_2=ipxPrinterMac802_2, ipxNetbiosIfTable=ipxNetbiosIfTable, ipxIfState=ipxIfState, ipxIfFilterDestNode=ipxIfFilterDestNode, ipxRipRtRowStatus=ipxRipRtRowStatus, ipxIfNetbiosForwarding=ipxIfNetbiosForwarding, ipxIfRipAgedOut=ipxIfRipAgedOut, ipxRipEntry=ipxRipEntry, ipxPrinterPortServer=ipxPrinterPortServer, xIpxPrinter=xIpxPrinter, ipxIfRipFilterEntry=ipxIfRipFilterEntry, ipxIfTable=ipxIfTable, ipxIfSapFilterType=ipxIfSapFilterType, ipxIfFilterRowStatus=ipxIfFilterRowStatus, ipxPrinterPortIndex=ipxPrinterPortIndex, ipxTimeout=ipxTimeout, ipxRipTransTime=ipxRipTransTime, ipxSapIfTable=ipxSapIfTable, ipxRipRtRouter=ipxRipRtRouter, xIpxFilter=xIpxFilter, ipxIfRipBcstTimer=ipxIfRipBcstTimer, ipxSapSvHops=ipxSapSvHops, ipxIfRipFilterTable=ipxIfRipFilterTable, ipxIfRipIn=ipxIfRipIn, ipxInternalNetwork=ipxInternalNetwork, ipxIfTransitDelayActual=ipxIfTransitDelayActual, ipxSapSvTable=ipxSapSvTable, ipxRipRtTable=ipxRipRtTable, ipxIfWatchdogSpoof=ipxIfWatchdogSpoof, ipxIfFilterStatusDestNodeAll=ipxIfFilterStatusDestNodeAll, ipxIfSapFilterNetwork=ipxIfSapFilterNetwork, ipxSapSvOrigin=ipxSapSvOrigin, ipxIfRipFilterAction=ipxIfRipFilterAction, ipxSapSvSocket=ipxSapSvSocket, ipxPrinterMac=ipxPrinterMac, ipxIfSapFilterServiceTypeAll=ipxIfSapFilterServiceTypeAll, ipxSapSvNetwork=ipxSapSvNetwork, ipxIfFilterAction=ipxIfFilterAction, ipxIfSapFilterTable=ipxIfSapFilterTable, ipxIfSapBcst=ipxIfSapBcst, ipxNetbiosHopLimit=ipxNetbiosHopLimit, ipxPrinterPortPrinter=ipxPrinterPortPrinter, ipxIfFilterSourceNetwork=ipxIfFilterSourceNetwork, ipxSapSvName=ipxSapSvName, ipxIfNetbiosIn=ipxIfNetbiosIn, ipxPrinterPortEntry=ipxPrinterPortEntry, xIpxSystem=xIpxSystem, ipxIfRipFilterNetwork=ipxIfRipFilterNetwork, ipxPrinterPortTable=ipxPrinterPortTable, ipxIfFilterIndex=ipxIfFilterIndex, ipxSapEntry=ipxSapEntry, ipxIfSapFilterAction=ipxIfSapFilterAction, ipxSapInterface=ipxSapInterface, ipxIfEntry=ipxIfEntry, ipxRipRtNetwork=ipxRipRtNetwork, ipxIfRipOut=ipxIfRipOut, ipxSapName=ipxSapName, ipxIfSapFilterEntry=ipxIfSapFilterEntry, ipxRipNetwork=ipxRipNetwork, ipxIfFilterStatusDestNetworkAll=ipxIfFilterStatusDestNetworkAll, ipxRipRouter=ipxRipRouter, ipxIfFilterPacketType=ipxIfFilterPacketType, ipxSapIfEntry=ipxSapIfEntry, ipxIfFramesIn=ipxIfFramesIn, ipxIfRipFilterType=ipxIfRipFilterType, ipxSapIfIndex=ipxSapIfIndex, ipxIfRipFilterHost=ipxIfRipFilterHost, ipxSapSvRowStatus=ipxSapSvRowStatus, ipxIfFrameStyle=ipxIfFrameStyle, ipxRipRtOrigin=ipxRipRtOrigin, ipxIfSapBcstTimer=ipxIfSapBcstTimer, ipxIfErrors=ipxIfErrors, ipxIfFilterTable=ipxIfFilterTable, ipxIfSapFilterHost=ipxIfSapFilterHost, ipxIfSapFilterServiceType=ipxIfSapFilterServiceType, xIpxSap=xIpxSap)
