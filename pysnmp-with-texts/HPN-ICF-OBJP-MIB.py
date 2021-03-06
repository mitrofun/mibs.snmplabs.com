#
# PySNMP MIB module HPN-ICF-OBJP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-OBJP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, TimeTicks, Gauge32, Unsigned32, Integer32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfObjp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155))
hpnicfObjp.setRevisions(('2014-03-10 15:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfObjp.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfObjp.setLastUpdated('201403101536Z')
if mibBuilder.loadTexts: hpnicfObjp.setOrganization('')
if mibBuilder.loadTexts: hpnicfObjp.setContactInfo('')
if mibBuilder.loadTexts: hpnicfObjp.setDescription('Object-policy management information base for managing devices that support object policy. ')
hpnicfObjpZonePairObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1))
hpnicfObjpZonePairRunningInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1), )
if mibBuilder.loadTexts: hpnicfObjpZonePairRunningInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairRunningInfoTable.setDescription('Object policy of zone pair running information base.')
hpnicfObjpZonePairRunningInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairSrcZone"), (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairDstZone"), (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairIPVersion"), (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairRuleID"))
if mibBuilder.loadTexts: hpnicfObjpZonePairRunningInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairRunningInfoEntry.setDescription('Object policy of zone pair running information entry.')
hpnicfObjpZonePairSrcZone = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hpnicfObjpZonePairSrcZone.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairSrcZone.setDescription('Name of the source security zone.')
hpnicfObjpZonePairDstZone = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hpnicfObjpZonePairDstZone.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairDstZone.setDescription('Name of the destination security zone.')
hpnicfObjpZonePairIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: hpnicfObjpZonePairIPVersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairIPVersion.setDescription('IP protocol version.')
hpnicfObjpZonePairRuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hpnicfObjpZonePairRuleID.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairRuleID.setDescription('Rule ID of object policy.')
hpnicfObjpZonePairMatchPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfObjpZonePairMatchPacketCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairMatchPacketCount.setDescription('Number of packets matching the rule.')
hpnicfObjpZonePairLastMatchTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfObjpZonePairLastMatchTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjpZonePairLastMatchTime.setDescription('Interval in seconds between the last match and 1970/1/1 00:00:00.')
mibBuilder.exportSymbols("HPN-ICF-OBJP-MIB", PYSNMP_MODULE_ID=hpnicfObjp, hpnicfObjpZonePairMatchPacketCount=hpnicfObjpZonePairMatchPacketCount, hpnicfObjpZonePairRunningInfoEntry=hpnicfObjpZonePairRunningInfoEntry, hpnicfObjpZonePairDstZone=hpnicfObjpZonePairDstZone, hpnicfObjpZonePairRuleID=hpnicfObjpZonePairRuleID, hpnicfObjp=hpnicfObjp, hpnicfObjpZonePairObjects=hpnicfObjpZonePairObjects, hpnicfObjpZonePairSrcZone=hpnicfObjpZonePairSrcZone, hpnicfObjpZonePairLastMatchTime=hpnicfObjpZonePairLastMatchTime, hpnicfObjpZonePairRunningInfoTable=hpnicfObjpZonePairRunningInfoTable, hpnicfObjpZonePairIPVersion=hpnicfObjpZonePairIPVersion)
