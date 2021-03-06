#
# PySNMP MIB module MITEL-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-NAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, IpAddress, Counter32, enterprises, Unsigned32, Integer32, iso, TimeTicks, NotificationType, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "IpAddress", "Counter32", "enterprises", "Unsigned32", "Integer32", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
mitelIpGrpNatGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2))
mitelIpGrpNatGroup.setRevisions(('2003-03-24 10:01', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpNatGroup.setRevisionsDescriptions(('Convert to SMIv2', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpNatGroup.setLastUpdated('200303241001Z')
if mibBuilder.loadTexts: mitelIpGrpNatGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpNatGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpNatGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelNatGrpIfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1), )
if mibBuilder.loadTexts: mitelNatGrpIfTable.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfTable.setDescription('The IP network address translation configuration table.')
mitelNatGrpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1), ).setIndexNames((0, "MITEL-NAT-MIB", "mitelNatGrpIfAddr"))
if mibBuilder.loadTexts: mitelNatGrpIfEntry.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfEntry.setDescription('Contains information about network address translation on a single IP interface.')
mitelNatGrpIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNatGrpIfAddr.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfAddr.setDescription('The IP address of the interface.')
mitelNatGrpIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfEnable.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfEnable.setDescription('Configures the router to enable IP NAT on a virtual interface.')
mitelNatGrpIfUdpLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 3), Integer32().clone(900)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfUdpLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfUdpLifetime.setDescription('Specifies timeout in seconds for a NAT UDP session.')
mitelNatGrpIfTcpLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 4), Integer32().clone(900)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfTcpLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfTcpLifetime.setDescription('Specifies timeout in seconds for a NAT TCP session.')
mitelNatGrpIfTcpFinLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 5), Integer32().clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfTcpFinLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfTcpFinLifetime.setDescription('Specifies timeout in seconds for a NAT TCP session once a FIN was seen.')
mitelNatGrpIfTcpRstLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 6), Integer32().clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfTcpRstLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfTcpRstLifetime.setDescription('Specifies timeout in seconds for a NAT TCP session once a RST was seen.')
mitelNatGrpIfPingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 7), Integer32().clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpIfPingLifetime.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfPingLifetime.setDescription('Specifies timeout in seconds for an ICMP echo.')
mitelNatGrpIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelNatGrpIfStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelNatGrpIfStatus.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfStatus.setDescription('The current status of this entry.')
mitelNatGrpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNatGrpIfIndex.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpIfIndex.setDescription('The current Interface this entry pertains to.')
mitelNatGrpRedirTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2), )
if mibBuilder.loadTexts: mitelNatGrpRedirTable.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirTable.setDescription('The IP network address translation redirection table.')
mitelNatGrpRedirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1), ).setIndexNames((0, "MITEL-NAT-MIB", "mitelNatGrpRedirOldAddr"), (0, "MITEL-NAT-MIB", "mitelNatGrpRedirProto"), (0, "MITEL-NAT-MIB", "mitelNatGrpRedirOldPort"))
if mibBuilder.loadTexts: mitelNatGrpRedirEntry.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirEntry.setDescription('Contains information about network address translation incoming on a single IP interface.')
mitelNatGrpRedirOldAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNatGrpRedirOldAddr.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirOldAddr.setDescription('The IP address of the interface.')
mitelNatGrpRedirProto = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNatGrpRedirProto.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirProto.setDescription('Identifies the IP protocol to redirect, 6 or 17.')
mitelNatGrpRedirOldPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNatGrpRedirOldPort.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirOldPort.setDescription('Identifies the TCP or UDP port to redirect.')
mitelNatGrpRedirNewAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpRedirNewAddr.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirNewAddr.setDescription('The IP address to which the datagram is to be redirected. Default is 0.0.0.0 ')
mitelNatGrpRedirNewPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNatGrpRedirNewPort.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirNewPort.setDescription('The TCP or UDP port to which the datagram is to be redirected.')
mitelNatGrpRedirStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelNatGrpRedirStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelNatGrpRedirStatus.setStatus('current')
if mibBuilder.loadTexts: mitelNatGrpRedirStatus.setDescription('The current status of this entry.')
mibBuilder.exportSymbols("MITEL-NAT-MIB", mitelNatGrpRedirNewPort=mitelNatGrpRedirNewPort, mitelProprietary=mitelProprietary, mitelNatGrpRedirEntry=mitelNatGrpRedirEntry, mitelNatGrpIfUdpLifetime=mitelNatGrpIfUdpLifetime, mitelNatGrpIfPingLifetime=mitelNatGrpIfPingLifetime, mitelNatGrpIfIndex=mitelNatGrpIfIndex, mitelNatGrpIfTcpLifetime=mitelNatGrpIfTcpLifetime, mitelNatGrpRedirTable=mitelNatGrpRedirTable, mitelNatGrpRedirStatus=mitelNatGrpRedirStatus, mitelNatGrpIfEnable=mitelNatGrpIfEnable, mitelIpNetRouter=mitelIpNetRouter, mitelNatGrpIfTcpRstLifetime=mitelNatGrpIfTcpRstLifetime, mitelNatGrpIfAddr=mitelNatGrpIfAddr, mitelNatGrpRedirProto=mitelNatGrpRedirProto, mitelNatGrpIfTable=mitelNatGrpIfTable, mitelPropIpNetworking=mitelPropIpNetworking, mitelNatGrpIfStatus=mitelNatGrpIfStatus, mitelNatGrpRedirOldPort=mitelNatGrpRedirOldPort, mitelRouterIpGroup=mitelRouterIpGroup, mitelNatGrpIfTcpFinLifetime=mitelNatGrpIfTcpFinLifetime, mitel=mitel, mitelNatGrpIfEntry=mitelNatGrpIfEntry, mitelIpGrpNatGroup=mitelIpGrpNatGroup, mitelNatGrpRedirOldAddr=mitelNatGrpRedirOldAddr, PYSNMP_MODULE_ID=mitelIpGrpNatGroup, mitelNatGrpRedirNewAddr=mitelNatGrpRedirNewAddr)
