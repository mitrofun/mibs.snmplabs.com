#
# PySNMP MIB module ZHONE-GEN-INTERFACE-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-GEN-INTERFACE-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, TimeTicks, Counter32, MibIdentifier, ObjectIdentity, Gauge32, NotificationType, Integer32, Counter64, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "TimeTicks", "Counter32", "MibIdentifier", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "Counter64", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
zhoneModules, zhoneInterfaceConfig = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneInterfaceConfig")
ZhoneAlarmSeverity, ZhoneRowStatus = mibBuilder.importSymbols("Zhone-TC", "ZhoneAlarmSeverity", "ZhoneRowStatus")
alarmConfigMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1))
alarmConfigMib.setRevisions(('2010-12-07 02:37', '2008-02-26 06:25',))
if mibBuilder.loadTexts: alarmConfigMib.setLastUpdated('201012071714Z')
if mibBuilder.loadTexts: alarmConfigMib.setOrganization('Organization.')
alarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1), )
if mibBuilder.loadTexts: alarmConfigTable.setStatus('current')
alarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: alarmConfigEntry.setStatus('current')
alarmConfigBitRateThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigBitRateThreshold.setStatus('current')
alarmConfigBitRateThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigBitRateThresholdValue.setStatus('current')
alarmConfigBitRateThresholdHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigBitRateThresholdHoldtime.setStatus('current')
alarmConfigStatusTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigStatusTrap.setStatus('current')
alarmConfigAdminUp = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigAdminUp.setStatus('current')
alarmConfigAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 6), ZhoneAlarmSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigAlarmSeverity.setStatus('current')
alarmConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 7), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmConfigRowStatus.setStatus('current')
alarmConfigTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2))
alarmConfigTrapPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0))
if mibBuilder.loadTexts: alarmConfigTrapPrefix.setStatus('current')
zhoneAlarmConfigThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0, 1))
if mibBuilder.loadTexts: zhoneAlarmConfigThresholdTrap.setStatus('current')
zhoneAlarmConfigThresholdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0, 2))
if mibBuilder.loadTexts: zhoneAlarmConfigThresholdClearTrap.setStatus('current')
mibBuilder.exportSymbols("ZHONE-GEN-INTERFACE-CONFIG-MIB", alarmConfigAdminUp=alarmConfigAdminUp, alarmConfigTrapPrefix=alarmConfigTrapPrefix, alarmConfigBitRateThresholdHoldtime=alarmConfigBitRateThresholdHoldtime, alarmConfigEntry=alarmConfigEntry, zhoneAlarmConfigThresholdClearTrap=zhoneAlarmConfigThresholdClearTrap, alarmConfigRowStatus=alarmConfigRowStatus, alarmConfigBitRateThresholdValue=alarmConfigBitRateThresholdValue, alarmConfigTable=alarmConfigTable, PYSNMP_MODULE_ID=alarmConfigMib, alarmConfigAlarmSeverity=alarmConfigAlarmSeverity, alarmConfigTraps=alarmConfigTraps, alarmConfigStatusTrap=alarmConfigStatusTrap, zhoneAlarmConfigThresholdTrap=zhoneAlarmConfigThresholdTrap, alarmConfigMib=alarmConfigMib, alarmConfigBitRateThreshold=alarmConfigBitRateThreshold)
