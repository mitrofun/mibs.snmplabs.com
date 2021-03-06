#
# PySNMP MIB module CISCO-OPTICAL-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-MONITORING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, MibIdentifier, ObjectIdentity, Unsigned32, NotificationType, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "IpAddress", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoOpticalMonitoringMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 83))
ciscoOpticalMonitoringMIB.setRevisions(('2001-12-04 11:30',))
if mibBuilder.loadTexts: ciscoOpticalMonitoringMIB.setLastUpdated('200112041130Z')
if mibBuilder.loadTexts: ciscoOpticalMonitoringMIB.setOrganization('Cisco Systems, Inc.')
ciscoOpticalMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 1))
comParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1))
comParametersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1), )
if mibBuilder.loadTexts: comParametersTable.setStatus('current')
comParametersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: comParametersEntry.setStatus('current')
comTxBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('milliamps').setMaxAccess("readonly")
if mibBuilder.loadTexts: comTxBiasCurrent.setStatus('current')
comTxPowerSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comTxPowerSupported.setStatus('current')
comTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('microWatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: comTxPower.setStatus('current')
comTxLaserTempSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comTxLaserTempSupported.setStatus('current')
comTxLaserTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-253, 200))).setUnits(' Degree Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: comTxLaserTemp.setStatus('current')
comRxPowerACDC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('microWatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: comRxPowerACDC.setStatus('current')
comRxPowerACSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comRxPowerACSupported.setStatus('current')
comRxPowerAC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 83, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('microWatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: comRxPowerAC.setStatus('current')
ciscoOpticalMonMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 2))
ciscoOpticalMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 2, 0))
ciscoOpticalMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 3))
ciscoOpticalMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 1))
ciscoOpticalMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 2))
ciscoOpticalMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 1, 1)).setObjects(("CISCO-OPTICAL-MONITORING-MIB", "ciscoOpticalMonMIBParamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonMIBCompliance = ciscoOpticalMonMIBCompliance.setStatus('current')
ciscoOpticalMonMIBParamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 83, 3, 2, 1)).setObjects(("CISCO-OPTICAL-MONITORING-MIB", "comTxBiasCurrent"), ("CISCO-OPTICAL-MONITORING-MIB", "comTxPowerSupported"), ("CISCO-OPTICAL-MONITORING-MIB", "comTxPower"), ("CISCO-OPTICAL-MONITORING-MIB", "comTxLaserTempSupported"), ("CISCO-OPTICAL-MONITORING-MIB", "comTxLaserTemp"), ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerACDC"), ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerACSupported"), ("CISCO-OPTICAL-MONITORING-MIB", "comRxPowerAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonMIBParamGroup = ciscoOpticalMonMIBParamGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITORING-MIB", comParameters=comParameters, comTxLaserTempSupported=comTxLaserTempSupported, comRxPowerACDC=comRxPowerACDC, comTxLaserTemp=comTxLaserTemp, ciscoOpticalMonMIBConformance=ciscoOpticalMonMIBConformance, comTxPower=comTxPower, ciscoOpticalMonMIBParamGroup=ciscoOpticalMonMIBParamGroup, comTxPowerSupported=comTxPowerSupported, ciscoOpticalMonitoringMIB=ciscoOpticalMonitoringMIB, comParametersEntry=comParametersEntry, comRxPowerAC=comRxPowerAC, ciscoOpticalMonMIBNotifications=ciscoOpticalMonMIBNotifications, comRxPowerACSupported=comRxPowerACSupported, ciscoOpticalMonMIBObjects=ciscoOpticalMonMIBObjects, comParametersTable=comParametersTable, PYSNMP_MODULE_ID=ciscoOpticalMonitoringMIB, comTxBiasCurrent=comTxBiasCurrent, ciscoOpticalMonMIBCompliances=ciscoOpticalMonMIBCompliances, ciscoOpticalMonMIBNotifPrefix=ciscoOpticalMonMIBNotifPrefix, ciscoOpticalMonMIBCompliance=ciscoOpticalMonMIBCompliance, ciscoOpticalMonMIBGroups=ciscoOpticalMonMIBGroups)
