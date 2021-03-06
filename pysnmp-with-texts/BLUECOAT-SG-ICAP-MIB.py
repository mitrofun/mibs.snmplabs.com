#
# PySNMP MIB module BLUECOAT-SG-ICAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-SG-ICAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, TimeTicks, Gauge32, ObjectIdentity, NotificationType, Bits, ModuleIdentity, Integer32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "TimeTicks", "Gauge32", "ObjectIdentity", "NotificationType", "Bits", "ModuleIdentity", "Integer32", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGICAPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 14))
bluecoatSGICAPMIB.setRevisions(('2013-02-08 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGICAPMIB.setRevisionsDescriptions(('Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setLastUpdated('201302081400Z')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setContactInfo('support.services@bluecoat.com http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setDescription('Internet Content Adaptation Protocol (ICAP) is an open standard protocol that allows content engines to send HTTP-based content to an ICAP server for performing value added services. The ProxySG appliance, when integrated with a supported ICAP server such as the Proxy-AV, provides content scanning, filtering, and repair service for Internet-based malicious code, in addition to reducing bandwidth usage and latency. This is the MIB module for ProxySG ICAP feature.')
bluecoatSgICAPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1))
bluecoatSgICAPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2))
sgICAPMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0))
bluecoatSgICAPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3))
class ICAPServiceEntityType(TextualConvention, Integer32):
    description = 'In the ProxySG appliance, an ICAP service is a collection of attributes that defines the communication between the appliance and the ICAP server. Similar ICAP scanning services can then be grouped together to create a service group that helps to distribute and load balance scanning requests. This data type distinguishes an ICAP service entity between a service group and service. service (1) - A single service entity which may or may not be part a service group serviceGroup (2) - a collection of services of same type of operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("service", 1), ("servivceGroup", 2))

class ICAPServiceNotificationType(TextualConvention, Integer32):
    description = 'This TC enumerates an event related to ProxySG ICAP service. The events are sent as part of ICAP service notification. The events include: queuedRequestsAboveThreshold(1) - The number of queued ICAP requests for a service has gone above the permissible threshold. This event denotes an impending service impact for new requests. New requests may be rejected and can cause serviceability issues for users. This problem usually occur because there is insufficient number of ICAP connections for the load the ProxySG is handling. queuedRequestsBelowThreshold(2) - The number of queued ICAP requests has fallen below the alert threshold. This event indicates that the number of queued requests is now within normal limits and that the ICAP service has returned to a healthy state. deferredRequestsAboveThreshold(3) - The number of deferred requests for a service has gone above the permissible threshold. This event denotes an impending service impact for new connections. deferredRequestsBelowThreshold(4) - The number of deferred ICAP requests has fallen below the threshold. This event indicates that the number of deferred ICAP requests is now within normal limits and that the ICAP service has returned to a healthy state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("queuedRequestsAboveThreshold", 1), ("queuedRequestsBelowThreshold", 2), ("deferredRequestsAboveThreshold", 3), ("deferredRequestsBelowThreshold", 4))

bluecoatSgICAPValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1))
icapService = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1))
icapServiceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1), )
if mibBuilder.loadTexts: icapServiceStatsTable.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsTable.setDescription('This table represents various operational statistics of ICAP services and service groups in an ProxySG appliance.')
icapServiceStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-ICAP-MIB", "icapServiceStatsIndex"))
if mibBuilder.loadTexts: icapServiceStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsTableEntry.setDescription('An entry in this table represents the statistics for an ICAP service entity. An entity is uniquely identified by the service name (icapServiceStatsEntityName).')
icapServiceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: icapServiceStatsIndex.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsIndex.setDescription('This is the index of the table and is an unique identifier of the entity.')
icapServiceStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsName.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsName.setDescription('This attribute represents the configured name of the service or the service group.')
icapServiceStatsEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 3), ICAPServiceEntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsEntityType.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsEntityType.setDescription('This attribute defines the entity type: service or service group. The service group statistics represent the sum of all the services that are members of the group.')
icapServiceStatsPlainConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainConns.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsPlainConns.setDescription('Number of ICAP scanning transactions that are not encrypted.')
icapServiceStatsSecuredConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecuredConns.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSecuredConns.setDescription('Number of ICAP scanning transactions that are encrypted and tunneled over SSL.')
icapServiceStatsPlainActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainActvReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsPlainActvReqs.setDescription('Line of communication between the ProxySG appliance and an ICAP server across which plain ICAP scanning requests are sent. This statistic is not tracked for service groups.')
icapServiceStatsSecureActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecureActvReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSecureActvReqs.setDescription('Secure line of communication between the ProxySG appliance and an ICAP server across which encrypted ICAP scanning requests are sent. This statistic is not tracked for service groups.')
icapServiceStatsQueuedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsQueuedReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsQueuedReqs.setDescription('ICAP scanning transactions that are waiting for an available connection.')
icapServiceStatsDeferredReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsDeferredReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsDeferredReqs.setDescription('Number of ICAP scanning transactions that have been deferred until the full object has been received.')
icapServiceStatsRcvdBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsRcvdBytes.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsRcvdBytes.setDescription('Number of data bytes received from the ICAP service or service group.')
icapServiceStatsSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSentBytes.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSentBytes.setDescription('Number of bytes of ICAP data sent to the ICAP service or service group.')
icapServiceStatsFailedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsFailedReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsFailedReqs.setDescription('Number of ICAP scanning transactions that failed because of a scanning timeout, connection failure, server error, or a variety of other situations.')
icapServiceStatsSuccessfullReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSuccessfullReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSuccessfullReqs.setDescription('Number of ICAP scanning transactions that completed successfully.')
sgICAPNotification = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 2), ICAPServiceNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgICAPNotification.setStatus('current')
if mibBuilder.loadTexts: sgICAPNotification.setDescription('A notification type that describes an ICAP event.')
sgICAPTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"))
if mibBuilder.loadTexts: sgICAPTrap.setStatus('current')
if mibBuilder.loadTexts: sgICAPTrap.setDescription('A notification that represents an ICAP- related event on an ProxySG appliance. The attributes of an ICAP notification include: sgICAPNotification - defines the event type. icapServiceStatsName - the service on which the event has occurred icapServiceStatsDeferredReqs - the number of deferred connections on the service, at the time of event icapServiceStatsQueuedReqs - the number of queued connections on the service, at the time of event.')
bluecoatSgICAPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1))
bluecoatSgICAPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2))
bluecoatSgICAPMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3))
bluecoatSgICAPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "bluecoatSgICAPMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBCompliance = bluecoatSgICAPMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBCompliance.setDescription('The compliance statement for ICAP Module. ')
bluecoatSgICAPMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsEntityType"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecuredConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecureActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsRcvdBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSentBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsFailedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSuccessfullReqs"), ("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBGroup = bluecoatSgICAPMIBGroup.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBGroup.setDescription('Group of ICAP-related objects implemented in ProxySG appliances.')
bluecoatSgICAPMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBNotifGroup = bluecoatSgICAPMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBNotifGroup.setDescription('Group of ICAP notifications implemented in ProxySG appliances.')
mibBuilder.exportSymbols("BLUECOAT-SG-ICAP-MIB", sgICAPMIBNotificationsPrefix=sgICAPMIBNotificationsPrefix, ICAPServiceEntityType=ICAPServiceEntityType, icapServiceStatsName=icapServiceStatsName, icapServiceStatsSecuredConns=icapServiceStatsSecuredConns, icapServiceStatsIndex=icapServiceStatsIndex, bluecoatSgICAPMIBNotifGroup=bluecoatSgICAPMIBNotifGroup, icapServiceStatsSuccessfullReqs=icapServiceStatsSuccessfullReqs, icapServiceStatsSecureActvReqs=icapServiceStatsSecureActvReqs, PYSNMP_MODULE_ID=bluecoatSGICAPMIB, icapServiceStatsFailedReqs=icapServiceStatsFailedReqs, bluecoatSgICAPMIBNotifGroups=bluecoatSgICAPMIBNotifGroups, icapService=icapService, bluecoatSgICAPMIBCompliance=bluecoatSgICAPMIBCompliance, icapServiceStatsRcvdBytes=icapServiceStatsRcvdBytes, bluecoatSgICAPMIBNotifications=bluecoatSgICAPMIBNotifications, bluecoatSgICAPValues=bluecoatSgICAPValues, icapServiceStatsQueuedReqs=icapServiceStatsQueuedReqs, bluecoatSgICAPMIBCompliances=bluecoatSgICAPMIBCompliances, bluecoatSGICAPMIB=bluecoatSGICAPMIB, bluecoatSgICAPMIBGroups=bluecoatSgICAPMIBGroups, sgICAPNotification=sgICAPNotification, bluecoatSgICAPMIBConformance=bluecoatSgICAPMIBConformance, ICAPServiceNotificationType=ICAPServiceNotificationType, bluecoatSgICAPMIBObjects=bluecoatSgICAPMIBObjects, icapServiceStatsPlainConns=icapServiceStatsPlainConns, icapServiceStatsDeferredReqs=icapServiceStatsDeferredReqs, sgICAPTrap=sgICAPTrap, bluecoatSgICAPMIBGroup=bluecoatSgICAPMIBGroup, icapServiceStatsEntityType=icapServiceStatsEntityType, icapServiceStatsPlainActvReqs=icapServiceStatsPlainActvReqs, icapServiceStatsSentBytes=icapServiceStatsSentBytes, icapServiceStatsTableEntry=icapServiceStatsTableEntry, icapServiceStatsTable=icapServiceStatsTable)
