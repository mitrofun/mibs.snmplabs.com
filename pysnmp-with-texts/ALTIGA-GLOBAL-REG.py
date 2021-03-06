#
# PySNMP MIB module ALTIGA-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-GLOBAL-REG
# Produced by pysmi-0.3.4 at Wed May  1 11:21:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Bits, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, iso, Integer32, Counter32, Counter64, Unsigned32, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "iso", "Integer32", "Counter32", "Counter64", "Unsigned32", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 1, 1))
altigaGlobalRegModule.setRevisions(('2005-01-05 00:00', '2003-10-20 00:00', '2003-04-25 00:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaGlobalRegModule.setRevisionsDescriptions(('Added the new MIB Modules(65 to 67)', 'Added the new MIB Modules(58 to 64)', 'Added the new MIB Modules(54 to 57)', 'Updated with new header',))
if mibBuilder.loadTexts: altigaGlobalRegModule.setLastUpdated('200501050000Z')
if mibBuilder.loadTexts: altigaGlobalRegModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaGlobalRegModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaGlobalRegModule.setDescription('The Altiga Networks central registration module. Acronyms The following acronyms are used in this document: ACE: Access Control Encryption BwMgmt: Bandwidth Management CTCP: Cisco Transmission Control Protocol DHCP: Dynamic Host Configuration Protocol DNS: Domain Name Service FTP: File Transfer Protocol FW: Firewall HTTP: HyperText Transfer Protocol ICMP: Internet Control Message Protocol IKE: Internet Key Exchange IP: Internet Protocol LBSSF: Load Balance Secure Session Failover L2TP: Layer-2 Tunneling Protocol MIB: Management Information Base NAT: Network Address Translation NTP: Network Time Protocol PPP: Point-to-Point Protocol PPTP: Point-to-Point Tunneling Protocol SEP: Scalable Encryption Processor SNMP: Simple Network Management Protocol SSH: Secure Shell Protocol SSL: Secure Sockets Layer UDP: User Datagram Protocol VPN: Virtual Private Network NAC: Network Admission Control ')
altigaRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 3076))
altigaReg = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1))
altigaModules = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1))
alGlobalRegModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 1))
alCapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2))
alMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 3))
alComplModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 4))
alVersionMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 6))
alAccessMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 7))
alEventMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8))
alAuthMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 9))
alPptpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 10))
alPppMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 11))
alHttpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 12))
alIpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13))
alFilterMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 14))
alUserMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 15))
alTelnetMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 16))
alFtpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 17))
alTftpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 18))
alSnmpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 19))
alIpSecMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 20))
alL2tpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 21))
alSessionMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 22))
alDnsMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23))
alAddressMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 24))
alDhcpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 25))
alWatchdogMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 26))
alHardwareMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 27))
alNatMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 28))
alLan2LanMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 29))
alGeneralMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30))
alSslMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 31))
alCertMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 32))
alNtpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 33))
alNetworkListMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 34))
alSepMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 35))
alIkeMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 36))
alSyncMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 37))
alT1E1MibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 38))
alMultiLinkMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 39))
alSshMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 40))
alLBSSFMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 41))
alDhcpServerMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 42))
alAutoUpdateMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 43))
alAdminAuthMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 44))
alPPPoEMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 45))
alXmlMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 46))
alCtcpMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 47))
alFwMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 48))
alGroupMatchMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 49))
alACEServerMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 50))
alNatTMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 51))
alBwMgmtMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 52))
alIpSecPreFragMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 53))
alFipsMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 54))
alBackupL2LMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 55))
alNotifyMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 56))
alRebootStatusMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 57))
alAuthorizationModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 58))
alWebPortalMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 59))
alWebEmailMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 60))
alPortForwardMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 61))
alRemoteServerMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 62))
alWebvpnAclMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 63))
alNbnsMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 64))
alSecureDesktopMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 65))
alSslTunnelClientMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 66))
alNacMibModule = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 67))
altigaGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2))
altigaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 3))
altigaCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 4))
altigaReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 5))
altigaExpr = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 6))
altigaHw = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2))
altigaVpnHw = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1))
altigaVpnChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1))
altigaVpnIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 2))
altigaVpnEncrypt = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 3))
vpnConcentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1))
vpnRemote = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 2))
vpnClient = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 3))
vpnConcentratorRev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: vpnConcentratorRev1.setStatus('current')
if mibBuilder.loadTexts: vpnConcentratorRev1.setDescription("The first revision of Altiga's VPN Concentrator hardware. 603e PPC processor. C10/15/20/30/50/60.")
vpnConcentratorRev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: vpnConcentratorRev2.setStatus('current')
if mibBuilder.loadTexts: vpnConcentratorRev2.setDescription("The second revision of Altiga's VPN Concentrator hardware. 740 PPC processor. C10/15/20/30/50/60.")
vpnRemoteRev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 2, 1))
if mibBuilder.loadTexts: vpnRemoteRev1.setStatus('current')
if mibBuilder.loadTexts: vpnRemoteRev1.setDescription("The first revision of Altiga's VPN Concentrator (Remote) hardware. 8240 PPC processor.")
vpnClientRev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 2, 1, 1, 3, 1))
if mibBuilder.loadTexts: vpnClientRev1.setStatus('current')
if mibBuilder.loadTexts: vpnClientRev1.setDescription("The first revision of Altiga's VPN Hardware Client hardware. 8260 PPC processor.")
mibBuilder.exportSymbols("ALTIGA-GLOBAL-REG", PYSNMP_MODULE_ID=altigaGlobalRegModule, alNatTMibModule=alNatTMibModule, alWebEmailMibModule=alWebEmailMibModule, alEventMibModule=alEventMibModule, alPptpMibModule=alPptpMibModule, alAccessMibModule=alAccessMibModule, alDhcpMibModule=alDhcpMibModule, alIkeMibModule=alIkeMibModule, alHttpMibModule=alHttpMibModule, alSepMibModule=alSepMibModule, alMibModule=alMibModule, altigaVpnHw=altigaVpnHw, altigaExpr=altigaExpr, alHardwareMibModule=alHardwareMibModule, altigaGeneric=altigaGeneric, alRebootStatusMibModule=alRebootStatusMibModule, alSslMibModule=alSslMibModule, alVersionMibModule=alVersionMibModule, altigaVpnChassis=altigaVpnChassis, alSyncMibModule=alSyncMibModule, altigaHw=altigaHw, alPppMibModule=alPppMibModule, vpnRemote=vpnRemote, alGroupMatchMibModule=alGroupMatchMibModule, alNotifyMibModule=alNotifyMibModule, alCapModule=alCapModule, altigaReg=altigaReg, altigaRoot=altigaRoot, altigaReqs=altigaReqs, vpnClient=vpnClient, alIpSecPreFragMibModule=alIpSecPreFragMibModule, alL2tpMibModule=alL2tpMibModule, alAutoUpdateMibModule=alAutoUpdateMibModule, alSshMibModule=alSshMibModule, alSslTunnelClientMibModule=alSslTunnelClientMibModule, alAddressMibModule=alAddressMibModule, alLan2LanMibModule=alLan2LanMibModule, alSecureDesktopMibModule=alSecureDesktopMibModule, alDhcpServerMibModule=alDhcpServerMibModule, altigaVpnEncrypt=altigaVpnEncrypt, alPortForwardMibModule=alPortForwardMibModule, alT1E1MibModule=alT1E1MibModule, alAuthorizationModule=alAuthorizationModule, vpnRemoteRev1=vpnRemoteRev1, vpnConcentratorRev1=vpnConcentratorRev1, alFwMibModule=alFwMibModule, altigaProducts=altigaProducts, alPPPoEMibModule=alPPPoEMibModule, alFilterMibModule=alFilterMibModule, alCertMibModule=alCertMibModule, alTelnetMibModule=alTelnetMibModule, alGlobalRegModule=alGlobalRegModule, alWebPortalMibModule=alWebPortalMibModule, alNacMibModule=alNacMibModule, alCtcpMibModule=alCtcpMibModule, vpnClientRev1=vpnClientRev1, vpnConcentrator=vpnConcentrator, alGeneralMibModule=alGeneralMibModule, alAuthMibModule=alAuthMibModule, alACEServerMibModule=alACEServerMibModule, alNetworkListMibModule=alNetworkListMibModule, altigaCaps=altigaCaps, alWebvpnAclMibModule=alWebvpnAclMibModule, altigaVpnIntf=altigaVpnIntf, alSessionMibModule=alSessionMibModule, alIpSecMibModule=alIpSecMibModule, alFipsMibModule=alFipsMibModule, alTftpMibModule=alTftpMibModule, vpnConcentratorRev2=vpnConcentratorRev2, alSnmpMibModule=alSnmpMibModule, alFtpMibModule=alFtpMibModule, alBackupL2LMibModule=alBackupL2LMibModule, alAdminAuthMibModule=alAdminAuthMibModule, alXmlMibModule=alXmlMibModule, alLBSSFMibModule=alLBSSFMibModule, alWatchdogMibModule=alWatchdogMibModule, alDnsMibModule=alDnsMibModule, alBwMgmtMibModule=alBwMgmtMibModule, altigaModules=altigaModules, alMultiLinkMibModule=alMultiLinkMibModule, alNtpMibModule=alNtpMibModule, alNbnsMibModule=alNbnsMibModule, alRemoteServerMibModule=alRemoteServerMibModule, alNatMibModule=alNatMibModule, altigaGlobalRegModule=altigaGlobalRegModule, alComplModule=alComplModule, alIpMibModule=alIpMibModule, alUserMibModule=alUserMibModule)
