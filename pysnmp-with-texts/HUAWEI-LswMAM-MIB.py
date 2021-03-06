#
# PySNMP MIB module HUAWEI-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswMAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
hwdot1qVlanIndex, = mibBuilder.importSymbols("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Bits, Counter32, Integer32, Unsigned32, IpAddress, Counter64, Gauge32, MibIdentifier, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Bits", "Counter32", "Integer32", "Unsigned32", "IpAddress", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
hwLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3))
hwLswMacPort.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLswMacPort.setRevisionsDescriptions((' ',))
if mibBuilder.loadTexts: hwLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswMacPort.setOrganization(' ')
if mibBuilder.loadTexts: hwLswMacPort.setContactInfo(' ')
if mibBuilder.loadTexts: hwLswMacPort.setDescription(' ')
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'

hwdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1), )
if mibBuilder.loadTexts: hwdot1qMacSearchTable.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchTable.setDescription('Information table for searching port with mac address ')
hwdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1), ).setIndexNames((0, "HUAWEI-LswMAM-MIB", "hwdot1qMacSearchAddress"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hwdot1qMacSearchEntry.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchEntry.setDescription(' Information table for searching port with mac address entry ')
hwdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAddress.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchAddress.setDescription('MAC address')
hwdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchVlanID.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchVlanID.setDescription(' VLANID of the native VLAN of the MAC address to be searched for ')
hwdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchPort.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchPort.setDescription('Interface index corresponding to the MAC address')
hwdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAgeTime.setStatus('current')
if mibBuilder.loadTexts: hwdot1qMacSearchAgeTime.setDescription(' Address aging time')
hwdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2), )
if mibBuilder.loadTexts: hwdot1qTpFdbSetTable.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetTable.setDescription('Unicast address setting table ')
hwdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbSetEntry.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetEntry.setDescription(' Unicast address setting table entry ')
hwdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbSetAddress.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetAddress.setDescription('Unicast MAC address ')
hwdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetPort.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetPort.setDescription('Interface index corresponding to the MAC address ')
hwdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetStatus.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetStatus.setDescription('State corresponding to the MAC address')
hwdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetOperate.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbSetOperate.setDescription('Add or delete an MAC address. Read operation not supported.')
hwdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3), )
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetTable.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetTable.setDescription('Multistcast address setting table, whose maximal row number is dynamically changed by the influence of IGSP. When reaching the upper limit of the table, no more row could be added, then an error will be returned.')
hwdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetEntry.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetEntry.setDescription('Multicast address setting table entry.')
hwdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetAddress.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetAddress.setDescription('Multicast MAC address.')
hwdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetPort.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetPort.setDescription('The complete set of ports, in this VLAN, to which frames destined to this Multicast MAC address are currently being explicitly forwarded. This does not include ports for which this address is only implicitly forwarded.')
hwdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetOperate.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetOperate.setDescription('Add or delete a Multicast MAC address. Read operation is meaningless. When adding a Multicast MAC address, it is required to provide MacAddress, VLAN and PortList all. For deleting operation, MacAddress and VLAN must be provided, but hwdot1qTpFdbGroupSetPort is optional.')
mibBuilder.exportSymbols("HUAWEI-LswMAM-MIB", hwdot1qTpFdbSetPort=hwdot1qTpFdbSetPort, hwdot1qTpFdbSetAddress=hwdot1qTpFdbSetAddress, hwdot1qMacSearchAddress=hwdot1qMacSearchAddress, hwdot1qTpFdbGroupSetTable=hwdot1qTpFdbGroupSetTable, hwdot1qTpFdbSetStatus=hwdot1qTpFdbSetStatus, hwdot1qMacSearchAgeTime=hwdot1qMacSearchAgeTime, hwdot1qTpFdbSetOperate=hwdot1qTpFdbSetOperate, hwdot1qTpFdbSetEntry=hwdot1qTpFdbSetEntry, PYSNMP_MODULE_ID=hwLswMacPort, hwdot1qTpFdbGroupSetPort=hwdot1qTpFdbGroupSetPort, hwdot1qTpFdbSetTable=hwdot1qTpFdbSetTable, hwdot1qTpFdbGroupSetAddress=hwdot1qTpFdbGroupSetAddress, hwdot1qTpFdbGroupSetOperate=hwdot1qTpFdbGroupSetOperate, hwdot1qMacSearchVlanID=hwdot1qMacSearchVlanID, PortList=PortList, InterfaceIndex=InterfaceIndex, hwLswMacPort=hwLswMacPort, hwdot1qMacSearchPort=hwdot1qMacSearchPort, hwdot1qMacSearchEntry=hwdot1qMacSearchEntry, hwdot1qMacSearchTable=hwdot1qMacSearchTable, hwdot1qTpFdbGroupSetEntry=hwdot1qTpFdbGroupSetEntry)
