#
# PySNMP MIB module TIARA-DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-DOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Bits, iso, ObjectIdentity, IpAddress, Counter32, MibIdentifier, Counter64, NotificationType, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Bits", "iso", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraDenialOfServiceMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 50))
if mibBuilder.loadTexts: tiaraDenialOfServiceMib.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: tiaraDenialOfServiceMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraDenialOfServiceMib.setContactInfo(' Tiara Networks Customer Service Postal: 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraDenialOfServiceMib.setDescription("The MIB module to describe Tiara's Denial of Service MIB")
tiaraDeosGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 50, 1))
tiaraDeosWan = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraDeosWan.setStatus('current')
if mibBuilder.loadTexts: tiaraDeosWan.setDescription('To enable DOS on interfaces other than ethernet interfaces, set the mib variable to the value true. By default, DOS operation is disabled')
tiaraDeosPing = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraDeosPing.setStatus('current')
if mibBuilder.loadTexts: tiaraDeosPing.setDescription('To enable dropping ping packets to the box, set the mib variable to the value true. By default, dropping ping is disabled')
tiaraDeosIcmp = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraDeosIcmp.setStatus('current')
if mibBuilder.loadTexts: tiaraDeosIcmp.setDescription('To enable dropping icmp packets to the box, set the mib By default, dropping icmp operation is disabled')
tiaraDeosEthTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 50, 2), )
if mibBuilder.loadTexts: tiaraDeosEthTable.setStatus('current')
if mibBuilder.loadTexts: tiaraDeosEthTable.setDescription('Table to configure DOS on ethernet interfaces. By default, DOS operation on ethernet interfaces is disabled')
tiaraDeosEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1), ).setIndexNames((0, "TIARA-DOS-MIB", "ethNum"))
if mibBuilder.loadTexts: tiaraDeosEthEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraDeosEthEntry.setDescription('An entry in the tiaraDeosEthTable')
ethNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: ethNum.setStatus('current')
if mibBuilder.loadTexts: ethNum.setDescription('Index to the tiaraDeosEthTable')
statusDeosEth = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: statusDeosEth.setStatus('current')
if mibBuilder.loadTexts: statusDeosEth.setDescription('To enable DOS on an ethernet interface indexed by ethNum, set statusDeosEth to value true. To disable set to value false. Get on statusDeosEth gives the current configuration of DOS for an ethernet interface.')
tiaraIncompleteTcpTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3), )
if mibBuilder.loadTexts: tiaraIncompleteTcpTable.setStatus('current')
if mibBuilder.loadTexts: tiaraIncompleteTcpTable.setDescription('Table of incomplete TCP connections')
tiaraIncompleteTcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1), ).setIndexNames((0, "TIARA-DOS-MIB", "ethNum"))
if mibBuilder.loadTexts: tiaraIncompleteTcpEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraIncompleteTcpEntry.setDescription('An entry in the tiaraIncompleteTcpTable')
tcpIncompleteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: tcpIncompleteIndex.setStatus('current')
if mibBuilder.loadTexts: tcpIncompleteIndex.setDescription('A unique identifier for the incomplete connection')
srcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcIpAddress.setStatus('current')
if mibBuilder.loadTexts: srcIpAddress.setDescription('Source IP Address')
destIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: destIpAddress.setStatus('current')
if mibBuilder.loadTexts: destIpAddress.setDescription('Destination IP Address')
srcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcPort.setStatus('current')
if mibBuilder.loadTexts: srcPort.setDescription('Source Port')
destPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: destPort.setStatus('current')
if mibBuilder.loadTexts: destPort.setDescription('Destination Port')
mibBuilder.exportSymbols("TIARA-DOS-MIB", tiaraDeosEthEntry=tiaraDeosEthEntry, tiaraDeosWan=tiaraDeosWan, tiaraDeosEthTable=tiaraDeosEthTable, tiaraDeosGlobal=tiaraDeosGlobal, statusDeosEth=statusDeosEth, srcIpAddress=srcIpAddress, tiaraIncompleteTcpEntry=tiaraIncompleteTcpEntry, srcPort=srcPort, tcpIncompleteIndex=tcpIncompleteIndex, destIpAddress=destIpAddress, tiaraDenialOfServiceMib=tiaraDenialOfServiceMib, destPort=destPort, tiaraIncompleteTcpTable=tiaraIncompleteTcpTable, tiaraDeosIcmp=tiaraDeosIcmp, ethNum=ethNum, PYSNMP_MODULE_ID=tiaraDenialOfServiceMib, tiaraDeosPing=tiaraDeosPing)
