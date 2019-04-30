#
# PySNMP MIB module COLUBRIS-CLIENT-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-CLIENT-TRACKING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, Bits, Integer32, Counter32, TimeTicks, ObjectIdentity, IpAddress, iso, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "Bits", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "IpAddress", "iso", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisClientTrackingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 19))
if mibBuilder.loadTexts: colubrisClientTrackingMIB.setLastUpdated('200502250000Z')
if mibBuilder.loadTexts: colubrisClientTrackingMIB.setOrganization('Colubris Networks, Inc.')
colubrisClientTrackingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1))
clientTrackingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1))
clientTrackingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 2))
clientTrackingSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 1), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociationNotificationEnabled.setStatus('current')
clientTrackingAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 2), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingAssociationFailureNotificationEnabled.setStatus('current')
clientTrackingSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 3), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociationNotificationEnabled.setStatus('current')
clientTrackingReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 4), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingReAssociationFailureNotificationEnabled.setStatus('current')
clientTrackingSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 5), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthenticationNotificationEnabled.setStatus('current')
clientTrackingAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 6), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingAuthenticationFailureNotificationEnabled.setStatus('current')
clientTrackingSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 7), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociationNotificationEnabled.setStatus('current')
clientTrackingDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 8), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingDisAssociationFailureNotificationEnabled.setStatus('current')
clientTrackingSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 9), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
clientTrackingDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 10), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailureNotificationEnabled.setStatus('current')
clientTrackingEventInformation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clientTrackingEventInformation.setStatus('current')
colubrisClientTrackingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2))
colubrisClientTrackingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0))
clientTrackingSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 1)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociation.setStatus('current')
clientTrackingAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 2)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingAssociationFailure.setStatus('current')
clientTrackingSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 3)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociation.setStatus('current')
clientTrackingReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 4)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingReAssociationFailure.setStatus('current')
clientTrackingSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 5)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthentication.setStatus('current')
clientTrackingAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 6)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingAuthenticationFailure.setStatus('current')
clientTrackingSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 7)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociation.setStatus('current')
clientTrackingDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 8)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingDisAssociationFailure.setStatus('current')
clientTrackingSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 9)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthentication.setStatus('current')
clientTrackingDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 10)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailure.setStatus('current')
colubrisClientTrackingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3))
colubrisClientTrackingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 1))
colubrisClientTrackingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2))
colubrisClientTrackingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 1, 1)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "colubrisClientTrackingConfigMIBGroup"), ("COLUBRIS-CLIENT-TRACKING-MIB", "colubrisClientTrackingInfoMIBGroup"), ("COLUBRIS-CLIENT-TRACKING-MIB", "colubrisClientTrackingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisClientTrackingMIBCompliance = colubrisClientTrackingMIBCompliance.setStatus('current')
colubrisClientTrackingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 1)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociationNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailureNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociationNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailureNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthenticationNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailureNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociationNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailureNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthenticationNotificationEnabled"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisClientTrackingConfigMIBGroup = colubrisClientTrackingConfigMIBGroup.setStatus('current')
colubrisClientTrackingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 2)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisClientTrackingInfoMIBGroup = colubrisClientTrackingInfoMIBGroup.setStatus('current')
colubrisClientTrackingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 3)).setObjects(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociation"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailure"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociation"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailure"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthentication"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailure"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociation"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailure"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthentication"), ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisClientTrackingNotificationGroup = colubrisClientTrackingNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-CLIENT-TRACKING-MIB", colubrisClientTrackingMIBNotifications=colubrisClientTrackingMIBNotifications, clientTrackingAuthenticationFailure=clientTrackingAuthenticationFailure, clientTrackingSuccessfulAuthentication=clientTrackingSuccessfulAuthentication, clientTrackingDeAuthenticationFailure=clientTrackingDeAuthenticationFailure, clientTrackingDisAssociationFailure=clientTrackingDisAssociationFailure, colubrisClientTrackingMIB=colubrisClientTrackingMIB, clientTrackingReAssociationFailure=clientTrackingReAssociationFailure, clientTrackingAssociationFailure=clientTrackingAssociationFailure, clientTrackingSuccessfulReAssociation=clientTrackingSuccessfulReAssociation, clientTrackingSuccessfulAssociation=clientTrackingSuccessfulAssociation, clientTrackingAssociationFailureNotificationEnabled=clientTrackingAssociationFailureNotificationEnabled, clientTrackingSuccessfulAuthenticationNotificationEnabled=clientTrackingSuccessfulAuthenticationNotificationEnabled, clientTrackingSuccessfulDisAssociationNotificationEnabled=clientTrackingSuccessfulDisAssociationNotificationEnabled, clientTrackingSuccessfulDisAssociation=clientTrackingSuccessfulDisAssociation, clientTrackingAuthenticationFailureNotificationEnabled=clientTrackingAuthenticationFailureNotificationEnabled, colubrisClientTrackingInfoMIBGroup=colubrisClientTrackingInfoMIBGroup, colubrisClientTrackingMIBGroups=colubrisClientTrackingMIBGroups, colubrisClientTrackingMIBObjects=colubrisClientTrackingMIBObjects, clientTrackingDisAssociationFailureNotificationEnabled=clientTrackingDisAssociationFailureNotificationEnabled, colubrisClientTrackingMIBConformance=colubrisClientTrackingMIBConformance, colubrisClientTrackingMIBCompliance=colubrisClientTrackingMIBCompliance, colubrisClientTrackingNotificationGroup=colubrisClientTrackingNotificationGroup, colubrisClientTrackingMIBNotificationPrefix=colubrisClientTrackingMIBNotificationPrefix, clientTrackingSuccessfulDeAuthentication=clientTrackingSuccessfulDeAuthentication, clientTrackingReAssociationFailureNotificationEnabled=clientTrackingReAssociationFailureNotificationEnabled, colubrisClientTrackingMIBCompliances=colubrisClientTrackingMIBCompliances, PYSNMP_MODULE_ID=colubrisClientTrackingMIB, clientTrackingConfig=clientTrackingConfig, clientTrackingInfo=clientTrackingInfo, clientTrackingEventInformation=clientTrackingEventInformation, clientTrackingSuccessfulDeAuthenticationNotificationEnabled=clientTrackingSuccessfulDeAuthenticationNotificationEnabled, clientTrackingSuccessfulReAssociationNotificationEnabled=clientTrackingSuccessfulReAssociationNotificationEnabled, clientTrackingSuccessfulAssociationNotificationEnabled=clientTrackingSuccessfulAssociationNotificationEnabled, colubrisClientTrackingConfigMIBGroup=colubrisClientTrackingConfigMIBGroup, clientTrackingDeAuthenticationFailureNotificationEnabled=clientTrackingDeAuthenticationFailureNotificationEnabled)