#
# PySNMP MIB module H3C-RRPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-RRPP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
h3cRrpp = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45))
if mibBuilder.loadTexts: h3cRrpp.setLastUpdated('200412020000Z')
if mibBuilder.loadTexts: h3cRrpp.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cRrpp.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cRrpp.setDescription('The RRPP (Rapid Ring Protection protocol) provides fast protection switching to layer 2 switches interconnected in an Ethernet ring topology. When a link in the ring breaks, the RRPP can recover the data path quickly. Its protection switching is similar to what can be achieved with the Spanning Tree Protocol (STP), but the converging time is less than a second after link failure. This MIB defines management information used on products which support RRPP.')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cRrppScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 1))
h3cRrppEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cRrppEnableStatus.setStatus('current')
if mibBuilder.loadTexts: h3cRrppEnableStatus.setDescription('Indicating whether the RRPP is enabled on this switch.')
h3cRrppPassword = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="303030464532303346443735")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cRrppPassword.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPassword.setDescription('Password configured for RRPP nodes to identify the validity of a link-down message. This value must be set together with h3cRrppPasswordType which indicates whether this value can be got. This value can not be set alone without configuring h3cRrppPasswordType.')
h3cRrppPasswordType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cRrppPasswordType.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPasswordType.setDescription('Indicating whether the h3cRrppPassword can be got. simple(1):h3cRrppPassword can be got. cipher(2):h3cRrppPassword can not be got. This value can not be set alone without configuring h3cRrppPassword.')
h3cRrppProtectVlanConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("instance", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppProtectVlanConfigMode.setStatus('current')
if mibBuilder.loadTexts: h3cRrppProtectVlanConfigMode.setDescription("Indicating the mode in which the protected VLANs of an RRPP domain are configured. The value 'vlan' indicates that h3cRrppDomainProtectVlanListLow and h3cRrppDomainProtectVlanListHigh can be used for setting protected VLANs, while h3cRrppDomainInstanceListLow and h3cRrppDomainInstanceListHigh cannot. By contraries, the value 'instance' indicates that 3cRrppDomainInstanceListLow and h3cRrppDomainInstanceListHigh can be used for setting protected VLANs while the other two cannot.")
h3cRrppTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2))
h3cRrppDomainTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1), )
if mibBuilder.loadTexts: h3cRrppDomainTable.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainTable.setDescription('A table containing information about configurations and status of a RRPP domain.')
h3cRrppDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1), ).setIndexNames((0, "H3C-RRPP-MIB", "h3cRrppDomainID"))
if mibBuilder.loadTexts: h3cRrppDomainEntry.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainEntry.setDescription('Detailed information of a specified RRPP domain.')
h3cRrppDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cRrppDomainID.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainID.setDescription("An index uniquely identifies a RRPP domain, which ranges from 1~16. This value can't be modified after created.")
h3cRrppDomainControlVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 4094), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainControlVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainControlVlanID.setDescription("Index of the control VLAN specified to a domain. The value 65535 indicates the control VLAN has not been configured. The VLAN assigned to a RRPP Domain must not have been created. This value can't be modified after created.")
h3cRrppDomainHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainHelloTime.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainHelloTime.setDescription('The value indicates the interval between two hello packets sent by master-node, and its unit is second. The value ranges from 1s~10s.')
h3cRrppDomainFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainFailTime.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainFailTime.setDescription("The expiration value of the fail-period timer and its unit is second. If not receiving hello packets before this expires, the master-node considers the ring is broken. The value of this node ranging from 3s~30s must not be less than triple h3cRrppDomainHelloTime's value.")
h3cRrppDomainRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation.')
h3cRrppDomainInstanceListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainInstanceListLow.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainInstanceListLow.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 0 through 7, the second octet specifying instances 8 through 15, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. Thus, each instance to which the protected VLANs of an RRPP domain are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the RRPP domain. By contraries, the VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with h3cRrppDomainInstanceListHigh at the same time when a SET operation is performed. This object is valid only when the value of h3cRrppProtectVlanConfigMode is 'instance'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
h3cRrppDomainInstanceListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainInstanceListHigh.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainInstanceListHigh.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 2048 through 2055, the second octet specifying instances 2056 through 2063, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. The most significant bit of the last octet is invalid. Thus, each instance to which the protected VLANs of an RRPP domain are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the RRPP domain. By contraries, the VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with h3cRrppDomainInstanceListLow at the same time when a SET operation is performed. This object is valid only when the value of h3cRrppProtectVlanConfigMode is 'instance'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
h3cRrppDomainProtectVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainProtectVlanListLow.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainProtectVlanListLow.setDescription("Each octet contained in this value specifies an eight-VLAN group, with the first octet specifying VLANs 1 through 7, the second octet specifying VLANs 8 through 15, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. The least significant bit of the first octet is invalid. Thus, each protected VLAN of an RRPP domain corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the corresponding VLAN is a protected VLAN of the RRPP domain. By contraries, the VLAN is not a protected VLAN if the corresponding bit has a value of '0'. The value of this object must be set with h3cRrppDomainProtectVlanListHigh at the same time when a SET operation is performed. This object is valid only when the value of h3cRrppProtectVlanConfigMode is 'vlan'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
h3cRrppDomainProtectVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppDomainProtectVlanListHigh.setStatus('current')
if mibBuilder.loadTexts: h3cRrppDomainProtectVlanListHigh.setDescription("Each octet contained in this value specifies an eight-VLAN group, with the first octet specifying VLANs 2048 through 2055, the second octet specifying VLANs 2056 through 2063, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. The most significant bit of the last octet is invalid. Thus, each protected VLAN of an RRPP domain corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the corresponding VLAN is a protected VLAN of the RRPP domain. By contraries, the VLAN is not a protected VLAN if the corresponding bit has a value of '0'. The value of this object must be set with h3cRrppDomainProtectVlanListLow at the same time when a SET operation is performed. This object is valid only when the value of h3cRrppProtectVlanConfigMode is 'vlan'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
h3cRrppRingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2), )
if mibBuilder.loadTexts: h3cRrppRingTable.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingTable.setDescription('A table containing information about configurations and status of a RRPP Ring.')
h3cRrppRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1), ).setIndexNames((0, "H3C-RRPP-MIB", "h3cRrppDomainID"), (0, "H3C-RRPP-MIB", "h3cRrppRingID"))
if mibBuilder.loadTexts: h3cRrppRingEntry.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingEntry.setDescription('Detailed information of a specified RRPP Ring.')
h3cRrppRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cRrppRingID.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingID.setDescription("An index uniquely identifies a RRPP Ring, which ranges from 1~64. This value can't be modified after created.")
h3cRrppRingEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingEnableStatus.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingEnableStatus.setDescription('Indicating whether the RRPP is enabled on this Ring. NOTE: If major-ring and sub-ring(s) of a domain coexist on a switch, major-ring must be enabled before sub-ring is enabled. And sub-ring must be disabled before major-ring is disabled.')
h3cRrppRingActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppRingActive.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingActive.setDescription('As both h3cRrppEnableStatus and h3cRrppRingEnableStatus are enabled, the ring is activated. Whereas either of the two items is disabled, the ring is inactive.')
h3cRrppRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("health", 2), ("fault", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppRingState.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingState.setDescription('The status (i.e. unknown, health or fault) of the Ethernet ring. This is valid only on the master-node.')
h3cRrppRingNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("master", 1), ("transit", 2), ("edge", 3), ("assistantEdge", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingNodeMode.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingNodeMode.setDescription("There are four RRPP node modes for the switch on a RRPP ring, such as master, transit, edge and assistant-edge. Each RRPP ring has a single designated master-node. All other nodes except edge-node and assistant-edge-node on that ring are referred to as transit-nodes. The node mode of edge and assistant-edge should be configured only on sub-ring. When there is a common link between a sub-ring and its major-ring, the node mode of the sub-ring must be edge or assistant-edge, and they must be configured in pairs. If node mode is designated as edge or assistant-edge, several points should be noticed: Major-ring must be created before a sub-ring is created; Major-ring can't be deleted unless all its sub-rings are deleted; The node mode of the switch on major-ring must be transit; Major-ring and sub-ring must have only a common port. This value can't be modified after created.")
h3cRrppRingPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingPrimaryPort.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingPrimaryPort.setDescription("If the switch is a master-node or transit-node, this value is the primary port ifIndex; otherwise, if the switch is a edge-node or assistant-edge-node, this value is the common port ifIndex. This value can't be modified after created.")
h3cRrppRingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingSecondaryPort.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingSecondaryPort.setDescription("If the switch is a master-node or transit-node, this value is the secondary port ifIndex; otherwise, if the switch is an edge-node or assistant-edge-node, this value is the edge port ifIndex. This value can't be modified after created.")
h3cRrppRingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("majorRing", 1), ("subRing", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingLevel.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingLevel.setDescription("Level of a ring. This field should be set 1 on major-ring and 2 on the sub-ring. This value can't be modified after created.")
h3cRrppRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRrppRingRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, h3cRrppRingNodeMode, h3cRrppRingPrimaryPort, h3cRrppRingSecondaryPort and h3cRrppRingLevel must be specified.')
h3cRrppPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3), )
if mibBuilder.loadTexts: h3cRrppPortTable.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTable.setDescription('A table containing information about configurations and status of a RRPP port.')
h3cRrppPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1), ).setIndexNames((0, "H3C-RRPP-MIB", "h3cRrppDomainID"), (0, "H3C-RRPP-MIB", "h3cRrppRingID"), (0, "H3C-RRPP-MIB", "h3cRrppPortID"))
if mibBuilder.loadTexts: h3cRrppPortEntry.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortEntry.setDescription('Detailed information of a specified RRPP port.')
h3cRrppPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cRrppPortID.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortID.setDescription('ifIndex of the port.')
h3cRrppPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("common", 3), ("edge", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRole.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRole.setDescription('The RRPP role of the port. (i.e. primary, secondary, common or edge port).')
h3cRrppPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("unblocked", 2), ("blocked", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortState.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortState.setDescription('State of RRPP port, including unknown, unblocked, blocked and down.')
h3cRrppPortRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXError.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXError.setDescription('The statistics of illegal RRPP packets received from this port.')
h3cRrppPortRXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXHello.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXHello.setDescription('The statistics of hello packets received from this port on specified ring.')
h3cRrppPortRXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXLinkUp.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXLinkUp.setDescription('The statistics of link-up packets received from this port on specified ring.')
h3cRrppPortRXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXLinkDown.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXLinkDown.setDescription('The statistics of link-down packets received from this port on specified ring.')
h3cRrppPortRXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXCommonFlush.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXCommonFlush.setDescription("The statistics of common-flush packets received from this port on specified ring. Instruction When master-node receives valid link-down packets or link-up packets, it will send common-flush packets, instructing the other nodes on the ring to flush their forwarding database. When the nodes except master-node receive common-flush, they will flush forwarding database. If there is any port blocked on that node, it won't be unblocked.")
h3cRrppPortRXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXCompleteFlush.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXCompleteFlush.setDescription('The statistics of complete-flush packets received from this port on specified ring. Instruction When the ring recovers, master-node will receive its own hello packets. It will send complete-flush packets, instructing the other nodes on the ring to flush their forwarding database. When the nodes except master-node receive complete-flush, they will flush forwarding database. If there is any port blocked on that node, it will be unblocked.')
h3cRrppPortTXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXHello.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXHello.setDescription('The statistics of hello packets sent from this port on specified ring.')
h3cRrppPortTXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXLinkUp.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXLinkUp.setDescription('The statistics of link-up packets sent from this port on specified ring.')
h3cRrppPortTXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXLinkDown.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXLinkDown.setDescription('The statistics of link-down packets sent from this port on specified ring.')
h3cRrppPortTXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXCommonFlush.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXCommonFlush.setDescription('The statistics of common-flush packets sent from this port on specified ring.')
h3cRrppPortTXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXCompleteFlush.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXCompleteFlush.setDescription('The statistics of complete-flush packets sent from this port on specified ring.')
h3cRrppPortRXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXEdgeHello.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXEdgeHello.setDescription('The statistics of edge-hello packets received from this port on specified ring. When edge-node sends edge-hello packets, assistantEdge-node will receive its own edge-hello packets from the common link and the master ring.')
h3cRrppPortRXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortRXMajorFault.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortRXMajorFault.setDescription("The statistics of major-fault packets received from this port on specified ring. When assistantEdge can't receive edge-hello packets in the specified fault-time, assistantEdge-node will send its own major-fault packets from the edge port around the sub ring. Edge-node will receive the major-fault packets from its edge port. Then Edge-node will block its edge port.")
h3cRrppPortTXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXEdgeHello.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXEdgeHello.setDescription('The statistics of edge-hello packets sent from this port on specified ring.')
h3cRrppPortTXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRrppPortTXMajorFault.setStatus('current')
if mibBuilder.loadTexts: h3cRrppPortTXMajorFault.setDescription('The statistics of major-fault packets sent from this port on specified ring.')
h3cRrppNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 3))
h3cRrppRingRecover = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 3, 1)).setObjects(("H3C-RRPP-MIB", "h3cRrppDomainID"), ("H3C-RRPP-MIB", "h3cRrppRingID"))
if mibBuilder.loadTexts: h3cRrppRingRecover.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingRecover.setDescription('Trap message is generated by master-node on the ring when the ring recovers from fault.')
h3cRrppRingFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 3, 2)).setObjects(("H3C-RRPP-MIB", "h3cRrppDomainID"), ("H3C-RRPP-MIB", "h3cRrppRingID"))
if mibBuilder.loadTexts: h3cRrppRingFail.setStatus('current')
if mibBuilder.loadTexts: h3cRrppRingFail.setDescription('Trap message is generated by master-node on the ring when the ring fails.')
h3cRrppMultiMaster = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 3, 3)).setObjects(("H3C-RRPP-MIB", "h3cRrppDomainID"), ("H3C-RRPP-MIB", "h3cRrppRingID"))
if mibBuilder.loadTexts: h3cRrppMultiMaster.setStatus('current')
if mibBuilder.loadTexts: h3cRrppMultiMaster.setDescription('Trap message is generated by master-node when it detects there are more than one master-node on the ring.')
h3cRrppMajorFault = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 45, 3, 4)).setObjects(("H3C-RRPP-MIB", "h3cRrppDomainID"), ("H3C-RRPP-MIB", "h3cRrppRingID"))
if mibBuilder.loadTexts: h3cRrppMajorFault.setStatus('current')
if mibBuilder.loadTexts: h3cRrppMajorFault.setDescription('Trap message is generated by edge-node or assistant-edge-node when it detects major fault.')
mibBuilder.exportSymbols("H3C-RRPP-MIB", h3cRrppRingNodeMode=h3cRrppRingNodeMode, h3cRrppPortRXMajorFault=h3cRrppPortRXMajorFault, h3cRrppDomainInstanceListLow=h3cRrppDomainInstanceListLow, PYSNMP_MODULE_ID=h3cRrpp, h3cRrppRingState=h3cRrppRingState, h3cRrppDomainControlVlanID=h3cRrppDomainControlVlanID, h3cRrppDomainTable=h3cRrppDomainTable, h3cRrppDomainInstanceListHigh=h3cRrppDomainInstanceListHigh, h3cRrppDomainProtectVlanListHigh=h3cRrppDomainProtectVlanListHigh, h3cRrppRingLevel=h3cRrppRingLevel, h3cRrppDomainFailTime=h3cRrppDomainFailTime, h3cRrppDomainEntry=h3cRrppDomainEntry, h3cRrppPortTXCommonFlush=h3cRrppPortTXCommonFlush, h3cRrppEnableStatus=h3cRrppEnableStatus, EnabledStatus=EnabledStatus, h3cRrppPortRXLinkDown=h3cRrppPortRXLinkDown, h3cRrppPortRXCompleteFlush=h3cRrppPortRXCompleteFlush, h3cRrppPortID=h3cRrppPortID, h3cRrppRingRecover=h3cRrppRingRecover, h3cRrppPortRXLinkUp=h3cRrppPortRXLinkUp, h3cRrppPortTXHello=h3cRrppPortTXHello, h3cRrppPortTXLinkDown=h3cRrppPortTXLinkDown, h3cRrppPortState=h3cRrppPortState, h3cRrpp=h3cRrpp, h3cRrppPassword=h3cRrppPassword, h3cRrppRingActive=h3cRrppRingActive, h3cRrppPortRXEdgeHello=h3cRrppPortRXEdgeHello, h3cRrppRingRowStatus=h3cRrppRingRowStatus, h3cRrppMajorFault=h3cRrppMajorFault, h3cRrppNotifications=h3cRrppNotifications, h3cRrppRingFail=h3cRrppRingFail, h3cRrppPortRXHello=h3cRrppPortRXHello, h3cRrppPortTXLinkUp=h3cRrppPortTXLinkUp, h3cRrppProtectVlanConfigMode=h3cRrppProtectVlanConfigMode, h3cRrppPasswordType=h3cRrppPasswordType, h3cRrppPortTXCompleteFlush=h3cRrppPortTXCompleteFlush, h3cRrppRingTable=h3cRrppRingTable, h3cRrppPortRole=h3cRrppPortRole, h3cRrppTable=h3cRrppTable, h3cRrppDomainHelloTime=h3cRrppDomainHelloTime, h3cRrppRingPrimaryPort=h3cRrppRingPrimaryPort, h3cRrppDomainProtectVlanListLow=h3cRrppDomainProtectVlanListLow, h3cRrppPortRXCommonFlush=h3cRrppPortRXCommonFlush, h3cRrppPortTXEdgeHello=h3cRrppPortTXEdgeHello, h3cRrppRingEnableStatus=h3cRrppRingEnableStatus, h3cRrppPortTXMajorFault=h3cRrppPortTXMajorFault, h3cRrppMultiMaster=h3cRrppMultiMaster, h3cRrppPortRXError=h3cRrppPortRXError, h3cRrppRingEntry=h3cRrppRingEntry, h3cRrppRingSecondaryPort=h3cRrppRingSecondaryPort, h3cRrppPortEntry=h3cRrppPortEntry, h3cRrppPortTable=h3cRrppPortTable, h3cRrppScalarGroup=h3cRrppScalarGroup, h3cRrppDomainID=h3cRrppDomainID, h3cRrppDomainRowStatus=h3cRrppDomainRowStatus, h3cRrppRingID=h3cRrppRingID)
