#
# PySNMP MIB module CT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
chassis, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "chassis")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Gauge32, IpAddress, Unsigned32, Counter32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "Counter32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chType.setStatus('mandatory')
chBackplaneTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2), )
if mibBuilder.loadTexts: chBackplaneTable.setStatus('mandatory')
chBackplaneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1), ).setIndexNames((0, "CT-CHASSIS-MIB", "chBackplaneID"))
if mibBuilder.loadTexts: chBackplaneEntry.setStatus('mandatory')
chBackplaneID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chBackplaneID.setStatus('mandatory')
chBackplaneType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chBackplaneType.setStatus('mandatory')
chNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNumSlots.setStatus('mandatory')
chCompTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4), )
if mibBuilder.loadTexts: chCompTable.setStatus('mandatory')
chCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1), ).setIndexNames((0, "CT-CHASSIS-MIB", "chCompID"))
if mibBuilder.loadTexts: chCompEntry.setStatus('mandatory')
chCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompID.setStatus('mandatory')
chCompAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("invalid", 2), ("enabled", 3), ("testing", 4), ("operational", 5), ("error", 6), ("disabled", 7), ("delete", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompAdminStatus.setStatus('mandatory')
chCompArg = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompArg.setStatus('mandatory')
chCompType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompType.setStatus('mandatory')
chCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompName.setStatus('mandatory')
chCompVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompVersion.setStatus('mandatory')
chCompTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompTimeStamp.setStatus('mandatory')
chCompAccessPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("invalid", 2), ("same", 3), ("otherCommStr", 4), ("other", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompAccessPolicy.setStatus('mandatory')
chCompBasicCommStr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompBasicCommStr.setStatus('mandatory')
chCompROCommStr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompROCommStr.setStatus('mandatory')
chCompRWCommStr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompRWCommStr.setStatus('mandatory')
chCompSUCommStr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompSUCommStr.setStatus('mandatory')
chCompNetAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompNetAdr.setStatus('mandatory')
chSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5), )
if mibBuilder.loadTexts: chSlotTable.setStatus('mandatory')
chSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1), ).setIndexNames((0, "CT-CHASSIS-MIB", "chSlotID"), (0, "CT-CHASSIS-MIB", "chSlotCompID"))
if mibBuilder.loadTexts: chSlotEntry.setStatus('mandatory')
chSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotID.setStatus('mandatory')
chSlotCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotCompID.setStatus('mandatory')
chSlotClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotClass.setStatus('mandatory')
chSlotModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotModuleType.setStatus('mandatory')
chSlotModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSlotModuleName.setStatus('mandatory')
chSlotModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotModuleVersion.setStatus('mandatory')
chSlotModuleTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSlotModuleTimeStamp.setStatus('mandatory')
chCompMIBTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6), )
if mibBuilder.loadTexts: chCompMIBTable.setStatus('deprecated')
chCompMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1), ).setIndexNames((0, "CT-CHASSIS-MIB", "chCompMIBID"), (0, "CT-CHASSIS-MIB", "chCompMIBSlotID"), (0, "CT-CHASSIS-MIB", "chCompMIBCompID"))
if mibBuilder.loadTexts: chCompMIBEntry.setStatus('deprecated')
chCompMIBID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompMIBID.setStatus('deprecated')
chCompMIBSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompMIBSlotID.setStatus('deprecated')
chCompMIBCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompMIBCompID.setStatus('deprecated')
chCompMIBGrpOID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompMIBGrpOID.setStatus('deprecated')
chCompMIBVectorObjectBase = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompMIBVectorObjectBase.setStatus('deprecated')
chCompMIBVectorNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompMIBVectorNum.setStatus('deprecated')
chCompMIBType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-instanced", 1), ("instanced", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompMIBType.setStatus('deprecated')
chCompMIBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("invalid", 2), ("agent", 3), ("management", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCompMIBStatus.setStatus('deprecated')
chPhysicalChanges = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPhysicalChanges.setStatus('deprecated')
chLogicalChanges = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chLogicalChanges.setStatus('deprecated')
chCompGlobalBasicCommStr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 27))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompGlobalBasicCommStr.setStatus('mandatory')
chCompGlobalROCommStr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 27))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompGlobalROCommStr.setStatus('mandatory')
chCompGlobalRWCommStr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 27))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompGlobalRWCommStr.setStatus('mandatory')
chCompGlobalSUCommStr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 27))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCompGlobalSUCommStr.setStatus('mandatory')
mibBuilder.exportSymbols("CT-CHASSIS-MIB", chSlotModuleName=chSlotModuleName, chCompROCommStr=chCompROCommStr, chCompMIBVectorObjectBase=chCompMIBVectorObjectBase, chType=chType, chCompEntry=chCompEntry, chCompMIBType=chCompMIBType, chPhysicalChanges=chPhysicalChanges, chLogicalChanges=chLogicalChanges, chCompID=chCompID, chBackplaneType=chBackplaneType, chCompRWCommStr=chCompRWCommStr, chSlotEntry=chSlotEntry, chCompMIBGrpOID=chCompMIBGrpOID, chBackplaneTable=chBackplaneTable, chCompMIBID=chCompMIBID, chSlotTable=chSlotTable, chCompMIBStatus=chCompMIBStatus, chCompTable=chCompTable, chCompMIBCompID=chCompMIBCompID, chCompVersion=chCompVersion, chCompTimeStamp=chCompTimeStamp, chCompBasicCommStr=chCompBasicCommStr, chCompAccessPolicy=chCompAccessPolicy, chCompMIBTable=chCompMIBTable, chCompSUCommStr=chCompSUCommStr, chCompMIBEntry=chCompMIBEntry, chSlotClass=chSlotClass, chBackplaneID=chBackplaneID, chCompGlobalSUCommStr=chCompGlobalSUCommStr, chSlotCompID=chSlotCompID, chCompType=chCompType, chBackplaneEntry=chBackplaneEntry, chCompGlobalRWCommStr=chCompGlobalRWCommStr, chCompMIBVectorNum=chCompMIBVectorNum, chNumSlots=chNumSlots, chCompGlobalROCommStr=chCompGlobalROCommStr, chCompAdminStatus=chCompAdminStatus, chSlotModuleType=chSlotModuleType, chSlotID=chSlotID, chCompGlobalBasicCommStr=chCompGlobalBasicCommStr, chCompName=chCompName, chSlotModuleVersion=chSlotModuleVersion, chCompNetAdr=chCompNetAdr, chCompArg=chCompArg, chSlotModuleTimeStamp=chSlotModuleTimeStamp, chCompMIBSlotID=chCompMIBSlotID)
