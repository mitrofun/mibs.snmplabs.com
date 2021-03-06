#
# PySNMP MIB module Spool-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Spool-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Counter32, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, Gauge32, iso, enterprises, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "iso", "enterprises", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
sniProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2))
sniSpool = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12))
sniSpoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1))
sniSpoolDevTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1))
sniSpoolSrvTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2))
sniSpoolSpvTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3))
sniSpoolDgrTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4))
sniSpoolHostTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5))
sniSpoolJobTable = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6))
spoolDevTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevTabNum.setStatus('mandatory')
spoolDevTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2), )
if mibBuilder.loadTexts: spoolDevTab.setStatus('mandatory')
spoolDevTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolDevTabIndex"))
if mibBuilder.loadTexts: spoolDevTabEntry.setStatus('mandatory')
spoolDevTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevTabIndex.setStatus('mandatory')
spoolDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevName.setStatus('mandatory')
spoolDevState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("error", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolDevState.setStatus('mandatory')
spoolDevSpoolin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolDevSpoolin.setStatus('mandatory')
spoolDevSpoolout = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolDevSpoolout.setStatus('mandatory')
spoolDevErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevErrorMsg.setStatus('mandatory')
spoolDevStaDate = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevStaDate.setStatus('mandatory')
spoolDevPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevPriority.setStatus('mandatory')
spoolDevWaitingJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevWaitingJobs.setStatus('mandatory')
spoolDevCurForm = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevCurForm.setStatus('mandatory')
spoolDevActJid = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevActJid.setStatus('mandatory')
spoolDevHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevHost.setStatus('mandatory')
spoolDevAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevAdmin.setStatus('mandatory')
spoolDevPcl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevPcl.setStatus('mandatory')
spoolDevDftForm = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevDftForm.setStatus('mandatory')
spoolDevSupervisor = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevSupervisor.setStatus('mandatory')
spoolDevAdmComment = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolDevAdmComment.setStatus('mandatory')
spoolDevUsrComment = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDevUsrComment.setStatus('mandatory')
spoolDevEnablePoll = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolDevEnablePoll.setStatus('mandatory')
spoolSrvTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvTabNum.setStatus('mandatory')
spoolSrvTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2), )
if mibBuilder.loadTexts: spoolSrvTab.setStatus('mandatory')
spoolSrvTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolSrvTabIndex"))
if mibBuilder.loadTexts: spoolSrvTabEntry.setStatus('mandatory')
spoolSrvTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvTabIndex.setStatus('mandatory')
spoolSrvName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvName.setStatus('mandatory')
spoolSrvAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvAdmin.setStatus('mandatory')
spoolSrvHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvHost.setStatus('mandatory')
spoolSrvSchedPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvSchedPolicy.setStatus('mandatory')
spoolSrvState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvState.setStatus('mandatory')
spoolSrvSpoolin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvSpoolin.setStatus('mandatory')
spoolSrvSpoolout = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvSpoolout.setStatus('mandatory')
spoolSrvLoadLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvLoadLevel.setStatus('mandatory')
spoolSrvMaxJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 4294967296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvMaxJobs.setStatus('mandatory')
spoolSrvWaitingJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSrvWaitingJobs.setStatus('mandatory')
spoolSpvTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvTabNum.setStatus('mandatory')
spoolSpvTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2), )
if mibBuilder.loadTexts: spoolSpvTab.setStatus('mandatory')
spoolSpvTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolSpvTabIndex"))
if mibBuilder.loadTexts: spoolSpvTabEntry.setStatus('mandatory')
spoolSpvTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvTabIndex.setStatus('mandatory')
spoolSpvName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvName.setStatus('mandatory')
spoolSpvServName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvServName.setStatus('mandatory')
spoolSpvAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvAdmin.setStatus('mandatory')
spoolSpvHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvHost.setStatus('mandatory')
spoolSpvState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolSpvState.setStatus('mandatory')
spoolDgrTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrTabNum.setStatus('mandatory')
spoolDgrTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2), )
if mibBuilder.loadTexts: spoolDgrTab.setStatus('mandatory')
spoolDgrTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolDgrTabIndex"))
if mibBuilder.loadTexts: spoolDgrTabEntry.setStatus('mandatory')
spoolDgrTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrTabIndex.setStatus('mandatory')
spoolDgrName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrName.setStatus('mandatory')
spoolDgrAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrAdmin.setStatus('mandatory')
spoolDgrDeviceList = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrDeviceList.setStatus('mandatory')
spoolDgrSpoolin = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrSpoolin.setStatus('mandatory')
spoolDgrDate = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrDate.setStatus('mandatory')
spoolDgrComment = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolDgrComment.setStatus('mandatory')
spoolHostTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostTabNum.setStatus('mandatory')
spoolHostTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2), )
if mibBuilder.loadTexts: spoolHostTab.setStatus('mandatory')
spoolHostTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolHostTabIndex"))
if mibBuilder.loadTexts: spoolHostTabEntry.setStatus('mandatory')
spoolHostTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostTabIndex.setStatus('mandatory')
spoolHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostName.setStatus('mandatory')
spoolHostDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostDestination.setStatus('mandatory')
spoolHostSuppHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostSuppHost.setStatus('mandatory')
spoolHostResponsibility = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("potmaster", 1), ("slave", 2), ("parasite", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostResponsibility.setStatus('mandatory')
spoolHostState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("activemaster", 2), ("inactive", 3), ("shutdown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolHostState.setStatus('mandatory')
spoolJobTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobTabNum.setStatus('mandatory')
spoolJobTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2), )
if mibBuilder.loadTexts: spoolJobTab.setStatus('mandatory')
spoolJobTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1), ).setIndexNames((0, "Spool-MIB", "spoolJobTabIndex"))
if mibBuilder.loadTexts: spoolJobTabEntry.setStatus('mandatory')
spoolJobTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobTabIndex.setStatus('mandatory')
spoolJobGlobalJid = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobGlobalJid.setStatus('mandatory')
spoolJobLocalJid = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobLocalJid.setStatus('mandatory')
spoolJobTitle = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobTitle.setStatus('mandatory')
spoolJobComment = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobComment.setStatus('mandatory')
spoolJobOriginator = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobOriginator.setStatus('mandatory')
spoolJobOrigHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobOrigHost.setStatus('mandatory')
spoolJobOrigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobOrigTime.setStatus('mandatory')
spoolJobDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolJobDestination.setStatus('mandatory')
spoolJobPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolJobPriority.setStatus('mandatory')
spoolJobSecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unclassified", 1), ("sensitive", 2), ("confidential", 3), ("secret", 4), ("topsecret", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobSecurityLevel.setStatus('mandatory')
spoolJobFileList = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobFileList.setStatus('mandatory')
spoolJobTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobTotalSize.setStatus('mandatory')
spoolJobRawMode = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobRawMode.setStatus('mandatory')
spoolJobStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobStartTime.setStatus('mandatory')
spoolJobDelTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobDelTime.setStatus('mandatory')
spoolJobRetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 4294967296))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobRetTime.setStatus('mandatory')
spoolJobDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobDevName.setStatus('mandatory')
spoolJobState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("active", 1), ("wait", 2), ("suspend", 3), ("top", 4), ("data-filtering", 5), ("file-transfer", 6), ("error", 7), ("terminated", 8), ("interrupted", 9), ("cancel", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spoolJobState.setStatus('mandatory')
spoolJobErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobErrorMsg.setStatus('mandatory')
spoolJobRank = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobRank.setStatus('mandatory')
spoolJobRqCopies = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobRqCopies.setStatus('mandatory')
spoolJobPrCopies = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobPrCopies.setStatus('mandatory')
spoolJobPrPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spoolJobPrPercent.setStatus('mandatory')
mibBuilder.exportSymbols("Spool-MIB", spoolSrvHost=spoolSrvHost, spoolJobTabEntry=spoolJobTabEntry, spoolDgrTabIndex=spoolDgrTabIndex, spoolJobComment=spoolJobComment, spoolSrvTabIndex=spoolSrvTabIndex, spoolJobGlobalJid=spoolJobGlobalJid, spoolJobOrigHost=spoolJobOrigHost, spoolJobOriginator=spoolJobOriginator, spoolDgrTab=spoolDgrTab, spoolDgrAdmin=spoolDgrAdmin, spoolDevName=spoolDevName, spoolSrvAdmin=spoolSrvAdmin, spoolSrvName=spoolSrvName, spoolDgrTabEntry=spoolDgrTabEntry, spoolDevStaDate=spoolDevStaDate, spoolHostResponsibility=spoolHostResponsibility, spoolDevActJid=spoolDevActJid, spoolDevAdmComment=spoolDevAdmComment, spoolJobRawMode=spoolJobRawMode, spoolDevTabNum=spoolDevTabNum, spoolSrvSpoolin=spoolSrvSpoolin, spoolJobRank=spoolJobRank, spoolSpvAdmin=spoolSpvAdmin, spoolJobDevName=spoolJobDevName, spoolDevEnablePoll=spoolDevEnablePoll, spoolDevPriority=spoolDevPriority, spoolJobStartTime=spoolJobStartTime, spoolSrvSpoolout=spoolSrvSpoolout, spoolDevTabIndex=spoolDevTabIndex, spoolHostTabIndex=spoolHostTabIndex, spoolDevSupervisor=spoolDevSupervisor, spoolJobRetTime=spoolJobRetTime, spoolJobDelTime=spoolJobDelTime, spoolSrvLoadLevel=spoolSrvLoadLevel, sniSpoolDevTable=sniSpoolDevTable, spoolJobTabNum=spoolJobTabNum, spoolJobPrCopies=spoolJobPrCopies, spoolJobTitle=spoolJobTitle, spoolDgrDeviceList=spoolDgrDeviceList, spoolDgrSpoolin=spoolDgrSpoolin, spoolDevState=spoolDevState, spoolJobPrPercent=spoolJobPrPercent, spoolSpvTabNum=spoolSpvTabNum, sniSpoolHostTable=sniSpoolHostTable, spoolSpvTabEntry=spoolSpvTabEntry, spoolDevWaitingJobs=spoolDevWaitingJobs, spoolJobErrorMsg=spoolJobErrorMsg, spoolDevHost=spoolDevHost, sniSpool=sniSpool, spoolHostTab=spoolHostTab, spoolHostState=spoolHostState, spoolDgrComment=spoolDgrComment, spoolSpvServName=spoolSpvServName, spoolSpvState=spoolSpvState, spoolHostSuppHost=spoolHostSuppHost, spoolDgrName=spoolDgrName, spoolDgrTabNum=spoolDgrTabNum, sniSpoolSpvTable=sniSpoolSpvTable, spoolDgrDate=spoolDgrDate, sni=sni, spoolDevSpoolin=spoolDevSpoolin, spoolJobTabIndex=spoolJobTabIndex, spoolDevUsrComment=spoolDevUsrComment, spoolHostDestination=spoolHostDestination, spoolJobState=spoolJobState, spoolJobRqCopies=spoolJobRqCopies, spoolSrvTabEntry=spoolSrvTabEntry, spoolJobTotalSize=spoolJobTotalSize, spoolSpvHost=spoolSpvHost, spoolSrvSchedPolicy=spoolSrvSchedPolicy, spoolHostTabNum=spoolHostTabNum, spoolSrvState=spoolSrvState, spoolJobTab=spoolJobTab, spoolSpvTab=spoolSpvTab, spoolDevCurForm=spoolDevCurForm, spoolSpvTabIndex=spoolSpvTabIndex, spoolHostName=spoolHostName, spoolSrvTabNum=spoolSrvTabNum, spoolSpvName=spoolSpvName, spoolDevDftForm=spoolDevDftForm, spoolJobOrigTime=spoolJobOrigTime, spoolJobLocalJid=spoolJobLocalJid, spoolSrvMaxJobs=spoolSrvMaxJobs, sniSpoolJobTable=sniSpoolJobTable, spoolJobDestination=spoolJobDestination, sniSpoolObjects=sniSpoolObjects, spoolSrvTab=spoolSrvTab, spoolJobPriority=spoolJobPriority, sniProductMibs=sniProductMibs, spoolDevTab=spoolDevTab, spoolDevErrorMsg=spoolDevErrorMsg, spoolSrvWaitingJobs=spoolSrvWaitingJobs, spoolJobSecurityLevel=spoolJobSecurityLevel, spoolJobFileList=spoolJobFileList, sniSpoolSrvTable=sniSpoolSrvTable, spoolDevSpoolout=spoolDevSpoolout, spoolDevTabEntry=spoolDevTabEntry, spoolDevAdmin=spoolDevAdmin, sniSpoolDgrTable=sniSpoolDgrTable, spoolDevPcl=spoolDevPcl, spoolHostTabEntry=spoolHostTabEntry)
