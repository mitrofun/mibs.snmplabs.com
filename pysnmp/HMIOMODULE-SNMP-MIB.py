#
# PySNMP MIB module HMIOMODULE-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HMIOMODULE-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
hmChassis, hmChassisEvent = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hmChassis", "hmChassisEvent")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, Integer32, TimeTicks, NotificationType, Bits, Counter64, IpAddress, iso, ModuleIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Integer32", "TimeTicks", "NotificationType", "Bits", "Counter64", "IpAddress", "iso", "ModuleIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HmEnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

hmIOModuleGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 1, 13))
hmIOModuleGroup.setRevisions(('2010-11-08 15:00',))
if mibBuilder.loadTexts: hmIOModuleGroup.setLastUpdated('201011081500Z')
if mibBuilder.loadTexts: hmIOModuleGroup.setOrganization('Hirschmann Automation and Control GmbH')
hmIOModuleConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1))
hmIOModConfigCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1))
hmIOModConfigDigInputAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigInputAdminState.setStatus('current')
hmIOModConfigDigOutputAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 2), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputAdminState.setStatus('current')
hmIOModConfigDigInputRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(500, 10000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigInputRefreshInterval.setStatus('current')
hmIOModConfigDigOutputRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(500, 10000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputRefreshInterval.setStatus('current')
hmIOModConfigDigOutputRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputRetryCount.setStatus('current')
hmIOModConfigDigInputTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2), )
if mibBuilder.loadTexts: hmIOModConfigDigInputTable.setStatus('current')
hmIOModConfigDigInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1), ).setIndexNames((0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigInputModID"), (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigInputID"))
if mibBuilder.loadTexts: hmIOModConfigDigInputEntry.setStatus('current')
hmIOModConfigDigInputModID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)))
if mibBuilder.loadTexts: hmIOModConfigDigInputModID.setStatus('current')
hmIOModConfigDigInputID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hmIOModConfigDigInputID.setStatus('current')
hmIOModConfigDigInputLogEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 3), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigInputLogEvent.setStatus('current')
hmIOModConfigDigInputSnmpTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 4), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigInputSnmpTrap.setStatus('current')
hmIOModConfigDigOutputTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3), )
if mibBuilder.loadTexts: hmIOModConfigDigOutputTable.setStatus('current')
hmIOModConfigDigOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1), ).setIndexNames((0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigOutputModID"), (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigOutputID"))
if mibBuilder.loadTexts: hmIOModConfigDigOutputEntry.setStatus('current')
hmIOModConfigDigOutputModID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)))
if mibBuilder.loadTexts: hmIOModConfigDigOutputModID.setStatus('current')
hmIOModConfigDigOutputID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hmIOModConfigDigOutputID.setStatus('current')
hmIOModConfigDigOutputLogEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 3), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputLogEvent.setStatus('current')
hmIOModConfigDigOutputSnmpTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 4), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputSnmpTrap.setStatus('current')
hmIOModConfigDigOutputSourceIP = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 5), IpAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputSourceIP.setStatus('current')
hmIOModConfigDigOutputSourceModID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputSourceModID.setStatus('current')
hmIOModConfigDigOutputSourceID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputSourceID.setStatus('current')
hmIOModConfigDigOutputSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 8), InetPortNumber().clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmIOModConfigDigOutputSourcePort.setStatus('current')
hmIOModuleValueGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2))
hmIOModValueDigInputTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1), )
if mibBuilder.loadTexts: hmIOModValueDigInputTable.setStatus('current')
hmIOModValueDigInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1), ).setIndexNames((0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputModID"), (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputID"))
if mibBuilder.loadTexts: hmIOModValueDigInputEntry.setStatus('current')
hmIOModValueDigInputModID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)))
if mibBuilder.loadTexts: hmIOModValueDigInputModID.setStatus('current')
hmIOModValueDigInputID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hmIOModValueDigInputID.setStatus('current')
hmIOModValueDigInputValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("not-available", 0), ("high", 1), ("low", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmIOModValueDigInputValue.setStatus('current')
hmIOModValueDigOutputTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2), )
if mibBuilder.loadTexts: hmIOModValueDigOutputTable.setStatus('current')
hmIOModValueDigOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1), ).setIndexNames((0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputModID"), (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputID"))
if mibBuilder.loadTexts: hmIOModValueDigOutputEntry.setStatus('current')
hmIOModValueDigOutputModID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)))
if mibBuilder.loadTexts: hmIOModValueDigOutputModID.setStatus('current')
hmIOModValueDigOutputID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hmIOModValueDigOutputID.setStatus('current')
hmIOModValueDigOutputValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("not-available", 0), ("high", 1), ("low", 2), ("invalid", 3), ("not-configured", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmIOModValueDigOutputValue.setStatus('current')
hmIOModDigInputChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 16)).setObjects(("HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputValue"))
if mibBuilder.loadTexts: hmIOModDigInputChangeTrap.setStatus('current')
hmIOModDigOutputChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 17)).setObjects(("HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputValue"))
if mibBuilder.loadTexts: hmIOModDigOutputChangeTrap.setStatus('current')
mibBuilder.exportSymbols("HMIOMODULE-SNMP-MIB", hmIOModConfigDigInputRefreshInterval=hmIOModConfigDigInputRefreshInterval, hmIOModValueDigInputID=hmIOModValueDigInputID, hmIOModConfigDigOutputAdminState=hmIOModConfigDigOutputAdminState, hmIOModValueDigOutputValue=hmIOModValueDigOutputValue, hmIOModConfigDigOutputSnmpTrap=hmIOModConfigDigOutputSnmpTrap, hmIOModConfigDigInputID=hmIOModConfigDigInputID, hmIOModConfigDigOutputSourcePort=hmIOModConfigDigOutputSourcePort, hmIOModConfigCommon=hmIOModConfigCommon, hmIOModValueDigOutputModID=hmIOModValueDigOutputModID, hmIOModConfigDigOutputEntry=hmIOModConfigDigOutputEntry, hmIOModConfigDigOutputSourceID=hmIOModConfigDigOutputSourceID, hmIOModConfigDigInputTable=hmIOModConfigDigInputTable, hmIOModConfigDigInputModID=hmIOModConfigDigInputModID, hmIOModConfigDigOutputModID=hmIOModConfigDigOutputModID, hmIOModuleValueGroup=hmIOModuleValueGroup, hmIOModValueDigInputValue=hmIOModValueDigInputValue, hmIOModConfigDigOutputLogEvent=hmIOModConfigDigOutputLogEvent, hmIOModConfigDigInputEntry=hmIOModConfigDigInputEntry, hmIOModValueDigOutputTable=hmIOModValueDigOutputTable, hmIOModValueDigInputEntry=hmIOModValueDigInputEntry, hmIOModConfigDigInputLogEvent=hmIOModConfigDigInputLogEvent, hmIOModConfigDigOutputTable=hmIOModConfigDigOutputTable, hmIOModConfigDigOutputSourceIP=hmIOModConfigDigOutputSourceIP, hmIOModConfigDigOutputRefreshInterval=hmIOModConfigDigOutputRefreshInterval, hmIOModConfigDigOutputRetryCount=hmIOModConfigDigOutputRetryCount, hmIOModConfigDigInputSnmpTrap=hmIOModConfigDigInputSnmpTrap, hmIOModuleConfigGroup=hmIOModuleConfigGroup, HmEnabledStatus=HmEnabledStatus, hmIOModConfigDigOutputSourceModID=hmIOModConfigDigOutputSourceModID, hmIOModValueDigOutputEntry=hmIOModValueDigOutputEntry, hmIOModValueDigInputTable=hmIOModValueDigInputTable, PYSNMP_MODULE_ID=hmIOModuleGroup, hmIOModConfigDigOutputID=hmIOModConfigDigOutputID, hmIOModConfigDigInputAdminState=hmIOModConfigDigInputAdminState, hmIOModDigInputChangeTrap=hmIOModDigInputChangeTrap, hmIOModDigOutputChangeTrap=hmIOModDigOutputChangeTrap, hmIOModValueDigOutputID=hmIOModValueDigOutputID, hmIOModValueDigInputModID=hmIOModValueDigInputModID, hmIOModuleGroup=hmIOModuleGroup)
