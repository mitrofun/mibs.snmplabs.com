#
# PySNMP MIB module Wellfleet-FSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-FSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Gauge32, TimeTicks, Unsigned32, MibIdentifier, Bits, IpAddress, NotificationType, Integer32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "IpAddress", "NotificationType", "Integer32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfFileSystemGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfFileSystemGroup")
wfFsBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1))
wfFsVolLastUpdated = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsVolLastUpdated.setStatus('mandatory')
wfFsVols = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsVols.setStatus('mandatory')
wfFsVolTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2), )
if mibBuilder.loadTexts: wfFsVolTable.setStatus('mandatory')
wfFsVolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1), ).setIndexNames((0, "Wellfleet-FSM-MIB", "wfFsVolID"))
if mibBuilder.loadTexts: wfFsVolEntry.setStatus('mandatory')
wfFsVolID = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsVolID.setStatus('mandatory')
wfFsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsSlot.setStatus('mandatory')
wfFsType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dos", 1), ("nvfs", 2), ("unix", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsType.setStatus('mandatory')
wfFsRemoveable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remove", 1), ("fixed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsRemoveable.setStatus('mandatory')
wfFsAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("readonly", 2), ("readwrite", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsAccess.setStatus('mandatory')
wfFsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("corrupt", 2), ("busy", 3), ("present", 4), ("incomplete", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsState.setStatus('mandatory')
wfFsSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsSize.setStatus('mandatory')
wfFsFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsFreeSize.setStatus('mandatory')
wfFsContigFree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsContigFree.setStatus('mandatory')
wfFsNumFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsNumFiles.setStatus('mandatory')
wfFsLastWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsLastWritten.setStatus('mandatory')
wfFsBecameActive = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsBecameActive.setStatus('mandatory')
wfFsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("dir", 1), ("format", 2), ("compact", 3), ("purge", 4), ("partcre", 5), ("partdel", 6), ("noaction", 7))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFsAction.setStatus('mandatory')
wfFsActionArg = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 14), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFsActionArg.setStatus('mandatory')
wfFsPercentDone = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsPercentDone.setStatus('mandatory')
wfFsDirBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3))
wfFsDirEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirEntries.setStatus('mandatory')
wfFsDirLastUpdated = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirLastUpdated.setStatus('mandatory')
wfFsDirTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5), )
if mibBuilder.loadTexts: wfFsDirTable.setStatus('mandatory')
wfFsDirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1), ).setIndexNames((0, "Wellfleet-FSM-MIB", "wfFsDirVolID"), (0, "Wellfleet-FSM-MIB", "wfFsDirFileIndex"))
if mibBuilder.loadTexts: wfFsDirEntry.setStatus('mandatory')
wfFsDirVolID = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirVolID.setStatus('mandatory')
wfFsDirFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirFileIndex.setStatus('mandatory')
wfFsDirFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirFileName.setStatus('mandatory')
wfFsDirCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirCreated.setStatus('mandatory')
wfFsDirFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirFileSize.setStatus('mandatory')
wfFsDirFileMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFsDirFileMask.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-FSM-MIB", wfFsPercentDone=wfFsPercentDone, wfFsDirEntries=wfFsDirEntries, wfFsDirLastUpdated=wfFsDirLastUpdated, wfFsDirFileMask=wfFsDirFileMask, wfFsDirFileName=wfFsDirFileName, wfFsDirCreated=wfFsDirCreated, wfFsState=wfFsState, wfFsLastWritten=wfFsLastWritten, wfFsVolLastUpdated=wfFsVolLastUpdated, wfFsRemoveable=wfFsRemoveable, wfFsVolID=wfFsVolID, wfFsDirFileIndex=wfFsDirFileIndex, wfFsType=wfFsType, wfFsSlot=wfFsSlot, wfFsBecameActive=wfFsBecameActive, wfFsVols=wfFsVols, wfFsFreeSize=wfFsFreeSize, wfFsAccess=wfFsAccess, wfFsActionArg=wfFsActionArg, wfFsVolEntry=wfFsVolEntry, wfFsDirTable=wfFsDirTable, wfFsDirVolID=wfFsDirVolID, wfFsBase=wfFsBase, wfFsDirEntry=wfFsDirEntry, wfFsNumFiles=wfFsNumFiles, wfFsDirFileSize=wfFsDirFileSize, wfFsDirBase=wfFsDirBase, wfFsVolTable=wfFsVolTable, wfFsContigFree=wfFsContigFree, wfFsSize=wfFsSize, wfFsAction=wfFsAction)
