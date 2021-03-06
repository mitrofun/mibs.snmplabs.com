#
# PySNMP MIB module NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifCounterDiscontinuityGroup, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifCounterDiscontinuityGroup", "ifIndex")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, Counter64, Counter32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, NotificationType, Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks")
DisplayString, StorageType, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "RowStatus")
natMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 123))
natMIB.setRevisions(('2015-10-02 00:00', '2005-03-21 00:00',))
if mibBuilder.loadTexts: natMIB.setLastUpdated('201510020000Z')
if mibBuilder.loadTexts: natMIB.setOrganization('IETF Behavior Engineering for Hindrance Avoidance (BEHAVE) Working Group')
natMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 1))
class NatProtocolType(TextualConvention, Integer32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("other", 2), ("icmp", 3), ("udp", 4), ("tcp", 5))

class NatProtocolMap(TextualConvention, Bits):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    namedValues = NamedValues(("other", 0), ("icmp", 1), ("udp", 2), ("tcp", 3))

class NatAddrMapId(TextualConvention, Unsigned32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NatBindIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NatBindId(TextualConvention, Unsigned32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NatSessionId(TextualConvention, Unsigned32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NatBindMode(TextualConvention, Integer32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("addressBind", 1), ("addressPortBind", 2))

class NatAssociationType(TextualConvention, Integer32):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class NatTranslationEntity(TextualConvention, Bits):
    reference = 'RFC 7658, RFC 7659'
    status = 'deprecated'
    namedValues = NamedValues(("inboundSrcEndPoint", 0), ("outboundDstEndPoint", 1), ("inboundDstEndPoint", 2), ("outboundSrcEndPoint", 3))

natDefTimeouts = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 1, 1))
natNotifCtrl = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 1, 2))
natBindDefIdleTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natBindDefIdleTimeout.setStatus('deprecated')
natUdpDefIdleTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natUdpDefIdleTimeout.setStatus('deprecated')
natIcmpDefIdleTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natIcmpDefIdleTimeout.setStatus('deprecated')
natOtherDefIdleTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natOtherDefIdleTimeout.setStatus('deprecated')
natTcpDefIdleTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natTcpDefIdleTimeout.setStatus('deprecated')
natTcpDefNegTimeout = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natTcpDefNegTimeout.setStatus('deprecated')
natNotifThrottlingInterval = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 3600), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: natNotifThrottlingInterval.setStatus('deprecated')
natInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 3), )
if mibBuilder.loadTexts: natInterfaceTable.setStatus('deprecated')
natInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: natInterfaceEntry.setStatus('deprecated')
natInterfaceRealm = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("private", 1), ("public", 2))).clone('public')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natInterfaceRealm.setStatus('deprecated')
natInterfaceServiceType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 2), Bits().clone(namedValues=NamedValues(("basicNat", 0), ("napt", 1), ("bidirectionalNat", 2), ("twiceNat", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natInterfaceServiceType.setStatus('deprecated')
natInterfaceInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natInterfaceInTranslates.setStatus('deprecated')
natInterfaceOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natInterfaceOutTranslates.setStatus('deprecated')
natInterfaceDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natInterfaceDiscards.setStatus('deprecated')
natInterfaceStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natInterfaceStorageType.setStatus('deprecated')
natInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natInterfaceRowStatus.setStatus('deprecated')
natAddrMapTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 4), )
if mibBuilder.loadTexts: natAddrMapTable.setStatus('deprecated')
natAddrMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NAT-MIB", "natAddrMapIndex"))
if mibBuilder.loadTexts: natAddrMapEntry.setStatus('deprecated')
natAddrMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 1), NatAddrMapId())
if mibBuilder.loadTexts: natAddrMapIndex.setStatus('deprecated')
natAddrMapName = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapName.setStatus('deprecated')
natAddrMapEntryType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 3), NatAssociationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapEntryType.setStatus('deprecated')
natAddrMapTranslationEntity = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 4), NatTranslationEntity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapTranslationEntity.setStatus('deprecated')
natAddrMapLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapLocalAddrType.setStatus('deprecated')
natAddrMapLocalAddrFrom = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapLocalAddrFrom.setStatus('deprecated')
natAddrMapLocalAddrTo = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapLocalAddrTo.setStatus('deprecated')
natAddrMapLocalPortFrom = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapLocalPortFrom.setStatus('deprecated')
natAddrMapLocalPortTo = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 9), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapLocalPortTo.setStatus('deprecated')
natAddrMapGlobalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 10), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapGlobalAddrType.setStatus('deprecated')
natAddrMapGlobalAddrFrom = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapGlobalAddrFrom.setStatus('deprecated')
natAddrMapGlobalAddrTo = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapGlobalAddrTo.setStatus('deprecated')
natAddrMapGlobalPortFrom = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 13), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapGlobalPortFrom.setStatus('deprecated')
natAddrMapGlobalPortTo = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 14), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapGlobalPortTo.setStatus('deprecated')
natAddrMapProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 15), NatProtocolMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapProtocol.setStatus('deprecated')
natAddrMapInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrMapInTranslates.setStatus('deprecated')
natAddrMapOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrMapOutTranslates.setStatus('deprecated')
natAddrMapDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrMapDiscards.setStatus('deprecated')
natAddrMapAddrUsed = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrMapAddrUsed.setStatus('deprecated')
natAddrMapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 20), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapStorageType.setStatus('deprecated')
natAddrMapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: natAddrMapRowStatus.setStatus('deprecated')
natAddrBindNumberOfEntries = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindNumberOfEntries.setStatus('deprecated')
natAddrBindTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 6), )
if mibBuilder.loadTexts: natAddrBindTable.setStatus('deprecated')
natAddrBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NAT-MIB", "natAddrBindLocalAddrType"), (0, "NAT-MIB", "natAddrBindLocalAddr"))
if mibBuilder.loadTexts: natAddrBindEntry.setStatus('deprecated')
natAddrBindLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 1), InetAddressType())
if mibBuilder.loadTexts: natAddrBindLocalAddrType.setStatus('deprecated')
natAddrBindLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: natAddrBindLocalAddr.setStatus('deprecated')
natAddrBindGlobalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindGlobalAddrType.setStatus('deprecated')
natAddrBindGlobalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindGlobalAddr.setStatus('deprecated')
natAddrBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 5), NatBindId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindId.setStatus('deprecated')
natAddrBindTranslationEntity = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 6), NatTranslationEntity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindTranslationEntity.setStatus('deprecated')
natAddrBindType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 7), NatAssociationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindType.setStatus('deprecated')
natAddrBindMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 8), NatAddrMapId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindMapIndex.setStatus('deprecated')
natAddrBindSessions = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindSessions.setStatus('deprecated')
natAddrBindMaxIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindMaxIdleTime.setStatus('deprecated')
natAddrBindCurrentIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindCurrentIdleTime.setStatus('deprecated')
natAddrBindInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindInTranslates.setStatus('deprecated')
natAddrBindOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrBindOutTranslates.setStatus('deprecated')
natAddrPortBindNumberOfEntries = MibScalar((1, 3, 6, 1, 2, 1, 123, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindNumberOfEntries.setStatus('deprecated')
natAddrPortBindTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 8), )
if mibBuilder.loadTexts: natAddrPortBindTable.setStatus('deprecated')
natAddrPortBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NAT-MIB", "natAddrPortBindLocalAddrType"), (0, "NAT-MIB", "natAddrPortBindLocalAddr"), (0, "NAT-MIB", "natAddrPortBindLocalPort"), (0, "NAT-MIB", "natAddrPortBindProtocol"))
if mibBuilder.loadTexts: natAddrPortBindEntry.setStatus('deprecated')
natAddrPortBindLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: natAddrPortBindLocalAddrType.setStatus('deprecated')
natAddrPortBindLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: natAddrPortBindLocalAddr.setStatus('deprecated')
natAddrPortBindLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: natAddrPortBindLocalPort.setStatus('deprecated')
natAddrPortBindProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 4), NatProtocolType())
if mibBuilder.loadTexts: natAddrPortBindProtocol.setStatus('deprecated')
natAddrPortBindGlobalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindGlobalAddrType.setStatus('deprecated')
natAddrPortBindGlobalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindGlobalAddr.setStatus('deprecated')
natAddrPortBindGlobalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 7), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindGlobalPort.setStatus('deprecated')
natAddrPortBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 8), NatBindId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindId.setStatus('deprecated')
natAddrPortBindTranslationEntity = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 9), NatTranslationEntity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindTranslationEntity.setStatus('deprecated')
natAddrPortBindType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 10), NatAssociationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindType.setStatus('deprecated')
natAddrPortBindMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 11), NatAddrMapId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindMapIndex.setStatus('deprecated')
natAddrPortBindSessions = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindSessions.setStatus('deprecated')
natAddrPortBindMaxIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindMaxIdleTime.setStatus('deprecated')
natAddrPortBindCurrentIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindCurrentIdleTime.setStatus('deprecated')
natAddrPortBindInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindInTranslates.setStatus('deprecated')
natAddrPortBindOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natAddrPortBindOutTranslates.setStatus('deprecated')
natSessionTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 9), )
if mibBuilder.loadTexts: natSessionTable.setStatus('deprecated')
natSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NAT-MIB", "natSessionIndex"))
if mibBuilder.loadTexts: natSessionEntry.setStatus('deprecated')
natSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 1), NatSessionId())
if mibBuilder.loadTexts: natSessionIndex.setStatus('deprecated')
natSessionPrivateSrcEPBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 2), NatBindIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateSrcEPBindId.setStatus('deprecated')
natSessionPrivateSrcEPBindMode = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 3), NatBindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateSrcEPBindMode.setStatus('deprecated')
natSessionPrivateDstEPBindId = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 4), NatBindIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateDstEPBindId.setStatus('deprecated')
natSessionPrivateDstEPBindMode = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 5), NatBindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateDstEPBindMode.setStatus('deprecated')
natSessionDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionDirection.setStatus('deprecated')
natSessionUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionUpTime.setStatus('deprecated')
natSessionAddrMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 8), NatAddrMapId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionAddrMapIndex.setStatus('deprecated')
natSessionProtocolType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 9), NatProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionProtocolType.setStatus('deprecated')
natSessionPrivateAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 10), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateAddrType.setStatus('deprecated')
natSessionPrivateSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 11), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateSrcAddr.setStatus('deprecated')
natSessionPrivateSrcPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 12), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateSrcPort.setStatus('deprecated')
natSessionPrivateDstAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 13), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateDstAddr.setStatus('deprecated')
natSessionPrivateDstPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 14), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPrivateDstPort.setStatus('deprecated')
natSessionPublicAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 15), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPublicAddrType.setStatus('deprecated')
natSessionPublicSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 16), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPublicSrcAddr.setStatus('deprecated')
natSessionPublicSrcPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 17), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPublicSrcPort.setStatus('deprecated')
natSessionPublicDstAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 18), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPublicDstAddr.setStatus('deprecated')
natSessionPublicDstPort = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 19), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionPublicDstPort.setStatus('deprecated')
natSessionMaxIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 20), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionMaxIdleTime.setStatus('deprecated')
natSessionCurrentIdleTime = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 21), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionCurrentIdleTime.setStatus('deprecated')
natSessionInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionInTranslates.setStatus('deprecated')
natSessionOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natSessionOutTranslates.setStatus('deprecated')
natProtocolTable = MibTable((1, 3, 6, 1, 2, 1, 123, 1, 10), )
if mibBuilder.loadTexts: natProtocolTable.setStatus('deprecated')
natProtocolEntry = MibTableRow((1, 3, 6, 1, 2, 1, 123, 1, 10, 1), ).setIndexNames((0, "NAT-MIB", "natProtocol"))
if mibBuilder.loadTexts: natProtocolEntry.setStatus('deprecated')
natProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 1), NatProtocolType())
if mibBuilder.loadTexts: natProtocol.setStatus('deprecated')
natProtocolInTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natProtocolInTranslates.setStatus('deprecated')
natProtocolOutTranslates = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natProtocolOutTranslates.setStatus('deprecated')
natProtocolDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: natProtocolDiscards.setStatus('deprecated')
natMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 0))
natPacketDiscard = NotificationType((1, 3, 6, 1, 2, 1, 123, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: natPacketDiscard.setStatus('deprecated')
natMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 2))
natMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 2, 1))
natMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 123, 2, 2))
natConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 1)).setObjects(("NAT-MIB", "natInterfaceRealm"), ("NAT-MIB", "natInterfaceServiceType"), ("NAT-MIB", "natInterfaceStorageType"), ("NAT-MIB", "natInterfaceRowStatus"), ("NAT-MIB", "natAddrMapName"), ("NAT-MIB", "natAddrMapEntryType"), ("NAT-MIB", "natAddrMapTranslationEntity"), ("NAT-MIB", "natAddrMapLocalAddrType"), ("NAT-MIB", "natAddrMapLocalAddrFrom"), ("NAT-MIB", "natAddrMapLocalAddrTo"), ("NAT-MIB", "natAddrMapLocalPortFrom"), ("NAT-MIB", "natAddrMapLocalPortTo"), ("NAT-MIB", "natAddrMapGlobalAddrType"), ("NAT-MIB", "natAddrMapGlobalAddrFrom"), ("NAT-MIB", "natAddrMapGlobalAddrTo"), ("NAT-MIB", "natAddrMapGlobalPortFrom"), ("NAT-MIB", "natAddrMapGlobalPortTo"), ("NAT-MIB", "natAddrMapProtocol"), ("NAT-MIB", "natAddrMapStorageType"), ("NAT-MIB", "natAddrMapRowStatus"), ("NAT-MIB", "natBindDefIdleTimeout"), ("NAT-MIB", "natUdpDefIdleTimeout"), ("NAT-MIB", "natIcmpDefIdleTimeout"), ("NAT-MIB", "natOtherDefIdleTimeout"), ("NAT-MIB", "natTcpDefIdleTimeout"), ("NAT-MIB", "natTcpDefNegTimeout"), ("NAT-MIB", "natNotifThrottlingInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natConfigGroup = natConfigGroup.setStatus('deprecated')
natTranslationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 2)).setObjects(("NAT-MIB", "natAddrBindNumberOfEntries"), ("NAT-MIB", "natAddrBindGlobalAddrType"), ("NAT-MIB", "natAddrBindGlobalAddr"), ("NAT-MIB", "natAddrBindId"), ("NAT-MIB", "natAddrBindTranslationEntity"), ("NAT-MIB", "natAddrBindType"), ("NAT-MIB", "natAddrBindMapIndex"), ("NAT-MIB", "natAddrBindSessions"), ("NAT-MIB", "natAddrBindMaxIdleTime"), ("NAT-MIB", "natAddrBindCurrentIdleTime"), ("NAT-MIB", "natAddrBindInTranslates"), ("NAT-MIB", "natAddrBindOutTranslates"), ("NAT-MIB", "natAddrPortBindNumberOfEntries"), ("NAT-MIB", "natAddrPortBindGlobalAddrType"), ("NAT-MIB", "natAddrPortBindGlobalAddr"), ("NAT-MIB", "natAddrPortBindGlobalPort"), ("NAT-MIB", "natAddrPortBindId"), ("NAT-MIB", "natAddrPortBindTranslationEntity"), ("NAT-MIB", "natAddrPortBindType"), ("NAT-MIB", "natAddrPortBindMapIndex"), ("NAT-MIB", "natAddrPortBindSessions"), ("NAT-MIB", "natAddrPortBindMaxIdleTime"), ("NAT-MIB", "natAddrPortBindCurrentIdleTime"), ("NAT-MIB", "natAddrPortBindInTranslates"), ("NAT-MIB", "natAddrPortBindOutTranslates"), ("NAT-MIB", "natSessionPrivateSrcEPBindId"), ("NAT-MIB", "natSessionPrivateSrcEPBindMode"), ("NAT-MIB", "natSessionPrivateDstEPBindId"), ("NAT-MIB", "natSessionPrivateDstEPBindMode"), ("NAT-MIB", "natSessionDirection"), ("NAT-MIB", "natSessionUpTime"), ("NAT-MIB", "natSessionAddrMapIndex"), ("NAT-MIB", "natSessionProtocolType"), ("NAT-MIB", "natSessionPrivateAddrType"), ("NAT-MIB", "natSessionPrivateSrcAddr"), ("NAT-MIB", "natSessionPrivateSrcPort"), ("NAT-MIB", "natSessionPrivateDstAddr"), ("NAT-MIB", "natSessionPrivateDstPort"), ("NAT-MIB", "natSessionPublicAddrType"), ("NAT-MIB", "natSessionPublicSrcAddr"), ("NAT-MIB", "natSessionPublicSrcPort"), ("NAT-MIB", "natSessionPublicDstAddr"), ("NAT-MIB", "natSessionPublicDstPort"), ("NAT-MIB", "natSessionMaxIdleTime"), ("NAT-MIB", "natSessionCurrentIdleTime"), ("NAT-MIB", "natSessionInTranslates"), ("NAT-MIB", "natSessionOutTranslates"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natTranslationGroup = natTranslationGroup.setStatus('deprecated')
natStatsInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 3)).setObjects(("NAT-MIB", "natInterfaceInTranslates"), ("NAT-MIB", "natInterfaceOutTranslates"), ("NAT-MIB", "natInterfaceDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natStatsInterfaceGroup = natStatsInterfaceGroup.setStatus('deprecated')
natStatsProtocolGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 4)).setObjects(("NAT-MIB", "natProtocolInTranslates"), ("NAT-MIB", "natProtocolOutTranslates"), ("NAT-MIB", "natProtocolDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natStatsProtocolGroup = natStatsProtocolGroup.setStatus('deprecated')
natStatsAddrMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 5)).setObjects(("NAT-MIB", "natAddrMapInTranslates"), ("NAT-MIB", "natAddrMapOutTranslates"), ("NAT-MIB", "natAddrMapDiscards"), ("NAT-MIB", "natAddrMapAddrUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natStatsAddrMapGroup = natStatsAddrMapGroup.setStatus('deprecated')
natMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 123, 2, 1, 6)).setObjects(("NAT-MIB", "natPacketDiscard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natMIBNotificationGroup = natMIBNotificationGroup.setStatus('deprecated')
natMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 123, 2, 2, 1)).setObjects(("IF-MIB", "ifCounterDiscontinuityGroup"), ("NAT-MIB", "natConfigGroup"), ("NAT-MIB", "natTranslationGroup"), ("NAT-MIB", "natStatsInterfaceGroup"), ("NAT-MIB", "natStatsProtocolGroup"), ("NAT-MIB", "natStatsAddrMapGroup"), ("NAT-MIB", "natMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natMIBFullCompliance = natMIBFullCompliance.setStatus('deprecated')
natMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 123, 2, 2, 2)).setObjects(("IF-MIB", "ifCounterDiscontinuityGroup"), ("NAT-MIB", "natConfigGroup"), ("NAT-MIB", "natTranslationGroup"), ("NAT-MIB", "natStatsInterfaceGroup"), ("NAT-MIB", "natStatsProtocolGroup"), ("NAT-MIB", "natStatsAddrMapGroup"), ("NAT-MIB", "natMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    natMIBReadOnlyCompliance = natMIBReadOnlyCompliance.setStatus('deprecated')
mibBuilder.exportSymbols("NAT-MIB", natSessionPrivateAddrType=natSessionPrivateAddrType, natAddrPortBindId=natAddrPortBindId, natAddrBindTable=natAddrBindTable, natTranslationGroup=natTranslationGroup, natAddrPortBindLocalAddr=natAddrPortBindLocalAddr, natOtherDefIdleTimeout=natOtherDefIdleTimeout, natAddrPortBindNumberOfEntries=natAddrPortBindNumberOfEntries, natAddrPortBindTable=natAddrPortBindTable, natInterfaceOutTranslates=natInterfaceOutTranslates, natAddrPortBindProtocol=natAddrPortBindProtocol, natSessionPrivateDstPort=natSessionPrivateDstPort, natAddrBindId=natAddrBindId, NatBindMode=NatBindMode, natSessionPublicSrcPort=natSessionPublicSrcPort, natSessionPrivateSrcPort=natSessionPrivateSrcPort, natAddrPortBindGlobalPort=natAddrPortBindGlobalPort, natMIBNotifications=natMIBNotifications, natInterfaceRealm=natInterfaceRealm, natAddrPortBindLocalPort=natAddrPortBindLocalPort, NatAddrMapId=NatAddrMapId, natAddrMapAddrUsed=natAddrMapAddrUsed, natProtocolInTranslates=natProtocolInTranslates, natConfigGroup=natConfigGroup, NatSessionId=NatSessionId, natSessionTable=natSessionTable, natAddrPortBindEntry=natAddrPortBindEntry, natStatsProtocolGroup=natStatsProtocolGroup, natAddrMapGlobalAddrType=natAddrMapGlobalAddrType, natSessionDirection=natSessionDirection, natAddrBindEntry=natAddrBindEntry, natAddrMapStorageType=natAddrMapStorageType, natAddrPortBindGlobalAddr=natAddrPortBindGlobalAddr, natAddrMapIndex=natAddrMapIndex, natMIBObjects=natMIBObjects, natAddrMapGlobalPortFrom=natAddrMapGlobalPortFrom, natMIB=natMIB, NatTranslationEntity=NatTranslationEntity, natSessionProtocolType=natSessionProtocolType, natDefTimeouts=natDefTimeouts, natAddrBindGlobalAddr=natAddrBindGlobalAddr, natMIBGroups=natMIBGroups, natAddrBindGlobalAddrType=natAddrBindGlobalAddrType, natSessionPrivateSrcEPBindId=natSessionPrivateSrcEPBindId, natAddrBindType=natAddrBindType, natSessionUpTime=natSessionUpTime, natInterfaceDiscards=natInterfaceDiscards, natSessionAddrMapIndex=natSessionAddrMapIndex, natBindDefIdleTimeout=natBindDefIdleTimeout, natStatsInterfaceGroup=natStatsInterfaceGroup, natAddrBindMapIndex=natAddrBindMapIndex, natMIBReadOnlyCompliance=natMIBReadOnlyCompliance, natAddrMapProtocol=natAddrMapProtocol, natAddrBindMaxIdleTime=natAddrBindMaxIdleTime, natSessionOutTranslates=natSessionOutTranslates, natProtocolTable=natProtocolTable, natTcpDefNegTimeout=natTcpDefNegTimeout, natSessionMaxIdleTime=natSessionMaxIdleTime, NatProtocolType=NatProtocolType, natProtocolEntry=natProtocolEntry, natAddrBindLocalAddrType=natAddrBindLocalAddrType, natAddrPortBindOutTranslates=natAddrPortBindOutTranslates, natAddrPortBindGlobalAddrType=natAddrPortBindGlobalAddrType, natAddrPortBindCurrentIdleTime=natAddrPortBindCurrentIdleTime, natInterfaceEntry=natInterfaceEntry, natAddrMapTranslationEntity=natAddrMapTranslationEntity, natSessionEntry=natSessionEntry, natProtocolDiscards=natProtocolDiscards, NatAssociationType=NatAssociationType, natInterfaceStorageType=natInterfaceStorageType, natSessionPublicSrcAddr=natSessionPublicSrcAddr, natAddrMapLocalAddrType=natAddrMapLocalAddrType, natAddrMapOutTranslates=natAddrMapOutTranslates, natMIBCompliances=natMIBCompliances, natAddrMapInTranslates=natAddrMapInTranslates, natInterfaceRowStatus=natInterfaceRowStatus, NatProtocolMap=NatProtocolMap, natUdpDefIdleTimeout=natUdpDefIdleTimeout, natAddrMapGlobalAddrTo=natAddrMapGlobalAddrTo, natAddrMapDiscards=natAddrMapDiscards, natInterfaceServiceType=natInterfaceServiceType, natAddrMapLocalAddrFrom=natAddrMapLocalAddrFrom, natAddrMapName=natAddrMapName, natSessionInTranslates=natSessionInTranslates, natSessionPrivateSrcAddr=natSessionPrivateSrcAddr, natAddrBindTranslationEntity=natAddrBindTranslationEntity, NatBindIdOrZero=NatBindIdOrZero, natAddrBindNumberOfEntries=natAddrBindNumberOfEntries, natAddrPortBindTranslationEntity=natAddrPortBindTranslationEntity, natAddrBindInTranslates=natAddrBindInTranslates, natInterfaceTable=natInterfaceTable, natMIBConformance=natMIBConformance, natAddrMapTable=natAddrMapTable, natSessionPublicAddrType=natSessionPublicAddrType, natMIBFullCompliance=natMIBFullCompliance, natMIBNotificationGroup=natMIBNotificationGroup, natAddrPortBindType=natAddrPortBindType, natSessionIndex=natSessionIndex, natInterfaceInTranslates=natInterfaceInTranslates, natProtocolOutTranslates=natProtocolOutTranslates, natAddrPortBindLocalAddrType=natAddrPortBindLocalAddrType, natIcmpDefIdleTimeout=natIcmpDefIdleTimeout, natAddrPortBindSessions=natAddrPortBindSessions, natPacketDiscard=natPacketDiscard, natSessionCurrentIdleTime=natSessionCurrentIdleTime, natAddrMapGlobalAddrFrom=natAddrMapGlobalAddrFrom, natStatsAddrMapGroup=natStatsAddrMapGroup, natSessionPublicDstAddr=natSessionPublicDstAddr, natAddrMapLocalPortTo=natAddrMapLocalPortTo, natAddrBindCurrentIdleTime=natAddrBindCurrentIdleTime, NatBindId=NatBindId, natAddrBindOutTranslates=natAddrBindOutTranslates, natNotifThrottlingInterval=natNotifThrottlingInterval, natSessionPublicDstPort=natSessionPublicDstPort, natAddrPortBindMaxIdleTime=natAddrPortBindMaxIdleTime, PYSNMP_MODULE_ID=natMIB, natSessionPrivateDstEPBindMode=natSessionPrivateDstEPBindMode, natAddrBindSessions=natAddrBindSessions, natAddrMapEntryType=natAddrMapEntryType, natAddrBindLocalAddr=natAddrBindLocalAddr, natAddrMapGlobalPortTo=natAddrMapGlobalPortTo, natAddrMapEntry=natAddrMapEntry, natAddrPortBindInTranslates=natAddrPortBindInTranslates, natTcpDefIdleTimeout=natTcpDefIdleTimeout, natSessionPrivateDstAddr=natSessionPrivateDstAddr, natAddrMapRowStatus=natAddrMapRowStatus, natNotifCtrl=natNotifCtrl, natSessionPrivateSrcEPBindMode=natSessionPrivateSrcEPBindMode, natSessionPrivateDstEPBindId=natSessionPrivateDstEPBindId, natProtocol=natProtocol, natAddrMapLocalAddrTo=natAddrMapLocalAddrTo, natAddrMapLocalPortFrom=natAddrMapLocalPortFrom, natAddrPortBindMapIndex=natAddrPortBindMapIndex)
