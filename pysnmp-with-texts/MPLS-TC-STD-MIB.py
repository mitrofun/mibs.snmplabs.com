#
# PySNMP MIB module MPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, iso, Bits, transmission, Unsigned32, Counter64, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "iso", "Bits", "transmission", "Unsigned32", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 1))
mplsTCStdMIB.setRevisions(('2004-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTCStdMIB.setRevisionsDescriptions(('Initial version published as part of RFC 3811.',))
if mibBuilder.loadTexts: mplsTCStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsTCStdMIB.setOrganization('IETF Multiprotocol Label Switching (MPLS) Working Group.')
if mibBuilder.loadTexts: mplsTCStdMIB.setContactInfo(' Thomas D. Nadeau Cisco Systems, Inc. tnadeau@cisco.com Joan Cucchiara Marconi Communications, Inc. jcucchiara@mindspring.com Cheenu Srinivasan Bloomberg L.P. cheenu@bloomberg.net Arun Viswanathan Force10 Networks, Inc. arunv@force10networks.com Hans Sjostrand ipUnplugged hans@ipunplugged.com Kireeti Kompella Juniper Networks kireeti@juniper.net Email comments to the MPLS WG Mailing List at mpls@uu.net.')
if mibBuilder.loadTexts: mplsTCStdMIB.setDescription('Copyright (C) The Internet Society (2004). The initial version of this MIB module was published in RFC 3811. For full legal notices see the RFC itself or see: http://www.ietf.org/copyrights/ianamib.html This MIB module defines TEXTUAL-CONVENTIONs for concepts used in Multiprotocol Label Switching (MPLS) networks.')
mplsStdMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'MPLS using LDP and ATM VC Switching, RFC3035.'
    description = 'A Label Switching Router (LSR) that creates LDP sessions on ATM interfaces uses the VCI or VPI/VCI field to hold the LDP Label. VCI values MUST NOT be in the 0-31 range. The values 0 to 31 are reserved for other uses by the ITU and ATM Forum. The value of 32 can only be used for the Control VC, although values greater than 32 could be configured for the Control VC. If a value from 0 to 31 is used for a VCI the management entity controlling the LDP subsystem should reject this with an inconsistentValue error. Also, if the value of 32 is used for a VC which is NOT the Control VC, this should result in an inconsistentValue error.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Unsigned32):
    description = "If the value of this object is greater than zero, then this represents the bandwidth of this MPLS interface (or Label Switched Path) in units of '1,000 bits per second'. The value, when greater than zero, represents the bandwidth of this MPLS interface (rounded to the nearest 1,000) in units of 1,000 bits per second. If the bandwidth of the MPLS interface is between ((n * 1000) - 500) and ((n * 1000) + 499), the value of this object is n, such that n > 0. If the value of this object is 0 (zero), this means that the traffic over this MPLS interface is considered to be best effort."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class MplsBurstSize(TextualConvention, Unsigned32):
    description = 'The number of octets of MPLS data that the stream may send back-to-back without concern for policing. The value of zero indicates that an implementation does not support Burst Size.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    description = 'A unique identifier for an MPLS Tunnel. This may represent an IPv4 address of the ingress or egress LSR for the tunnel. This value is derived from the Extended Tunnel Id in RSVP or the Ingress Router ID for CR-LDP.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabel(TextualConvention, Unsigned32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. MPLS Label Stack Encoding, [RFC3032]. Use of Label Switching on Frame Relay Networks, RFC3034. MPLS using LDP and ATM VC Switching, RFC3035. Generalized Multiprotocol Label Switching (GMPLS) Architecture, [RFC3471].'
    description = "This value represents an MPLS label as defined in [RFC3031], [RFC3032], [RFC3034], [RFC3035] and [RFC3471]. The label contents are specific to the label being represented, such as: * The label carried in an MPLS shim header (for LDP this is the Generic Label) is a 20-bit number represented by 4 octets. Bits 0-19 contain a label or a reserved label value. Bits 20-31 MUST be zero. The following is quoted directly from [RFC3032]. There are several reserved label values: i. A value of 0 represents the 'IPv4 Explicit NULL Label'. This label value is only legal at the bottom of the label stack. It indicates that the label stack must be popped, and the forwarding of the packet must then be based on the IPv4 header. ii. A value of 1 represents the 'Router Alert Label'. This label value is legal anywhere in the label stack except at the bottom. When a received packet contains this label value at the top of the label stack, it is delivered to a local software module for processing. The actual forwarding of the packet is determined by the label beneath it in the stack. However, if the packet is forwarded further, the Router Alert Label should be pushed back onto the label stack before forwarding. The use of this label is analogous to the use of the 'Router Alert Option' in IP packets [RFC2113]. Since this label cannot occur at the bottom of the stack, it is not associated with a particular network layer protocol. iii. A value of 2 represents the 'IPv6 Explicit NULL Label'. This label value is only legal at the bottom of the label stack. It indicates that the label stack must be popped, and the forwarding of the packet must then be based on the IPv6 header. iv. A value of 3 represents the 'Implicit NULL Label'. This is a label that an LSR may assign and distribute, but which never actually appears in the encapsulation. When an LSR would otherwise replace the label at the top of the stack with a new label, but the new label is 'Implicit NULL', the LSR will pop the stack instead of doing the replacement. Although this value may never appear in the encapsulation, it needs to be specified in the Label Distribution Protocol, so a value is reserved. v. Values 4-15 are reserved. * The frame relay label can be either 10-bits or 23-bits depending on the DLCI field size and the upper 22-bits or upper 9-bits must be zero, respectively. * For an ATM label the lower 16-bits represents the VCI, the next 12-bits represents the VPI and the remaining bits MUST be zero. * The Generalized-MPLS (GMPLS) label contains a value greater than 2^24-1 and used in GMPLS as defined in [RFC3471]."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.3.'
    description = 'The label distribution method which is also called the label advertisement mode [RFC3036]. Each interface on an LSR is configured to operate in either Downstream Unsolicited or Downstream on Demand.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class MplsLdpIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is a six octet quantity which is used to identify a Label Switching Router (LSR) label space. The first four octets identify the LSR and must be a globally unique value, such as a 32-bit router ID assigned to the LSR, and the last two octets identify a specific label space within the LSR.'
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLsrIdentifier(TextualConvention, OctetString):
    description = 'The Label Switching Router (LSR) identifier is the first 4 bytes of the Label Distribution Protocol (LDP) identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsLdpLabelType(TextualConvention, Integer32):
    description = 'The Layer 2 label types which are defined for MPLS LDP and/or CR-LDP are generic(1), atm(2), or frameRelay(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLSPID(TextualConvention, OctetString):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    description = 'A unique identifier within an MPLS network that is assigned to each LSP. This is assigned at the head end of the LSP and can be used by all LSRs to identify this LSP. This value is piggybacked by the signaling protocol when this LSP is signaled within the network. This identifier can then be used at each LSR to identify which labels are being swapped to other labels for this LSP. This object can also be used to disambiguate LSPs that share the same RSVP sessions between the same source and destination. For LSPs established using CR-LDP, the LSPID is composed of the ingress LSR Router ID (or any of its own IPv4 addresses) and a locally unique CR-LSP ID to that LSR. The first two bytes carry the CR-LSPID, and the remaining 4 bytes carry the Router ID. The LSPID is useful in network management, in CR-LSP repair, and in using an already established CR-LSP as a hop in an ER-TLV. For LSPs signaled using RSVP-TE, the LSP ID is defined as a 16-bit (2 byte) identifier used in the SENDER_TEMPLATE and the FILTER_SPEC that can be changed to allow a sender to share resources with itself. The length of this object should only be 2 or 6 bytes. If the length of this octet string is 2 bytes, then it must identify an RSVP-TE LSPID, or it is 6 bytes, it must contain a CR-LDP LSPID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(6, 6), )
class MplsLspType(TextualConvention, Integer32):
    description = 'Types of Label Switch Paths (LSPs) on a Label Switching Router (LSR) or a Label Edge Router (LER) are: unknown(1) -- if the LSP is not known to be one of the following. terminatingLsp(2) -- if the LSP terminates on the LSR/LER, then this is an egressing LSP which ends on the LSR/LER, originatingLsp(3) -- if the LSP originates from this LSR/LER, then this is an ingressing LSP which is the head-end of the LSP, crossConnectingLsp(4) -- if the LSP ingresses and egresses on the LSR, then it is cross-connecting on that LSR.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("terminatingLsp", 2), ("originatingLsp", 3), ("crossConnectingLsp", 4))

class MplsOwner(TextualConvention, Integer32):
    description = 'This object indicates the local network management subsystem that originally created the object(s) in question. The values of this enumeration are defined as follows: unknown(1) - the local network management subsystem cannot discern which component created the object. other(2) - the local network management subsystem is able to discern which component created the object, but the component is not listed within the following choices, e.g., command line interface (cli). snmp(3) - The Simple Network Management Protocol was used to configure this object initially. ldp(4) - The Label Distribution Protocol was used to configure this object initially. crldp(5) - The Constraint-Based Label Distribution Protocol was used to configure this object initially. rsvpTe(6) - The Resource Reservation Protocol was used to configure this object initially. policyAgent(7) - A policy agent (perhaps in combination with one of the above protocols) was used to configure this object initially. An object created by any of the above choices MAY be modified or destroyed by the same or a different choice.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmp", 3), ("ldp", 4), ("crldp", 5), ("rsvpTe", 6), ("policyAgent", 7))

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific path used by a tunnel. A value of 0 (zero) means that no path is in use.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsPathIndex(TextualConvention, Unsigned32):
    description = 'A unique value to index (by Path number) an entry in a table.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.2.'
    description = 'The label retention mode which specifies whether an LSR maintains a label binding for a FEC learned from a neighbor that is not its next hop for the FEC. If the value is conservative(1) then advertised label mappings are retained only if they will be used to forward packets, i.e., if label came from a valid next hop. If the value is liberal(2) then all advertised label mappings are retained whether they are from a valid next hop or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, RFC3209, Section 4.7.4.'
    description = 'Describes the configured 32-bit Include-any, include-all, or exclude-all constraint for constraint-based link selection.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsTunnelIndex(TextualConvention, Unsigned32):
    description = 'A unique index into mplsTunnelTable. For tunnels signaled using RSVP, this value should correspond to the RSVP Tunnel ID used for the RSVP-TE session.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    description = 'The tunnel entry with instance index 0 should refer to the configured tunnel interface (if one exists). Values greater than 0, but less than or equal to 65535, should be used to indicate signaled (or backup) tunnel LSP instances. For tunnel LSPs signaled using RSVP, this value should correspond to the RSVP LSP ID used for the RSVP-TE LSP. Values greater than 65535 apply to FRR detour instances.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 4294967295), )
class TeHopAddressType(TextualConvention, Integer32):
    reference = 'TEXTUAL-CONVENTIONs for Internet Network Addresses, RFC3291. Constraint-Based LSP Setup using LDP, [RFC3212]'
    description = 'A value that represents a type of address for a Traffic Engineered (TE) Tunnel hop. unknown(0) An unknown address type. This value MUST be used if the value of the corresponding TeHopAddress object is a zero-length string. It may also be used to indicate a TeHopAddress which is not in one of the formats defined below. ipv4(1) An IPv4 network address as defined by the InetAddressIPv4 TEXTUAL-CONVENTION [RFC3291]. ipv6(2) A global IPv6 address as defined by the InetAddressIPv6 TEXTUAL-CONVENTION [RFC3291]. asnumber(3) An Autonomous System (AS) number as defined by the TeHopAddressAS TEXTUAL-CONVENTION. unnum(4) An unnumbered interface index as defined by the TeHopAddressUnnum TEXTUAL-CONVENTION. lspid(5) An LSP ID for TE Tunnels (RFC3212) as defined by the MplsLSPID TEXTUAL-CONVENTION. Each definition of a concrete TeHopAddressType value must be accompanied by a definition of a TEXTUAL-CONVENTION for use with that TeHopAddress. To support future extensions, the TeHopAddressType TEXTUAL-CONVENTION SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that TeHopAddressType objects and any dependent objects (e.g., TeHopAddress objects) are consistent. An inconsistentValue error must be generated if an attempt to change a TeHopAddressType object would, for example, lead to an undefined TeHopAddress value that is not defined herein. In particular, TeHopAddressType/TeHopAddress pairs must be changed together if the address type changes (e.g., from ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("asnumber", 3), ("unnum", 4), ("lspid", 5))

class TeHopAddress(TextualConvention, OctetString):
    description = "Denotes a generic Tunnel hop address, that is, the address of a node which an LSP traverses, including the source and destination nodes. An address may be very concrete, for example, an IPv4 host address (i.e., with prefix length 32); if this IPv4 address is an interface address, then that particular interface must be traversed. An address may also specify an 'abstract node', for example, an IPv4 address with prefix length less than 32, in which case, the LSP can traverse any node whose address falls in that range. An address may also specify an Autonomous System (AS), in which case the LSP can traverse any node that falls within that AS. A TeHopAddress value is always interpreted within the context of an TeHopAddressType value. Every usage of the TeHopAddress TEXTUAL-CONVENTION is required to specify the TeHopAddressType object which provides the context. It is suggested that the TeHopAddressType object is logically registered before the object(s) which use the TeHopAddress TEXTUAL-CONVENTION if they appear in the same logical row. The value of a TeHopAddress object must always be consistent with the value of the associated TeHopAddressType object. Attempts to set a TeHopAddress object to a value which is inconsistent with the associated TeHopAddressType must fail with an inconsistentValue error."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TeHopAddressAS(TextualConvention, OctetString):
    reference = 'Textual Conventions for Internet Network Addresses, [RFC3291]. The InetAutonomousSystemsNumber TEXTUAL-CONVENTION has a SYNTAX of Unsigned32, whereas this TC has a SYNTAX of OCTET STRING (SIZE (4)). Both TCs represent an autonomous system number but use different syntaxes to do so.'
    description = 'Represents a two or four octet AS number. The AS number is represented in network byte order (MSB first). A two-octet AS number has the two MSB octets set to zero.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TeHopAddressUnnum(TextualConvention, OctetString):
    description = 'Represents an unnumbered interface: octets contents encoding 1-4 unnumbered interface network-byte order The corresponding TeHopAddressType value is unnum(5).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

mibBuilder.exportSymbols("MPLS-TC-STD-MIB", MplsLspType=MplsLspType, MplsBitRate=MplsBitRate, TeHopAddressAS=TeHopAddressAS, TeHopAddressType=TeHopAddressType, MplsTunnelIndex=MplsTunnelIndex, PYSNMP_MODULE_ID=mplsTCStdMIB, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsRetentionMode=MplsRetentionMode, MplsLdpIdentifier=MplsLdpIdentifier, MplsOwner=MplsOwner, MplsLabel=MplsLabel, MplsLabelDistributionMethod=MplsLabelDistributionMethod, mplsTCStdMIB=mplsTCStdMIB, MplsTunnelAffinity=MplsTunnelAffinity, mplsStdMIB=mplsStdMIB, MplsLsrIdentifier=MplsLsrIdentifier, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsBurstSize=MplsBurstSize, MplsPathIndex=MplsPathIndex, TeHopAddressUnnum=TeHopAddressUnnum, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, MplsLSPID=MplsLSPID, MplsLdpLabelType=MplsLdpLabelType, TeHopAddress=TeHopAddress, MplsPathIndexOrZero=MplsPathIndexOrZero)
