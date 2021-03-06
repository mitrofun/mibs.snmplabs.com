#
# PySNMP MIB module HPN-ICF-LswTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswTRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfLswSlotIndex, hpnicfLswFrameIndex, hpnicfLswSubslotIndex = mibBuilder.importSymbols("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex", "hpnicfLswFrameIndex", "hpnicfLswSubslotIndex")
hpnicfDevMFirstTrapTime, hpnicfDevMPowerNum, hpnicfDevMFanNum = mibBuilder.importSymbols("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime", "hpnicfDevMPowerNum", "hpnicfDevMFanNum")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, ObjectIdentity, Unsigned32, Counter64, Bits, ModuleIdentity, iso, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "iso", "IpAddress", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfLswTrapMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12))
hpnicfLswTrapMib.setRevisions(('2011-11-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLswTrapMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hpnicfLswTrapMib.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: hpnicfLswTrapMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfLswTrapMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLswTrapMib.setDescription('')
hpnicfsLswTRAPMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1))
hpnicfpowerfailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 1)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"), ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfpowerfailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfpowerfailure.setDescription('Power supply failure')
hpnicfPowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 2)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"), ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfPowerNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfPowerNormal.setDescription('Power supply normal')
hpnicfMasterPowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 3)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfMasterPowerNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfMasterPowerNormal.setDescription('Master power supply normal')
hpnicfSlavePowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 4)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfSlavePowerNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfSlavePowerNormal.setDescription('Slave power supply normal')
hpnicfPowerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 5)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfPowerRemoved.setStatus('current')
if mibBuilder.loadTexts: hpnicfPowerRemoved.setDescription('Power removed')
hpnicffanfailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 6)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum"))
if mibBuilder.loadTexts: hpnicffanfailure.setStatus('current')
if mibBuilder.loadTexts: hpnicffanfailure.setDescription('Fan failure')
hpnicfFanNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 7)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum"))
if mibBuilder.loadTexts: hpnicfFanNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfFanNormal.setDescription('Fan normal')
hpnicfBoardRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 8)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardRemoved.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardRemoved.setDescription('Board removed')
hpnicfBoardInserted = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 9)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardInserted.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardInserted.setDescription('Board inserted')
hpnicfBoardFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 10)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardFailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardFailure.setDescription('Board failed')
hpnicfBoardNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 11)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardNormal.setDescription('Board normal')
hpnicfSubcardRemove = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 12)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
if mibBuilder.loadTexts: hpnicfSubcardRemove.setStatus('current')
if mibBuilder.loadTexts: hpnicfSubcardRemove.setDescription('Sub card removeed')
hpnicfSubcardInsert = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 13)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
if mibBuilder.loadTexts: hpnicfSubcardInsert.setStatus('current')
if mibBuilder.loadTexts: hpnicfSubcardInsert.setDescription('Sub card inserted')
hpnicfBoardTemperatureLower = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 14)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureLower.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardTemperatureLower.setDescription('Board temperature low')
hpnicfBoardTemperatureFromLowerToNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 15)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureFromLowerToNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardTemperatureFromLowerToNormal.setDescription('Board temperature form lower to normal')
hpnicfBoardTemperatureHigher = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 16)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureHigher.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardTemperatureHigher.setDescription('Board temperature high')
hpnicfBoardTemperatureFormHigherToNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 17)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureFormHigherToNormal.setStatus('current')
if mibBuilder.loadTexts: hpnicfBoardTemperatureFormHigherToNormal.setDescription('Board temperature from higher to normal')
hpnicfRequestLoading = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 18)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfRequestLoading.setStatus('current')
if mibBuilder.loadTexts: hpnicfRequestLoading.setDescription('Board request load')
hpnicfLoadFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 19)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfLoadFailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfLoadFailure.setDescription('Board load failure')
hpnicfLoadFinished = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 20)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfLoadFinished.setStatus('current')
if mibBuilder.loadTexts: hpnicfLoadFinished.setDescription('Board load finished')
hpnicfBackBoardModeSetFuilure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 21)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"))
if mibBuilder.loadTexts: hpnicfBackBoardModeSetFuilure.setStatus('current')
if mibBuilder.loadTexts: hpnicfBackBoardModeSetFuilure.setDescription('Back board mode set failure')
hpnicfBackBoardModeSetOK = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 22)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"))
if mibBuilder.loadTexts: hpnicfBackBoardModeSetOK.setStatus('current')
if mibBuilder.loadTexts: hpnicfBackBoardModeSetOK.setDescription('Back board mode set OK')
hpnicfPowerInserted = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 23)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfPowerInserted.setStatus('current')
if mibBuilder.loadTexts: hpnicfPowerInserted.setDescription('Power inserted')
hpnicfBootImageUpdated = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 24)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBootImageUpdated.setStatus('current')
if mibBuilder.loadTexts: hpnicfBootImageUpdated.setDescription('This trap node indicates that the boot image of specified board is updated.')
hpnicfNetworkHealthMonitorFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 98))
hpnicfNetworkHealthMonitorNormal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 99))
mibBuilder.exportSymbols("HPN-ICF-LswTRAP-MIB", hpnicfsLswTRAPMibObject=hpnicfsLswTRAPMibObject, hpnicfSubcardRemove=hpnicfSubcardRemove, hpnicfSubcardInsert=hpnicfSubcardInsert, hpnicffanfailure=hpnicffanfailure, hpnicfRequestLoading=hpnicfRequestLoading, hpnicfNetworkHealthMonitorNormal=hpnicfNetworkHealthMonitorNormal, hpnicfBoardRemoved=hpnicfBoardRemoved, hpnicfBootImageUpdated=hpnicfBootImageUpdated, hpnicfMasterPowerNormal=hpnicfMasterPowerNormal, hpnicfPowerRemoved=hpnicfPowerRemoved, hpnicfpowerfailure=hpnicfpowerfailure, hpnicfLoadFinished=hpnicfLoadFinished, hpnicfBoardTemperatureHigher=hpnicfBoardTemperatureHigher, hpnicfBackBoardModeSetOK=hpnicfBackBoardModeSetOK, hpnicfBoardInserted=hpnicfBoardInserted, hpnicfPowerInserted=hpnicfPowerInserted, PYSNMP_MODULE_ID=hpnicfLswTrapMib, hpnicfLswTrapMib=hpnicfLswTrapMib, hpnicfLoadFailure=hpnicfLoadFailure, hpnicfBoardTemperatureFormHigherToNormal=hpnicfBoardTemperatureFormHigherToNormal, hpnicfSlavePowerNormal=hpnicfSlavePowerNormal, hpnicfBackBoardModeSetFuilure=hpnicfBackBoardModeSetFuilure, hpnicfBoardFailure=hpnicfBoardFailure, hpnicfFanNormal=hpnicfFanNormal, hpnicfNetworkHealthMonitorFailure=hpnicfNetworkHealthMonitorFailure, hpnicfPowerNormal=hpnicfPowerNormal, hpnicfBoardTemperatureFromLowerToNormal=hpnicfBoardTemperatureFromLowerToNormal, hpnicfBoardNormal=hpnicfBoardNormal, hpnicfBoardTemperatureLower=hpnicfBoardTemperatureLower)
