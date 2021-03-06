#
# PySNMP MIB module AT-BOARDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-BOARDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
objects, = mibBuilder.importSymbols("AT-SMI-MIB", "objects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Gauge32, Counter64, Unsigned32, iso, ObjectIdentity, IpAddress, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "iso", "ObjectIdentity", "IpAddress", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
boards = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1))
boards.setRevisions(('2013-08-01 00:00', '2013-07-09 00:00', '2012-06-07 00:00', '2012-05-21 00:00', '2012-05-15 00:00', '2012-03-16 00:00', '2011-12-18 05:00', '2011-10-25 00:00', '2011-09-20 00:00', '2011-09-15 00:00', '2011-09-14 00:00', '2011-09-05 00:00', '2011-05-10 00:00', '2011-04-28 00:00', '2011-04-04 00:00', '2011-03-08 00:00', '2010-12-01 00:00', '2010-10-12 00:00', '2010-09-07 00:00', '2010-08-19 00:00', '2010-07-22 00:00', '2010-06-14 04:45', '2010-05-19 00:00', '2009-05-15 00:00', '2008-12-11 00:00', '2008-11-24 00:00', '2008-03-03 15:00', '2007-03-21 00:00', '2007-02-07 00:00', '2006-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: boards.setRevisionsDescriptions(('Added x930s (IDs 388-392), x310s (IDs 393-400) and x230s (IDs 401-409)', 'Added board ID for pprx510DP52GTX, pprIX528GPX, pprPWR100R and pprPWR250DCR', 'Correct a typo for the name from pprXumStk to pprXemStk', 'Added pprAtSBx81XZ4 for the SBx8112', 'Changed the board name from pprAtSBx81XZ6 to pprAtSBx81XS6 and pprAtSBx81GS24 to pprAtSBx81GS24a', 'Added board ID for x510 series.', 'Added pprSBx81CFC960, pprSBx81GT24a, pprSBx81GP24a, pprSBx81GT40 and pprSBx81XS16boards for the SBx8112', 'Added AT-SBx81FAN06', 'Added SBx8100 card products.', 'Added AT-SBx8106 product.', 'Added AT-SBx8112 product.', 'Added board ID for x210-9GT, x210-16GT, x210-24GT.', 'Added board ID for pprXem2XS, pprXem24T, pprXem12Tv2, pprXem12Sv2.', 'Added pics AR030 AR031', 'Added Rapier 48x product', 'Corrected syntax problems.', 'Added board ID for pprPWR250DC.', 'Added pprx200GE52T and pprx200GE28T', 'Generic syntax tidy up', 'Added board 330 pprAR560', 'Renamed boardID pprx60024TSPOE220WPSU to pprx60024TSPOEPLUS', 'MIB revision history dates in descriptions updated.', 'x610 product range, added pprx61048TsPOEPlus, pprx61024TsXPOEPlus, pprx61024TsPOEPlus, pprPWR800, pprPWR1200, pprPWR250, pprx61048TsX, pprx61048Ts, pprx61024TsX, pprx61024Ts, and pprx61024SPX', 'Added boardID for pprx60024TSPOE and pprx60024TSPOE220WPSU.', 'Added boardID for pprXum100M, pprAtPWR05AC, pprAtPWR05DC and pprXem2XT.', 'Added boardID for x60024TS,x60024TSXP,x60048TS and x60048TSXP.', 'Change Added boards 271,272,282,284-286,288. Added boards 290-297, Added boards 300,304-311.', 'Added boardID for x900-48FS.', 'Added boardID for AT-8824R.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: boards.setLastUpdated('201308010000Z')
if mibBuilder.loadTexts: boards.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: boards.setContactInfo(' http://www.alliedtelesis.com')
if mibBuilder.loadTexts: boards.setDescription('OID boards is a subtree beneath which board ids are assigned. release is a subtree beneath which release ids are assigned. ifTypes is a subtree beneath which interface type ids are assigned. chips is a subtree beneath which chip ids are assigned.')
pprIcmAr023 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 39))
pprIcmAr021s = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 40))
pprIcmAr022 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 41))
pprIcmAr025 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 45))
pprIcmAr024 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 46))
pprAr300 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 49))
pprAr300L = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 52))
pprAr310 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 53))
pprAr120 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 54))
pprAr300Lu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 55))
pprAr300u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 56))
pprAr310u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 57))
pprAr350 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 58))
pprIcmAr021u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 59))
pprAr720 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 63))
pprAr010 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 67))
pprAr012 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 68))
pprAr011 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 69))
pprAr370 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 70))
pprAr330 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 71))
pprAr395 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 72))
pprAr390 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 73))
pprAr370u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 75))
pprIcmAr020 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 76))
pprAr740 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 79))
pprAr140s = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 80))
pprAr140u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 81))
pprAr160su = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 82))
pprAr320 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 83))
pprAr130s = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 85))
pprAr130u = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 86))
pprRapier24 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 87))
pprNsm0404Pic = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 88))
pprA35SXSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 89))
pprA35LXSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 90))
pprA36MTRJ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 91))
pprA37VF45 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 92))
pprA38LC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 93))
pprA39Tx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 94))
pprAr740DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 95))
pprNsm0418BRI = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 96))
pprRapier16fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 97))
ppr8624xl80 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 98))
pprRapier16fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 99))
pprRapier16fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 100))
pprRapier8t8fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 101))
pprRapier8t8fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 102))
pprRapier8t8fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 103))
pprRapier8t8fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 104))
pprRapier8fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 105))
pprRapier8fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 106))
pprRapier8fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 107))
pprRapier8fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 108))
pprRapierG6 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 110))
pprRapierG6SX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 111))
pprRapierG6LX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 112))
pprRapierG6MT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 113))
pprRapier16fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 114))
pprRapier24i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 115))
pprAr824 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 116))
pprAr816fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 117))
pprAr816fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 118))
pprAr816fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 119))
pprAr816fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 120))
pprAr88t8fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 121))
pprAr88t8fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 122))
pprAr88t8fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 123))
pprAr88t8fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 124))
pprAr88fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 125))
pprAr88fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 126))
pprAr88fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 127))
pprAr88fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 128))
pprAr824i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 129))
pprAt8724XL = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 130))
pprAt8748XL = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 131))
pprAt8724XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 132))
pprAt8748XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 133))
pprAt8824 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 134))
pprAt8824DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 135))
ppr8724XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 141))
ppr8748XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 142))
pprRapier24iDC_NEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 144))
pprAt8724XLDC_NEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 146))
pprAt8848DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 147))
pprRapier48 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 148))
pprAt8848 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 149))
pprRapier48i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 150))
pprNsm0424BRI = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 151))
pprIcmAR026 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 153))
ppr9816GF = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 157))
ppr9812TF = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 158))
pprSbChassis4AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 159))
pprSbChassis4DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 160))
pprSbChassis8AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 161))
pprSbChassis8DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 162))
pprSbChassis16AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 163))
pprSbChassis16DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 164))
pprSbControl = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 165))
pprSbControlDTM = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 166))
pprSb48t = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 167))
pprSb96t = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 168))
pprSb32fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 169))
pprSb32fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 170))
pprSb8fRJ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 172))
pprSb8fSXSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 173))
pprSb8fSXMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 174))
pprSb8fLXSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 175))
pprSb8fLXMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 176))
pprAr410 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 177))
pprA40SC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 178))
pprA40MTRJ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 179))
pprA41SC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 180))
pprA41MTRJ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 181))
pprAr725 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 182))
pprAr745 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 183))
pprSb8GBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 184))
pprA42GBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 185))
ppr9816GB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 186))
ppr9812T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 187))
pprNsm048DS3 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 188))
pprAr450 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 191))
pprAr450Dual = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 192))
pprSbExpander = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 193))
pprAr725DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 194))
pprAr745DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 195))
pprAr410v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 196))
pprAr410v3 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 197))
pprIcmAr027 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 198))
ppr8948EX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 202))
ppr8948i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 203))
ppr9816GBDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 204))
ppr9812TDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 205))
pprIcmAr021v2s = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 206))
pprA50 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 207))
pprA51 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 208))
pprA52 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 209))
pprA53 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 210))
pprFanA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 212))
pprAtPwr01AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 213))
pprAtPwr01DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 214))
pprAtFan01 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 215))
pprSb24RJ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 216))
pprSb1XFP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 217))
ppr9924T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 218))
ppr9924SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 219))
ppr9924TEMC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 220))
ppr9924T4SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 221))
pprAR440 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 227))
pprAR441 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 228))
pprAR442 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 229))
pprAR443 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 230))
pprAR444 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 231))
pprAR420 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 232))
pprAt8624T2M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 239))
pprA46Tx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 240))
pprAR550 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 241))
pprAR551 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 242))
pprAR552 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 243))
pprC8724MLB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 248))
pprAt86482SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 252))
pprAt8624POE = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 253))
pprAtPwr01RAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 254))
pprAtFan01R = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 255))
ppr9924Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 256))
pprAR570 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 258))
pprAtPwr02AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 264))
pprAtPwr02RAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 265))
pprAtXum10G = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 266))
pprAtXum12T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 267))
pprAtXum12SFP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 268))
pprSb24SFP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 269))
pprAR770 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 270))
pprx90024XT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 271))
pprx90024XS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 272))
pprAtXum10Gi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 273))
pprAtXum12SFPi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 274))
pprAtXum12Ti = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 275))
pprAR415S = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 276))
pprAR415SDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 277))
pprAR550SDP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 278))
ppr8948iN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 279))
pprAtXum12TiN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 280))
pprx90024XTN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 281))
pprSwitchBladex908 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 282))
pprRapier48w = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 283))
pprAt8316XLCR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 284))
pprAt8324XLCR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 285))
pprXemStk = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 286))
pprAt8824R = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 287))
pprx90012XTS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 288))
pprX90048FS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 289))
pprx60024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 290))
pprx60024TSXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 291))
pprAt9724TS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 292))
pprAt9724TSXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 293))
pprx60048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 294))
pprx60048TSXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 295))
pprAt9748TS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 296))
pprAt9748TSXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 297))
pprXum100M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 298))
pprAtPWR05AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 299))
pprIcmAr021v3s = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 300))
pprRapier48wb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 301))
pprRapier48wAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 302))
pprRapier48wbAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 303))
pprX30024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 304))
pprXemPOE = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 305))
pprXem2XP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 306))
pprATStackXG = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 307))
pprATEMXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 308))
pprATLBM = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 309))
pprAt8624TCR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 310))
pprAt8624POECR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 311))
pprAtSBx8112 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 316))
pprAtSBx81CFC400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 317))
pprAtSBx81GP24 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 318))
pprAtSBx81XZ4 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 319))
pprAtSBx8161SYSAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 320))
pprAtSBx8165POEAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 321))
pprAtSBx81FAN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 322))
pprAtPWR05DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 323))
pprXem2XT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 325))
pprx60024TSPOE = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 326))
pprx60024TSPOEPLUS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 327))
pprAR560 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 330))
pprx61048TsXPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 331))
pprx61048TsPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 332))
pprx61024TsXPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 333))
pprx61024TsPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 334))
pprPWR800 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 336))
pprPWR1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 337))
pprPWR250 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 338))
pprx61048TsX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 339))
pprx61048Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 340))
pprx61024TsX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 341))
pprx61024Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 342))
pprx61024SPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 343))
pprRapier48xDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 345))
pprAR030 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 347))
pprx200GE52T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 348))
pprx200GE28T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 349))
pprXem2XS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 350))
pprPWR250DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 351))
pprAtSBx81GT24 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 352))
pprAtSBx81GS24a = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 353))
pprAtSBx81XS6 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 354))
pprXem24T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 356))
pprAR031 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 357))
pprXem12Tv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 358))
pprXem12Sv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 359))
pprx2109GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 367))
pprx21016GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 368))
pprx21024GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 369))
pprx51028GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 370))
pprx51028GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 371))
pprx51028GSX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 372))
pprx51052GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 373))
pprx51052GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 374))
pprAtSBx8106 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 375))
pprAtSBx81FAN06 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 376))
pprSBx81CFC960 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 377))
pprSBx81GT24a = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 378))
pprSBx81GP24a = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 379))
pprSBx81GT40 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 381))
pprSBx81XS16 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 382))
pprPWR100R = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 384))
pprPWR250DCR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 385))
pprx510DP52GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 386))
pprIX528GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 387))
pprx93028GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 388))
pprx93028GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 389))
pprx93028GSX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 390))
pprx93052GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 391))
pprx93052GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 392))
pprx31026FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 393))
pprx31050FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 394))
pprx31026FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 395))
pprx31050FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 396))
pprx31026GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 397))
pprx31050GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 398))
pprx31026GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 399))
pprx31050GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 400))
pprx23010GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 401))
pprx23018GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 402))
pprx23028GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 403))
pprx23052GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 404))
pprx23010GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 405))
pprx23018GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 406))
pprx23028GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 407))
pprx23052GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 408))
pprx23010GPT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 1, 409))
release = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 2))
iftypes = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3))
ifaceEth = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 1))
ifaceSyn = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 2))
ifaceAsyn = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 3))
ifaceBri = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 4))
ifacePri = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 5))
ifacePots = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 6))
ifaceGBIC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 3, 7))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4))
chip68020Cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 1))
chip68340Cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 2))
chip68302Cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 3))
chip68360Cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 4))
chip860TCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 5))
chipRtc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 21))
chipRtc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 22))
chipRtc3 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 23))
chipRtc4 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 24))
chipRam1mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 31))
chipRam2mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 32))
chipRam3mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 33))
chipRam4mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 34))
chipRam6mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 36))
chipRam8mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 38))
chipRam12mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 42))
chipRam16mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 46))
chipRam20mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 50))
chipRam32mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 62))
chipFlash1mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 71))
chipFlash2mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 72))
chipFlash3mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 73))
chipFlash4mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 74))
chipFlash6mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 76))
chipFlash8mb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 78))
chipPem = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1, 4, 120))
mibBuilder.exportSymbols("AT-BOARDS-MIB", chipRam32mb=chipRam32mb, pprRapier48wb=pprRapier48wb, pprAt8624TCR=pprAt8624TCR, pprAt8824DC=pprAt8824DC, chipRam8mb=chipRam8mb, pprx60048TSXP=pprx60048TSXP, pprRapier16fMTi=pprRapier16fMTi, pprRapierG6=pprRapierG6, pprAt9748TS=pprAt9748TS, pprx90012XTS=pprx90012XTS, pprx61024Ts=pprx61024Ts, pprSbChassis4AC=pprSbChassis4AC, pprRapier48i=pprRapier48i, ppr9924SP=ppr9924SP, chipRam20mb=chipRam20mb, pprAR420=pprAR420, pprRapier24=pprRapier24, pprx93052GTX=pprx93052GTX, pprRapier8fSC=pprRapier8fSC, pprAr320=pprAr320, pprx200GE28T=pprx200GE28T, pprx23018GT=pprx23018GT, ppr9816GF=ppr9816GF, pprAr740DC=pprAr740DC, pprAr745=pprAr745, pprAr330=pprAr330, pprAr300Lu=pprAr300Lu, pprAt8824=pprAt8824, pprAr410v3=pprAr410v3, pprx51028GTX=pprx51028GTX, pprAr390=pprAr390, pprAtSBx81FAN=pprAtSBx81FAN, pprAr740=pprAr740, pprA36MTRJ=pprA36MTRJ, pprA42GBIC=pprA42GBIC, pprSbChassis8DC=pprSbChassis8DC, pprRapier8t8fMTi=pprRapier8t8fMTi, pprRapier8t8fSC=pprRapier8t8fSC, pprAr410v2=pprAr410v2, pprSbControl=pprSbControl, pprIcmAr025=pprIcmAr025, pprAr350=pprAr350, pprx31050GT=pprx31050GT, pprAR444=pprAR444, pprx23052GP=pprx23052GP, pprXem24T=pprXem24T, pprSwitchBladex908=pprSwitchBladex908, pprAtSBx81XZ4=pprAtSBx81XZ4, pprXem12Tv2=pprXem12Tv2, pprAt8724XLDC_NEBS=pprAt8724XLDC_NEBS, pprRapier8fMTi=pprRapier8fMTi, pprAr370u=pprAr370u, pprAtPwr01AC=pprAtPwr01AC, pprAt86482SP=pprAt86482SP, pprRapier8fMT=pprRapier8fMT, pprx510DP52GTX=pprx510DP52GTX, pprIX528GPX=pprIX528GPX, pprx31026GT=pprx31026GT, pprAt9724TS=pprAt9724TS, pprA39Tx=pprA39Tx, pprAt8848=pprAt8848, pprx23010GP=pprx23010GP, pprIcmAr024=pprIcmAr024, pprRapier48wbAC=pprRapier48wbAC, ppr8748XLDC=ppr8748XLDC, chips=chips, pprXem2XT=pprXem2XT, pprNsm0424BRI=pprNsm0424BRI, pprx61048Ts=pprx61048Ts, pprAr450=pprAr450, chipRam12mb=chipRam12mb, chipFlash6mb=chipFlash6mb, pprAr88fMT=pprAr88fMT, pprAtXum12Ti=pprAtXum12Ti, pprAr824i=pprAr824i, pprAtSBx81FAN06=pprAtSBx81FAN06, pprAr88t8fMT=pprAr88t8fMT, pprSb96t=pprSb96t, pprx31026FT=pprx31026FT, pprA51=pprA51, pprA40MTRJ=pprA40MTRJ, pprSBx81GT40=pprSBx81GT40, pprXem12Sv2=pprXem12Sv2, pprAtXum10Gi=pprAtXum10Gi, pprRapier16fSCi=pprRapier16fSCi, pprx61048TsXPOEPlus=pprx61048TsXPOEPlus, pprAr816fSCi=pprAr816fSCi, pprAr725DC=pprAr725DC, pprPWR250DCR=pprPWR250DCR, pprAr410=pprAr410, pprRapier48xDC=pprRapier48xDC, pprRapier24iDC_NEBS=pprRapier24iDC_NEBS, pprAtPwr02AC=pprAtPwr02AC, pprFanA01=pprFanA01, ppr9924Ts=ppr9924Ts, pprPWR250DC=pprPWR250DC, pprA35LXSC=pprA35LXSC, pprSBx81XS16=pprSBx81XS16, pprAr88fMTi=pprAr88fMTi, pprAtPWR05DC=pprAtPWR05DC, pprX90048FS=pprX90048FS, pprx2109GT=pprx2109GT, pprAtPwr01DC=pprAtPwr01DC, pprx23018GP=pprx23018GP, pprAr010=pprAr010, pprx61024TsX=pprx61024TsX, pprx51052GTX=pprx51052GTX, pprRapier16fSC=pprRapier16fSC, ifaceAsyn=ifaceAsyn, pprA35SXSC=pprA35SXSC, pprAt8724XLDC=pprAt8724XLDC, pprx90024XS=pprx90024XS, pprRapierG6SX=pprRapierG6SX, iftypes=iftypes, pprAr160su=pprAr160su, pprAr395=pprAr395, chip68360Cpu=chip68360Cpu, pprNsm0404Pic=pprNsm0404Pic, pprx61024SPX=pprx61024SPX, pprx23028GT=pprx23028GT, pprAr88fSC=pprAr88fSC, pprXem2XS=pprXem2XS, pprx60024TSPOE=pprx60024TSPOE, pprx93028GSX=pprx93028GSX, pprAR443=pprAR443, pprAr88t8fMTi=pprAr88t8fMTi, pprAr88t8fSCi=pprAr88t8fSCi, pprSb24RJ=pprSb24RJ, pprSb48t=pprSb48t, pprAtSBx8165POEAC=pprAtSBx8165POEAC, ppr9812T=ppr9812T, pprSbChassis8AC=pprSbChassis8AC, chipRtc4=chipRtc4, pprAR551=pprAR551, pprA37VF45=pprA37VF45, chipFlash2mb=chipFlash2mb, chipRam4mb=chipRam4mb, pprAtPwr02RAC=pprAtPwr02RAC, pprRapierG6MT=pprRapierG6MT, pprAr300u=pprAr300u, pprAr745DC=pprAr745DC, ppr8948i=ppr8948i, pprAtSBx81GP24=pprAtSBx81GP24, pprXem2XP=pprXem2XP, chipRam16mb=chipRam16mb, pprRapier8fSCi=pprRapier8fSCi, pprA50=pprA50, ifaceSyn=ifaceSyn, pprAR550SDP=pprAR550SDP, pprSbExpander=pprSbExpander, pprAtPWR05AC=pprAtPWR05AC, pprAtSBx81CFC400=pprAtSBx81CFC400, pprAtSBx81XS6=pprAtSBx81XS6, ppr8724XLDC=ppr8724XLDC, pprx31026GP=pprx31026GP, pprSbChassis16DC=pprSbChassis16DC, pprSb8fLXSC=pprSb8fLXSC, pprx90024XTN=pprx90024XTN, pprIcmAr023=pprIcmAr023, pprAr130u=pprAr130u, ppr9816GB=ppr9816GB, pprRapier48wAC=pprRapier48wAC, pprAr130s=pprAr130s, pprx51052GPX=pprx51052GPX, pprSb8GBIC=pprSb8GBIC, pprSb8fLXMT=pprSb8fLXMT, ifaceGBIC=ifaceGBIC, pprAR560=pprAR560, pprXum100M=pprXum100M, chip860TCpu=chip860TCpu, pprIcmAr021s=pprIcmAr021s, pprx60048TS=pprx60048TS, pprAR415S=pprAR415S, pprAr725=pprAr725, pprAtXum12T=pprAtXum12T, pprAr300L=pprAr300L, ppr9812TF=ppr9812TF, pprSbChassis4DC=pprSbChassis4DC, pprAt9748TSXP=pprAt9748TSXP, chipRam6mb=chipRam6mb, pprx21024GT=pprx21024GT, pprAr011=pprAr011, pprx31026FP=pprx31026FP, pprAt8624POE=pprAt8624POE, pprAtPwr01RAC=pprAtPwr01RAC, ppr9924T=ppr9924T, pprXemStk=pprXemStk, pprx51028GSX=pprx51028GSX, ifaceEth=ifaceEth, pprSBx81CFC960=pprSBx81CFC960, pprIcmAr021v3s=pprIcmAr021v3s, pprA41SC=pprA41SC, pprAR570=pprAR570, pprx21016GT=pprx21016GT, pprAR770=pprAR770, pprSBx81GP24a=pprSBx81GP24a, chipPem=chipPem, pprx31050FT=pprx31050FT, pprSBx81GT24a=pprSBx81GT24a, pprx200GE52T=pprx200GE52T, pprA38LC=pprA38LC, pprx61024TsXPOEPlus=pprx61024TsXPOEPlus, pprXemPOE=pprXemPOE, pprAt8316XLCR=pprAt8316XLCR, pprAr88fSCi=pprAr88fSCi, pprAt8724XL=pprAt8724XL, ppr9924TEMC=ppr9924TEMC, pprSb8fSXSC=pprSb8fSXSC, pprAr816fMTi=pprAr816fMTi, chipFlash1mb=chipFlash1mb, pprAtXum12SFPi=pprAtXum12SFPi, pprAtXum12SFP=pprAtXum12SFP, pprRapier8t8fMT=pprRapier8t8fMT, pprAR415SDC=pprAR415SDC, ppr9812TDC=ppr9812TDC, pprC8724MLB=pprC8724MLB, pprNsm0418BRI=pprNsm0418BRI, pprx61048TsPOEPlus=pprx61048TsPOEPlus, pprA40SC=pprA40SC, pprx90024XT=pprx90024XT, pprAt8848DC=pprAt8848DC, pprAR442=pprAR442, pprAtSBx8112=pprAtSBx8112, pprx61048TsX=pprx61048TsX, ppr8624xl80=ppr8624xl80, chipRtc2=chipRtc2, pprAtSBx81GT24=pprAtSBx81GT24, pprx23052GT=pprx23052GT, pprA46Tx=pprA46Tx, pprA53=pprA53, pprAt8748XLDC=pprAt8748XLDC, pprx23010GPT=pprx23010GPT, pprSb1XFP=pprSb1XFP, pprAr450Dual=pprAr450Dual, boards=boards, pprx23028GP=pprx23028GP, pprA41MTRJ=pprA41MTRJ, ifaceBri=ifaceBri, pprIcmAr022=pprIcmAr022, pprIcmAr027=pprIcmAr027, pprx23010GT=pprx23010GT, pprAr816fSC=pprAr816fSC, pprPWR800=pprPWR800, chipRam1mb=chipRam1mb, pprA52=pprA52, chipRam2mb=chipRam2mb, chipFlash4mb=chipFlash4mb, pprAr012=pprAr012, pprAr370=pprAr370, pprSbChassis16AC=pprSbChassis16AC, pprPWR250=pprPWR250, pprATEMXP=pprATEMXP, pprRapier8t8fSCi=pprRapier8t8fSCi, pprx93028GPX=pprx93028GPX)
mibBuilder.exportSymbols("AT-BOARDS-MIB", pprRapier48=pprRapier48, pprAr816fMT=pprAr816fMT, pprAR550=pprAR550, pprAtSBx81GS24a=pprAtSBx81GS24a, chip68302Cpu=chip68302Cpu, pprRapier24i=pprRapier24i, pprx51028GPX=pprx51028GPX, pprx93028GTX=pprx93028GTX, pprPWR1200=pprPWR1200, pprSb8fRJ=pprSb8fRJ, pprX30024TS=pprX30024TS, ppr8948EX=ppr8948EX, pprSb8fSXMT=pprSb8fSXMT, pprRapier48w=pprRapier48w, chipFlash8mb=chipFlash8mb, pprAr120=pprAr120, pprAtSBx8106=pprAtSBx8106, pprx60024TS=pprx60024TS, chipRam3mb=chipRam3mb, ppr9924T4SP=ppr9924T4SP, pprRapierG6LX=pprRapierG6LX, pprAtFan01R=pprAtFan01R, pprAR552=pprAR552, pprRapier16fMT=pprRapier16fMT, chipFlash3mb=chipFlash3mb, pprIcmAR026=pprIcmAR026, pprAr88t8fSC=pprAr88t8fSC, pprAr140s=pprAr140s, pprAt9724TSXP=pprAt9724TSXP, pprx31050FP=pprx31050FP, pprAtXum10G=pprAtXum10G, pprIcmAr020=pprIcmAr020, pprAt8748XL=pprAt8748XL, pprAr720=pprAr720, PYSNMP_MODULE_ID=boards, pprx61024TsPOEPlus=pprx61024TsPOEPlus, pprx93052GPX=pprx93052GPX, pprSb24SFP=pprSb24SFP, ppr9816GBDC=ppr9816GBDC, pprATStackXG=pprATStackXG, pprAt8624T2M=pprAt8624T2M, pprx60024TSPOEPLUS=pprx60024TSPOEPLUS, pprNsm048DS3=pprNsm048DS3, pprAr310=pprAr310, pprAr824=pprAr824, chip68340Cpu=chip68340Cpu, pprAR031=pprAR031, pprx31050GP=pprx31050GP, pprSb32fSC=pprSb32fSC, pprAt8624POECR=pprAt8624POECR, pprAR440=pprAR440, pprAtSBx8161SYSAC=pprAtSBx8161SYSAC, pprAt8824R=pprAt8824R, pprATLBM=pprATLBM, pprAtXum12TiN=pprAtXum12TiN, ifacePots=ifacePots, pprIcmAr021v2s=pprIcmAr021v2s, pprAtFan01=pprAtFan01, pprAr300=pprAr300, pprSbControlDTM=pprSbControlDTM, pprx60024TSXP=pprx60024TSXP, pprAR441=pprAR441, pprIcmAr021u=pprIcmAr021u, pprAr140u=pprAr140u, ifacePri=ifacePri, chipRtc1=chipRtc1, ppr8948iN=ppr8948iN, pprAr310u=pprAr310u, pprSb32fMT=pprSb32fMT, pprAR030=pprAR030, pprPWR100R=pprPWR100R, release=release, chip68020Cpu=chip68020Cpu, pprAt8324XLCR=pprAt8324XLCR, chipRtc3=chipRtc3)
