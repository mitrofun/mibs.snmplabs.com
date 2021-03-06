#
# PySNMP MIB module Vct-Loopdetect-59-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Vct-Loopdetect-59-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, TimeTicks, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, MibIdentifier, Counter32, mgmt, Bits, Counter64, NotificationType, Unsigned32, experimental, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "TimeTicks", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "MibIdentifier", "Counter32", "mgmt", "Bits", "Counter64", "NotificationType", "Unsigned32", "experimental", "enterprises")
MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10switch = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102))
switch59vct = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24))
switch59loopdetect = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25))
class DisplayString(OctetString):
    pass

vctTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1), )
if mibBuilder.loadTexts: vctTable.setStatus('current')
vctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1), ).setIndexNames((0, "Vct-Loopdetect-59-MIB", "vctIfindex"))
if mibBuilder.loadTexts: vctEntry.setStatus('current')
vctIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: vctIfindex.setStatus('current')
vctSetIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vctSetIfindex.setStatus('current')
cableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("good", 1), ("fault", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cableStatus.setStatus('current')
doubleCableStatus1_2 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("good", 0), ("open", 1), ("short", 2), ("broken", 3), ("mismatch", 4), ("fail", 5), ("unknown", 6), ("null", 7)))).setLabel("doubleCableStatus1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableStatus1_2.setStatus('current')
doubleCableStatus3_6 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("good", 0), ("open", 1), ("short", 2), ("broken", 3), ("mismatch", 4), ("fail", 5), ("unknown", 6), ("null", 7)))).setLabel("doubleCableStatus3-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableStatus3_6.setStatus('current')
doubleCableStatus4_5 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("good", 0), ("open", 1), ("short", 2), ("broken", 3), ("mismatch", 4), ("fail", 5), ("unknown", 6), ("null", 7)))).setLabel("doubleCableStatus4-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableStatus4_5.setStatus('current')
doubleCableStatus7_8 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("good", 0), ("open", 1), ("short", 2), ("broken", 3), ("mismatch", 4), ("fail", 5), ("unknown", 6), ("null", 7)))).setLabel("doubleCableStatus7-8").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableStatus7_8.setStatus('current')
doubleCableLength1_2 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(200, 201, 202, 203, 204, 205, 206))).clone(namedValues=NamedValues(("lessthan50", 200), ("from50to80", 201), ("from80to110", 202), ("from110to140", 203), ("morethan140", 204), ("unknow", 205), ("null", 206)))).setLabel("doubleCableLength1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableLength1_2.setStatus('current')
doubleCableLength3_6 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(200, 201, 202, 203, 204, 205, 206))).clone(namedValues=NamedValues(("lessthan50", 200), ("from50to80", 201), ("from80to110", 202), ("from110to140", 203), ("morethan140", 204), ("unknow", 205), ("null", 206)))).setLabel("doubleCableLength3-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableLength3_6.setStatus('current')
doubleCableLength4_5 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(200, 201, 202, 203, 204, 205, 206))).clone(namedValues=NamedValues(("lessthan50", 200), ("from50to80", 201), ("from80to110", 202), ("from110to140", 203), ("morethan140", 204), ("unknow", 205), ("null", 206)))).setLabel("doubleCableLength4-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableLength4_5.setStatus('current')
doubleCableLength7_8 = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(200, 201, 202, 203, 204, 205, 206))).clone(namedValues=NamedValues(("lessthan50", 200), ("from50to80", 201), ("from80to110", 202), ("from110to140", 203), ("morethan140", 204), ("unknow", 205), ("null", 206)))).setLabel("doubleCableLength7-8").setMaxAccess("readonly")
if mibBuilder.loadTexts: doubleCableLength7_8.setStatus('current')
loopdetectReopenTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16777216))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopdetectReopenTime.setStatus('current')
loopdetectTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2), )
if mibBuilder.loadTexts: loopdetectTable.setStatus('current')
loopdetectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1), ).setIndexNames((0, "Vct-Loopdetect-59-MIB", "loopdetectPortIfindex"))
if mibBuilder.loadTexts: loopdetectEntry.setStatus('current')
loopdetectPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: loopdetectPortIfindex.setStatus('current')
loopdetectPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("up", 1), ("down", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopdetectPortOperStatus.setStatus('current')
loopdetectPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopdetectPortControl.setStatus('current')
loopdetectPortVid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopdetectPortVid.setStatus('current')
loopdetectPortFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopdetectPortFlag.setStatus('current')
loopdetectPortProtectFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopdetectPortProtectFlag.setStatus('current')
loopdetectPortReopenTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopdetectPortReopenTime.setStatus('current')
loopdetectVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopdetectVlan.setStatus('current')
mibBuilder.exportSymbols("Vct-Loopdetect-59-MIB", zxr10=zxr10, loopdetectPortProtectFlag=loopdetectPortProtectFlag, vctIfindex=vctIfindex, doubleCableStatus4_5=doubleCableStatus4_5, doubleCableLength4_5=doubleCableLength4_5, vctEntry=vctEntry, loopdetectTable=loopdetectTable, DisplayString=DisplayString, zxr10switch=zxr10switch, vctTable=vctTable, cableStatus=cableStatus, zte=zte, loopdetectReopenTime=loopdetectReopenTime, doubleCableLength1_2=doubleCableLength1_2, doubleCableLength3_6=doubleCableLength3_6, loopdetectVlan=loopdetectVlan, doubleCableStatus7_8=doubleCableStatus7_8, loopdetectPortFlag=loopdetectPortFlag, doubleCableStatus1_2=doubleCableStatus1_2, doubleCableStatus3_6=doubleCableStatus3_6, loopdetectPortOperStatus=loopdetectPortOperStatus, loopdetectPortControl=loopdetectPortControl, switch59loopdetect=switch59loopdetect, loopdetectPortIfindex=loopdetectPortIfindex, loopdetectPortReopenTime=loopdetectPortReopenTime, switch59vct=switch59vct, doubleCableLength7_8=doubleCableLength7_8, loopdetectEntry=loopdetectEntry, loopdetectPortVid=loopdetectPortVid, vctSetIfindex=vctSetIfindex)
