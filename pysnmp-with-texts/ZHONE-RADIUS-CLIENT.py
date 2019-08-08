#
# PySNMP MIB module ZHONE-RADIUS-CLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-RADIUS-CLIENT
# Produced by pysmi-0.3.4 at Wed May  1 15:47:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, ModuleIdentity, iso, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, IpAddress, TimeTicks, Gauge32, ObjectIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "iso", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "Integer32", "Unsigned32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zhoneRadius, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneRadius", "zhoneModules")
comRadiusClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 112))
comRadiusClient.setRevisions(('2006-11-15 14:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comRadiusClient.setRevisionsDescriptions(('Version 1.0.0 - initial creation of Zhone Radius MIB.',))
if mibBuilder.loadTexts: comRadiusClient.setLastUpdated('200611151230Z')
if mibBuilder.loadTexts: comRadiusClient.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: comRadiusClient.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: comRadiusClient.setDescription('This is the Zhone module identifier for the Zhone Bonding module.')
zhoneRadiusClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1))
if mibBuilder.loadTexts: zhoneRadiusClient.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClient.setDescription('Start of the Zhone RADIUS Client MIB.')
zhoneRadiusClientTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1), )
if mibBuilder.loadTexts: zhoneRadiusClientTable.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientTable.setDescription('The ZhoneRadiusClientTable contains the information required to authenticate a user using the RADIUS protocol. One entry exists per RADIUS server. ')
zhoneRadiusClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1), ).setIndexNames((0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientIndex"), (0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientId"))
if mibBuilder.loadTexts: zhoneRadiusClientEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientEntry.setDescription('An entry in the Zhone Radius Client table. ')
zhoneRadiusClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2137483647)))
if mibBuilder.loadTexts: zhoneRadiusClientIndex.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientIndex.setDescription('This index is used to group serveral RADIUS server description together. This index is used in various Zhone provisioning information to specify which group of entries to use for a specific task or purpose. ')
zhoneRadiusClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2137483647)))
if mibBuilder.loadTexts: zhoneRadiusClientId.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientId.setDescription('This index specifies the specific RADIUS server information into a group of entries. When this group is provisioned for a task, this index is the order in which the servers will be contacted by the client. ')
zhoneRadiusClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientRowStatus.setDescription('Entry row status for SNMP create-and-go operation. ')
zhoneRadiusClientServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientServerName.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientServerName.setDescription('Radius server host name or IP address.')
zhoneRadiusClientUdpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientUdpPortNumber.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientUdpPortNumber.setDescription('The destination UDP port number for RADIUS authentication packets when authenticating using this server. ')
zhoneRadiusClientSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientSharedSecret.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientSharedSecret.setDescription('This is the shared secret used by the RADIUS client and server for authentication and packet encryption. ')
zhoneRadiusClientRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRetryCount.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientRetryCount.setDescription('The number of times to retry a failed request before we rotate to the next server in the list. ')
zhoneRadiusClientRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRetryInterval.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusClientRetryInterval.setDescription('This is the minimum time (in seconds) the device will wait before asuuming an error occurred and the request is retried. ')
zhoneRadiusObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 14, 2)).setObjects(("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientServerName"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientUdpPortNumber"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientSharedSecret"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryCount"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneRadiusObjectGroup = zhoneRadiusObjectGroup.setStatus('current')
if mibBuilder.loadTexts: zhoneRadiusObjectGroup.setDescription('Description.')
mibBuilder.exportSymbols("ZHONE-RADIUS-CLIENT", zhoneRadiusClientEntry=zhoneRadiusClientEntry, zhoneRadiusClientId=zhoneRadiusClientId, zhoneRadiusClientRowStatus=zhoneRadiusClientRowStatus, zhoneRadiusClientTable=zhoneRadiusClientTable, zhoneRadiusClientRetryCount=zhoneRadiusClientRetryCount, PYSNMP_MODULE_ID=comRadiusClient, zhoneRadiusClient=zhoneRadiusClient, zhoneRadiusClientServerName=zhoneRadiusClientServerName, comRadiusClient=comRadiusClient, zhoneRadiusClientSharedSecret=zhoneRadiusClientSharedSecret, zhoneRadiusClientRetryInterval=zhoneRadiusClientRetryInterval, zhoneRadiusObjectGroup=zhoneRadiusObjectGroup, zhoneRadiusClientIndex=zhoneRadiusClientIndex, zhoneRadiusClientUdpPortNumber=zhoneRadiusClientUdpPortNumber)