#
# PySNMP MIB module Fore-frs-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-frs-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
frameInternetworking, = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Bits, IpAddress, Counter64, Gauge32, Integer32, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Bits", "IpAddress", "Counter64", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreFrameRelayModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 1))
if mibBuilder.loadTexts: foreFrameRelayModule.setLastUpdated('9705011044-0400')
if mibBuilder.loadTexts: foreFrameRelayModule.setOrganization('FORE')
frextDlcmiTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1), )
if mibBuilder.loadTexts: frextDlcmiTable.setStatus('current')
frextDlcmiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1), ).setIndexNames((0, "Fore-frs-MIB", "frextDlcmiServiceIfIndex"))
if mibBuilder.loadTexts: frextDlcmiEntry.setStatus('current')
frextDlcmiServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiServiceIfIndex.setStatus('current')
frextDlcmiProfileLmiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiProfileLmiIndex.setStatus('current')
frextDlcmiProfileServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiProfileServiceIndex.setStatus('current')
frextDlcmiStatsMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiStatsMonitor.setStatus('current')
frextDlcmiStatsEnabledTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiStatsEnabledTimeStamp.setStatus('current')
frextDlcmiLmiDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiDlci.setStatus('current')
frextDlcmiLmiFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiLmiFlowControl.setStatus('current')
frextDlcmiRAControl = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiRAControl.setStatus('current')
frextDlcmiLmiBandwidthControl = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextDlcmiLmiBandwidthControl.setStatus('current')
frextDlcmiRxAbortedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRxAbortedFrames.setStatus('current')
frextDlcmiRcvCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRcvCrcErrors.setStatus('current')
frextDlcmiRcvShortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRcvShortFrames.setStatus('current')
frextDlcmiRcvLongFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRcvLongFrames.setStatus('current')
frextDlcmiRcvInvalidDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRcvInvalidDLCI.setStatus('current')
frextDlcmiRcvUnknownErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiRcvUnknownErrs.setStatus('current')
frextDlcmiLmiTxStatusResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiTxStatusResponses.setStatus('current')
frextDlcmiLmiTxFullStatusResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiTxFullStatusResponses.setStatus('current')
frextDlcmiLmiTxStatusEnquiries = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiTxStatusEnquiries.setStatus('current')
frextDlcmiLmiTxFullStatusEnquiries = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiTxFullStatusEnquiries.setStatus('current')
frextDlcmiLmiRxStatusResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiRxStatusResponses.setStatus('current')
frextDlcmiLmiRxFullStatusResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiRxFullStatusResponses.setStatus('current')
frextDlcmiLmiRxStatusEnquiries = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiRxStatusEnquiries.setStatus('current')
frextDlcmiLmiRxFullStatusEnquiries = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiRxFullStatusEnquiries.setStatus('current')
frextDlcmiLmiUnknownMessagesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiUnknownMessagesRcvd.setStatus('current')
frextDlcmiLmiStatusLostSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiStatusLostSequences.setStatus('current')
frextDlcmiLmiStatusEnqLostSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiStatusEnqLostSequences.setStatus('current')
frextDlcmiLmiMissingStatEnquiries = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiMissingStatEnquiries.setStatus('current')
frextDlcmiLmiUnexpectedPVCStatMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiUnexpectedPVCStatMsg.setStatus('current')
frextDlcmiLmiUnexpectedDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiUnexpectedDLCI.setStatus('current')
frextDlcmiLmiStatEnqRatePlus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiStatEnqRatePlus.setStatus('current')
frextDlcmiLmiInvInfoFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiInvInfoFrame.setStatus('current')
frextDlcmiLmiInvFrameHdr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiInvFrameHdr.setStatus('current')
frextDlcmiLmiNoIERepType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiNoIERepType.setStatus('current')
frextDlcmiLmiNoIEKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiNoIEKeepAlive.setStatus('current')
frextDlcmiLmiMissingResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiMissingResponses.setStatus('current')
frextDlcmiLmiUnsuppIERcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiLmiUnsuppIERcvd.setStatus('current')
frextDlcmiPvccs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 1, 1, 37), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextDlcmiPvccs.setStatus('current')
frextCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2), )
if mibBuilder.loadTexts: frextCircuitTable.setStatus('current')
frextCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1), ).setIndexNames((0, "Fore-frs-MIB", "frextCircuitServiceIfIndex"), (0, "Fore-frs-MIB", "frextCircuitDlci"))
if mibBuilder.loadTexts: frextCircuitEntry.setStatus('current')
frextCircuitServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitServiceIfIndex.setStatus('current')
frextCircuitDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitDlci.setStatus('current')
frextCircuitName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextCircuitName.setStatus('current')
frextCircuitProfileFrRateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextCircuitProfileFrRateIndex.setStatus('current')
frextCircuitREMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("standard", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frextCircuitREMonitor.setStatus('current')
frextCircuitRateFallbacks = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRateFallbacks.setStatus('current')
frextCircuitRateFallforwards = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRateFallforwards.setStatus('current')
frextCircuitEgFramesDroppedQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitEgFramesDroppedQueueFull.setStatus('current')
frextCircuitNormalSentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitNormalSentFrames.setStatus('current')
frextCircuitNormalSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitNormalSentOctets.setStatus('current')
frextCircuitExcessSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitExcessSentOctets.setStatus('current')
frextCircuitHeldBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitHeldBuffers.setStatus('current')
frextCircuitOctetsOnQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitOctetsOnQueue.setStatus('current')
frextCircuitBuffersOnQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitBuffersOnQueue.setStatus('current')
frextCircuitRxMonNormalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonNormalFrames.setStatus('current')
frextCircuitRxMonNormalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonNormalOctets.setStatus('current')
frextCircuitRxMonExcessOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonExcessOctets.setStatus('current')
frextCircuitRxMonDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonDroppedOctets.setStatus('current')
frextCircuitRxMonDroppedDEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonDroppedDEFrames.setStatus('current')
frextCircuitRxMonDroppedDEOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonDroppedDEOctets.setStatus('current')
frextCircuitRxMonDEOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonDEOctets.setStatus('current')
frextCircuitRxMonSetDEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonSetDEFrames.setStatus('current')
frextCircuitRxMonSetDEOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRxMonSetDEOctets.setStatus('current')
frextCircuitRecvdBECNS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRecvdBECNS.setStatus('current')
frextCircuitRecvdFECNS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frextCircuitRecvdFECNS.setStatus('current')
frsOamF5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3), )
if mibBuilder.loadTexts: frsOamF5Table.setStatus('current')
frsOamF5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1), ).setIndexNames((0, "Fore-frs-MIB", "frsOamF5AtmIf"), (0, "Fore-frs-MIB", "frsOamF5AtmVpi"), (0, "Fore-frs-MIB", "frsOamF5AtmVci"))
if mibBuilder.loadTexts: frsOamF5Entry.setStatus('current')
frsOamF5AtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5AtmIf.setStatus('current')
frsOamF5AtmVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5AtmVpi.setStatus('current')
frsOamF5AtmVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5AtmVci.setStatus('current')
frsOamF5AISRxCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5AISRxCounter.setStatus('current')
frsOamF5AISTxCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5AISTxCounter.setStatus('current')
frsOamF5RDIRxCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5RDIRxCounter.setStatus('current')
frsOamF5RDITxCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frsOamF5RDITxCounter.setStatus('current')
mibBuilder.exportSymbols("Fore-frs-MIB", frextDlcmiLmiUnsuppIERcvd=frextDlcmiLmiUnsuppIERcvd, frextCircuitRxMonNormalOctets=frextCircuitRxMonNormalOctets, frsOamF5AtmIf=frsOamF5AtmIf, frextCircuitNormalSentFrames=frextCircuitNormalSentFrames, frextDlcmiLmiStatEnqRatePlus=frextDlcmiLmiStatEnqRatePlus, frextCircuitRateFallforwards=frextCircuitRateFallforwards, frextCircuitOctetsOnQueue=frextCircuitOctetsOnQueue, frextCircuitHeldBuffers=frextCircuitHeldBuffers, frextDlcmiLmiMissingResponses=frextDlcmiLmiMissingResponses, frextDlcmiLmiUnexpectedDLCI=frextDlcmiLmiUnexpectedDLCI, frextDlcmiLmiInvInfoFrame=frextDlcmiLmiInvInfoFrame, frextDlcmiLmiTxFullStatusResponses=frextDlcmiLmiTxFullStatusResponses, frsOamF5AISRxCounter=frsOamF5AISRxCounter, frextCircuitRxMonDroppedOctets=frextCircuitRxMonDroppedOctets, frextCircuitEntry=frextCircuitEntry, frextDlcmiProfileServiceIndex=frextDlcmiProfileServiceIndex, frextDlcmiLmiNoIERepType=frextDlcmiLmiNoIERepType, frextDlcmiServiceIfIndex=frextDlcmiServiceIfIndex, frextCircuitRxMonExcessOctets=frextCircuitRxMonExcessOctets, frextCircuitREMonitor=frextCircuitREMonitor, frextDlcmiEntry=frextDlcmiEntry, frextDlcmiRcvShortFrames=frextDlcmiRcvShortFrames, frsOamF5Table=frsOamF5Table, frsOamF5Entry=frsOamF5Entry, frextCircuitDlci=frextCircuitDlci, frextDlcmiRcvUnknownErrs=frextDlcmiRcvUnknownErrs, frextDlcmiPvccs=frextDlcmiPvccs, PYSNMP_MODULE_ID=foreFrameRelayModule, frextDlcmiRcvInvalidDLCI=frextDlcmiRcvInvalidDLCI, frsOamF5RDITxCounter=frsOamF5RDITxCounter, frextCircuitRecvdFECNS=frextCircuitRecvdFECNS, frextDlcmiLmiDlci=frextDlcmiLmiDlci, frextDlcmiLmiStatusEnqLostSequences=frextDlcmiLmiStatusEnqLostSequences, frsOamF5AtmVpi=frsOamF5AtmVpi, foreFrameRelayModule=foreFrameRelayModule, frextDlcmiRAControl=frextDlcmiRAControl, frextCircuitRxMonDroppedDEFrames=frextCircuitRxMonDroppedDEFrames, frextCircuitTable=frextCircuitTable, frextDlcmiLmiRxStatusResponses=frextDlcmiLmiRxStatusResponses, frsOamF5AtmVci=frsOamF5AtmVci, frextCircuitRxMonSetDEOctets=frextCircuitRxMonSetDEOctets, frextDlcmiLmiRxStatusEnquiries=frextDlcmiLmiRxStatusEnquiries, frsOamF5AISTxCounter=frsOamF5AISTxCounter, frsOamF5RDIRxCounter=frsOamF5RDIRxCounter, frextCircuitRateFallbacks=frextCircuitRateFallbacks, frextDlcmiTable=frextDlcmiTable, frextCircuitRecvdBECNS=frextCircuitRecvdBECNS, frextDlcmiLmiRxFullStatusEnquiries=frextDlcmiLmiRxFullStatusEnquiries, frextCircuitNormalSentOctets=frextCircuitNormalSentOctets, frextCircuitRxMonDroppedDEOctets=frextCircuitRxMonDroppedDEOctets, frextDlcmiLmiStatusLostSequences=frextDlcmiLmiStatusLostSequences, frextDlcmiLmiInvFrameHdr=frextDlcmiLmiInvFrameHdr, frextDlcmiLmiMissingStatEnquiries=frextDlcmiLmiMissingStatEnquiries, frextDlcmiRxAbortedFrames=frextDlcmiRxAbortedFrames, frextDlcmiLmiTxFullStatusEnquiries=frextDlcmiLmiTxFullStatusEnquiries, frextDlcmiLmiBandwidthControl=frextDlcmiLmiBandwidthControl, frextDlcmiProfileLmiIndex=frextDlcmiProfileLmiIndex, frextCircuitName=frextCircuitName, frextCircuitRxMonDEOctets=frextCircuitRxMonDEOctets, frextCircuitEgFramesDroppedQueueFull=frextCircuitEgFramesDroppedQueueFull, frextDlcmiLmiRxFullStatusResponses=frextDlcmiLmiRxFullStatusResponses, frextDlcmiStatsEnabledTimeStamp=frextDlcmiStatsEnabledTimeStamp, frextDlcmiRcvCrcErrors=frextDlcmiRcvCrcErrors, frextDlcmiLmiTxStatusEnquiries=frextDlcmiLmiTxStatusEnquiries, frextDlcmiRcvLongFrames=frextDlcmiRcvLongFrames, frextDlcmiLmiNoIEKeepAlive=frextDlcmiLmiNoIEKeepAlive, frextCircuitBuffersOnQueue=frextCircuitBuffersOnQueue, frextDlcmiLmiTxStatusResponses=frextDlcmiLmiTxStatusResponses, frextDlcmiLmiFlowControl=frextDlcmiLmiFlowControl, frextCircuitExcessSentOctets=frextCircuitExcessSentOctets, frextCircuitRxMonSetDEFrames=frextCircuitRxMonSetDEFrames, frextCircuitProfileFrRateIndex=frextCircuitProfileFrRateIndex, frextCircuitRxMonNormalFrames=frextCircuitRxMonNormalFrames, frextDlcmiLmiUnexpectedPVCStatMsg=frextDlcmiLmiUnexpectedPVCStatMsg, frextCircuitServiceIfIndex=frextCircuitServiceIfIndex, frextDlcmiLmiUnknownMessagesRcvd=frextDlcmiLmiUnknownMessagesRcvd, frextDlcmiStatsMonitor=frextDlcmiStatsMonitor)
