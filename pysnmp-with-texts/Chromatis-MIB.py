#
# PySNMP MIB module Chromatis-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Chromatis-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, ObjectIdentity, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, MibIdentifier, Integer32, Gauge32, Bits, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "Bits", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chromatis = ModuleIdentity((1, 3, 6, 1, 4, 1, 3695))
chromatis.setRevisions(('1999-05-17 18:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: chromatis.setRevisionsDescriptions(('Compiled for the first time by Zvika',))
if mibBuilder.loadTexts: chromatis.setLastUpdated('9905170000Z')
if mibBuilder.loadTexts: chromatis.setOrganization('Chromatis Networks Inc.')
if mibBuilder.loadTexts: chromatis.setContactInfo('Chromatis Networks 21 c Yagea Kapaim , Kiryat Arye, Petach Tikva, Israel Phone: 972-3-9231030 Fax: 972-3-9231050 emil@chromatis.com')
if mibBuilder.loadTexts: chromatis.setDescription("This MIB module is the SNMP version of Chromatis Networks' Metrpolis")
chrCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1))
chrProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 2))
chrComHW = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 1))
chrComIf = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2))
chrComConfigVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 3))
chrComSwVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 4))
chrComAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 5))
chrComTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 6))
chrComActions = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 7))
chrComCompressData = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 8))
chrComAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 9))
chrComPM = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10))
chrComFM = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 11))
chrComProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12))
chrComNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 13))
chrComHwNe = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 1, 1))
chrComIfSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2, 1))
chrComIfAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2, 2))
chrComIfOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3))
chrComIfDS3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2, 4))
chrComIfEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 2, 5))
chrComAtmVpl = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 9, 1))
chrComAtmVcl = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 9, 2))
chrComPmOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1))
chrComPmSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2))
chrComPmDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3))
chrComPmAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4))
chrComPmEth = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5))
chrComProtectionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12, 1))
chrComProtectionVp = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2))
chrComProtectionVc = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3))
chrComProtectSinglePath = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4))
chrComProtectEquip = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 12, 5))
chrComNetClockSync = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 1, 13, 1))
chrProductsMetropolis2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 2, 1))
chrProductsMetropolis2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 2, 2))
chrProductsMetropolis4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 2, 3))
chrProductsMetropolis4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3695, 2, 4))
mibBuilder.exportSymbols("Chromatis-MIB", chrComFM=chrComFM, chrProductsMetropolis4500=chrProductsMetropolis4500, chrComActions=chrComActions, chrComIfSonet=chrComIfSonet, chrComHW=chrComHW, chrComPmEth=chrComPmEth, chrComIf=chrComIf, PYSNMP_MODULE_ID=chromatis, chrComProtectionGroup=chrComProtectionGroup, chrComTrap=chrComTrap, chrComCompressData=chrComCompressData, chrComNetwork=chrComNetwork, chrCommon=chrCommon, chrComConfigVersion=chrComConfigVersion, chrComNetClockSync=chrComNetClockSync, chrComProtectSinglePath=chrComProtectSinglePath, chrComIfAtm=chrComIfAtm, chrComPmOptics=chrComPmOptics, chrComProtectionVc=chrComProtectionVc, chrComAtmVpl=chrComAtmVpl, chrComPM=chrComPM, chrComAtmVcl=chrComAtmVcl, chrComIfOptics=chrComIfOptics, chrComProtectionVp=chrComProtectionVp, chrProductsMetropolis2000=chrProductsMetropolis2000, chromatis=chromatis, chrComPmSonet=chrComPmSonet, chrComSwVersion=chrComSwVersion, chrComProtectEquip=chrComProtectEquip, chrComHwNe=chrComHwNe, chrComIfEthernet=chrComIfEthernet, chrComAccess=chrComAccess, chrProductsMetropolis2500=chrProductsMetropolis2500, chrComProtection=chrComProtection, chrProducts=chrProducts, chrComIfDS3=chrComIfDS3, chrComPmAtm=chrComPmAtm, chrProductsMetropolis4000=chrProductsMetropolis4000, chrComPmDs3=chrComPmDs3, chrComAtm=chrComAtm)