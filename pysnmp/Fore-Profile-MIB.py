#
# PySNMP MIB module Fore-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Profile-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
frameInternetworking, = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, Gauge32, ModuleIdentity, Integer32, Counter64, ObjectIdentity, MibIdentifier, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
foreProfileModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 4))
if mibBuilder.loadTexts: foreProfileModule.setLastUpdated('9704011044-0400')
if mibBuilder.loadTexts: foreProfileModule.setOrganization('FORE')
profileLmiTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1), )
if mibBuilder.loadTexts: profileLmiTable.setStatus('current')
profileLmiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileLmiIndex"))
if mibBuilder.loadTexts: profileLmiEntry.setStatus('current')
profileLmiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileLmiIndex.setStatus('current')
profileLmiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiRowStatus.setStatus('current')
profileLmiName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiName.setStatus('current')
profileLmiFlavour = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("lmi", 2), ("t1617d", 3), ("t1617b", 4), ("q933a", 5))).clone('q933a')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiFlavour.setStatus('current')
profileLmiT391 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiT391.setStatus('current')
profileLmiN391 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiN391.setStatus('current')
profileLmiT392 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiT392.setStatus('current')
profileLmiN392 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiN392.setStatus('current')
profileLmiN393 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiN393.setStatus('current')
profileLminT3 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), )).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLminT3.setStatus('current')
profileLmiDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uni", 1), ("bi", 2))).clone('bi')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiDirection.setStatus('current')
profileLmiRole = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("network", 2))).clone('network')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileLmiRole.setStatus('current')
profileLmiRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileLmiRefCnt.setStatus('current')
profileFrRateTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2), )
if mibBuilder.loadTexts: profileFrRateTable.setStatus('current')
profileFrRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileFrRateIndex"))
if mibBuilder.loadTexts: profileFrRateEntry.setStatus('current')
profileFrRateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrRateIndex.setStatus('current')
profileFrRateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateRowStatus.setStatus('current')
profileFrRateName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateName.setStatus('current')
profileFrRateInBc = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateInBc.setStatus('current')
profileFrRateInBe = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateInBe.setStatus('current')
profileFrRateInCir = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateInCir.setStatus('current')
profileFrRateOutBc = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateOutBc.setStatus('current')
profileFrRateOutBe = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateOutBe.setStatus('current')
profileFrRateOutCir = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateOutCir.setStatus('current')
profileFrRateMinBc = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 10), Integer32().clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateMinBc.setStatus('current')
profileFrRateCmPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 11), Integer32().clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrRateCmPeriod.setStatus('current')
profileFrRateRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrRateRefCnt.setStatus('current')
profileFuniTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3), )
if mibBuilder.loadTexts: profileFuniTable.setStatus('current')
profileFuniEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileFuniIndex"))
if mibBuilder.loadTexts: profileFuniEntry.setStatus('current')
profileFuniIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFuniIndex.setStatus('current')
profileFuniRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniRowStatus.setStatus('current')
profileFuniName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniName.setStatus('current')
profileFuniIlmiVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniIlmiVpi.setStatus('current')
profileFuniIlmiVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 5), Integer32().clone(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniIlmiVci.setStatus('current')
profileFuniSigVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniSigVpi.setStatus('current')
profileFuniSigVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 7), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniSigVci.setStatus('current')
profileFuniMinVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 63)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniMinVci.setStatus('current')
profileFuniMaxVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 63)).clone(63)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniMaxVci.setStatus('current')
profileFuniIlmiSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniIlmiSupport.setStatus('current')
profileFuniSigSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniSigSupport.setStatus('current')
profileFuniOamSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniOamSupport.setStatus('current')
profileFuniActiveVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniActiveVpiBits.setStatus('current')
profileFuniActiveVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniActiveVciBits.setStatus('current')
profileFuniConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode3", 3), ("mode4", 4))).clone('mode1a')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniConfMode.setStatus('current')
profileFuniFcsBits = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fcsBits16", 1), ("fcsBits32", 2))).clone('fcsBits16')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniFcsBits.setStatus('current')
profileFuniHdrBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hdrBytes2", 1), ("hdrBytes4", 2))).clone('hdrBytes2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniHdrBytes.setStatus('current')
profileFuniAal34Support = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFuniAal34Support.setStatus('current')
profileFuniRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFuniRefCnt.setStatus('current')
profileFrf8Table = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4), )
if mibBuilder.loadTexts: profileFrf8Table.setStatus('current')
profileFrf8Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileFrf8Index"))
if mibBuilder.loadTexts: profileFrf8Entry.setStatus('current')
profileFrf8Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrf8Index.setStatus('current')
profileFrf8RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8RowStatus.setStatus('current')
profileFrf8Name = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8Name.setStatus('current')
profileFrf8DeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mapped", 1), ("ignored", 2))).clone('mapped')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8DeMode.setStatus('current')
profileFrf8ClpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mapped", 1), ("ignored", 2))).clone('mapped')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8ClpMode.setStatus('current')
profileFrf8FecnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mapped", 1), ("ignored", 2))).clone('mapped')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8FecnMode.setStatus('current')
profileFrf8DefaultDe = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8DefaultDe.setStatus('current')
profileFrf8DefaultClp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8DefaultClp.setStatus('current')
profileFrf8Protocols = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileFrf8Protocols.setStatus('current')
profileFrf8RefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrf8RefCnt.setStatus('current')
profileServiceTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5), )
if mibBuilder.loadTexts: profileServiceTable.setStatus('current')
profileServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileServiceIndex"))
if mibBuilder.loadTexts: profileServiceEntry.setStatus('current')
profileServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileServiceIndex.setStatus('current')
profileServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceRowStatus.setStatus('current')
profileServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceName.setStatus('current')
profileServiceAccRate = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceAccRate.setStatus('current')
profileServiceMaxVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 5), Integer32().clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceMaxVccs.setStatus('current')
profileServiceMaxPayloadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 6), Integer32().clone(4096)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceMaxPayloadSize.setStatus('current')
profileServiceInBwOb = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 500)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceInBwOb.setStatus('current')
profileServiceOutBwOb = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 500)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileServiceOutBwOb.setStatus('current')
profileServiceRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileServiceRefCnt.setStatus('current')
profileEpdPpdTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6), )
if mibBuilder.loadTexts: profileEpdPpdTable.setStatus('current')
profileEpdPpdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileEpdPpdIndex"))
if mibBuilder.loadTexts: profileEpdPpdEntry.setStatus('current')
profileEpdPpdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileEpdPpdIndex.setStatus('current')
profileEpdPpdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdRowStatus.setStatus('current')
profileEpdPpdName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdName.setStatus('current')
profileEpdPpdPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2))).clone('low')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdPriority.setStatus('current')
profileEpdPpdClp0Epd = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdClp0Epd.setStatus('current')
profileEpdPpdClp1Ppd = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdClp1Ppd.setStatus('current')
profileEpdPpdClp1Epd = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: profileEpdPpdClp1Epd.setStatus('current')
profileEpdPpdRefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileEpdPpdRefCnt.setStatus('current')
profileFrf5Table = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7), )
if mibBuilder.loadTexts: profileFrf5Table.setStatus('current')
profileFrf5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1), ).setIndexNames((0, "Fore-Profile-MIB", "profileFrf5Index"))
if mibBuilder.loadTexts: profileFrf5Entry.setStatus('current')
profileFrf5Index = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrf5Index.setStatus('current')
profileFrf5RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5RowStatus.setStatus('current')
profileFrf5Name = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5Name.setStatus('current')
profileFrf5DeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mapped", 1), ("ignored", 2))).clone('mapped')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5DeMode.setStatus('current')
profileFrf5ClpFrsscsDeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mapped", 1), ("ignored", 2))).clone('mapped')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5ClpFrsscsDeMode.setStatus('current')
profileFrf5DefaultClp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5DefaultClp.setStatus('current')
profileFrf5MaxDlcis = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 7), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5MaxDlcis.setStatus('current')
profileFrf5MaxPayloadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 8), Integer32().clone(4092)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profileFrf5MaxPayloadSize.setStatus('current')
profileFrf5RefCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 4, 7, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: profileFrf5RefCnt.setStatus('current')
mibBuilder.exportSymbols("Fore-Profile-MIB", profileFuniEntry=profileFuniEntry, profileEpdPpdClp1Epd=profileEpdPpdClp1Epd, profileLmiTable=profileLmiTable, profileFrf5Table=profileFrf5Table, profileFrRateCmPeriod=profileFrRateCmPeriod, profileLmiRefCnt=profileLmiRefCnt, profileFrRateName=profileFrRateName, profileLmiT391=profileLmiT391, profileFrRateRefCnt=profileFrRateRefCnt, profileLmiIndex=profileLmiIndex, profileFrf8Table=profileFrf8Table, profileFrf8Index=profileFrf8Index, profileFrRateOutBc=profileFrRateOutBc, profileFrf5ClpFrsscsDeMode=profileFrf5ClpFrsscsDeMode, profileLmiFlavour=profileLmiFlavour, profileFrf5RowStatus=profileFrf5RowStatus, profileEpdPpdTable=profileEpdPpdTable, profileFuniFcsBits=profileFuniFcsBits, profileLmiRole=profileLmiRole, profileFrf5DeMode=profileFrf5DeMode, profileFrRateTable=profileFrRateTable, profileServiceMaxPayloadSize=profileServiceMaxPayloadSize, profileLmiN392=profileLmiN392, profileFrf8Protocols=profileFrf8Protocols, profileFrf8Name=profileFrf8Name, profileFrf5Entry=profileFrf5Entry, profileLmiDirection=profileLmiDirection, profileLmiEntry=profileLmiEntry, profileFrRateIndex=profileFrRateIndex, profileFuniRefCnt=profileFuniRefCnt, profileEpdPpdClp0Epd=profileEpdPpdClp0Epd, profileFuniIlmiVci=profileFuniIlmiVci, profileFrf8DeMode=profileFrf8DeMode, profileFrf8DefaultDe=profileFrf8DefaultDe, profileFrf8DefaultClp=profileFrf8DefaultClp, profileLmiRowStatus=profileLmiRowStatus, profileServiceTable=profileServiceTable, PYSNMP_MODULE_ID=foreProfileModule, profileFrf5MaxDlcis=profileFrf5MaxDlcis, profileFrf8ClpMode=profileFrf8ClpMode, profileFuniIlmiSupport=profileFuniIlmiSupport, profileFrRateEntry=profileFrRateEntry, profileFrRateMinBc=profileFrRateMinBc, profileFuniIlmiVpi=profileFuniIlmiVpi, profileFuniSigVci=profileFuniSigVci, profileEpdPpdRowStatus=profileEpdPpdRowStatus, profileFrf8RowStatus=profileFrf8RowStatus, profileFuniTable=profileFuniTable, profileFrf5DefaultClp=profileFrf5DefaultClp, profileLmiT392=profileLmiT392, profileEpdPpdIndex=profileEpdPpdIndex, profileFuniActiveVciBits=profileFuniActiveVciBits, profileEpdPpdClp1Ppd=profileEpdPpdClp1Ppd, profileFuniRowStatus=profileFuniRowStatus, profileFrRateOutCir=profileFrRateOutCir, profileFuniMinVci=profileFuniMinVci, profileLmiName=profileLmiName, profileServiceName=profileServiceName, profileServiceRefCnt=profileServiceRefCnt, profileFrf5RefCnt=profileFrf5RefCnt, profileServiceAccRate=profileServiceAccRate, profileFuniHdrBytes=profileFuniHdrBytes, profileServiceRowStatus=profileServiceRowStatus, profileFrRateInBc=profileFrRateInBc, profileFrf5Name=profileFrf5Name, profileFrRateInCir=profileFrRateInCir, profileEpdPpdRefCnt=profileEpdPpdRefCnt, profileServiceInBwOb=profileServiceInBwOb, profileFuniOamSupport=profileFuniOamSupport, profileFuniActiveVpiBits=profileFuniActiveVpiBits, profileEpdPpdEntry=profileEpdPpdEntry, profileFuniSigSupport=profileFuniSigSupport, profileFrRateOutBe=profileFrRateOutBe, profileFuniSigVpi=profileFuniSigVpi, profileServiceMaxVccs=profileServiceMaxVccs, profileServiceOutBwOb=profileServiceOutBwOb, profileLmiN393=profileLmiN393, profileFuniMaxVci=profileFuniMaxVci, profileFrf5Index=profileFrf5Index, profileFuniConfMode=profileFuniConfMode, profileFrRateInBe=profileFrRateInBe, foreProfileModule=foreProfileModule, profileFuniIndex=profileFuniIndex, profileLmiN391=profileLmiN391, profileFuniAal34Support=profileFuniAal34Support, profileEpdPpdName=profileEpdPpdName, profileFrRateRowStatus=profileFrRateRowStatus, profileFrf8Entry=profileFrf8Entry, profileLminT3=profileLminT3, profileFuniName=profileFuniName, profileFrf8RefCnt=profileFrf8RefCnt, profileEpdPpdPriority=profileEpdPpdPriority, profileServiceIndex=profileServiceIndex, profileFrf8FecnMode=profileFrf8FecnMode, profileFrf5MaxPayloadSize=profileFrf5MaxPayloadSize, profileServiceEntry=profileServiceEntry)
