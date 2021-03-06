#
# PySNMP MIB module Wellfleet-COPSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-COPSC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Integer32, Counter32, Bits, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, Counter64, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "Counter32", "Bits", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfCopsCGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfCopsCGroup")
wfCopsCBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1))
wfCopsCDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCDelete.setStatus('mandatory')
wfCopsCDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCDisable.setStatus('mandatory')
wfCopsCState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("localrecovery", 2), ("init", 3), ("down", 4), ("notpresent", 5))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfCopsCState.setStatus('mandatory')
wfCopsCCurrentSlotMask = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfCopsCCurrentSlotMask.setStatus('mandatory')
wfCopsCSoloSlot = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfCopsCSoloSlot.setStatus('mandatory')
wfCopsCSoloSlotMask = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 6), Gauge32().clone(4294705152)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCSoloSlotMask.setStatus('mandatory')
wfCopsCDebugLogFilter = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCDebugLogFilter.setStatus('mandatory')
wfCopsCIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCIPAddr.setStatus('mandatory')
wfCopsCID = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCID.setStatus('mandatory')
wfCopsSvrTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2), )
if mibBuilder.loadTexts: wfCopsSvrTable.setStatus('mandatory')
wfCopsSvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1), ).setIndexNames((0, "Wellfleet-COPSC-MIB", "wfCopsSvrIPAddr"))
if mibBuilder.loadTexts: wfCopsSvrEntry.setStatus('mandatory')
wfCopsSvrDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrDelete.setStatus('mandatory')
wfCopsSvrDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrDisable.setStatus('mandatory')
wfCopsSvrIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfCopsSvrIPAddr.setStatus('mandatory')
wfCopsSvrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 4), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrPriority.setStatus('mandatory')
wfCopsSvrConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("serverready", 1), ("connnegotiation", 2), ("connrecovery", 3), ("servercontacted", 4), ("noconn", 5))).clone('noconn')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfCopsSvrConnState.setStatus('mandatory')
wfCopsSvrConnTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrConnTimer.setStatus('mandatory')
wfCopsSvrConnRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrConnRetryCount.setStatus('mandatory')
wfCopsSvrKeepAliveTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrKeepAliveTimer.setStatus('mandatory')
wfCopsSvrReportTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(360)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrReportTimer.setStatus('mandatory')
wfCopsSvrTCPKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrTCPKeepAliveInterval.setStatus('mandatory')
wfCopsSvrTCPKeepAliveRetryTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrTCPKeepAliveRetryTimeOut.setStatus('mandatory')
wfCopsSvrTCPKeepAliveMaxRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrTCPKeepAliveMaxRetryCount.setStatus('mandatory')
wfCopsSvrRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3288)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsSvrRemotePort.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-COPSC-MIB", wfCopsCState=wfCopsCState, wfCopsCIPAddr=wfCopsCIPAddr, wfCopsSvrDisable=wfCopsSvrDisable, wfCopsCID=wfCopsCID, wfCopsSvrConnTimer=wfCopsSvrConnTimer, wfCopsSvrPriority=wfCopsSvrPriority, wfCopsCDisable=wfCopsCDisable, wfCopsCCurrentSlotMask=wfCopsCCurrentSlotMask, wfCopsSvrTCPKeepAliveInterval=wfCopsSvrTCPKeepAliveInterval, wfCopsSvrEntry=wfCopsSvrEntry, wfCopsSvrIPAddr=wfCopsSvrIPAddr, wfCopsSvrConnRetryCount=wfCopsSvrConnRetryCount, wfCopsSvrTCPKeepAliveRetryTimeOut=wfCopsSvrTCPKeepAliveRetryTimeOut, wfCopsCSoloSlot=wfCopsCSoloSlot, wfCopsSvrTable=wfCopsSvrTable, wfCopsCDelete=wfCopsCDelete, wfCopsSvrRemotePort=wfCopsSvrRemotePort, wfCopsCBase=wfCopsCBase, wfCopsSvrKeepAliveTimer=wfCopsSvrKeepAliveTimer, wfCopsSvrDelete=wfCopsSvrDelete, wfCopsSvrConnState=wfCopsSvrConnState, wfCopsCSoloSlotMask=wfCopsCSoloSlotMask, wfCopsSvrReportTimer=wfCopsSvrReportTimer, wfCopsCDebugLogFilter=wfCopsCDebugLogFilter, wfCopsSvrTCPKeepAliveMaxRetryCount=wfCopsSvrTCPKeepAliveMaxRetryCount)
