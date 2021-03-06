#
# PySNMP MIB module ZHONE-COM-IP-DNS-RESOLVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-DNS-RESOLVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, TimeTicks, Integer32, iso, MibIdentifier, ObjectIdentity, Unsigned32, Bits, Counter64, Counter32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "iso", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Bits", "Counter64", "Counter32", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdEntry, rdIndex = mibBuilder.importSymbols("ZHONE-COM-IP-RD-MIB", "rdEntry", "rdIndex")
zhoneModules, zhoneIp = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneIp")
ZhoneAdminString, ZhoneRowStatus = mibBuilder.importSymbols("Zhone-TC", "ZhoneAdminString", "ZhoneRowStatus")
comIpDnsResolver = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 62))
comIpDnsResolver.setRevisions(('1900-09-11 16:08', '1900-09-29 09:33',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comIpDnsResolver.setRevisionsDescriptions(('V01.00.00 - Initial Release', 'V01.00.01 - Added ZHONE-KEYWORD markup',))
if mibBuilder.loadTexts: comIpDnsResolver.setLastUpdated('0009291000Z')
if mibBuilder.loadTexts: comIpDnsResolver.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: comIpDnsResolver.setContactInfo('Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: comIpDnsResolver.setDescription('DNS Resolver MIB IP Software Minneapolis, MN')
dnsResolver = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12))
if mibBuilder.loadTexts: dnsResolver.setStatus('current')
if mibBuilder.loadTexts: dnsResolver.setDescription('DNS Resolver objects based on RFC 1612.')
zhDnsResConfigImplementIdent = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 1), ZhoneAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhDnsResConfigImplementIdent.setReference('See RFC1612: dnsResConfig.dnsResConfigImplementIdent')
if mibBuilder.loadTexts: zhDnsResConfigImplementIdent.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigImplementIdent.setDescription("The implementation identification string for the resolver software in use on the system, for example; `RES-2.1'. The maximum length for this name is 32 characters.")
zhDnsResConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2), )
if mibBuilder.loadTexts: zhDnsResConfigTable.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigTable.setDescription('Table of nameservers information used by the resolver to send a query. Rows are created and destroyed whenever a routing domain is created or destroyed. Rows cannot be created or destroyed via SNMP.')
zhDnsResConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1), )
rdEntry.registerAugmentions(("ZHONE-COM-IP-DNS-RESOLVER-MIB", "zhDnsResConfigEntry"))
zhDnsResConfigEntry.setIndexNames(*rdEntry.getIndexNames())
if mibBuilder.loadTexts: zhDnsResConfigEntry.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigEntry.setDescription('A single routing domain in a single subnet.')
zhDnsResConfigQueryOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hostsFirst", 1), ("dnsFirst", 2), ("dnsOnly", 3))).clone('hostsFirst')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhDnsResConfigQueryOrder.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigQueryOrder.setDescription('Kind of resolver query for this routing domain: hostsFirst(1) searches the local hosts table first, then the list of nameservers dnsFirst(2) searches the list of nameservers first, then the local hosts table dnsOnly(3) searches only the list of nameservers')
zhDnsResConfigDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhDnsResConfigDomainName.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigDomainName.setDescription('Domain name to use for searches in this routing domain. The maximum length for this name is 255 characters.')
zhDnsResConfigFirstNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhDnsResConfigFirstNameServer.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigFirstNameServer.setDescription('The IP address of the first/primary name server for this routing domain.')
zhDnsResConfigSecondNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 4), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhDnsResConfigSecondNameServer.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigSecondNameServer.setDescription('The IP address of the secondary name server for this routing domain. This nameserver is queried if the first nameserver cannot resolve the query. If a secondary name server has not been defined, this field is set to 0.0.0.0')
zhDnsResConfigThirdNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhDnsResConfigThirdNameServer.setStatus('current')
if mibBuilder.loadTexts: zhDnsResConfigThirdNameServer.setDescription('The IP address of the third name server for this routing domain. This nameserver is queried if the first nameserver and the secondary nameserver cannot resolve the query. If a third name server has not been defined, this field is set to 0.0.0.0')
zhDnsResHostsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3), )
if mibBuilder.loadTexts: zhDnsResHostsTable.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsTable.setDescription('This is the local hosts table (ie. /etc/hosts) for each routing domain.')
zhDnsResHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1), ).setIndexNames((0, "ZHONE-COM-IP-RD-MIB", "rdIndex"), (0, "ZHONE-COM-IP-DNS-RESOLVER-MIB", "zhDnsResHostsIpAddress"))
if mibBuilder.loadTexts: zhDnsResHostsEntry.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsEntry.setDescription('A particular host entry per routing domain. Rows are created and destroyed whenever a hostname within a routing domain is created and destroyed, ie. rows are added by setting zhDnsResHostsRowStatus to createAndGo. Rows are removed by setting zhDnsResHostsRowStatus to destroy. The minimum columns required to create new entry are zhDnsResHostsIpAddress and zhDnsResHostsName.')
zhDnsResHostsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: zhDnsResHostsIpAddress.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsIpAddress.setDescription('The IP address of this entry. 127.1 (127.0.0.1) is a valid ip address.')
zhDnsResHostsName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsName.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsName.setDescription('Hostname for this entry. The hostname can be either fully-qualified or hostname only. The maximum length for this name is 255 characters.')
zhDnsResHostsAlias1 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsAlias1.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsAlias1.setDescription('Hostname alias for this entry. The hostname can be either fully-qualified or hostname only. The maximum length for this name is 255 characters.')
zhDnsResHostsAlias2 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsAlias2.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsAlias2.setDescription('Another hostname alias for this entry. The hostname can be either fully-qualified or hostname only. The maximum length for this name is 255 characters.')
zhDnsResHostsAlias3 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsAlias3.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsAlias3.setDescription('Another hostname alias for this entry. The hostname can be either fully-qualified or hostname only. The maximum length for this name is 255 characters.')
zhDnsResHostsAlias4 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 6), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsAlias4.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsAlias4.setDescription('Another hostname alias for this entry. The hostname can be either fully-qualified or hostname only. The maximum length for this name is 255 characters.')
zhDnsResHostsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 7), ZhoneRowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhDnsResHostsRowStatus.setReference('See ZHONE-TC-MIB for definition of ZhoneRowStatus.')
if mibBuilder.loadTexts: zhDnsResHostsRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhDnsResHostsRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
mibBuilder.exportSymbols("ZHONE-COM-IP-DNS-RESOLVER-MIB", zhDnsResHostsIpAddress=zhDnsResHostsIpAddress, zhDnsResConfigQueryOrder=zhDnsResConfigQueryOrder, zhDnsResConfigSecondNameServer=zhDnsResConfigSecondNameServer, zhDnsResHostsRowStatus=zhDnsResHostsRowStatus, zhDnsResHostsEntry=zhDnsResHostsEntry, zhDnsResConfigEntry=zhDnsResConfigEntry, zhDnsResHostsAlias4=zhDnsResHostsAlias4, dnsResolver=dnsResolver, zhDnsResHostsAlias1=zhDnsResHostsAlias1, zhDnsResConfigDomainName=zhDnsResConfigDomainName, zhDnsResHostsTable=zhDnsResHostsTable, zhDnsResHostsName=zhDnsResHostsName, PYSNMP_MODULE_ID=comIpDnsResolver, zhDnsResHostsAlias2=zhDnsResHostsAlias2, zhDnsResConfigImplementIdent=zhDnsResConfigImplementIdent, zhDnsResHostsAlias3=zhDnsResHostsAlias3, zhDnsResConfigTable=zhDnsResConfigTable, zhDnsResConfigFirstNameServer=zhDnsResConfigFirstNameServer, comIpDnsResolver=comIpDnsResolver, zhDnsResConfigThirdNameServer=zhDnsResConfigThirdNameServer)
