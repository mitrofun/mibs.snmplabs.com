#
# PySNMP MIB module CTRON-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-DHCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
nwIpMibs, nwIpComponents, nwIpClientServices, nwIpRouter = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpMibs", "nwIpComponents", "nwIpClientServices", "nwIpRouter")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Bits, ModuleIdentity, IpAddress, Gauge32, iso, Counter32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Bits", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "Counter32", "Integer32", "NotificationType")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
ctDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2))
ctDhcpServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1))
ctDhcpInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2))
ctDhcpClientStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3))
ctDhcpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpAdminStatus.setDescription('This object is used to enable or disable the DHCP server function for the entire device. This object must be set to enabled for the server to function on this device.')
ctDhcpOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOperStatus.setDescription('Indicates the current operating status of the DHCP server function on this device. The value of ctDhcpIfOperStatus for at least one interface must be set to enabled for this object to be enabled.')
ctDhcpDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDiscovers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpDiscovers.setDescription('This value is the number of discover messages received by the DHCP server since the last reset.')
ctDhcpOffers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOffers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOffers.setDescription('This value is the number of offer messages sent by the DHCP server since the last reset.')
ctDhcpRequests = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpRequests.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpRequests.setDescription('This value is the number of request messages received by the DHCP server since the last reset.')
ctDhcpDeclines = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDeclines.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpDeclines.setDescription('This value is the number of decline messages received by the DHCP server since the last reset.')
ctDhcpReleases = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpReleases.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpReleases.setDescription('This value is the number of release messages received by the DHCP server since the last reset.')
ctDhcpAcks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpAcks.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpAcks.setDescription('This value is the number of ack messages sent by the DHCP server since the last reset.')
ctDhcpNaks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNaks.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpNaks.setDescription('This value is the number of nak messages sent by the DHCP server since the last reset.')
ctDhcpOtherServers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOtherServers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOtherServers.setDescription('This value is the number of messages received by the DHCP server since the last reset which were directed to other servers.')
ctDhcpProtocolErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setDescription('This value is the number of protocol errors detected by the DHCP server since the last reset.')
ctDhcpServerTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpServerTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerTime.setDescription('This value is the number of seconds that this DHCP server has been in operation since its non-volatile memory was last cleared.')
ctDhcpNoOfActiveClients = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setDescription('This value is the number of clients who currently have network addresses assigned by this DHCP server.')
ctDhcpReclaimIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpReclaimIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpReclaimIP.setDescription('This object is a method of reclaiming abandoned IP addresses. The value reads as 0.0.0.0. Writing to it with an IP address of a client on the active list will remove the entry from the list. It is used to recover addresses with long leases from clients who have left the network without sending a release notice.')
ctDhcpServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1), )
if mibBuilder.loadTexts: ctDhcpServerIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerIfTable.setDescription("This table contains an entry for each port of a DHCP server which is eligible to perform DHCP functions. The table is indexed by ctDhcpIfIndex, which indicates the value of the MIB 2 ifindex which identifies the device's interface for which the entry exists.")
ctDhcpServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpIfIndex"))
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setDescription('A description of the configuration parameters for a single interface on the DHCP server.')
ctDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfIndex.setDescription('A unique value identifying an element in a sequence of entries which belong to the DHCP server interface list. This value ranges from 1 to 2.')
ctDhcpIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setDescription('Used to enable and disable the DHCP functions on this interface only. This object must be set to enabled for the DHCP functions to occur on this interface.')
ctDhcpIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setDescription('Indicates the current operating status of the DHCP server function on this interface.')
ctDhcpIfServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setDescription('This is the IP address of the interface which is providing access to the DHCP server for clients which are connected to this network.')
ctDhcpIfNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setDescription('This is the IP subnet which is being served by this interface of the DHCP server.')
ctDhcpIfSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setDescription('This is the subnet mask of the IP subnet which is being served by this interface of the DHCP server.')
ctDhcpIfLowestaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setDescription('This is the lowest numerical value of the IP address range that will be assigned to clients by this interface of the DHCP server. Its value must be greater or equal to ctDhcpIfNetworkAddress and less than or equal to ctDhcpIfHighestAddress.')
ctDhcpIfHighestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setDescription('This is the highest numerical value of the IP address range that will be assigned to clients by this interface of the DHCP server. Its value must be greater or equal to ctDhcpIfLowestaddress but remain within ctDhcpIfNetworkAddress.')
ctDhcpIfAddressesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setDescription('This value is the number of clients which are currently using IP addresses assigned by this interface of the DHCP server.')
ctDhcpIfAddressesFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setDescription('This value is the number of IP addresses that are currently available for distribution by this interface of the DHCP server.')
ctDhcpIfLeasePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setDescription('This value is the time period for which an IP address assigned by this interface is valid. The units are seconds. A value of 0 signifys that the lease will never expire.')
ctDhcpIfDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setDescription('This value is an DHCP option that can be passed to a client by this interface if it is requested as part of the DHCP process. This value is the IP address of the default gateway to be used by the client.')
ctDhcpIfDomainNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setDescription('This value is an DHCP option that can be passed to a client by this interface if it is requested as part of the DHCP process. This value is the IP address of the domain name server to be used by the client.')
ctDhcpIfDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 14), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDomainName.setDescription('This value is an DHCP option that can be passed to a client by this interface if it is requested as part of the DHCP process. This value is the domain name to be used by the client.')
ctDhcpIfWINServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfWINServer.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfWINServer.setDescription('This value is an DHCP option that can be passed to a client by this interface if it is requested as part of the DHCP process. This value is the IP address of the NetBIOS overTCP/IP name server to be used by the client.')
ctDhcpClientStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1), )
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setDescription('This table contains an entry for each DHCP client. The table is indexed by ctDhcpClientStatsID, which indicates an arbitrary order of entries.')
ctDhcpClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpClientStatsID"))
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setDescription('A description of a single client, which could be on any of the subnets being served by participating interfaces.')
ctDhcpClientStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientStatsID.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsID.setDescription('A unique value identifying an element in a sequence of active clients which have been given network addresses by this DHCP server.')
ctDhcpClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientName.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientName.setDescription('This is the name of the client as listed by the client in a DHCP request packet.')
ctDhcpClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientIP.setDescription('This is the assigned IP address of the client during this active connection.')
ctDhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientID.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientID.setDescription("This is the ID of the client as listed by the client in a DHCP request packet. It is normally the client's Ethernet MAC address.")
ctDhcpEndOfLease = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpEndOfLease.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpEndOfLease.setDescription('This value is the time at which the lease of the IP address will expire. The units are seconds and the value is relative to the same starting point as ctDhcpIfServerTime.')
mibBuilder.exportSymbols("CTRON-DHCP-MIB", ctDhcpClientID=ctDhcpClientID, ctDhcpIfDefaultGateway=ctDhcpIfDefaultGateway, ctDhcpReleases=ctDhcpReleases, ctDhcpOffers=ctDhcpOffers, ctDhcpAcks=ctDhcpAcks, ctDhcpServerIfTable=ctDhcpServerIfTable, ctDhcpRequests=ctDhcpRequests, ctDhcpOtherServers=ctDhcpOtherServers, ctDhcpServerIfEntry=ctDhcpServerIfEntry, ctDhcpServerTime=ctDhcpServerTime, ctDhcpIfAddressesFree=ctDhcpIfAddressesFree, ctDhcpIfDomainNameServer=ctDhcpIfDomainNameServer, ctDhcpIfAddressesUsed=ctDhcpIfAddressesUsed, ctDhcpClientStatsEntry=ctDhcpClientStatsEntry, ctDhcpClientIP=ctDhcpClientIP, ctDhcp=ctDhcp, ctDhcpIfSubnetMask=ctDhcpIfSubnetMask, ctDhcpIfHighestAddress=ctDhcpIfHighestAddress, ctDhcpIfWINServer=ctDhcpIfWINServer, ctDhcpIfDomainName=ctDhcpIfDomainName, ctDhcpNoOfActiveClients=ctDhcpNoOfActiveClients, ctDhcpReclaimIP=ctDhcpReclaimIP, ctDhcpDeclines=ctDhcpDeclines, ctDhcpClientStatsTable=ctDhcpClientStatsTable, ctDhcpInterfaceConfig=ctDhcpInterfaceConfig, ctDhcpIfIndex=ctDhcpIfIndex, ctDhcpIfNetworkAddress=ctDhcpIfNetworkAddress, ctDhcpNaks=ctDhcpNaks, ctDhcpServerStats=ctDhcpServerStats, ctDhcpAdminStatus=ctDhcpAdminStatus, ctDhcpIfAdminStatus=ctDhcpIfAdminStatus, ctDhcpClientStatsID=ctDhcpClientStatsID, ctDhcpIfLeasePeriod=ctDhcpIfLeasePeriod, ctDhcpClientName=ctDhcpClientName, ctDhcpEndOfLease=ctDhcpEndOfLease, ctDhcpIfLowestaddress=ctDhcpIfLowestaddress, ctDhcpIfOperStatus=ctDhcpIfOperStatus, ctDhcpDiscovers=ctDhcpDiscovers, ctDhcpClientStatusTable=ctDhcpClientStatusTable, ctDhcpProtocolErrors=ctDhcpProtocolErrors, ctDhcpOperStatus=ctDhcpOperStatus, ctDhcpIfServerAddress=ctDhcpIfServerAddress)
