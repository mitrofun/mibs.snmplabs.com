#
# PySNMP MIB module HH3C-DOT11-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DOT11-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3cDot11, Hh3cDot11ObjectIDType, Hh3cDot11QosAcType, Hh3cDot11RadioElementIndex, Hh3cDot11RadioScopeType = mibBuilder.importSymbols("HH3C-DOT11-REF-MIB", "hh3cDot11", "Hh3cDot11ObjectIDType", "Hh3cDot11QosAcType", "Hh3cDot11RadioElementIndex", "Hh3cDot11RadioScopeType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, iso, Gauge32, ObjectIdentity, Counter32, Integer32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "iso", "Gauge32", "ObjectIdentity", "Counter32", "Integer32", "IpAddress", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
hh3cDot11QoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9))
hh3cDot11QoS.setRevisions(('2008-07-23 12:00',))
if mibBuilder.loadTexts: hh3cDot11QoS.setLastUpdated('200807231200Z')
if mibBuilder.loadTexts: hh3cDot11QoS.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
class Hh3cDot11WMMSVPMapAC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4), ("disable", 5))

class Hh3cDot11WMMCACPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelUtilization", 1), ("userNumber", 2))

hh3cDot11WmmCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1))
hh3cDot11RadioWmmCfgTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1), )
if mibBuilder.loadTexts: hh3cDot11RadioWmmCfgTable.setStatus('current')
hh3cDot11RadioWmmCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1), ).setIndexNames((0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"))
if mibBuilder.loadTexts: hh3cDot11RadioWmmCfgEntry.setStatus('current')
hh3cDot11WmmRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 1), Hh3cDot11RadioElementIndex())
if mibBuilder.loadTexts: hh3cDot11WmmRadioIndex.setStatus('current')
hh3cDot11RadioWmmEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmEnabled.setStatus('current')
hh3cDot11RadioSVPMapToAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 3), Hh3cDot11WMMSVPMapAC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioSVPMapToAC.setStatus('current')
hh3cDot11RadioCacPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 4), Hh3cDot11WMMCACPolicy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioCacPolicy.setStatus('current')
hh3cDot11RadioCacChlUtlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioCacChlUtlValue.setStatus('current')
hh3cDot11RadioCacUserNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioCacUserNum.setStatus('current')
hh3cDot11RadioWmmEdcaCfgTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2), )
if mibBuilder.loadTexts: hh3cDot11RadioWmmEdcaCfgTable.setStatus('current')
hh3cDot11RadioWmmEdcaCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1), ).setIndexNames((0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"), (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11RadioWmmAC"))
if mibBuilder.loadTexts: hh3cDot11RadioWmmEdcaCfgEntry.setStatus('current')
hh3cDot11RadioWmmAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 1), Hh3cDot11QosAcType())
if mibBuilder.loadTexts: hh3cDot11RadioWmmAC.setStatus('current')
hh3cDot11RadioWmmAifsn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmAifsn.setStatus('current')
hh3cDot11RadioWmmEcwMin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmEcwMin.setStatus('current')
hh3cDot11RadioWmmEcwMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmEcwMax.setStatus('current')
hh3cDot11RadioWmmTxoplimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmTxoplimit.setStatus('current')
hh3cDot11RadioWmmNoAck = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RadioWmmNoAck.setStatus('current')
hh3cDot11StationWmmEdcaTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3), )
if mibBuilder.loadTexts: hh3cDot11StationWmmEdcaTable.setStatus('current')
hh3cDot11StationWmmEdcaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1), ).setIndexNames((0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WmmRadioIndex"), (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11StationWmmAC"))
if mibBuilder.loadTexts: hh3cDot11StationWmmEdcaEntry.setStatus('current')
hh3cDot11StationWmmAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 1), Hh3cDot11QosAcType())
if mibBuilder.loadTexts: hh3cDot11StationWmmAC.setStatus('current')
hh3cDot11StationWmmAifsn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11StationWmmAifsn.setStatus('current')
hh3cDot11StationWmmEcwMin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11StationWmmEcwMin.setStatus('current')
hh3cDot11StationWmmEcwMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11StationWmmEcwMax.setStatus('current')
hh3cDot11StationWmmTxoplimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11StationWmmTxoplimit.setStatus('current')
hh3cDot11StationWmmCacEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 3, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11StationWmmCacEnabled.setStatus('current')
hh3cDot11WmmResetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4))
hh3cDot11WmmResetRadioByAP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11WmmResetRadioByAP.setStatus('current')
hh3cDot11WmmResetStationByAP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11WmmResetStationByAP.setStatus('current')
hh3cDot11RadioWmmEdcaCfg2Table = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5), )
if mibBuilder.loadTexts: hh3cDot11RadioWmmEdcaCfg2Table.setStatus('current')
hh3cDot11RadioWmmEdcaCfg2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1), ).setIndexNames((0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WMMAPSerialID"), (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11WMMRdId"), (0, "HH3C-DOT11-QOS-MIB", "hh3cDot11RdWmmAC"))
if mibBuilder.loadTexts: hh3cDot11RadioWmmEdcaCfg2Entry.setStatus('current')
hh3cDot11WMMAPSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 1), Hh3cDot11ObjectIDType())
if mibBuilder.loadTexts: hh3cDot11WMMAPSerialID.setStatus('current')
hh3cDot11WMMRdId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 2), Hh3cDot11RadioScopeType())
if mibBuilder.loadTexts: hh3cDot11WMMRdId.setStatus('current')
hh3cDot11RdWmmAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 3), Hh3cDot11QosAcType())
if mibBuilder.loadTexts: hh3cDot11RdWmmAC.setStatus('current')
hh3cDot11RdWmmAifsn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RdWmmAifsn.setStatus('current')
hh3cDot11RdWmmEcwMin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RdWmmEcwMin.setStatus('current')
hh3cDot11RdWmmEcwMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RdWmmEcwMax.setStatus('current')
hh3cDot11RdWmmTxoplimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 75, 9, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDot11RdWmmTxoplimit.setStatus('current')
mibBuilder.exportSymbols("HH3C-DOT11-QOS-MIB", hh3cDot11RadioWmmCfgEntry=hh3cDot11RadioWmmCfgEntry, hh3cDot11RadioCacPolicy=hh3cDot11RadioCacPolicy, hh3cDot11RadioWmmEdcaCfgEntry=hh3cDot11RadioWmmEdcaCfgEntry, hh3cDot11StationWmmAifsn=hh3cDot11StationWmmAifsn, hh3cDot11RdWmmEcwMax=hh3cDot11RdWmmEcwMax, hh3cDot11RadioWmmAC=hh3cDot11RadioWmmAC, hh3cDot11RadioWmmNoAck=hh3cDot11RadioWmmNoAck, Hh3cDot11WMMSVPMapAC=Hh3cDot11WMMSVPMapAC, hh3cDot11StationWmmEcwMax=hh3cDot11StationWmmEcwMax, hh3cDot11RadioWmmEnabled=hh3cDot11RadioWmmEnabled, hh3cDot11WmmResetRadioByAP=hh3cDot11WmmResetRadioByAP, hh3cDot11RadioWmmCfgTable=hh3cDot11RadioWmmCfgTable, hh3cDot11WmmResetStationByAP=hh3cDot11WmmResetStationByAP, hh3cDot11RadioWmmEdcaCfg2Entry=hh3cDot11RadioWmmEdcaCfg2Entry, hh3cDot11RadioWmmTxoplimit=hh3cDot11RadioWmmTxoplimit, hh3cDot11WMMAPSerialID=hh3cDot11WMMAPSerialID, hh3cDot11QoS=hh3cDot11QoS, hh3cDot11RadioSVPMapToAC=hh3cDot11RadioSVPMapToAC, hh3cDot11StationWmmEdcaEntry=hh3cDot11StationWmmEdcaEntry, hh3cDot11WmmRadioIndex=hh3cDot11WmmRadioIndex, hh3cDot11RdWmmEcwMin=hh3cDot11RdWmmEcwMin, hh3cDot11WmmCfgGroup=hh3cDot11WmmCfgGroup, hh3cDot11StationWmmTxoplimit=hh3cDot11StationWmmTxoplimit, hh3cDot11RadioCacUserNum=hh3cDot11RadioCacUserNum, hh3cDot11RadioWmmEdcaCfg2Table=hh3cDot11RadioWmmEdcaCfg2Table, hh3cDot11RdWmmAifsn=hh3cDot11RdWmmAifsn, hh3cDot11WmmResetGroup=hh3cDot11WmmResetGroup, PYSNMP_MODULE_ID=hh3cDot11QoS, hh3cDot11WMMRdId=hh3cDot11WMMRdId, hh3cDot11StationWmmCacEnabled=hh3cDot11StationWmmCacEnabled, hh3cDot11StationWmmAC=hh3cDot11StationWmmAC, hh3cDot11RadioWmmEdcaCfgTable=hh3cDot11RadioWmmEdcaCfgTable, hh3cDot11RadioWmmEcwMax=hh3cDot11RadioWmmEcwMax, hh3cDot11StationWmmEcwMin=hh3cDot11StationWmmEcwMin, hh3cDot11RadioCacChlUtlValue=hh3cDot11RadioCacChlUtlValue, hh3cDot11RdWmmTxoplimit=hh3cDot11RdWmmTxoplimit, hh3cDot11RdWmmAC=hh3cDot11RdWmmAC, hh3cDot11RadioWmmEcwMin=hh3cDot11RadioWmmEcwMin, hh3cDot11StationWmmEdcaTable=hh3cDot11StationWmmEdcaTable, hh3cDot11RadioWmmAifsn=hh3cDot11RadioWmmAifsn, Hh3cDot11WMMCACPolicy=Hh3cDot11WMMCACPolicy)