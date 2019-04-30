#
# PySNMP MIB module FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
IndexInteger, diffServMeterEntry, IfDirection, IndexIntegerNextFree = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "diffServMeterEntry", "IfDirection", "IndexIntegerNextFree")
fastPathQOS, = mibBuilder.importSymbols("FASTPATH-QOS-MIB", "fastPathQOS")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, ObjectIdentity, NotificationType, Counter64, TimeTicks, Gauge32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "TimeTicks", "Gauge32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Unsigned32", "Counter32")
TextualConvention, StorageType, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "MacAddress", "DisplayString")
fastPathQOSDiffServExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6))
fastPathQOSDiffServExtensions.setRevisions(('2007-05-23 00:00', '2004-06-30 00:00', '2003-11-21 00:00', '2001-11-01 09:33',))
if mibBuilder.loadTexts: fastPathQOSDiffServExtensions.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathQOSDiffServExtensions.setOrganization('Netgear')
class IpPrecedence(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class Cos(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class CosOrAny(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class VlanIdOrAny(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4094), )
class EtypeOrAny(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1536, 65535), )
agentDiffServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1))
agentDiffServMIBAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2))
agentDiffServClassifier = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1))
agentDiffServAuxMfClfrNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 1), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrNextFree.setStatus('current')
agentDiffServAuxMfClfrTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2), )
if mibBuilder.loadTexts: agentDiffServAuxMfClfrTable.setStatus('current')
agentDiffServAuxMfClfrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServAuxMfClfrId"))
if mibBuilder.loadTexts: agentDiffServAuxMfClfrEntry.setStatus('current')
agentDiffServAuxMfClfrId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 1), IndexInteger())
if mibBuilder.loadTexts: agentDiffServAuxMfClfrId.setStatus('current')
agentDiffServAuxMfClfrDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstAddr.setStatus('current')
agentDiffServAuxMfClfrDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstMask.setStatus('current')
agentDiffServAuxMfClfrSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcAddr.setStatus('current')
agentDiffServAuxMfClfrSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcMask.setStatus('current')
agentDiffServAuxMfClfrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrProtocol.setStatus('current')
agentDiffServAuxMfClfrDstL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstL4PortMin.setStatus('current')
agentDiffServAuxMfClfrDstL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 8), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstL4PortMax.setStatus('current')
agentDiffServAuxMfClfrSrcL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 9), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcL4PortMin.setStatus('current')
agentDiffServAuxMfClfrSrcL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 10), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcL4PortMax.setStatus('current')
agentDiffServAuxMfClfrCos = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 11), CosOrAny().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrCos.setStatus('current')
agentDiffServAuxMfClfrTos = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrTos.setStatus('current')
agentDiffServAuxMfClfrTosMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrTosMask.setStatus('current')
agentDiffServAuxMfClfrDstMac = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 14), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstMac.setStatus('current')
agentDiffServAuxMfClfrDstMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 15), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrDstMacMask.setStatus('current')
agentDiffServAuxMfClfrSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 16), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcMac.setStatus('current')
agentDiffServAuxMfClfrSrcMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 17), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrSrcMacMask.setStatus('current')
agentDiffServAuxMfClfrVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 18), VlanIdOrAny().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrVlanId.setStatus('obsolete')
agentDiffServAuxMfClfrStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 19), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrStorage.setStatus('current')
agentDiffServAuxMfClfrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrStatus.setStatus('current')
agentDiffServAuxMfClfrCos2 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 21), CosOrAny().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrCos2.setStatus('current')
agentDiffServAuxMfClfrEtypeVal1 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 22), EtypeOrAny()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrEtypeVal1.setStatus('current')
agentDiffServAuxMfClfrEtypeVal2 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 23), EtypeOrAny()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrEtypeVal2.setStatus('current')
agentDiffServAuxMfClfrVlanIdMin = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrVlanIdMin.setStatus('current')
agentDiffServAuxMfClfrVlanIdMax = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(4094)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrVlanIdMax.setStatus('current')
agentDiffServAuxMfClfrVlanId2Min = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 26), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrVlanId2Min.setStatus('current')
agentDiffServAuxMfClfrVlanId2Max = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 1, 2, 1, 27), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(4094)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAuxMfClfrVlanId2Max.setStatus('current')
agentDiffServAction = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2))
agentDiffServIpPrecMarkActTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4), )
if mibBuilder.loadTexts: agentDiffServIpPrecMarkActTable.setStatus('current')
agentDiffServIpPrecMarkActEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServIpPrecMarkActPrecedence"))
if mibBuilder.loadTexts: agentDiffServIpPrecMarkActEntry.setStatus('current')
agentDiffServIpPrecMarkActPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 4, 1, 1), IpPrecedence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServIpPrecMarkActPrecedence.setStatus('current')
agentDiffServCosMarkActTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2), )
if mibBuilder.loadTexts: agentDiffServCosMarkActTable.setStatus('current')
agentDiffServCosMarkActEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServCosMarkActCos"))
if mibBuilder.loadTexts: agentDiffServCosMarkActEntry.setStatus('current')
agentDiffServCosMarkActCos = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 2, 1, 1), Cos()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServCosMarkActCos.setStatus('current')
agentDiffServCos2MarkActTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5), )
if mibBuilder.loadTexts: agentDiffServCos2MarkActTable.setStatus('current')
agentDiffServCos2MarkActEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServCos2MarkActCos"))
if mibBuilder.loadTexts: agentDiffServCos2MarkActEntry.setStatus('current')
agentDiffServCos2MarkActCos = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 5, 1, 1), Cos()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServCos2MarkActCos.setStatus('current')
agentDiffServAssignQueueNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 6), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServAssignQueueNextFree.setStatus('current')
agentDiffServAssignQueueTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7), )
if mibBuilder.loadTexts: agentDiffServAssignQueueTable.setStatus('current')
agentDiffServAssignQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServAssignQueueIndex"))
if mibBuilder.loadTexts: agentDiffServAssignQueueEntry.setStatus('current')
agentDiffServAssignQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 1), IndexInteger())
if mibBuilder.loadTexts: agentDiffServAssignQueueIndex.setStatus('current')
agentDiffServAssignQueueQnum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAssignQueueQnum.setStatus('current')
agentDiffServAssignQueueStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAssignQueueStorage.setStatus('current')
agentDiffServAssignQueueStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServAssignQueueStatus.setStatus('current')
agentDiffServRedirectNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 8), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServRedirectNextFree.setStatus('current')
agentDiffServRedirectTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9), )
if mibBuilder.loadTexts: agentDiffServRedirectTable.setStatus('current')
agentDiffServRedirectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServRedirectId"))
if mibBuilder.loadTexts: agentDiffServRedirectEntry.setStatus('current')
agentDiffServRedirectId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 1), IndexInteger())
if mibBuilder.loadTexts: agentDiffServRedirectId.setStatus('current')
agentDiffServRedirectIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServRedirectIntf.setStatus('current')
agentDiffServRedirectStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServRedirectStorage.setStatus('current')
agentDiffServRedirectStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServRedirectStatus.setStatus('current')
agentDiffServMirrorNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 10), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDiffServMirrorNextFree.setStatus('current')
agentDiffServMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11), )
if mibBuilder.loadTexts: agentDiffServMirrorTable.setStatus('current')
agentDiffServMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1), ).setIndexNames((0, "FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServMirrorId"))
if mibBuilder.loadTexts: agentDiffServMirrorEntry.setStatus('current')
agentDiffServMirrorId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 1), IndexInteger())
if mibBuilder.loadTexts: agentDiffServMirrorId.setStatus('current')
agentDiffServMirrorIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServMirrorIntf.setStatus('current')
agentDiffServMirrorStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServMirrorStorage.setStatus('current')
agentDiffServMirrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 2, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServMirrorStatus.setStatus('current')
agentDiffServMeter = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3))
agentDiffServColorAwareTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1), )
if mibBuilder.loadTexts: agentDiffServColorAwareTable.setStatus('current')
agentDiffServColorAwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1), )
diffServMeterEntry.registerAugmentions(("FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", "agentDiffServColorAwareEntry"))
agentDiffServColorAwareEntry.setIndexNames(*diffServMeterEntry.getIndexNames())
if mibBuilder.loadTexts: agentDiffServColorAwareEntry.setStatus('current')
agentDiffServColorAwareLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("conform", 1), ("exceed", 2), ("unused", 3))).clone('unused')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServColorAwareLevel.setStatus('current')
agentDiffServColorAwareMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("blind", 1), ("awarecos", 2), ("awarecos2", 3), ("awareipdscp", 4), ("awareipprec", 5), ("awareunused", 6))).clone('blind')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServColorAwareMode.setStatus('current')
agentDiffServColorAwareValue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentDiffServColorAwareValue.setStatus('current')
agentDiffServTBMeters = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2, 1))
agentDiffServTBParamSimpleTokenBucketAware = ObjectIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 6, 2, 1, 1))
if mibBuilder.loadTexts: agentDiffServTBParamSimpleTokenBucketAware.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-QOS-DIFFSERV-EXTENSIONS-MIB", agentDiffServRedirectEntry=agentDiffServRedirectEntry, agentDiffServAuxMfClfrEtypeVal1=agentDiffServAuxMfClfrEtypeVal1, agentDiffServAuxMfClfrDstMacMask=agentDiffServAuxMfClfrDstMacMask, agentDiffServMirrorNextFree=agentDiffServMirrorNextFree, agentDiffServAuxMfClfrDstMask=agentDiffServAuxMfClfrDstMask, agentDiffServAuxMfClfrCos=agentDiffServAuxMfClfrCos, agentDiffServMirrorEntry=agentDiffServMirrorEntry, agentDiffServAuxMfClfrTos=agentDiffServAuxMfClfrTos, agentDiffServAssignQueueQnum=agentDiffServAssignQueueQnum, VlanIdOrAny=VlanIdOrAny, agentDiffServCos2MarkActTable=agentDiffServCos2MarkActTable, agentDiffServRedirectTable=agentDiffServRedirectTable, agentDiffServAssignQueueTable=agentDiffServAssignQueueTable, agentDiffServMIBAdmin=agentDiffServMIBAdmin, agentDiffServAuxMfClfrDstL4PortMax=agentDiffServAuxMfClfrDstL4PortMax, agentDiffServIpPrecMarkActEntry=agentDiffServIpPrecMarkActEntry, agentDiffServAuxMfClfrCos2=agentDiffServAuxMfClfrCos2, agentDiffServAssignQueueEntry=agentDiffServAssignQueueEntry, EtypeOrAny=EtypeOrAny, agentDiffServColorAwareLevel=agentDiffServColorAwareLevel, agentDiffServAuxMfClfrVlanIdMax=agentDiffServAuxMfClfrVlanIdMax, agentDiffServColorAwareMode=agentDiffServColorAwareMode, agentDiffServAuxMfClfrSrcMask=agentDiffServAuxMfClfrSrcMask, agentDiffServTBMeters=agentDiffServTBMeters, agentDiffServAuxMfClfrDstL4PortMin=agentDiffServAuxMfClfrDstL4PortMin, agentDiffServRedirectNextFree=agentDiffServRedirectNextFree, agentDiffServMirrorId=agentDiffServMirrorId, agentDiffServCosMarkActCos=agentDiffServCosMarkActCos, agentDiffServAuxMfClfrSrcMacMask=agentDiffServAuxMfClfrSrcMacMask, agentDiffServMirrorStorage=agentDiffServMirrorStorage, agentDiffServRedirectStatus=agentDiffServRedirectStatus, agentDiffServCosMarkActEntry=agentDiffServCosMarkActEntry, agentDiffServRedirectStorage=agentDiffServRedirectStorage, agentDiffServAssignQueueIndex=agentDiffServAssignQueueIndex, agentDiffServAuxMfClfrDstAddr=agentDiffServAuxMfClfrDstAddr, agentDiffServClassifier=agentDiffServClassifier, agentDiffServAuxMfClfrVlanId2Min=agentDiffServAuxMfClfrVlanId2Min, agentDiffServAuxMfClfrId=agentDiffServAuxMfClfrId, agentDiffServMirrorStatus=agentDiffServMirrorStatus, agentDiffServRedirectIntf=agentDiffServRedirectIntf, agentDiffServAuxMfClfrTable=agentDiffServAuxMfClfrTable, agentDiffServRedirectId=agentDiffServRedirectId, agentDiffServAuxMfClfrStatus=agentDiffServAuxMfClfrStatus, agentDiffServCos2MarkActCos=agentDiffServCos2MarkActCos, agentDiffServAuxMfClfrEntry=agentDiffServAuxMfClfrEntry, agentDiffServMIBObjects=agentDiffServMIBObjects, Cos=Cos, agentDiffServIpPrecMarkActPrecedence=agentDiffServIpPrecMarkActPrecedence, agentDiffServAuxMfClfrSrcAddr=agentDiffServAuxMfClfrSrcAddr, agentDiffServAuxMfClfrVlanIdMin=agentDiffServAuxMfClfrVlanIdMin, CosOrAny=CosOrAny, agentDiffServColorAwareEntry=agentDiffServColorAwareEntry, agentDiffServAuxMfClfrSrcMac=agentDiffServAuxMfClfrSrcMac, agentDiffServMirrorIntf=agentDiffServMirrorIntf, agentDiffServCos2MarkActEntry=agentDiffServCos2MarkActEntry, agentDiffServIpPrecMarkActTable=agentDiffServIpPrecMarkActTable, agentDiffServAuxMfClfrVlanId=agentDiffServAuxMfClfrVlanId, agentDiffServAuxMfClfrEtypeVal2=agentDiffServAuxMfClfrEtypeVal2, agentDiffServAuxMfClfrProtocol=agentDiffServAuxMfClfrProtocol, agentDiffServMeter=agentDiffServMeter, agentDiffServColorAwareValue=agentDiffServColorAwareValue, fastPathQOSDiffServExtensions=fastPathQOSDiffServExtensions, agentDiffServAuxMfClfrNextFree=agentDiffServAuxMfClfrNextFree, agentDiffServAuxMfClfrVlanId2Max=agentDiffServAuxMfClfrVlanId2Max, agentDiffServMirrorTable=agentDiffServMirrorTable, agentDiffServCosMarkActTable=agentDiffServCosMarkActTable, agentDiffServAction=agentDiffServAction, agentDiffServAssignQueueStatus=agentDiffServAssignQueueStatus, agentDiffServAssignQueueNextFree=agentDiffServAssignQueueNextFree, agentDiffServAuxMfClfrStorage=agentDiffServAuxMfClfrStorage, agentDiffServTBParamSimpleTokenBucketAware=agentDiffServTBParamSimpleTokenBucketAware, agentDiffServAuxMfClfrSrcL4PortMin=agentDiffServAuxMfClfrSrcL4PortMin, agentDiffServAuxMfClfrSrcL4PortMax=agentDiffServAuxMfClfrSrcL4PortMax, agentDiffServAuxMfClfrDstMac=agentDiffServAuxMfClfrDstMac, IpPrecedence=IpPrecedence, PYSNMP_MODULE_ID=fastPathQOSDiffServExtensions, agentDiffServAuxMfClfrTosMask=agentDiffServAuxMfClfrTosMask, agentDiffServAssignQueueStorage=agentDiffServAssignQueueStorage, agentDiffServColorAwareTable=agentDiffServColorAwareTable)