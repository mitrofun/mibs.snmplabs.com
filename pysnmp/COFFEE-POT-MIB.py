#
# PySNMP MIB module COFFEE-POT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COFFEE-POT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, transmission, TimeTicks, Gauge32, Bits, IpAddress, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, NotificationType, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "transmission", "TimeTicks", "Gauge32", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "NotificationType", "iso", "Counter32")
TimeStamp, TextualConvention, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TimeInterval", "DisplayString")
coffee = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 132))
if mibBuilder.loadTexts: coffee.setLastUpdated('9803231700Z')
if mibBuilder.loadTexts: coffee.setOrganization('Networked Appliance Management Working Group')
potName = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potName.setStatus('current')
potCapacity = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: potCapacity.setStatus('current')
potType = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("automatic-drip", 1), ("percolator", 2), ("french-press", 3), ("espresso", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potType.setStatus('current')
potLocation = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potLocation.setStatus('current')
potMonitor = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 132, 6))
potOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 1), ("brewing", 2), ("holding", 3), ("other", 4), ("waiting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potOperStatus.setStatus('current')
potLevel = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: potLevel.setStatus('current')
potMetric = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("espresso", 1), ("demi-tasse", 2), ("cup", 3), ("mug", 4), ("bucket", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potMetric.setStatus('current')
potStartTime = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potStartTime.setStatus('current')
lastStartTime = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastStartTime.setStatus('current')
potTemperature = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 6), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: potTemperature.setStatus('current')
mibBuilder.exportSymbols("COFFEE-POT-MIB", lastStartTime=lastStartTime, potLevel=potLevel, potLocation=potLocation, potType=potType, coffee=coffee, potCapacity=potCapacity, PYSNMP_MODULE_ID=coffee, potMetric=potMetric, potStartTime=potStartTime, potTemperature=potTemperature, potOperStatus=potOperStatus, potMonitor=potMonitor, potName=potName)