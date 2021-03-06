#
# PySNMP MIB module IANA-IPPM-METRICS-REGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-IPPM-METRICS-REGISTRY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, mib_2, ObjectIdentity, NotificationType, IpAddress, Integer32, MibIdentifier, iso, Unsigned32, ModuleIdentity, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "mib-2", "ObjectIdentity", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "iso", "Unsigned32", "ModuleIdentity", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaIppmMetricsRegistry = ModuleIdentity((1, 3, 6, 1, 2, 1, 128))
ianaIppmMetricsRegistry.setRevisions(('2015-08-14 00:00', '2014-05-22 00:00', '2010-09-07 00:00', '2009-09-02 00:00', '2009-04-20 00:00', '2006-12-04 00:00', '2005-04-12 00:00',))
if mibBuilder.loadTexts: ianaIppmMetricsRegistry.setLastUpdated('201508140000Z')
if mibBuilder.loadTexts: ianaIppmMetricsRegistry.setOrganization('IANA')
ianaIppmMetrics = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1))
if mibBuilder.loadTexts: ianaIppmMetrics.setStatus('current')
ietfInstantUnidirConnectivity = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 1))
if mibBuilder.loadTexts: ietfInstantUnidirConnectivity.setStatus('current')
ietfInstantBidirConnectivity = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 2))
if mibBuilder.loadTexts: ietfInstantBidirConnectivity.setStatus('current')
ietfIntervalUnidirConnectivity = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 3))
if mibBuilder.loadTexts: ietfIntervalUnidirConnectivity.setStatus('current')
ietfIntervalBidirConnectivity = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 4))
if mibBuilder.loadTexts: ietfIntervalBidirConnectivity.setStatus('current')
ietfIntervalTemporalConnectivity = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 5))
if mibBuilder.loadTexts: ietfIntervalTemporalConnectivity.setStatus('current')
ietfOneWayDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 6))
if mibBuilder.loadTexts: ietfOneWayDelay.setStatus('current')
ietfOneWayDelayPoissonStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 7))
if mibBuilder.loadTexts: ietfOneWayDelayPoissonStream.setStatus('current')
ietfOneWayDelayPercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 8))
if mibBuilder.loadTexts: ietfOneWayDelayPercentile.setStatus('current')
ietfOneWayDelayMedian = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 9))
if mibBuilder.loadTexts: ietfOneWayDelayMedian.setStatus('current')
ietfOneWayDelayMinimum = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 10))
if mibBuilder.loadTexts: ietfOneWayDelayMinimum.setStatus('current')
ietfOneWayDelayInversePercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 11))
if mibBuilder.loadTexts: ietfOneWayDelayInversePercentile.setStatus('current')
ietfOneWayPktLoss = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 12))
if mibBuilder.loadTexts: ietfOneWayPktLoss.setStatus('current')
ietfOneWayPktLossPoissonStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 13))
if mibBuilder.loadTexts: ietfOneWayPktLossPoissonStream.setStatus('current')
ietfOneWayPktLossAverage = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 14))
if mibBuilder.loadTexts: ietfOneWayPktLossAverage.setStatus('current')
ietfRoundTripDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 15))
if mibBuilder.loadTexts: ietfRoundTripDelay.setStatus('current')
ietfRoundTripDelayPoissonStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 16))
if mibBuilder.loadTexts: ietfRoundTripDelayPoissonStream.setStatus('current')
ietfRoundTripDelayPercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 17))
if mibBuilder.loadTexts: ietfRoundTripDelayPercentile.setStatus('current')
ietfRoundTripDelayMedian = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 18))
if mibBuilder.loadTexts: ietfRoundTripDelayMedian.setStatus('current')
ietfRoundTripDelayMinimum = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 19))
if mibBuilder.loadTexts: ietfRoundTripDelayMinimum.setStatus('current')
ietfRoundTripDelayInvPercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 20))
if mibBuilder.loadTexts: ietfRoundTripDelayInvPercentile.setStatus('current')
ietfOneWayLossDistanceStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 21))
if mibBuilder.loadTexts: ietfOneWayLossDistanceStream.setStatus('current')
ietfOneWayLossPeriodStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 22))
if mibBuilder.loadTexts: ietfOneWayLossPeriodStream.setStatus('current')
ietfOneWayLossNoticeableRate = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 23))
if mibBuilder.loadTexts: ietfOneWayLossNoticeableRate.setStatus('current')
ietfOneWayLossPeriodTotal = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 24))
if mibBuilder.loadTexts: ietfOneWayLossPeriodTotal.setStatus('current')
ietfOneWayLossPeriodLengths = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 25))
if mibBuilder.loadTexts: ietfOneWayLossPeriodLengths.setStatus('current')
ietfOneWayInterLossPeriodLengths = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 26))
if mibBuilder.loadTexts: ietfOneWayInterLossPeriodLengths.setStatus('current')
ietfOneWayIpdv = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 27))
if mibBuilder.loadTexts: ietfOneWayIpdv.setStatus('current')
ietfOneWayIpdvPoissonStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 28))
if mibBuilder.loadTexts: ietfOneWayIpdvPoissonStream.setStatus('current')
ietfOneWayIpdvPercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 29))
if mibBuilder.loadTexts: ietfOneWayIpdvPercentile.setStatus('current')
ietfOneWayIpdvInversePercentile = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 30))
if mibBuilder.loadTexts: ietfOneWayIpdvInversePercentile.setStatus('current')
ietfOneWayIpdvJitter = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 31))
if mibBuilder.loadTexts: ietfOneWayIpdvJitter.setStatus('current')
ietfOneWayPeakToPeakIpdv = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 32))
if mibBuilder.loadTexts: ietfOneWayPeakToPeakIpdv.setStatus('current')
ietfOneWayDelayPeriodicStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 33))
if mibBuilder.loadTexts: ietfOneWayDelayPeriodicStream.setStatus('current')
ietfReorderedSingleton = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 34))
if mibBuilder.loadTexts: ietfReorderedSingleton.setStatus('current')
ietfReorderedPacketRatio = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 35))
if mibBuilder.loadTexts: ietfReorderedPacketRatio.setStatus('current')
ietfReorderingExtent = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 36))
if mibBuilder.loadTexts: ietfReorderingExtent.setStatus('current')
ietfReorderingLateTimeOffset = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 37))
if mibBuilder.loadTexts: ietfReorderingLateTimeOffset.setStatus('current')
ietfReorderingByteOffset = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 38))
if mibBuilder.loadTexts: ietfReorderingByteOffset.setStatus('current')
ietfReorderingGap = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 39))
if mibBuilder.loadTexts: ietfReorderingGap.setStatus('current')
ietfReorderingGapTime = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 40))
if mibBuilder.loadTexts: ietfReorderingGapTime.setStatus('current')
ietfReorderingFreeRunx = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 41))
if mibBuilder.loadTexts: ietfReorderingFreeRunx.setStatus('current')
ietfReorderingFreeRunq = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 42))
if mibBuilder.loadTexts: ietfReorderingFreeRunq.setStatus('current')
ietfReorderingFreeRunp = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 43))
if mibBuilder.loadTexts: ietfReorderingFreeRunp.setStatus('current')
ietfReorderingFreeRuna = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 44))
if mibBuilder.loadTexts: ietfReorderingFreeRuna.setStatus('current')
ietfnReordering = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 45))
if mibBuilder.loadTexts: ietfnReordering.setStatus('current')
ietfOneWayPacketArrivalCount = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 46))
if mibBuilder.loadTexts: ietfOneWayPacketArrivalCount.setStatus('current')
ietfOneWayPacketDuplication = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 47))
if mibBuilder.loadTexts: ietfOneWayPacketDuplication.setStatus('current')
ietfOneWayPacketDuplicationPoissonStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 48))
if mibBuilder.loadTexts: ietfOneWayPacketDuplicationPoissonStream.setStatus('current')
ietfOneWayPacketDuplicationPeriodicStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 49))
if mibBuilder.loadTexts: ietfOneWayPacketDuplicationPeriodicStream.setStatus('current')
ietfOneWayPacketDuplicationFraction = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 50))
if mibBuilder.loadTexts: ietfOneWayPacketDuplicationFraction.setStatus('current')
ietfOneWayReplicatedPacketRate = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 51))
if mibBuilder.loadTexts: ietfOneWayReplicatedPacketRate.setStatus('current')
ietfSpatialOneWayDelayVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 52))
if mibBuilder.loadTexts: ietfSpatialOneWayDelayVector.setStatus('current')
ietfSpatialPacketLossVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 53))
if mibBuilder.loadTexts: ietfSpatialPacketLossVector.setStatus('current')
ietfSpatialOneWayIpdvVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 54))
if mibBuilder.loadTexts: ietfSpatialOneWayIpdvVector.setStatus('current')
ietfSegmentOneWayDelayStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 55))
if mibBuilder.loadTexts: ietfSegmentOneWayDelayStream.setStatus('current')
ietfSegmentPacketLossStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 56))
if mibBuilder.loadTexts: ietfSegmentPacketLossStream.setStatus('current')
ietfSegmentIpdvPrevStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 57))
if mibBuilder.loadTexts: ietfSegmentIpdvPrevStream.setStatus('current')
ietfSegmentIpdvMinStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 58))
if mibBuilder.loadTexts: ietfSegmentIpdvMinStream.setStatus('current')
ietfOneToGroupDelayVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 59))
if mibBuilder.loadTexts: ietfOneToGroupDelayVector.setStatus('current')
ietfOneToGroupPacketLossVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 60))
if mibBuilder.loadTexts: ietfOneToGroupPacketLossVector.setStatus('current')
ietfOneToGroupIpdvVector = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 61))
if mibBuilder.loadTexts: ietfOneToGroupIpdvVector.setStatus('current')
ietfOnetoGroupReceiverNMeanDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 62))
if mibBuilder.loadTexts: ietfOnetoGroupReceiverNMeanDelay.setStatus('current')
ietfOneToGroupMeanDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 63))
if mibBuilder.loadTexts: ietfOneToGroupMeanDelay.setStatus('current')
ietfOneToGroupRangeMeanDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 64))
if mibBuilder.loadTexts: ietfOneToGroupRangeMeanDelay.setStatus('current')
ietfOneToGroupMaxMeanDelay = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 65))
if mibBuilder.loadTexts: ietfOneToGroupMaxMeanDelay.setStatus('current')
ietfOneToGroupReceiverNLossRatio = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 66))
if mibBuilder.loadTexts: ietfOneToGroupReceiverNLossRatio.setStatus('current')
ietfOneToGroupReceiverNCompLossRatio = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 67))
if mibBuilder.loadTexts: ietfOneToGroupReceiverNCompLossRatio.setStatus('current')
ietfOneToGroupLossRatio = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 68))
if mibBuilder.loadTexts: ietfOneToGroupLossRatio.setStatus('current')
ietfOneToGroupRangeLossRatio = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 69))
if mibBuilder.loadTexts: ietfOneToGroupRangeLossRatio.setStatus('current')
ietfOneToGroupRangeDelayVariation = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 70))
if mibBuilder.loadTexts: ietfOneToGroupRangeDelayVariation.setStatus('current')
ietfFiniteOneWayDelayStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 71))
if mibBuilder.loadTexts: ietfFiniteOneWayDelayStream.setStatus('current')
ietfFiniteOneWayDelayMean = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 72))
if mibBuilder.loadTexts: ietfFiniteOneWayDelayMean.setStatus('current')
ietfCompositeOneWayDelayMean = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 73))
if mibBuilder.loadTexts: ietfCompositeOneWayDelayMean.setStatus('current')
ietfFiniteOneWayDelayMinimum = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 74))
if mibBuilder.loadTexts: ietfFiniteOneWayDelayMinimum.setStatus('current')
ietfCompositeOneWayDelayMinimum = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 75))
if mibBuilder.loadTexts: ietfCompositeOneWayDelayMinimum.setStatus('current')
ietfOneWayPktLossEmpiricProb = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 76))
if mibBuilder.loadTexts: ietfOneWayPktLossEmpiricProb.setStatus('current')
ietfCompositeOneWayPktLossEmpiricProb = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 77))
if mibBuilder.loadTexts: ietfCompositeOneWayPktLossEmpiricProb.setStatus('current')
ietfOneWayPdvRefminStream = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 78))
if mibBuilder.loadTexts: ietfOneWayPdvRefminStream.setStatus('current')
ietfOneWayPdvRefminMean = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 79))
if mibBuilder.loadTexts: ietfOneWayPdvRefminMean.setStatus('current')
ietfOneWayPdvRefminVariance = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 80))
if mibBuilder.loadTexts: ietfOneWayPdvRefminVariance.setStatus('current')
ietfOneWayPdvRefminSkewness = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 81))
if mibBuilder.loadTexts: ietfOneWayPdvRefminSkewness.setStatus('current')
ietfCompositeOneWayPdvRefminQtil = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 82))
if mibBuilder.loadTexts: ietfCompositeOneWayPdvRefminQtil.setStatus('current')
ietfCompositeOneWayPdvRefminNPA = ObjectIdentity((1, 3, 6, 1, 2, 1, 128, 1, 83))
if mibBuilder.loadTexts: ietfCompositeOneWayPdvRefminNPA.setStatus('current')
mibBuilder.exportSymbols("IANA-IPPM-METRICS-REGISTRY-MIB", ietfRoundTripDelayInvPercentile=ietfRoundTripDelayInvPercentile, ietfOneWayLossNoticeableRate=ietfOneWayLossNoticeableRate, ietfOneWayPktLoss=ietfOneWayPktLoss, ietfOneWayIpdv=ietfOneWayIpdv, ietfOneWayInterLossPeriodLengths=ietfOneWayInterLossPeriodLengths, ietfOnetoGroupReceiverNMeanDelay=ietfOnetoGroupReceiverNMeanDelay, ietfOneWayDelayPoissonStream=ietfOneWayDelayPoissonStream, ietfCompositeOneWayPktLossEmpiricProb=ietfCompositeOneWayPktLossEmpiricProb, ietfOneWayPdvRefminMean=ietfOneWayPdvRefminMean, ietfnReordering=ietfnReordering, ietfSpatialOneWayDelayVector=ietfSpatialOneWayDelayVector, ietfOneWayPacketDuplicationFraction=ietfOneWayPacketDuplicationFraction, ietfSegmentPacketLossStream=ietfSegmentPacketLossStream, ietfSegmentIpdvMinStream=ietfSegmentIpdvMinStream, ietfCompositeOneWayPdvRefminQtil=ietfCompositeOneWayPdvRefminQtil, ietfReorderingExtent=ietfReorderingExtent, ietfOneToGroupRangeDelayVariation=ietfOneToGroupRangeDelayVariation, ietfOneToGroupRangeLossRatio=ietfOneToGroupRangeLossRatio, ietfOneWayIpdvPercentile=ietfOneWayIpdvPercentile, ietfInstantBidirConnectivity=ietfInstantBidirConnectivity, ietfCompositeOneWayDelayMean=ietfCompositeOneWayDelayMean, ietfOneToGroupDelayVector=ietfOneToGroupDelayVector, ietfRoundTripDelayMinimum=ietfRoundTripDelayMinimum, ietfFiniteOneWayDelayStream=ietfFiniteOneWayDelayStream, ietfOneWayDelayMinimum=ietfOneWayDelayMinimum, ietfOneWayDelayPeriodicStream=ietfOneWayDelayPeriodicStream, ietfOneToGroupIpdvVector=ietfOneToGroupIpdvVector, ietfOneWayPacketDuplicationPeriodicStream=ietfOneWayPacketDuplicationPeriodicStream, ietfReorderingByteOffset=ietfReorderingByteOffset, ietfReorderingFreeRuna=ietfReorderingFreeRuna, ietfOneWayLossPeriodLengths=ietfOneWayLossPeriodLengths, ietfOneToGroupMeanDelay=ietfOneToGroupMeanDelay, ietfOneToGroupReceiverNLossRatio=ietfOneToGroupReceiverNLossRatio, ietfReorderingGapTime=ietfReorderingGapTime, PYSNMP_MODULE_ID=ianaIppmMetricsRegistry, ietfCompositeOneWayPdvRefminNPA=ietfCompositeOneWayPdvRefminNPA, ietfOneWayPktLossEmpiricProb=ietfOneWayPktLossEmpiricProb, ietfOneWayPdvRefminVariance=ietfOneWayPdvRefminVariance, ietfOneWayPdvRefminSkewness=ietfOneWayPdvRefminSkewness, ietfOneToGroupReceiverNCompLossRatio=ietfOneToGroupReceiverNCompLossRatio, ietfReorderedPacketRatio=ietfReorderedPacketRatio, ietfOneWayPktLossAverage=ietfOneWayPktLossAverage, ietfOneToGroupLossRatio=ietfOneToGroupLossRatio, ietfOneWayDelay=ietfOneWayDelay, ietfReorderingGap=ietfReorderingGap, ietfOneToGroupMaxMeanDelay=ietfOneToGroupMaxMeanDelay, ietfSpatialPacketLossVector=ietfSpatialPacketLossVector, ietfOneWayDelayMedian=ietfOneWayDelayMedian, ietfCompositeOneWayDelayMinimum=ietfCompositeOneWayDelayMinimum, ietfReorderingLateTimeOffset=ietfReorderingLateTimeOffset, ietfOneWayPktLossPoissonStream=ietfOneWayPktLossPoissonStream, ietfIntervalBidirConnectivity=ietfIntervalBidirConnectivity, ietfOneWayPacketDuplication=ietfOneWayPacketDuplication, ietfOneWayPacketArrivalCount=ietfOneWayPacketArrivalCount, ietfIntervalUnidirConnectivity=ietfIntervalUnidirConnectivity, ietfSegmentIpdvPrevStream=ietfSegmentIpdvPrevStream, ietfReorderedSingleton=ietfReorderedSingleton, ietfIntervalTemporalConnectivity=ietfIntervalTemporalConnectivity, ietfReorderingFreeRunp=ietfReorderingFreeRunp, ietfFiniteOneWayDelayMinimum=ietfFiniteOneWayDelayMinimum, ianaIppmMetricsRegistry=ianaIppmMetricsRegistry, ietfOneToGroupRangeMeanDelay=ietfOneToGroupRangeMeanDelay, ietfOneWayIpdvInversePercentile=ietfOneWayIpdvInversePercentile, ietfOneWayIpdvJitter=ietfOneWayIpdvJitter, ietfOneWayPdvRefminStream=ietfOneWayPdvRefminStream, ietfOneToGroupPacketLossVector=ietfOneToGroupPacketLossVector, ietfOneWayDelayInversePercentile=ietfOneWayDelayInversePercentile, ietfReorderingFreeRunq=ietfReorderingFreeRunq, ietfOneWayPeakToPeakIpdv=ietfOneWayPeakToPeakIpdv, ianaIppmMetrics=ianaIppmMetrics, ietfInstantUnidirConnectivity=ietfInstantUnidirConnectivity, ietfRoundTripDelay=ietfRoundTripDelay, ietfRoundTripDelayPoissonStream=ietfRoundTripDelayPoissonStream, ietfReorderingFreeRunx=ietfReorderingFreeRunx, ietfFiniteOneWayDelayMean=ietfFiniteOneWayDelayMean, ietfOneWayIpdvPoissonStream=ietfOneWayIpdvPoissonStream, ietfOneWayDelayPercentile=ietfOneWayDelayPercentile, ietfSegmentOneWayDelayStream=ietfSegmentOneWayDelayStream, ietfOneWayLossDistanceStream=ietfOneWayLossDistanceStream, ietfOneWayLossPeriodStream=ietfOneWayLossPeriodStream, ietfOneWayReplicatedPacketRate=ietfOneWayReplicatedPacketRate, ietfRoundTripDelayPercentile=ietfRoundTripDelayPercentile, ietfOneWayPacketDuplicationPoissonStream=ietfOneWayPacketDuplicationPoissonStream, ietfRoundTripDelayMedian=ietfRoundTripDelayMedian, ietfOneWayLossPeriodTotal=ietfOneWayLossPeriodTotal, ietfSpatialOneWayIpdvVector=ietfSpatialOneWayIpdvVector)
