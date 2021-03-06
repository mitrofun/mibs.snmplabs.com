#
# PySNMP MIB module HPN-ICF-FC-PSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FC-PSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
HpnicfFcNameIdOrZero, = mibBuilder.importSymbols("HPN-ICF-FC-TC-MIB", "HpnicfFcNameIdOrZero")
hpnicfSan, = mibBuilder.importSymbols("HPN-ICF-VSAN-MIB", "hpnicfSan")
InterfaceIndexOrZero, InterfaceIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, IpAddress, ModuleIdentity, Counter64, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "IpAddress", "ModuleIdentity", "Counter64", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Integer32", "Bits")
TextualConvention, TimeStamp, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "RowStatus", "TruthValue")
hpnicfFcPsm = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8))
hpnicfFcPsm.setRevisions(('2013-10-17 00:00',))
if mibBuilder.loadTexts: hpnicfFcPsm.setLastUpdated('201310170000Z')
if mibBuilder.loadTexts: hpnicfFcPsm.setOrganization('')
hpnicfFcPsmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0))
hpnicfFcPsmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1))
hpnicfFcPsmScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 1))
hpnicfFcPsmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2))
hpnicfFcPsmStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3))
class HpnicfFcPsmPortBindDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nWWN", 1), ("pWWN", 2), ("sWWN", 3), ("wildCard", 4))

class HpnicfFcPsmClearEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clearStatic", 1), ("clearAutoLearn", 2), ("clearAll", 3), ("noop", 4))

hpnicfFcPsmNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmNotifyEnable.setStatus('current')
hpnicfFcPsmEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfFcPsmEnableTable.setStatus('current')
hpnicfFcPsmEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmEnableEntry.setStatus('current')
hpnicfFcPsmEnableVsanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: hpnicfFcPsmEnableVsanIndex.setStatus('current')
hpnicfFcPsmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("enableWithAutoLearn", 2), ("disable", 3), ("noop", 4))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmEnable.setStatus('current')
hpnicfFcPsmEnableState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmEnableState.setStatus('current')
hpnicfFcPsmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2), )
if mibBuilder.loadTexts: hpnicfFcPsmConfigTable.setStatus('current')
hpnicfFcPsmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"), (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmConfigEntry.setStatus('current')
hpnicfFcPsmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768)))
if mibBuilder.loadTexts: hpnicfFcPsmIndex.setStatus('current')
hpnicfFcPsmLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 2), HpnicfFcPsmPortBindDevType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFcPsmLoginDevType.setStatus('current')
hpnicfFcPsmLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 3), HpnicfFcNameIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFcPsmLoginDev.setStatus('current')
hpnicfFcPsmLoginPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFcPsmLoginPoint.setStatus('current')
hpnicfFcPsmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFcPsmRowStatus.setStatus('current')
hpnicfFcPsmEnfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3), )
if mibBuilder.loadTexts: hpnicfFcPsmEnfTable.setStatus('current')
hpnicfFcPsmEnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"), (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnfIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmEnfEntry.setStatus('current')
hpnicfFcPsmEnfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768)))
if mibBuilder.loadTexts: hpnicfFcPsmEnfIndex.setStatus('current')
hpnicfFcPsmEnfLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 2), HpnicfFcPsmPortBindDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmEnfLoginDevType.setStatus('current')
hpnicfFcPsmEnfLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 3), HpnicfFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmEnfLoginDev.setStatus('current')
hpnicfFcPsmEnfLoginPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmEnfLoginPoint.setStatus('current')
hpnicfFcPsmEnfEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("learning", 1), ("learnt", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmEnfEntryType.setStatus('current')
hpnicfFcPsmCopyToConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4), )
if mibBuilder.loadTexts: hpnicfFcPsmCopyToConfigTable.setStatus('current')
hpnicfFcPsmCopyToConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmCopyToConfigEntry.setStatus('current')
hpnicfFcPsmCopyToConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copy", 1), ("noop", 2))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmCopyToConfig.setStatus('current')
hpnicfFcPsmAutoLearnTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5), )
if mibBuilder.loadTexts: hpnicfFcPsmAutoLearnTable.setStatus('current')
hpnicfFcPsmAutoLearnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmAutoLearnEntry.setStatus('current')
hpnicfFcPsmAutoLearnEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmAutoLearnEnable.setStatus('current')
hpnicfFcPsmClearTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6), )
if mibBuilder.loadTexts: hpnicfFcPsmClearTable.setStatus('current')
hpnicfFcPsmClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmClearEntry.setStatus('current')
hpnicfFcPsmClearType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1, 1), HpnicfFcPsmClearEntryType().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmClearType.setStatus('current')
hpnicfFcPsmClearIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmClearIntf.setStatus('current')
hpnicfFcPsmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1), )
if mibBuilder.loadTexts: hpnicfFcPsmStatsTable.setStatus('current')
hpnicfFcPsmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmStatsEntry.setStatus('current')
hpnicfFcPsmAllowedLogins = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmAllowedLogins.setStatus('current')
hpnicfFcPsmDeniedLogins = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmDeniedLogins.setStatus('current')
hpnicfFcPsmStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noop", 2))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcPsmStatsClear.setStatus('current')
hpnicfFcPsmViolationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2), )
if mibBuilder.loadTexts: hpnicfFcPsmViolationTable.setStatus('current')
hpnicfFcPsmViolationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"), (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmViolationIndex"))
if mibBuilder.loadTexts: hpnicfFcPsmViolationEntry.setStatus('current')
hpnicfFcPsmViolationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: hpnicfFcPsmViolationIndex.setStatus('current')
hpnicfFcPsmLoginPWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 2), HpnicfFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginPWWN.setStatus('current')
hpnicfFcPsmLoginNWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 3), HpnicfFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginNWWN.setStatus('current')
hpnicfFcPsmLoginSWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 4), HpnicfFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginSWWN.setStatus('current')
hpnicfFcPsmLoginIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginIntf.setStatus('current')
hpnicfFcPsmLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginTime.setStatus('current')
hpnicfFcPsmLoginCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcPsmLoginCount.setStatus('current')
hpnicfFcPsmFPortDenyNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginPWWN"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginIntf"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginTime"))
if mibBuilder.loadTexts: hpnicfFcPsmFPortDenyNotify.setStatus('current')
hpnicfFcPsmEPortDenyNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginSWWN"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginIntf"), ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginTime"))
if mibBuilder.loadTexts: hpnicfFcPsmEPortDenyNotify.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FC-PSM-MIB", hpnicfFcPsmLoginTime=hpnicfFcPsmLoginTime, hpnicfFcPsmNotifications=hpnicfFcPsmNotifications, hpnicfFcPsmAllowedLogins=hpnicfFcPsmAllowedLogins, hpnicfFcPsmStatsTable=hpnicfFcPsmStatsTable, hpnicfFcPsmLoginSWWN=hpnicfFcPsmLoginSWWN, hpnicfFcPsmEnfIndex=hpnicfFcPsmEnfIndex, hpnicfFcPsmConfiguration=hpnicfFcPsmConfiguration, hpnicfFcPsmFPortDenyNotify=hpnicfFcPsmFPortDenyNotify, hpnicfFcPsmCopyToConfigTable=hpnicfFcPsmCopyToConfigTable, hpnicfFcPsmEnfLoginPoint=hpnicfFcPsmEnfLoginPoint, hpnicfFcPsm=hpnicfFcPsm, hpnicfFcPsmEnableEntry=hpnicfFcPsmEnableEntry, hpnicfFcPsmLoginDev=hpnicfFcPsmLoginDev, HpnicfFcPsmPortBindDevType=HpnicfFcPsmPortBindDevType, hpnicfFcPsmLoginDevType=hpnicfFcPsmLoginDevType, hpnicfFcPsmEnableTable=hpnicfFcPsmEnableTable, hpnicfFcPsmEnfEntry=hpnicfFcPsmEnfEntry, hpnicfFcPsmNotifyEnable=hpnicfFcPsmNotifyEnable, hpnicfFcPsmRowStatus=hpnicfFcPsmRowStatus, hpnicfFcPsmEnfLoginDevType=hpnicfFcPsmEnfLoginDevType, hpnicfFcPsmStatsClear=hpnicfFcPsmStatsClear, hpnicfFcPsmEnableVsanIndex=hpnicfFcPsmEnableVsanIndex, hpnicfFcPsmClearEntry=hpnicfFcPsmClearEntry, hpnicfFcPsmStats=hpnicfFcPsmStats, hpnicfFcPsmLoginIntf=hpnicfFcPsmLoginIntf, hpnicfFcPsmEnable=hpnicfFcPsmEnable, hpnicfFcPsmStatsEntry=hpnicfFcPsmStatsEntry, hpnicfFcPsmAutoLearnEnable=hpnicfFcPsmAutoLearnEnable, hpnicfFcPsmViolationEntry=hpnicfFcPsmViolationEntry, hpnicfFcPsmScalarObjects=hpnicfFcPsmScalarObjects, hpnicfFcPsmObjects=hpnicfFcPsmObjects, hpnicfFcPsmViolationTable=hpnicfFcPsmViolationTable, hpnicfFcPsmEPortDenyNotify=hpnicfFcPsmEPortDenyNotify, hpnicfFcPsmConfigEntry=hpnicfFcPsmConfigEntry, HpnicfFcPsmClearEntryType=HpnicfFcPsmClearEntryType, hpnicfFcPsmLoginPoint=hpnicfFcPsmLoginPoint, hpnicfFcPsmClearIntf=hpnicfFcPsmClearIntf, hpnicfFcPsmClearTable=hpnicfFcPsmClearTable, hpnicfFcPsmEnfTable=hpnicfFcPsmEnfTable, hpnicfFcPsmAutoLearnTable=hpnicfFcPsmAutoLearnTable, hpnicfFcPsmLoginNWWN=hpnicfFcPsmLoginNWWN, hpnicfFcPsmIndex=hpnicfFcPsmIndex, hpnicfFcPsmCopyToConfigEntry=hpnicfFcPsmCopyToConfigEntry, hpnicfFcPsmLoginCount=hpnicfFcPsmLoginCount, hpnicfFcPsmConfigTable=hpnicfFcPsmConfigTable, hpnicfFcPsmAutoLearnEntry=hpnicfFcPsmAutoLearnEntry, hpnicfFcPsmClearType=hpnicfFcPsmClearType, PYSNMP_MODULE_ID=hpnicfFcPsm, hpnicfFcPsmDeniedLogins=hpnicfFcPsmDeniedLogins, hpnicfFcPsmEnableState=hpnicfFcPsmEnableState, hpnicfFcPsmEnfLoginDev=hpnicfFcPsmEnfLoginDev, hpnicfFcPsmViolationIndex=hpnicfFcPsmViolationIndex, hpnicfFcPsmCopyToConfig=hpnicfFcPsmCopyToConfig, hpnicfFcPsmLoginPWWN=hpnicfFcPsmLoginPWWN, hpnicfFcPsmEnfEntryType=hpnicfFcPsmEnfEntryType)
