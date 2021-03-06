#
# PySNMP MIB module ALVARION-VSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-VSC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSID, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSID")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, IpAddress, iso, NotificationType, ModuleIdentity, Bits, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "NotificationType", "ModuleIdentity", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "TimeTicks", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
alvarionVscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22))
if mibBuilder.loadTexts: alvarionVscMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionVscMIB.setOrganization('Alvarion Ltd.')
alvarionVscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1))
coVscConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1))
coVscConfigTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1), )
if mibBuilder.loadTexts: coVscConfigTable.setStatus('current')
coVscConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-VSC-MIB", "coVscCfgIndex"))
if mibBuilder.loadTexts: coVscConfigEntry.setStatus('current')
coVscCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVscCfgIndex.setStatus('current')
coVscCfgFriendlyVscName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setStatus('current')
coVscCfgSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 3), AlvarionSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSSID.setStatus('current')
coVscCfgAccessControlled = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgAccessControlled.setStatus('current')
coVscCfgSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("ieee802dot1x", 2), ("wpa", 3), ("wpa2", 4), ("wpaAndWpa2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSecurity.setStatus('current')
coVscCfgEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("tkipAndAes", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgEncryption.setStatus('current')
coVscCfg8021xAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("psk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setStatus('current')
coVscCfgMACAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setStatus('current')
coVscCfgHTMLAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setStatus('current')
alvarionVscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2))
alvarionVscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1))
alvarionVscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2))
alvarionVscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1, 1)).setObjects(("ALVARION-VSC-MIB", "alvarionVscMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionVscMIBCompliance = alvarionVscMIBCompliance.setStatus('current')
alvarionVscMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2, 1)).setObjects(("ALVARION-VSC-MIB", "coVscCfgFriendlyVscName"), ("ALVARION-VSC-MIB", "coVscCfgSSID"), ("ALVARION-VSC-MIB", "coVscCfgAccessControlled"), ("ALVARION-VSC-MIB", "coVscCfgSecurity"), ("ALVARION-VSC-MIB", "coVscCfgEncryption"), ("ALVARION-VSC-MIB", "coVscCfg8021xAuthentication"), ("ALVARION-VSC-MIB", "coVscCfgMACAuthentication"), ("ALVARION-VSC-MIB", "coVscCfgHTMLAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionVscMIBGroup = alvarionVscMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-VSC-MIB", alvarionVscMIBGroups=alvarionVscMIBGroups, coVscCfg8021xAuthentication=coVscCfg8021xAuthentication, alvarionVscMIBCompliance=alvarionVscMIBCompliance, coVscCfgHTMLAuthentication=coVscCfgHTMLAuthentication, coVscConfigTable=coVscConfigTable, coVscConfigEntry=coVscConfigEntry, alvarionVscMIB=alvarionVscMIB, coVscCfgMACAuthentication=coVscCfgMACAuthentication, coVscCfgEncryption=coVscCfgEncryption, coVscCfgSecurity=coVscCfgSecurity, PYSNMP_MODULE_ID=alvarionVscMIB, coVscCfgAccessControlled=coVscCfgAccessControlled, coVscCfgFriendlyVscName=coVscCfgFriendlyVscName, coVscConfigGroup=coVscConfigGroup, alvarionVscMIBObjects=alvarionVscMIBObjects, coVscCfgIndex=coVscCfgIndex, coVscCfgSSID=coVscCfgSSID, alvarionVscMIBCompliances=alvarionVscMIBCompliances, alvarionVscMIBGroup=alvarionVscMIBGroup, alvarionVscMIBConformance=alvarionVscMIBConformance)
