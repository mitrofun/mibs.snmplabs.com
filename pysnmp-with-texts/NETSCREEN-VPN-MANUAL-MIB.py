#
# PySNMP MIB module NETSCREEN-VPN-MANUAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-VPN-MANUAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
netscreenVpn, netscreenVpnMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn", "netscreenVpnMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, Counter64, MibIdentifier, Gauge32, Bits, ObjectIdentity, IpAddress, iso, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "iso", "Counter32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenVpnManualMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 2))
netscreenVpnManualMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2002-05-21 00:00', '2001-09-28 00:00', '2001-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenVpnManualMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct spelling mistake', 'Zwang add sha-256 in nsVpnManualKeyEspAuthAlg', 'no comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenVpnManualMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVpnManualMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenVpnManualMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenVpnManualMibModule.setDescription('This module defines NetScreen private MIBs for VPN Manual Key')
nsVpnManualKey = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 2))
nsVpnManualKeyTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1), )
if mibBuilder.loadTexts: nsVpnManualKeyTable.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyTable.setDescription("This table specifies the configuration attributes for NetScreen device's manual key setting.")
nsVpnManualKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1), ).setIndexNames((0, "NETSCREEN-VPN-MANUAL-MIB", "nsVpnManualKeyIndex"))
if mibBuilder.loadTexts: nsVpnManualKeyEntry.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyEntry.setDescription('Each entry in the nsVpnManualKeyTable holds a set of configuration parameters associated with an instance of manual key.')
nsVpnManualKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyIndex.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyIndex.setDescription('A unique value for manual key table. Its value ranges between 0 and 65535 and may not be contiguous.')
nsVpnManualKeyTunName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyTunName.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyTunName.setDescription('VPN tunnel name that uses this manual key configuration.')
nsVpnManualKeyGW = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyGW.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyGW.setDescription('VPN tunnel peer gateway IP address.')
nsVpnManualKeySILocal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeySILocal.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeySILocal.setDescription('Local Security Index.')
nsVpnManualKeySIRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeySIRemote.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeySIRemote.setDescription('Remote Security Index.')
nsVpnManualKeyTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("esp", 0), ("ah", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyTunnelType.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyTunnelType.setDescription('VPN tunnel type.')
nsVpnManualKeyEspEncAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("null", 0), ("des-cbc", 1), ("tripple-des-cbc", 2), ("aes-cbc", 3), ("aes-192", 4), ("aes-256", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyEspEncAlg.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyEspEncAlg.setDescription('ESP Encryption Algorithm when manual key vpn tunnel type is ESP.')
nsVpnManualKeyEspAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2), ("sha256", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyEspAuthAlg.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyEspAuthAlg.setDescription('ESP Authentication Algorithm when manual key vpn tunnel type is ESP.')
nsVpnManualKeyAhHash = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyAhHash.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyAhHash.setDescription('AH Hash Algorithm when manual key vpn tunnel type is AH.')
nsVpnManualKeyMonitorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyMonitorEnable.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyMonitorEnable.setDescription("Enable monitor vpn tunnel's link status.")
nsVpnManualKeyTunToTrust = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyTunToTrust.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyTunToTrust.setDescription('Tunnel to Trusted Interface')
nsVpnManualKeyVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyVsys.setStatus('current')
if mibBuilder.loadTexts: nsVpnManualKeyVsys.setDescription('vsys this vpn manual key setting belongs to.')
mibBuilder.exportSymbols("NETSCREEN-VPN-MANUAL-MIB", nsVpnManualKeyTunName=nsVpnManualKeyTunName, nsVpnManualKeyEntry=nsVpnManualKeyEntry, nsVpnManualKeyMonitorEnable=nsVpnManualKeyMonitorEnable, nsVpnManualKeyVsys=nsVpnManualKeyVsys, nsVpnManualKeyEspAuthAlg=nsVpnManualKeyEspAuthAlg, nsVpnManualKeyAhHash=nsVpnManualKeyAhHash, nsVpnManualKeyEspEncAlg=nsVpnManualKeyEspEncAlg, nsVpnManualKey=nsVpnManualKey, netscreenVpnManualMibModule=netscreenVpnManualMibModule, nsVpnManualKeySILocal=nsVpnManualKeySILocal, nsVpnManualKeyTunnelType=nsVpnManualKeyTunnelType, nsVpnManualKeyTunToTrust=nsVpnManualKeyTunToTrust, nsVpnManualKeySIRemote=nsVpnManualKeySIRemote, nsVpnManualKeyIndex=nsVpnManualKeyIndex, nsVpnManualKeyGW=nsVpnManualKeyGW, PYSNMP_MODULE_ID=netscreenVpnManualMibModule, nsVpnManualKeyTable=nsVpnManualKeyTable)
