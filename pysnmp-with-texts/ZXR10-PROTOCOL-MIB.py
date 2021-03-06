#
# PySNMP MIB module ZXR10-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, TimeTicks, iso, Counter64, MibIdentifier, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ModuleIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "iso", "Counter64", "MibIdentifier", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10protocol = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101))
zxr10ip = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1))
zxr10tcp = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2))
class DisplayString(OctetString):
    pass

zxr10ipvrfaddrTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1), )
if mibBuilder.loadTexts: zxr10ipvrfaddrTable.setStatus('current')
if mibBuilder.loadTexts: zxr10ipvrfaddrTable.setDescription('The description of zxr10 vrf address table. It is a list of vrf address entries.')
zxr10ipvrfaddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1), ).setIndexNames((0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfVpnName"), (0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfAddr"))
if mibBuilder.loadTexts: zxr10ipvrfaddrEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10ipvrfaddrEntry.setDescription('A vrf address entry containing objects that vrf interface address infomation,such as: vrf ifindex, vrf address, mask.')
zxr10ipVrfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfVpnName.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfVpnName.setDescription('The IP address of this vrf interface.')
zxr10ipVrfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfAddr.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfAddr.setDescription('The IP address of this vrf interface.')
zxr10ipVrfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfNetMask.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfNetMask.setDescription('The subnet mask associated with the IP address of this vrf interface. The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0.')
zxr10ipVrfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfIfIndex.setDescription('The index value which uniquely identifies the vrf interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
zxr10ipVrfBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfBcastAddr.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfBcastAddr.setDescription('The value of the least-significant bit in the IP broadcast address used for sending datagrams on the vrf interface associated with the IP address. For example, when the Internet standard all-ones broadcast address is used, the value will be 1. This value applies to both the subnet and network broadcasts addresses used by the vrf interface.')
zxr10ipVrfReasmMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfReasmMaxSize.setStatus('current')
if mibBuilder.loadTexts: zxr10ipVrfReasmMaxSize.setDescription('The size of the largest IP datagram which this vrf interface can re-assemble from incoming IP fragmented datagrams received on this interface.')
zxr10tcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1), )
if mibBuilder.loadTexts: zxr10tcpConnTable.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnTable.setDescription('A table containing TCP connection-specific information.')
zxr10tcpconnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1), ).setIndexNames((0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnVrfVpnName"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalAddress"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalPort"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemAddress"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemPort"))
if mibBuilder.loadTexts: zxr10tcpconnEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpconnEntry.setDescription('Information about a particular current TCP connection. An object of this type is transient, in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state.')
zxr10tcpConnVrfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnVrfVpnName.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnVrfVpnName.setDescription('The IP address of this vrf interface.')
zxr10tcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10tcpConnState.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnState.setDescription("The state of this TCP connection. The only value which may be set by a management station is deleteTCB(12). Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value. If a management station sets this object to the value deleteTCB(12), then this has the effect of deleting the TCB (as defined in RFC 793) of the corresponding connection on the managed node, resulting in immediate termination of the connection. As an implementation-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note however that RST segments are not sent reliably).")
zxr10tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnLocalAddress.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnLocalAddress.setDescription('The local IP address for this TCP connection. In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used.')
zxr10tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnLocalPort.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnLocalPort.setDescription('The local port number for this TCP connection.')
zxr10tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnRemAddress.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnRemAddress.setDescription('The remote IP address for this TCP connection.')
zxr10tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnRemPort.setStatus('current')
if mibBuilder.loadTexts: zxr10tcpConnRemPort.setDescription('The remote port number for this TCP connection.')
mibBuilder.exportSymbols("ZXR10-PROTOCOL-MIB", zxr10ipvrfaddrEntry=zxr10ipvrfaddrEntry, zxr10tcpConnTable=zxr10tcpConnTable, zxr10ipVrfVpnName=zxr10ipVrfVpnName, zxr10ipVrfBcastAddr=zxr10ipVrfBcastAddr, zxr10tcpConnLocalAddress=zxr10tcpConnLocalAddress, zxr10ipvrfaddrTable=zxr10ipvrfaddrTable, zxr10ipVrfIfIndex=zxr10ipVrfIfIndex, zxr10tcpConnVrfVpnName=zxr10tcpConnVrfVpnName, zxr10tcpConnRemPort=zxr10tcpConnRemPort, zxr10tcp=zxr10tcp, zxr10protocol=zxr10protocol, DisplayString=DisplayString, zxr10tcpconnEntry=zxr10tcpconnEntry, zte=zte, zxr10tcpConnState=zxr10tcpConnState, zxr10ipVrfNetMask=zxr10ipVrfNetMask, zxr10=zxr10, zxr10ipVrfAddr=zxr10ipVrfAddr, zxr10tcpConnRemAddress=zxr10tcpConnRemAddress, zxr10ip=zxr10ip, zxr10tcpConnLocalPort=zxr10tcpConnLocalPort, zxr10ipVrfReasmMaxSize=zxr10ipVrfReasmMaxSize)
