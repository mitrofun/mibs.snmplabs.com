#
# PySNMP MIB module JUNIPER-JS-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-NAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressIPv4, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressType", "InetAddress")
jnxJsNAT, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsNAT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, IpAddress, Gauge32, Counter32, Counter64, iso, NotificationType, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "IpAddress", "Gauge32", "Counter32", "Counter64", "iso", "NotificationType", "Integer32", "Unsigned32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
jnxJsNatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1))
jnxJsNatMIB.setRevisions(('2007-04-13 20:22', '2012-03-01 11:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJsNatMIB.setRevisionsDescriptions(('Creation Date', 'Deprecated jnxJsNatRuleTransHits and jnxJsNatPoolTransHits, added jnxJsNatRuleHits and jnxJsNatPoolHits.',))
if mibBuilder.loadTexts: jnxJsNatMIB.setLastUpdated('201203011122Z')
if mibBuilder.loadTexts: jnxJsNatMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsNatMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxJsNatMIB.setDescription('This module defines the object that are used to monitor network address translation attributes.')
jnxJsNatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0))
jnxJsNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1))
jnxJsNatTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2))
jnxJsSrcNatNumOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSrcNatNumOfEntries.setStatus('current')
if mibBuilder.loadTexts: jnxJsSrcNatNumOfEntries.setDescription('Total number of dynamic addresses being translated. jnxJsSrcNatNumOfEntries provides the total number of entries in the jnxJsSrcNatTable. ')
jnxJsSrcNatTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2), )
if mibBuilder.loadTexts: jnxJsSrcNatTable.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsSrcNatTable.setDescription('This table exposes the source NAT translation attributes of the translated addresses. When performing source IP address translation, the device translates the original source IP address and/or port number to different one. The resource, address source pools provide the security device with a supply of addresses from which to draw when performing source network address translation. The security device has the following types of source pools: - source pool with PAT (Port Address Translation) - source pool without PAT - Static Source Pool This table contains information on source IP address translation only.')
jnxJsSrcNatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcIpPoolName"), (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcGlobalAddr"))
if mibBuilder.loadTexts: jnxJsSrcNatEntry.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsSrcNatEntry.setDescription('Source NAT address entries. It is indexed by the address pool table and the address allocated. ')
jnxJsNatSrcIpPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsNatSrcIpPoolName.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcIpPoolName.setDescription('The name of dynamic source IP address pool. This is the address pool where the translated address is allocated from. ')
jnxJsNatSrcGlobalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 2), InetAddressIPv4())
if mibBuilder.loadTexts: jnxJsNatSrcGlobalAddr.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcGlobalAddr.setDescription('The name of dynamic source IP address allocated from the address pool used in the NAT translation. ')
jnxJsNatSrcPortPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("withPAT", 1), ("withoutPAT", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcPortPoolType.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcPortPoolType.setDescription('Source NAT can do address translation with or without port address translation (PAT). The source port pool type indicates whether the address translation is done with port or without the port, or if it is a static translation. withPAT(Source Pool with PAT): the security device translates both source IP address and port number of the packets withoutPAT (Source Pool without PAT): the device performs source network address translation for the IP address without performing port address translation (PAT) for the source port number. Static translation means that one range of IP addresses is statically mapped one to one to a shifted range of IP addresses. ')
jnxJsNatSrcNumOfPortInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcNumOfPortInuse.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcNumOfPortInuse.setDescription('The number of ports in use for this NAT address entry. This attribute is only applicable to NAT translation with PAT.')
jnxJsNatSrcNumOfSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcNumOfSessions.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcNumOfSessions.setDescription('The number of sessions are in use based on this NAT address entry. This attribute is only applicable to NAT translation without PAT.')
jnxJsNatSrcAssocatedIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcAssocatedIf.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatSrcAssocatedIf.setDescription('The index of interface associated with this NAT address entry. This is an unique value, greater than zero, for each interface.')
jnxJsNatIfSrcPoolPortTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3), )
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolPortTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolPortTable.setDescription('This table monitors the port usage of the NAT interface source IP address pool. Interface source pool is pre-defined. This source pool is referenced in a policy it is configured. The security device translates the source IP address to the address of the egress interface for the traffic matching a policy which references interface source pool. The security device always applies port address translation (PAT) for interface source pool. ')
jnxJsNatIfSrcPoolPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1), ).setIndexNames((0, "JUNIPER-JS-NAT-MIB", "jnxJsNatIfSrcPoolIndex"))
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolPortEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolPortEntry.setDescription('Source NAT address entries. It is indexed by the address pool table and the address. ')
jnxJsNatIfSrcPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolIndex.setDescription('The index of the port pool of this address pool.')
jnxJsNatIfSrcPoolTotalSinglePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolTotalSinglePorts.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolTotalSinglePorts.setDescription('The total number of single ports in a port pool.')
jnxJsNatIfSrcPoolAllocSinglePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolAllocSinglePorts.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolAllocSinglePorts.setDescription('The number of single ports in a port pool allocated or inuse.')
jnxJsNatIfSrcPoolTotalTwinPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolTotalTwinPorts.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolTotalTwinPorts.setDescription('The total number of twin ports in a port pool.')
jnxJsNatIfSrcPoolAllocTwinPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolAllocTwinPorts.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatIfSrcPoolAllocTwinPorts.setDescription('The number of twin ports in a port pool allocated or inuse.')
jnxJsSrcNatStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4), )
if mibBuilder.loadTexts: jnxJsSrcNatStatsTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsSrcNatStatsTable.setDescription('This table exposes the source NAT translation attributes of the translated addresses. When performing source IP address translation, the device translates the original source IP address and/or port number to different one. The resource, address source pools provide the security device with a supply of addresses from which to draw when performing source network address translation. The security device has the following types of source pools: - source pool with PAT (Port Address Translation) - source pool without PAT - Static Source Pool This table contains information on source IP address translation only.')
jnxJsSrcNatStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1), ).setIndexNames((0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcPoolName"), (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcXlatedAddrType"), (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcXlatedAddr"))
if mibBuilder.loadTexts: jnxJsSrcNatStatsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsSrcNatStatsEntry.setDescription('Source NAT address entries. It is indexed by the address pool table and the address allocated. ')
jnxJsNatSrcPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsNatSrcPoolName.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcPoolName.setDescription('The name of dynamic source IP address pool. This is the address pool where the translated address is allocated from. ')
jnxJsNatSrcXlatedAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 2), InetAddressType())
if mibBuilder.loadTexts: jnxJsNatSrcXlatedAddrType.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcXlatedAddrType.setDescription('The type of dynamic source IP address allocated from the address pool used in the NAT translation. For NAT MIB, supporting ipv4(1) and ipv6(2) only.')
jnxJsNatSrcXlatedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 3), InetAddress())
if mibBuilder.loadTexts: jnxJsNatSrcXlatedAddr.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcXlatedAddr.setDescription('The name of dynamic source IP address allocated from the address pool used in the NAT translation. For NAT MIB, supporting IPv4 and IPv6 address only. ')
jnxJsNatSrcPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("withPAT", 1), ("withoutPAT", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcPoolType.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcPoolType.setDescription('Source NAT can do address translation with or without port address translation (PAT). The source port pool type indicates whether the address translation is done with port or without the port, or if it is a static translation. withPAT(Source Pool with PAT): the security device translates both source IP address and port number of the packets withoutPAT (Source Pool without PAT): the device performs source network address translation for the IP address without performing port address translation (PAT) for the source port number. Static translation means that one range of IP addresses is statically mapped one to one to a shifted range of IP addresses. ')
jnxJsNatSrcNumPortInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcNumPortInuse.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcNumPortInuse.setDescription('The number of ports in use for this NAT address entry. This attribute is only applicable to NAT translation with PAT.')
jnxJsNatSrcNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatSrcNumSessions.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatSrcNumSessions.setDescription('The number of sessions are in use based on this NAT address entry. This attribute is only applicable to NAT translation without PAT.')
jnxJsNatRuleTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5), )
if mibBuilder.loadTexts: jnxJsNatRuleTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatRuleTable.setDescription('This table monitors NAT rule hits ')
jnxJsNatRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1), ).setIndexNames((0, "JUNIPER-JS-NAT-MIB", "jnxJsNatRuleName"), (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatRuleType"))
if mibBuilder.loadTexts: jnxJsNatRuleEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatRuleEntry.setDescription('NAT rule hit entries. It is indexed by the rule index')
jnxJsNatRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatRuleName.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatRuleName.setDescription('NAT rule name')
jnxJsNatRuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("destination", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatRuleType.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatRuleType.setDescription('NAT types: Source, Destination and Static')
jnxJsNatRuleTransHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatRuleTransHits.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatRuleTransHits.setDescription('The number of hits on this NAT rule, Deprecated to avoid negative value.')
jnxJsNatRuleHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatRuleHits.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatRuleHits.setDescription('The number of hits on this NAT rule to deprecate jnxJsNatRuleTransHits')
jnxJsNatPoolTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6), )
if mibBuilder.loadTexts: jnxJsNatPoolTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatPoolTable.setDescription('This table monitors NAT pool hits ')
jnxJsNatPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1), ).setIndexNames((0, "JUNIPER-JS-NAT-MIB", "jnxJsNatPoolName"), (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatPoolType"))
if mibBuilder.loadTexts: jnxJsNatPoolEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatPoolEntry.setDescription('NAT pool hit entries. It is indexed by the pool index')
jnxJsNatPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatPoolName.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatPoolName.setDescription('NAT Pool name')
jnxJsNatPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("destination", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatPoolType.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatPoolType.setDescription('NAT types: Source, Destination and Static')
jnxJsNatPoolTransHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatPoolTransHits.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatPoolTransHits.setDescription('The number of hits on this NAT Pool, Deprecated to avoid negative value.')
jnxJsNatPoolHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNatPoolHits.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatPoolHits.setDescription('The number of hits on this NAT Pool to deprecate jnxJsNatPoolTransHits.')
jnxJsNatAddrPoolThresholdStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0, 1)).setObjects(("JUNIPER-JS-NAT-MIB", "jnxJsNatSrcIpPoolName"), ("JUNIPER-JS-NAT-MIB", "jnxJsNatAddrPoolUtil"))
if mibBuilder.loadTexts: jnxJsNatAddrPoolThresholdStatus.setStatus('deprecated')
if mibBuilder.loadTexts: jnxJsNatAddrPoolThresholdStatus.setDescription('The NAT address pool untilization threshold status trap signifies that the address pool utilization is either exceeds certain percentage, or clear of that percentage. jnxJsNatSrcIpPoolName is the name of the resource pool jnxJsNatAddrPoolUtil is the percentage of utilization of the address pool.')
jnxJsNatAddrPoolUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsNatAddrPoolUtil.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatAddrPoolUtil.setDescription('The dynamic address pool utilization in percentage.')
jnxJsNatTrapPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsNatTrapPoolName.setStatus('current')
if mibBuilder.loadTexts: jnxJsNatTrapPoolName.setDescription('Source NAT Pool name who issues trap')
jnxJsSrcNatPoolThresholdStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0, 2)).setObjects(("JUNIPER-JS-NAT-MIB", "jnxJsNatTrapPoolName"), ("JUNIPER-JS-NAT-MIB", "jnxJsNatAddrPoolUtil"))
if mibBuilder.loadTexts: jnxJsSrcNatPoolThresholdStatus.setStatus('current')
if mibBuilder.loadTexts: jnxJsSrcNatPoolThresholdStatus.setDescription('The Source NAT pool untilization threshold status trap signifies that the address pool or PAT utilization is either exceeds certain percentage, or clear of that percentage. jnxJsNatTrapPoolName is the name of source pool jnxJsNatAddrPoolUtil is the percentage of utilization of the address pool.')
mibBuilder.exportSymbols("JUNIPER-JS-NAT-MIB", jnxJsSrcNatNumOfEntries=jnxJsSrcNatNumOfEntries, jnxJsNatPoolTable=jnxJsNatPoolTable, jnxJsNatRuleType=jnxJsNatRuleType, jnxJsNatObjects=jnxJsNatObjects, jnxJsNatIfSrcPoolPortEntry=jnxJsNatIfSrcPoolPortEntry, jnxJsNatSrcGlobalAddr=jnxJsNatSrcGlobalAddr, jnxJsNatTrapVars=jnxJsNatTrapVars, jnxJsSrcNatEntry=jnxJsSrcNatEntry, jnxJsNatAddrPoolThresholdStatus=jnxJsNatAddrPoolThresholdStatus, jnxJsNatPoolType=jnxJsNatPoolType, jnxJsNatIfSrcPoolPortTable=jnxJsNatIfSrcPoolPortTable, jnxJsSrcNatPoolThresholdStatus=jnxJsSrcNatPoolThresholdStatus, jnxJsNatPoolHits=jnxJsNatPoolHits, PYSNMP_MODULE_ID=jnxJsNatMIB, jnxJsNatNotifications=jnxJsNatNotifications, jnxJsNatSrcXlatedAddr=jnxJsNatSrcXlatedAddr, jnxJsNatIfSrcPoolAllocTwinPorts=jnxJsNatIfSrcPoolAllocTwinPorts, jnxJsNatMIB=jnxJsNatMIB, jnxJsNatIfSrcPoolTotalTwinPorts=jnxJsNatIfSrcPoolTotalTwinPorts, jnxJsNatSrcIpPoolName=jnxJsNatSrcIpPoolName, jnxJsNatRuleName=jnxJsNatRuleName, jnxJsNatIfSrcPoolIndex=jnxJsNatIfSrcPoolIndex, jnxJsNatSrcNumSessions=jnxJsNatSrcNumSessions, jnxJsNatSrcPortPoolType=jnxJsNatSrcPortPoolType, jnxJsNatRuleHits=jnxJsNatRuleHits, jnxJsSrcNatStatsTable=jnxJsSrcNatStatsTable, jnxJsNatAddrPoolUtil=jnxJsNatAddrPoolUtil, jnxJsSrcNatStatsEntry=jnxJsSrcNatStatsEntry, jnxJsNatSrcPoolName=jnxJsNatSrcPoolName, jnxJsNatPoolEntry=jnxJsNatPoolEntry, jnxJsNatIfSrcPoolTotalSinglePorts=jnxJsNatIfSrcPoolTotalSinglePorts, jnxJsNatRuleTable=jnxJsNatRuleTable, jnxJsNatRuleTransHits=jnxJsNatRuleTransHits, jnxJsNatPoolTransHits=jnxJsNatPoolTransHits, jnxJsSrcNatTable=jnxJsSrcNatTable, jnxJsNatSrcXlatedAddrType=jnxJsNatSrcXlatedAddrType, jnxJsNatSrcNumOfPortInuse=jnxJsNatSrcNumOfPortInuse, jnxJsNatPoolName=jnxJsNatPoolName, jnxJsNatSrcNumOfSessions=jnxJsNatSrcNumOfSessions, jnxJsNatSrcPoolType=jnxJsNatSrcPoolType, jnxJsNatIfSrcPoolAllocSinglePorts=jnxJsNatIfSrcPoolAllocSinglePorts, jnxJsNatSrcAssocatedIf=jnxJsNatSrcAssocatedIf, jnxJsNatRuleEntry=jnxJsNatRuleEntry, jnxJsNatTrapPoolName=jnxJsNatTrapPoolName, jnxJsNatSrcNumPortInuse=jnxJsNatSrcNumPortInuse)
