#
# PySNMP MIB module TUBS-IBR-XEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-XEN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Counter64, Gauge32, ObjectIdentity, NotificationType, Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, IpAddress, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "IpAddress", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
xenMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 14))
xenMIB.setRevisions(('2006-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: xenMIB.setRevisionsDescriptions(('The initial revision of this module.',))
if mibBuilder.loadTexts: xenMIB.setLastUpdated('200602200000Z')
if mibBuilder.loadTexts: xenMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: xenMIB.setContactInfo('Frank Strauss, Oliver Wellnitz TU Braunschweig Muehlenpfordtstrasse 23 38106 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: {strauss,wellnitz}@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: xenMIB.setDescription('Experimental MIB module for Xen Virtual Hosting.')
xenObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1))
xenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 2))
xenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3))
class XenDomainState(TextualConvention, Integer32):
    description = 'This data type represents the state of a Xen domain. unknown(1): No known/defined state. running(2): The domain is running on any CPU. blocked(3): The domain is blocked, e.g., waiting for I/O. paused(4): The domain has been paused. crashed(5): The domain exepectedly crashed. dying(6): The domain is in the process of going down or dying to any other reason. shutdown(7): The domain has been shutdown. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("running", 2), ("blocked", 3), ("paused", 4), ("crashed", 5), ("dying", 6), ("shutdown", 7))

xenHost = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1))
xenHostXenVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostXenVersion.setStatus('current')
if mibBuilder.loadTexts: xenHostXenVersion.setDescription('The version string of the Xen version running on the physical host.')
xenHostTotalMemKBytes = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostTotalMemKBytes.setStatus('current')
if mibBuilder.loadTexts: xenHostTotalMemKBytes.setDescription('The total amount of available memory in Kbytes on the physical host.')
xenHostCPUs = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUs.setStatus('current')
if mibBuilder.loadTexts: xenHostCPUs.setDescription('The total number of CPUs on the physical host.')
xenHostCPUMHz = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUMHz.setStatus('current')
if mibBuilder.loadTexts: xenHostCPUMHz.setDescription('The CPU frequency in MHz of the CPUs on the physical host.')
xenDomainTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2), )
if mibBuilder.loadTexts: xenDomainTable.setStatus('current')
if mibBuilder.loadTexts: xenDomainTable.setDescription('A list of all Xen domains on the physical host.')
xenDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"))
if mibBuilder.loadTexts: xenDomainEntry.setStatus('current')
if mibBuilder.loadTexts: xenDomainEntry.setDescription('An entry describing a particular Xen domain.')
xenDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: xenDomainName.setStatus('current')
if mibBuilder.loadTexts: xenDomainName.setDescription('The name of the Xen domain.')
xenDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 2), XenDomainState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainState.setStatus('current')
if mibBuilder.loadTexts: xenDomainState.setDescription('The state of the Xen domain.')
xenDomainMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMemKBytes.setStatus('current')
if mibBuilder.loadTexts: xenDomainMemKBytes.setDescription('The amount of memory in Kbytes currently occupied by the Xen domain.')
xenDomainMaxMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMaxMemKBytes.setStatus('current')
if mibBuilder.loadTexts: xenDomainMaxMemKBytes.setDescription('The total amount of memory in Kbytes assigned to the Xen domain. A value of zero denotes that there is no limit.')
xenVCPUTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3), )
if mibBuilder.loadTexts: xenVCPUTable.setStatus('current')
if mibBuilder.loadTexts: xenVCPUTable.setDescription('A list of all VCPUs per Xen domain.')
xenVCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenVCPUIndex"))
if mibBuilder.loadTexts: xenVCPUEntry.setStatus('current')
if mibBuilder.loadTexts: xenVCPUEntry.setDescription('An entry describing a VCPU of a Xen domain.')
xenVCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: xenVCPUIndex.setStatus('current')
if mibBuilder.loadTexts: xenVCPUIndex.setDescription('The index of the VCPU.')
xenVCPUMilliseconds = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenVCPUMilliseconds.setStatus('current')
if mibBuilder.loadTexts: xenVCPUMilliseconds.setDescription('The number milliseconds consumed by the VCPU since the Xen domain has been set up.')
xenNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4), )
if mibBuilder.loadTexts: xenNetworkTable.setStatus('current')
if mibBuilder.loadTexts: xenNetworkTable.setDescription('A list of all networks per Xen domain.')
xenNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1), ).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenNetworkIndex"))
if mibBuilder.loadTexts: xenNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: xenNetworkEntry.setDescription('An entry describing a network of a Xen domain.')
xenNetworkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: xenNetworkIndex.setStatus('current')
if mibBuilder.loadTexts: xenNetworkIndex.setDescription('The index of the network.')
xenNetworkInKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInKBytes.setStatus('current')
if mibBuilder.loadTexts: xenNetworkInKBytes.setDescription('The number of Kbytes received on the network interface since the Xen domain has been set up.')
xenNetworkInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInPkts.setStatus('current')
if mibBuilder.loadTexts: xenNetworkInPkts.setDescription('The number of packets received on the network interface since the Xen domain has been set up.')
xenNetworkInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInErrors.setStatus('current')
if mibBuilder.loadTexts: xenNetworkInErrors.setDescription('The number of erroneous packets received on the network interface since the Xen domain has been set up.')
xenNetworkInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInDiscards.setStatus('current')
if mibBuilder.loadTexts: xenNetworkInDiscards.setDescription('The number of dropped packets received on the network interface since the Xen domain has been set up.')
xenNetworkOutKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutKBytes.setStatus('current')
if mibBuilder.loadTexts: xenNetworkOutKBytes.setDescription('The number of Kbytes sent on the network interface since the Xen domain has been set up.')
xenNetworkOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutPkts.setStatus('current')
if mibBuilder.loadTexts: xenNetworkOutPkts.setDescription('The number of packets sent on the network interface since the Xen domain has been set up.')
xenNetworkOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutErrors.setStatus('current')
if mibBuilder.loadTexts: xenNetworkOutErrors.setDescription('The number of packets that could not be sent on the network interface because of any errors since the Xen domain has been set up.')
xenNetworkOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutDiscards.setStatus('current')
if mibBuilder.loadTexts: xenNetworkOutDiscards.setDescription('The number of packets that have not been sent on the network interface even though no errors had been detected since the Xen domain has been set up.')
xenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1))
xenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2))
xenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1, 1)).setObjects(("TUBS-IBR-XEN-MIB", "xenGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xenCompliance = xenCompliance.setStatus('current')
if mibBuilder.loadTexts: xenCompliance.setDescription('The compliance statement for an SNMP entity which implements the Xen MIB.')
xenGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2, 1)).setObjects(("TUBS-IBR-XEN-MIB", "xenHostXenVersion"), ("TUBS-IBR-XEN-MIB", "xenHostTotalMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenHostCPUs"), ("TUBS-IBR-XEN-MIB", "xenHostCPUMHz"), ("TUBS-IBR-XEN-MIB", "xenDomainState"), ("TUBS-IBR-XEN-MIB", "xenDomainMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenDomainMaxMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenVCPUMilliseconds"), ("TUBS-IBR-XEN-MIB", "xenNetworkInKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkInPkts"), ("TUBS-IBR-XEN-MIB", "xenNetworkInErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkInDiscards"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutPkts"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xenGeneralGroup = xenGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: xenGeneralGroup.setDescription('A collection of all Xen MIB objects.')
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", xenDomainTable=xenDomainTable, PYSNMP_MODULE_ID=xenMIB, xenDomainMemKBytes=xenDomainMemKBytes, xenNetworkInPkts=xenNetworkInPkts, xenCompliances=xenCompliances, xenHostCPUs=xenHostCPUs, xenGroups=xenGroups, xenHostXenVersion=xenHostXenVersion, xenNetworkOutKBytes=xenNetworkOutKBytes, xenNetworkIndex=xenNetworkIndex, xenNetworkInKBytes=xenNetworkInKBytes, xenVCPUEntry=xenVCPUEntry, xenDomainMaxMemKBytes=xenDomainMaxMemKBytes, xenNetworkOutDiscards=xenNetworkOutDiscards, xenTraps=xenTraps, xenNetworkInDiscards=xenNetworkInDiscards, xenHost=xenHost, xenCompliance=xenCompliance, xenHostCPUMHz=xenHostCPUMHz, xenDomainName=xenDomainName, xenNetworkEntry=xenNetworkEntry, xenNetworkOutPkts=xenNetworkOutPkts, xenVCPUIndex=xenVCPUIndex, xenHostTotalMemKBytes=xenHostTotalMemKBytes, xenObjects=xenObjects, xenNetworkTable=xenNetworkTable, xenNetworkInErrors=xenNetworkInErrors, xenGeneralGroup=xenGeneralGroup, xenNetworkOutErrors=xenNetworkOutErrors, xenMIB=xenMIB, XenDomainState=XenDomainState, xenVCPUMilliseconds=xenVCPUMilliseconds, xenDomainState=xenDomainState, xenVCPUTable=xenVCPUTable, xenDomainEntry=xenDomainEntry, xenConformance=xenConformance)
