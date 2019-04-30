#
# PySNMP MIB module RADLAN-VRRP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-VRRP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:42:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ipSpec, = mibBuilder.importSymbols("RADLAN-IP", "ipSpec")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Gauge32, mib_2, Counter64, Unsigned32, ModuleIdentity, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Gauge32", "mib-2", "Counter64", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Bits")
TextualConvention, TimeInterval, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "RowStatus", "DisplayString")
vrrpv3OperationsEntry, vrrpv3AssociatedIpAddrEntry = mibBuilder.importSymbols("VRRPV3-MIB", "vrrpv3OperationsEntry", "vrrpv3AssociatedIpAddrEntry")
rlVrrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 26, 26))
rlVrrp.setRevisions(('2010-12-09 00:00',))
if mibBuilder.loadTexts: rlVrrp.setLastUpdated('201012090000Z')
if mibBuilder.loadTexts: rlVrrp.setOrganization('Marvell Semiconductor, Inc.')
rlVrrpv3OperationsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 26, 1), )
if mibBuilder.loadTexts: rlVrrpv3OperationsTable.setStatus('current')
rlVrrpv3OperationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1), )
vrrpv3OperationsEntry.registerAugmentions(("RADLAN-VRRP", "rlVrrpv3OperationsEntry"))
rlVrrpv3OperationsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
if mibBuilder.loadTexts: rlVrrpv3OperationsEntry.setStatus('current')
rlVrrpv3OperationsDefaultPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsDefaultPrimaryIpAddr.setStatus('current')
rlVrrpv3OperationsPrimaryIpAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsPrimaryIpAddrState.setStatus('current')
rlVrrpv3OperationsVrDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVrrpv3OperationsVrDescription.setStatus('current')
rlVrrpv3OperationsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVrrpv3OperationsAdminState.setStatus('current')
rlVrrpv3OperationsVrrpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version2and3", 1), ("version2", 2), ("version3", 3))).clone('version3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVrrpv3OperationsVrrpVersion.setStatus('current')
rlVrrpv3OperationsMasterPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsMasterPriority.setStatus('current')
rlVrrpv3OperationsMasterAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 7), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsMasterAdvInterval.setStatus('current')
rlVrrpv3OperationsMasterDownInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 8), TimeInterval()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsMasterDownInterval.setStatus('current')
rlVrrpv3OperationsSkewTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 1, 1, 9), TimeInterval()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3OperationsSkewTime.setStatus('current')
rlVrrpv3AssociatedIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 26, 2), )
if mibBuilder.loadTexts: rlVrrpv3AssociatedIpAddrTable.setStatus('current')
rlVrrpv3AssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 26, 2, 1), )
vrrpv3AssociatedIpAddrEntry.registerAugmentions(("RADLAN-VRRP", "rlVrrpv3AssociatedIpAddrEntry"))
rlVrrpv3AssociatedIpAddrEntry.setIndexNames(*vrrpv3AssociatedIpAddrEntry.getIndexNames())
if mibBuilder.loadTexts: rlVrrpv3AssociatedIpAddrEntry.setStatus('current')
rlVrrpv3AssociatedIpAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3AssociatedIpAddrState.setStatus('current')
rlVrrpv3CountersTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 26, 3), )
if mibBuilder.loadTexts: rlVrrpv3CountersTable.setStatus('current')
rlVrrpv3CountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1), ).setIndexNames((0, "RADLAN-VRRP", "rlVrrpv3CountersIfIndex"))
if mibBuilder.loadTexts: rlVrrpv3CountersEntry.setStatus('current')
rlVrrpv3CountersIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: rlVrrpv3CountersIfIndex.setStatus('current')
rlVrrpv3CountersChecksumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersChecksumErrors.setStatus('current')
rlVrrpv3CountersRcvdPacketsLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersRcvdPacketsLength.setStatus('current')
rlVrrpv3CountersIpTtlErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersIpTtlErrors.setStatus('current')
rlVrrpv3CountersRcvdInvalidTypePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersRcvdInvalidTypePackets.setStatus('current')
rlVrrpv3CountersRcvdInvalidVrrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersRcvdInvalidVrrpId.setStatus('current')
rlVrrpv3CountersProtoErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersProtoErrors.setStatus('current')
rlVrrpv3CountersAddressListErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersAddressListErrors.setStatus('current')
rlVrrpv3CountersAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersAdvIntervalErrors.setStatus('current')
rlVrrpv3CountersAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVrrpv3CountersAuthErrors.setStatus('current')
rlVrrpv3CountersRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 26, 3, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVrrpv3CountersRowStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-VRRP", rlVrrpv3OperationsAdminState=rlVrrpv3OperationsAdminState, rlVrrpv3OperationsEntry=rlVrrpv3OperationsEntry, rlVrrpv3CountersChecksumErrors=rlVrrpv3CountersChecksumErrors, rlVrrpv3OperationsTable=rlVrrpv3OperationsTable, rlVrrp=rlVrrp, rlVrrpv3OperationsMasterDownInterval=rlVrrpv3OperationsMasterDownInterval, rlVrrpv3OperationsSkewTime=rlVrrpv3OperationsSkewTime, rlVrrpv3CountersIpTtlErrors=rlVrrpv3CountersIpTtlErrors, rlVrrpv3CountersRcvdPacketsLength=rlVrrpv3CountersRcvdPacketsLength, rlVrrpv3AssociatedIpAddrTable=rlVrrpv3AssociatedIpAddrTable, rlVrrpv3AssociatedIpAddrEntry=rlVrrpv3AssociatedIpAddrEntry, rlVrrpv3OperationsPrimaryIpAddrState=rlVrrpv3OperationsPrimaryIpAddrState, rlVrrpv3OperationsVrrpVersion=rlVrrpv3OperationsVrrpVersion, rlVrrpv3CountersTable=rlVrrpv3CountersTable, rlVrrpv3OperationsMasterPriority=rlVrrpv3OperationsMasterPriority, rlVrrpv3CountersProtoErrors=rlVrrpv3CountersProtoErrors, rlVrrpv3CountersRowStatus=rlVrrpv3CountersRowStatus, rlVrrpv3CountersAddressListErrors=rlVrrpv3CountersAddressListErrors, rlVrrpv3CountersRcvdInvalidTypePackets=rlVrrpv3CountersRcvdInvalidTypePackets, rlVrrpv3CountersRcvdInvalidVrrpId=rlVrrpv3CountersRcvdInvalidVrrpId, rlVrrpv3OperationsVrDescription=rlVrrpv3OperationsVrDescription, rlVrrpv3CountersIfIndex=rlVrrpv3CountersIfIndex, rlVrrpv3OperationsDefaultPrimaryIpAddr=rlVrrpv3OperationsDefaultPrimaryIpAddr, rlVrrpv3CountersAdvIntervalErrors=rlVrrpv3CountersAdvIntervalErrors, PYSNMP_MODULE_ID=rlVrrp, rlVrrpv3CountersAuthErrors=rlVrrpv3CountersAuthErrors, rlVrrpv3OperationsMasterAdvInterval=rlVrrpv3OperationsMasterAdvInterval, rlVrrpv3AssociatedIpAddrState=rlVrrpv3AssociatedIpAddrState, rlVrrpv3CountersEntry=rlVrrpv3CountersEntry)