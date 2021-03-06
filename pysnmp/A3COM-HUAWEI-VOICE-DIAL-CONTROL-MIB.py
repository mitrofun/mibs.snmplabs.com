#
# PySNMP MIB module A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cVoice, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cVoice")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
AbsoluteCounter32, = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "AbsoluteCounter32")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Counter64, iso, IpAddress, Integer32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Counter64", "iso", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ObjectIdentity")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
h3cVoiceEntityControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14))
h3cVoiceEntityControl.setRevisions(('2009-04-16 00:00',))
if mibBuilder.loadTexts: h3cVoiceEntityControl.setLastUpdated('200904160000Z')
if mibBuilder.loadTexts: h3cVoiceEntityControl.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
class H3cCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("g711a", 1), ("g711u", 2), ("g723r53", 3), ("g723r63", 4), ("g729r8", 5), ("g729a", 6), ("g726r16", 7), ("g726r24", 8), ("g726r32", 9), ("g726r40", 10), ("unknown", 11), ("g729br8", 12))

class H3cOutBandMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("voice", 1), ("h245AlphaNumeric", 2), ("h225", 3), ("sip", 4), ("nte", 5), ("vofr", 6))

class H3cFaxProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("t38", 1), ("standardt38", 2), ("pcmG711alaw", 3), ("pcmG711ulaw", 4))

class H3cFaxBaudrateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disable", 1), ("voice", 2), ("b2400", 3), ("b4800", 4), ("b9600", 5), ("b14400", 6))

class H3cFaxTrainMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("ppp", 2))

class H3cRegisterdStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("login", 4), ("logout", 5))

h3cVoEntityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1))
h3cVoEntityCreateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1), )
if mibBuilder.loadTexts: h3cVoEntityCreateTable.setStatus('current')
h3cVoEntityCreateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"))
if mibBuilder.loadTexts: h3cVoEntityCreateEntry.setStatus('current')
h3cVoEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoEntityIndex.setStatus('current')
h3cVoEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pots", 1), ("voip", 2), ("vofr", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoEntityType.setStatus('current')
h3cVoEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoEntityRowStatus.setStatus('current')
h3cVoEntityCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2), )
if mibBuilder.loadTexts: h3cVoEntityCommonConfigTable.setStatus('current')
h3cVoEntityCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityCfgIndex"))
if mibBuilder.loadTexts: h3cVoEntityCommonConfigEntry.setStatus('current')
h3cVoEntityCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoEntityCfgIndex.setStatus('current')
h3cVoEntityCfgCodec1st = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 2), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec1st.setStatus('current')
h3cVoEntityCfgCodec2nd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 3), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec2nd.setStatus('current')
h3cVoEntityCfgCodec3rd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 4), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec3rd.setStatus('current')
h3cVoEntityCfgCodec4th = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 5), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec4th.setStatus('current')
h3cVoEntityCfgDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgDSCP.setStatus('current')
h3cVoEntityCfgVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgVADEnable.setStatus('current')
h3cVoEntityCfgOutbandMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 8), H3cOutBandMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgOutbandMode.setStatus('current')
h3cVoEntityCfgFaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, -3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLevel.setStatus('current')
h3cVoEntityCfgFaxBaudrate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 10), H3cFaxBaudrateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxBaudrate.setStatus('current')
h3cVoEntityCfgFaxLocalTrainPara = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLocalTrainPara.setStatus('current')
h3cVoEntityCfgFaxProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 12), H3cFaxProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxProtocol.setStatus('current')
h3cVoEntityCfgFaxHRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxHRPackNum.setStatus('current')
h3cVoEntityCfgFaxLRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLRPackNum.setStatus('current')
h3cVoEntityCfgFaxSendNSFEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxSendNSFEnable.setStatus('current')
h3cVoEntityCfgFaxTrainMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 16), H3cFaxTrainMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxTrainMode.setStatus('current')
h3cVoEntityCfgFaxEcm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxEcm.setStatus('current')
h3cVoEntityCfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgPriority.setStatus('current')
h3cVoEntityCfgDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgDescription.setStatus('current')
h3cVoPOTSEntityConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3), )
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigTable.setStatus('current')
h3cVoPOTSEntityConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoPOTSEntityConfigIndex"))
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigEntry.setStatus('current')
h3cVoPOTSEntityConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigIndex.setStatus('current')
h3cVoPOTSEntityConfigPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigPrefix.setStatus('current')
h3cVoPOTSEntityConfigSubLine = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSubLine.setStatus('current')
h3cVoPOTSEntityConfigSendNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 31), ValueRangeConstraint(65534, 65534), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSendNum.setStatus('current')
h3cVoVoIPEntityConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4), )
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigTable.setStatus('current')
h3cVoVoIPEntityConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoVoIPEntityCfgIndex"))
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigEntry.setStatus('current')
h3cVoVoIPEntityCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgIndex.setStatus('current')
h3cVoVoIPEntityCfgTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ras", 2), ("h323IpAddress", 3), ("sipIpAddress", 4), ("sipProxy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetType.setStatus('current')
h3cVoVoIPEntityCfgTargetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddrType.setStatus('current')
h3cVoVoIPEntityCfgTargetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddr.setStatus('current')
h3cVoEntityNumberTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5), )
if mibBuilder.loadTexts: h3cVoEntityNumberTable.setStatus('current')
h3cVoEntityNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"))
if mibBuilder.loadTexts: h3cVoEntityNumberEntry.setStatus('current')
h3cVoEntityNumberAuthUser = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberAuthUser.setStatus('current')
h3cVoEntityNumberPasswordType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberPasswordType.setStatus('current')
h3cVoEntityNumberPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 16), ValueSizeConstraint(24, 24), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberPassword.setStatus('current')
h3cVoEntityNumberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 4), H3cRegisterdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoEntityNumberStatus.setStatus('current')
h3cVoEntityNumberExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoEntityNumberExpires.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", h3cVoEntityCfgFaxHRPackNum=h3cVoEntityCfgFaxHRPackNum, h3cVoVoIPEntityCfgTargetType=h3cVoVoIPEntityCfgTargetType, h3cVoPOTSEntityConfigSubLine=h3cVoPOTSEntityConfigSubLine, h3cVoEntityCfgCodec2nd=h3cVoEntityCfgCodec2nd, h3cVoEntityCfgFaxProtocol=h3cVoEntityCfgFaxProtocol, h3cVoEntityRowStatus=h3cVoEntityRowStatus, h3cVoEntityCfgIndex=h3cVoEntityCfgIndex, h3cVoVoIPEntityConfigEntry=h3cVoVoIPEntityConfigEntry, H3cFaxBaudrateType=H3cFaxBaudrateType, h3cVoEntityNumberEntry=h3cVoEntityNumberEntry, h3cVoVoIPEntityCfgTargetAddr=h3cVoVoIPEntityCfgTargetAddr, h3cVoEntityNumberTable=h3cVoEntityNumberTable, h3cVoEntityCfgFaxLRPackNum=h3cVoEntityCfgFaxLRPackNum, h3cVoEntityCfgDescription=h3cVoEntityCfgDescription, h3cVoEntityCommonConfigTable=h3cVoEntityCommonConfigTable, h3cVoEntityCfgFaxBaudrate=h3cVoEntityCfgFaxBaudrate, h3cVoEntityCfgFaxEcm=h3cVoEntityCfgFaxEcm, PYSNMP_MODULE_ID=h3cVoiceEntityControl, h3cVoPOTSEntityConfigEntry=h3cVoPOTSEntityConfigEntry, h3cVoEntityType=h3cVoEntityType, h3cVoEntityCfgCodec1st=h3cVoEntityCfgCodec1st, H3cFaxTrainMode=H3cFaxTrainMode, h3cVoEntityCreateEntry=h3cVoEntityCreateEntry, h3cVoVoIPEntityCfgTargetAddrType=h3cVoVoIPEntityCfgTargetAddrType, h3cVoEntityCfgFaxTrainMode=h3cVoEntityCfgFaxTrainMode, h3cVoEntityNumberAuthUser=h3cVoEntityNumberAuthUser, h3cVoEntityCfgPriority=h3cVoEntityCfgPriority, H3cRegisterdStatus=H3cRegisterdStatus, H3cFaxProtocolType=H3cFaxProtocolType, h3cVoEntityCommonConfigEntry=h3cVoEntityCommonConfigEntry, h3cVoEntityCfgCodec3rd=h3cVoEntityCfgCodec3rd, h3cVoEntityCfgVADEnable=h3cVoEntityCfgVADEnable, H3cOutBandMode=H3cOutBandMode, h3cVoEntityNumberStatus=h3cVoEntityNumberStatus, h3cVoEntityCfgFaxLevel=h3cVoEntityCfgFaxLevel, h3cVoEntityNumberPasswordType=h3cVoEntityNumberPasswordType, h3cVoEntityCfgDSCP=h3cVoEntityCfgDSCP, h3cVoEntityCfgOutbandMode=h3cVoEntityCfgOutbandMode, h3cVoEntityNumberExpires=h3cVoEntityNumberExpires, h3cVoEntityIndex=h3cVoEntityIndex, h3cVoEntityCreateTable=h3cVoEntityCreateTable, h3cVoVoIPEntityCfgIndex=h3cVoVoIPEntityCfgIndex, h3cVoEntityCfgFaxLocalTrainPara=h3cVoEntityCfgFaxLocalTrainPara, h3cVoEntityNumberPassword=h3cVoEntityNumberPassword, h3cVoPOTSEntityConfigTable=h3cVoPOTSEntityConfigTable, h3cVoVoIPEntityConfigTable=h3cVoVoIPEntityConfigTable, h3cVoPOTSEntityConfigPrefix=h3cVoPOTSEntityConfigPrefix, h3cVoEntityCfgFaxSendNSFEnable=h3cVoEntityCfgFaxSendNSFEnable, H3cCodecType=H3cCodecType, h3cVoPOTSEntityConfigIndex=h3cVoPOTSEntityConfigIndex, h3cVoEntityCfgCodec4th=h3cVoEntityCfgCodec4th, h3cVoiceEntityControl=h3cVoiceEntityControl, h3cVoEntityObjects=h3cVoEntityObjects, h3cVoPOTSEntityConfigSendNum=h3cVoPOTSEntityConfigSendNum)
