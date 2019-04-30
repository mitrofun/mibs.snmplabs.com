#
# PySNMP MIB module DELL-NETWORKING-BPSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-BPSTATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, iso, IpAddress, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32, NotificationType, ObjectIdentity, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "IpAddress", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Unsigned32")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
dellNetBpStatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 24))
dellNetBpStatsMib.setRevisions(('2013-05-22 12:48',))
if mibBuilder.loadTexts: dellNetBpStatsMib.setLastUpdated('201309181248Z')
if mibBuilder.loadTexts: dellNetBpStatsMib.setOrganization('Dell Inc')
dellNetBpStatsLinkBundleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 1))
dellNetBpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2))
dellNetBpStatsAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3))
bpLinkBundleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1))
bpLinkBundleRateInterval = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 299))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bpLinkBundleRateInterval.setStatus('current')
bpLinkBundleTriggerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 90))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bpLinkBundleTriggerThreshold.setStatus('current')
bpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1))
bpDropsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1), )
if mibBuilder.loadTexts: bpDropsTable.setStatus('current')
bpDropsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1), ).setIndexNames((0, "DELL-NETWORKING-BPSTATS-MIB", "bpDropsStackUnitIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpDropsPortPipe"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpDropsPortIndex"))
if mibBuilder.loadTexts: bpDropsEntry.setStatus('current')
bpDropsStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: bpDropsStackUnitIndex.setStatus('current')
bpDropsPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: bpDropsPortPipe.setStatus('current')
bpDropsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: bpDropsPortIndex.setStatus('current')
bpDropsInDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsInDrops.setStatus('current')
bpDropsInUnKnownHgHdr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsInUnKnownHgHdr.setStatus('current')
bpDropsInUnKnownHgOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsInUnKnownHgOpcode.setStatus('current')
bpDropsInMTUExceeds = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsInMTUExceeds.setStatus('current')
bpDropsInMacDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsInMacDrops.setStatus('current')
bpDropsMMUHOLDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsMMUHOLDrops.setStatus('current')
bpDropsEgMacDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsEgMacDrops.setStatus('current')
bpDropsEgTxAgedCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsEgTxAgedCounter.setStatus('current')
bpDropsEgTxErrCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsEgTxErrCounter.setStatus('current')
bpDropsEgTxMACUnderflow = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsEgTxMACUnderflow.setStatus('current')
bpDropsEgTxErrPktCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpDropsEgTxErrPktCounter.setStatus('current')
bpIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2), )
if mibBuilder.loadTexts: bpIfStatsTable.setStatus('current')
bpIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1), ).setIndexNames((0, "DELL-NETWORKING-BPSTATS-MIB", "bpIfStatsStackUnitIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpIfStatsPortPipe"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpIfStatsPortIndex"))
if mibBuilder.loadTexts: bpIfStatsEntry.setStatus('current')
bpIfStatsStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: bpIfStatsStackUnitIndex.setStatus('current')
bpIfStatsPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: bpIfStatsPortPipe.setStatus('current')
bpIfStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: bpIfStatsPortIndex.setStatus('current')
bpIfStatsIn64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsIn64BytePkts.setStatus('current')
bpIfStatsIn65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsIn65To127BytePkts.setStatus('current')
bpIfStatsIn128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsIn128To255BytePkts.setStatus('current')
bpIfStatsIn256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsIn256To511BytePkts.setStatus('current')
bpIfStatsIn512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsIn512To1023BytePkts.setStatus('current')
bpIfStatsInOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInOver1023BytePkts.setStatus('current')
bpIfStatsInThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInThrottles.setStatus('current')
bpIfStatsInRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInRunts.setStatus('current')
bpIfStatsInGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInGiants.setStatus('current')
bpIfStatsInCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInCRC.setStatus('current')
bpIfStatsInOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInOverruns.setStatus('current')
bpIfStatsOutUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutUnderruns.setStatus('current')
bpIfStatsOutUnicasts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutUnicasts.setStatus('current')
bpIfStatsOutCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutCollisions.setStatus('current')
bpIfStatsOutWredDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutWredDrops.setStatus('current')
bpIfStatsOut64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOut64BytePkts.setStatus('current')
bpIfStatsOut65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOut65To127BytePkts.setStatus('current')
bpIfStatsOut128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOut128To255BytePkts.setStatus('current')
bpIfStatsOut256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOut256To511BytePkts.setStatus('current')
bpIfStatsOut512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOut512To1023BytePkts.setStatus('current')
bpIfStatsOutOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutOver1023BytePkts.setStatus('current')
bpIfStatsOutThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutThrottles.setStatus('current')
bpIfStatsLastDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 26), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsLastDiscontinuityTime.setStatus('current')
bpIfStatsInCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsInCentRate.setStatus('current')
bpIfStatsOutCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsOutCentRate.setStatus('current')
bpIfStatsLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 29), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIfStatsLastChange.setStatus('current')
bpPacketBufferTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3), )
if mibBuilder.loadTexts: bpPacketBufferTable.setStatus('current')
bpPacketBufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1), ).setIndexNames((0, "DELL-NETWORKING-BPSTATS-MIB", "bpPacketBufferStackUnitIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpPacketBufferPortPipe"))
if mibBuilder.loadTexts: bpPacketBufferEntry.setStatus('current')
bpPacketBufferStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: bpPacketBufferStackUnitIndex.setStatus('current')
bpPacketBufferPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: bpPacketBufferPortPipe.setStatus('current')
bpPacketBufferTotalPacketBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpPacketBufferTotalPacketBuffer.setStatus('current')
bpPacketBufferCurrentAvailBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpPacketBufferCurrentAvailBuffer.setStatus('current')
bpPacketBufferPacketBufferAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpPacketBufferPacketBufferAlloc.setStatus('current')
bpBufferStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4), )
if mibBuilder.loadTexts: bpBufferStatsTable.setStatus('current')
bpBufferStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1), ).setIndexNames((0, "DELL-NETWORKING-BPSTATS-MIB", "bpBufferStatsStackUnitIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpBufferStatsPortPipe"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpBufferStatsPortIndex"))
if mibBuilder.loadTexts: bpBufferStatsEntry.setStatus('current')
bpBufferStatsStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: bpBufferStatsStackUnitIndex.setStatus('current')
bpBufferStatsPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: bpBufferStatsPortPipe.setStatus('current')
bpBufferStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: bpBufferStatsPortIndex.setStatus('current')
bpBufferStatsCurrentUsagePerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpBufferStatsCurrentUsagePerPort.setStatus('current')
bpBufferStatsDefaultPacketBuffAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpBufferStatsDefaultPacketBuffAlloc.setStatus('current')
bpBufferStatsMaxLimitPerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpBufferStatsMaxLimitPerPort.setStatus('current')
bpCosStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5), )
if mibBuilder.loadTexts: bpCosStatsTable.setStatus('current')
bpCosStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1), ).setIndexNames((0, "DELL-NETWORKING-BPSTATS-MIB", "bpCosStatsStackUnitIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpCosStatsPortPipe"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpCosStatsPortIndex"), (0, "DELL-NETWORKING-BPSTATS-MIB", "bpCosStatsCOSNumber"))
if mibBuilder.loadTexts: bpCosStatsEntry.setStatus('current')
bpCosStatsStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: bpCosStatsStackUnitIndex.setStatus('current')
bpCosStatsPortPipe = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: bpCosStatsPortPipe.setStatus('current')
bpCosStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: bpCosStatsPortIndex.setStatus('current')
bpCosStatsCOSNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: bpCosStatsCOSNumber.setStatus('current')
bpCosStatsCurrentUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpCosStatsCurrentUsage.setStatus('current')
bpCosStatsDefaultPacketBuffAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpCosStatsDefaultPacketBuffAlloc.setStatus('current')
bpCosStatsMaxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpCosStatsMaxLimit.setStatus('current')
bpCosStatsHOLDDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpCosStatsHOLDDrops.setStatus('current')
bpLinkBundleNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1))
bpLinkBundleAlarmVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2))
bpLinkBundleType = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("bpHgBundle", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bpLinkBundleType.setStatus('current')
bpLinkBundleSlot = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bpLinkBundleSlot.setStatus('current')
bpLinkBundleNpuUnit = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bpLinkBundleNpuUnit.setStatus('current')
bpLinkBundleLocalId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bpLinkBundleLocalId.setStatus('current')
bpLinkBundleImbalance = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1, 1)).setObjects(("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleType"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleSlot"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleNpuUnit"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleLocalId"))
if mibBuilder.loadTexts: bpLinkBundleImbalance.setStatus('current')
bpLinkBundleImbalanceClear = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1, 2)).setObjects(("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleType"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleSlot"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleNpuUnit"), ("DELL-NETWORKING-BPSTATS-MIB", "bpLinkBundleLocalId"))
if mibBuilder.loadTexts: bpLinkBundleImbalanceClear.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-BPSTATS-MIB", bpIfStatsOutUnderruns=bpIfStatsOutUnderruns, bpCosStatsHOLDDrops=bpCosStatsHOLDDrops, bpPacketBufferCurrentAvailBuffer=bpPacketBufferCurrentAvailBuffer, bpDropsInUnKnownHgHdr=bpDropsInUnKnownHgHdr, bpIfStatsIn65To127BytePkts=bpIfStatsIn65To127BytePkts, bpLinkBundleAlarmVariable=bpLinkBundleAlarmVariable, bpDropsInUnKnownHgOpcode=bpDropsInUnKnownHgOpcode, bpIfStatsInThrottles=bpIfStatsInThrottles, bpPacketBufferPortPipe=bpPacketBufferPortPipe, bpLinkBundleNotifications=bpLinkBundleNotifications, bpIfStatsIn64BytePkts=bpIfStatsIn64BytePkts, bpIfStatsInCentRate=bpIfStatsInCentRate, bpPacketBufferEntry=bpPacketBufferEntry, bpIfStatsIn256To511BytePkts=bpIfStatsIn256To511BytePkts, bpBufferStatsCurrentUsagePerPort=bpBufferStatsCurrentUsagePerPort, bpIfStatsEntry=bpIfStatsEntry, bpLinkBundleSlot=bpLinkBundleSlot, bpDropsInMTUExceeds=bpDropsInMTUExceeds, bpDropsEgTxMACUnderflow=bpDropsEgTxMACUnderflow, dellNetBpStatsObjects=dellNetBpStatsObjects, bpIfStatsStackUnitIndex=bpIfStatsStackUnitIndex, bpDropsPortPipe=bpDropsPortPipe, bpPacketBufferStackUnitIndex=bpPacketBufferStackUnitIndex, bpCosStatsCurrentUsage=bpCosStatsCurrentUsage, bpIfStatsOutCentRate=bpIfStatsOutCentRate, bpIfStatsIn512To1023BytePkts=bpIfStatsIn512To1023BytePkts, bpBufferStatsEntry=bpBufferStatsEntry, bpLinkBundleRateInterval=bpLinkBundleRateInterval, bpDropsInDrops=bpDropsInDrops, bpLinkBundleObjects=bpLinkBundleObjects, bpIfStatsOutCollisions=bpIfStatsOutCollisions, bpDropsPortIndex=bpDropsPortIndex, bpCosStatsDefaultPacketBuffAlloc=bpCosStatsDefaultPacketBuffAlloc, bpBufferStatsPortPipe=bpBufferStatsPortPipe, bpCosStatsCOSNumber=bpCosStatsCOSNumber, bpLinkBundleImbalance=bpLinkBundleImbalance, bpCosStatsStackUnitIndex=bpCosStatsStackUnitIndex, bpBufferStatsStackUnitIndex=bpBufferStatsStackUnitIndex, bpIfStatsOut65To127BytePkts=bpIfStatsOut65To127BytePkts, bpIfStatsInOver1023BytePkts=bpIfStatsInOver1023BytePkts, bpIfStatsPortIndex=bpIfStatsPortIndex, bpDropsMMUHOLDrops=bpDropsMMUHOLDrops, bpPacketBufferTotalPacketBuffer=bpPacketBufferTotalPacketBuffer, bpLinkBundleNpuUnit=bpLinkBundleNpuUnit, bpBufferStatsDefaultPacketBuffAlloc=bpBufferStatsDefaultPacketBuffAlloc, bpBufferStatsTable=bpBufferStatsTable, bpDropsInMacDrops=bpDropsInMacDrops, bpIfStatsOut64BytePkts=bpIfStatsOut64BytePkts, bpIfStatsOutWredDrops=bpIfStatsOutWredDrops, bpIfStatsOut512To1023BytePkts=bpIfStatsOut512To1023BytePkts, dellNetBpStatsLinkBundleObjects=dellNetBpStatsLinkBundleObjects, PYSNMP_MODULE_ID=dellNetBpStatsMib, bpIfStatsOutUnicasts=bpIfStatsOutUnicasts, bpIfStatsLastChange=bpIfStatsLastChange, dellNetBpStatsMib=dellNetBpStatsMib, bpDropsEntry=bpDropsEntry, bpCosStatsEntry=bpCosStatsEntry, bpDropsEgTxErrPktCounter=bpDropsEgTxErrPktCounter, bpLinkBundleLocalId=bpLinkBundleLocalId, bpDropsTable=bpDropsTable, bpIfStatsIn128To255BytePkts=bpIfStatsIn128To255BytePkts, bpPacketBufferTable=bpPacketBufferTable, bpCosStatsPortIndex=bpCosStatsPortIndex, bpDropsEgTxErrCounter=bpDropsEgTxErrCounter, bpIfStatsOut256To511BytePkts=bpIfStatsOut256To511BytePkts, bpIfStatsLastDiscontinuityTime=bpIfStatsLastDiscontinuityTime, bpIfStatsInOverruns=bpIfStatsInOverruns, bpDropsEgTxAgedCounter=bpDropsEgTxAgedCounter, bpCosStatsPortPipe=bpCosStatsPortPipe, bpCosStatsMaxLimit=bpCosStatsMaxLimit, bpBufferStatsPortIndex=bpBufferStatsPortIndex, bpLinkBundleType=bpLinkBundleType, bpPacketBufferPacketBufferAlloc=bpPacketBufferPacketBufferAlloc, bpIfStatsOutOver1023BytePkts=bpIfStatsOutOver1023BytePkts, bpLinkBundleTriggerThreshold=bpLinkBundleTriggerThreshold, bpIfStatsInRunts=bpIfStatsInRunts, bpIfStatsOutThrottles=bpIfStatsOutThrottles, bpStatsObjects=bpStatsObjects, bpIfStatsInCRC=bpIfStatsInCRC, dellNetBpStatsAlarms=dellNetBpStatsAlarms, bpBufferStatsMaxLimitPerPort=bpBufferStatsMaxLimitPerPort, bpIfStatsTable=bpIfStatsTable, bpDropsStackUnitIndex=bpDropsStackUnitIndex, bpLinkBundleImbalanceClear=bpLinkBundleImbalanceClear, bpDropsEgMacDrops=bpDropsEgMacDrops, bpCosStatsTable=bpCosStatsTable, bpIfStatsInGiants=bpIfStatsInGiants, bpIfStatsOut128To255BytePkts=bpIfStatsOut128To255BytePkts, bpIfStatsPortPipe=bpIfStatsPortPipe)