#
# PySNMP MIB module LLDP-EXT-DOT1-PE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LLDP-EXT-DOT1-PE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:57:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifGeneralInformationGroup, = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup")
lldpXdot1StandAloneExtensions, = mibBuilder.importSymbols("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1StandAloneExtensions")
lldpV2RemLocalDestMACAddress, lldpV2RemLocalIfIndex, lldpV2RemTimeMark, lldpV2RemIndex, lldpV2LocPortIfIndex, lldpV2Extensions, lldpV2PortConfigEntry = mibBuilder.importSymbols("LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress", "lldpV2RemLocalIfIndex", "lldpV2RemTimeMark", "lldpV2RemIndex", "lldpV2LocPortIfIndex", "lldpV2Extensions", "lldpV2PortConfigEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, Integer32, Counter64, Counter32, IpAddress, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter64", "Counter32", "IpAddress", "Bits", "TimeTicks", "Gauge32")
DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
lldpXDot1PEExtensions = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2))
lldpXDot1PEExtensions.setRevisions(('2012-01-23 00:00',))
if mibBuilder.loadTexts: lldpXDot1PEExtensions.setLastUpdated('201201230000Z')
if mibBuilder.loadTexts: lldpXDot1PEExtensions.setOrganization('IEEE 802.1 Working Group')
lldpXdot1PeMIB = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1))
lldpXdot1PeObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1))
lldpXdot1PeConfig = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1))
lldpXdot1PeLocalData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2))
lldpXdot1PeRemoteData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3))
lldpXdot1PeConfigPortExtensionTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXdot1PeConfigPortExtensionTable.setStatus('current')
lldpXdot1PeConfigPortExtensionEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1, 1), )
lldpV2PortConfigEntry.registerAugmentions(("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeConfigPortExtensionEntry"))
lldpXdot1PeConfigPortExtensionEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1PeConfigPortExtensionEntry.setStatus('current')
lldpXdot1PeConfigPortExtensionTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1PeConfigPortExtensionTxEnable.setStatus('current')
lldpXdot1PeLocPortExtensionTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1), )
if mibBuilder.loadTexts: lldpXdot1PeLocPortExtensionTable.setStatus('current')
lldpXdot1PeLocPortExtensionEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: lldpXdot1PeLocPortExtensionEntry.setStatus('current')
lldpXdot1PeLocPECascadePortPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1PeLocPECascadePortPriority.setStatus('current')
lldpXdot1PeLocPEAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1PeLocPEAddress.setStatus('current')
lldpXdot1PeLocPECSPAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1PeLocPECSPAddress.setStatus('current')
lldpXdot1PeRemPortExtensionTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: lldpXdot1PeRemPortExtensionTable.setStatus('current')
lldpXdot1PeRemPortExtensionEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: lldpXdot1PeRemPortExtensionEntry.setStatus('current')
lldpXdot1PeRemPECascadePortPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1PeRemPECascadePortPriority.setStatus('current')
lldpXdot1PeRemPEAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1PeRemPEAddress.setStatus('current')
lldpXdot1PeRemPECSPAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1PeRemPECSPAddress.setStatus('current')
lldpXdot1PeConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2))
lldpXdot1PeCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 1))
lldpXdot1PeGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 2))
lldpXdot1PeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 1, 1)).setObjects(("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeGroup"), ("LLDP-EXT-DOT1-PE-MIB", "ifGeneralInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1PeCompliance = lldpXdot1PeCompliance.setStatus('current')
lldpXdot1PeGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 2, 1)).setObjects(("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeConfigPortExtensionTxEnable"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPECascadePortPriority"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPEAddress"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPECSPAddress"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPECascadePortPriority"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPEAddress"), ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPECSPAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1PeGroup = lldpXdot1PeGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-DOT1-PE-MIB", lldpXdot1PeGroup=lldpXdot1PeGroup, lldpXdot1PeLocalData=lldpXdot1PeLocalData, lldpXdot1PeLocPECSPAddress=lldpXdot1PeLocPECSPAddress, lldpXdot1PeLocPortExtensionTable=lldpXdot1PeLocPortExtensionTable, lldpXdot1PeLocPEAddress=lldpXdot1PeLocPEAddress, lldpXdot1PeGroups=lldpXdot1PeGroups, lldpXdot1PeRemPEAddress=lldpXdot1PeRemPEAddress, lldpXdot1PeCompliance=lldpXdot1PeCompliance, lldpXDot1PEExtensions=lldpXDot1PEExtensions, lldpXdot1PeRemPortExtensionTable=lldpXdot1PeRemPortExtensionTable, lldpXdot1PeObjects=lldpXdot1PeObjects, lldpXdot1PeRemPECascadePortPriority=lldpXdot1PeRemPECascadePortPriority, lldpXdot1PeRemPortExtensionEntry=lldpXdot1PeRemPortExtensionEntry, lldpXdot1PeConfigPortExtensionTxEnable=lldpXdot1PeConfigPortExtensionTxEnable, PYSNMP_MODULE_ID=lldpXDot1PEExtensions, lldpXdot1PeConfigPortExtensionEntry=lldpXdot1PeConfigPortExtensionEntry, lldpXdot1PeMIB=lldpXdot1PeMIB, lldpXdot1PeCompliances=lldpXdot1PeCompliances, lldpXdot1PeRemoteData=lldpXdot1PeRemoteData, lldpXdot1PeConfigPortExtensionTable=lldpXdot1PeConfigPortExtensionTable, lldpXdot1PeLocPECascadePortPriority=lldpXdot1PeLocPECascadePortPriority, lldpXdot1PeLocPortExtensionEntry=lldpXdot1PeLocPortExtensionEntry, lldpXdot1PeRemPECSPAddress=lldpXdot1PeRemPECSPAddress, lldpXdot1PeConformance=lldpXdot1PeConformance, lldpXdot1PeConfig=lldpXdot1PeConfig)
