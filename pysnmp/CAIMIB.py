#
# PySNMP MIB module CAIMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAIMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, NotificationType, Unsigned32, Counter32, Gauge32, iso, TimeTicks, Integer32, MibIdentifier, IpAddress, ModuleIdentity, Counter64, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "NotificationType", "Unsigned32", "Counter32", "Gauge32", "iso", "TimeTicks", "Integer32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Counter64", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cai = MibIdentifier((1, 3, 6, 1, 4, 1, 791))
caiSysMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 2))
caiDbMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 3))
caiAppSft = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 4))
caiUnicenter = MibIdentifier((1, 3, 6, 1, 4, 1, 791, 2, 2))
caiUniGenlvl = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniGenlvl.setStatus('mandatory')
caiUniConfig = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniConfig.setStatus('mandatory')
caiUniLicExp = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniLicExp.setStatus('mandatory')
caiUniLstMsg = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniLstMsg.setStatus('mandatory')
caiUniCltSrv = MibScalar((1, 3, 6, 1, 4, 1, 791, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("client", 1), ("server", 2), ("standalone", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniCltSrv.setStatus('mandatory')
caiUniStatTable = MibTable((1, 3, 6, 1, 4, 1, 791, 2, 2, 7), )
if mibBuilder.loadTexts: caiUniStatTable.setStatus('mandatory')
caiUniStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2), ).setIndexNames((0, "CAIMIB", "caiUniStatEntIdx"))
if mibBuilder.loadTexts: caiUniStatEntry.setStatus('mandatory')
caiUniStatEntIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniStatEntIdx.setStatus('mandatory')
caiUniStatComp = MibTableColumn((1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caiUniStatComp.setStatus('mandatory')
caiUniSecuT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,1)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,2)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT3 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,3)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT4 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,4)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT5 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,5)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT6 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,6)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT7 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,7)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniSecuT8 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,8)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,100)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,101)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT3 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,102)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT4 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,103)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT5 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,104)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT6 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,105)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT7 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,106)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniScheT8 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,107)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniGuiT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,200)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,300)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,301)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT3 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,302)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT4 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,303)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT5 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,304)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT6 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,305)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT7 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,306)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT8 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,307)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniTapeT9 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,308)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniAsmT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,400)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniAsmT2 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,401)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniCciT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,500)).setObjects(("CAIMIB", "caiUniLstMsg"))
caiUniEnfT1 = NotificationType((1, 3, 6, 1, 4, 1, 791) + (0,501)).setObjects(("CAIMIB", "caiUniLstMsg"))
mibBuilder.exportSymbols("CAIMIB", caiUniScheT7=caiUniScheT7, caiUniLstMsg=caiUniLstMsg, caiUniSecuT6=caiUniSecuT6, caiUniAsmT1=caiUniAsmT1, caiUniScheT5=caiUniScheT5, caiUniSecuT8=caiUniSecuT8, cai=cai, caiSysMgt=caiSysMgt, caiUniTapeT9=caiUniTapeT9, caiUniStatTable=caiUniStatTable, caiUniSecuT1=caiUniSecuT1, caiUniScheT3=caiUniScheT3, caiUniScheT1=caiUniScheT1, caiUniScheT6=caiUniScheT6, caiUniTapeT8=caiUniTapeT8, caiUniGuiT1=caiUniGuiT1, caiUniTapeT2=caiUniTapeT2, caiUniSecuT4=caiUniSecuT4, caiUniSecuT3=caiUniSecuT3, caiUniCltSrv=caiUniCltSrv, caiUniTapeT3=caiUniTapeT3, caiUniLicExp=caiUniLicExp, caiUniScheT4=caiUniScheT4, caiUniTapeT5=caiUniTapeT5, caiAppSft=caiAppSft, caiUniConfig=caiUniConfig, caiUniScheT8=caiUniScheT8, caiUniStatEntIdx=caiUniStatEntIdx, caiUniStatComp=caiUniStatComp, caiUniCciT1=caiUniCciT1, caiUniScheT2=caiUniScheT2, caiUniTapeT6=caiUniTapeT6, caiUniTapeT1=caiUniTapeT1, caiUniSecuT2=caiUniSecuT2, caiUniAsmT2=caiUniAsmT2, caiUniTapeT4=caiUniTapeT4, caiUniGenlvl=caiUniGenlvl, caiDbMgt=caiDbMgt, caiUniEnfT1=caiUniEnfT1, caiUniSecuT5=caiUniSecuT5, caiUniSecuT7=caiUniSecuT7, caiUnicenter=caiUnicenter, caiUniTapeT7=caiUniTapeT7, caiUniStatEntry=caiUniStatEntry)
