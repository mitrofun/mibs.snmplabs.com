#
# PySNMP MIB module RBN-MEDIA-GATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-MEDIA-GATEWAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IANAItuProbableCause, IANAItuEventType = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuProbableCause", "IANAItuEventType")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, Integer32, Unsigned32, IpAddress, MibIdentifier, NotificationType, iso, Counter32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "iso", "Counter32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter64")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rbnMediaGatewayMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 52))
rbnMediaGatewayMib.setRevisions(('2010-04-19 00:00', '2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnMediaGatewayMib.setRevisionsDescriptions(('Modified the rbnH248LinkStatusAlarm Description regarding timeout value which triggers this notification', 'Initial Version.',))
if mibBuilder.loadTexts: rbnMediaGatewayMib.setLastUpdated('201004190000Z')
if mibBuilder.loadTexts: rbnMediaGatewayMib.setOrganization('Ericsson Inc.')
if mibBuilder.loadTexts: rbnMediaGatewayMib.setContactInfo(' Ericsson Inc. 100 Headquarters Drive San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 ')
if mibBuilder.loadTexts: rbnMediaGatewayMib.setDescription('Defines the objects necessary to support the management of Media Gateway(MG) objects.')
rbnMediaGatewayNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 0))
rbnMediaGatewayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1))
rbnMediaGatewayConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2))
rbnMediaGatewayNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1))
rbnMGEventDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventDateAndTime.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventDateAndTime.setDescription('The local date and time when the event was raised.')
rbnMGEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 2), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventSeverity.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventSeverity.setDescription('The current severity of the event.')
rbnMGEventSender = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventSender.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventSender.setDescription('Identifier of the entity sending the event.')
rbnMGEventType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 4), IANAItuEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventType.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventType.setDescription('The type of the event.')
rbnMGEventProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 5), IANAItuProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventProbableCause.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventProbableCause.setDescription('The probable cause for this event.')
rbnMGEventInformation = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventInformation.setStatus('current')
if mibBuilder.loadTexts: rbnMGEventInformation.setDescription('Additional information to describe the problem.')
rbnH248LinkStatusAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 52, 0, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
if mibBuilder.loadTexts: rbnH248LinkStatusAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnH248LinkStatusAlarm.setDescription("This notification signifies that the SNMP entity has detected that the H.248 link for a Media Gateway Controller (MGC) Group is down for more than configured timeout when rbnMGEventSeverity has the value 'major'. The timeout value is out of scope of the MIB module. The notification is sent with a value of 'clear' for rbnMGEventSeverity when the link state is restored (operationally up) or is obsoleted due to certain configuration change.")
rbnMediaGatewayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1))
rbnMediaGatewayGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2))
rbnMGCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGNotifyObjectGroup"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGLinkNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGCompliance = rbnMGCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnMGCompliance.setDescription('The compliance statement for SNMP entities which implement the Media Gateway MIB.')
rbnMGNotifyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGNotifyObjectGroup = rbnMGNotifyObjectGroup.setStatus('current')
if mibBuilder.loadTexts: rbnMGNotifyObjectGroup.setDescription('The collection of objects related to Media Gateway notifications.')
rbnMGLinkNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 2)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnH248LinkStatusAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGLinkNotifyGroup = rbnMGLinkNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: rbnMGLinkNotifyGroup.setDescription('Notification for tracking Media Gateway events.')
mibBuilder.exportSymbols("RBN-MEDIA-GATEWAY-MIB", rbnMediaGatewayConformance=rbnMediaGatewayConformance, rbnMediaGatewayCompliances=rbnMediaGatewayCompliances, PYSNMP_MODULE_ID=rbnMediaGatewayMib, rbnMGEventSeverity=rbnMGEventSeverity, rbnMGEventSender=rbnMGEventSender, rbnMGEventType=rbnMGEventType, rbnMGEventInformation=rbnMGEventInformation, rbnMediaGatewayObjects=rbnMediaGatewayObjects, rbnMediaGatewayNotify=rbnMediaGatewayNotify, rbnMediaGatewayMib=rbnMediaGatewayMib, rbnMGEventDateAndTime=rbnMGEventDateAndTime, rbnMGEventProbableCause=rbnMGEventProbableCause, rbnMediaGatewayGroups=rbnMediaGatewayGroups, rbnMGNotifyObjectGroup=rbnMGNotifyObjectGroup, rbnMGLinkNotifyGroup=rbnMGLinkNotifyGroup, rbnMGCompliance=rbnMGCompliance, rbnMediaGatewayNotifications=rbnMediaGatewayNotifications, rbnH248LinkStatusAlarm=rbnH248LinkStatusAlarm)
