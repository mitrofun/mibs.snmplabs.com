#
# PySNMP MIB module BROCADE-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
brcdQos, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "brcdQos")
PortPriorityTC, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "PortPriorityTC")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Gauge32, Counter32, ModuleIdentity, ObjectIdentity, TimeTicks, iso, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "iso", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brcdQosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1))
brcdQosMIB.setRevisions(('2012-07-18 00:00',))
if mibBuilder.loadTexts: brcdQosMIB.setLastUpdated('201207180000Z')
if mibBuilder.loadTexts: brcdQosMIB.setOrganization('Brocade Communications Systems, Inc.')
brcdHqosObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1))
brcdHqosStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1), )
if mibBuilder.loadTexts: brcdHqosStatsTable.setStatus('current')
brcdHqosStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1), ).setIndexNames((0, "BROCADE-QOS-MIB", "brcdHqosIfIndex"), (0, "BROCADE-QOS-MIB", "brcdHqosEndpointType"), (0, "BROCADE-QOS-MIB", "brcdHqosEndpointTag"), (0, "BROCADE-QOS-MIB", "brcdHqosEndpointInnerTag"), (0, "BROCADE-QOS-MIB", "brcdHqosStatsPriority"))
if mibBuilder.loadTexts: brcdHqosStatsEntry.setStatus('current')
brcdHqosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: brcdHqosIfIndex.setStatus('current')
brcdHqosEndpointType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("singleTaggedVlan", 2), ("doubleTaggedVlan", 3), ("bVlanIsid", 4))))
if mibBuilder.loadTexts: brcdHqosEndpointType.setStatus('current')
brcdHqosEndpointTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: brcdHqosEndpointTag.setStatus('current')
brcdHqosEndpointInnerTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 4), Unsigned32())
if mibBuilder.loadTexts: brcdHqosEndpointInnerTag.setStatus('current')
brcdHqosStatsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 5), PortPriorityTC())
if mibBuilder.loadTexts: brcdHqosStatsPriority.setStatus('current')
brcdHqosStatsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsDescription.setStatus('current')
brcdHqosStatsEnquePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsEnquePkts.setStatus('current')
brcdHqosStatsEnqueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsEnqueBytes.setStatus('current')
brcdHqosStatsDequePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsDequePkts.setStatus('current')
brcdHqosStatsDequeBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsDequeBytes.setStatus('current')
brcdHqosStatsTotalDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsTotalDiscardPkts.setStatus('current')
brcdHqosStatsTotalDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsTotalDiscardBytes.setStatus('current')
brcdHqosStatsOldestDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsOldestDiscardPkts.setStatus('current')
brcdHqosStatsOldestDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsOldestDiscardBytes.setStatus('current')
brcdHqosStatsWREDDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsWREDDroppedPkts.setStatus('current')
brcdHqosStatsWREDDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsWREDDroppedBytes.setStatus('current')
brcdHqosStatsCurrentQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsCurrentQDepth.setStatus('current')
brcdHqosStatsMaxQDepthSinceLastRead = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 14, 1, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdHqosStatsMaxQDepthSinceLastRead.setStatus('current')
mibBuilder.exportSymbols("BROCADE-QOS-MIB", brcdHqosObjects=brcdHqosObjects, brcdHqosStatsDequePkts=brcdHqosStatsDequePkts, brcdHqosStatsMaxQDepthSinceLastRead=brcdHqosStatsMaxQDepthSinceLastRead, brcdHqosStatsEnqueBytes=brcdHqosStatsEnqueBytes, brcdHqosStatsTotalDiscardPkts=brcdHqosStatsTotalDiscardPkts, brcdHqosStatsDequeBytes=brcdHqosStatsDequeBytes, brcdHqosIfIndex=brcdHqosIfIndex, brcdHqosStatsDescription=brcdHqosStatsDescription, brcdHqosStatsEntry=brcdHqosStatsEntry, brcdHqosEndpointInnerTag=brcdHqosEndpointInnerTag, brcdHqosStatsTotalDiscardBytes=brcdHqosStatsTotalDiscardBytes, brcdHqosStatsCurrentQDepth=brcdHqosStatsCurrentQDepth, brcdHqosStatsTable=brcdHqosStatsTable, brcdHqosStatsOldestDiscardPkts=brcdHqosStatsOldestDiscardPkts, brcdHqosStatsPriority=brcdHqosStatsPriority, brcdQosMIB=brcdQosMIB, PYSNMP_MODULE_ID=brcdQosMIB, brcdHqosStatsEnquePkts=brcdHqosStatsEnquePkts, brcdHqosEndpointTag=brcdHqosEndpointTag, brcdHqosEndpointType=brcdHqosEndpointType, brcdHqosStatsWREDDroppedBytes=brcdHqosStatsWREDDroppedBytes, brcdHqosStatsOldestDiscardBytes=brcdHqosStatsOldestDiscardBytes, brcdHqosStatsWREDDroppedPkts=brcdHqosStatsWREDDroppedPkts)
