#
# PySNMP MIB module TERAWAVE-teraU-ds3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraU-ds3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, TimeTicks, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "enterprises", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraUDs3Group = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 15))
teraUds3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 1), )
if mibBuilder.loadTexts: teraUds3ConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ConfigTable.setDescription(' table teraUds3ConfigTable')
teraUds3ConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"))
if mibBuilder.loadTexts: teraUds3ConfigTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ConfigTableEntry.setDescription(' table entry teraUds3ConfigTableEntry ')
teraUds3LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3LineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LineIndex.setDescription('')
teraUds3TimeElasped = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3TimeElasped.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3TimeElasped.setDescription('')
teraUds3ValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ValidIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ValidIntervals.setDescription('')
teraUds3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("m23", 1), ("cbitParity", 2), ("e3-G-751", 3), ("e3-G-832", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3LineType.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LineType.setDescription('')
teraUds3ATMMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pLCP", 1), ("direct-Mapping", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3ATMMapping.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ATMMapping.setDescription('')
teraUds3LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("b3ZS", 2), ("hDB3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3LineCoding.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LineCoding.setDescription('')
teraUds3CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3CircuitIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3CircuitIdentifier.setDescription('')
teraUds3LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 32))).clone(namedValues=NamedValues(("noLoop", 1), ("facility", 4), ("equipped", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3LoopbackConfig.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LoopbackConfig.setDescription('')
teraUds3LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048))).clone(namedValues=NamedValues(("noAlarm", 1), ("rcvRAIFailure", 2), ("xmtRAIAlarm", 4), ("rcvAIS", 8), ("xmitAIS", 16), ("lOF", 32), ("lOS", 64), ("loopbackState", 128), ("rcvTestCode", 256), ("otherFailure", 512), ("unavailSigState", 1024), ("netEquipOOS", 2048)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3LineStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LineStatus.setDescription('')
teraUds3TransmitClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3TransmitClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3TransmitClockSource.setDescription('')
teraUds3InvalidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3InvalidIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3InvalidIntervals.setDescription('')
teraUds3LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ft-250", 1), ("ft-450", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3LineLength.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LineLength.setDescription('')
teraUds3LoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 64))).clone(namedValues=NamedValues(("noLoopback", 1), ("nearEndPayloadLoopback", 2), ("nearEndLineLoopback", 4), ("farEndLineLoopback", 64)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3LoopbackStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3LoopbackStatus.setDescription('')
teraUds3FarEndLineLoopbackTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 71581))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3FarEndLineLoopbackTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndLineLoopbackTimeout.setDescription('')
teraUds3SendFarEndLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("sendEnable", 2), ("sendDisable", 3), ("cancelLoopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3SendFarEndLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3SendFarEndLoopback.setDescription('')
teraUds3BERTConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 2), )
if mibBuilder.loadTexts: teraUds3BERTConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERTConfigTable.setDescription(' table teraUds3BERTConfigTable')
teraUds3BERTConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"))
if mibBuilder.loadTexts: teraUds3BERTConfigTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERTConfigTableEntry.setDescription(' table entry teraUds3BERTConfigTableEntry ')
teraUds3BERTPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("user", 2), ("qRSS", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3BERTPattern.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERTPattern.setDescription('')
teraUds3BERTUserPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3BERTUserPattern.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERTUserPattern.setDescription('')
teraUds3BERTSyncInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("n-a", 1), ("yes", 2), ("no", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3BERTSyncInfo.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERTSyncInfo.setDescription('')
teraUds3BERT_ES = MibScalar((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 4), Counter32()).setLabel("teraUds3BERT-ES").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3BERT_ES.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERT_ES.setDescription('')
teraUds3BERT_BES = MibScalar((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 5), Counter32()).setLabel("teraUds3BERT-BES").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3BERT_BES.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERT_BES.setDescription('')
teraUds3BERT_BER = MibScalar((1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 6), Counter32()).setLabel("teraUds3BERT-BER").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3BERT_BER.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3BERT_BER.setDescription('')
teraUds3ExtendTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 3), )
if mibBuilder.loadTexts: teraUds3ExtendTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalTable.setDescription(' table teraUds3ExtendTotalTable')
teraUds3ExtendTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "teraUds3ExtendTotalIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3ExtendTotalNumber"))
if mibBuilder.loadTexts: teraUds3ExtendTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalTableEntry.setDescription(' table entry teraUds3ExtendTotalTableEntry ')
teraUds3ExtendTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalIndex.setDescription('')
teraUds3ExtendTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalNumber.setDescription('')
teraUds3ExtendTotalPESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalPESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalPESs.setDescription('')
teraUds3ExtendTotalPSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalPSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalPSESs.setDescription('')
teraUds3ExtendTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalSEFSs.setDescription('')
teraUds3ExtendTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalUASs.setDescription('')
teraUds3ExtendTotalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalLCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalLCVs.setDescription('')
teraUds3ExtendTotalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalPCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalPCVs.setDescription('')
teraUds3ExtendTotalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalLESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalLESs.setDescription('')
teraUds3ExtendTotalCCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalCCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalCCVs.setDescription('')
teraUds3ExtendTotalCESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalCESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalCESs.setDescription('')
teraUds3ExtendTotalCSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalCSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalCSESs.setDescription('')
teraUds3ExtendTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3ExtendTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3ExtendTotalValidData.setDescription('')
teraUds3FarEndExtendTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 4), )
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalTable.setDescription(' table teraUds3FarEndExtendTotalTable')
teraUds3FarEndExtendTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "teraUds3FarEndExtendTotalIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3FarEndExtendTotalNumber"))
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalTableEntry.setDescription(' table entry teraUds3FarEndExtendTotalTableEntry ')
teraUds3FarEndExtendTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalIndex.setDescription('')
teraUds3FarEndExtendTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalNumber.setDescription('')
teraUds3FarEndExtendTotalCESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCESs.setDescription('')
teraUds3FarEndExtendTotalCSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCSESs.setDescription('')
teraUds3FarEndExtendTotalCCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalCCVs.setDescription('')
teraUds3FarEndExtendTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalUASs.setDescription('')
teraUds3FarEndExtendTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3FarEndExtendTotalValidData.setDescription('')
teraUds3atmInterfacePlcpIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 5), )
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalTable.setDescription(' table teraUds3atmInterfacePlcpIntervalTable')
teraUds3atmInterfacePlcpIntervalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfacePlcpIntervalNumber"))
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalTableEntry.setDescription(' table entry teraUds3atmInterfacePlcpIntervalTableEntry ')
teraUds3atmInterfacePlcpIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalNumber.setDescription('')
teraUds3atmInterfacePlcpIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalSEFSs.setDescription('')
teraUds3atmInterfacePlcpIntervalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAlarm", 0), ("receivedFarEndAlarm", 1), ("incomingLOF", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalAlarmState.setDescription('')
teraUds3atmInterfacePlcpIntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalUASs.setDescription('')
teraUds3atmInterfacePlcpIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpIntervalValidData.setDescription('')
teraUds3atmInterfacePlcpTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 6), )
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalTable.setDescription(' table teraUds3atmInterfacePlcpTotalTable')
teraUds3atmInterfacePlcpTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 6, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"))
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalTableEntry.setDescription(' table entry teraUds3atmInterfacePlcpTotalTableEntry ')
teraUds3atmInterfacePlcpTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalSEFSs.setDescription('')
teraUds3atmInterfacePlcpTotalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAlarm", 0), ("receivedFarEndAlarm", 1), ("incomingLOF", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalAlarmState.setDescription('')
teraUds3atmInterfacePlcpTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpTotalUASs.setDescription('')
teraUds3atmInterfacePlcpExtendTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 7), )
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalTable.setDescription(' table teraUds3atmInterfacePlcpExtendTotalTable')
teraUds3atmInterfacePlcpExtendTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfacePlcpExtendTotalNumber"))
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalTableEntry.setDescription(' table entry teraUds3atmInterfacePlcpExtendTotalTableEntry ')
teraUds3atmInterfacePlcpExtendTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalNumber.setDescription('')
teraUds3atmInterfacePlcpExtendTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalSEFSs.setDescription('')
teraUds3atmInterfacePlcpExtendTotalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAlarm", 0), ("receivedFarEndAlarm", 1), ("incomingLOF", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalAlarmState.setDescription('')
teraUds3atmInterfacePlcpExtendTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalUASs.setDescription('')
teraUds3atmInterfacePlcpExtendTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfacePlcpExtendTotalValidData.setDescription('')
teraUds3atmInterfaceTCIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 8), )
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalTable.setDescription(' table teraUds3atmInterfaceTCIntervalTable')
teraUds3atmInterfaceTCIntervalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 8, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfaceTCIntervalNumber"))
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalTableEntry.setDescription(' table entry teraUds3atmInterfaceTCIntervalTableEntry ')
teraUds3atmInterfaceTCIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalNumber.setDescription('')
teraUds3atmInterfaceTCIntervalOCDEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalOCDEvents.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalOCDEvents.setDescription('')
teraUds3atmInterfaceTCIntervalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("lcdFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalAlarmState.setDescription('')
teraUds3atmInterfaceTCIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCIntervalValidData.setDescription('')
teraUds3atmInterfaceTCTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 9), )
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalTable.setDescription(' table teraUds3atmInterfaceTCTotalTable')
teraUds3atmInterfaceTCTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 9, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"))
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalTableEntry.setDescription(' table entry teraUds3atmInterfaceTCTotalTableEntry ')
teraUds3atmInterfaceTCTotalOCDEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 9, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalOCDEvents.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalOCDEvents.setDescription('')
teraUds3atmInterfaceTCTotalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("lcdFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCTotalAlarmState.setDescription('')
teraUds3atmInterfaceTCExtendTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 10), )
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalTable.setDescription(' table teraUds3atmInterfaceTCExtendTotalTable')
teraUds3atmInterfaceTCExtendTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 10, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"), (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfaceTCExtendTotalNumber"))
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalTableEntry.setDescription(' table entry teraUds3atmInterfaceTCExtendTotalTableEntry ')
teraUds3atmInterfaceTCExtendTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalNumber.setDescription('')
teraUds3atmInterfaceTCExtendTotalOCDEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalOCDEvents.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalOCDEvents.setDescription('')
teraUds3atmInterfaceTCExtendTotalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("lcdFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalAlarmState.setDescription('')
teraUds3atmInterfaceTCExtendTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3atmInterfaceTCExtendTotalValidData.setDescription('')
teraUds3PMControlTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 15, 11), )
if mibBuilder.loadTexts: teraUds3PMControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3PMControlTable.setDescription(' table teraUds3PMControlTable')
teraUds3PMControlTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 15, 11, 1), ).setIndexNames((0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"))
if mibBuilder.loadTexts: teraUds3PMControlTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3PMControlTableEntry.setDescription(' table entry teraUds3PMControlTableEntry ')
teraUds3PMControlClearAll = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 15, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraUds3PMControlClearAll.setStatus('mandatory')
if mibBuilder.loadTexts: teraUds3PMControlClearAll.setDescription('')
mibBuilder.exportSymbols("TERAWAVE-teraU-ds3-MIB", teraUds3atmInterfacePlcpIntervalUASs=teraUds3atmInterfacePlcpIntervalUASs, teraUds3LineType=teraUds3LineType, teraUds3atmInterfaceTCIntervalTable=teraUds3atmInterfaceTCIntervalTable, teraUds3FarEndExtendTotalIndex=teraUds3FarEndExtendTotalIndex, teraUds3atmInterfacePlcpTotalTable=teraUds3atmInterfacePlcpTotalTable, teraUds3FarEndExtendTotalNumber=teraUds3FarEndExtendTotalNumber, teraUds3atmInterfaceTCTotalTable=teraUds3atmInterfaceTCTotalTable, teraUds3atmInterfacePlcpExtendTotalUASs=teraUds3atmInterfacePlcpExtendTotalUASs, teraUds3FarEndExtendTotalUASs=teraUds3FarEndExtendTotalUASs, teraUds3ExtendTotalUASs=teraUds3ExtendTotalUASs, teraUds3atmInterfaceTCExtendTotalOCDEvents=teraUds3atmInterfaceTCExtendTotalOCDEvents, teraUds3atmInterfaceTCIntervalTableEntry=teraUds3atmInterfaceTCIntervalTableEntry, teraUds3FarEndExtendTotalTableEntry=teraUds3FarEndExtendTotalTableEntry, teraUds3ExtendTotalSEFSs=teraUds3ExtendTotalSEFSs, teraUds3atmInterfacePlcpIntervalAlarmState=teraUds3atmInterfacePlcpIntervalAlarmState, teraUds3atmInterfacePlcpExtendTotalTableEntry=teraUds3atmInterfacePlcpExtendTotalTableEntry, teraUds3atmInterfacePlcpIntervalTable=teraUds3atmInterfacePlcpIntervalTable, teraUds3PMControlTableEntry=teraUds3PMControlTableEntry, teraUds3BERT_ES=teraUds3BERT_ES, teraUds3FarEndExtendTotalValidData=teraUds3FarEndExtendTotalValidData, terawave=terawave, teraUds3BERTPattern=teraUds3BERTPattern, teraUds3LoopbackConfig=teraUds3LoopbackConfig, teraUds3BERTUserPattern=teraUds3BERTUserPattern, teraUds3ExtendTotalCSESs=teraUds3ExtendTotalCSESs, teraUds3ExtendTotalTableEntry=teraUds3ExtendTotalTableEntry, teraUds3ExtendTotalPSESs=teraUds3ExtendTotalPSESs, teraUds3atmInterfacePlcpIntervalNumber=teraUds3atmInterfacePlcpIntervalNumber, teraUds3FarEndExtendTotalTable=teraUds3FarEndExtendTotalTable, teraUds3atmInterfacePlcpExtendTotalSEFSs=teraUds3atmInterfacePlcpExtendTotalSEFSs, teraUds3SendFarEndLoopback=teraUds3SendFarEndLoopback, teraUds3FarEndExtendTotalCESs=teraUds3FarEndExtendTotalCESs, teraUds3TransmitClockSource=teraUds3TransmitClockSource, teraUds3atmInterfaceTCIntervalNumber=teraUds3atmInterfaceTCIntervalNumber, teraUds3InvalidIntervals=teraUds3InvalidIntervals, teraUds3atmInterfaceTCExtendTotalAlarmState=teraUds3atmInterfaceTCExtendTotalAlarmState, teraUds3BERTSyncInfo=teraUds3BERTSyncInfo, teraUds3ConfigTable=teraUds3ConfigTable, teraUds3atmInterfaceTCExtendTotalTable=teraUds3atmInterfaceTCExtendTotalTable, teraUds3CircuitIdentifier=teraUds3CircuitIdentifier, teraUds3atmInterfacePlcpIntervalTableEntry=teraUds3atmInterfacePlcpIntervalTableEntry, teraUds3atmInterfacePlcpTotalAlarmState=teraUds3atmInterfacePlcpTotalAlarmState, teraUds3ExtendTotalTable=teraUds3ExtendTotalTable, teraUds3atmInterfacePlcpTotalUASs=teraUds3atmInterfacePlcpTotalUASs, teraUds3atmInterfacePlcpExtendTotalAlarmState=teraUds3atmInterfacePlcpExtendTotalAlarmState, teraUds3atmInterfacePlcpExtendTotalTable=teraUds3atmInterfacePlcpExtendTotalTable, teraUds3FarEndExtendTotalCCVs=teraUds3FarEndExtendTotalCCVs, teraUds3atmInterfaceTCTotalOCDEvents=teraUds3atmInterfaceTCTotalOCDEvents, teraUds3ExtendTotalValidData=teraUds3ExtendTotalValidData, teraUds3ValidIntervals=teraUds3ValidIntervals, teraUDs3Group=teraUDs3Group, teraUds3ExtendTotalPESs=teraUds3ExtendTotalPESs, teraUds3atmInterfaceTCIntervalAlarmState=teraUds3atmInterfaceTCIntervalAlarmState, teraUds3PMControlTable=teraUds3PMControlTable, teraUds3ConfigTableEntry=teraUds3ConfigTableEntry, teraUds3ExtendTotalCESs=teraUds3ExtendTotalCESs, teraUds3LoopbackStatus=teraUds3LoopbackStatus, teraUds3TimeElasped=teraUds3TimeElasped, teraUds3FarEndExtendTotalCSESs=teraUds3FarEndExtendTotalCSESs, teraUds3ExtendTotalLESs=teraUds3ExtendTotalLESs, teraUds3atmInterfacePlcpExtendTotalValidData=teraUds3atmInterfacePlcpExtendTotalValidData, teraUds3ExtendTotalIndex=teraUds3ExtendTotalIndex, teraUds3atmInterfaceTCIntervalOCDEvents=teraUds3atmInterfaceTCIntervalOCDEvents, teraUds3atmInterfaceTCIntervalValidData=teraUds3atmInterfaceTCIntervalValidData, teraUds3atmInterfacePlcpIntervalSEFSs=teraUds3atmInterfacePlcpIntervalSEFSs, teraUds3BERT_BES=teraUds3BERT_BES, teraUds3FarEndLineLoopbackTimeout=teraUds3FarEndLineLoopbackTimeout, teraUds3atmInterfaceTCTotalTableEntry=teraUds3atmInterfaceTCTotalTableEntry, teraUds3atmInterfacePlcpExtendTotalNumber=teraUds3atmInterfacePlcpExtendTotalNumber, teraUds3LineStatus=teraUds3LineStatus, teraUds3PMControlClearAll=teraUds3PMControlClearAll, teraUds3ATMMapping=teraUds3ATMMapping, teraUds3BERT_BER=teraUds3BERT_BER, teraUds3atmInterfaceTCExtendTotalValidData=teraUds3atmInterfaceTCExtendTotalValidData, teraUds3ExtendTotalCCVs=teraUds3ExtendTotalCCVs, teraUds3atmInterfacePlcpIntervalValidData=teraUds3atmInterfacePlcpIntervalValidData, teraUds3ExtendTotalLCVs=teraUds3ExtendTotalLCVs, teraUds3BERTConfigTable=teraUds3BERTConfigTable, teraUds3ExtendTotalNumber=teraUds3ExtendTotalNumber, teraUds3atmInterfaceTCExtendTotalTableEntry=teraUds3atmInterfaceTCExtendTotalTableEntry, teraUds3BERTConfigTableEntry=teraUds3BERTConfigTableEntry, teraUds3atmInterfaceTCTotalAlarmState=teraUds3atmInterfaceTCTotalAlarmState, teraUds3atmInterfacePlcpTotalSEFSs=teraUds3atmInterfacePlcpTotalSEFSs, teraUds3ExtendTotalPCVs=teraUds3ExtendTotalPCVs, teraUds3LineLength=teraUds3LineLength, teraUds3LineIndex=teraUds3LineIndex, teraUds3atmInterfaceTCExtendTotalNumber=teraUds3atmInterfaceTCExtendTotalNumber, teraUds3atmInterfacePlcpTotalTableEntry=teraUds3atmInterfacePlcpTotalTableEntry, teraUds3LineCoding=teraUds3LineCoding)