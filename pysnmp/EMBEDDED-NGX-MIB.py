#
# PySNMP MIB module EMBEDDED-NGX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EMBEDDED-NGX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, enterprises, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, MibIdentifier, Counter64, ObjectIdentity, IpAddress, Integer32, TimeTicks, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "MibIdentifier", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

sofaware = MibIdentifier((1, 3, 6, 1, 4, 1, 6983))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1))
swHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 1))
swStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 2))
swLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 3))
swFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 4))
swMem = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 5))
swAV = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 6))
swFW = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 7))
swWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 8))
swHA = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 9))
swGWType = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10))
swHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swHardwareVersion.setStatus('mandatory')
swHardwareType = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swHardwareType.setStatus('mandatory')
swStorageConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 2, 1))
swStorageFirm = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 2, 2))
swStorageCF = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 2, 3))
swStorageConfigTotal = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageConfigTotal.setStatus('mandatory')
swStorageConfigFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageConfigFree.setStatus('mandatory')
swStorageFirmTotal = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageFirmTotal.setStatus('mandatory')
swStorageFirmFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageFirmFree.setStatus('mandatory')
swStorageCFTotal = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageCFTotal.setStatus('mandatory')
swStorageCFFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageCFFree.setStatus('mandatory')
swLicenseMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLicenseMacAddress.setStatus('mandatory')
swLicenseProductKey = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLicenseProductKey.setStatus('mandatory')
swLicenseProductName = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLicenseProductName.setStatus('mandatory')
swLicenseUsedNodes = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLicenseUsedNodes.setStatus('mandatory')
swFirmwareRunning = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFirmwareRunning.setStatus('mandatory')
swFirmwarePrimary = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFirmwarePrimary.setStatus('mandatory')
swFirmwareBackup = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFirmwareBackup.setStatus('mandatory')
swFirmwareBootcodeVersion = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFirmwareBootcodeVersion.setStatus('mandatory')
swFirmwareDebugMode = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFirmwareDebugMode.setStatus('mandatory')
swMemRAM = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 5, 1))
swMemDFA = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 5, 2))
swMemRamFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMemRamFree.setStatus('mandatory')
swMemRamTotal = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMemRamTotal.setStatus('mandatory')
swMemDfaFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMemDfaFree.setStatus('mandatory')
swMemDfaTotal = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMemDfaTotal.setStatus('mandatory')
swMemDfaTest = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMemDfaTest.setStatus('mandatory')
swUserMemFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUserMemFree.setStatus('mandatory')
swKernelMemFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swKernelMemFree.setStatus('mandatory')
swFwMEMFree = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFwMEMFree.setStatus('mandatory')
swAvMain = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvMain.setStatus('mandatory')
swAvDaily = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvDaily.setStatus('mandatory')
swAvStatus = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvStatus.setStatus('mandatory')
swAvNextUpdate = MibScalar((1, 3, 6, 1, 4, 1, 6983, 1, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvNextUpdate.setStatus('mandatory')
swFwActiveComputersTable = MibTable((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1), )
if mibBuilder.loadTexts: swFwActiveComputersTable.setStatus('mandatory')
swFwActiveComputerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1), ).setIndexNames((0, "EMBEDDED-NGX-MIB", "swActCompNetwork"))
if mibBuilder.loadTexts: swFwActiveComputerEntry.setStatus('mandatory')
swActCompNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompNetwork.setStatus('mandatory')
swActCompIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompIpAddress.setStatus('mandatory')
swActCompMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompMac.setStatus('mandatory')
swActCompType = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompType.setStatus('mandatory')
swActCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompName.setStatus('mandatory')
swActCompLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompLicense.setStatus('mandatory')
swActCompAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompAuthStatus.setStatus('mandatory')
swActCompAuthUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompAuthUsername.setStatus('mandatory')
swActCompAuthSessionExpiresTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 7, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swActCompAuthSessionExpiresTime.setStatus('mandatory')
swWirelessStationsTable = MibTable((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1), )
if mibBuilder.loadTexts: swWirelessStationsTable.setStatus('mandatory')
swWirelessStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1), ).setIndexNames((0, "EMBEDDED-NGX-MIB", "swWStationMac"))
if mibBuilder.loadTexts: swWirelessStationEntry.setStatus('mandatory')
swWStationMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationMac.setStatus('mandatory')
swWStationSignalDb = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationSignalDb.setStatus('mandatory')
swWStationQos = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationQos.setStatus('mandatory')
swWStationXr = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationXr.setStatus('mandatory')
swWStationRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRate.setStatus('mandatory')
swWStationCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationCipher.setStatus('mandatory')
swWStationRxFramesOk = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxFramesOk.setStatus('mandatory')
swWStationRxFramesManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxFramesManagement.setStatus('mandatory')
swWStationRxFramesControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxFramesControl.setStatus('mandatory')
swWStationRxFramesErrorFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxFramesErrorFrame.setStatus('mandatory')
swWStationRxRetryRation = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxRetryRation.setStatus('mandatory')
swWStationRxDupRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationRxDupRatio.setStatus('mandatory')
swWStationTxFramesOk = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationTxFramesOk.setStatus('mandatory')
swWStationTxFramesManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationTxFramesManagement.setStatus('mandatory')
swWStationTxFramesError = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationTxFramesError.setStatus('mandatory')
swWStationTxFailRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationTxFailRatio.setStatus('mandatory')
swWStationTxPacketErrorRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 8, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWStationTxPacketErrorRatio.setStatus('mandatory')
swVirtualIpTable = MibTable((1, 3, 6, 1, 4, 1, 6983, 1, 9, 1), )
if mibBuilder.loadTexts: swVirtualIpTable.setStatus('mandatory')
swVirtualIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1), ).setIndexNames((0, "EMBEDDED-NGX-MIB", "swVirtualIpAddr"))
if mibBuilder.loadTexts: swVirtualIpEntry.setStatus('mandatory')
swVirtualIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVirtualIpAddr.setStatus('mandatory')
swVirtualIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6983, 1, 9, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVirtualIpStatus.setStatus('mandatory')
SafeAtOffice205 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 7))
SafeAtOffice210 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 9))
SafeAtOffice225 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 11))
UTM1EdgeX = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 15))
SafeAtOffice405 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 16))
SafeAtOffice410 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 17))
SafeAtOffice425 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 18))
UTM1EdgeW = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 20))
SafeAtOffice500 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 21))
SafeAtOffice500P = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 22))
UTM_1X300 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 23)).setLabel("UTM-1X300")
UTM_1X400 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 24)).setLabel("UTM-1X400")
UTM_1X1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 6983, 1, 10, 25)).setLabel("UTM-1X1000")
mibBuilder.exportSymbols("EMBEDDED-NGX-MIB", products=products, swWirelessStationsTable=swWirelessStationsTable, swWirelessStationEntry=swWirelessStationEntry, swStorageConfig=swStorageConfig, swVirtualIpAddr=swVirtualIpAddr, swMemRAM=swMemRAM, swVirtualIpTable=swVirtualIpTable, swVirtualIpStatus=swVirtualIpStatus, swFirmware=swFirmware, swActCompType=swActCompType, swMemDfaFree=swMemDfaFree, swStorageCF=swStorageCF, swHardwareVersion=swHardwareVersion, SafeAtOffice425=SafeAtOffice425, swLicenseProductName=swLicenseProductName, SafeAtOffice210=SafeAtOffice210, swAvNextUpdate=swAvNextUpdate, swWStationTxFramesManagement=swWStationTxFramesManagement, swStorageFirm=swStorageFirm, SafeAtOffice405=SafeAtOffice405, UTM1EdgeX=UTM1EdgeX, swWStationQos=swWStationQos, swHardware=swHardware, swActCompAuthSessionExpiresTime=swActCompAuthSessionExpiresTime, UTM_1X300=UTM_1X300, swWStationXr=swWStationXr, swHardwareType=swHardwareType, swStorage=swStorage, swStorageFirmFree=swStorageFirmFree, swStorageCFFree=swStorageCFFree, SafeAtOffice500P=SafeAtOffice500P, swGWType=swGWType, swWStationTxFailRatio=swWStationTxFailRatio, swFirmwareRunning=swFirmwareRunning, swLicense=swLicense, swActCompNetwork=swActCompNetwork, swVirtualIpEntry=swVirtualIpEntry, swWStationRxFramesErrorFrame=swWStationRxFramesErrorFrame, swLicenseProductKey=swLicenseProductKey, swFwActiveComputerEntry=swFwActiveComputerEntry, swStorageConfigTotal=swStorageConfigTotal, swAV=swAV, SafeAtOffice500=SafeAtOffice500, swWStationRxFramesOk=swWStationRxFramesOk, SafeAtOffice225=SafeAtOffice225, swFirmwareDebugMode=swFirmwareDebugMode, swMemRamFree=swMemRamFree, swWStationSignalDb=swWStationSignalDb, swHA=swHA, swActCompAuthStatus=swActCompAuthStatus, swWStationTxFramesError=swWStationTxFramesError, swLicenseUsedNodes=swLicenseUsedNodes, swActCompIpAddress=swActCompIpAddress, swActCompAuthUsername=swActCompAuthUsername, swStorageConfigFree=swStorageConfigFree, swFirmwareBackup=swFirmwareBackup, swFwActiveComputersTable=swFwActiveComputersTable, swActCompName=swActCompName, swWStationRxRetryRation=swWStationRxRetryRation, swStorageCFTotal=swStorageCFTotal, swWStationRxDupRatio=swWStationRxDupRatio, swMemDfaTest=swMemDfaTest, swWStationTxPacketErrorRatio=swWStationTxPacketErrorRatio, swAvMain=swAvMain, swMemRamTotal=swMemRamTotal, swActCompLicense=swActCompLicense, swWStationTxFramesOk=swWStationTxFramesOk, swWStationMac=swWStationMac, sofaware=sofaware, swLicenseMacAddress=swLicenseMacAddress, UTM_1X400=UTM_1X400, swWireless=swWireless, swMem=swMem, swActCompMac=swActCompMac, swWStationRxFramesManagement=swWStationRxFramesManagement, swUserMemFree=swUserMemFree, swAvStatus=swAvStatus, swStorageFirmTotal=swStorageFirmTotal, SafeAtOffice410=SafeAtOffice410, DisplayString=DisplayString, swFirmwareBootcodeVersion=swFirmwareBootcodeVersion, swWStationCipher=swWStationCipher, SafeAtOffice205=SafeAtOffice205, swMemDfaTotal=swMemDfaTotal, UTM1EdgeW=UTM1EdgeW, swMemDFA=swMemDFA, swWStationRate=swWStationRate, UTM_1X1000=UTM_1X1000, swKernelMemFree=swKernelMemFree, swAvDaily=swAvDaily, swWStationRxFramesControl=swWStationRxFramesControl, swFwMEMFree=swFwMEMFree, swFW=swFW, swFirmwarePrimary=swFirmwarePrimary)