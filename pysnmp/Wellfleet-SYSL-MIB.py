#
# PySNMP MIB module Wellfleet-SYSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-SYSL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, TimeTicks, iso, MibIdentifier, Gauge32, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "TimeTicks", "iso", "MibIdentifier", "Gauge32", "Counter32", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfSyslogGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSyslogGroup")
wfSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1))
wfSyslogDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogDelete.setStatus('mandatory')
wfSyslogDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogDisable.setStatus('mandatory')
wfSyslogOperState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogOperState.setStatus('mandatory')
wfSyslogMaxHosts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogMaxHosts.setStatus('mandatory')
wfSyslogPollTimer = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 610000)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogPollTimer.setStatus('mandatory')
wfSyslogActTimeSeqHosts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogActTimeSeqHosts.setStatus('mandatory')
wfSyslogActNonSeqHosts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogActNonSeqHosts.setStatus('mandatory')
wfSyslogTotalMsgFwds = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogTotalMsgFwds.setStatus('mandatory')
wfSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2), )
if mibBuilder.loadTexts: wfSyslogHostTable.setStatus('mandatory')
wfSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1), ).setIndexNames((0, "Wellfleet-SYSL-MIB", "wfSyslogHostDest"))
if mibBuilder.loadTexts: wfSyslogHostEntry.setStatus('mandatory')
wfSyslogHostDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogHostDelete.setStatus('mandatory')
wfSyslogHostDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogHostDisable.setStatus('mandatory')
wfSyslogHostDest = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogHostDest.setStatus('mandatory')
wfSyslogHostUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 4), Integer32().clone(514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogHostUDPPort.setStatus('mandatory')
wfSyslogHostLogFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(128, 136, 144, 152, 160, 168, 176, 184))).clone(namedValues=NamedValues(("local0", 128), ("local1", 136), ("local2", 144), ("local3", 152), ("local4", 160), ("local5", 168), ("local6", 176), ("local7", 184))).clone('local7')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogHostLogFacility.setStatus('mandatory')
wfSyslogHostTimeSeqEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogHostTimeSeqEnable.setStatus('mandatory')
wfSyslogHostOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogHostOperState.setStatus('mandatory')
wfSyslogHostMsgFwds = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogHostMsgFwds.setStatus('mandatory')
wfSyslogEntityFilterTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3), )
if mibBuilder.loadTexts: wfSyslogEntityFilterTable.setStatus('mandatory')
wfSyslogEntFltrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1), ).setIndexNames((0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrHostIndex"), (0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrNum"), (0, "Wellfleet-SYSL-MIB", "wfSyslogEntFltrIndex"))
if mibBuilder.loadTexts: wfSyslogEntFltrEntry.setStatus('mandatory')
wfSyslogEntFltrDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrDelete.setStatus('mandatory')
wfSyslogEntFltrDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrDisable.setStatus('mandatory')
wfSyslogEntFltrHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogEntFltrHostIndex.setStatus('mandatory')
wfSyslogEntFltrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogEntFltrNum.setStatus('mandatory')
wfSyslogEntFltrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogEntFltrIndex.setStatus('mandatory')
wfSyslogEntFltrOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSyslogEntFltrOperState.setStatus('mandatory')
wfSyslogEntFltrLogEvtLowBnd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrLogEvtLowBnd.setStatus('mandatory')
wfSyslogEntFltrLogEvtUppBnd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 8), Integer32().clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrLogEvtUppBnd.setStatus('mandatory')
wfSyslogEntFltrSevMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrSevMask.setStatus('mandatory')
wfSyslogEntFltrSlotLowBnd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrSlotLowBnd.setStatus('mandatory')
wfSyslogEntFltrSlotUppBnd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrSlotUppBnd.setStatus('mandatory')
wfSyslogEntFltrFaultMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('crit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrFaultMap.setStatus('mandatory')
wfSyslogEntFltrWarningMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrWarningMap.setStatus('mandatory')
wfSyslogEntFltrInfoMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrInfoMap.setStatus('mandatory')
wfSyslogEntFltrTraceMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('debug')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrTraceMap.setStatus('mandatory')
wfSyslogEntFltrDebugMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emerg", 1), ("alert", 2), ("crit", 3), ("err", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('debug')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrDebugMap.setStatus('mandatory')
wfSyslogEntFltrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15, 3, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSyslogEntFltrName.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-SYSL-MIB", wfSyslogHostLogFacility=wfSyslogHostLogFacility, wfSyslogEntFltrWarningMap=wfSyslogEntFltrWarningMap, wfSyslogEntFltrInfoMap=wfSyslogEntFltrInfoMap, wfSyslogTotalMsgFwds=wfSyslogTotalMsgFwds, wfSyslogHostUDPPort=wfSyslogHostUDPPort, wfSyslogEntFltrIndex=wfSyslogEntFltrIndex, wfSyslogEntFltrLogEvtUppBnd=wfSyslogEntFltrLogEvtUppBnd, wfSyslogEntFltrSlotUppBnd=wfSyslogEntFltrSlotUppBnd, wfSyslogEntFltrTraceMap=wfSyslogEntFltrTraceMap, wfSyslogHostEntry=wfSyslogHostEntry, wfSyslogHostTimeSeqEnable=wfSyslogHostTimeSeqEnable, wfSyslogHostOperState=wfSyslogHostOperState, wfSyslogMaxHosts=wfSyslogMaxHosts, wfSyslogDisable=wfSyslogDisable, wfSyslogEntFltrDebugMap=wfSyslogEntFltrDebugMap, wfSyslogEntFltrSevMask=wfSyslogEntFltrSevMask, wfSyslogEntFltrOperState=wfSyslogEntFltrOperState, wfSyslogActNonSeqHosts=wfSyslogActNonSeqHosts, wfSyslogHostDelete=wfSyslogHostDelete, wfSyslogEntFltrNum=wfSyslogEntFltrNum, wfSyslogHostTable=wfSyslogHostTable, wfSyslogHostMsgFwds=wfSyslogHostMsgFwds, wfSyslogDelete=wfSyslogDelete, wfSyslogEntFltrDelete=wfSyslogEntFltrDelete, wfSyslogEntFltrLogEvtLowBnd=wfSyslogEntFltrLogEvtLowBnd, wfSyslogHostDest=wfSyslogHostDest, wfSyslogEntFltrName=wfSyslogEntFltrName, wfSyslogEntFltrSlotLowBnd=wfSyslogEntFltrSlotLowBnd, wfSyslogPollTimer=wfSyslogPollTimer, wfSyslog=wfSyslog, wfSyslogEntityFilterTable=wfSyslogEntityFilterTable, wfSyslogEntFltrEntry=wfSyslogEntFltrEntry, wfSyslogOperState=wfSyslogOperState, wfSyslogEntFltrDisable=wfSyslogEntFltrDisable, wfSyslogEntFltrFaultMap=wfSyslogEntFltrFaultMap, wfSyslogHostDisable=wfSyslogHostDisable, wfSyslogEntFltrHostIndex=wfSyslogEntFltrHostIndex, wfSyslogActTimeSeqHosts=wfSyslogActTimeSeqHosts)