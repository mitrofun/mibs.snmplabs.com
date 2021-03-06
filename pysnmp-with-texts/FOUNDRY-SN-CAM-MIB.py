#
# PySNMP MIB module FOUNDRY-SN-CAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-CAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
platform, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "platform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Unsigned32, Bits, NotificationType, Integer32, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Bits", "NotificationType", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snCamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1))
snCamMIB.setRevisions(('2010-06-02 00:00', '2007-11-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snCamMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Initial revision',))
if mibBuilder.loadTexts: snCamMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snCamMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snCamMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snCamMIB.setDescription("The MIB module to describe generic objects for the usage of Content Addressable Memory (CAM). Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
class Percent(TextualConvention, Gauge32):
    description = 'An integer that is in the range of a percent value.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

snCamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1))
snCamProfile = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("default", 1), ("ipv4", 2), ("ipv4Ipv6", 3), ("ipv4Ipv62", 4), ("ipv4Vpls", 5), ("ipv4Vpn", 6), ("ipv6", 7), ("l2Metro", 8), ("l2Metro2", 9), ("mplsL3vpn", 10), ("mplsL3vpn2", 11), ("mplsVpls", 12), ("mplsVpls2", 13), ("mplsVpnVpls", 14), ("multiService", 15), ("multiService2", 16), ("multiService3", 17), ("multiService4", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamProfile.setStatus('current')
if mibBuilder.loadTexts: snCamProfile.setDescription('This object identifies CAM partition profile. Each profile adjusts the partitions to optimize the device for corresponding applications.')
snCamUsage = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2))
snCamUsageL3Table = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1), )
if mibBuilder.loadTexts: snCamUsageL3Table.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Table.setDescription("A list of snCamUsageL3 entries. This table contains information of the entity's CAM usage for layer 3 traffic.")
snCamUsageL3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Slot"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Processor"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Type"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Supernet"))
if mibBuilder.loadTexts: snCamUsageL3Entry.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Entry.setDescription('An entry containing management information applicable to CAM usage for layer 3 traffic')
snCamUsageL3Slot = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: snCamUsageL3Slot.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Slot.setDescription('A number which uniquely identifies a linecard in the device')
snCamUsageL3Processor = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: snCamUsageL3Processor.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Processor.setDescription('A number which uniquely identifies the network processor within a linecard in the device')
snCamUsageL3Type = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("ipv4vpn", 3), ("ipv6vpn", 4))))
if mibBuilder.loadTexts: snCamUsageL3Type.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Type.setDescription('This object identifies the type of layer 3 traffic passing through the network processor.')
snCamUsageL3Supernet = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 4), Unsigned32())
if mibBuilder.loadTexts: snCamUsageL3Supernet.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Supernet.setDescription('This object identifies the Supernet for the layer 3 type traffic. It provides information for longest match lookup. For example, zero indicates all the bits of IP address will be matched, and one indicates all but the lowest bit in IP address will be matched. The range is [0..32] for IPv4 and IPv4VPN, where a value of 32 indicates the entry is the total of other supernets indexed by [0..31]. The range is [0..10] for IPv6, where a value of 10 indicates the entry is the total of other supernets indexed by [0..9].')
snCamUsageL3Size = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 5), Unsigned32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL3Size.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Size.setDescription('The effective CAM size for this layer 3 traffic entry. For ipv4 traffic, each unit is 4 bytes. For ipv4vpn, each unit is 8 bytes. For ipv6, each unit is 16 bytes.')
snCamUsageL3Free = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 6), Gauge32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL3Free.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3Free.setDescription('The amount of CAM currently available for this layer 3 traffic entry. For ipv4 traffic, each unit is 4 bytes. For ipv4vpn, each unit is 8 bytes. For ipv6, each unit is 16 bytes.')
snCamUsageL3UsedPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 7), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL3UsedPercent.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL3UsedPercent.setDescription('The percentage of CAM currently being used for this layer 3 traffic entry. ')
snCamUsageL2Table = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2), )
if mibBuilder.loadTexts: snCamUsageL2Table.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Table.setDescription("A list of snCamUsageL2 entries. This table contains information of the entity's CAM usage for layer 2 traffic.")
snCamUsageL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Slot"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Processor"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Type"))
if mibBuilder.loadTexts: snCamUsageL2Entry.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Entry.setDescription('An entry containing management information applicable to CAM usage for layer 2 traffic')
snCamUsageL2Slot = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: snCamUsageL2Slot.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Slot.setDescription('A number which uniquely identifies a linecard in the device')
snCamUsageL2Processor = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: snCamUsageL2Processor.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Processor.setDescription('A number which uniquely identifies the network processor within a linecard in the device')
snCamUsageL2Type = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("forwarding", 1), ("protocol", 2), ("flooding", 3), ("total", 4))))
if mibBuilder.loadTexts: snCamUsageL2Type.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Type.setDescription('This object identifies the type of layer 2 traffic passing through the network processor.')
snCamUsageL2Size = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 4), Unsigned32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL2Size.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Size.setDescription('The effective CAM size for this layer 2 traffic entry. Each unit is 8 bytes.')
snCamUsageL2Free = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 5), Gauge32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL2Free.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2Free.setDescription('The amount of CAM currently available for this layer 2 traffic entry. Each unit is 8 bytes.')
snCamUsageL2UsedPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 6), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageL2UsedPercent.setStatus('current')
if mibBuilder.loadTexts: snCamUsageL2UsedPercent.setDescription('The percentage of CAM currently being used for this layer 2 traffic entry. ')
snCamUsageSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3), )
if mibBuilder.loadTexts: snCamUsageSessionTable.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionTable.setDescription("A list of snCamUsageSession entries. This table contains information of the entitiy's CAM usage for sessions. ")
snCamUsageSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionSlot"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionProcessor"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionType"))
if mibBuilder.loadTexts: snCamUsageSessionEntry.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionEntry.setDescription('An entry containing management information applicable to CAM usage for sessions. ')
snCamUsageSessionSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: snCamUsageSessionSlot.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionSlot.setDescription('A number which uniquely identifies a linecard in the device')
snCamUsageSessionProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: snCamUsageSessionProcessor.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionProcessor.setDescription('A number which uniquely identifies the network processor within a linecard in the device')
snCamUsageSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ipv4Multicast", 1), ("ipv4andMacReceiveAcl", 2), ("ipv4andMacRuleAcl", 3), ("ipv4andMacTotal", 4), ("ipv4andMacOut", 5), ("ipv6Multicast", 6), ("ipv6ReceiveAcl", 7), ("ipv6RuleAcl", 8), ("ipv6Total", 9), ("ipv6Out", 10), ("labelOut", 11), ("ipv4SrcGuardDenial", 12), ("ipv4SrcGuardPermit", 13), ("internalForwardingLookup", 14))))
if mibBuilder.loadTexts: snCamUsageSessionType.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionType.setDescription('This object identifies the type of sessions.')
snCamUsageSessionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 4), Unsigned32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageSessionSize.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionSize.setDescription('The effective CAM size for this session traffic entry. For IPv4 sessions, each unit is 16 bytes. For IPv4 sessions, each unit is 64 bytes.')
snCamUsageSessionFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 5), Gauge32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageSessionFree.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionFree.setDescription('The amount of CAM currently available this session traffic entry. For IPv4 sessions, each unit is 16 bytes. For IPv4 sessions, each unit is 64 bytes.')
snCamUsageSessionUsedPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 6), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageSessionUsedPercent.setStatus('current')
if mibBuilder.loadTexts: snCamUsageSessionUsedPercent.setDescription('The percentage of CAM currently being used by this session traffic entry ')
snCamUsageOtherTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4), )
if mibBuilder.loadTexts: snCamUsageOtherTable.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherTable.setDescription("A list of snCamUsageOther entries. This table contains information of the entitiy's CAM usage for types other than L3, L2, or Session.")
snCamUsageOtherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherSlot"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherProcessor"), (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherType"))
if mibBuilder.loadTexts: snCamUsageOtherEntry.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherEntry.setDescription('An entry containing management information applicable to CAM usage for types other than L3, L2, or Session')
snCamUsageOtherSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: snCamUsageOtherSlot.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherSlot.setDescription('A number which uniquely identifies a linecard in the device')
snCamUsageOtherProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: snCamUsageOtherProcessor.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherProcessor.setDescription('A number which uniquely identifies the network processor within a linecard in the device')
snCamUsageOtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gre", 1), ("multicastVpls", 2))))
if mibBuilder.loadTexts: snCamUsageOtherType.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherType.setDescription('This object identifies the type.')
snCamUsageOtherSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 4), Unsigned32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageOtherSize.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherSize.setDescription('The effective CAM size for this Other traffic entry. For GRE, each unit is 8 bytes. For multicast VPLS, each unit is 16 bytes.')
snCamUsageOtherFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 5), Gauge32()).setUnits('Entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageOtherFree.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherFree.setDescription('The amount of CAM currently available this Other traffic entry. For GRE, each unit is 8 bytes. For multicast VPLS, each unit is 16 bytes.')
snCamUsageOtherUsedPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 6), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snCamUsageOtherUsedPercent.setStatus('current')
if mibBuilder.loadTexts: snCamUsageOtherUsedPercent.setDescription('The percentage of CAM currently being used by this entry ')
mibBuilder.exportSymbols("FOUNDRY-SN-CAM-MIB", snCamUsageOtherSlot=snCamUsageOtherSlot, Percent=Percent, snCamUsageL3Size=snCamUsageL3Size, snCamUsageSessionTable=snCamUsageSessionTable, snCamUsageOtherType=snCamUsageOtherType, snCamUsageSessionType=snCamUsageSessionType, snCamUsageL3Entry=snCamUsageL3Entry, snCamUsageOtherTable=snCamUsageOtherTable, snCamUsageOtherEntry=snCamUsageOtherEntry, snCamUsageL2Slot=snCamUsageL2Slot, snCamUsageL2Free=snCamUsageL2Free, snCamUsageSessionProcessor=snCamUsageSessionProcessor, snCamUsageL2Table=snCamUsageL2Table, snCamUsageL2Size=snCamUsageL2Size, snCamUsageSessionFree=snCamUsageSessionFree, snCamObjects=snCamObjects, snCamUsageOtherSize=snCamUsageOtherSize, snCamUsageOtherProcessor=snCamUsageOtherProcessor, snCamUsageL2Entry=snCamUsageL2Entry, snCamUsageL2Processor=snCamUsageL2Processor, snCamUsageSessionSize=snCamUsageSessionSize, snCamUsageL3Processor=snCamUsageL3Processor, snCamUsageL3Slot=snCamUsageL3Slot, snCamMIB=snCamMIB, PYSNMP_MODULE_ID=snCamMIB, snCamUsageSessionUsedPercent=snCamUsageSessionUsedPercent, snCamUsageOtherUsedPercent=snCamUsageOtherUsedPercent, snCamUsageOtherFree=snCamUsageOtherFree, snCamUsageL3Table=snCamUsageL3Table, snCamUsageL3Free=snCamUsageL3Free, snCamProfile=snCamProfile, snCamUsageSessionSlot=snCamUsageSessionSlot, snCamUsageL3UsedPercent=snCamUsageL3UsedPercent, snCamUsageL2Type=snCamUsageL2Type, snCamUsageSessionEntry=snCamUsageSessionEntry, snCamUsageL3Supernet=snCamUsageL3Supernet, snCamUsageL3Type=snCamUsageL3Type, snCamUsage=snCamUsage, snCamUsageL2UsedPercent=snCamUsageL2UsedPercent)
