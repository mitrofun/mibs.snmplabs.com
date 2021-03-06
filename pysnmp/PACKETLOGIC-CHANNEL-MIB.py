#
# PySNMP MIB module PACKETLOGIC-CHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETLOGIC-CHANNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Integer32, MibIdentifier, Counter32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "Counter32", "TimeTicks", "NotificationType")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
channelstats = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 2))
channelstats.setRevisions(('2012-09-26 12:48',))
if mibBuilder.loadTexts: channelstats.setLastUpdated('201209261248Z')
if mibBuilder.loadTexts: channelstats.setOrganization('Procera Networks, Inc.')
channelCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8))
channelInfoTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17), )
if mibBuilder.loadTexts: channelInfoTable.setStatus('current')
channelInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "channelInfoEntryIndex"))
if mibBuilder.loadTexts: channelInfoEntry.setStatus('current')
channelInfoEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: channelInfoEntryIndex.setStatus('current')
netDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25), )
if mibBuilder.loadTexts: netDeviceTable.setStatus('current')
netDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "netDeviceEntryIndex"))
if mibBuilder.loadTexts: netDeviceEntry.setStatus('current')
netDeviceEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: netDeviceEntryIndex.setStatus('current')
channelRxPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1))
channelTxPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2))
channelRxBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3))
channelTxBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4))
channelRxErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5))
channelTxErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6))
channelRxDrops = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7))
channelTxDrops = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8))
channelCollisions = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9))
channelMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10))
channelRxLengthErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11))
channelRxCrcErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12))
channelRxFrameErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13))
channelRxFifoErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14))
channelRxMissedErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15))
channelTxAborted = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16))
channelTxWindowErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17))
channelTxCarrierErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18))
channelNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumber.setStatus('current')
channelInternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMedia.setStatus('current')
channelExternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMedia.setStatus('current')
channelInternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMedia.setStatus('current')
channelExternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalNegotiatedMedia.setStatus('current')
channelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelActive.setStatus('current')
channelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelName.setStatus('current')
channelInternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMediaTime.setStatus('current')
channelexternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelexternalNegotiatedMediaTime.setStatus('current')
channelInternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxPackets.setStatus('current')
channelExternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxPackets.setStatus('current')
channelInternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxPackets.setStatus('current')
channelExternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxPackets.setStatus('current')
channelInternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxBytes.setStatus('current')
channelExternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxBytes.setStatus('current')
channelInternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxBytes.setStatus('current')
channelExternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxBytes.setStatus('current')
channelInternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxErrors.setStatus('current')
channelExternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxErrors.setStatus('current')
channelInternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxErrors.setStatus('current')
channelExternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxErrors.setStatus('current')
channelInternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxDrops.setStatus('current')
channelExternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxDrops.setStatus('current')
channelInternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxDrops.setStatus('current')
channelExternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxDrops.setStatus('current')
channelInternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalCollisions.setStatus('current')
channelExternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalCollisions.setStatus('current')
channelInternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMulticast.setStatus('current')
channelExternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMulticast.setStatus('current')
channelInternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxLengthErrors.setStatus('current')
channelExternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxLengthErrors.setStatus('current')
channelInternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxCrcErrors.setStatus('current')
channelExternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxCrcErrors.setStatus('current')
channelInternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxFrameErrors.setStatus('current')
channelExternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFrameErrors.setStatus('current')
channelINternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelINternalRxFifoErrors.setStatus('current')
channelExternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFifoErrors.setStatus('current')
channelInternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxMissedErrors.setStatus('current')
channelExternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxMissedErrors.setStatus('current')
channelInternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxAborted.setStatus('current')
channelExternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxAborted.setStatus('current')
channelInternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxWindowErrors.setStatus('current')
channelExternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxWindowErrors.setStatus('current')
channelInternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxCarrierErrors.setStatus('current')
channelExternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxCarrierErrors.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-CHANNEL-MIB", channelINternalRxFifoErrors=channelINternalRxFifoErrors, channelExternalNegotiatedMedia=channelExternalNegotiatedMedia, channelInternalTxBytes=channelInternalTxBytes, channelInternalTxWindowErrors=channelInternalTxWindowErrors, channelMulticast=channelMulticast, channelInternalTxPackets=channelInternalTxPackets, channelInfoEntry=channelInfoEntry, channelExternalRxFrameErrors=channelExternalRxFrameErrors, channelExternalTxAborted=channelExternalTxAborted, channelInternalRxCrcErrors=channelInternalRxCrcErrors, channelExternalMedia=channelExternalMedia, channelInternalMulticast=channelInternalMulticast, channelActive=channelActive, netDeviceEntryIndex=netDeviceEntryIndex, channelExternalMulticast=channelExternalMulticast, channelInternalTxDrops=channelInternalTxDrops, channelExternalCollisions=channelExternalCollisions, channelExternalTxPackets=channelExternalTxPackets, channelInternalRxFrameErrors=channelInternalRxFrameErrors, channelExternalTxCarrierErrors=channelExternalTxCarrierErrors, channelRxLengthErrors=channelRxLengthErrors, channelRxBytes=channelRxBytes, channelCfg=channelCfg, channelInternalMedia=channelInternalMedia, channelInternalRxErrors=channelInternalRxErrors, channelRxFifoErrors=channelRxFifoErrors, netDeviceTable=netDeviceTable, channelRxPackets=channelRxPackets, channelInfoEntryIndex=channelInfoEntryIndex, channelInternalRxDrops=channelInternalRxDrops, channelExternalRxMissedErrors=channelExternalRxMissedErrors, channelInternalRxBytes=channelInternalRxBytes, channelRxFrameErrors=channelRxFrameErrors, channelInternalTxAborted=channelInternalTxAborted, channelexternalNegotiatedMediaTime=channelexternalNegotiatedMediaTime, PYSNMP_MODULE_ID=channelstats, channelInternalCollisions=channelInternalCollisions, channelRxMissedErrors=channelRxMissedErrors, channelInternalRxLengthErrors=channelInternalRxLengthErrors, channelTxDrops=channelTxDrops, channelExternalTxErrors=channelExternalTxErrors, channelExternalRxPackets=channelExternalRxPackets, channelExternalRxBytes=channelExternalRxBytes, channelstats=channelstats, channelExternalRxFifoErrors=channelExternalRxFifoErrors, channelInternalRxMissedErrors=channelInternalRxMissedErrors, channelExternalTxBytes=channelExternalTxBytes, channelInfoTable=channelInfoTable, channelTxErrors=channelTxErrors, channelInternalNegotiatedMedia=channelInternalNegotiatedMedia, channelRxCrcErrors=channelRxCrcErrors, channelTxPackets=channelTxPackets, channelRxDrops=channelRxDrops, channelTxAborted=channelTxAborted, channelExternalRxDrops=channelExternalRxDrops, channelCollisions=channelCollisions, channelNumber=channelNumber, channelInternalTxErrors=channelInternalTxErrors, netDeviceEntry=netDeviceEntry, channelName=channelName, channelExternalRxLengthErrors=channelExternalRxLengthErrors, channelInternalRxPackets=channelInternalRxPackets, channelExternalRxErrors=channelExternalRxErrors, channelTxCarrierErrors=channelTxCarrierErrors, channelTxWindowErrors=channelTxWindowErrors, channelExternalTxWindowErrors=channelExternalTxWindowErrors, channelTxBytes=channelTxBytes, channelRxErrors=channelRxErrors, channelExternalRxCrcErrors=channelExternalRxCrcErrors, channelExternalTxDrops=channelExternalTxDrops, channelInternalTxCarrierErrors=channelInternalTxCarrierErrors, channelInternalNegotiatedMediaTime=channelInternalNegotiatedMediaTime)
