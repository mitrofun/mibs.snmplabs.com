#
# PySNMP MIB module NETSCREEN-SET-GLB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-GLB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
netscreenSettingMibModule, netscreenSetting = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSettingMibModule", "netscreenSetting")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Counter64, Bits, ModuleIdentity, Gauge32, Integer32, iso, TimeTicks, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Counter64", "Bits", "ModuleIdentity", "Gauge32", "Integer32", "iso", "TimeTicks", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetGlbMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 10))
netscreenSetGlbMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenSetGlbMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'No Comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenSetGlbMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetGlbMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenSetGlbMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenSetGlbMibModule.setDescription('This module defines the object that are used to monitor Global, Global-Pro and NSM setting')
nsSetGlbMng = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 10))
nsSetGlbMngVPNEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngVPNEnable.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngVPNEnable.setDescription('Secure NS Global Manager/PRO traffic via VPN encryption.')
nsSetGlbMngEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngEnable.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngEnable.setDescription('Enable Global Manager service on NetScreen device.')
nsSetGlbProEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbProEnable.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbProEnable.setDescription('Enable Global Pro Management service on NetScreen device.')
nsSetGlbManagerSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 10, 4))
nsSetGlbMngSerName = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngSerName.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngSerName.setDescription('Server Name of Global Manager service.')
nsSetGlbMngSerTCP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngSerTCP.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngSerTCP.setDescription('TCP port number of Global Manager service.')
nsSetGlbMngSerUDP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngSerUDP.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngSerUDP.setDescription('UDP port number of Global Manager service.')
nsSetGlbMngLocal = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngLocal.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngLocal.setDescription('Global Manager service listening port number(NS device side).')
nsSetGlbProManagerSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 10, 5))
nsSetGlbProPriSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 5, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbProPriSer.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbProPriSer.setDescription('Primary IP Address of Global PRO Server.')
nsSetGlbProSecSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 5, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbProSecSer.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbProSecSer.setDescription('Secondary IP Address of Global PRO Server')
nsSetGlbMngSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6))
nsSetGlbMngProtDist = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngProtDist.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngProtDist.setDescription('Enable Protocol Distribution in global management service.')
nsSetGlbMngEthStatis = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngEthStatis.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngEthStatis.setDescription('Enable Ethernet Statistics in global management service.')
nsSetGlbMngAttStatis = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngAttStatis.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngAttStatis.setDescription('Enable Attack Statistics in global management service.')
nsSetGlbMngPlyStatis = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngPlyStatis.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngPlyStatis.setDescription('Enable Policy Statistics in global management service.')
nsSetGlbMngFlowStatis = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngFlowStatis.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngFlowStatis.setDescription('Enable Flow Statistics in global management service.')
nsSetGlbMngTrafAlm = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngTrafAlm.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngTrafAlm.setDescription('Enable Traffic Alarms in global management service.')
nsSetGlbMngAttAlm = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngAttAlm.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngAttAlm.setDescription('Enable Attack Alarms in global management service.')
nsSetGlbMngEvtAlm = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngEvtAlm.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngEvtAlm.setDescription('Enable Event Alarms in global management service.')
nsSetGlbMngCfgLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngCfgLog.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngCfgLog.setDescription('Enable Configuration Logs in global management service.')
nsSetGlbMngTrafLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngTrafLog.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngTrafLog.setDescription('Enable Traffic Logs in global management service.')
nsSetGlbMngInfoLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngInfoLog.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngInfoLog.setDescription('Enable Information Logs in global management service.')
nsSetGlbMngSelfLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGlbMngSelfLog.setStatus('current')
if mibBuilder.loadTexts: nsSetGlbMngSelfLog.setDescription('Enable Self Logs in global management service.')
mibBuilder.exportSymbols("NETSCREEN-SET-GLB-MIB", nsSetGlbMngEnable=nsSetGlbMngEnable, nsSetGlbMngVPNEnable=nsSetGlbMngVPNEnable, nsSetGlbMngLocal=nsSetGlbMngLocal, nsSetGlbProManagerSetting=nsSetGlbProManagerSetting, nsSetGlbMng=nsSetGlbMng, nsSetGlbMngSetting=nsSetGlbMngSetting, nsSetGlbMngSerUDP=nsSetGlbMngSerUDP, nsSetGlbMngEvtAlm=nsSetGlbMngEvtAlm, nsSetGlbProPriSer=nsSetGlbProPriSer, nsSetGlbMngPlyStatis=nsSetGlbMngPlyStatis, PYSNMP_MODULE_ID=netscreenSetGlbMibModule, nsSetGlbMngFlowStatis=nsSetGlbMngFlowStatis, nsSetGlbMngEthStatis=nsSetGlbMngEthStatis, nsSetGlbProSecSer=nsSetGlbProSecSer, nsSetGlbMngInfoLog=nsSetGlbMngInfoLog, nsSetGlbMngAttAlm=nsSetGlbMngAttAlm, netscreenSetGlbMibModule=netscreenSetGlbMibModule, nsSetGlbMngCfgLog=nsSetGlbMngCfgLog, nsSetGlbMngSerName=nsSetGlbMngSerName, nsSetGlbMngTrafLog=nsSetGlbMngTrafLog, nsSetGlbProEnable=nsSetGlbProEnable, nsSetGlbManagerSetting=nsSetGlbManagerSetting, nsSetGlbMngProtDist=nsSetGlbMngProtDist, nsSetGlbMngSerTCP=nsSetGlbMngSerTCP, nsSetGlbMngAttStatis=nsSetGlbMngAttStatis, nsSetGlbMngSelfLog=nsSetGlbMngSelfLog, nsSetGlbMngTrafAlm=nsSetGlbMngTrafAlm)
