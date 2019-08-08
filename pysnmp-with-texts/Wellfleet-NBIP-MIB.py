#
# PySNMP MIB module Wellfleet-NBIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-NBIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Bits, ModuleIdentity, IpAddress, Integer32, TimeTicks, ObjectIdentity, Gauge32, Counter32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Bits", "ModuleIdentity", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "Gauge32", "Counter32", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfNetBIOSIpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfNetBIOSIpGroup")
wfNetbiosIp = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1))
wfNetbiosIpDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpDelete.setDescription('Create/Delete parameter. Default is created. Users perform an SNMP SET operation on this object in order to create/delete the NetBIOS over IP support.')
wfNetbiosIpDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform an SNMP SET operation on this object in order to enable/disable the NetBIOS over IP support.')
wfNetbiosIpState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpState.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpState.setDescription('The current state of the entire NetBIOS over IP.')
wfNetbiosIpNameCacheDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheDisable.setDescription('Enable/Disable parameter for the NetBIOS name cache.')
wfNetbiosIp15CharacterDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIp15CharacterDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIp15CharacterDisable.setDescription('Enable/Disable parameter for 15-character NetBIOS name caching.')
wfNetbiosIpNameCacheMibDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMibDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMibDisable.setDescription('Enable/Disable creation of MIB instances for each cached name.')
wfNetbiosIpNameCacheMaximumEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 7), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMaximumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMaximumEntries.setDescription('The maximum number of entries allowed in the NetBIOS name cache.')
wfNetbiosIpNameCacheCurrentEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheCurrentEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheCurrentEntries.setDescription('The number of entries currently in the NetBIOS name cache.')
wfNetbiosIpNameCacheAgeTime = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 604800)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheAgeTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheAgeTime.setDescription('The age in seconds when inactive NetBIOS names will be aged out of the cache.')
wfNetbiosIpNameCacheHashEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 10), Integer32().clone(253)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheHashEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheHashEntries.setDescription('The number of entries in the NetBIOS name cache hash table.')
wfNetbiosIpNameCacheHits = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheHits.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheHits.setDescription('The number of times the NetBIOS name cache has been used.')
wfNetbiosIpNameCacheMisses = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMisses.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameCacheMisses.setDescription('The number of failed lookups on the NetBIOS name cache.')
wfNetbiosIpRebroadcastTTL = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpRebroadcastTTL.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpRebroadcastTTL.setDescription('The default time-to-live value in seconds to use in rebroadcasted packets.')
wfNetbiosIpRebroadcastRecordRoute = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpRebroadcastRecordRoute.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpRebroadcastRecordRoute.setDescription('Enable/Disable insertion of Record Route option in rebroadcasted packets.')
wfNetbiosIpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2), )
if mibBuilder.loadTexts: wfNetbiosIpInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceTable.setDescription('A table that contains information about every interface that is configured to run/not run NetBIOS over IP. inst_id[1] = wfNetbiosIpInterfaceIndex')
wfNetbiosIpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1), ).setIndexNames((0, "Wellfleet-NBIP-MIB", "wfNetbiosIpInterfaceIndex"))
if mibBuilder.loadTexts: wfNetbiosIpInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceEntry.setDescription('An entry in the NetBIOS interface table.')
wfNetbiosIpInterfaceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceDelete.setDescription('Create/Delete parameter. Default is created. Users perform an SNMP SET operation on this object in order to create/delete an interface.')
wfNetbiosIpInterfaceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform an SNMP SET operation on this object in order to enable/disable an interface.')
wfNetbiosIpInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceState.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceState.setDescription('The current state of NetBIOS over IP on this interface.')
wfNetbiosIpInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceIndex.setDescription('The IP address of this interface.')
wfNetbiosIpInterfaceReceivedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceReceivedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceReceivedFrames.setDescription('The number of frames that have been received by this interface from its circuit.')
wfNetbiosIpInterfaceReceivedBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceReceivedBadFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceReceivedBadFrames.setDescription('The number of invalid frames that have been received by this interface from its circuit.')
wfNetbiosIpInterfaceTransmittedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceTransmittedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceTransmittedFrames.setDescription('The number of frames that have been transmitted by this interface.')
wfNetbiosIpInterfaceNameCacheDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceNameCacheDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceNameCacheDisable.setDescription('Enable/Disable parameter for NetBIOS name caching.')
wfNetbiosIpInterfaceInBroadcastDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceInBroadcastDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceInBroadcastDisable.setDescription('Enable/Disable parameter for the input of NetBIOS broadcasts.')
wfNetbiosIpInterfaceOutBroadcastDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceOutBroadcastDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceOutBroadcastDisable.setDescription('Enable/Disable parameter for the output of NetBIOS broadcasts.')
wfNetbiosIpInterfaceRebroadcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 2, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpInterfaceRebroadcastAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpInterfaceRebroadcastAddr.setDescription('The IP broadcast address to use for rebroadcasted packets out this interface.')
wfNetbiosIpNameTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3), )
if mibBuilder.loadTexts: wfNetbiosIpNameTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameTable.setDescription('The NetBIOS name cache table.')
wfNetbiosIpNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1), ).setIndexNames((0, "Wellfleet-NBIP-MIB", "wfNetbiosIpName"), (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpAddress"), (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpIdNumber"))
if mibBuilder.loadTexts: wfNetbiosIpNameEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpNameEntry.setDescription('An entry in the NetBIOS name cache table.')
wfNetbiosIpName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpName.setDescription('The NetBIOS name of this station. It is a maximum of 16 characters.')
wfNetbiosIpScopeId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpScopeId.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpScopeId.setDescription('The NetBIOS scope id of this station.')
wfNetbiosIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpAddress.setDescription('The IP address of the NetBIOS station.')
wfNetbiosIpStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("learned", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpStatic.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStatic.setDescription('Indicates whether this entry is a static or learned entry.')
wfNetbiosIpCacheHits = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpCacheHits.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpCacheHits.setDescription('The number of Name Query Responses that have been converted by this station.')
wfNetbiosIpIdNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpIdNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpIdNumber.setDescription('Uniqueness ID for the MIB entry.')
wfNetbiosIpStaticTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4), )
if mibBuilder.loadTexts: wfNetbiosIpStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticTable.setDescription('The NetBIOS static server/client entry table.')
wfNetbiosIpStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1), ).setIndexNames((0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticName"), (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticIpAddress"), (0, "Wellfleet-NBIP-MIB", "wfNetbiosIpStaticIdNumber"))
if mibBuilder.loadTexts: wfNetbiosIpStaticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticEntry.setDescription('An entry in the NetBIOS static entry table.')
wfNetbiosIpStaticDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpStaticDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticDelete.setDescription('Create/Delete parameter for the NetBIOS static entry.')
wfNetbiosIpStaticDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpStaticDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticDisable.setDescription('Enable/Disable parameter for the NetBIOS static entry.')
wfNetbiosIpStaticState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2))).clone('invalid')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpStaticState.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticState.setDescription('The state of this NetBIOS static entry.')
wfNetbiosIpStaticName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpStaticName.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticName.setDescription('The NetBIOS name of the station. It is a maximum of 16 characters. Names that are shorter are padded with ASCII spaces - 0x20.')
wfNetbiosIpStaticScopeId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNetbiosIpStaticScopeId.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticScopeId.setDescription('The NetBIOS scope id of the station. Once set, this should not be changed.')
wfNetbiosIpStaticIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpStaticIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticIpAddress.setDescription('The IP address of the NetBIOS station.')
wfNetbiosIpStaticIdNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfNetbiosIpStaticIdNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfNetbiosIpStaticIdNumber.setDescription('Uniqueness ID for the MIB entry.')
mibBuilder.exportSymbols("Wellfleet-NBIP-MIB", wfNetbiosIpDelete=wfNetbiosIpDelete, wfNetbiosIpInterfaceReceivedFrames=wfNetbiosIpInterfaceReceivedFrames, wfNetbiosIpNameCacheDisable=wfNetbiosIpNameCacheDisable, wfNetbiosIpNameCacheMisses=wfNetbiosIpNameCacheMisses, wfNetbiosIpStaticIdNumber=wfNetbiosIpStaticIdNumber, wfNetbiosIpInterfaceNameCacheDisable=wfNetbiosIpInterfaceNameCacheDisable, wfNetbiosIpCacheHits=wfNetbiosIpCacheHits, wfNetbiosIpStaticName=wfNetbiosIpStaticName, wfNetbiosIpStaticIpAddress=wfNetbiosIpStaticIpAddress, wfNetbiosIpInterfaceTransmittedFrames=wfNetbiosIpInterfaceTransmittedFrames, wfNetbiosIpName=wfNetbiosIpName, wfNetbiosIpStaticTable=wfNetbiosIpStaticTable, wfNetbiosIpInterfaceInBroadcastDisable=wfNetbiosIpInterfaceInBroadcastDisable, wfNetbiosIpNameTable=wfNetbiosIpNameTable, wfNetbiosIpInterfaceOutBroadcastDisable=wfNetbiosIpInterfaceOutBroadcastDisable, wfNetbiosIpInterfaceState=wfNetbiosIpInterfaceState, wfNetbiosIpNameEntry=wfNetbiosIpNameEntry, wfNetbiosIpInterfaceDisable=wfNetbiosIpInterfaceDisable, wfNetbiosIpDisable=wfNetbiosIpDisable, wfNetbiosIpNameCacheHashEntries=wfNetbiosIpNameCacheHashEntries, wfNetbiosIpInterfaceEntry=wfNetbiosIpInterfaceEntry, wfNetbiosIpState=wfNetbiosIpState, wfNetbiosIpNameCacheMaximumEntries=wfNetbiosIpNameCacheMaximumEntries, wfNetbiosIpScopeId=wfNetbiosIpScopeId, wfNetbiosIpAddress=wfNetbiosIpAddress, wfNetbiosIpRebroadcastTTL=wfNetbiosIpRebroadcastTTL, wfNetbiosIpInterfaceIndex=wfNetbiosIpInterfaceIndex, wfNetbiosIpStatic=wfNetbiosIpStatic, wfNetbiosIpInterfaceReceivedBadFrames=wfNetbiosIpInterfaceReceivedBadFrames, wfNetbiosIpIdNumber=wfNetbiosIpIdNumber, wfNetbiosIpStaticState=wfNetbiosIpStaticState, wfNetbiosIpNameCacheCurrentEntries=wfNetbiosIpNameCacheCurrentEntries, wfNetbiosIp=wfNetbiosIp, wfNetbiosIpStaticDisable=wfNetbiosIpStaticDisable, wfNetbiosIpStaticEntry=wfNetbiosIpStaticEntry, wfNetbiosIpRebroadcastRecordRoute=wfNetbiosIpRebroadcastRecordRoute, wfNetbiosIpStaticDelete=wfNetbiosIpStaticDelete, wfNetbiosIpInterfaceDelete=wfNetbiosIpInterfaceDelete, wfNetbiosIpNameCacheAgeTime=wfNetbiosIpNameCacheAgeTime, wfNetbiosIp15CharacterDisable=wfNetbiosIp15CharacterDisable, wfNetbiosIpStaticScopeId=wfNetbiosIpStaticScopeId, wfNetbiosIpInterfaceTable=wfNetbiosIpInterfaceTable, wfNetbiosIpNameCacheMibDisable=wfNetbiosIpNameCacheMibDisable, wfNetbiosIpInterfaceRebroadcastAddr=wfNetbiosIpInterfaceRebroadcastAddr, wfNetbiosIpNameCacheHits=wfNetbiosIpNameCacheHits)