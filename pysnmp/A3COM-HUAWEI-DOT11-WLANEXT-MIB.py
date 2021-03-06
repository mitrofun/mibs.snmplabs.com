#
# PySNMP MIB module A3COM-HUAWEI-DOT11-WLANEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-DOT11-WLANEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cDot11, H3cDot11ObjectIDType, H3cDot11QosAcType, H3cDot11RadioScopeType = mibBuilder.importSymbols("A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11", "H3cDot11ObjectIDType", "H3cDot11QosAcType", "H3cDot11RadioScopeType")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, Counter64, Counter32, Bits, IpAddress, NotificationType, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter64", "Counter32", "Bits", "IpAddress", "NotificationType", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cDot11WLANEXT = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7))
h3cDot11WLANEXT.setRevisions(('2007-06-08 20:00',))
if mibBuilder.loadTexts: h3cDot11WLANEXT.setLastUpdated('200706082000Z')
if mibBuilder.loadTexts: h3cDot11WLANEXT.setOrganization('HUAWEI-3COM Technologies Co., Ltd.')
h3cDot11RFGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1))
h3cDot11QosGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2))
h3cDot11RFSignalStatisTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1), )
if mibBuilder.loadTexts: h3cDot11RFSignalStatisTable.setStatus('current')
h3cDot11RFSignalStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11RFAPID"), (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11RFRadioID"))
if mibBuilder.loadTexts: h3cDot11RFSignalStatisEntry.setStatus('current')
h3cDot11RFAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 1), H3cDot11ObjectIDType())
if mibBuilder.loadTexts: h3cDot11RFAPID.setStatus('current')
h3cDot11RFRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 2), H3cDot11RadioScopeType())
if mibBuilder.loadTexts: h3cDot11RFRadioID.setStatus('current')
h3cDot11RFSignalStatisInterv = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 3), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFSignalStatisInterv.setStatus('current')
h3cDot11RFAverageSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 4), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFAverageSignalStrength.setStatus('current')
h3cDot11RFMaxSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 5), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFMaxSignalStrength.setStatus('current')
h3cDot11RFMinSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 1, 1, 1, 6), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFMinSignalStrength.setStatus('current')
h3cDot11QosStatisTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1), )
if mibBuilder.loadTexts: h3cDot11QosStatisTable.setStatus('current')
h3cDot11QosStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"), (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"))
if mibBuilder.loadTexts: h3cDot11QosStatisEntry.setStatus('current')
h3cDot11QosAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 1), H3cDot11ObjectIDType())
if mibBuilder.loadTexts: h3cDot11QosAPID.setStatus('current')
h3cDot11QosRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 2), H3cDot11RadioScopeType())
if mibBuilder.loadTexts: h3cDot11QosRadioID.setStatus('current')
h3cDot11QosAverageQueLen = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosAverageQueLen.setStatus('current')
h3cDot11QosDropFrameRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosDropFrameRatio.setStatus('current')
h3cDot11QosAverageDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 1, 1, 5), Integer32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosAverageDataRate.setStatus('current')
h3cDot11QosAcStatisTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2), )
if mibBuilder.loadTexts: h3cDot11QosAcStatisTable.setStatus('current')
h3cDot11QosAcStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"), (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"), (0, "A3COM-HUAWEI-DOT11-WLANEXT-MIB", "h3cDot11QosAcType"))
if mibBuilder.loadTexts: h3cDot11QosAcStatisEntry.setStatus('current')
h3cDot11QosAcType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1, 1), H3cDot11QosAcType())
if mibBuilder.loadTexts: h3cDot11QosAcType.setStatus('current')
h3cDot11AcDropFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 7, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11AcDropFrameCnt.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-DOT11-WLANEXT-MIB", h3cDot11QosRadioID=h3cDot11QosRadioID, h3cDot11WLANEXT=h3cDot11WLANEXT, h3cDot11RFMinSignalStrength=h3cDot11RFMinSignalStrength, h3cDot11AcDropFrameCnt=h3cDot11AcDropFrameCnt, h3cDot11RFRadioID=h3cDot11RFRadioID, h3cDot11QosAverageDataRate=h3cDot11QosAverageDataRate, h3cDot11RFSignalStatisTable=h3cDot11RFSignalStatisTable, h3cDot11RFAverageSignalStrength=h3cDot11RFAverageSignalStrength, h3cDot11RFAPID=h3cDot11RFAPID, PYSNMP_MODULE_ID=h3cDot11WLANEXT, h3cDot11QosStatisTable=h3cDot11QosStatisTable, h3cDot11QosGroup=h3cDot11QosGroup, h3cDot11QosAcStatisEntry=h3cDot11QosAcStatisEntry, h3cDot11QosStatisEntry=h3cDot11QosStatisEntry, h3cDot11QosAPID=h3cDot11QosAPID, h3cDot11RFSignalStatisEntry=h3cDot11RFSignalStatisEntry, h3cDot11RFGroup=h3cDot11RFGroup, h3cDot11RFSignalStatisInterv=h3cDot11RFSignalStatisInterv, h3cDot11QosDropFrameRatio=h3cDot11QosDropFrameRatio, h3cDot11QosAcType=h3cDot11QosAcType, h3cDot11RFMaxSignalStrength=h3cDot11RFMaxSignalStrength, h3cDot11QosAverageQueLen=h3cDot11QosAverageQueLen, h3cDot11QosAcStatisTable=h3cDot11QosAcStatisTable)
