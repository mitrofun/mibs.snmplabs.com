#
# PySNMP MIB module CISCO-OPTICAL-PATCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-PATCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, MibIdentifier, TimeTicks, iso, Unsigned32, Counter32, ObjectIdentity, Gauge32, NotificationType, ModuleIdentity, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "Gauge32", "NotificationType", "ModuleIdentity", "Counter64", "IpAddress")
TimeStamp, TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ciscoOpticalPatchMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 67))
ciscoOpticalPatchMIB.setRevisions(('2002-03-18 00:00', '2001-09-05 00:00',))
if mibBuilder.loadTexts: ciscoOpticalPatchMIB.setLastUpdated('200203180000Z')
if mibBuilder.loadTexts: ciscoOpticalPatchMIB.setOrganization('Cisco Systems, Inc.')
cOPatchMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 67, 1))
cOPatchInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1), )
if mibBuilder.loadTexts: cOPatchInterfaceTable.setStatus('deprecated')
cOPatchInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cOPatchInterfaceEntry.setStatus('deprecated')
cOPatchIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483547))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchIdentifier.setStatus('deprecated')
cOPatchIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchIndexNext.setStatus('current')
cOPatchLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchLastChange.setStatus('current')
cOPatchEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("create", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchEventType.setStatus('current')
cOPatchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5), )
if mibBuilder.loadTexts: cOPatchTable.setStatus('current')
cOPatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1), ).setIndexNames((0, "CISCO-OPTICAL-PATCH-MIB", "cOPatchIndex"))
if mibBuilder.loadTexts: cOPatchEntry.setStatus('current')
cOPatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cOPatchIndex.setStatus('current')
cOPatchLowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cOPatchLowIfIndex.setStatus('current')
cOPatchHighIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cOPatchHighIfIndex.setStatus('current')
cOPatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("provisioned", 1), ("automatic", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchType.setStatus('current')
cOPatchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noError", 1), ("otherError", 2), ("interfaceError", 3), ("interfaceChannelError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchStatus.setStatus('current')
cOPatchCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchCreationTime.setStatus('current')
cOPatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cOPatchRowStatus.setStatus('current')
cOPatchDirOnLowIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lowIfDirReceive", 1), ("lowIfDirTransmit", 2), ("lowIfDirBoth", 3))).clone('lowIfDirBoth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cOPatchDirOnLowIf.setStatus('current')
cOPatchEventEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOPatchEventEnabled.setStatus('current')
cOPatchIntfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7), )
if mibBuilder.loadTexts: cOPatchIntfTable.setStatus('current')
cOPatchIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfDirection"))
if mibBuilder.loadTexts: cOPatchIntfEntry.setStatus('current')
cOPatchIntfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("receive", 1), ("transmit", 2), ("both", 3))))
if mibBuilder.loadTexts: cOPatchIntfDirection.setStatus('current')
cOPatchIntfPatchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483547))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOPatchIntfPatchId.setStatus('current')
cOPatchMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 67, 2))
cOPatchEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 67, 2, 1)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"))
if mibBuilder.loadTexts: cOPatchEvent.setStatus('current')
cOPatchMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 67, 3))
cOPatchMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1))
cOPatchMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2))
cOPatchMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1, 1)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchInterfaceGroup"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchGroup"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchMIBCompliance = cOPatchMIBCompliance.setStatus('deprecated')
cOPatchMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1, 2)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfGroup"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchGroup1"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchMIBCompliance1 = cOPatchMIBCompliance1.setStatus('current')
cOPatchInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 1)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchInterfaceGroup = cOPatchInterfaceGroup.setStatus('deprecated')
cOPatchGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 2)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIndexNext"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastChange"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventEnabled"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchCreationTime"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchGroup = cOPatchGroup.setStatus('deprecated')
cOPatchNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 3)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchNotifyGroup = cOPatchNotifyGroup.setStatus('current')
cOPatchIntfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 4)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfPatchId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchIntfGroup = cOPatchIntfGroup.setStatus('current')
cOPatchGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 5)).setObjects(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIndexNext"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastChange"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventEnabled"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchCreationTime"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchRowStatus"), ("CISCO-OPTICAL-PATCH-MIB", "cOPatchDirOnLowIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOPatchGroup1 = cOPatchGroup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-PATCH-MIB", cOPatchHighIfIndex=cOPatchHighIfIndex, cOPatchIntfDirection=cOPatchIntfDirection, cOPatchStatus=cOPatchStatus, cOPatchIntfEntry=cOPatchIntfEntry, cOPatchIdentifier=cOPatchIdentifier, cOPatchMIBCompliance1=cOPatchMIBCompliance1, cOPatchGroup=cOPatchGroup, cOPatchMIBCompliance=cOPatchMIBCompliance, cOPatchRowStatus=cOPatchRowStatus, cOPatchGroup1=cOPatchGroup1, cOPatchIntfGroup=cOPatchIntfGroup, cOPatchMIBObjects=cOPatchMIBObjects, cOPatchIndex=cOPatchIndex, cOPatchMIBGroups=cOPatchMIBGroups, cOPatchNotifyGroup=cOPatchNotifyGroup, cOPatchEventEnabled=cOPatchEventEnabled, cOPatchType=cOPatchType, cOPatchCreationTime=cOPatchCreationTime, cOPatchMIBNotifications=cOPatchMIBNotifications, cOPatchEventType=cOPatchEventType, cOPatchEvent=cOPatchEvent, cOPatchLowIfIndex=cOPatchLowIfIndex, PYSNMP_MODULE_ID=ciscoOpticalPatchMIB, cOPatchMIBCompliances=cOPatchMIBCompliances, cOPatchInterfaceTable=cOPatchInterfaceTable, cOPatchTable=cOPatchTable, ciscoOpticalPatchMIB=ciscoOpticalPatchMIB, cOPatchIndexNext=cOPatchIndexNext, cOPatchMIBConformance=cOPatchMIBConformance, cOPatchDirOnLowIf=cOPatchDirOnLowIf, cOPatchLastChange=cOPatchLastChange, cOPatchIntfPatchId=cOPatchIntfPatchId, cOPatchInterfaceGroup=cOPatchInterfaceGroup, cOPatchEntry=cOPatchEntry, cOPatchIntfTable=cOPatchIntfTable, cOPatchInterfaceEntry=cOPatchInterfaceEntry)
