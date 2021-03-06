#
# PySNMP MIB module Juniper-UNI-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-UNI-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, IpAddress, Counter64, Bits, NotificationType, Integer32, Unsigned32, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "IpAddress", "Counter64", "Bits", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniperUni = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874))
juniperUni.setRevisions(('2003-07-30 19:03', '2002-11-13 20:14', '2001-06-01 21:46', '2000-06-01 14:30', '2000-05-24 04:00', '1999-12-13 19:36', '1999-11-08 00:00',))
if mibBuilder.loadTexts: juniperUni.setLastUpdated('200307301903Z')
if mibBuilder.loadTexts: juniperUni.setOrganization('Juniper Networks, Inc.')
juniProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1))
juniperUniMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 2))
if mibBuilder.loadTexts: juniperUniMibs.setStatus('current')
usVoiceMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 1))
juniMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2))
juniperUniExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3))
if mibBuilder.loadTexts: juniperUniExperiment.setStatus('current')
usVoiceExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 1))
juniExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2))
juniperUniAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4))
if mibBuilder.loadTexts: juniperUniAdmin.setStatus('current')
usVoiceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 1))
juniAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2))
juniAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5))
if mibBuilder.loadTexts: juniAgentCapability.setStatus('current')
usVoiceAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 1))
juniAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2))
juniNetMgmtProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 6))
if mibBuilder.loadTexts: juniNetMgmtProducts.setStatus('current')
juniSdxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 6, 1))
mibBuilder.exportSymbols("Juniper-UNI-SMI", PYSNMP_MODULE_ID=juniperUni, juniProducts=juniProducts, juniNetMgmtProducts=juniNetMgmtProducts, usVoiceExperiment=usVoiceExperiment, juniperUni=juniperUni, juniperUniExperiment=juniperUniExperiment, usVoiceMibs=usVoiceMibs, juniAgentCapability=juniAgentCapability, juniExperiment=juniExperiment, juniAgents=juniAgents, juniMibs=juniMibs, juniSdxMibs=juniSdxMibs, juniAdmin=juniAdmin, usVoiceAdmin=usVoiceAdmin, usVoiceAgents=usVoiceAgents, juniperUniMibs=juniperUniMibs, juniperUniAdmin=juniperUniAdmin)
