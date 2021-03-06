#
# PySNMP MIB module CISCO-DMN-DSG-PROTOCOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-PROTOCOLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Integer32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits, Counter64, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits", "Counter64", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGProtocols = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39))
ciscoDSGProtocols.setRevisions(('2013-07-10 19:03', '2012-03-07 07:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGProtocols.setRevisionsDescriptions(('V01.00.01 2013-07-10 Replace DTX with Syslog.', 'V01.00.00 2012-03-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGProtocols.setLastUpdated('201307101903Z')
if mibBuilder.loadTexts: ciscoDSGProtocols.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGProtocols.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGProtocols.setDescription('Cisco Routing MIB.')
protocolsCtrlTelnet = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlTelnet.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlTelnet.setDescription('Select whether to allow Telnet connections or not')
protocolsCtrlSSH = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSSH.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlSSH.setDescription('Select whether to allow secure shell connections or not.')
protocolsCtrlHTTP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("secure", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlHTTP.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlHTTP.setDescription('Select whether to allow web connections or not and choose secure or unsecure mode.')
protocolsCtrlSNMP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSNMP.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlSNMP.setDescription('Select whether to allow SNMP connections or not.')
protocolsCtrlRIP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlRIP.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlRIP.setDescription('Select whether to allow RIPv2 protocol or not.')
protocolsCtrlMPE = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fwdNone", 1), ("fwdAll", 2), ("fwdFiltered", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlMPE.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlMPE.setDescription('Select whether to allow MPE protocol or not and select a mode.')
protocolsCtrlIGMP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("v3", 2), ("v2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlIGMP.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlIGMP.setDescription('Select whether to allow IGMP protocol or not.')
protocolslTimeoutsIdleSessonGlobal = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1209600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolslTimeoutsIdleSessonGlobal.setStatus('current')
if mibBuilder.loadTexts: protocolslTimeoutsIdleSessonGlobal.setDescription('Number of seconds after which an idle session will timeout. Enter 0 to never timeout. Minimum timeout is 30 seconds.')
protocolsCtrlSyslog = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disable", 1), ("legacy", 2), ("syslogTcp", 3), ("syslogUdp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslog.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlSyslog.setDescription('Select whether to allow Syslog and select a mode.')
protocolsCtrlSyslogCfgIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgIpAddr.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgIpAddr.setDescription('Syslog server entry IP Address.')
protocolsCtrlSyslogCfgPort = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgPort.setStatus('current')
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgPort.setDescription('Syslog server entry port number.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-PROTOCOLS-MIB", protocolsCtrlSSH=protocolsCtrlSSH, protocolsCtrlSyslog=protocolsCtrlSyslog, protocolsCtrlIGMP=protocolsCtrlIGMP, protocolslTimeoutsIdleSessonGlobal=protocolslTimeoutsIdleSessonGlobal, PYSNMP_MODULE_ID=ciscoDSGProtocols, protocolsCtrlSyslogCfgPort=protocolsCtrlSyslogCfgPort, protocolsCtrlMPE=protocolsCtrlMPE, protocolsCtrlHTTP=protocolsCtrlHTTP, protocolsCtrlTelnet=protocolsCtrlTelnet, protocolsCtrlSNMP=protocolsCtrlSNMP, protocolsCtrlSyslogCfgIpAddr=protocolsCtrlSyslogCfgIpAddr, ciscoDSGProtocols=ciscoDSGProtocols, protocolsCtrlRIP=protocolsCtrlRIP)
