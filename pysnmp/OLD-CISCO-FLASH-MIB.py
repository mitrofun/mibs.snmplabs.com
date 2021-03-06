#
# PySNMP MIB module OLD-CISCO-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OLD-CISCO-FLASH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:23:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, IpAddress, NotificationType, Counter32, Counter64, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "Counter64", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lflash = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 10))
flashSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashSize.setStatus('mandatory')
flashFree = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFree.setStatus('mandatory')
flashController = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashController.setStatus('mandatory')
flashCard = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCard.setStatus('mandatory')
flashVPP = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("installed", 1), ("missing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVPP.setStatus('mandatory')
flashErase = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 6), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: flashErase.setStatus('mandatory')
flashEraseTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashEraseTime.setStatus('mandatory')
flashEraseStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashEraseStatus.setStatus('mandatory')
flashToNet = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 9), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: flashToNet.setStatus('mandatory')
flashToNetTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashToNetTime.setStatus('mandatory')
flashToNetStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashToNetStatus.setStatus('mandatory')
netToFlash = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 12), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: netToFlash.setStatus('mandatory')
netToFlashTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netToFlashTime.setStatus('mandatory')
netToFlashStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netToFlashStatus.setStatus('mandatory')
flashStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("busy", 1), ("available", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashStatus.setStatus('mandatory')
flashEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 10, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashEntries.setStatus('mandatory')
lflashFileDirTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 10, 17), )
if mibBuilder.loadTexts: lflashFileDirTable.setStatus('mandatory')
lflashFileDirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1), ).setIndexNames((0, "OLD-CISCO-FLASH-MIB", "flashEntries"))
if mibBuilder.loadTexts: lflashFileDirEntry.setStatus('mandatory')
flashDirName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashDirName.setStatus('mandatory')
flashDirSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashDirSize.setStatus('mandatory')
flashDirStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("deleted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashDirStatus.setStatus('mandatory')
mibBuilder.exportSymbols("OLD-CISCO-FLASH-MIB", flashDirStatus=flashDirStatus, flashController=flashController, flashSize=flashSize, netToFlashStatus=netToFlashStatus, lflashFileDirEntry=lflashFileDirEntry, flashFree=flashFree, lflashFileDirTable=lflashFileDirTable, flashDirName=flashDirName, flashVPP=flashVPP, flashEntries=flashEntries, flashDirSize=flashDirSize, flashEraseTime=flashEraseTime, flashEraseStatus=flashEraseStatus, netToFlashTime=netToFlashTime, flashToNetStatus=flashToNetStatus, lflash=lflash, flashToNet=flashToNet, flashErase=flashErase, flashToNetTime=flashToNetTime, flashCard=flashCard, netToFlash=netToFlash, flashStatus=flashStatus)
