#
# PySNMP MIB module MSIPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSIPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
software, microsoft = mibBuilder.importSymbols("MSFT-MIB", "software", "microsoft")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, Gauge32, Counter32, Bits, enterprises, IpAddress, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "Gauge32", "Counter32", "Bits", "enterprises", "IpAddress", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipx = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8))
ipxBase = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8, 1))
ipxInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8, 2))
ipxForwarding = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8, 3))
ipxServices = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8, 4))
ipxTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 8, 5))
class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class PhysAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ipxBaseOperState = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseOperState.setStatus('mandatory')
ipxBasePrimaryNetNumber = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 2), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBasePrimaryNetNumber.setStatus('mandatory')
ipxBaseNode = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseNode.setStatus('mandatory')
ipxBaseSysName = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseSysName.setStatus('mandatory')
ipxBaseMaxPathSplits = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseMaxPathSplits.setStatus('mandatory')
ipxBaseIfCount = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseIfCount.setStatus('mandatory')
ipxBaseDestCount = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseDestCount.setStatus('mandatory')
ipxBaseServCount = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxBaseServCount.setStatus('mandatory')
ipxIfTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1), )
if mibBuilder.loadTexts: ipxIfTable.setStatus('mandatory')
ipxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1), ).setIndexNames((0, "MSIPX-MIB", "ipxIfIndex"))
if mibBuilder.loadTexts: ipxIfEntry.setStatus('mandatory')
ipxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfIndex.setStatus('mandatory')
ipxIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfAdminState.setStatus('mandatory')
ipxIfOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("sleeping", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfOperState.setStatus('mandatory')
ipxIfAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfAdapterIndex.setStatus('mandatory')
ipxIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfName.setStatus('mandatory')
ipxIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("lan", 2), ("wanRouter", 3), ("wanWorkstation", 4), ("internal", 5), ("personalWanRouter", 6), ("routerWorkstationDialout", 7), ("standaloneWorkstationDialout", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfType.setStatus('mandatory')
ipxIfLocalMaxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfLocalMaxPacketSize.setStatus('mandatory')
ipxIfMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfMediaType.setStatus('mandatory')
ipxIfNetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 9), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetNumber.setStatus('mandatory')
ipxIfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 10), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfMacAddress.setStatus('mandatory')
ipxIfDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfDelay.setStatus('mandatory')
ipxIfThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfThroughput.setStatus('mandatory')
ipxIfIpxWanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfIpxWanEnable.setStatus('mandatory')
ipxIfNetbiosAccept = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetbiosAccept.setStatus('mandatory')
ipxIfNetbiosDeliver = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("enabledForStaticlySeededNames", 3), ("enabledWhenOperStateUp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetbiosDeliver.setStatus('mandatory')
ipxIfInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInHdrErrors.setStatus('mandatory')
ipxIfInFilterDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInFilterDrops.setStatus('mandatory')
ipxIfInNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInNoRoutes.setStatus('mandatory')
ipxIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInDiscards.setStatus('mandatory')
ipxIfInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInDelivers.setStatus('mandatory')
ipxIfOutFilterDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfOutFilterDrops.setStatus('mandatory')
ipxIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfOutDiscards.setStatus('mandatory')
ipxIfOutDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfOutDelivers.setStatus('mandatory')
ipxIfInNetbiosPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfInNetbiosPackets.setStatus('mandatory')
ipxIfOutNetbiosPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfOutNetbiosPackets.setStatus('mandatory')
ipxDestTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1), )
if mibBuilder.loadTexts: ipxDestTable.setStatus('mandatory')
ipxDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1), ).setIndexNames((0, "MSIPX-MIB", "ipxDestNetNum"))
if mibBuilder.loadTexts: ipxDestEntry.setStatus('mandatory')
ipxDestNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 1), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestNetNum.setStatus('mandatory')
ipxDestProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("rip", 3), ("nlsp", 4), ("static", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestProtocol.setStatus('mandatory')
ipxDestTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestTicks.setStatus('mandatory')
ipxDestHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestHopCount.setStatus('mandatory')
ipxDestNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestNextHopIfIndex.setStatus('mandatory')
ipxDestNextHopMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestNextHopMacAddress.setStatus('mandatory')
ipxDestFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxDestFlags.setStatus('mandatory')
ipxStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2), )
if mibBuilder.loadTexts: ipxStaticRouteTable.setStatus('mandatory')
ipxStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1), ).setIndexNames((0, "MSIPX-MIB", "ipxStaticRouteIfIndex"), (0, "MSIPX-MIB", "ipxStaticRouteNetNum"))
if mibBuilder.loadTexts: ipxStaticRouteEntry.setStatus('mandatory')
ipxStaticRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxStaticRouteIfIndex.setStatus('mandatory')
ipxStaticRouteNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 2), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxStaticRouteNetNum.setStatus('mandatory')
ipxStaticRouteEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deleted", 1), ("created", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticRouteEntryStatus.setStatus('mandatory')
ipxStaticRouteTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticRouteTicks.setStatus('mandatory')
ipxStaticRouteHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticRouteHopCount.setStatus('mandatory')
ipxStaticRouteNextHopMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 3, 2, 1, 6), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticRouteNextHopMacAddress.setStatus('mandatory')
ipxServTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1), )
if mibBuilder.loadTexts: ipxServTable.setStatus('mandatory')
ipxServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1), ).setIndexNames((0, "MSIPX-MIB", "ipxServType"), (0, "MSIPX-MIB", "ipxServName"))
if mibBuilder.loadTexts: ipxServEntry.setStatus('mandatory')
ipxServType = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServType.setStatus('mandatory')
ipxServName = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServName.setStatus('mandatory')
ipxServProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("nlsp", 4), ("static", 5), ("sap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServProtocol.setStatus('mandatory')
ipxServNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 4), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServNetNum.setStatus('mandatory')
ipxServNode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServNode.setStatus('mandatory')
ipxServSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServSocket.setStatus('mandatory')
ipxServHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxServHopCount.setStatus('mandatory')
ipxStaticServTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2), )
if mibBuilder.loadTexts: ipxStaticServTable.setStatus('mandatory')
ipxStaticServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1), ).setIndexNames((0, "MSIPX-MIB", "ipxStaticServIfIndex"), (0, "MSIPX-MIB", "ipxStaticServType"), (0, "MSIPX-MIB", "ipxStaticServName"))
if mibBuilder.loadTexts: ipxStaticServEntry.setStatus('mandatory')
ipxStaticServIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxStaticServIfIndex.setStatus('mandatory')
ipxStaticServType = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxStaticServType.setStatus('mandatory')
ipxStaticServName = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxStaticServName.setStatus('mandatory')
ipxStaticServEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deleted", 1), ("created", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticServEntryStatus.setStatus('mandatory')
ipxStaticServNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 5), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticServNetNum.setStatus('mandatory')
ipxStaticServNode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 6), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticServNode.setStatus('mandatory')
ipxStaticServSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticServSocket.setStatus('mandatory')
ipxStaticServHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 8, 4, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxStaticServHopCount.setStatus('mandatory')
mibBuilder.exportSymbols("MSIPX-MIB", ipxIfMacAddress=ipxIfMacAddress, ipxBaseServCount=ipxBaseServCount, ipxIfMediaType=ipxIfMediaType, ipxDestNetNum=ipxDestNetNum, ipxDestNextHopMacAddress=ipxDestNextHopMacAddress, ipxStaticRouteTicks=ipxStaticRouteTicks, ipxBasePrimaryNetNumber=ipxBasePrimaryNetNumber, ipxBase=ipxBase, ipxServEntry=ipxServEntry, ipxServNetNum=ipxServNetNum, ipxStaticServSocket=ipxStaticServSocket, ipxForwarding=ipxForwarding, ipxBaseSysName=ipxBaseSysName, ipxIfOutNetbiosPackets=ipxIfOutNetbiosPackets, ipxIfOperState=ipxIfOperState, ipxStaticServType=ipxStaticServType, ipxIfNetbiosAccept=ipxIfNetbiosAccept, ipxStaticServEntry=ipxStaticServEntry, ipxIfOutFilterDrops=ipxIfOutFilterDrops, ipxIfType=ipxIfType, ipxStaticRouteIfIndex=ipxStaticRouteIfIndex, NetNumber=NetNumber, ipxDestEntry=ipxDestEntry, ipx=ipx, ipxStaticServNetNum=ipxStaticServNetNum, ipxDestFlags=ipxDestFlags, ipxIfIpxWanEnable=ipxIfIpxWanEnable, ipxIfLocalMaxPacketSize=ipxIfLocalMaxPacketSize, ipxIfInNoRoutes=ipxIfInNoRoutes, ipxServSocket=ipxServSocket, ipxIfAdminState=ipxIfAdminState, ipxBaseIfCount=ipxBaseIfCount, ipxStaticRouteNextHopMacAddress=ipxStaticRouteNextHopMacAddress, ipxStaticRouteTable=ipxStaticRouteTable, ipxIfInNetbiosPackets=ipxIfInNetbiosPackets, ipxDestTable=ipxDestTable, ipxStaticServTable=ipxStaticServTable, ipxIfInDiscards=ipxIfInDiscards, ipxStaticServNode=ipxStaticServNode, ipxBaseNode=ipxBaseNode, ipxBaseDestCount=ipxBaseDestCount, ipxIfIndex=ipxIfIndex, ipxStaticServHopCount=ipxStaticServHopCount, ipxServHopCount=ipxServHopCount, PhysAddress=PhysAddress, ipxTraps=ipxTraps, ipxDestProtocol=ipxDestProtocol, ipxIfTable=ipxIfTable, ipxServNode=ipxServNode, ipxServTable=ipxServTable, ipxIfInDelivers=ipxIfInDelivers, ipxStaticServName=ipxStaticServName, ipxBaseOperState=ipxBaseOperState, ipxServProtocol=ipxServProtocol, ipxBaseMaxPathSplits=ipxBaseMaxPathSplits, ipxIfNetbiosDeliver=ipxIfNetbiosDeliver, ipxIfAdapterIndex=ipxIfAdapterIndex, ipxStaticServEntryStatus=ipxStaticServEntryStatus, ipxDestNextHopIfIndex=ipxDestNextHopIfIndex, ipxIfNetNumber=ipxIfNetNumber, ipxDestTicks=ipxDestTicks, ipxIfDelay=ipxIfDelay, ipxIfEntry=ipxIfEntry, ipxStaticRouteEntryStatus=ipxStaticRouteEntryStatus, ipxServName=ipxServName, ipxIfThroughput=ipxIfThroughput, ipxStaticRouteEntry=ipxStaticRouteEntry, ipxIfOutDelivers=ipxIfOutDelivers, ipxIfName=ipxIfName, ipxServices=ipxServices, ipxStaticRouteHopCount=ipxStaticRouteHopCount, ipxStaticRouteNetNum=ipxStaticRouteNetNum, ipxIfOutDiscards=ipxIfOutDiscards, ipxIfInHdrErrors=ipxIfInHdrErrors, ipxDestHopCount=ipxDestHopCount, ipxIfInFilterDrops=ipxIfInFilterDrops, ipxServType=ipxServType, ipxStaticServIfIndex=ipxStaticServIfIndex, ipxInterface=ipxInterface)
