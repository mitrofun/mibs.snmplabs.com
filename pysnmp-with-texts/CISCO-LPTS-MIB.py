#
# PySNMP MIB module CISCO-LPTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LPTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, MibIdentifier, Gauge32, Counter64, Unsigned32, Counter32, IpAddress, ObjectIdentity, ModuleIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "Counter32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLptsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 812))
ciscoLptsMIB.setRevisions(('2013-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLptsMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLptsMIB.setLastUpdated('201309030000Z')
if mibBuilder.loadTexts: ciscoLptsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLptsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-q-lpts-dev@cisco.com')
if mibBuilder.loadTexts: ciscoLptsMIB.setDescription("The MIB module for Local Packet Transport Services(LPTS) related information like the flows and the policer values related to various flows present in the system. The number of packets coming into the system is controlled by the policer values associated with the protocol. Each protocol is classified into different flows and a rate limit is associated with the flows. Policer is a numerical value controlling the number of packets entering the box. The flows represent individual, specific protocols. Flow types also represent the degree of trust for a given packet. Ex: BGP packets coming from established session is assigned one flow, packets from configured BGP peer are assigned different flow . Other BGP packets are assigned a third flow. Definitions: LPTS - Local Packet Transport Services. It is a network infrastructure subsystem that provides a common facility for transport of packets which are destined towards the router (for-us packets), to the exact applications. In addtion to that, it also provides policing of for-us packets FlowType - Represents individual, specific protocols. Flow also represents the degree of trust for a given packet. LC - Line Cards. Policer - Index to FlowType. CurrentRate - Number of packets allowed into the box in PPS (Packets Per Second). Type - Defines the scope of the flow applicable at a specific node or Line card. Precedence - Precedence is the selection mechanism for a specific Type if more than one Type is configured for the same flow. 'local' FlowType has higher precedence over 'global' and 'static' FlowTypes. 'global' FlowType has higher precedence over 'static' FlowType. nodeID - The line card for which the flow configuration is made.")
class ClFlowType(TextualConvention, Integer32):
    description = "An enumeration unsigned integer which indicates the scope of flow applicable at a specific node or Line Card (LC). Precedence is the selection mechanism for a specific Type if more than one Type is configured for the same flow. When Type 'local' and 'global' are configured for the same flow, then 'local' Type takes precedence. If 'local' Type is not configured, then 'global' Type would be applied if it is present. If neither the 'local' nor the 'global' Type is configured, then the ClFlowType is derived from the static configuration file which is of Type 'static'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("static", 1), ("global", 2), ("local", 3))

ciscoLptsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 0))
ciscoLptsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 1))
ciscoLptsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2))
clGlobalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1), )
if mibBuilder.loadTexts: clGlobalFlowTable.setStatus('current')
if mibBuilder.loadTexts: clGlobalFlowTable.setDescription('This table respresents the flows configured globally and the configuration will be reflected across all the linecards')
clGlobalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"))
if mibBuilder.loadTexts: clGlobalFlowEntry.setStatus('current')
if mibBuilder.loadTexts: clGlobalFlowEntry.setDescription("An entry will be added into clGlobalFlowTable when LPTS flows configured without any location specific details. Similarly when the global LPTS flow config is removed, then type and rate retained as per Static config file. The entries in this table can be of Type either 'global' or 'static'.")
clGlobalFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: clGlobalFlowIndex.setStatus('current')
if mibBuilder.loadTexts: clGlobalFlowIndex.setDescription('An unique value used to represent a row in the clGlobalFlowTable')
clGlobalFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalFlowType.setStatus('current')
if mibBuilder.loadTexts: clGlobalFlowType.setDescription('This object indicates the flow type name associated with every flow. Eg. FlowType could be BGP-Known, BGP-configured BGP-default.')
clGlobalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 3), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalType.setStatus('current')
if mibBuilder.loadTexts: clGlobalType.setDescription("This object indicates an enumeration which indicates whether LPTS flow configured across all the linecards are 'global' or 'static' depending on the predecedence")
clGlobalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 4), Unsigned32()).setUnits('PPS').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clGlobalCurrentRate.setStatus('current')
if mibBuilder.loadTexts: clGlobalCurrentRate.setDescription('This object specifies the rate associated with the flow type which is configured globally.')
clLocalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2), )
if mibBuilder.loadTexts: clLocalFlowTable.setStatus('current')
if mibBuilder.loadTexts: clLocalFlowTable.setDescription('This table represents the configurations for the local flow types & affects a particular nodeID for which config is applied. When local flow type is not configured & we have a global configuration then the clLocalFlowTable has global flow value. If neither local flow nor the global flows are configured, then clLocalFlowTable will have static values derived from the config file. If both the local flow and global flow is configured, then the local flow information takes precedence over the global flow information.')
clLocalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"), (0, "CISCO-LPTS-MIB", "clLocalNodeID"))
if mibBuilder.loadTexts: clLocalFlowEntry.setStatus('current')
if mibBuilder.loadTexts: clLocalFlowEntry.setDescription('An entry in clLocalFlowTable will be added when LPTS flows are configured specific to a location. This table is indexed based on nodeID and clGlobalFlowIndex. When NMS polls for flow in clLocalFlowTable, the flow name is retrieved from the clGlobalFlowTable. When a local configuration is removed for a flow, then clGlobalCurrentRate will be applied if it is present, else static rate will be applied.')
clLocalNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: clLocalNodeID.setStatus('current')
if mibBuilder.loadTexts: clLocalNodeID.setDescription('The linecard for which the flow configuration is made.')
clLocalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 2), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalType.setStatus('current')
if mibBuilder.loadTexts: clLocalType.setDescription('This object indicates an enumeration which indicates LPTS flows configured specific to a linecard')
clLocalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 3), Unsigned32()).setUnits('PPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalCurrentRate.setStatus('current')
if mibBuilder.loadTexts: clLocalCurrentRate.setDescription('This object indicates the packet rate associated with the flow type with which packets are accepted or dropped specific to a linecard.')
clLocalAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalAccepted.setStatus('current')
if mibBuilder.loadTexts: clLocalAccepted.setDescription('This object indicates the total number of packets accepted on a linecard for a specific flow.')
clLocalDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalDropped.setStatus('current')
if mibBuilder.loadTexts: clLocalDropped.setDescription('This object indicates the total number of packets dropped on a linecard for a specific flow.')
clLocalTosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalTosValue.setStatus('current')
if mibBuilder.loadTexts: clLocalTosValue.setDescription('This object indicates the type of service.')
ciscoLptsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1))
ciscoLptsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2))
ciscoLptsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1, 1)).setObjects(("CISCO-LPTS-MIB", "clLocalFlowGroup"), ("CISCO-LPTS-MIB", "clGlobalFlowGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLptsMIBCompliance = ciscoLptsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLptsMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco LPTS MIB.')
clGlobalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 1)).setObjects(("CISCO-LPTS-MIB", "clGlobalFlowType"), ("CISCO-LPTS-MIB", "clGlobalCurrentRate"), ("CISCO-LPTS-MIB", "clGlobalType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clGlobalFlowGroup = clGlobalFlowGroup.setStatus('current')
if mibBuilder.loadTexts: clGlobalFlowGroup.setDescription('A collection of objects which provides information about flow type and current rate configured across all Linecards.')
clLocalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 2)).setObjects(("CISCO-LPTS-MIB", "clLocalCurrentRate"), ("CISCO-LPTS-MIB", "clLocalAccepted"), ("CISCO-LPTS-MIB", "clLocalDropped"), ("CISCO-LPTS-MIB", "clLocalType"), ("CISCO-LPTS-MIB", "clLocalTosValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clLocalFlowGroup = clLocalFlowGroup.setStatus('current')
if mibBuilder.loadTexts: clLocalFlowGroup.setDescription('A collection of objects which provides information about current rate and accept/drop statistics for a specific linecard.')
mibBuilder.exportSymbols("CISCO-LPTS-MIB", clGlobalFlowIndex=clGlobalFlowIndex, clLocalAccepted=clLocalAccepted, clLocalType=clLocalType, clGlobalFlowTable=clGlobalFlowTable, clGlobalFlowEntry=clGlobalFlowEntry, clGlobalFlowGroup=clGlobalFlowGroup, clGlobalType=clGlobalType, clLocalFlowTable=clLocalFlowTable, clLocalFlowGroup=clLocalFlowGroup, clGlobalCurrentRate=clGlobalCurrentRate, ciscoLptsMIBConform=ciscoLptsMIBConform, clLocalTosValue=clLocalTosValue, clGlobalFlowType=clGlobalFlowType, ciscoLptsMIBNotifs=ciscoLptsMIBNotifs, clLocalCurrentRate=clLocalCurrentRate, ciscoLptsMIB=ciscoLptsMIB, ciscoLptsMIBObjects=ciscoLptsMIBObjects, clLocalNodeID=clLocalNodeID, ciscoLptsMIBCompliance=ciscoLptsMIBCompliance, PYSNMP_MODULE_ID=ciscoLptsMIB, clLocalFlowEntry=clLocalFlowEntry, ciscoLptsMIBGroups=ciscoLptsMIBGroups, ClFlowType=ClFlowType, clLocalDropped=clLocalDropped, ciscoLptsMIBCompliances=ciscoLptsMIBCompliances)
