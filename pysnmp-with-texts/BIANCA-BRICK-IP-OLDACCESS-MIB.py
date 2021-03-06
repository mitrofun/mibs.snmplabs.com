#
# PySNMP MIB module BIANCA-BRICK-IP-OLDACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-IP-OLDACCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Bits, ModuleIdentity, Counter64, iso, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Bits", "ModuleIdentity", "Counter64", "iso", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboipold = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
ipAllowTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 1), )
if mibBuilder.loadTexts: ipAllowTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowTable.setDescription("The ipAllowTable defines all allowed IP packets. Each entry describes a subset of IP Packets, which are allowed to be processed. The overall set of allowed IP packets is the union of all subsets that are described in this table. If at least one entry is defined in the ipAllowTable, only IP datagrams which are allowed by the ipAllowTable are processed by the BRICK. All other packets are refused. Please note that the ipDenyTable overwrites the ipAllowTable. IP datagrams specified in the ipDenyTable are always refused, even if they are allowed by the ipAllowTable. Creating entries: Entries are created by setting the ipAllowProtocolMode and ipAllowSrcIfIndexMode objects in one operation (on one command line). Deleting entries: Entries are deleted by setting the ipAllowProtocolMode object to 'delete'.")
ipAllowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipAllowProtocolMode"), (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipAllowSrcIfIndexMode"))
if mibBuilder.loadTexts: ipAllowEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowEntry.setDescription('')
ipAllowProtocolMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3))))
if mibBuilder.loadTexts: ipAllowProtocolMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowProtocolMode.setDescription("Specifies whether or not the protocol field of the IP datagram header should be used to determine if the datagram belongs to the subset of the entry. dont-verify(1) = don't check the protocol field; verify(2) = check the protocol field; delete(3) = delete the entry from the table")
ipAllowProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 8, 12, 17, 20, 22, 27, 89))).clone(namedValues=NamedValues(("icmp", 1), ("ggp", 3), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("hmp", 20), ("xns-idp", 22), ("rdp", 27), ("ospf", 89))))
if mibBuilder.loadTexts: ipAllowProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowProtocol.setDescription("If the ipAllowProtocolMode is set to 'verify', this object specifies the protocol of IP datagrams belonging to the subset described by this entry. Otherwise, this field has no meaning.")
ipAllowSrcIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2))))
if mibBuilder.loadTexts: ipAllowSrcIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcIfIndexMode.setDescription('This object specifies whether or not the originating interface of the IP datagram should be checked to determine whether a datagram belongs to the subset.')
ipAllowSrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: ipAllowSrcIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcIfIndex.setDescription("If ipAllowSrcIfIndexMode is set to 'verify', then this object specifies the ifIndex of the datagrams belonging to the subset defined by this entry.")
ipAllowSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 5), IpAddress())
if mibBuilder.loadTexts: ipAllowSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcAddr.setDescription('This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipAllowSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 6), IpAddress())
if mibBuilder.loadTexts: ipAllowSrcMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcMask.setDescription('This object specifies the set of IP addresses of data grams that belong to the subset defined by this entry.')
ipAllowSrcPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ignore", 1), ("specific", 2), ("clients", 3), ("server", 4), ("unpriv", 5), ("priv", 6))))
if mibBuilder.loadTexts: ipAllowSrcPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcPortMode.setDescription('This object specifies the range of source port numbers of IP datagrams belonging to the subset. ignore(1) = All ports: 0 ..65535; specific(2) = a specific port number i.e. ipAllowScrPort; clients(3) = clientports: 1024 .. 4999, 32768..65535; server(4) = server ports: 0..1023 5000..32767; unpriv(5) = unprivileged ports: 1024..65535; priv(6) = privileged ports: 0..1023')
ipAllowSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipAllowSrcPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcPort.setDescription("If ipAllowSrcPortMode is set to 'specific', then this object contains a specific port number. Otherwise this object is not used.")
ipAllowDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 9), IpAddress())
if mibBuilder.loadTexts: ipAllowDstAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowDstAddr.setDescription('This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipAllowDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 10), IpAddress())
if mibBuilder.loadTexts: ipAllowDstMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowDstMask.setDescription(' This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipAllowDstPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ignore", 1), ("specific", 2), ("clients", 3), ("server", 4), ("unpriv", 5), ("priv", 6))))
if mibBuilder.loadTexts: ipAllowDstPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowDstPortMode.setDescription('This object specifies the range of destination port numbers of IP datagrams belonging to the subset. ignore(1) = All ports: 0..65535; specific(2) = a specific port number i.e. ipAllowDstPort; clients(3) = client ports: 1024..4999, 32768..65535; server(4) = server ports. 0..1023, 5000..32767; unpriv(5) = unprivileged ports: 1024..65535; priv(6) = privileged ports: 0..1023')
ipAllowDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipAllowDstPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowDstPort.setDescription("If ipAllowDstPortMode is set to 'specific', then this object contains a specific port number. Otherwise this object is not used.")
ipAllowSrcPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535)))
if mibBuilder.loadTexts: ipAllowSrcPortRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowSrcPortRange.setDescription('This object can be used together with ipAllowSrcPort to apply the rule to a port range, instead of a single port. When ipAllowSrcPortMode is set to specific and this object is not set to -1, than the rule applies to the Range of ports from ipAllowSrcPort to ipAllowSrcPortRange. When this object is set to -1, the rule applies only to port ipAllowSrcPort.')
ipAllowDstPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535)))
if mibBuilder.loadTexts: ipAllowDstPortRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipAllowDstPortRange.setDescription('This object can be used together with ipAllowDstPort to apply the rule to a port range, instead of a single port. When ipAllowDstPortMode is set to specific and this object is not set to -1, than the rule applies to the Range of ports from ipAllowDstPort to ipAllowDstPortRange. When this object is set to -1, the rule applies only to port ipAllowDstPort.')
ipDenyTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 2), )
if mibBuilder.loadTexts: ipDenyTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyTable.setDescription("The ipDenyTable defines all IP packets to be denied. Each entry describes a subset of IP Packets, which are denied processing. The overall set of denied IP packets is the union of all subsets that are described in this table. The ipDenyTable overwrites the ipAllowTable. IP datagrams specified in the ipDenyTable are always refused, even if they are allowed by the ipAllowTable. Creating entries: Entries are created by setting the ipDenyProtocolMode and ipDenySrcIfIndexMode objects in one operation (i.e. on one command line). Deleting entries: Entries are deleted by setting the ipDenyProtocolMode object to 'delete'.")
ipDenyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1), ).setIndexNames((0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipDenyProtocolMode"), (0, "BIANCA-BRICK-IP-OLDACCESS-MIB", "ipDenySrcIfIndexMode"))
if mibBuilder.loadTexts: ipDenyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyEntry.setDescription('')
ipDenyProtocolMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3))))
if mibBuilder.loadTexts: ipDenyProtocolMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyProtocolMode.setDescription("Specifies whether or not the protocol field of the IP datagram header should be used to determine if the datagram belongs to the subset of this entry. dont-verify(1) = don't check the protocol field; verify(2) = check the protocol field; delete(3) = delete the entry from the table")
ipDenyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 8, 12, 17, 20, 22, 27, 89))).clone(namedValues=NamedValues(("icmp", 1), ("ggp", 3), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("hmp", 20), ("xns-idp", 22), ("rdp", 27), ("ospf", 89))))
if mibBuilder.loadTexts: ipDenyProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyProtocol.setDescription("If the ipDenyProtocolMode is set to 'verify', this object specifies the protocol of IP datagrams belonging to the subset described by this entry. Otherwise, this field has no meaning.")
ipDenySrcIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2))))
if mibBuilder.loadTexts: ipDenySrcIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcIfIndexMode.setDescription('This object specifies whether or not the originating interface of the IP datagram should be checked to determine whether a datagram belongs to this subset.')
ipDenySrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 4), Integer32())
if mibBuilder.loadTexts: ipDenySrcIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcIfIndex.setDescription("If ipDenySrcIfIndexMode is set to 'verify', then this object specifies the ifIndex of the datagrams belonging to the subset defined by this entry.")
ipDenySrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 5), IpAddress())
if mibBuilder.loadTexts: ipDenySrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcAddr.setDescription("If ipDenySrcIfIndexMode is set to 'verify', then this object specifies the ifIndex of the datagrams belonging to the subset defined by this entry.")
ipDenySrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 6), IpAddress())
if mibBuilder.loadTexts: ipDenySrcMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcMask.setDescription('This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipDenySrcPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ignore", 1), ("specific", 2), ("clients", 3), ("server", 4), ("unpriv", 5), ("priv", 6))))
if mibBuilder.loadTexts: ipDenySrcPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcPortMode.setDescription('This object specifies the range of source port numbers of IP datagrams belonging to this subset. ignore(1) = All ports: 0..65535; specific(2) = a specific port number i.e. ipAllowDstPort; clients(3) = client ports: 1024..4999, 32768..65535; server(4) = server ports. 0..1023, 5000..32767; unpriv(5) = unprivileged ports: 1024..65535; priv(6) = privileged ports: 0..1023')
ipDenySrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipDenySrcPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcPort.setDescription("If ipDenySrcPortMode is set to 'specific', then this object contains a specific port number. Otherwise this object is not used.")
ipDenyDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 9), IpAddress())
if mibBuilder.loadTexts: ipDenyDstAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyDstAddr.setDescription('This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipDenyDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 10), IpAddress())
if mibBuilder.loadTexts: ipDenyDstMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyDstMask.setDescription('This object specifies the set of IP addresses of datagrams that belong to the subset defined by this entry.')
ipDenyDstPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ignore", 1), ("specific", 2), ("clients", 3), ("server", 4), ("unpriv", 5), ("priv", 6))))
if mibBuilder.loadTexts: ipDenyDstPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyDstPortMode.setDescription('This object specifies the range of destination port numbers of IP datagrams belonging to the subset. ignore(1) = All ports: 0..65535; specific(2) = a specific port number i.e. ipAllowDstPort; clients(3) = client ports: 1024..4999, 32768..65535; server(4) = server ports. 0..1023, 5000..32767; unpriv(5) = unprivileged ports: 1024..65535; priv(6) = privileged ports: 0..1023')
ipDenyDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipDenyDstPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyDstPort.setDescription("If ipDenyDstPortMode is set to 'specific', then this object contains a specific port number. Otherwise this object is not used.")
ipDenySrcPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535)))
if mibBuilder.loadTexts: ipDenySrcPortRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenySrcPortRange.setDescription('This object can be used together with ipDenySrcPort to apply the rule to a port range, instead of a single port. When ipDenySrcPortMode is set to specific and this object is not set to -1, than the rule applies to the Range of ports from ipDenySrcPort to ipDenySrcPortRange. When this object is set to -1, the rule applies only to port ipDenySrcPort.')
ipDenyDstPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535)))
if mibBuilder.loadTexts: ipDenyDstPortRange.setStatus('mandatory')
if mibBuilder.loadTexts: ipDenyDstPortRange.setDescription('This object can be used together with ipDenyDstPort to apply the rule to a port range, instead of a single port. When ipDenyDstPortMode is set to specific and this object is not set to -1, than the rule applies to the Range of ports from ipDenyDstPort to ipDenyDstPortRange. When this object is set to -1, the rule applies only to port ipDenyDstPort.')
mibBuilder.exportSymbols("BIANCA-BRICK-IP-OLDACCESS-MIB", biboipold=biboipold, ipAllowDstPortMode=ipAllowDstPortMode, ipAllowEntry=ipAllowEntry, ipAllowProtocol=ipAllowProtocol, org=org, ipDenyProtocol=ipDenyProtocol, ipAllowSrcPortMode=ipAllowSrcPortMode, ipAllowProtocolMode=ipAllowProtocolMode, ipDenySrcIfIndexMode=ipDenySrcIfIndexMode, dod=dod, ipDenyDstPort=ipDenyDstPort, ipAllowSrcIfIndexMode=ipAllowSrcIfIndexMode, ipDenyEntry=ipDenyEntry, ipAllowSrcPort=ipAllowSrcPort, ipAllowDstPort=ipAllowDstPort, ipDenyProtocolMode=ipDenyProtocolMode, ipDenyDstPortRange=ipDenyDstPortRange, ipAllowTable=ipAllowTable, ipDenySrcPort=ipDenySrcPort, ipAllowSrcMask=ipAllowSrcMask, ipDenySrcIfIndex=ipDenySrcIfIndex, ipDenySrcMask=ipDenySrcMask, ipDenyDstMask=ipDenyDstMask, internet=internet, ipDenyTable=ipDenyTable, ipAllowDstMask=ipAllowDstMask, ipDenySrcAddr=ipDenySrcAddr, bintec=bintec, bibo=bibo, ipDenySrcPortMode=ipDenySrcPortMode, ipAllowSrcAddr=ipAllowSrcAddr, ipAllowDstPortRange=ipAllowDstPortRange, ipDenyDstPortMode=ipDenyDstPortMode, ipDenyDstAddr=ipDenyDstAddr, ipDenySrcPortRange=ipDenySrcPortRange, private=private, ipAllowSrcPortRange=ipAllowSrcPortRange, ipAllowDstAddr=ipAllowDstAddr, ipAllowSrcIfIndex=ipAllowSrcIfIndex, enterprises=enterprises)
