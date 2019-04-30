#
# PySNMP MIB module CISCO-LWAPP-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
CLSecKeyFormat, = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLSecKeyFormat")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity, NotificationType, IpAddress, Bits, Gauge32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity", "NotificationType", "IpAddress", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier")
MacAddress, TimeInterval, DisplayString, TruthValue, RowStatus, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeInterval", "DisplayString", "TruthValue", "RowStatus", "TextualConvention", "StorageType")
ciscoLwappAAAMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 598))
ciscoLwappAAAMIB.setRevisions(('2010-07-25 00:00', '2006-11-21 00:00',))
if mibBuilder.loadTexts: ciscoLwappAAAMIB.setLastUpdated('201007250000Z')
if mibBuilder.loadTexts: ciscoLwappAAAMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappAAAMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 0))
ciscoLwappAAAMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 1))
ciscoLwappAAAMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 2))
claConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1))
claStatusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2))
claPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1), )
if mibBuilder.loadTexts: claPriorityTable.setStatus('current')
claPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AAA-MIB", "claPriorityAuth"))
if mibBuilder.loadTexts: claPriorityEntry.setStatus('current')
claPriorityAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local", 1), ("radius", 2), ("tacacsplus", 3))))
if mibBuilder.loadTexts: claPriorityAuth.setStatus('current')
claPriorityOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claPriorityOrder.setStatus('current')
claTacacsServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2), )
if mibBuilder.loadTexts: claTacacsServerTable.setStatus('current')
claTacacsServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerType"), (0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerPriority"))
if mibBuilder.loadTexts: claTacacsServerEntry.setStatus('current')
claTacacsServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authentication", 1), ("authorization", 2), ("accounting", 3))))
if mibBuilder.loadTexts: claTacacsServerType.setStatus('current')
claTacacsServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: claTacacsServerPriority.setStatus('current')
claTacacsServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerAddressType.setStatus('current')
claTacacsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerAddress.setStatus('current')
claTacacsServerPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 5), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerPortNum.setStatus('current')
claTacacsServerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerEnabled.setStatus('current')
claTacacsServerSecretType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 7), CLSecKeyFormat()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerSecretType.setStatus('current')
claTacacsServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerSecret.setStatus('current')
claTacacsServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerTimeout.setStatus('current')
claTacacsServerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 10), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerStorageType.setStatus('current')
claTacacsServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claTacacsServerRowStatus.setStatus('current')
claWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3), )
if mibBuilder.loadTexts: claWlanTable.setStatus('current')
claWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: claWlanEntry.setStatus('current')
claWlanAcctServerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claWlanAcctServerEnabled.setStatus('current')
claWlanAuthServerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claWlanAuthServerEnabled.setStatus('current')
claSaveUserData = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claSaveUserData.setStatus('current')
claWebRadiusAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pap", 1), ("chap", 2), ("md5-chap", 3))).clone('pap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claWebRadiusAuthentication.setStatus('current')
claRadiusFallbackMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("passive", 2), ("active", 3))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusFallbackMode.setStatus('current')
claRadiusFallbackUsername = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 12), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusFallbackUsername.setStatus('current')
claRadiusFallbackInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 13), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(180, 3600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusFallbackInterval.setStatus('current')
claRadiusAuthMacDelimiter = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noDelimiter", 1), ("colon", 2), ("hyphen", 3), ("singleHyphen", 4))).clone('hyphen')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusAuthMacDelimiter.setStatus('current')
claRadiusAcctMacDelimiter = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noDelimiter", 1), ("colon", 2), ("hyphen", 3), ("singleHyphen", 4))).clone('hyphen')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusAcctMacDelimiter.setStatus('current')
claAcceptMICertificate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claAcceptMICertificate.setStatus('current')
claAcceptLSCertificate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claAcceptLSCertificate.setStatus('current')
claAllowAuthorizeLscApAgainstAAA = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claAllowAuthorizeLscApAgainstAAA.setStatus('current')
claRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1), )
if mibBuilder.loadTexts: claRadiusServerTable.setStatus('current')
claRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AAA-MIB", "claRadiusReqId"))
if mibBuilder.loadTexts: claRadiusServerEntry.setStatus('current')
claRadiusReqId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: claRadiusReqId.setStatus('current')
claRadiusAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusAddressType.setStatus('current')
claRadiusAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusAddress.setStatus('current')
claRadiusPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusPortNum.setStatus('current')
claRadiusWlanIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusWlanIdx.setStatus('current')
claRadiusClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusClientMacAddress.setStatus('current')
claRadiusUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claRadiusUserName.setStatus('current')
claDBCurrentUsedEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claDBCurrentUsedEntries.setStatus('current')
claRadiusServerGlobalActivatedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusServerGlobalActivatedEnabled.setStatus('current')
claRadiusServerGlobalDeactivatedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusServerGlobalDeactivatedEnabled.setStatus('current')
claRadiusServerWlanActivatedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusServerWlanActivatedEnabled.setStatus('current')
claRadiusServerWlanDeactivatedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusServerWlanDeactivatedEnabled.setStatus('current')
claRadiusReqTimedOutEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claRadiusReqTimedOutEnabled.setStatus('current')
ciscoLwappAAARadiusServerGlobalActivated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 1)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
if mibBuilder.loadTexts: ciscoLwappAAARadiusServerGlobalActivated.setStatus('current')
ciscoLwappAAARadiusServerGlobalDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 2)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
if mibBuilder.loadTexts: ciscoLwappAAARadiusServerGlobalDeactivated.setStatus('current')
ciscoLwappAAARadiusServerWlanActivated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 3)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"), ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
if mibBuilder.loadTexts: ciscoLwappAAARadiusServerWlanActivated.setStatus('current')
ciscoLwappAAARadiusServerWlanDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 4)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"), ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
if mibBuilder.loadTexts: ciscoLwappAAARadiusServerWlanDeactivated.setStatus('current')
ciscoLwappAAARadiusReqTimedOut = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 5)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"), ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
if mibBuilder.loadTexts: ciscoLwappAAARadiusReqTimedOut.setStatus('current')
ciscoLwappAAAMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1))
ciscoLwappAAAMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2))
ciscoLwappAAAMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 1)).setObjects(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBNotifsGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBStatusObjsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBCompliance = ciscoLwappAAAMIBCompliance.setStatus('deprecated')
ciscoLwappAAAMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 2)).setObjects(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBSaveUserConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBRadiusConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBAPPolicyConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBWlanAuthAccServerConfigGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBNotifsGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBStatusObjsGroup"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBDBEntriesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBComplianceRev1 = ciscoLwappAAAMIBComplianceRev1.setStatus('current')
ciscoLwappAAAMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 1)).setObjects(("CISCO-LWAPP-AAA-MIB", "claPriorityOrder"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddressType"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddress"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerPortNum"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerEnabled"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecretType"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecret"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerTimeout"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerStorageType"), ("CISCO-LWAPP-AAA-MIB", "claTacacsServerRowStatus"), ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalActivatedEnabled"), ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalDeactivatedEnabled"), ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanActivatedEnabled"), ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanDeactivatedEnabled"), ("CISCO-LWAPP-AAA-MIB", "claRadiusReqTimedOutEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBConfigGroup = ciscoLwappAAAMIBConfigGroup.setStatus('current')
ciscoLwappAAAMIBSaveUserConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 2)).setObjects(("CISCO-LWAPP-AAA-MIB", "claSaveUserData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBSaveUserConfigGroup = ciscoLwappAAAMIBSaveUserConfigGroup.setStatus('current')
ciscoLwappAAAMIBNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 3)).setObjects(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalActivated"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalDeactivated"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanActivated"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanDeactivated"), ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusReqTimedOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBNotifsGroup = ciscoLwappAAAMIBNotifsGroup.setStatus('current')
ciscoLwappAAAMIBStatusObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 4)).setObjects(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"), ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"), ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"), ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBStatusObjsGroup = ciscoLwappAAAMIBStatusObjsGroup.setStatus('current')
ciscoLwappAAAMIBDBEntriesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 5)).setObjects(("CISCO-LWAPP-AAA-MIB", "claDBCurrentUsedEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBDBEntriesGroup = ciscoLwappAAAMIBDBEntriesGroup.setStatus('current')
ciscoLwappAAAMIBRadiusConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 6)).setObjects(("CISCO-LWAPP-AAA-MIB", "claWebRadiusAuthentication"), ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackMode"), ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackUsername"), ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackInterval"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthMacDelimiter"), ("CISCO-LWAPP-AAA-MIB", "claRadiusAcctMacDelimiter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBRadiusConfigGroup = ciscoLwappAAAMIBRadiusConfigGroup.setStatus('current')
ciscoLwappAAAMIBAPPolicyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 7)).setObjects(("CISCO-LWAPP-AAA-MIB", "claAcceptMICertificate"), ("CISCO-LWAPP-AAA-MIB", "claAcceptLSCertificate"), ("CISCO-LWAPP-AAA-MIB", "claAllowAuthorizeLscApAgainstAAA"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBAPPolicyConfigGroup = ciscoLwappAAAMIBAPPolicyConfigGroup.setStatus('current')
ciscoLwappAAAMIBWlanAuthAccServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 8)).setObjects(("CISCO-LWAPP-AAA-MIB", "claWlanAuthServerEnabled"), ("CISCO-LWAPP-AAA-MIB", "claWlanAcctServerEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappAAAMIBWlanAuthAccServerConfigGroup = ciscoLwappAAAMIBWlanAuthAccServerConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-AAA-MIB", claRadiusReqTimedOutEnabled=claRadiusReqTimedOutEnabled, ciscoLwappAAAMIBCompliances=ciscoLwappAAAMIBCompliances, claConfigObjects=claConfigObjects, claAllowAuthorizeLscApAgainstAAA=claAllowAuthorizeLscApAgainstAAA, claRadiusUserName=claRadiusUserName, ciscoLwappAAAMIBNotifs=ciscoLwappAAAMIBNotifs, ciscoLwappAAAMIBConform=ciscoLwappAAAMIBConform, claRadiusFallbackUsername=claRadiusFallbackUsername, claStatusObjects=claStatusObjects, claTacacsServerRowStatus=claTacacsServerRowStatus, claRadiusServerEntry=claRadiusServerEntry, claSaveUserData=claSaveUserData, claWebRadiusAuthentication=claWebRadiusAuthentication, claWlanEntry=claWlanEntry, claRadiusWlanIdx=claRadiusWlanIdx, ciscoLwappAAAMIBGroups=ciscoLwappAAAMIBGroups, ciscoLwappAAAMIBCompliance=ciscoLwappAAAMIBCompliance, claTacacsServerSecretType=claTacacsServerSecretType, claRadiusFallbackMode=claRadiusFallbackMode, claRadiusAuthMacDelimiter=claRadiusAuthMacDelimiter, claRadiusServerTable=claRadiusServerTable, ciscoLwappAAAMIBSaveUserConfigGroup=ciscoLwappAAAMIBSaveUserConfigGroup, ciscoLwappAAAMIBComplianceRev1=ciscoLwappAAAMIBComplianceRev1, ciscoLwappAAAMIBStatusObjsGroup=ciscoLwappAAAMIBStatusObjsGroup, claRadiusPortNum=claRadiusPortNum, claRadiusServerGlobalDeactivatedEnabled=claRadiusServerGlobalDeactivatedEnabled, claWlanTable=claWlanTable, PYSNMP_MODULE_ID=ciscoLwappAAAMIB, ciscoLwappAAAMIB=ciscoLwappAAAMIB, claPriorityEntry=claPriorityEntry, ciscoLwappAAAMIBConfigGroup=ciscoLwappAAAMIBConfigGroup, claDBCurrentUsedEntries=claDBCurrentUsedEntries, claTacacsServerType=claTacacsServerType, claTacacsServerTimeout=claTacacsServerTimeout, claRadiusServerWlanActivatedEnabled=claRadiusServerWlanActivatedEnabled, claRadiusFallbackInterval=claRadiusFallbackInterval, ciscoLwappAAARadiusServerWlanDeactivated=ciscoLwappAAARadiusServerWlanDeactivated, claTacacsServerTable=claTacacsServerTable, claTacacsServerStorageType=claTacacsServerStorageType, claPriorityTable=claPriorityTable, claTacacsServerAddressType=claTacacsServerAddressType, ciscoLwappAAARadiusServerGlobalDeactivated=ciscoLwappAAARadiusServerGlobalDeactivated, claRadiusServerWlanDeactivatedEnabled=claRadiusServerWlanDeactivatedEnabled, claRadiusClientMacAddress=claRadiusClientMacAddress, ciscoLwappAAAMIBNotifsGroup=ciscoLwappAAAMIBNotifsGroup, claRadiusAcctMacDelimiter=claRadiusAcctMacDelimiter, claRadiusReqId=claRadiusReqId, claTacacsServerPriority=claTacacsServerPriority, claAcceptMICertificate=claAcceptMICertificate, claRadiusServerGlobalActivatedEnabled=claRadiusServerGlobalActivatedEnabled, ciscoLwappAAARadiusReqTimedOut=ciscoLwappAAARadiusReqTimedOut, ciscoLwappAAAMIBObjects=ciscoLwappAAAMIBObjects, claTacacsServerEnabled=claTacacsServerEnabled, ciscoLwappAAARadiusServerWlanActivated=ciscoLwappAAARadiusServerWlanActivated, claTacacsServerSecret=claTacacsServerSecret, claWlanAuthServerEnabled=claWlanAuthServerEnabled, claTacacsServerEntry=claTacacsServerEntry, claTacacsServerAddress=claTacacsServerAddress, claRadiusAddressType=claRadiusAddressType, claRadiusAddress=claRadiusAddress, claWlanAcctServerEnabled=claWlanAcctServerEnabled, ciscoLwappAAAMIBRadiusConfigGroup=ciscoLwappAAAMIBRadiusConfigGroup, ciscoLwappAAAMIBAPPolicyConfigGroup=ciscoLwappAAAMIBAPPolicyConfigGroup, claPriorityOrder=claPriorityOrder, ciscoLwappAAAMIBWlanAuthAccServerConfigGroup=ciscoLwappAAAMIBWlanAuthAccServerConfigGroup, ciscoLwappAAAMIBDBEntriesGroup=ciscoLwappAAAMIBDBEntriesGroup, claAcceptLSCertificate=claAcceptLSCertificate, ciscoLwappAAARadiusServerGlobalActivated=ciscoLwappAAARadiusServerGlobalActivated, claTacacsServerPortNum=claTacacsServerPortNum, claPriorityAuth=claPriorityAuth)