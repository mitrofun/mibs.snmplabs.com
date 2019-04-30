#
# PySNMP MIB module DNOS-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-LOOPBACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InetAddressIPv4, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, NotificationType, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, mib_2, Bits, Counter32, Integer32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "mib-2", "Bits", "Counter32", "Integer32", "MibIdentifier", "TimeTicks")
DisplayString, TruthValue, TextualConvention, PhysAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "PhysAddress", "RowStatus")
fastPathLoopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22))
fastPathLoopback.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathLoopback.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLoopback.setOrganization('Dell, Inc.')
agentLoopbackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1))
agentLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackTable.setStatus('current')
agentLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1), ).setIndexNames((0, "DNOS-LOOPBACK-MIB", "agentLoopbackID"))
if mibBuilder.loadTexts: agentLoopbackEntry.setStatus('current')
agentLoopbackID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: agentLoopbackID.setStatus('current')
agentLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLoopbackIfIndex.setStatus('current')
agentLoopbackIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 3), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPAddress.setStatus('current')
agentLoopbackIPSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPSubnet.setStatus('current')
agentLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackStatus.setStatus('current')
mibBuilder.exportSymbols("DNOS-LOOPBACK-MIB", agentLoopbackStatus=agentLoopbackStatus, agentLoopbackIPSubnet=agentLoopbackIPSubnet, agentLoopbackIPAddress=agentLoopbackIPAddress, fastPathLoopback=fastPathLoopback, agentLoopbackEntry=agentLoopbackEntry, PYSNMP_MODULE_ID=fastPathLoopback, agentLoopbackTable=agentLoopbackTable, agentLoopbackID=agentLoopbackID, agentLoopbackGroup=agentLoopbackGroup, agentLoopbackIfIndex=agentLoopbackIfIndex)