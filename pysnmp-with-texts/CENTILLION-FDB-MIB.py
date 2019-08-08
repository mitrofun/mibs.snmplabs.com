#
# PySNMP MIB module CENTILLION-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-FDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
BitField, sysConfig, PortId, StatusIndicator, CardId = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "BitField", "sysConfig", "PortId", "StatusIndicator", "CardId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Counter64, Integer32, Bits, ModuleIdentity, Unsigned32, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Counter64", "Integer32", "Bits", "ModuleIdentity", "Unsigned32", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
class FdbTypeId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("token-ring", 2), ("ethernet", 3), ("route-descriptor", 4))

class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

fdbGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22))
fdbRemoteAgingTimer = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbRemoteAgingTimer.setStatus('mandatory')
if mibBuilder.loadTexts: fdbRemoteAgingTimer.setDescription('The timeout period in seconds for aging out dynamically learned remote (off-ring) stations. The default value is 300 seconds.')
fdbTableFlush = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbTableFlush.setStatus('mandatory')
if mibBuilder.loadTexts: fdbTableFlush.setDescription('When read, this object returns a zero length string. If set, the octets describe which stations to flush. All 4 octets must be specified. The encoding of the octet string follows: octet 1: the fdb type identifier to flush, unknown (1) indicates flush any fdb type. octet 2: 0x0 to flush remote stations 0x1 to flush local stations 0x2 to flush all stations octet 3: the card number to flush, a value of 0xff will flush all cards. octet 4: the port number to flush, a value of 0xff will flush all ports.')
fdbTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3), )
if mibBuilder.loadTexts: fdbTable.setStatus('deprecated')
if mibBuilder.loadTexts: fdbTable.setDescription('This table contains fdb information for each station known to the system, one entry per station. Static stations may be created by setting fdbStatus to be valid. The index of fdbStatus will contains infomation on the station type, stationAddress, stationCard and stationPort. Entries may be subsequently modified by setting the appropriate object for the entry. Entries are deleted by clearing stationInUse.')
fdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "fdbType"), (0, "CENTILLION-FDB-MIB", "fdbAddress"), (0, "CENTILLION-FDB-MIB", "fdbCard"), (0, "CENTILLION-FDB-MIB", "fdbPort"))
if mibBuilder.loadTexts: fdbEntry.setStatus('deprecated')
if mibBuilder.loadTexts: fdbEntry.setDescription('An list of station information for each station known to the system. Static stations may be configured by properly specifying at least the fdbType, fdbAddress, fdbCard and fdbPort.')
fdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 1), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbType.setStatus('deprecated')
if mibBuilder.loadTexts: fdbType.setDescription('The type of the station. Station address are represented in the canonical form as specified by their type.')
fdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbAddress.setStatus('deprecated')
if mibBuilder.loadTexts: fdbAddress.setDescription('The fdbs physical address. The physical address is represented in the canonical form according to the corresponding stationType. If the entry is a route-descriptor type, then the physical address is in the form of ring-ring-bridge.')
fdbCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbCard.setStatus('deprecated')
if mibBuilder.loadTexts: fdbCard.setDescription('The card number through which this station is reached.')
fdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbPort.setStatus('deprecated')
if mibBuilder.loadTexts: fdbPort.setDescription('The interface through which this station is reached.')
fdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: fdbIfIndex.setDescription('The interface through which this station is reached. The value for this object identifies the instance of the ifIndex object defined in MIB-II. If no such entry exists, the value 0 may be returned.')
fdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 6), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbStatus.setStatus('deprecated')
if mibBuilder.loadTexts: fdbStatus.setDescription('This indicates the validity of the station. Stations are added by supplying the required objects as index of fdbStatus, and setting the status to valid. Static stations may be deleted by setting this object to invalid.')
fdbLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 7), BitField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbLocal.setStatus('deprecated')
if mibBuilder.loadTexts: fdbLocal.setDescription('If set, this object indicates the station is attached to a ring that is directly attached to the token ring port. This object does not apply to Ethernet stations.')
fdbStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 8), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbStatic.setStatus('deprecated')
if mibBuilder.loadTexts: fdbStatic.setDescription('Fdb is static if this bit is set.')
fdbDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 9), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbDuplicate.setStatus('deprecated')
if mibBuilder.loadTexts: fdbDuplicate.setDescription('Indicates that another fdb with the same address was learned from a different card and port.')
fdbRIFPath = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 28))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbRIFPath.setStatus('deprecated')
if mibBuilder.loadTexts: fdbRIFPath.setDescription('The RIF path to the station. The RIF Path is specified as being sourced from the system, as read from left-to-right. A RIF path is valid only for objects whose stationType is token-ring. The value may be a zero length string.')
fdbSSTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4), )
if mibBuilder.loadTexts: fdbSSTable.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSTable.setDescription('This table contains the list of user defined static stations. All the objects in this table are read-only and are intended to aid reading static station configuration.')
fdbSSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "fdbSSIndex"))
if mibBuilder.loadTexts: fdbSSEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSEntry.setDescription('This is an entry in the fdbSSTable which is indexed by fdbSSIndex. Adding to the static station list is done via fdbTable. All objects here are read-only.')
fdbSSIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSIndex.setDescription('This is the index to the static station table.')
fdbSSType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 2), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSType.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSType.setDescription('This represents the media type for this static station.')
fdbSSAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSAddress.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSAddress.setDescription('This is the MAC address for this static station.')
fdbSSCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 4), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSCard.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSCard.setDescription('This is the card where this station station is.')
fdbSSPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 5), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSPort.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSPort.setDescription('This is the port where this station station is.')
fdbSSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 6), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: fdbSSVlanId.setDescription('This is a vlan id of a vlan to which this static station belongs to.')
cnfdbTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5), )
if mibBuilder.loadTexts: cnfdbTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbTable.setDescription('This table contains fdb information for each station known to the system, one entry per station per vlan. Static stations may be created by setting fdbStatus to be valid. The index of fdbStatus will contains infomation on the station type, stationAddress, stationCard, stationPort and vlanId. Entries may be subsequently modified by setting the appropriate object for the entry. Entries are deleted by clearing stationInUse. Basically, this table is identical with the fdbTable except with fdbVlanId being introduced')
cnfdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "cnfdbType"), (0, "CENTILLION-FDB-MIB", "cnfdbAddress"), (0, "CENTILLION-FDB-MIB", "cnfdbCard"), (0, "CENTILLION-FDB-MIB", "cnfdbPort"), (0, "CENTILLION-FDB-MIB", "cnfdbVlanId"))
if mibBuilder.loadTexts: cnfdbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbEntry.setDescription('An list of station information for each station per vlan known to the system. Static stations may be configured by properly specifying at least the cnfdbType, cnfdbAddress, cnfdbCard, cnfdbPort and cnfdbVlanId.')
cnfdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 1), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbType.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbType.setDescription('The type of the station. Station address are represented in the canonical form as specified by their type.')
cnfdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbAddress.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbAddress.setDescription('The fdbs physical address. The physical address is represented in the canonical form according to the corresponding stationType. If the entry is a route-descriptor type, then the physical address is in the form of ring-ring-bridge.')
cnfdbCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbCard.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbCard.setDescription('The card number through which this station is reached.')
cnfdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbPort.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbPort.setDescription('The interface through which this station is reached.')
cnfdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 5), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbVlanId.setDescription('The vlan ID through which this station is reached.')
cnfdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbIfIndex.setDescription('The interface through which this station is reached. The value for this object identifies the instance of the ifIndex object defined in MIB-II. If no such entry exists, the value 0 may be returned.')
cnfdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 7), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbStatus.setDescription('This indicates the validity of the station. Stations are added by supplying the required objects as index of fdbStatus, and setting the status to valid. Static stations may be deleted by setting this object to invalid.')
cnfdbLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 8), BitField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbLocal.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbLocal.setDescription('If set, this object indicates the station is attached to a ring that is directly attached to the token ring port. This object does not apply to Ethernet stations.')
cnfdbStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 9), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbStatic.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbStatic.setDescription('Fdb is static if this bit is set.')
cnfdbDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 10), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbDuplicate.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbDuplicate.setDescription('Indicates that another fdb with the same address was learned from a different card and port.')
cnfdbRIFPath = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 28))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbRIFPath.setStatus('mandatory')
if mibBuilder.loadTexts: cnfdbRIFPath.setDescription('The RIF path to the station. The RIF Path is specified as being sourced from the system, as read from left-to-right. A RIF path is valid only for objects whose stationType is token-ring. The value may be a zero length string.')
mibBuilder.exportSymbols("CENTILLION-FDB-MIB", fdbIfIndex=fdbIfIndex, cnfdbDuplicate=cnfdbDuplicate, fdbTableFlush=fdbTableFlush, fdbStatic=fdbStatic, cnfdbRIFPath=cnfdbRIFPath, fdbGroup=fdbGroup, fdbSSAddress=fdbSSAddress, cnfdbStatus=cnfdbStatus, fdbSSPort=fdbSSPort, fdbSSType=fdbSSType, cnfdbEntry=cnfdbEntry, fdbEntry=fdbEntry, fdbPort=fdbPort, cnfdbTable=cnfdbTable, fdbStatus=fdbStatus, fdbRIFPath=fdbRIFPath, cnfdbIfIndex=cnfdbIfIndex, cnfdbType=cnfdbType, fdbAddress=fdbAddress, fdbDuplicate=fdbDuplicate, fdbRemoteAgingTimer=fdbRemoteAgingTimer, cnfdbVlanId=cnfdbVlanId, fdbSSEntry=fdbSSEntry, cnfdbAddress=cnfdbAddress, fdbTable=fdbTable, fdbSSIndex=fdbSSIndex, cnfdbCard=cnfdbCard, VlanId=VlanId, fdbLocal=fdbLocal, fdbSSCard=fdbSSCard, fdbCard=fdbCard, FdbTypeId=FdbTypeId, cnfdbStatic=cnfdbStatic, fdbType=fdbType, cnfdbPort=cnfdbPort, cnfdbLocal=cnfdbLocal, fdbSSTable=fdbSSTable, fdbSSVlanId=fdbSSVlanId)