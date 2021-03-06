#
# PySNMP MIB module ACLEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACLEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aclExt, = mibBuilder.importSymbols("APENT-MIB", "aclExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, iso, ObjectIdentity, IpAddress, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
apAclExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 23, 1))
if mibBuilder.loadTexts: apAclExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apAclExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apAclExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978 206 3000 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apAclExtMib.setDescription('The MIB module used to describe the ArrowPoint Control List clause table')
apAclExtEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 23, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apAclExtEnable.setStatus('current')
if mibBuilder.loadTexts: apAclExtEnable.setDescription('The global state of the ACLs, either enabled or disabled')
apAclExtLogEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 23, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apAclExtLogEnable.setStatus('obsolete')
if mibBuilder.loadTexts: apAclExtLogEnable.setDescription('This MIB is Obsoleted')
apMainAclTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 23, 4), )
if mibBuilder.loadTexts: apMainAclTable.setStatus('current')
if mibBuilder.loadTexts: apMainAclTable.setDescription('A list of ACLs.')
apMainAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1), ).setIndexNames((0, "ACLEXT-MIB", "apMainAclIndex"))
if mibBuilder.loadTexts: apMainAclEntry.setStatus('current')
if mibBuilder.loadTexts: apMainAclEntry.setDescription('A set of parameters which describe an access control list.')
apMainAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apMainAclIndex.setStatus('current')
if mibBuilder.loadTexts: apMainAclIndex.setDescription('The ACL Index')
apMainAclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apMainAclStatus.setStatus('current')
if mibBuilder.loadTexts: apMainAclStatus.setDescription('Status entry for this row ')
apMainAclCountZero = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("reset", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apMainAclCountZero.setStatus('current')
if mibBuilder.loadTexts: apMainAclCountZero.setDescription('Reset all clause hit counts for the ACL')
apAclTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5), )
if mibBuilder.loadTexts: apAclTable.setStatus('current')
if mibBuilder.loadTexts: apAclTable.setDescription('A list of ACL clauses.')
apAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1), ).setIndexNames((0, "ACLEXT-MIB", "apMainAclIndex"), (0, "ACLEXT-MIB", "apAclSubIndex"))
if mibBuilder.loadTexts: apAclEntry.setStatus('current')
if mibBuilder.loadTexts: apAclEntry.setDescription('A set of parameters which describe an access control list clause.')
apAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclIndex.setStatus('current')
if mibBuilder.loadTexts: apAclIndex.setDescription('The ACL Index')
apAclSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSubIndex.setStatus('current')
if mibBuilder.loadTexts: apAclSubIndex.setDescription('The ACL Current line Index')
apAclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2), ("bypass", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclAction.setStatus('current')
if mibBuilder.loadTexts: apAclAction.setDescription('The ACL Permit or Deny Action')
apAclProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 9, 17, 6, 89))).clone(namedValues=NamedValues(("any", 0), ("icmp", 1), ("igmp", 2), ("igp", 9), ("udp", 17), ("tcp", 6), ("ospf", 89)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclProtocol.setStatus('current')
if mibBuilder.loadTexts: apAclProtocol.setDescription('The IP Protocol')
apAclSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourceIpAddr.setStatus('current')
if mibBuilder.loadTexts: apAclSourceIpAddr.setDescription('The source IP Address')
apAclSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourceMask.setStatus('current')
if mibBuilder.loadTexts: apAclSourceMask.setDescription('The source IP Address Mask')
apAclSourceGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourceGroup.setStatus('current')
if mibBuilder.loadTexts: apAclSourceGroup.setDescription('The source group name')
apAclDestIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestIpAddr.setStatus('current')
if mibBuilder.loadTexts: apAclDestIpAddr.setDescription('The destination IP Address')
apAclDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestMask.setStatus('current')
if mibBuilder.loadTexts: apAclDestMask.setDescription('The destination IP Address mask')
apAclDestContent = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 10), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestContent.setStatus('current')
if mibBuilder.loadTexts: apAclDestContent.setDescription('The destination Content Rule name')
apAclPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclPrecedence.setStatus('current')
if mibBuilder.loadTexts: apAclPrecedence.setDescription('The IP precedence field')
apAclTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclTOS.setStatus('current')
if mibBuilder.loadTexts: apAclTOS.setDescription('The IP TOS field')
apAclLog = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclLog.setStatus('current')
if mibBuilder.loadTexts: apAclLog.setDescription('Log hits on this clause')
apAclStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclStartTime.setStatus('current')
if mibBuilder.loadTexts: apAclStartTime.setDescription('Time for this clause to take effect')
apAclStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclStopTime.setStatus('current')
if mibBuilder.loadTexts: apAclStopTime.setDescription('Time for this clause to cease having an effect')
apAclQOSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclQOSClass.setStatus('current')
if mibBuilder.loadTexts: apAclQOSClass.setDescription('Log hits on this clause')
apAclSourcePortOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("lt", 1), ("gt", 2), ("eq", 3), ("neq", 4), ("range", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourcePortOperator.setStatus('current')
if mibBuilder.loadTexts: apAclSourcePortOperator.setDescription('Source Port Operator')
apAclSourcePortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourcePortStart.setStatus('current')
if mibBuilder.loadTexts: apAclSourcePortStart.setDescription('Source Port Range Start')
apAclSourcePortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourcePortEnd.setStatus('current')
if mibBuilder.loadTexts: apAclSourcePortEnd.setDescription('Source Port Range End')
apAclDestPortOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("lt", 1), ("gt", 2), ("eq", 3), ("neq", 4), ("range", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestPortOperator.setStatus('current')
if mibBuilder.loadTexts: apAclDestPortOperator.setDescription('Destination Port Operator')
apAclDestPortEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 20, 21, 23, 25, 53, 70, 80, 110, 119, 123, 179, 389, 443))).clone(namedValues=NamedValues(("none", 0), ("ftp-data", 20), ("ftp", 21), ("telnet", 23), ("smtp", 25), ("domain", 53), ("gopher", 70), ("http", 80), ("pop", 110), ("nntp", 119), ("ntp", 123), ("bgp", 179), ("ldap", 389), ("https", 443)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestPortEnum.setStatus('current')
if mibBuilder.loadTexts: apAclDestPortEnum.setDescription('Destination Port Enumeration')
apAclDestPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestPortStart.setStatus('current')
if mibBuilder.loadTexts: apAclDestPortStart.setDescription('Destination Port Range Start')
apAclDestPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestPortEnd.setStatus('current')
if mibBuilder.loadTexts: apAclDestPortEnd.setDescription('Destination Port Range End')
apAclEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclEnable.setStatus('current')
if mibBuilder.loadTexts: apAclEnable.setDescription('The state of the ACL, either enabled or disabled')
apAclProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclProtocolNumber.setStatus('current')
if mibBuilder.loadTexts: apAclProtocolNumber.setDescription('The IP Protocol')
apAclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 26), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclStatus.setStatus('current')
if mibBuilder.loadTexts: apAclStatus.setDescription('Status entry for this row ')
apAclPreferredService = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclPreferredService.setStatus('current')
if mibBuilder.loadTexts: apAclPreferredService.setDescription('Preferred Service based on hits on this ACL clause')
apAclSourceNQLName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclSourceNQLName.setStatus('current')
if mibBuilder.loadTexts: apAclSourceNQLName.setDescription('Network Qualifier List used in the source this ACL clause')
apAclDestNQLName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclDestNQLName.setStatus('current')
if mibBuilder.loadTexts: apAclDestNQLName.setDescription('Network Qualifier List used in the source this ACL clause')
apAclCountContentHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 30), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclCountContentHits.setStatus('current')
if mibBuilder.loadTexts: apAclCountContentHits.setDescription('Count of content hits on this ACL clause')
apAclCountRouterHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 31), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclCountRouterHits.setStatus('current')
if mibBuilder.loadTexts: apAclCountRouterHits.setDescription('Count of router hits on this ACL clause')
apAclCountDNSHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 32), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAclCountDNSHits.setStatus('current')
if mibBuilder.loadTexts: apAclCountDNSHits.setDescription('Count of DNS hits on this ACL clause')
mibBuilder.exportSymbols("ACLEXT-MIB", apAclCountRouterHits=apAclCountRouterHits, PYSNMP_MODULE_ID=apAclExtMib, apAclQOSClass=apAclQOSClass, apAclSourcePortOperator=apAclSourcePortOperator, apAclPrecedence=apAclPrecedence, apAclTOS=apAclTOS, apAclStatus=apAclStatus, apAclSourceMask=apAclSourceMask, apAclAction=apAclAction, apAclSubIndex=apAclSubIndex, apAclSourcePortStart=apAclSourcePortStart, apMainAclIndex=apMainAclIndex, apAclDestPortEnum=apAclDestPortEnum, apMainAclEntry=apMainAclEntry, apAclProtocolNumber=apAclProtocolNumber, apAclStopTime=apAclStopTime, apAclPreferredService=apAclPreferredService, apAclExtEnable=apAclExtEnable, apMainAclTable=apMainAclTable, apAclSourceGroup=apAclSourceGroup, apAclDestNQLName=apAclDestNQLName, apAclCountDNSHits=apAclCountDNSHits, apAclStartTime=apAclStartTime, apAclDestPortEnd=apAclDestPortEnd, apAclEnable=apAclEnable, apAclExtLogEnable=apAclExtLogEnable, apAclDestPortStart=apAclDestPortStart, apAclEntry=apAclEntry, apAclSourceNQLName=apAclSourceNQLName, apAclDestPortOperator=apAclDestPortOperator, apAclLog=apAclLog, apAclProtocol=apAclProtocol, apMainAclStatus=apMainAclStatus, apAclDestMask=apAclDestMask, apAclExtMib=apAclExtMib, apAclDestIpAddr=apAclDestIpAddr, apAclTable=apAclTable, apMainAclCountZero=apMainAclCountZero, apAclSourceIpAddr=apAclSourceIpAddr, apAclCountContentHits=apAclCountContentHits, apAclSourcePortEnd=apAclSourcePortEnd, apAclIndex=apAclIndex, apAclDestContent=apAclDestContent)
