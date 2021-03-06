#
# PySNMP MIB module PCEDP-PCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCEDP-PCC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Bits, TimeTicks, ModuleIdentity, Integer32, Unsigned32, Counter32, Gauge32, experimental, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Bits", "TimeTicks", "ModuleIdentity", "Integer32", "Unsigned32", "Counter32", "Gauge32", "experimental", "MibIdentifier", "Counter64", "IpAddress")
TextualConvention, DisplayString, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "RowStatus")
pcedpPccMIB = ModuleIdentity((1, 3, 6, 1, 3, 10000))
if mibBuilder.loadTexts: pcedpPccMIB.setLastUpdated('200606150000Z')
if mibBuilder.loadTexts: pcedpPccMIB.setOrganization('PCE Working Group')
if mibBuilder.loadTexts: pcedpPccMIB.setContactInfo('WG-email: pce@ietf.org WG-URL: http://www.ietf.org/html.charters/pce-charter.html TODO: This section has to be completed with chairs and authors addresses ')
if mibBuilder.loadTexts: pcedpPccMIB.setDescription('This MIB module defines a collection of objects for managing Path Computation Elements (PCEs) Discovery Protocol inside a Path Computation Client (PCC) application.')
pcedpPccNotifications = MibIdentifier((1, 3, 6, 1, 3, 10000, 0))
pcedpPccMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1))
pcedpPccDiscoveryGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 1))
pcedpPccPceDiscoveryAdminStatus = MibScalar((1, 3, 6, 1, 3, 10000, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcedpPccPceDiscoveryAdminStatus.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceDiscoveryAdminStatus.setDescription('Setting this object to disabled(2) disables the discovery of PCEs. Once disabled, The discovery must be explicitly enabled to restore discovery of PCEs. Setting this object to enabled(1) enables the discovery of PCEs.')
pcedpPccPceDiscoveryTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 1, 2), )
if mibBuilder.loadTexts: pcedpPccPceDiscoveryTable.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceDiscoveryTable.setDescription('Information describing the PCEs discovered by the PCC.')
pcedpPccPceDiscoveryEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1), ).setIndexNames((0, "PCEDP-PCC-MIB", "pcedpPccPceIndex"))
if mibBuilder.loadTexts: pcedpPccPceDiscoveryEntry.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceDiscoveryEntry.setDescription('Information describing the general information of each PCE discovered by the PCC.')
pcedpPccPceIndex = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pcedpPccPceIndex.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceIndex.setDescription('This object identifies locally the PCE for which this entry contains information.')
pcedpPccPceIPv4Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceIPv4Address.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceIPv4Address.setDescription('The IP address to be used to reach the PCE. A value of 0.0.0.0 indicates the absence of this address.')
pcedpPccPceIPv6Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 3), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceIPv6Address.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceIPv6Address.setDescription('The IP address to be used to reach the PCE. A value of ::0 indicates the absence of this address.')
pcedpPccPceTimeDiscovered = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceTimeDiscovered.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceTimeDiscovered.setDescription('The value of sysUpTime at the time this entry was created. Static entry: the value of sysUpTime at the time PCC restarted.')
pcedpPccPceLastUpdated = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceLastUpdated.setStatus('current')
if mibBuilder.loadTexts: pcedpPccPceLastUpdated.setDescription('The value of sysUpTime at the time this entry was last updated. Static entry: if the entry values keep unchanged since the re- initialization of the PCC then this object contains a zero value.')
pcedpPccPcesCapabilityGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 2))
pcedpPccPcesActivityGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 3))
pcedpPccConformance = MibIdentifier((1, 3, 6, 1, 3, 10000, 2))
pcedpPccGroups = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 1))
pcedpPccCompliances = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 2))
pcedpPccGeneralPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcedpPccGeneralPceInformation = pcedpPccGeneralPceInformation.setStatus('current')
if mibBuilder.loadTexts: pcedpPccGeneralPceInformation.setDescription('The compliance statement for SNMP entities that monitors only general information as proposed in the 2nd S. of the section 6.1 of [I-D.ietf-pce-discovery-reqs].')
pcedpPccDetailledPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 2)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcedpPccDetailledPceInformation = pcedpPccDetailledPceInformation.setStatus('current')
if mibBuilder.loadTexts: pcedpPccDetailledPceInformation.setDescription('The compliance statement for SNMP entities that implement detailled monitoring as proposed in the 3rd S. of the section 6.1 of [I-D.ietf-pce-discovery-reqs].')
mibBuilder.exportSymbols("PCEDP-PCC-MIB", pcedpPccPceIPv4Address=pcedpPccPceIPv4Address, pcedpPccConformance=pcedpPccConformance, PYSNMP_MODULE_ID=pcedpPccMIB, pcedpPccPceTimeDiscovered=pcedpPccPceTimeDiscovered, pcedpPccCompliances=pcedpPccCompliances, pcedpPccPceIndex=pcedpPccPceIndex, pcedpPccGroups=pcedpPccGroups, pcedpPccMIBObjects=pcedpPccMIBObjects, pcedpPccPceDiscoveryEntry=pcedpPccPceDiscoveryEntry, pcedpPccGeneralPceInformation=pcedpPccGeneralPceInformation, pcedpPccPceDiscoveryAdminStatus=pcedpPccPceDiscoveryAdminStatus, pcedpPccPceIPv6Address=pcedpPccPceIPv6Address, pcedpPccNotifications=pcedpPccNotifications, pcedpPccPcesActivityGroup=pcedpPccPcesActivityGroup, pcedpPccDetailledPceInformation=pcedpPccDetailledPceInformation, pcedpPccDiscoveryGroup=pcedpPccDiscoveryGroup, pcedpPccMIB=pcedpPccMIB, pcedpPccPceLastUpdated=pcedpPccPceLastUpdated, pcedpPccPcesCapabilityGroup=pcedpPccPcesCapabilityGroup, pcedpPccPceDiscoveryTable=pcedpPccPceDiscoveryTable)
