#
# PySNMP MIB module NETSCREEN-VPN-MON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-VPN-MON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
netscreenVpnMibModule, netscreenVpn = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpnMibModule", "netscreenVpn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Unsigned32, TimeTicks, Bits, NotificationType, Gauge32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenVpnMonMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 1))
netscreenVpnMonMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenVpnMonMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct spelling mistake', 'no comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenVpnMonMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVpnMonMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenVpnMonMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenVpnMonMibModule.setDescription('This module defines the object that are used to monitor VPN tunnels')
netscreenVpnMon = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 1))
nsVpnMonTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1), )
if mibBuilder.loadTexts: nsVpnMonTable.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonTable.setDescription('A list of active VPN tunnel entries.')
nsVpnMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1), ).setIndexNames((0, "NETSCREEN-VPN-MON-MIB", "nsVpnMonIndex"))
if mibBuilder.loadTexts: nsVpnMonEntry.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonEntry.setDescription('A VPN tunnel entry containing attributes for both IKE Phase 1 and Phase 2 as well as associated policy')
nsVpnMonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonIndex.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonIndex.setDescription('A unique value for each active VPN tunnel. Its value ranges between 1 and 65535 and may not be contiguous. Due to the dynamic nature of active VPN tunnels, the index has no other meaning but a pure index')
nsVpnMonInPlyId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonInPlyId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonInPlyId.setDescription('The incoming policy ID for which this tunnel is created for. -1 means no policy associates with this SA.')
nsVpnMonOutPlyId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonOutPlyId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonOutPlyId.setDescription('The outgoing policy ID for which this tunnel is created for. -1 means no policy associates with this SA.')
nsVpnMonVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonVpnName.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonVpnName.setDescription('A textual string contains information about the VPN entity from which this tunnel was derived.')
nsVpnMonVsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonVsysName.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonVsysName.setDescription('A textual string contains the Virtual system to which this tunnel belongs.')
nsVpnMonTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("reserved", 0), ("proto-isakmp", 1), ("proto-ipsec-ah", 2), ("proto-ipsec-esp", 3), ("proto-ipcomp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonTunnelType.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonTunnelType.setDescription('Protocol type used for the tunnel')
nsVpnMonEspEncAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21))).clone(namedValues=NamedValues(("reserved", 0), ("esp-des-iv64", 1), ("esp-des", 2), ("esp-3des", 3), ("esp-rc5", 4), ("esp-idea", 5), ("esp-cast", 6), ("esp-blowfish", 7), ("esp-3idea", 8), ("esp-des-iv32", 9), ("esp-rc4", 10), ("esp-null", 11), ("esp-aes", 12), ("esp-aes192", 20), ("esp-aes256", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonEspEncAlg.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonEspEncAlg.setDescription('a value which identifies a particular algorithm to be used to provide secrecy protection for ESP.')
nsVpnMonEspAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("reserved", 0), ("hmac-md5", 1), ("hmac-sha", 2), ("des-mac", 3), ("ipdk", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonEspAuthAlg.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonEspAuthAlg.setDescription('The ESP Authentication Algorithm used in the IPsec.')
nsVpnMonAhAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4))).clone(namedValues=NamedValues(("reserved", 0), ("ah-md5", 2), ("ah-sha", 3), ("ah-des", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonAhAlg.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonAhAlg.setDescription('a value which identifies a particular algorithm to be used to provide integrity protection for AH.')
nsVpnMonKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("manual", 0), ("auto-ike", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonKeyType.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonKeyType.setDescription('a value which identifies a key exchange protocol to be used for the negotiation')
nsVpnMonP1Auth = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unused", 0), ("preshared-key", 1), ("dss-Signature", 2), ("rsa-Signature", 3), ("rsa-Encryption1", 4), ("rsa-Encryption2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP1Auth.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP1Auth.setDescription('a value which identifies Phase 1 authentication method')
nsVpnMonVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("reserved", 0), ("dialup", 1), ("site-to-site", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonVpnType.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonVpnType.setDescription('The type of this VPN tunnel, either a dialup or site-to-site')
nsVpnMonRmtGwIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonRmtGwIp.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonRmtGwIp.setDescription("The peer Gateway's IP address")
nsVpnMonRmtGwId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonRmtGwId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonRmtGwId.setDescription("The peer Gateway's ID")
nsVpnMonMyGwIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonMyGwIp.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonMyGwIp.setDescription("The local Gateway's IP address")
nsVpnMonMyGwId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonMyGwId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonMyGwId.setDescription("The local Gateway's ID")
nsVpnMonOutSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonOutSpi.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonOutSpi.setDescription('The SPI for outgoing packets')
nsVpnMonInSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonInSpi.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonInSpi.setDescription('The SPI for incoming packets')
nsVpnMonMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonMonState.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonMonState.setDescription('The monitoring status, if it is on, an icmp ping will be sent over the tunnel periodically to test the connectivity and latency')
nsVpnMonTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonTunnelState.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonTunnelState.setDescription('The current tunnel status determined by the icmp ping if The monitoring status is on.')
nsVpnMonP1State = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP1State.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP1State.setDescription("The IKE's Phase 1 status")
nsVpnMonP1LifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP1LifeTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP1LifeTime.setDescription("an active Phase 1 sa's time left before re-key. -1 means unlimited lifetime.")
nsVpnMonP2State = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP2State.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP2State.setDescription("The IKE's Phase 2 status")
nsVpnMonP2LifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP2LifeTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP2LifeTime.setDescription("an active Phase 2 sa's time left before re-key. -1 means unlimited life time.")
nsVpnMonP2LifeBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonP2LifeBytes.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonP2LifeBytes.setDescription("an active Phase 2 sa's bytes left before re-key. -1 means unlimited life bytes.")
nsVpnMonDelayAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonDelayAvg.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonDelayAvg.setDescription('a kind of rolling average of latency, in milliseconds. -1 has no meaning here, which means nsVpnMonDelayAvg has not been calculated yet.')
nsVpnMonDelayLast = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonDelayLast.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonDelayLast.setDescription('latency in last sample, in milliseconds. -1 means either vpn tunnel is inactive or vpn tunnel monitor is not turned on.')
nsVpnMonAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonAvail.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonAvail.setDescription('percentage over 30 samples')
nsVpnMonSaId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSaId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonSaId.setDescription('SA identifier, also used as table index')
nsVpnMonGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonGroupId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonGroupId.setDescription('Group Identifier')
nsVpnMonUsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonUsrId.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonUsrId.setDescription('User Identifier')
nsVpnMonStartSessRequestTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 32), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonStartSessRequestTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonStartSessRequestTime.setDescription('Start Session request timestamp')
nsVpnMonStartSessEstTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 33), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonStartSessEstTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonStartSessEstTime.setDescription('Start Session establish timestamp')
nsVpnMonEndSessTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 34), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonEndSessTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonEndSessTime.setDescription('End Session timestamp [when session terminates]')
nsVpnMonBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonBytesIn.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonBytesIn.setDescription('Incoming bytes through this sa.')
nsVpnMonBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonBytesOut.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonBytesOut.setDescription('Outgoing bytes through this sa.')
nsVpnMonPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonPacketsIn.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonPacketsIn.setDescription('Incoming packets through this sa.')
nsVpnMonPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonPacketsOut.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonPacketsOut.setDescription('Outgoing packets through this sa.')
nsVpnMonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonIfIndex.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonIfIndex.setDescription('interface index.')
nsVpnMonUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 40), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonUpdateTime.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonUpdateTime.setDescription('Timestamp [Whenever any member of the row gets updated, the timestamp is updated]')
nsVpnMonDN = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 41), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonDN.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonDN.setDescription('DN name')
nsVpnMonIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 42), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonIfInfo.setStatus('current')
if mibBuilder.loadTexts: nsVpnMonIfInfo.setDescription('Internal id assigned to this interface. Stays persistent across resets.')
mibBuilder.exportSymbols("NETSCREEN-VPN-MON-MIB", nsVpnMonBytesOut=nsVpnMonBytesOut, netscreenVpnMonMibModule=netscreenVpnMonMibModule, nsVpnMonSaId=nsVpnMonSaId, nsVpnMonPacketsOut=nsVpnMonPacketsOut, nsVpnMonIndex=nsVpnMonIndex, nsVpnMonMyGwIp=nsVpnMonMyGwIp, nsVpnMonStartSessRequestTime=nsVpnMonStartSessRequestTime, nsVpnMonVpnName=nsVpnMonVpnName, nsVpnMonP2LifeBytes=nsVpnMonP2LifeBytes, nsVpnMonPacketsIn=nsVpnMonPacketsIn, nsVpnMonIfInfo=nsVpnMonIfInfo, nsVpnMonDN=nsVpnMonDN, nsVpnMonRmtGwId=nsVpnMonRmtGwId, nsVpnMonEspEncAlg=nsVpnMonEspEncAlg, nsVpnMonOutPlyId=nsVpnMonOutPlyId, nsVpnMonEndSessTime=nsVpnMonEndSessTime, netscreenVpnMon=netscreenVpnMon, nsVpnMonMonState=nsVpnMonMonState, nsVpnMonRmtGwIp=nsVpnMonRmtGwIp, nsVpnMonVsysName=nsVpnMonVsysName, nsVpnMonStartSessEstTime=nsVpnMonStartSessEstTime, nsVpnMonTunnelState=nsVpnMonTunnelState, nsVpnMonP2LifeTime=nsVpnMonP2LifeTime, nsVpnMonMyGwId=nsVpnMonMyGwId, nsVpnMonVpnType=nsVpnMonVpnType, nsVpnMonInPlyId=nsVpnMonInPlyId, PYSNMP_MODULE_ID=netscreenVpnMonMibModule, nsVpnMonKeyType=nsVpnMonKeyType, nsVpnMonInSpi=nsVpnMonInSpi, nsVpnMonIfIndex=nsVpnMonIfIndex, nsVpnMonDelayLast=nsVpnMonDelayLast, nsVpnMonTunnelType=nsVpnMonTunnelType, nsVpnMonDelayAvg=nsVpnMonDelayAvg, nsVpnMonUpdateTime=nsVpnMonUpdateTime, nsVpnMonEspAuthAlg=nsVpnMonEspAuthAlg, nsVpnMonUsrId=nsVpnMonUsrId, nsVpnMonAhAlg=nsVpnMonAhAlg, nsVpnMonOutSpi=nsVpnMonOutSpi, nsVpnMonTable=nsVpnMonTable, nsVpnMonEntry=nsVpnMonEntry, nsVpnMonP2State=nsVpnMonP2State, nsVpnMonBytesIn=nsVpnMonBytesIn, nsVpnMonGroupId=nsVpnMonGroupId, nsVpnMonP1Auth=nsVpnMonP1Auth, nsVpnMonAvail=nsVpnMonAvail, nsVpnMonP1State=nsVpnMonP1State, nsVpnMonP1LifeTime=nsVpnMonP1LifeTime)
