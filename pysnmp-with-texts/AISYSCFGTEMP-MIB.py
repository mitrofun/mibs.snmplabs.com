#
# PySNMP MIB module AISYSCFGTEMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISYSCFGTEMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, Integer32, TimeTicks, Gauge32, MibIdentifier, iso, ObjectIdentity, NotificationType, ModuleIdentity, IpAddress, Unsigned32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "IpAddress", "Unsigned32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 32))
aiSysCfgTemp = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 32, 5))
aiSysCfgTemp.setRevisions(('2001-04-30 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aiSysCfgTemp.setRevisionsDescriptions(('The initial revision of this module.',))
if mibBuilder.loadTexts: aiSysCfgTemp.setLastUpdated('200104301700Z')
if mibBuilder.loadTexts: aiSysCfgTemp.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiSysCfgTemp.setContactInfo(' Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email: snmp@aiinet.com')
if mibBuilder.loadTexts: aiSysCfgTemp.setDescription('MIB module for Temperature Probes.')
aiSCTempTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 32, 5, 0))
aiSCTempTrapFail = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 5, 0, 1)).setObjects(("AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"), ("AISYSCFGTEMP-MIB", "aiSCTempProbeTempCelsius"))
if mibBuilder.loadTexts: aiSCTempTrapFail.setStatus('current')
if mibBuilder.loadTexts: aiSCTempTrapFail.setDescription('Trap sent when a temperature probe reads a value outside its operational range.')
aiSCTempTrapOk = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 5, 0, 2)).setObjects(("AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"), ("AISYSCFGTEMP-MIB", "aiSCTempProbeTempCelsius"))
if mibBuilder.loadTexts: aiSCTempTrapOk.setStatus('current')
if mibBuilder.loadTexts: aiSCTempTrapOk.setDescription('Trap sent when a temperature probe reverts to its operational range from a failure mode.')
aiSCTempAgregateStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("okay", 1), ("trouble", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempAgregateStatus.setStatus('current')
if mibBuilder.loadTexts: aiSCTempAgregateStatus.setDescription('Aggregate status of the temperature probes in the system.')
aiSCTempProbeTable = MibTable((1, 3, 6, 1, 4, 1, 539, 32, 5, 2), )
if mibBuilder.loadTexts: aiSCTempProbeTable.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeTable.setDescription('A table of information on each temperature probe in the system.')
aiSCTempProbeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1), ).setIndexNames((0, "AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"))
if mibBuilder.loadTexts: aiSCTempProbeEntry.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeEntry.setDescription('')
aiSCTempProbeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempProbeIndex.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeIndex.setDescription('Self referential index into this table.')
aiSCTempProbeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempProbeDescription.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeDescription.setDescription('Description of the temperature probe to which this table entry refers.')
aiSCTempProbeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempProbeStatus.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeStatus.setDescription('The state of this temperature probe. available(1) indicates that the value returned in aiSCTempCelsius is valid.')
aiSCTempProbeLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("external", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempProbeLocation.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeLocation.setDescription('The location of this temperature probe. It is either available or unavailable.')
aiSCTempProbeLowThreshCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 5), Integer32()).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTempProbeLowThreshCelsius.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeLowThreshCelsius.setDescription('The lower threshold for this temperature probe (Celsius). When the temp drops below this value, an SNMP trap is sent.')
aiSCTempProbeHighThreshCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 6), Integer32()).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiSCTempProbeHighThreshCelsius.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeHighThreshCelsius.setDescription('The upper threshold for this temperature probe (Celsius). When the temp rises above this value, an SNMP trap is sent.')
aiSCTempProbeTempCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 7), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCTempProbeTempCelsius.setStatus('current')
if mibBuilder.loadTexts: aiSCTempProbeTempCelsius.setDescription('The current temperature of this probe (Celsius).')
mibBuilder.exportSymbols("AISYSCFGTEMP-MIB", aiSCTempProbeTempCelsius=aiSCTempProbeTempCelsius, aiSysCfg=aiSysCfg, aiSCTempTrapFail=aiSCTempTrapFail, aiSysCfgTemp=aiSysCfgTemp, aiSCTempProbeEntry=aiSCTempProbeEntry, aii=aii, aiSCTempProbeIndex=aiSCTempProbeIndex, aiSCTempProbeLocation=aiSCTempProbeLocation, aiSCTempTrapInfo=aiSCTempTrapInfo, aiSCTempTrapOk=aiSCTempTrapOk, aiSCTempProbeTable=aiSCTempProbeTable, aiSCTempProbeHighThreshCelsius=aiSCTempProbeHighThreshCelsius, PYSNMP_MODULE_ID=aiSysCfgTemp, aiSCTempProbeLowThreshCelsius=aiSCTempProbeLowThreshCelsius, aiSCTempProbeStatus=aiSCTempProbeStatus, aiSCTempAgregateStatus=aiSCTempAgregateStatus, aiSCTempProbeDescription=aiSCTempProbeDescription)