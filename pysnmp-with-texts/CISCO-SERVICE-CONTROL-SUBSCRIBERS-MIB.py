#
# PySNMP MIB module CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:11:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalName, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalName", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, Counter64, iso, NotificationType, Unsigned32, Integer32, Gauge32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "Counter64", "iso", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "Counter32", "TimeTicks")
DisplayString, RowStatus, TextualConvention, TruthValue, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "StorageType")
ciscoServiceControlSubscribersMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 628))
ciscoServiceControlSubscribersMIB.setRevisions(('2007-05-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoServiceControlSubscribersMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoServiceControlSubscribersMIB.setLastUpdated('200705220000Z')
if mibBuilder.loadTexts: ciscoServiceControlSubscribersMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoServiceControlSubscribersMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-excelsior-dev@cisco.com')
if mibBuilder.loadTexts: ciscoServiceControlSubscribersMIB.setDescription("This MIB provides global and specific information on subscribers managed by a service control entity, which is a network element that monitors network traffic between network subscribers based on user configured policies. The network subscribers are the end users of the network with a unique network address for each subscriber. A specific subscriber is identified by this MIB by its subscriber name which is assured to be unique, this id is used to retrieve this specific subscriber's information.")
ciscoServiceControlSubscribersMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 628, 0))
ciscoServiceControlSubscribersMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 628, 1))
ciscoServiceControlSubscribersMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 628, 2))
cServiceControlSubscribersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1), )
if mibBuilder.loadTexts: cServiceControlSubscribersTable.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersTable.setDescription("This table maintains list of subscribers of the service control entity that has an entry in the entPhysicalTable of the ENTITY-MIB. An entry must be created in this table to monitor the subscriber so that NMS application can query subscriber data from the CISCO-SERVICE-CONTROL-DPI-MIB. If the service control entity is not required to monitor a particular subscriber, the corresponding entry is deleted by setting the cServiceControlSubscribersRowStatus object to 'destroy'. When the service control entity reboots, the entries associated with this entity will be cleared.")
cServiceControlSubscribersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersIndex"))
if mibBuilder.loadTexts: cServiceControlSubscribersEntry.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersEntry.setDescription("An entry (conceptual row) in the cServiceControlSubscribersTable. An entry is created to specify which subscriber (cServiceControlSubscribersName) will be monitored by a service control entity, identified by entPhysicalIndex in the entPhysicalTable with its entPhysicalClass of 'module' or 'chassis'.")
cServiceControlSubscribersIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cServiceControlSubscribersIndex.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersIndex.setDescription('A unique subscriber entry index.')
cServiceControlSubscribersName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cServiceControlSubscribersName.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersName.setDescription('The name of the subscriber to be monitored by this service control entity.')
cServiceControlSubscriberStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cServiceControlSubscriberStorageType.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscriberStorageType.setDescription('This object specifies the storage type for this conceptual row. The following columnar objects are allowed to be writable when the storageType of this conceptual row is permanent(4): cServiceControlSubscribersName')
cServiceControlSubscribersRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cServiceControlSubscribersRowStatus.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersRowStatus.setDescription("The status of this conceptual row: To create a row in this table, a manager must set this object to either 'createAndGo' or 'createAndWait'. Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of this object is 'notReady'. In particular, a newly created row cannot be made active until the appropriate columns have been set. Default value will be automatically provisioned for those objects not specified during row creation. cServiceControlSubscribersName may not be modified while the value of this object is 'active'. An entry is deleted by setting the value of corresponding instance of this object to 'destroy' or the subscriber is not using the service anymore by disconnecting from the network. The entries will be deleted when the service control entity reboots.")
cServiceControlSubscribersInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2), )
if mibBuilder.loadTexts: cServiceControlSubscribersInfoTable.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersInfoTable.setDescription('This table provides listing of subscribers data for a service control entity that has an entry in the entPhysicalTable of the ENTITY-MIB. A subscriber of a service on the network is uniquely identified by the cServiceControlSubscribersName. The subscriber may either be mapped to a network address known by the service control entity, or may be anonymous. This table maintains statistical data for subscribers known by the service control entity.')
cServiceControlSubscribersInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cServiceControlSubscribersInfoEntry.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersInfoEntry.setDescription("An entry (conceptual row) in the cServiceControlSubscribersInfoTable. This entry lists information about the data regarding subscribers management operations performed, and the current status of the subscribers database on a service control entity that has an entry in the entPhysicalTable. entPhysicalIndex is index for this table which represents entities of 'module' or 'chassis' entPhysicalClass.")
cServiceControlSubscribersNumIntroduced = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumIntroduced.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumIntroduced.setDescription('This object indicates the current number of subscribers that have been introduced to the system. These subscribers may or may not have IP address or VLAN mappings.')
cServiceControlSubscribersNumFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumFree.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumFree.setDescription('This object indicates the free subscriber space available in the system. This is the number of subscribers that can be introduced to the system in addition to the subscribers that are already introduced to the system as maintained by cServiceControlSubscribersNumIntroduced.')
cServiceControlSubscribersNumIpAddrMappings = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpAddrMappings.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpAddrMappings.setDescription('This object indicates the current number of subscriber mappings to a single network address or to different network addresses. Each address mapped to a subscriber constitutes a subscriber mapping.')
cServiceControlSubscribersNumIpAddrMappingsFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpAddrMappingsFree.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpAddrMappingsFree.setDescription("This object indicates the number of free 'IP address to subscriber' mappings that may be used for defining new mappings.")
cServiceControlSubscribersNumIpRangeMappings = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpRangeMappings.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpRangeMappings.setDescription("This object indicates the current number of 'IP-range to subscriber' mappings. Each mapping instance corresponds to a subscriber mapped to a range of IP addresses.")
cServiceControlSubscribersNumIpRangeMappingsFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpRangeMappingsFree.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumIpRangeMappingsFree.setDescription("This object indicates the number of free 'IP-range to subscriber' mappings that may be used for defining new mappings.")
cServiceControlSubscribersNumVlanMappings = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumVlanMappings.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumVlanMappings.setDescription('This object indicates the current number of subscriber mappings to a single VLAN ID or to different VLAN IDs. Each VLAN ID mapped to a subscriber constitutes a subscriber mapping.')
cServiceControlSubscribersNumVlanMappingsFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumVlanMappingsFree.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumVlanMappingsFree.setDescription("This object indicates the number of free 'VLAN to subscriber' mappings that may be used for defining new mappings.")
cServiceControlSubscribersNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumActive.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumActive.setDescription('This object indicates the current number of active subscribers. These subscribers necessarily have an IP address or VLAN mappings that define the traffic that should be associated and served according to the subscriber service agreement.')
cServiceControlSubscribersNumUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumUpdates.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumUpdates.setDescription('This object indicates the accumulated number of subscribers database updates received by the system.')
cServiceControlSubscribersNumTpIpRanges = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumTpIpRanges.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumTpIpRanges.setDescription("This object indicates the current number of 'Traffic Processor IP address ranges' used. This object is equal to the total number of network address ranges used to map to all the subscribers in the system. For multiple traffic processor systems, the address ranges are distributed between traffic processors for dedicated processing of data belonging to the mapped address space.")
cServiceControlSubscribersNumTpIpRangesFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumTpIpRangesFree.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumTpIpRangesFree.setDescription("This object indicates the number of free 'Traffic Processor IP ranges'.")
cServiceControlSubscribersNumAnonymous = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumAnonymous.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumAnonymous.setDescription('This object indicates the current number of anonymous subscribers.')
cServiceControlSubscribersNumWithSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscribersNumWithSessions.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNumWithSessions.setDescription('This object indicates the current number of subscribers with open flows.')
cServiceControlSubscriberMappingFailedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubscriberMappingFailedReason.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscriberMappingFailedReason.setDescription('This contains user readable description of the problem when some external entity attempts to create illegal or inconsistent subscriber mappings. For example, an attempt to map a subscriber to incorrect address will culminate in the subscriber name and the address to which mapping attempt is made and the reason why the mapping attempt failed.')
cServiceControlSubsribersMaxSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cServiceControlSubsribersMaxSupported.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubsribersMaxSupported.setDescription('This object indicates the max number of subscribers that can be monitored by this service control entity.')
cServiceControlSubscribersNotifsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cServiceControlSubscribersNotifsEnable.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNotifsEnable.setDescription("This object controls whether the system produces cServiceControlSubscriberMapping notifications. A 'false' value will prevent cServiceControlSubscriberMapping notifications from being generated by this system.")
cServiceControlSubscriberMapping = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 628, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMappingFailedReason"))
if mibBuilder.loadTexts: cServiceControlSubscriberMapping.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscriberMapping.setDescription('This notification is sent by the service control entity when some external entity attempts to create illegal or inconsistent subscriber mappings. The cServiceControlSubscriberMappingFailedReason contains a message describing the problem and entPhysicalName contains the name of the service control entity generating the notification.')
cServiceControlSubscribersCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 1))
cServiceControlSubscribersGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2))
cServiceControlSubscribersCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersObjectGroup"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNotificationGroup"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersInfoObjectGroup"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceControlSubscribersCompliance = cServiceControlSubscribersCompliance.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersCompliance.setDescription('The compliance statement for SNMP Agents which implement this MIB.')
cServiceControlSubscribersObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersName"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersRowStatus"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceControlSubscribersObjectGroup = cServiceControlSubscribersObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersObjectGroup.setDescription('Group of objects for subscribers.')
cServiceControlSubscribersNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMapping"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceControlSubscribersNotificationGroup = cServiceControlSubscribersNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNotificationGroup.setDescription('Group of notifications for this MIB.')
cServiceControlSubscribersInfoObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIntroduced"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumFree"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpAddrMappings"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpAddrMappingsFree"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpRangeMappings"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpRangeMappingsFree"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumVlanMappings"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumVlanMappingsFree"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumActive"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumUpdates"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumTpIpRanges"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumTpIpRangesFree"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumAnonymous"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumWithSessions"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMappingFailedReason"), ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubsribersMaxSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceControlSubscribersInfoObjectGroup = cServiceControlSubscribersInfoObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersInfoObjectGroup.setDescription('Group of objects for subscriber mappings subscriber statistics.')
cServiceControlSubscribersNotifsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 4)).setObjects(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNotifsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceControlSubscribersNotifsGroup = cServiceControlSubscribersNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: cServiceControlSubscribersNotifsGroup.setDescription('A collection of objects providing configuration information applicable to all subscriber mapping notifications.')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", ciscoServiceControlSubscribersMIBNotifs=ciscoServiceControlSubscribersMIBNotifs, cServiceControlSubscribersNumActive=cServiceControlSubscribersNumActive, cServiceControlSubscribersNumUpdates=cServiceControlSubscribersNumUpdates, cServiceControlSubscriberMappingFailedReason=cServiceControlSubscriberMappingFailedReason, cServiceControlSubscribersGroups=cServiceControlSubscribersGroups, cServiceControlSubscribersNumVlanMappingsFree=cServiceControlSubscribersNumVlanMappingsFree, cServiceControlSubscribersNumFree=cServiceControlSubscribersNumFree, ciscoServiceControlSubscribersMIBConform=ciscoServiceControlSubscribersMIBConform, PYSNMP_MODULE_ID=ciscoServiceControlSubscribersMIB, cServiceControlSubscribersCompliance=cServiceControlSubscribersCompliance, cServiceControlSubscribersName=cServiceControlSubscribersName, cServiceControlSubscribersNumIpRangeMappingsFree=cServiceControlSubscribersNumIpRangeMappingsFree, cServiceControlSubsribersMaxSupported=cServiceControlSubsribersMaxSupported, ciscoServiceControlSubscribersMIB=ciscoServiceControlSubscribersMIB, cServiceControlSubscribersCompliances=cServiceControlSubscribersCompliances, cServiceControlSubscribersNumIpAddrMappingsFree=cServiceControlSubscribersNumIpAddrMappingsFree, cServiceControlSubscribersNumIpAddrMappings=cServiceControlSubscribersNumIpAddrMappings, cServiceControlSubscribersNumTpIpRangesFree=cServiceControlSubscribersNumTpIpRangesFree, cServiceControlSubscribersNotificationGroup=cServiceControlSubscribersNotificationGroup, cServiceControlSubscribersInfoObjectGroup=cServiceControlSubscribersInfoObjectGroup, cServiceControlSubscribersNumIpRangeMappings=cServiceControlSubscribersNumIpRangeMappings, cServiceControlSubscribersInfoTable=cServiceControlSubscribersInfoTable, cServiceControlSubscribersTable=cServiceControlSubscribersTable, cServiceControlSubscriberMapping=cServiceControlSubscriberMapping, cServiceControlSubscribersNumWithSessions=cServiceControlSubscribersNumWithSessions, cServiceControlSubscribersInfoEntry=cServiceControlSubscribersInfoEntry, cServiceControlSubscribersRowStatus=cServiceControlSubscribersRowStatus, cServiceControlSubscribersNumIntroduced=cServiceControlSubscribersNumIntroduced, cServiceControlSubscriberStorageType=cServiceControlSubscriberStorageType, cServiceControlSubscribersNumTpIpRanges=cServiceControlSubscribersNumTpIpRanges, cServiceControlSubscribersIndex=cServiceControlSubscribersIndex, cServiceControlSubscribersNumVlanMappings=cServiceControlSubscribersNumVlanMappings, cServiceControlSubscribersEntry=cServiceControlSubscribersEntry, ciscoServiceControlSubscribersMIBObjects=ciscoServiceControlSubscribersMIBObjects, cServiceControlSubscribersNotifsEnable=cServiceControlSubscribersNotifsEnable, cServiceControlSubscribersObjectGroup=cServiceControlSubscribersObjectGroup, cServiceControlSubscribersNotifsGroup=cServiceControlSubscribersNotifsGroup, cServiceControlSubscribersNumAnonymous=cServiceControlSubscribersNumAnonymous)
