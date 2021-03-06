#
# PySNMP MIB module BASP-Statistics-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BASP-Statistics-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Integer32, TimeTicks, NotificationType, ObjectIdentity, Counter64, iso, Counter32, enterprises, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter64", "iso", "Counter32", "enterprises", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTeamStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1))
baspPhyAdapterStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2))
baspVirAdapterStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3))
btsTeamNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsTeamNumber.setStatus('mandatory')
btsTeamTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2), )
if mibBuilder.loadTexts: btsTeamTable.setStatus('mandatory')
btsTeamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1), ).setIndexNames((0, "BASP-Statistics-MIB", "btsTeamIndex"))
if mibBuilder.loadTexts: btsTeamEntry.setStatus('mandatory')
btsTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsTeamIndex.setStatus('mandatory')
btsTeamName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsTeamName.setStatus('mandatory')
btsPhyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPhyNumber.setStatus('mandatory')
btsVirNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsVirNumber.setStatus('mandatory')
btsPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSends.setStatus('mandatory')
btsPacketSendDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSendDiscardeds.setStatus('mandatory')
btsPacketSendQueueds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSendQueueds.setStatus('mandatory')
btsPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketRecvs.setStatus('mandatory')
btsPacketRecvDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketRecvDiscardeds.setStatus('mandatory')
btsLinkPacketsSents = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsLinkPacketsSents.setStatus('mandatory')
btsLinkPacketsRetrieds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsLinkPacketsRetrieds.setStatus('mandatory')
btsPhyAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPhyAdapterNumber.setStatus('mandatory')
btsPhyAdapterStatTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2), )
if mibBuilder.loadTexts: btsPhyAdapterStatTable.setStatus('mandatory')
btsPhyAdapterStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1), ).setIndexNames((0, "BASP-Statistics-MIB", "btspTeamIndex"), (0, "BASP-Statistics-MIB", "btspAdapterIndex"))
if mibBuilder.loadTexts: btsPhyAdapterStatEntry.setStatus('mandatory')
btspTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btspTeamIndex.setStatus('mandatory')
btspAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btspAdapterIndex.setStatus('mandatory')
btspAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspAdapterDesc.setStatus('mandatory')
btspPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketSends.setStatus('mandatory')
btspPacketSendDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketSendDiscardeds.setStatus('mandatory')
btspPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketRecvs.setStatus('mandatory')
btspPacketRecvDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketRecvDiscardeds.setStatus('mandatory')
btspLinkPacketsSents = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspLinkPacketsSents.setStatus('mandatory')
btspLinkPacketsRetrieds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspLinkPacketsRetrieds.setStatus('mandatory')
btsVirAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsVirAdapterNumber.setStatus('mandatory')
btsVirAdapterStatTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2), )
if mibBuilder.loadTexts: btsVirAdapterStatTable.setStatus('mandatory')
btsVirAdapterStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1), ).setIndexNames((0, "BASP-Statistics-MIB", "btsvTeamIndex"), (0, "BASP-Statistics-MIB", "btsvAdapterIndex"))
if mibBuilder.loadTexts: btsVirAdapterStatEntry.setStatus('mandatory')
btsvTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsvTeamIndex.setStatus('mandatory')
btsvAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsvAdapterIndex.setStatus('mandatory')
btsvAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvAdapterDesc.setStatus('mandatory')
btsvPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketSends.setStatus('mandatory')
btsvPacketSendQueueds = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketSendQueueds.setStatus('mandatory')
btsvPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketRecvs.setStatus('mandatory')
mibBuilder.exportSymbols("BASP-Statistics-MIB", baspVirAdapterStat=baspVirAdapterStat, baspPhyAdapterStat=baspPhyAdapterStat, btsPhyNumber=btsPhyNumber, btsPacketSendQueueds=btsPacketSendQueueds, btsvAdapterDesc=btsvAdapterDesc, btsLinkPacketsSents=btsLinkPacketsSents, btspPacketRecvs=btspPacketRecvs, btsTeamName=btsTeamName, btsVirAdapterStatTable=btsVirAdapterStatTable, baspTeamStat=baspTeamStat, btsVirNumber=btsVirNumber, btsvPacketSends=btsvPacketSends, btspTeamIndex=btspTeamIndex, btspLinkPacketsRetrieds=btspLinkPacketsRetrieds, btsVirAdapterStatEntry=btsVirAdapterStatEntry, enet=enet, btspAdapterDesc=btspAdapterDesc, basp=basp, btsTeamTable=btsTeamTable, btsPhyAdapterStatTable=btsPhyAdapterStatTable, broadcom=broadcom, btsTeamEntry=btsTeamEntry, btspPacketSends=btspPacketSends, btsPacketSends=btsPacketSends, btsvAdapterIndex=btsvAdapterIndex, btspAdapterIndex=btspAdapterIndex, btsvPacketRecvs=btsvPacketRecvs, btsPhyAdapterStatEntry=btsPhyAdapterStatEntry, btsTeamNumber=btsTeamNumber, btsLinkPacketsRetrieds=btsLinkPacketsRetrieds, baspStat=baspStat, btsTeamIndex=btsTeamIndex, btsPhyAdapterNumber=btsPhyAdapterNumber, btspPacketRecvDiscardeds=btspPacketRecvDiscardeds, btspLinkPacketsSents=btspLinkPacketsSents, btsVirAdapterNumber=btsVirAdapterNumber, btspPacketSendDiscardeds=btspPacketSendDiscardeds, btsvTeamIndex=btsvTeamIndex, btsvPacketSendQueueds=btsvPacketSendQueueds, btsPacketRecvs=btsPacketRecvs, btsPacketSendDiscardeds=btsPacketSendDiscardeds, btsPacketRecvDiscardeds=btsPacketRecvDiscardeds)
