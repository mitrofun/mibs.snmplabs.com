#
# PySNMP MIB module ARISTA-HARDWARE-UTILIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-HARDWARE-UTILIZATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter64, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Unsigned32, IpAddress, MibIdentifier, iso, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "Bits")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
aristaHardwareUtilizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 22))
aristaHardwareUtilizationMIB.setRevisions(('2016-05-24 00:00',))
if mibBuilder.loadTexts: aristaHardwareUtilizationMIB.setLastUpdated('201605240000Z')
if mibBuilder.loadTexts: aristaHardwareUtilizationMIB.setOrganization('Arista Networks, Inc.')
aristaHardwareUtilizationMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 22, 0))
aristaHardwareUtilizationMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1))
aristaHardwareUtilizationMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2))
aristaHardwareUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1), )
if mibBuilder.loadTexts: aristaHardwareUtilizationTable.setStatus('current')
aristaHardwareUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1), ).setIndexNames((0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationResource"), (0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationFeature"), (0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationForwardingElement"))
if mibBuilder.loadTexts: aristaHardwareUtilizationEntry.setStatus('current')
aristaHardwareUtilizationResource = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35)))
if mibBuilder.loadTexts: aristaHardwareUtilizationResource.setStatus('current')
aristaHardwareUtilizationFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35)))
if mibBuilder.loadTexts: aristaHardwareUtilizationFeature.setStatus('current')
aristaHardwareUtilizationForwardingElement = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35)))
if mibBuilder.loadTexts: aristaHardwareUtilizationForwardingElement.setStatus('current')
aristaHardwareUtilizationInUseEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationInUseEntries.setStatus('current')
aristaHardwareUtilizationFreeEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationFreeEntries.setStatus('current')
aristaHardwareUtilizationCommittedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationCommittedEntries.setStatus('current')
aristaHardwareUtilizationMaxEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationMaxEntries.setStatus('current')
aristaHardwareUtilizationHighWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationHighWatermark.setStatus('current')
aristaHardwareUtilizationHighWatermarkTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaHardwareUtilizationHighWatermarkTime.setStatus('current')
aristaHardwareUtilizationAlert = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 22, 0, 1)).setObjects(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationInUseEntries"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermark"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermarkTime"))
if mibBuilder.loadTexts: aristaHardwareUtilizationAlert.setStatus('current')
aristaHardwareUtilizationMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 1))
aristaHardwareUtilizationMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2))
aristaHardwareUtilizationMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 1, 1)).setObjects(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationTableGroup"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaHardwareUtilizationMibCompliance = aristaHardwareUtilizationMibCompliance.setStatus('current')
aristaHardwareUtilizationTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2, 1)).setObjects(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationInUseEntries"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationFreeEntries"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationCommittedEntries"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationMaxEntries"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermark"), ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermarkTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaHardwareUtilizationTableGroup = aristaHardwareUtilizationTableGroup.setStatus('current')
aristaHardwareUtilizationNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2, 2)).setObjects(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaHardwareUtilizationNotificationsGroup = aristaHardwareUtilizationNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-HARDWARE-UTILIZATION-MIB", aristaHardwareUtilizationHighWatermark=aristaHardwareUtilizationHighWatermark, aristaHardwareUtilizationTableGroup=aristaHardwareUtilizationTableGroup, aristaHardwareUtilizationMibCompliance=aristaHardwareUtilizationMibCompliance, aristaHardwareUtilizationMibNotifications=aristaHardwareUtilizationMibNotifications, PYSNMP_MODULE_ID=aristaHardwareUtilizationMIB, aristaHardwareUtilizationTable=aristaHardwareUtilizationTable, aristaHardwareUtilizationAlert=aristaHardwareUtilizationAlert, aristaHardwareUtilizationForwardingElement=aristaHardwareUtilizationForwardingElement, aristaHardwareUtilizationFeature=aristaHardwareUtilizationFeature, aristaHardwareUtilizationMibObjects=aristaHardwareUtilizationMibObjects, aristaHardwareUtilizationEntry=aristaHardwareUtilizationEntry, aristaHardwareUtilizationInUseEntries=aristaHardwareUtilizationInUseEntries, aristaHardwareUtilizationMibCompliances=aristaHardwareUtilizationMibCompliances, aristaHardwareUtilizationMIB=aristaHardwareUtilizationMIB, aristaHardwareUtilizationMibConformance=aristaHardwareUtilizationMibConformance, aristaHardwareUtilizationHighWatermarkTime=aristaHardwareUtilizationHighWatermarkTime, aristaHardwareUtilizationMaxEntries=aristaHardwareUtilizationMaxEntries, aristaHardwareUtilizationMibGroups=aristaHardwareUtilizationMibGroups, aristaHardwareUtilizationCommittedEntries=aristaHardwareUtilizationCommittedEntries, aristaHardwareUtilizationNotificationsGroup=aristaHardwareUtilizationNotificationsGroup, aristaHardwareUtilizationFreeEntries=aristaHardwareUtilizationFreeEntries, aristaHardwareUtilizationResource=aristaHardwareUtilizationResource)
