#
# PySNMP MIB module ZhoneProductRegistrations (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZhoneProductRegistrations
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter32, ObjectIdentity, Bits, NotificationType, MibIdentifier, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Counter64", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneModules, zhoneRegistrations, zhoneRegCpe, zhoneRegMux, zhoneRegPls, zhoneRegSechtor, zhoneRegMalc = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneRegistrations", "zhoneRegCpe", "zhoneRegMux", "zhoneRegPls", "zhoneRegSechtor", "zhoneRegMalc")
zhoneRegistrationsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 1))
zhoneRegistrationsModule.setRevisions(('2012-08-01 16:11', '2011-11-30 11:56', '2011-08-15 07:13', '2011-05-13 05:14', '2010-09-23 14:40', '2010-08-03 10:12', '2010-02-11 15:38', '2009-08-13 14:04', '2008-10-28 13:44', '2007-11-15 12:08', '2007-10-31 13:13', '2007-06-27 11:54', '2007-06-11 16:12', '2007-05-11 16:00', '2007-05-09 10:56', '2007-04-03 10:48', '2007-03-09 14:13', '2006-10-26 15:17', '2006-08-31 20:02', '2006-07-13 16:07', '2006-05-22 16:01', '2006-05-05 15:42', '2006-04-28 13:36', '2006-04-27 13:23', '2006-04-24 12:06', '2006-04-18 17:43', '2006-03-27 11:14', '2005-12-09 14:14', '2004-09-08 17:28', '2004-08-30 11:07', '2004-05-25 12:30', '2004-05-21 14:25', '2004-05-21 13:26', '2004-04-06 01:45', '2004-03-17 10:54', '2004-03-02 14:00', '2003-10-31 14:26', '2003-07-10 12:19', '2003-05-16 17:04', '2003-02-11 14:58', '2002-10-23 10:18', '2002-10-10 09:43', '2002-10-10 09:42', '2001-06-26 17:04', '2001-06-07 11:59', '2001-05-15 11:53', '2001-02-01 13:10', '2000-09-28 16:48', '2000-09-12 10:55',))
if mibBuilder.loadTexts: zhoneRegistrationsModule.setLastUpdated('201208011611Z')
if mibBuilder.loadTexts: zhoneRegistrationsModule.setOrganization('Zhone Technologies')
ban_2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 1, 1)).setLabel("ban-2000")
if mibBuilder.loadTexts: ban_2000.setStatus('current')
zedge64 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 1))
if mibBuilder.loadTexts: zedge64.setStatus('current')
zedge64_SHDSL_FXS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 1)).setLabel("zedge64-SHDSL-FXS")
if mibBuilder.loadTexts: zedge64_SHDSL_FXS.setStatus('current')
zedge64_SHDSL_BRI = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 2)).setLabel("zedge64-SHDSL-BRI")
if mibBuilder.loadTexts: zedge64_SHDSL_BRI.setStatus('current')
zedge64_T1_FXS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 3)).setLabel("zedge64-T1-FXS")
if mibBuilder.loadTexts: zedge64_T1_FXS.setStatus('current')
zedge64_E1_FXS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 1, 4)).setLabel("zedge64-E1-FXS")
if mibBuilder.loadTexts: zedge64_E1_FXS.setStatus('current')
zedge6200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 2))
if mibBuilder.loadTexts: zedge6200.setStatus('current')
zedge6200_IP_T1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 1)).setLabel("zedge6200-IP-T1")
if mibBuilder.loadTexts: zedge6200_IP_T1.setStatus('current')
zedge6200_IP_EM = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 2)).setLabel("zedge6200-IP-EM")
if mibBuilder.loadTexts: zedge6200_IP_EM.setStatus('current')
zedge6200_IP_FXS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 2, 3)).setLabel("zedge6200-IP-FXS")
if mibBuilder.loadTexts: zedge6200_IP_FXS.setStatus('current')
zrg3xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 3))
if mibBuilder.loadTexts: zrg3xx.setStatus('current')
zrg300_IDU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 3, 1)).setLabel("zrg300-IDU")
if mibBuilder.loadTexts: zrg300_IDU.setStatus('current')
zrg300_ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 3, 2)).setLabel("zrg300-ODU")
if mibBuilder.loadTexts: zrg300_ODU.setStatus('current')
zrg5xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 4))
if mibBuilder.loadTexts: zrg5xx.setStatus('current')
zrg500_IDU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 4, 1)).setLabel("zrg500-IDU")
if mibBuilder.loadTexts: zrg500_IDU.setStatus('current')
zrg500_ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 4, 2)).setLabel("zrg500-ODU")
if mibBuilder.loadTexts: zrg500_ODU.setStatus('current')
zrg7xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 5))
if mibBuilder.loadTexts: zrg7xx.setStatus('current')
zrg700_IDU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 5, 1)).setLabel("zrg700-IDU")
if mibBuilder.loadTexts: zrg700_IDU.setStatus('current')
zrg700_ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 5, 2)).setLabel("zrg700-ODU")
if mibBuilder.loadTexts: zrg700_ODU.setStatus('current')
zrg6xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 6))
if mibBuilder.loadTexts: zrg6xx.setStatus('current')
zrg600_IDU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 6, 1)).setLabel("zrg600-IDU")
if mibBuilder.loadTexts: zrg600_IDU.setStatus('current')
zrg600_ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 6, 2)).setLabel("zrg600-ODU")
if mibBuilder.loadTexts: zrg600_ODU.setStatus('current')
zrg8xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 7))
if mibBuilder.loadTexts: zrg8xx.setStatus('current')
zrg800_IDU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 7, 1)).setLabel("zrg800-IDU")
if mibBuilder.loadTexts: zrg800_IDU.setStatus('current')
zrg800_ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 7, 2)).setLabel("zrg800-ODU")
if mibBuilder.loadTexts: zrg800_ODU.setStatus('current')
ethXtendxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8))
if mibBuilder.loadTexts: ethXtendxx.setStatus('current')
ethXtendShdsl = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 1))
if mibBuilder.loadTexts: ethXtendShdsl.setStatus('current')
ethXtendT1E1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 2))
if mibBuilder.loadTexts: ethXtendT1E1.setStatus('current')
ethXtend30xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 3))
if mibBuilder.loadTexts: ethXtend30xx.setStatus('current')
ethXtend31xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 4))
if mibBuilder.loadTexts: ethXtend31xx.setStatus('current')
ethXtend32xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 8, 5))
if mibBuilder.loadTexts: ethXtend32xx.setStatus('current')
znid = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9))
if mibBuilder.loadTexts: znid.setStatus('current')
znid42xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1))
if mibBuilder.loadTexts: znid42xx.setStatus('current')
znidGPON42xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1, 2))
if mibBuilder.loadTexts: znidGPON42xx.setStatus('current')
znidEth422x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 1, 3))
if mibBuilder.loadTexts: znidEth422x.setStatus('current')
znid420x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 2))
if mibBuilder.loadTexts: znid420x.setStatus('current')
znidGPON420x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 9, 2, 1))
if mibBuilder.loadTexts: znidGPON420x.setStatus('current')
znidNextGen = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10))
if mibBuilder.loadTexts: znidNextGen.setStatus('current')
znidNextGen22xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 1))
if mibBuilder.loadTexts: znidNextGen22xx.setStatus('current')
znidNextGenGE22xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 1, 1))
if mibBuilder.loadTexts: znidNextGenGE22xx.setStatus('current')
znidNextGen42xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2))
if mibBuilder.loadTexts: znidNextGen42xx.setStatus('current')
znidNextGenGPON42xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2, 1))
if mibBuilder.loadTexts: znidNextGenGPON42xx.setStatus('current')
znidNextGenGE42xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 2, 2))
if mibBuilder.loadTexts: znidNextGenGE42xx.setStatus('current')
znidNextGen9xxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3))
if mibBuilder.loadTexts: znidNextGen9xxx.setStatus('current')
znidNextGenGPON9xxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 1))
if mibBuilder.loadTexts: znidNextGenGPON9xxx.setStatus('current')
znidNextGenGE9xxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 2))
if mibBuilder.loadTexts: znidNextGenGE9xxx.setStatus('current')
znidNextGenGPON94xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 3))
if mibBuilder.loadTexts: znidNextGenGPON94xx.setStatus('current')
znidNextGenGE94xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 4))
if mibBuilder.loadTexts: znidNextGenGE94xx.setStatus('current')
znidNextGenGPON97xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 5))
if mibBuilder.loadTexts: znidNextGenGPON97xx.setStatus('current')
znidNextGenGE97xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 3, 6))
if mibBuilder.loadTexts: znidNextGenGE97xx.setStatus('current')
fiberJack = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 4))
if mibBuilder.loadTexts: fiberJack.setStatus('current')
znidNextGen21xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5))
if mibBuilder.loadTexts: znidNextGen21xx.setStatus('current')
znidNextGenGPON21xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5, 1))
if mibBuilder.loadTexts: znidNextGenGPON21xx.setStatus('current')
znidNextGenGE21xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 5, 2))
if mibBuilder.loadTexts: znidNextGenGE21xx.setStatus('current')
znidNextGen24xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6))
if mibBuilder.loadTexts: znidNextGen24xx.setStatus('current')
znidNextGenGPON24xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6, 1))
if mibBuilder.loadTexts: znidNextGenGPON24xx.setStatus('current')
znidNextGenGE24xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 6, 2))
if mibBuilder.loadTexts: znidNextGenGE24xx.setStatus('current')
znidNextGen26xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7))
if mibBuilder.loadTexts: znidNextGen26xx.setStatus('current')
znidNextGenGPON26xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7, 1))
if mibBuilder.loadTexts: znidNextGenGPON26xx.setStatus('current')
znidNextGenGE26xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 2, 10, 7, 2))
if mibBuilder.loadTexts: znidNextGenGE26xx.setStatus('current')
z_plex10B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 3, 1)).setLabel("z-plex10B")
if mibBuilder.loadTexts: z_plex10B.setStatus('current')
z_plex10B_FXS_FXO = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 1)).setLabel("z-plex10B-FXS-FXO")
if mibBuilder.loadTexts: z_plex10B_FXS_FXO.setStatus('current')
z_plex10B_FXS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 3, 1, 2)).setLabel("z-plex10B-FXS")
if mibBuilder.loadTexts: z_plex10B_FXS.setStatus('current')
sechtor_100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 4, 1)).setLabel("sechtor-100")
if mibBuilder.loadTexts: sechtor_100.setStatus('current')
s100_ATM_SM_16T1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 1)).setLabel("s100-ATM-SM-16T1")
if mibBuilder.loadTexts: s100_ATM_SM_16T1.setStatus('current')
s100_ATM_SM_16E1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 4, 1, 2)).setLabel("s100-ATM-SM-16E1")
if mibBuilder.loadTexts: s100_ATM_SM_16E1.setStatus('current')
sechtor_300 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 4, 2)).setLabel("sechtor-300")
if mibBuilder.loadTexts: sechtor_300.setStatus('current')
zhoneRegWtn = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5))
if mibBuilder.loadTexts: zhoneRegWtn.setStatus('current')
node5700Mhz = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 1))
if mibBuilder.loadTexts: node5700Mhz.setStatus('current')
skyZhone45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1))
if mibBuilder.loadTexts: skyZhone45.setStatus('current')
oduTypeA = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 1))
if mibBuilder.loadTexts: oduTypeA.setStatus('current')
oduTypeB = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 1, 1, 2))
if mibBuilder.loadTexts: oduTypeB.setStatus('current')
node23000Mhz = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2))
if mibBuilder.loadTexts: node23000Mhz.setStatus('current')
skyZhone8e1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1))
if mibBuilder.loadTexts: skyZhone8e1.setStatus('current')
oduTypeE1A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 1))
if mibBuilder.loadTexts: oduTypeE1A.setStatus('current')
oduTypeE1B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 1, 2))
if mibBuilder.loadTexts: oduTypeE1B.setStatus('current')
skyZhone8e2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2))
if mibBuilder.loadTexts: skyZhone8e2.setStatus('current')
oduTypeE2A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 1))
if mibBuilder.loadTexts: oduTypeE2A.setStatus('current')
oduTypeE2B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 2, 2))
if mibBuilder.loadTexts: oduTypeE2B.setStatus('current')
skyZhone8e3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3))
if mibBuilder.loadTexts: skyZhone8e3.setStatus('current')
oduTypeE3A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 1))
if mibBuilder.loadTexts: oduTypeE3A.setStatus('current')
oduTypeE3B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 3, 2))
if mibBuilder.loadTexts: oduTypeE3B.setStatus('current')
skyZhone8e4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4))
if mibBuilder.loadTexts: skyZhone8e4.setStatus('current')
oduTypeE4A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 1))
if mibBuilder.loadTexts: oduTypeE4A.setStatus('current')
oduTypeE4B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 4, 2))
if mibBuilder.loadTexts: oduTypeE4B.setStatus('current')
skyZhone8t1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5))
if mibBuilder.loadTexts: skyZhone8t1.setStatus('current')
oduTypeT1A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 1))
if mibBuilder.loadTexts: oduTypeT1A.setStatus('current')
oduTypeT1B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 5, 2))
if mibBuilder.loadTexts: oduTypeT1B.setStatus('current')
skyZhone8t2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6))
if mibBuilder.loadTexts: skyZhone8t2.setStatus('current')
oduTypeT2A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 1))
if mibBuilder.loadTexts: oduTypeT2A.setStatus('current')
oduTypeT2B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 6, 2))
if mibBuilder.loadTexts: oduTypeT2B.setStatus('current')
skyZhone8t3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7))
if mibBuilder.loadTexts: skyZhone8t3.setStatus('current')
oduTypeT3A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 1))
if mibBuilder.loadTexts: oduTypeT3A.setStatus('current')
oduTypeT3B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 7, 2))
if mibBuilder.loadTexts: oduTypeT3B.setStatus('current')
skyZhone8t4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8))
if mibBuilder.loadTexts: skyZhone8t4.setStatus('current')
oduTypeT4A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 1))
if mibBuilder.loadTexts: oduTypeT4A.setStatus('current')
oduTypeT4B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 8, 2))
if mibBuilder.loadTexts: oduTypeT4B.setStatus('current')
skyZhone155s1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9))
if mibBuilder.loadTexts: skyZhone155s1.setStatus('current')
oduTypeS1A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 1))
if mibBuilder.loadTexts: oduTypeS1A.setStatus('current')
oduTypeS1B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 9, 2))
if mibBuilder.loadTexts: oduTypeS1B.setStatus('current')
skyZhone155s2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10))
if mibBuilder.loadTexts: skyZhone155s2.setStatus('current')
oduTypeS2A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 1))
if mibBuilder.loadTexts: oduTypeS2A.setStatus('current')
oduTypeS2B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 10, 2))
if mibBuilder.loadTexts: oduTypeS2B.setStatus('current')
skyZhone155s3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11))
if mibBuilder.loadTexts: skyZhone155s3.setStatus('current')
oduTypeS3A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 1))
if mibBuilder.loadTexts: oduTypeS3A.setStatus('current')
oduTypeS3B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 11, 2))
if mibBuilder.loadTexts: oduTypeS3B.setStatus('current')
skyZhone155s4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12))
if mibBuilder.loadTexts: skyZhone155s4.setStatus('current')
oduTypeS4A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 1))
if mibBuilder.loadTexts: oduTypeS4A.setStatus('current')
oduTypeS4B = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 2, 12, 2))
if mibBuilder.loadTexts: oduTypeS4B.setStatus('current')
skyZhone1xxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 5, 3))
if mibBuilder.loadTexts: skyZhone1xxx.setStatus('current')
malc19 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 1))
if mibBuilder.loadTexts: malc19.setStatus('current')
malc23 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 2))
if mibBuilder.loadTexts: malc23.setStatus('current')
malc319 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 3))
if mibBuilder.loadTexts: malc319.setStatus('current')
raptor319A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 4))
if mibBuilder.loadTexts: raptor319A.setStatus('current')
raptor319I = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 5))
if mibBuilder.loadTexts: raptor319I.setStatus('current')
raptor719A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 6))
if mibBuilder.loadTexts: raptor719A.setStatus('current')
raptor719I = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 7))
if mibBuilder.loadTexts: raptor719I.setStatus('current')
raptor723A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 8))
if mibBuilder.loadTexts: raptor723A.setStatus('current')
raptor723I = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 9))
if mibBuilder.loadTexts: raptor723I.setStatus('current')
raptor100A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 10))
if mibBuilder.loadTexts: raptor100A.setStatus('current')
raptor100I = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 11))
if mibBuilder.loadTexts: raptor100I.setStatus('current')
raptor100LP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 12))
if mibBuilder.loadTexts: raptor100LP.setStatus('current')
raptor50Gshdsl = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 13))
if mibBuilder.loadTexts: raptor50Gshdsl.setStatus('current')
isc303 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 14))
if mibBuilder.loadTexts: isc303.setStatus('current')
r100adsl2Pxxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15))
if mibBuilder.loadTexts: r100adsl2Pxxx.setStatus('current')
r100adsl2pip = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 1))
if mibBuilder.loadTexts: r100adsl2pip.setStatus('current')
r100adsl2phdsl4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 2))
if mibBuilder.loadTexts: r100adsl2phdsl4.setStatus('current')
r100adsl2pt1ima = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 3))
if mibBuilder.loadTexts: r100adsl2pt1ima.setStatus('current')
r100adsl2pgige = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 4))
if mibBuilder.loadTexts: r100adsl2pgige.setStatus('current')
r100adsl2pgm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 5))
if mibBuilder.loadTexts: r100adsl2pgm.setStatus('obsolete')
r100adsl2pgte = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 6))
if mibBuilder.loadTexts: r100adsl2pgte.setStatus('obsolete')
r100adsl2panxb = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 15, 7))
if mibBuilder.loadTexts: r100adsl2panxb.setStatus('current')
m100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16))
if mibBuilder.loadTexts: m100.setStatus('current')
m100adsl2pxxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1))
if mibBuilder.loadTexts: m100adsl2pxxx.setStatus('current')
m100adsl2pgige = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 1))
if mibBuilder.loadTexts: m100adsl2pgige.setStatus('current')
m100adsl2pgm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 2))
if mibBuilder.loadTexts: m100adsl2pgm.setStatus('obsolete')
m100Adsl2pAnxB = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 1, 3))
if mibBuilder.loadTexts: m100Adsl2pAnxB.setStatus('current')
m100Vdsl2xxx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 2))
if mibBuilder.loadTexts: m100Vdsl2xxx.setStatus('obsolete')
m100vdsl2gm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 16, 2, 1))
if mibBuilder.loadTexts: m100vdsl2gm.setStatus('obsolete')
r100Vdsl2xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 17))
if mibBuilder.loadTexts: r100Vdsl2xx.setStatus('obsolete')
r100vdsl2gm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 17, 1))
if mibBuilder.loadTexts: r100vdsl2gm.setStatus('obsolete')
fiberSlam = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 18))
if mibBuilder.loadTexts: fiberSlam.setStatus('current')
fs105 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 18, 1))
if mibBuilder.loadTexts: fs105.setStatus('current')
fs101 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 18, 2))
if mibBuilder.loadTexts: fs101.setStatus('current')
raptorXP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19))
if mibBuilder.loadTexts: raptorXP.setStatus('current')
raptorXP150A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1))
if mibBuilder.loadTexts: raptorXP150A.setStatus('current')
raptorXP150A_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1, 1))
if mibBuilder.loadTexts: raptorXP150A_ISP.setStatus('current')
raptorXP150A_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 1, 2))
if mibBuilder.loadTexts: raptorXP150A_OSP.setStatus('current')
raptorXP350A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2))
if mibBuilder.loadTexts: raptorXP350A.setStatus('current')
raptorXP350A_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2, 1))
if mibBuilder.loadTexts: raptorXP350A_ISP.setStatus('current')
raptorXP350A_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 2, 2))
if mibBuilder.loadTexts: raptorXP350A_OSP.setStatus('current')
raptorXP160 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3))
if mibBuilder.loadTexts: raptorXP160.setStatus('current')
raptorXP160_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3, 1))
if mibBuilder.loadTexts: raptorXP160_ISP.setStatus('current')
raptorXP160_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 3, 2))
if mibBuilder.loadTexts: raptorXP160_OSP.setStatus('current')
raptorXP170 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4))
if mibBuilder.loadTexts: raptorXP170.setStatus('current')
raptorXP170_WC = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1))
if mibBuilder.loadTexts: raptorXP170_WC.setStatus('current')
raptorXP170_ISP_WC = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1, 1))
if mibBuilder.loadTexts: raptorXP170_ISP_WC.setStatus('current')
raptorXP170_OSP_WC = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 1, 2))
if mibBuilder.loadTexts: raptorXP170_OSP_WC.setStatus('current')
raptorXP170_WC_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2))
if mibBuilder.loadTexts: raptorXP170_WC_SD.setStatus('current')
raptorXP170_ISP_WC_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2, 1))
if mibBuilder.loadTexts: raptorXP170_ISP_WC_SD.setStatus('current')
raptorXP170_OSP_WC_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 2, 2))
if mibBuilder.loadTexts: raptorXP170_OSP_WC_SD.setStatus('current')
raptorXP170_LP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3))
if mibBuilder.loadTexts: raptorXP170_LP.setStatus('current')
raptorXP170_ISP_LP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3, 1))
if mibBuilder.loadTexts: raptorXP170_ISP_LP.setStatus('current')
raptorXP170_OSP_LP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 3, 2))
if mibBuilder.loadTexts: raptorXP170_OSP_LP.setStatus('current')
raptorXP170_LP_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4))
if mibBuilder.loadTexts: raptorXP170_LP_SD.setStatus('current')
raptorXP170_ISP_LP_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4, 1))
if mibBuilder.loadTexts: raptorXP170_ISP_LP_SD.setStatus('current')
raptorXP170_OSP_LP_SD = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 19, 4, 4, 2))
if mibBuilder.loadTexts: raptorXP170_OSP_LP_SD.setStatus('current')
malcXP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20))
if mibBuilder.loadTexts: malcXP.setStatus('current')
malcXP150A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1))
if mibBuilder.loadTexts: malcXP150A.setStatus('current')
malcXP150A_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1, 1))
if mibBuilder.loadTexts: malcXP150A_ISP.setStatus('current')
malcXP150A_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 1, 2))
if mibBuilder.loadTexts: malcXP150A_OSP.setStatus('current')
malcXP350A = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4))
if mibBuilder.loadTexts: malcXP350A.setStatus('current')
malcXP350A_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4, 1))
if mibBuilder.loadTexts: malcXP350A_ISP.setStatus('current')
malcXP350A_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 4, 2))
if mibBuilder.loadTexts: malcXP350A_OSP.setStatus('current')
malcXP160 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5))
if mibBuilder.loadTexts: malcXP160.setStatus('current')
malcXP160_ISP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5, 1))
if mibBuilder.loadTexts: malcXP160_ISP.setStatus('current')
malcXP160_OSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 6, 20, 5, 2))
if mibBuilder.loadTexts: malcXP160_OSP.setStatus('current')
zhoneRegMxNextGen = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7))
if mibBuilder.loadTexts: zhoneRegMxNextGen.setStatus('current')
mx19 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 1))
if mibBuilder.loadTexts: mx19.setStatus('current')
mx23 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 2))
if mibBuilder.loadTexts: mx23.setStatus('current')
mx319 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 3))
if mibBuilder.loadTexts: mx319.setStatus('current')
mx1U = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4))
if mibBuilder.loadTexts: mx1U.setStatus('current')
mx1Ux6x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1))
if mibBuilder.loadTexts: mx1Ux6x.setStatus('current')
mx1U16x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1))
if mibBuilder.loadTexts: mx1U16x.setStatus('current')
mx1U160 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 1))
if mibBuilder.loadTexts: mx1U160.setStatus('current')
mx1U161 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 2))
if mibBuilder.loadTexts: mx1U161.setStatus('current')
mx1U162 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 1, 3))
if mibBuilder.loadTexts: mx1U162.setStatus('current')
mx1U26x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2))
if mibBuilder.loadTexts: mx1U26x.setStatus('current')
mx1U260 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 1))
if mibBuilder.loadTexts: mx1U260.setStatus('current')
mx1U261 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 2))
if mibBuilder.loadTexts: mx1U261.setStatus('current')
mx1U262 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 1, 2, 3))
if mibBuilder.loadTexts: mx1U262.setStatus('current')
mx1Ux80 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2))
if mibBuilder.loadTexts: mx1Ux80.setStatus('current')
mx1U180 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 1))
if mibBuilder.loadTexts: mx1U180.setStatus('current')
mx1U280 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 2))
if mibBuilder.loadTexts: mx1U280.setStatus('current')
mx1U180_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 3))
if mibBuilder.loadTexts: mx1U180_TP_RJ45.setStatus('current')
mx1U280_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 4))
if mibBuilder.loadTexts: mx1U280_TP_RJ45.setStatus('current')
mx1U180_LT_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 5))
if mibBuilder.loadTexts: mx1U180_LT_TP_RJ45.setStatus('current')
mx1U280_LT_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 2, 6))
if mibBuilder.loadTexts: mx1U280_LT_TP_RJ45.setStatus('current')
mx1U19x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3))
if mibBuilder.loadTexts: mx1U19x.setStatus('current')
mx1U194 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 1))
if mibBuilder.loadTexts: mx1U194.setStatus('current')
mx1U198 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 2))
if mibBuilder.loadTexts: mx1U198.setStatus('current')
mx1U194_10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 3))
if mibBuilder.loadTexts: mx1U194_10GE.setStatus('current')
mx1U198_10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 4))
if mibBuilder.loadTexts: mx1U198_10GE.setStatus('current')
mx1U194_TOP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 5))
if mibBuilder.loadTexts: mx1U194_TOP.setStatus('current')
mx1U198_TOP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 6))
if mibBuilder.loadTexts: mx1U198_TOP.setStatus('current')
mx1U194_10GE_TOP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 7))
if mibBuilder.loadTexts: mx1U194_10GE_TOP.setStatus('current')
mx1U198_10GE_TOP = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 3, 8))
if mibBuilder.loadTexts: mx1U198_10GE_TOP.setStatus('current')
mx1Ux5x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4))
if mibBuilder.loadTexts: mx1Ux5x.setStatus('current')
mx1U15x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1))
if mibBuilder.loadTexts: mx1U15x.setStatus('current')
mx1U150 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 1))
if mibBuilder.loadTexts: mx1U150.setStatus('current')
mx1U151 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 2))
if mibBuilder.loadTexts: mx1U151.setStatus('current')
mx1U152 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 4, 4, 1, 3))
if mibBuilder.loadTexts: mx1U152.setStatus('current')
mxp1U = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5))
if mibBuilder.loadTexts: mxp1U.setStatus('current')
mxp1Ux60 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1))
if mibBuilder.loadTexts: mxp1Ux60.setStatus('current')
mxp1U160Family = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 1))
if mibBuilder.loadTexts: mxp1U160Family.setStatus('current')
mxp1U160 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 1, 1))
if mibBuilder.loadTexts: mxp1U160.setStatus('current')
mxp1U260Family = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 2))
if mibBuilder.loadTexts: mxp1U260Family.setStatus('current')
mxp1U260 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 1, 2, 1))
if mibBuilder.loadTexts: mxp1U260.setStatus('current')
mxp1Ux80 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2))
if mibBuilder.loadTexts: mxp1Ux80.setStatus('current')
mxp1U180 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 1))
if mibBuilder.loadTexts: mxp1U180.setStatus('current')
mxp1U280 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 2))
if mibBuilder.loadTexts: mxp1U280.setStatus('current')
mxp1U180_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 3))
if mibBuilder.loadTexts: mxp1U180_TP_RJ45.setStatus('current')
mxp1U280_TP_RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 2, 4))
if mibBuilder.loadTexts: mxp1U280_TP_RJ45.setStatus('current')
mxp1Ux5x = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3))
if mibBuilder.loadTexts: mxp1Ux5x.setStatus('current')
mxp1U15xFamily = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3, 1))
if mibBuilder.loadTexts: mxp1U15xFamily.setStatus('current')
mxp1U150 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 1, 7, 5, 3, 1, 1))
if mibBuilder.loadTexts: mxp1U150.setStatus('current')
mibBuilder.exportSymbols("ZhoneProductRegistrations", malc19=malc19, raptorXP170_OSP_WC=raptorXP170_OSP_WC, raptorXP150A_ISP=raptorXP150A_ISP, raptorXP170_LP=raptorXP170_LP, malcXP=malcXP, mxp1Ux5x=mxp1Ux5x, mx1U162=mx1U162, mxp1U150=mxp1U150, oduTypeE2B=oduTypeE2B, raptorXP150A=raptorXP150A, mx1U194_TOP=mx1U194_TOP, oduTypeS3B=oduTypeS3B, mxp1U180_TP_RJ45=mxp1U180_TP_RJ45, z_plex10B=z_plex10B, zedge64_SHDSL_FXS=zedge64_SHDSL_FXS, mxp1U180=mxp1U180, znidNextGenGPON42xx=znidNextGenGPON42xx, zedge6200_IP_FXS=zedge6200_IP_FXS, fs105=fs105, raptorXP350A=raptorXP350A, malc319=malc319, mx1U280_TP_RJ45=mx1U280_TP_RJ45, oduTypeT3B=oduTypeT3B, zrg6xx=zrg6xx, zrg8xx=zrg8xx, r100adsl2pt1ima=r100adsl2pt1ima, zedge6200_IP_T1=zedge6200_IP_T1, znidGPON42xx=znidGPON42xx, znidNextGen26xx=znidNextGen26xx, ethXtendShdsl=ethXtendShdsl, oduTypeT3A=oduTypeT3A, oduTypeE4A=oduTypeE4A, m100adsl2pgm=m100adsl2pgm, m100adsl2pgige=m100adsl2pgige, mx1U194_10GE_TOP=mx1U194_10GE_TOP, znidNextGenGPON26xx=znidNextGenGPON26xx, malc23=malc23, raptorXP170_OSP_LP_SD=raptorXP170_OSP_LP_SD, znid=znid, znidNextGenGE94xx=znidNextGenGE94xx, raptorXP170_WC=raptorXP170_WC, skyZhone8t2=skyZhone8t2, node23000Mhz=node23000Mhz, oduTypeS4B=oduTypeS4B, mxp1U160Family=mxp1U160Family, oduTypeE1A=oduTypeE1A, r100Vdsl2xx=r100Vdsl2xx, z_plex10B_FXS_FXO=z_plex10B_FXS_FXO, fiberSlam=fiberSlam, zrg300_ODU=zrg300_ODU, oduTypeT1A=oduTypeT1A, oduTypeE3B=oduTypeE3B, zedge64=zedge64, mx1U161=mx1U161, mx1U280_LT_TP_RJ45=mx1U280_LT_TP_RJ45, mxp1U260=mxp1U260, oduTypeS1A=oduTypeS1A, znidEth422x=znidEth422x, fs101=fs101, raptor319I=raptor319I, ethXtendxx=ethXtendxx, r100adsl2pgm=r100adsl2pgm, r100adsl2pgte=r100adsl2pgte, mx1U198=mx1U198, zedge6200=zedge6200, raptorXP170_WC_SD=raptorXP170_WC_SD, oduTypeS2B=oduTypeS2B, mx1Ux80=mx1Ux80, node5700Mhz=node5700Mhz, zedge64_SHDSL_BRI=zedge64_SHDSL_BRI, mx1U262=mx1U262, znidNextGenGE22xx=znidNextGenGE22xx, mxp1Ux80=mxp1Ux80, mx1U151=mx1U151, oduTypeA=oduTypeA, mx19=mx19, znidNextGen=znidNextGen, raptor719I=raptor719I, mx1U198_10GE=mx1U198_10GE, r100vdsl2gm=r100vdsl2gm, zrg300_IDU=zrg300_IDU, mx1U=mx1U, skyZhone155s3=skyZhone155s3, raptorXP170_ISP_LP=raptorXP170_ISP_LP, skyZhone8e1=skyZhone8e1, r100adsl2pgige=r100adsl2pgige, mx1U180_LT_TP_RJ45=mx1U180_LT_TP_RJ45, znidNextGenGPON24xx=znidNextGenGPON24xx, zrg700_ODU=zrg700_ODU, zrg600_ODU=zrg600_ODU, znidNextGenGPON94xx=znidNextGenGPON94xx, zedge6200_IP_EM=zedge6200_IP_EM, skyZhone8e2=skyZhone8e2, sechtor_100=sechtor_100, znidNextGen22xx=znidNextGen22xx, znidNextGenGE26xx=znidNextGenGE26xx, raptorXP160_ISP=raptorXP160_ISP, raptorXP170_LP_SD=raptorXP170_LP_SD, raptorXP170_ISP_LP_SD=raptorXP170_ISP_LP_SD, mx1Ux5x=mx1Ux5x, znidNextGen21xx=znidNextGen21xx, zrg500_ODU=zrg500_ODU, oduTypeE3A=oduTypeE3A, malcXP350A=malcXP350A, s100_ATM_SM_16E1=s100_ATM_SM_16E1, mx23=mx23, zrg800_IDU=zrg800_IDU, znidNextGenGPON9xxx=znidNextGenGPON9xxx, PYSNMP_MODULE_ID=zhoneRegistrationsModule, oduTypeT4A=oduTypeT4A, ethXtend30xx=ethXtend30xx, ethXtend32xx=ethXtend32xx, sechtor_300=sechtor_300, oduTypeT1B=oduTypeT1B, s100_ATM_SM_16T1=s100_ATM_SM_16T1, mxp1Ux60=mxp1Ux60, znidNextGen24xx=znidNextGen24xx, znidNextGenGE97xx=znidNextGenGE97xx, raptor723I=raptor723I, mxp1U280=mxp1U280, skyZhone45=skyZhone45, zedge64_T1_FXS=zedge64_T1_FXS, m100=m100, zrg800_ODU=zrg800_ODU, oduTypeS3A=oduTypeS3A, mx1U180_TP_RJ45=mx1U180_TP_RJ45, raptorXP170_OSP_LP=raptorXP170_OSP_LP, mx1U198_TOP=mx1U198_TOP, oduTypeT2A=oduTypeT2A, mx1U198_10GE_TOP=mx1U198_10GE_TOP, fiberJack=fiberJack, mx1U194_10GE=mx1U194_10GE, zhoneRegistrationsModule=zhoneRegistrationsModule, zrg500_IDU=zrg500_IDU, r100adsl2pip=r100adsl2pip, skyZhone8e4=skyZhone8e4, oduTypeB=oduTypeB, skyZhone1xxx=skyZhone1xxx, raptorXP170_ISP_WC_SD=raptorXP170_ISP_WC_SD, skyZhone155s2=skyZhone155s2, malcXP160_OSP=malcXP160_OSP, mx1U16x=mx1U16x, oduTypeT4B=oduTypeT4B, skyZhone8t1=skyZhone8t1, znid42xx=znid42xx, mx1U160=mx1U160, mx1U261=mx1U261, ethXtend31xx=ethXtend31xx, raptor723A=raptor723A, zrg700_IDU=zrg700_IDU, r100adsl2phdsl4=r100adsl2phdsl4, zrg600_IDU=zrg600_IDU, oduTypeE4B=oduTypeE4B, raptorXP160=raptorXP160, zhoneRegMxNextGen=zhoneRegMxNextGen, mx1U26x=mx1U26x, znidNextGenGE42xx=znidNextGenGE42xx, mx1U280=mx1U280, raptorXP170_ISP_WC=raptorXP170_ISP_WC, znidGPON420x=znidGPON420x, oduTypeS4A=oduTypeS4A, raptorXP170_OSP_WC_SD=raptorXP170_OSP_WC_SD, raptorXP150A_OSP=raptorXP150A_OSP, mx1U180=mx1U180, oduTypeE1B=oduTypeE1B, mx1U15x=mx1U15x, malcXP350A_ISP=malcXP350A_ISP, malcXP150A=malcXP150A, r100adsl2panxb=r100adsl2panxb, mx1U152=mx1U152, zrg7xx=zrg7xx, znidNextGenGPON97xx=znidNextGenGPON97xx, ban_2000=ban_2000, mx1U19x=mx1U19x, znidNextGen42xx=znidNextGen42xx, znidNextGenGPON21xx=znidNextGenGPON21xx, malcXP150A_ISP=malcXP150A_ISP, oduTypeT2B=oduTypeT2B, raptor319A=raptor319A, mx1U194=mx1U194, raptor719A=raptor719A, skyZhone155s4=skyZhone155s4, mxp1U=mxp1U, skyZhone8t3=skyZhone8t3, zrg5xx=zrg5xx, oduTypeS1B=oduTypeS1B, raptor100LP=raptor100LP, malcXP160=malcXP160, r100adsl2Pxxx=r100adsl2Pxxx, mxp1U15xFamily=mxp1U15xFamily, m100vdsl2gm=m100vdsl2gm, skyZhone8e3=skyZhone8e3, raptor100A=raptor100A, m100Vdsl2xxx=m100Vdsl2xxx, znidNextGen9xxx=znidNextGen9xxx, mx319=mx319, raptorXP160_OSP=raptorXP160_OSP, z_plex10B_FXS=z_plex10B_FXS, mxp1U260Family=mxp1U260Family, raptorXP170=raptorXP170, skyZhone155s1=skyZhone155s1, malcXP150A_OSP=malcXP150A_OSP, mx1U260=mx1U260, malcXP350A_OSP=malcXP350A_OSP, isc303=isc303, zedge64_E1_FXS=zedge64_E1_FXS, mxp1U160=mxp1U160, znidNextGenGE9xxx=znidNextGenGE9xxx, mx1U150=mx1U150, raptor50Gshdsl=raptor50Gshdsl, mx1Ux6x=mx1Ux6x, skyZhone8t4=skyZhone8t4, raptorXP350A_ISP=raptorXP350A_ISP, mxp1U280_TP_RJ45=mxp1U280_TP_RJ45, oduTypeE2A=oduTypeE2A, malcXP160_ISP=malcXP160_ISP, znid420x=znid420x, oduTypeS2A=oduTypeS2A, raptorXP350A_OSP=raptorXP350A_OSP, m100adsl2pxxx=m100adsl2pxxx, m100Adsl2pAnxB=m100Adsl2pAnxB, znidNextGenGE21xx=znidNextGenGE21xx, znidNextGenGE24xx=znidNextGenGE24xx, raptorXP=raptorXP, zhoneRegWtn=zhoneRegWtn, ethXtendT1E1=ethXtendT1E1, raptor100I=raptor100I, zrg3xx=zrg3xx)
