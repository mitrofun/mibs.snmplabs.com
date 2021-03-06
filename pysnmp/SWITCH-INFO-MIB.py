#
# PySNMP MIB module SWITCH-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWITCH-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:05:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, Gauge32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, NotificationType, MibIdentifier, Counter64, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Gauge32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "NotificationType", "MibIdentifier", "Counter64", "Bits", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
switchVendor, = mibBuilder.importSymbols("TELESYN-ATI-TC", "switchVendor")
switchVendorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1))
switchVendorMib.setRevisions(('1997-05-16 22:00', '1996-11-05 22:00',))
if mibBuilder.loadTexts: switchVendorMib.setLastUpdated('9611052200Z')
if mibBuilder.loadTexts: switchVendorMib.setOrganization('')
vendorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1))
vendorName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
vendorProductName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorProductName.setStatus('current')
vendorModelName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorModelName.setStatus('current')
vendorModelId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorModelId.setStatus('current')
vendorCopyright = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorCopyright.setStatus('current')
mibBuilder.exportSymbols("SWITCH-INFO-MIB", vendorName=vendorName, vendorInfo=vendorInfo, vendorProductName=vendorProductName, switchVendorMib=switchVendorMib, vendorModelName=vendorModelName, vendorModelId=vendorModelId, vendorCopyright=vendorCopyright, PYSNMP_MODULE_ID=switchVendorMib)
