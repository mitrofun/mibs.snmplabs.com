#
# PySNMP MIB module SONUS-ATM-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-ATM-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AtmVcIdentifier, AtmVpIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, iso, MibIdentifier, Unsigned32, Integer32, Gauge32, ObjectIdentity, Counter32, IpAddress, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "MibIdentifier", "Unsigned32", "Integer32", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
sonusEventClass, sonusEventDescription, sonusEventLevel = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusEventClass", "sonusEventDescription", "sonusEventLevel")
sonusNifPort, sonusNifIndex, sonusNifSlot, sonusNifShelf = mibBuilder.importSymbols("SONUS-IP-INTERFACE-MIB", "sonusNifPort", "sonusNifIndex", "sonusNifSlot", "sonusNifShelf")
sonusPacketMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusPacketMIBs")
SonusSlotIndex, SonusShelfIndex = mibBuilder.importSymbols("SONUS-TC", "SonusSlotIndex", "SonusShelfIndex")
sonusAtmExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5))
if mibBuilder.loadTexts: sonusAtmExtMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusAtmExtMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusAtmExtMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusAtmExtMIB.setDescription('The MIB Module for Sonus ATM extensions.')
sonusAtmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1))
sonusAtmExtVclAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1), )
if mibBuilder.loadTexts: sonusAtmExtVclAdmnTable.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnTable.setDescription('The Virtual Channel Link (VCL) Extension table.')
sonusAtmExtVclAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1), ).setIndexNames((0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnIfIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"))
if mibBuilder.loadTexts: sonusAtmExtVclAdmnEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnEntry.setDescription('An entry in the VCL Extension table. This entry adds additional objects to the atmVclTable. A row is added to this table when a row is created in the atmVclTable.')
sonusAtmExtVclAdmnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnIfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnIfIndex.setDescription('The ifIndex value of the NIF that VCL is on.')
sonusAtmExtVclAdmnVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnVpi.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnVpi.setDescription('The VPI value of the VCL.')
sonusAtmExtVclAdmnVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnVci.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnVci.setDescription('The VCI value of the VCL.')
sonusAtmExtVclAdmnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("outOfService", 1), ("inService", 2))).clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnMode.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnMode.setDescription('The operation mode for VC.')
sonusAtmExtVclAdmnAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dryUp", 1), ("force", 2))).clone('dryUp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnAction.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnAction.setDescription('The dryup option for VC.')
sonusAtmExtVclAdmnTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnTimeout.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnTimeout.setDescription('The dryup timeout in minute. The default is one hour ')
sonusAtmExtVclAdmnState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnState.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnState.setDescription('A VCL must be enabled before System Manager will fully recognize it. The VCL must be disabled before the server module can be deleted.')
sonusAtmExtVclAdmnOutOfServiceReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("admin", 2), ("gateway", 3), ("portDown", 4), ("serverDown", 5), ("srvrAbsent", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnOutOfServiceReason.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnOutOfServiceReason.setDescription('The reason of ATM VC being out of service. The NIF could be out of service due to one of the following reasons: operator initiated command, gateway not responding to arp request, port failure/outOfService, or server failure/outOfService. The notApplicable is set when the ATM VC is inService or dryUp state')
sonusAtmExtVclAdmnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnRowStatus.setDescription('')
sonusAtmExtVclAdmnBwDeviation = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnBwDeviation.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnBwDeviation.setDescription('The deviation between actual and expected VCL bandwidth in percentage of the overall VCL bandwidth. If actual bandwidth is greater than the expected bandwdith plus deviation amount, a trap will be set and the trap will be only cleared when the actual bandwidth dropped below the expected bandwidth. If the actual bandwidth is lower than the expected badniwdth minus 2 times of deviation amount, a different trap will be set and the trap will be cleared when the actual bandwdith reaches the expected bandwidth. ')
sonusAtmExtVclAdmnBwContingency = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtVclAdmnBwContingency.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclAdmnBwContingency.setDescription('The percentage of the overall VCL bandwidth is reserved for contigency. If actual bandwidth is greater than the expected bandwdith and less than the overall VCL bandwidth minus contingency amount, calls will still be accepted. ')
sonusAtmExtVclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2), )
if mibBuilder.loadTexts: sonusAtmExtVclStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatTable.setDescription('The Virtual Channel Link (VCL) Extension stat table.')
sonusAtmExtVclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1), ).setIndexNames((0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatIfIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatVpi"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatVci"))
if mibBuilder.loadTexts: sonusAtmExtVclStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatEntry.setDescription('An entry in the VCL Extension stat table.')
sonusAtmExtVclStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatIfIndex.setDescription('The ifIndex value of the NIF that VCL is on.')
sonusAtmExtVclStatVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatVpi.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatVpi.setDescription('The VPI value of the VCL.')
sonusAtmExtVclStatVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatVci.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatVci.setDescription('The VCI value of the VCL.')
sonusAtmExtVclStatState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("outOfService", 1), ("inService", 2), ("dryUp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatState.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatState.setDescription('VCL enrties are created with a state of inService. A VCL which is outOfService has had all active calls terminated. A VCL must be outOfService in order to change its state to disabled.')
sonusAtmExtVclStatCallNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatCallNum.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatCallNum.setDescription('The number of calls on this VCL')
sonusAtmExtVclStatSpeedCur = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedCur.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedCur.setDescription('The current speed(bandwidth) allocated on this VCL')
sonusAtmExtVclStatSpeedMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedMax.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedMax.setDescription('The maximum speed allowed on this VCL')
sonusAtmExtVclStatSpeedActual = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedActual.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedActual.setDescription('The actual speed(bandwidth) on this VCL')
sonusAtmExtVclStatSpeedDeviation = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedDeviation.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclStatSpeedDeviation.setDescription('The actual speed(bandwidth) deviation on this VCL')
sonusAtmExtAtmLayerTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3), )
if mibBuilder.loadTexts: sonusAtmExtAtmLayerTable.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerTable.setDescription('The ATM layer table. This table maps ATM layer ifIndex to a shelf, slot, and port.')
sonusAtmExtAtmLayerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1), ).setIndexNames((0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerShelfIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerSlotIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerPortIndex"))
if mibBuilder.loadTexts: sonusAtmExtAtmLayerEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerEntry.setDescription('An entry in the ATM layer table. This entry maps the ifIndex of the ATM layer to a shelf, slot and port. A row is added to this table when a SONET port is created')
sonusAtmExtAtmLayerShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 1), SonusShelfIndex())
if mibBuilder.loadTexts: sonusAtmExtAtmLayerShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerShelfIndex.setDescription('The index for a Sonus shelf.')
sonusAtmExtAtmLayerSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 2), SonusSlotIndex())
if mibBuilder.loadTexts: sonusAtmExtAtmLayerSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerSlotIndex.setDescription('The index for a Sonus slot.')
sonusAtmExtAtmLayerPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: sonusAtmExtAtmLayerPortIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerPortIndex.setDescription('The index for a logical ATM layer port.')
sonusAtmExtAtmLayerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtAtmLayerIfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerIfIndex.setDescription('The ifIndex at the ATM layer for this shelf, slot, and port.')
sonusAtmExtAtmLayerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sonusAtmExtAtmLayerRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAtmLayerRowStatus.setDescription('This object is used to create, delete, or modify a row in this table.')
sonusAtmExtAal5LayerTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4), )
if mibBuilder.loadTexts: sonusAtmExtAal5LayerTable.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerTable.setDescription('The AAL5 layer table. This table maps AAL5 layer ifIndex to a shelf, slot, and port.')
sonusAtmExtAal5LayerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1), ).setIndexNames((0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerShelfIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerSlotIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerPortIndex"))
if mibBuilder.loadTexts: sonusAtmExtAal5LayerEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerEntry.setDescription('An entry in the AAL5 layer table. This entry maps the ifIndex of the AAL5 layer to a shelf, slot and port. A row is added to this table when a SONET port is created')
sonusAtmExtAal5LayerShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 1), SonusShelfIndex())
if mibBuilder.loadTexts: sonusAtmExtAal5LayerShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerShelfIndex.setDescription('The index for a Sonus shelf.')
sonusAtmExtAal5LayerSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 2), SonusSlotIndex())
if mibBuilder.loadTexts: sonusAtmExtAal5LayerSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerSlotIndex.setDescription('The index for a Sonus slot.')
sonusAtmExtAal5LayerPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: sonusAtmExtAal5LayerPortIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerPortIndex.setDescription('The index for a logical AAL5 layer port.')
sonusAtmExtAal5LayerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtAal5LayerIfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerIfIndex.setDescription('The ifIndex at the AAL5 layer for this shelf, slot, and port.')
sonusAtmExtAal5LayerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sonusAtmExtAal5LayerRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtAal5LayerRowStatus.setDescription('This object is used to create, delete, or modify a row in this table.')
sonusAtmExtOamF5Table = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5), )
if mibBuilder.loadTexts: sonusAtmExtOamF5Table.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5Table.setDescription('A list of ATM OAM F5 entries.')
sonusAtmExtOamF5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1), ).setIndexNames((0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5IfIndex"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5Vpi"), (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5Vci"))
if mibBuilder.loadTexts: sonusAtmExtOamF5Entry.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5Entry.setDescription('An entry of sonusAtmExtOamF5Table which is used to provide OAM feature for Virtual circuit in this ATM interface. Three major OAM functions are supported in this MIB entry. The first function is the Loopback capability for this virtual circuit which includes both of End2end Loopback and UNILoopback. The second function is the OAM continuity capability for this virtual circuit which uses Loopback cells to transmit periodically. Transmit and recieve loopback cell statisitics can be used to determine if there is continuity. The third function is basic fault management feature using AIS/RDI cells to inform the upstream/downstream failure condition, the counters are used to keep failure statistics.')
sonusAtmExtOamF5IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: sonusAtmExtOamF5IfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5IfIndex.setDescription('The ifIndex of this entry.')
sonusAtmExtOamF5Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: sonusAtmExtOamF5Vpi.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5Vpi.setDescription('The virtual path identifier of this entry')
sonusAtmExtOamF5Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: sonusAtmExtOamF5Vci.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5Vci.setDescription('The virtual circuit identifier of this entry')
sonusAtmExtOamF5Enable = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtOamF5Enable.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5Enable.setDescription('This objects is used to enable or disable the F5 OAM loopback cells. Whenever this object is set to enable, at least one F5 OAM loopback cell will be sent. If the loopback timer is non-zero, then F5 OAM loopback cells will be sent continuosly at the interval defined by the loopback timer to perform a continuity test.')
sonusAtmExtOamF5LoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("end2end", 1), ("uni", 2))).clone('end2end')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtOamF5LoopbackType.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5LoopbackType.setDescription('This object is used to define the F5 OAM loopback type for this virtual circuit. Loopback cells may be sent to the local UNI or end to end.')
sonusAtmExtOamF5LoopbackTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAtmExtOamF5LoopbackTimer.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5LoopbackTimer.setDescription('This object is used to define the time between OAM F5 loopback cells. If this object is set to zero, then a single F5 OAM cell will be sent every time the sonusAtmOamF5Enable object is set to enable. If this obkect is non-zero, then loopback cells will be sent continuously at the interval defined by this object to perform a continuity test.')
sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure.setDescription('This is a counter object to collect the end2endLoopback failure statistics for this virtual circuit. It counts end to end F5 OAM loopback cells received with an error.')
sonusAtmExtOamF5ReceiveUNILoopbackFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveUNILoopbackFailure.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveUNILoopbackFailure.setDescription('This is a counter object to collect the UNILoopback failure statistics for this virtual circuit. It counts UNI F5 OAM loopback cells received with an error.')
sonusAtmExtOamF5TransmitEnd2EndLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitEnd2EndLoopback.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitEnd2EndLoopback.setDescription('This is a counter object to collect the all transmitted end2endLoopback statistics for this virtual circuit. It counts end to end F5 OAM loopback cells sent.')
sonusAtmExtOamF5TransmitUNILoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitUNILoopback.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitUNILoopback.setDescription('This is a counter object to collect the all transmitted UNILoopback statistics for this virtual circuit. It counts UNI F5 OAM loopback cells sent.')
sonusAtmExtOamF5ReceiveEnd2EndLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndLoopback.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndLoopback.setDescription('This is a counter object to collect the all received end2endLoopback statistics for this virtual circuit. It counts good end to end F5 OAM loopback cells received.')
sonusAtmExtOamF5ReceiveUNILoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveUNILoopback.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveUNILoopback.setDescription('This is a counter object to collect the all received UNILoopback statistics for this virtual circuit. It counts good UNI F5 OAM loopback cells received.')
sonusAtmExtOamF5ReceiveEnd2EndAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndAIS.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndAIS.setDescription('This is a counter object to collect the end2endAIS cells received in this virtual circuit.')
sonusAtmExtOamF5ReceiveEnd2EndRDI = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndRDI.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5ReceiveEnd2EndRDI.setDescription('This is a counter object to collect the end2endRDI cells received in this virtual circuit.')
sonusAtmExtOamF5TransmitEnd2EndRDI = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitEnd2EndRDI.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtOamF5TransmitEnd2EndRDI.setDescription('This is a counter object to collect the end2endRDI cells transmit in this virtual circuit.')
sonusAtmExtVclMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2))
sonusAtmExtVclMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0))
sonusAtmExtVclMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 1))
sonusAtmExtVclInServiceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 1)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclInServiceNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclInServiceNotification.setDescription('This trap indicates that an ATM VC is available to support call processing.')
sonusAtmExtVclOutOfServiceNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 2)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnOutOfServiceReason"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclOutOfServiceNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclOutOfServiceNotification.setDescription('This trap indicates that an ATM VC is no longer available to support call processing.')
sonusAtmExtVclEnabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 3)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclEnabledNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclEnabledNotification.setDescription("This trap indicates that an ATM VC's configuration is enabled.")
sonusAtmExtVclDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 4)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclDisabledNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclDisabledNotification.setDescription("This trap indicates that an ATM VC's configuration is disabled.")
sonusAtmExtVclDeletedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 5)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclDeletedNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclDeletedNotification.setDescription("This trap indicates that an ATM VC's configuration is deleted.")
sonusAtmExtVclHighWatermarkNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 6)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclHighWatermarkNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclHighWatermarkNotification.setDescription("This trap indicates that an ATM VC's high watermark has been reached the first time since the ATM VC's low watermark has beend reached.")
sonusAtmExtVclLowWatermarkNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 7)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclLowWatermarkNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclLowWatermarkNotification.setDescription("This trap indicates that an ATM VC's low watermark has been reached the first time since the ATM VC's high watermark has been reached.")
sonusAtmExtVclBwHighDeviationNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 8)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclBwHighDeviationNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclBwHighDeviationNotification.setDescription("This trap indicates that a VCL's actual bandwidth is greater than the expected bandwidth plus deviation amount. This trap will be re-armed when the actual bandwdith dropped below the expected level. ")
sonusAtmExtVclBwLowDeviationNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 9)).setObjects(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"), ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"), ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"), ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"), ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAtmExtVclBwLowDeviationNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAtmExtVclBwLowDeviationNotification.setDescription("This trap indicates that a VCL's actual bandwidth is lower than the expected bandwidth minus 2 times the deviation amount.This trap will be re-armed when the actual bandwdith reached the expected level.")
mibBuilder.exportSymbols("SONUS-ATM-EXTENSIONS-MIB", sonusAtmExtOamF5Enable=sonusAtmExtOamF5Enable, sonusAtmExtVclStatVci=sonusAtmExtVclStatVci, sonusAtmExtOamF5Vci=sonusAtmExtOamF5Vci, sonusAtmExtAal5LayerEntry=sonusAtmExtAal5LayerEntry, sonusAtmExtVclAdmnAction=sonusAtmExtVclAdmnAction, sonusAtmExtAal5LayerIfIndex=sonusAtmExtAal5LayerIfIndex, sonusAtmExtOamF5ReceiveEnd2EndLoopback=sonusAtmExtOamF5ReceiveEnd2EndLoopback, sonusAtmExtOamF5ReceiveEnd2EndAIS=sonusAtmExtOamF5ReceiveEnd2EndAIS, sonusAtmExtOamF5ReceiveEnd2EndRDI=sonusAtmExtOamF5ReceiveEnd2EndRDI, sonusAtmExtVclAdmnIfIndex=sonusAtmExtVclAdmnIfIndex, sonusAtmExtVclAdmnState=sonusAtmExtVclAdmnState, sonusAtmExtVclAdmnBwContingency=sonusAtmExtVclAdmnBwContingency, sonusAtmExtVclAdmnMode=sonusAtmExtVclAdmnMode, sonusAtmExtVclStatSpeedActual=sonusAtmExtVclStatSpeedActual, sonusAtmExtVclMIBNotifications=sonusAtmExtVclMIBNotifications, sonusAtmExtMIBObjects=sonusAtmExtMIBObjects, sonusAtmExtAtmLayerSlotIndex=sonusAtmExtAtmLayerSlotIndex, sonusAtmExtVclMIBNotificationsObjects=sonusAtmExtVclMIBNotificationsObjects, sonusAtmExtOamF5Entry=sonusAtmExtOamF5Entry, sonusAtmExtVclHighWatermarkNotification=sonusAtmExtVclHighWatermarkNotification, sonusAtmExtVclStatState=sonusAtmExtVclStatState, sonusAtmExtAal5LayerRowStatus=sonusAtmExtAal5LayerRowStatus, sonusAtmExtVclMIBNotificationsPrefix=sonusAtmExtVclMIBNotificationsPrefix, sonusAtmExtVclDisabledNotification=sonusAtmExtVclDisabledNotification, sonusAtmExtOamF5TransmitUNILoopback=sonusAtmExtOamF5TransmitUNILoopback, sonusAtmExtOamF5IfIndex=sonusAtmExtOamF5IfIndex, sonusAtmExtAtmLayerTable=sonusAtmExtAtmLayerTable, sonusAtmExtVclBwHighDeviationNotification=sonusAtmExtVclBwHighDeviationNotification, sonusAtmExtVclBwLowDeviationNotification=sonusAtmExtVclBwLowDeviationNotification, sonusAtmExtVclAdmnVpi=sonusAtmExtVclAdmnVpi, sonusAtmExtOamF5Table=sonusAtmExtOamF5Table, sonusAtmExtAal5LayerTable=sonusAtmExtAal5LayerTable, sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure=sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure, sonusAtmExtAtmLayerPortIndex=sonusAtmExtAtmLayerPortIndex, sonusAtmExtAtmLayerShelfIndex=sonusAtmExtAtmLayerShelfIndex, sonusAtmExtAtmLayerIfIndex=sonusAtmExtAtmLayerIfIndex, sonusAtmExtVclInServiceNotification=sonusAtmExtVclInServiceNotification, sonusAtmExtVclStatTable=sonusAtmExtVclStatTable, sonusAtmExtVclStatSpeedMax=sonusAtmExtVclStatSpeedMax, sonusAtmExtVclLowWatermarkNotification=sonusAtmExtVclLowWatermarkNotification, sonusAtmExtVclStatSpeedDeviation=sonusAtmExtVclStatSpeedDeviation, sonusAtmExtVclEnabledNotification=sonusAtmExtVclEnabledNotification, sonusAtmExtVclAdmnOutOfServiceReason=sonusAtmExtVclAdmnOutOfServiceReason, sonusAtmExtVclStatSpeedCur=sonusAtmExtVclStatSpeedCur, sonusAtmExtVclAdmnTable=sonusAtmExtVclAdmnTable, sonusAtmExtVclAdmnEntry=sonusAtmExtVclAdmnEntry, sonusAtmExtVclStatVpi=sonusAtmExtVclStatVpi, sonusAtmExtOamF5TransmitEnd2EndLoopback=sonusAtmExtOamF5TransmitEnd2EndLoopback, sonusAtmExtVclAdmnBwDeviation=sonusAtmExtVclAdmnBwDeviation, sonusAtmExtVclAdmnVci=sonusAtmExtVclAdmnVci, sonusAtmExtAtmLayerEntry=sonusAtmExtAtmLayerEntry, sonusAtmExtOamF5TransmitEnd2EndRDI=sonusAtmExtOamF5TransmitEnd2EndRDI, sonusAtmExtVclStatIfIndex=sonusAtmExtVclStatIfIndex, sonusAtmExtAal5LayerShelfIndex=sonusAtmExtAal5LayerShelfIndex, sonusAtmExtOamF5ReceiveUNILoopback=sonusAtmExtOamF5ReceiveUNILoopback, sonusAtmExtOamF5LoopbackType=sonusAtmExtOamF5LoopbackType, sonusAtmExtAal5LayerPortIndex=sonusAtmExtAal5LayerPortIndex, sonusAtmExtOamF5ReceiveUNILoopbackFailure=sonusAtmExtOamF5ReceiveUNILoopbackFailure, sonusAtmExtVclStatEntry=sonusAtmExtVclStatEntry, PYSNMP_MODULE_ID=sonusAtmExtMIB, sonusAtmExtVclStatCallNum=sonusAtmExtVclStatCallNum, sonusAtmExtVclAdmnRowStatus=sonusAtmExtVclAdmnRowStatus, sonusAtmExtAtmLayerRowStatus=sonusAtmExtAtmLayerRowStatus, sonusAtmExtAal5LayerSlotIndex=sonusAtmExtAal5LayerSlotIndex, sonusAtmExtVclAdmnTimeout=sonusAtmExtVclAdmnTimeout, sonusAtmExtMIB=sonusAtmExtMIB, sonusAtmExtVclDeletedNotification=sonusAtmExtVclDeletedNotification, sonusAtmExtOamF5LoopbackTimer=sonusAtmExtOamF5LoopbackTimer, sonusAtmExtOamF5Vpi=sonusAtmExtOamF5Vpi, sonusAtmExtVclOutOfServiceNotification=sonusAtmExtVclOutOfServiceNotification)
