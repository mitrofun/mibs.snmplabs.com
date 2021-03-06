#
# PySNMP MIB module HPICF-TR069-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-TR069-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Gauge32, IpAddress, Integer32, MibIdentifier, ModuleIdentity, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "IpAddress", "Integer32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "TimeTicks", "iso")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
hpicfTR069MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98))
hpicfTR069MIB.setRevisions(('2014-03-03 00:00',))
if mibBuilder.loadTexts: hpicfTR069MIB.setLastUpdated('201403030000Z')
if mibBuilder.loadTexts: hpicfTR069MIB.setOrganization('HP Networking')
hpicfTR069Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 0))
hpicfTR069Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1))
hpicfTR069Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2))
hpicfTR069EnableCWMP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069EnableCWMP.setStatus('current')
hpicfTR069CWMPDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("device", 1), ("gateway", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CWMPDeviceType.setStatus('current')
hpicfTR069AcsUrl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsUrl.setStatus('current')
hpicfTR069AcsUrlOrigin = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("config", 2), ("dhcp", 3), ("acs", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069AcsUrlOrigin.setStatus('current')
hpicfTR069AcsProxyUrl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsProxyUrl.setStatus('current')
hpicfTR069AcsUsername = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsUsername.setStatus('current')
hpicfTR069AcsPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsPassword.setStatus('current')
hpicfTR069AcsPasswordEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsPasswordEncrypted.setStatus('current')
hpicfTR069AcsConnectRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069AcsConnectRetryInterval.setStatus('current')
hpicfTR069CpeUsername = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpeUsername.setStatus('current')
hpicfTR069CpePassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpePassword.setStatus('current')
hpicfTR069CpePasswordEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpePasswordEncrypted.setStatus('current')
hpicfTR069CpeWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 13), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069CpeWaitTimeout.setStatus('current')
hpicfTR069PeriodicInformEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformEnable.setStatus('current')
hpicfTR069PeriodicInformInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformInterval.setStatus('current')
hpicfTR069PeriodicInformTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 16), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformTime.setStatus('current')
hpicfTR069MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1))
hpicfTR069MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2))
hpicfTR069MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1, 1)).setObjects(("HPICF-TR069-MIB", "hpicfTR069Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTR069MIBCompliance = hpicfTR069MIBCompliance.setStatus('current')
hpicfTR069Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2, 1)).setObjects(("HPICF-TR069-MIB", "hpicfTR069EnableCWMP"), ("HPICF-TR069-MIB", "hpicfTR069CWMPDeviceType"), ("HPICF-TR069-MIB", "hpicfTR069AcsUrl"), ("HPICF-TR069-MIB", "hpicfTR069AcsUrlOrigin"), ("HPICF-TR069-MIB", "hpicfTR069AcsProxyUrl"), ("HPICF-TR069-MIB", "hpicfTR069AcsUsername"), ("HPICF-TR069-MIB", "hpicfTR069AcsPassword"), ("HPICF-TR069-MIB", "hpicfTR069AcsPasswordEncrypted"), ("HPICF-TR069-MIB", "hpicfTR069AcsConnectRetryInterval"), ("HPICF-TR069-MIB", "hpicfTR069CpeUsername"), ("HPICF-TR069-MIB", "hpicfTR069CpePassword"), ("HPICF-TR069-MIB", "hpicfTR069CpePasswordEncrypted"), ("HPICF-TR069-MIB", "hpicfTR069CpeWaitTimeout"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformEnable"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformInterval"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTR069Group = hpicfTR069Group.setStatus('current')
mibBuilder.exportSymbols("HPICF-TR069-MIB", hpicfTR069Notifications=hpicfTR069Notifications, hpicfTR069AcsUsername=hpicfTR069AcsUsername, hpicfTR069AcsPasswordEncrypted=hpicfTR069AcsPasswordEncrypted, hpicfTR069Conformance=hpicfTR069Conformance, hpicfTR069Objects=hpicfTR069Objects, hpicfTR069PeriodicInformTime=hpicfTR069PeriodicInformTime, hpicfTR069AcsUrl=hpicfTR069AcsUrl, hpicfTR069MIBCompliance=hpicfTR069MIBCompliance, hpicfTR069AcsUrlOrigin=hpicfTR069AcsUrlOrigin, hpicfTR069CWMPDeviceType=hpicfTR069CWMPDeviceType, hpicfTR069PeriodicInformEnable=hpicfTR069PeriodicInformEnable, hpicfTR069AcsConnectRetryInterval=hpicfTR069AcsConnectRetryInterval, hpicfTR069MIB=hpicfTR069MIB, hpicfTR069PeriodicInformInterval=hpicfTR069PeriodicInformInterval, hpicfTR069Group=hpicfTR069Group, hpicfTR069CpePassword=hpicfTR069CpePassword, hpicfTR069EnableCWMP=hpicfTR069EnableCWMP, hpicfTR069CpePasswordEncrypted=hpicfTR069CpePasswordEncrypted, hpicfTR069MIBGroups=hpicfTR069MIBGroups, hpicfTR069AcsPassword=hpicfTR069AcsPassword, hpicfTR069AcsProxyUrl=hpicfTR069AcsProxyUrl, hpicfTR069CpeUsername=hpicfTR069CpeUsername, hpicfTR069MIBCompliances=hpicfTR069MIBCompliances, hpicfTR069CpeWaitTimeout=hpicfTR069CpeWaitTimeout, PYSNMP_MODULE_ID=hpicfTR069MIB)
