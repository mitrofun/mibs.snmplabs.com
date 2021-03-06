#
# PySNMP MIB module ChrComIfOpticsOTS-SNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComIfOpticsOTS-SNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
chrComIfOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComIfOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Unsigned32, Counter64, Gauge32, ObjectIdentity, Integer32, iso, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Unsigned32", "Counter64", "Gauge32", "ObjectIdentity", "Integer32", "iso", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComIfOpticsOTS_SNKTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1), ).setLabel("chrComIfOpticsOTS-SNKTable")
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKTable.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKTable.setDescription('1. The OTS-SNK is managed only for the Ring side of the Metropolis Network (not for the Trib side). 2. When pre-OPA exists, the following ADOM/OMDM does NOT have an OTS-SNK layer \x13 This layer should be grayed and not accessible to the user. ')
chrComIfOpticsOTS_SNKEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1), ).setLabel("chrComIfOpticsOTS-SNKEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKEntry.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKEntry.setDescription('')
chrComIfOpticsOtsSnkInPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkInPower.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkInPower.setDescription('Total Optical Power Monitored at the input of ADOM/OMDM/pre-OPA/in-line-OPA.')
chrComIfOpticsOtsSnkLOOPThr = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkLOOPThr.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkLOOPThr.setDescription('This is a threshold on OTS-SNK total input Power . ')
chrComIfOpticsAlarmVector = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsAlarmVector.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsAlarmVector.setDescription('')
chrComIfOpticsAlarmSeverityProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsAlarmSeverityProfileIndex.setStatus('current')
if mibBuilder.loadTexts: chrComIfOpticsAlarmSeverityProfileIndex.setDescription('')
mibBuilder.exportSymbols("ChrComIfOpticsOTS-SNK-MIB", chrComIfOpticsOtsSnkInPower=chrComIfOpticsOtsSnkInPower, chrComIfOpticsOTS_SNKTable=chrComIfOpticsOTS_SNKTable, chrComIfOpticsOtsSnkLOOPThr=chrComIfOpticsOtsSnkLOOPThr, chrComIfOpticsAlarmSeverityProfileIndex=chrComIfOpticsAlarmSeverityProfileIndex, chrComIfOpticsOTS_SNKEntry=chrComIfOpticsOTS_SNKEntry, chrComIfOpticsAlarmVector=chrComIfOpticsAlarmVector)
