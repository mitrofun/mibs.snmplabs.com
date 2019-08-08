#
# PySNMP MIB module GENERIC-3COM-VLAN-MIB-1-0-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENERIC-3COM-VLAN-MIB-1-0-1
# Produced by pysmi-0.3.4 at Wed May  1 13:19:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, IpAddress, Gauge32, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Bits, Counter32, ObjectIdentity, iso, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "IpAddress", "Gauge32", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Bits", "Counter32", "ObjectIdentity", "iso", "enterprises")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
generic = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10))
genExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1))
genVirtual = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14))
a3ComVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1))
a3ComVlanProtocolsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2))
a3ComVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3))
a3ComEncapsulationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4))
class A3ComVlanType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("vlanLayer2", 1), ("vlanDefaultProtocols", 2), ("vlanIPProtocol", 3), ("vlanIPXProtocol", 4), ("vlanAppleTalkProtocol", 5), ("vlanXNSProtocol", 6), ("vlanISOProtocol", 7), ("vlanDECNetProtocol", 8), ("vlanNetBIOSProtocol", 9), ("vlanSNAProtocol", 10), ("vlanVINESProtocol", 11), ("vlanX25Protocol", 12), ("vlanIGMPProtocol", 13), ("vlanSessionLayer", 14), ("vlanNetBeui", 15))

a3ComVlanGlobalMappingTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1), )
if mibBuilder.loadTexts: a3ComVlanGlobalMappingTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingTable.setDescription('This table lists VLAN interfaces that are globally identified. A single entry exists in this list for each VLAN interface in the system that is bound to a global identifier.')
a3ComVlanGlobalMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanGlobalMappingIdentifier"))
if mibBuilder.loadTexts: a3ComVlanGlobalMappingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingEntry.setDescription('An individual VLAN interface global mapping entry. Entries in this table are created by setting the a3ComVlanIfGlobalIdentifier object in the a3ComVlanIfTable to a non-zero value.')
a3ComVlanGlobalMappingIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIdentifier.setDescription('An index into the a3ComVlanGlobalMappingTable and an administratively assigned global VLAN identifier. The value of this object globally identifies the VLAN interface. For VLAN interfaces, on different network devices, which are part of the same globally identified VLAN, the value of this object will be the same.')
a3ComVlanGlobalMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanGlobalMappingIfIndex.setDescription('The value of a3ComVlanIfIndex for the VLAN interface in the a3ComVlanIfTable, which is bound to the global identifier specified by this entry.')
a3ComVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2), )
if mibBuilder.loadTexts: a3ComVlanIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfTable.setDescription('This table lists VLAN interfaces that exist within a device. A single entry exists in this list for each VLAN interface in the system. A VLAN interface may be created, destroyed and/or mapped to a globally identified vlan.')
a3ComVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComVlanIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfEntry.setDescription('An individual VLAN interface entry. When an NMS wishes to create a new entry in this table, it must obtain a non-zero index from the a3ComNextAvailableVirtIfIndex object. Row creation in this table will fail if the chosen index value does not match the current value returned from the a3ComNextAvailableVirtIfIndex object.')
a3ComVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfIndex.setDescription("The index value of this row and the vlan's ifIndex in the ifTable. The NMS obtains the index value for this row by reading the a3ComNextAvailableVirtIfIndex object.")
a3ComVlanIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfDescr.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfDescr.setDescription('This is a description of the VLAN interface.')
a3ComVlanIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 3), A3ComVlanType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfType.setDescription('The VLAN interface type.')
a3ComVlanIfGlobalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfGlobalIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfGlobalIdentifier.setDescription('An administratively assigned global VLAN identifier. For VLAN interfaces, on different network devices, which are part of the same globally identified VLAN, the value of this object will be the same. The binding between a global identifier and a VLAN interface can be created or removed. To create a binding an NMS must write a non-zero value to this object. To delete a binding, the NMS must write a zero to this object.')
a3ComVlanIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanIfInfo.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfInfo.setDescription('A TLV encoded information string for the VLAN interface. The information contained within this string corresponds to VLAN information not contained within this table, but contained elsewhere within this MIB module. The purpose of this string is to provide an NMS with a quick read mechanism of all related VLAN interface information. The encoding rules are defined according to: tag = 2 bytes length = 2 bytes value = n bytes The following tags are defined: TAG OBJECT DESCRIPTION 1 a3ComIpVlanIpNetAddress IP Network Address of IP VLAN 2 a3ComIpVlanIpNetMask IP Network Mask of IP VLAN')
a3ComVlanIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfStatus.setDescription('The status column for this VLAN interface. This OBJECT can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notInService(2) notReady(3). Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row and the values are acceptible to the agent, the agent will change the status to active(1). If any of the necessary objects are not available, the agent will reject the creation request. Setting this object to createAndWait(5) causes a row in this table to be created. The agent sets the status to notInService(2) if all of the information is present in the row and the values are acceptable to the agent; otherwise, the agent sets the status to notReady(3). Setting this object to active(1) is only valid when the current status is active(1) or notInService(2). When the state of the row transitions is set to active(1), the agent creates the corresponding row in the ifTable.. Setting this object to destroy(6) will remove the corresponding VLAN interface, remove the entry in this table, and the corresponding entries in the a3ComVlanGlobalMappingTable and the ifTable. In order for a set of this object to destroy(6) to succeed, all dependencies on this row must have been removed. These will include any stacking dependencies in the ifStackTable and any protocol specific tables dependencies.')
a3ComVlanIfIgnoreStpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanIfIgnoreStpFlag.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanIfIgnoreStpFlag.setDescription('Enable/disable STP for this VLAN interface. Setting this object to true will cause the ports on this VLAN to ignore STP BPDUs. When a vlan is first created, the Default value is FALSE, which means that the VLAN uses STP port information')
a3ComIpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1), )
if mibBuilder.loadTexts: a3ComIpVlanTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanTable.setDescription('A list of IP VLAN interface information entries. Entries in this table are related to entries in the a3ComVlanIfTable by using the same index.')
a3ComIpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComIpVlanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanEntry.setDescription('A a3ComIpVlanEntry contains layer 3 information about a particular IP VLAN interface. Note entries in this table cannot be deleted until the entries in the ifStackTable that produce overlap are removed.')
a3ComIpVlanIpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanIpNetAddress.setDescription('The IP network number for the IP VLAN interface defined in the a3ComVlanIfTable identified with the same index. The IpNetAdress and the IpNetMask must be set and the the row creation process completed by a NMS before overlapping rows in the ifStackTable can be created. Sets to the ifStackTable that produce overlapping IP VLAN interfaces will fail if this object is not set.')
a3ComIpVlanIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanIpNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanIpNetMask.setDescription('The IP network mask corresponding to the IP Network address defined by a3ComIpVlanIpNetAddress. The IpNetAdress and the IpNetMask must be set and the row creation process completed by a NMS before overlapping rows in the ifStackTable can be created. Sets to the ifStackTable that produce overlapping IP VLAN interfaces will fail if this object is not set.')
a3ComIpVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComIpVlanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComIpVlanStatus.setDescription('The status column for this IP VLAN entry. This object can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notInService(2) notReady(3). Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row and the values are acceptible to the agent, the agent will change the status to active(1). If any of the necessary objects are not available, the agent will reject the row creation request. Setting this object to createAndWait(5) causes a row in in this table to be created. The agent sets the status to notInService(2) if all of the information is present in the row and the values are acceptible to the agent; otherwise, the agent sets the status to notReady(3). Setting this object to active(1) is only valid when the current status is active(1) or notInService(2). When the status changes to active(1), the agent applies the IP parmeters to the IP VLAN interface identified by the corresponding value of the a3ComIpVlanIndex object. Setting this object to destroy(6) will remove the IP parmeters from the IP VLAN interface and remove the entry from this table. Setting this object to destroy(6) will remove the layer 3 information from the IP VLAN interface and will remove the row from this table. Note that this action cannot be performed if there are ifStackTable entries that result in overlapping IP VLAN interfaces. Note that these dependencies must be removed first.')
class A3ComVlanEncapsType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vlanEncaps3ComProprietaryPDD", 1), ("vlanEncaps8021q", 2), ("vlanEncapsPre8021qONcore", 3))

a3ComVlanEncapsIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1), )
if mibBuilder.loadTexts: a3ComVlanEncapsIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfTable.setDescription('This table lists VLAN encapsulation interfaces that exist within a device. A single entry exists in this list for each VLAN encapsulation interface in the system. A VLAN encapsulation interface may be created or destroyed.')
a3ComVlanEncapsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanEncapsIfIndex"))
if mibBuilder.loadTexts: a3ComVlanEncapsIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfEntry.setDescription('An individual VLAN encapsulation interface entry. When an NMS wishes to create a new entry in this table, it must obtain a non-zero index from the a3ComNextAvailableVirtIfIndex object. Row creation in this table will fail if the chosen index value does not match the current value returned from the a3ComNextAvailableVirtIfIndex object.')
a3ComVlanEncapsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfIndex.setDescription("The index value of this row and the encapsulation interface's ifIndex in the ifTable. The NMS obtains the index value used for creating a row in this table by reading the a3ComNextAvailableVirtIfIndex object.")
a3ComVlanEncapsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 2), A3ComVlanEncapsType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfType.setDescription('The encapsulation algorithm used when encapsulating packets transmitted, or de-encapsulating packets received through this interface.')
a3ComVlanEncapsIfTag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfTag.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfTag.setDescription('The tag used when encapsulating packets transmitted, or de-encapsulating packets received through this interface.')
a3ComVlanEncapsIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanEncapsIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanEncapsIfStatus.setDescription('The row status for this VLAN encapsulation interface. This OBJECT can be set to: active(1) createAndGo(4) createAndWait(5) destroy(6) The following values may be read: active(1) notReady(3). In order for a row to become active, the NMS must set a3ComVlanEncapsIfTagType and a3ComVlanEncapsIfTag to some valid and consistent values. Setting this object to createAndGo(4) causes the agent to attempt to create and commit the row based on the contents of the objects in the row. If all necessary information is present in the row, the agent will create the row and change the status to active(1). If any of the necessary objects are not available, or specify an invalid configuration, the row will not be created and the agent will return an appropriate error. Setting this object to createAndWait(5) causes a row in in this table to be created. If all necessary objects in the row have been assigned values and specify a valid configuration, the status of the row will be set to notInService(2); otherwise, the status will be set to notReady(3). This object may only be set to createAndGo(4) or createAndWait(5) if it does not exist. Setting this object to active(1) when the status is notInService(2) causes the agent to commit the row. Setting this object to active(1) when its value is already active(1) is a no-op. Setting this object to destroy(6) will remove the corresponding VLAN encapsulation interface, remove the entry in this table, and remove the corresponding entry in the ifTable. In order for a set of this object to destroy(6) to succeed, all dependencies on this row must have been removed. These will include any references to this interface in the ifStackTable.')
a3ComNextAvailableVirtIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComNextAvailableVirtIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComNextAvailableVirtIfIndex.setDescription("The value of the next available virtual ifIndex. This object is used by an NMS to select an index value for row-creation in tables indexed by ifIndex. The current value of this object is changed to a new value when the current value is written to an agent's table, that is indexed by ifIndex. Row creation using the current value of this object, allocates a virtual ifIndex. Note the following: 1. A newly created row does not have to be active(1) for the agent to allocate the virtual ifIndex. 2. Race conditions between multiple NMS's end when a row is created. Rows are deemed created when a setRequest is successfully committed (i.e. the errorStats is noError(0)). 3. An agent that exhausts its supply of virual ifIndex values returns zero as the value of this object. This can be used by an NMS as an indication to deleted unused rows and reboot the device.")
mibBuilder.exportSymbols("GENERIC-3COM-VLAN-MIB-1-0-1", a3ComNextAvailableVirtIfIndex=a3ComNextAvailableVirtIfIndex, generic=generic, RowStatus=RowStatus, a3ComVlanEncapsIfStatus=a3ComVlanEncapsIfStatus, a3ComEncapsulationGroup=a3ComEncapsulationGroup, a3ComIpVlanIpNetMask=a3ComIpVlanIpNetMask, a3ComVlanEncapsIfIndex=a3ComVlanEncapsIfIndex, a3ComVlanGroup=a3ComVlanGroup, a3ComIpVlanIpNetAddress=a3ComIpVlanIpNetAddress, a3ComVlanEncapsIfType=a3ComVlanEncapsIfType, a3ComVlanGlobalMappingTable=a3ComVlanGlobalMappingTable, a3ComVlanEncapsIfEntry=a3ComVlanEncapsIfEntry, a3ComVlanIfTable=a3ComVlanIfTable, a3ComVlanProtocolsGroup=a3ComVlanProtocolsGroup, a3ComVlanGlobalMappingIfIndex=a3ComVlanGlobalMappingIfIndex, a3ComVlanEncapsIfTag=a3ComVlanEncapsIfTag, a3ComVlanIfIndex=a3ComVlanIfIndex, a3ComVlanIfDescr=a3ComVlanIfDescr, A3ComVlanEncapsType=A3ComVlanEncapsType, a3ComVlanEncapsIfTable=a3ComVlanEncapsIfTable, a3ComIpVlanStatus=a3ComIpVlanStatus, a3ComVlanGlobalMappingIdentifier=a3ComVlanGlobalMappingIdentifier, a3ComVlanIfGlobalIdentifier=a3ComVlanIfGlobalIdentifier, genVirtual=genVirtual, a3ComIpVlanTable=a3ComIpVlanTable, a3ComIpVlanEntry=a3ComIpVlanEntry, a3ComVirtualGroup=a3ComVirtualGroup, a3ComVlanIfIgnoreStpFlag=a3ComVlanIfIgnoreStpFlag, a3ComVlanIfInfo=a3ComVlanIfInfo, a3Com=a3Com, genExperimental=genExperimental, a3ComVlanIfType=a3ComVlanIfType, a3ComVlanIfStatus=a3ComVlanIfStatus, a3ComVlanIfEntry=a3ComVlanIfEntry, a3ComVlanGlobalMappingEntry=a3ComVlanGlobalMappingEntry, A3ComVlanType=A3ComVlanType)