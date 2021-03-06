#
# PySNMP MIB module Chromatis-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Chromatis-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Counter32, Gauge32, iso, ObjectIdentity, IpAddress, MibIdentifier, TimeTicks, Unsigned32, enterprises, Bits, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "MibIdentifier", "TimeTicks", "Unsigned32", "enterprises", "Bits", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chromatis = ModuleIdentity((1, 3, 6, 1, 4, 1, 3695))
chromatis.setRevisions(('1999-05-17 18:30',))
if mibBuilder.loadTexts: chromatis.setLastUpdated('9905170000Z')
if mibBuilder.loadTexts: chromatis.setOrganization('Chromatis Networks Inc.')
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
mibBuilder.exportSymbols("Chromatis-MIB", chrComTrap=chrComTrap, chrProductsMetropolis2500=chrProductsMetropolis2500, chrComIfAtm=chrComIfAtm, chrComPmEth=chrComPmEth, chrComProtectSinglePath=chrComProtectSinglePath, chrComIf=chrComIf, chrComProtectEquip=chrComProtectEquip, chrComProtectionVp=chrComProtectionVp, chrComAccess=chrComAccess, chrComSwVersion=chrComSwVersion, chrComIfDS3=chrComIfDS3, chrProducts=chrProducts, chrComPM=chrComPM, chrComProtectionGroup=chrComProtectionGroup, chrProductsMetropolis2000=chrProductsMetropolis2000, chrComFM=chrComFM, chrComIfOptics=chrComIfOptics, chrComAtmVcl=chrComAtmVcl, chrProductsMetropolis4000=chrProductsMetropolis4000, chrComProtection=chrComProtection, chrComPmSonet=chrComPmSonet, chrComPmDs3=chrComPmDs3, chrComNetClockSync=chrComNetClockSync, chrCommon=chrCommon, PYSNMP_MODULE_ID=chromatis, chrComNetwork=chrComNetwork, chrComPmAtm=chrComPmAtm, chrComConfigVersion=chrComConfigVersion, chrComIfSonet=chrComIfSonet, chrComProtectionVc=chrComProtectionVc, chrComCompressData=chrComCompressData, chrComPmOptics=chrComPmOptics, chrProductsMetropolis4500=chrProductsMetropolis4500, chrComActions=chrComActions, chrComHwNe=chrComHwNe, chromatis=chromatis, chrComHW=chrComHW, chrComAtm=chrComAtm, chrComAtmVpl=chrComAtmVpl, chrComIfEthernet=chrComIfEthernet)
