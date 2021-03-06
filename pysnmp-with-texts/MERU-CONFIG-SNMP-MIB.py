#
# PySNMP MIB module MERU-CONFIG-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, Gauge32, Counter32, MibIdentifier, enterprises, Integer32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "Gauge32", "Counter32", "MibIdentifier", "enterprises", "Integer32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "Counter64")
TimeInterval, TextualConvention, MacAddress, TimeStamp, DisplayString, DateAndTime, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "MacAddress", "TimeStamp", "DisplayString", "DateAndTime", "RowStatus", "TruthValue")
mwConfigSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12))
if mibBuilder.loadTexts: mwConfigSnmp.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigSnmp.setOrganization('Meru Networks')
if mibBuilder.loadTexts: mwConfigSnmp.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: mwConfigSnmp.setDescription('This MIB defines all the managed objects used to manage the Meru WLAN SNMP Configuration infrastructure')
mwWncTrapCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2), )
if mibBuilder.loadTexts: mwWncTrapCommunityTable.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunityTable.setDescription('This object describes SNMP Trap Management ')
mwWncTrapCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1), ).setIndexNames((0, "MERU-CONFIG-SNMP-MIB", "mwWncTrapCommunityTableIndex"))
if mibBuilder.loadTexts: mwWncTrapCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunityEntry.setDescription('This object describes SNMP Trap Management ')
mwWncTrapCommunityTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwWncTrapCommunityTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunityTableIndex.setDescription('The index value of the table ')
mwWncTrapCommunitypCommunityStr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunitypCommunityStr.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunitypCommunityStr.setDescription('This object describes Trap Community')
mwWncTrapCommunityClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunityClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunityClientIpAddress.setDescription('This object describes Trap Destination IP')
mwWncTrapCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunityRowStatus.setStatus('current')
if mibBuilder.loadTexts: mwWncTrapCommunityRowStatus.setDescription('This object is used to create and delete rows in the table')
mibBuilder.exportSymbols("MERU-CONFIG-SNMP-MIB", mwWncTrapCommunityTableIndex=mwWncTrapCommunityTableIndex, mwWncTrapCommunitypCommunityStr=mwWncTrapCommunitypCommunityStr, mwWncTrapCommunityClientIpAddress=mwWncTrapCommunityClientIpAddress, mwConfigSnmp=mwConfigSnmp, mwWncTrapCommunityRowStatus=mwWncTrapCommunityRowStatus, mwWncTrapCommunityEntry=mwWncTrapCommunityEntry, PYSNMP_MODULE_ID=mwConfigSnmp, mwWncTrapCommunityTable=mwWncTrapCommunityTable)
