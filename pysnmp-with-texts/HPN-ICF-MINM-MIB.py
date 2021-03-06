#
# PySNMP MIB module HPN-ICF-MINM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MINM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
hpnicfVsiIndex, = mibBuilder.importSymbols("HPN-ICF-VSI-MIB", "hpnicfVsiIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, TimeTicks, MibIdentifier, iso, Counter64, Gauge32, Bits, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "TimeTicks", "MibIdentifier", "iso", "Counter64", "Gauge32", "Bits", "NotificationType", "ModuleIdentity")
RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
hpnicfMinm = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107))
hpnicfMinm.setRevisions(('2009-08-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfMinm.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: hpnicfMinm.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: hpnicfMinm.setOrganization('')
if mibBuilder.loadTexts: hpnicfMinm.setContactInfo('')
if mibBuilder.loadTexts: hpnicfMinm.setDescription('802.1ah MAC-in-MAC MIB')
class HpnicfMinmEnabledStatus(TextualConvention, Integer32):
    description = 'A enumerated value which indicates the state of object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfMinmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1))
hpnicfMinmScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1))
hpnicfMinmCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1, 1), Bits().clone(namedValues=NamedValues(("reEncapsulation", 0), ("uplink", 1), ("vsiShareConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMinmCapabilities.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmCapabilities.setDescription('This object displays the MAC-in-MAC capabilities with respect to certain fields. The following values may be supported: reEncapsulation: Support for configuring re-encapsulation (denoted by hpnicfMinmVsiReEncapsulation). uplink: Support for configuring uplink (denoted by hpnicfMinmUplinkTable). vsiShareConnection: It indicates that connection entry is shared in all VSIs. hpnicfVsiIndex is meaningless and must be value 1 in hpnicfMinmConnectionTable.')
hpnicfMinmBmac = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMinmBmac.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmBmac.setDescription('A MAC address used in creating the MAC header of I-tagged frames transmitted across a Provider Backbone Bridged Network. The invalid value FF:FF:FF:FF:FF:FF indicates that this node is not supported by the device.')
hpnicfMinmVsiTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2), )
if mibBuilder.loadTexts: hpnicfMinmVsiTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmVsiTable.setDescription('A table for configuring MAC-in-MAC service instance parameter.')
hpnicfMinmVsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"))
if mibBuilder.loadTexts: hpnicfMinmVsiEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmVsiEntry.setDescription('An entry for configuring MAC-in-MAC service instance parameter.')
hpnicfMinmVsiBvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMinmVsiBvlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmVsiBvlan.setDescription('BVLAN ID. The value 65535 indicates the BVLAN has not been configured for get operation, and it indicates deleting the BVLAN configration for set operation.')
hpnicfMinmVsiReEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 2), HpnicfMinmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMinmVsiReEncapsulation.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmVsiReEncapsulation.setDescription('Whether the re-encapsulation is enabled. The reEncapsulation field of hpnicfMinmCapabilities denotes whether this node is supported.')
hpnicfMinmVsiNextAvailableLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMinmVsiNextAvailableLinkId.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmVsiNextAvailableLinkId.setDescription('Next available connection entry index for creating a connection entry. Its value ranges from 0x1 to 0xFFFFFFFF.The invalid value 0xFFFFFFFF indicates that connection entry can not be created. When the vsiShareConnection field of hpnicfMinmCapabilities is set, this node returns an invalid value if the value of hpnicfVsiIndex is not 1.')
hpnicfMinmUplinkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3), )
if mibBuilder.loadTexts: hpnicfMinmUplinkTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmUplinkTable.setDescription('A table for uplink ports of the VSI in MAC-in-MAC. The uplink field of hpnicfMinmCapabilities denotes whether this table is supported.')
hpnicfMinmUplinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfMinmUplinkEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmUplinkEntry.setDescription('An entry for uplink ports of the VSI in MAC-in-MAC.')
hpnicfMinmUplinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmUplinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmUplinkRowStatus.setDescription('Operation status of this table entry.')
hpnicfMinmConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4), )
if mibBuilder.loadTexts: hpnicfMinmConnectionTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionTable.setDescription('A table for the connection information of BMAC.')
hpnicfMinmConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"), (0, "HPN-ICF-MINM-MIB", "hpnicfMinmConnectionLinkId"))
if mibBuilder.loadTexts: hpnicfMinmConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionEntry.setDescription('An entry for the connection information of BMAC. When the vsiShareConnection field of hpnicfMinmCapabilities is set, connection entry is shared in all VSIs. hpnicfVsiIndex is meaningless and must be value 1 in hpnicfMinmConnectionTable.')
hpnicfMinmConnectionLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfMinmConnectionLinkId.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionLinkId.setDescription('Entry index when the vsiShareConnection bit of hpnicfMinmCapabilities is set(hpnicfVsiIndex is meaningless and must be value 1), else entry index in the VSI of hpnicfVsiIndex.Its value ranges from 0x1 to 0xFFFFFFFE. It should be obtained from hpnicfMinmVsiNextAvailableLinkId for create operation.')
hpnicfMinmConnectionBmac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmConnectionBmac.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionBmac.setDescription('BMAC of an connection entry.')
hpnicfMinmConnectionBvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmConnectionBvlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionBvlan.setDescription('BVLAN of an connection entry.')
hpnicfMinmConnectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmConnectionPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionPort.setDescription('Port ifindex of an connection entry.')
hpnicfMinmConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("learned", 1), ("configDynamic", 2), ("configStatic", 3), ("blackhole", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmConnectionStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionStatus.setDescription('State of an connection entry.')
hpnicfMinmConnectionAgingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aging", 1), ("noAged", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMinmConnectionAgingStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionAgingStatus.setDescription('Aging time of an connection entry.')
hpnicfMinmConnectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmConnectionRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMinmConnectionRowStatus.setDescription('Operation status of this table entry.')
mibBuilder.exportSymbols("HPN-ICF-MINM-MIB", hpnicfMinmConnectionStatus=hpnicfMinmConnectionStatus, hpnicfMinmVsiNextAvailableLinkId=hpnicfMinmVsiNextAvailableLinkId, HpnicfMinmEnabledStatus=HpnicfMinmEnabledStatus, hpnicfMinmConnectionLinkId=hpnicfMinmConnectionLinkId, hpnicfMinmVsiBvlan=hpnicfMinmVsiBvlan, hpnicfMinmConnectionPort=hpnicfMinmConnectionPort, hpnicfMinmUplinkRowStatus=hpnicfMinmUplinkRowStatus, hpnicfMinm=hpnicfMinm, hpnicfMinmConnectionBvlan=hpnicfMinmConnectionBvlan, hpnicfMinmConnectionAgingStatus=hpnicfMinmConnectionAgingStatus, hpnicfMinmConnectionEntry=hpnicfMinmConnectionEntry, hpnicfMinmBmac=hpnicfMinmBmac, hpnicfMinmConnectionBmac=hpnicfMinmConnectionBmac, hpnicfMinmVsiEntry=hpnicfMinmVsiEntry, hpnicfMinmUplinkEntry=hpnicfMinmUplinkEntry, hpnicfMinmScalarGroup=hpnicfMinmScalarGroup, hpnicfMinmVsiReEncapsulation=hpnicfMinmVsiReEncapsulation, hpnicfMinmConnectionRowStatus=hpnicfMinmConnectionRowStatus, hpnicfMinmConnectionTable=hpnicfMinmConnectionTable, hpnicfMinmVsiTable=hpnicfMinmVsiTable, hpnicfMinmUplinkTable=hpnicfMinmUplinkTable, hpnicfMinmCapabilities=hpnicfMinmCapabilities, hpnicfMinmObjects=hpnicfMinmObjects, PYSNMP_MODULE_ID=hpnicfMinm)
