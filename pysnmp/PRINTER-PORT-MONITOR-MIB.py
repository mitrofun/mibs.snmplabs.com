#
# PySNMP MIB module PRINTER-PORT-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PRINTER-PORT-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, Integer32, Counter32, Gauge32, iso, Counter64, TimeTicks, IpAddress, Unsigned32, ObjectIdentity, ModuleIdentity, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Integer32", "Counter32", "Gauge32", "iso", "Counter64", "TimeTicks", "IpAddress", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ppmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2699, 1, 2))
ppmMIB.setRevisions(('2005-10-25 00:00',))
if mibBuilder.loadTexts: ppmMIB.setLastUpdated('200510250000Z')
if mibBuilder.loadTexts: ppmMIB.setOrganization('Printer Working Group, a Program of IEEE/ISTO')
ppmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1))
ppmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2))
ppmMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2))
ppmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1))
ppmGeneralNaturalLanguage = MibScalar((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmGeneralNaturalLanguage.setStatus('current')
ppmGeneralNumberOfPrinters = MibScalar((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmGeneralNumberOfPrinters.setStatus('current')
ppmGeneralNumberOfPorts = MibScalar((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmGeneralNumberOfPorts.setStatus('current')
ppmPrinter = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2))
ppmPrinterTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1), )
if mibBuilder.loadTexts: ppmPrinterTable.setStatus('current')
ppmPrinterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1), ).setIndexNames((0, "PRINTER-PORT-MONITOR-MIB", "ppmPrinterIndex"))
if mibBuilder.loadTexts: ppmPrinterEntry.setStatus('current')
ppmPrinterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ppmPrinterIndex.setStatus('current')
ppmPrinterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterName.setStatus('current')
ppmPrinterIEEE1284DeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1023)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterIEEE1284DeviceId.setStatus('current')
ppmPrinterNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterNumberOfPorts.setStatus('current')
ppmPrinterPreferredPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterPreferredPortIndex.setStatus('current')
ppmPrinterHrDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterHrDeviceIndex.setStatus('current')
ppmPrinterSnmpCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterSnmpCommunityName.setStatus('current')
ppmPrinterSnmpQueryEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPrinterSnmpQueryEnabled.setStatus('current')
ppmPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3))
ppmPortTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1), )
if mibBuilder.loadTexts: ppmPortTable.setStatus('current')
ppmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1), ).setIndexNames((0, "PRINTER-PORT-MONITOR-MIB", "ppmPrinterIndex"), (0, "PRINTER-PORT-MONITOR-MIB", "ppmPortIndex"))
if mibBuilder.loadTexts: ppmPortEntry.setStatus('current')
ppmPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ppmPortIndex.setStatus('current')
ppmPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortEnabled.setStatus('current')
ppmPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortName.setStatus('current')
ppmPortServiceNameOrURI = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortServiceNameOrURI.setStatus('current')
ppmPortProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortProtocolType.setStatus('current')
ppmPortProtocolTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortProtocolTargetPort.setStatus('current')
ppmPortProtocolAltSourceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortProtocolAltSourceEnabled.setStatus('current')
ppmPortPrtChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortPrtChannelIndex.setStatus('current')
ppmPortLprByteCountEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppmPortLprByteCountEnabled.setStatus('current')
ppmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 1)).setObjects(("PRINTER-PORT-MONITOR-MIB", "ppmGeneralGroup"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterGroup"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppmMIBCompliance = ppmMIBCompliance.setStatus('current')
ppmGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 1)).setObjects(("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNaturalLanguage"), ("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNumberOfPrinters"), ("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNumberOfPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppmGeneralGroup = ppmGeneralGroup.setStatus('current')
ppmPrinterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 2)).setObjects(("PRINTER-PORT-MONITOR-MIB", "ppmPrinterName"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterIEEE1284DeviceId"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterNumberOfPorts"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterPreferredPortIndex"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterHrDeviceIndex"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterSnmpCommunityName"), ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterSnmpQueryEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppmPrinterGroup = ppmPrinterGroup.setStatus('current')
ppmPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 3)).setObjects(("PRINTER-PORT-MONITOR-MIB", "ppmPortEnabled"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortName"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortServiceNameOrURI"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolType"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolTargetPort"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolAltSourceEnabled"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortPrtChannelIndex"), ("PRINTER-PORT-MONITOR-MIB", "ppmPortLprByteCountEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppmPortGroup = ppmPortGroup.setStatus('current')
mibBuilder.exportSymbols("PRINTER-PORT-MONITOR-MIB", ppmMIBObjects=ppmMIBObjects, ppmGeneral=ppmGeneral, ppmPortName=ppmPortName, ppmPrinterTable=ppmPrinterTable, ppmPortPrtChannelIndex=ppmPortPrtChannelIndex, ppmMIBConformance=ppmMIBConformance, ppmPrinterName=ppmPrinterName, ppmPortProtocolAltSourceEnabled=ppmPortProtocolAltSourceEnabled, ppmPortTable=ppmPortTable, PYSNMP_MODULE_ID=ppmMIB, ppmPrinterGroup=ppmPrinterGroup, ppmPrinterSnmpQueryEnabled=ppmPrinterSnmpQueryEnabled, ppmPrinterPreferredPortIndex=ppmPrinterPreferredPortIndex, ppmPortGroup=ppmPortGroup, ppmMIBCompliance=ppmMIBCompliance, ppmGeneralNumberOfPorts=ppmGeneralNumberOfPorts, ppmPrinterIEEE1284DeviceId=ppmPrinterIEEE1284DeviceId, ppmMIB=ppmMIB, ppmPort=ppmPort, ppmGeneralNumberOfPrinters=ppmGeneralNumberOfPrinters, ppmPrinterSnmpCommunityName=ppmPrinterSnmpCommunityName, ppmPrinterEntry=ppmPrinterEntry, ppmPrinterHrDeviceIndex=ppmPrinterHrDeviceIndex, ppmPrinterNumberOfPorts=ppmPrinterNumberOfPorts, ppmPrinterIndex=ppmPrinterIndex, ppmPortProtocolType=ppmPortProtocolType, ppmPortIndex=ppmPortIndex, ppmPrinter=ppmPrinter, ppmMIBObjectGroups=ppmMIBObjectGroups, ppmPortProtocolTargetPort=ppmPortProtocolTargetPort, ppmGeneralNaturalLanguage=ppmGeneralNaturalLanguage, ppmGeneralGroup=ppmGeneralGroup, ppmPortLprByteCountEnabled=ppmPortLprByteCountEnabled, ppmPortEnabled=ppmPortEnabled, ppmPortServiceNameOrURI=ppmPortServiceNameOrURI, ppmPortEntry=ppmPortEntry)
