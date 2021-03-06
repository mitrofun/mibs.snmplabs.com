#
# PySNMP MIB module FOUNDRY-SN-ARP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-ARP-GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, Bits, iso, Gauge32, Integer32, TimeTicks, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Bits", "iso", "Gauge32", "Integer32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snArpInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22))
snArpInfo.setRevisions(('2010-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snArpInfo.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.',))
if mibBuilder.loadTexts: snArpInfo.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snArpInfo.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snArpInfo.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snArpInfo.setDescription("The Enterprise MIB for ARP support in SNMP. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snArpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1))
snArpStatsTotalReceived = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsTotalReceived.setStatus('current')
if mibBuilder.loadTexts: snArpStatsTotalReceived.setDescription('The total number of ARP packets received from interfaces, including those received in error.')
snArpStatsRequestReceived = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRequestReceived.setStatus('current')
if mibBuilder.loadTexts: snArpStatsRequestReceived.setDescription('The total number of input ARP Request packets received from interfaces.')
snArpStatsRequestSent = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRequestSent.setStatus('current')
if mibBuilder.loadTexts: snArpStatsRequestSent.setDescription('The total number of output ARP Request packets sent from interfaces.')
snArpStatsRepliesSent = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsRepliesSent.setStatus('current')
if mibBuilder.loadTexts: snArpStatsRepliesSent.setDescription('The total number of output ARP Reply packets sent from interfaces.')
snArpStatsPendingDrop = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsPendingDrop.setStatus('current')
if mibBuilder.loadTexts: snArpStatsPendingDrop.setDescription('The total number of ARP pending packets discarded.')
snArpStatsInvalidSource = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsInvalidSource.setStatus('current')
if mibBuilder.loadTexts: snArpStatsInvalidSource.setDescription('The total number of ARP packets received with invalid sender protocol address.')
snArpStatsInvalidDestination = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snArpStatsInvalidDestination.setStatus('current')
if mibBuilder.loadTexts: snArpStatsInvalidDestination.setDescription('The total number of ARP packets received with invalid destination protocol address.')
mibBuilder.exportSymbols("FOUNDRY-SN-ARP-GROUP-MIB", snArpInfo=snArpInfo, snArpStatsRequestSent=snArpStatsRequestSent, snArpStatsInvalidDestination=snArpStatsInvalidDestination, PYSNMP_MODULE_ID=snArpInfo, snArpStatsTotalReceived=snArpStatsTotalReceived, snArpStatsRequestReceived=snArpStatsRequestReceived, snArpStatsInvalidSource=snArpStatsInvalidSource, snArpStatsPendingDrop=snArpStatsPendingDrop, snArpStatsRepliesSent=snArpStatsRepliesSent, snArpStats=snArpStats)
