#
# PySNMP MIB module NETSTAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSTAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifDescr, ifIndex, ifInOctets, ifOutOctets = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex", "ifInOctets", "ifOutOctets")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmp, = mibBuilder.importSymbols("SNMPv2-MIB", "snmp")
ModuleIdentity, NotificationType, Bits, TimeTicks, Counter64, Unsigned32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, Counter32, Integer32, ObjectIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks", "Counter64", "Unsigned32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netstar = MibIdentifier((1, 3, 6, 1, 4, 1, 1080))
netstar_products = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1)).setLabel("netstar-products")
netstar_daemons = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2)).setLabel("netstar-daemons")
gigarouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1))
clusterswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 2))
gr2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 3))
grf = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 4))
grf400 = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 4, 1))
grf1600 = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 4, 2))
mib2Daemon = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2, 1))
frameRelayDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2, 2))
dynamicRoutingDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2, 3))
mibmgrDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2, 4))
atmpDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 2, 5))
grChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1))
grHIPPI = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 2))
grFDDI4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 3))
grAtmV1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4))
grAtmUNI = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 5))
grThreshPoll = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6))
grPingLog = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 7))
grAtmp = MibIdentifier((1, 3, 6, 1, 4, 1, 1080, 1, 1, 8))
grPowerSupplyStatus = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPowerSupplyStatus.setStatus('mandatory')
grTempStatus = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("over-temp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grTempStatus.setStatus('mandatory')
grFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grFanStatus.setStatus('mandatory')
grPortCardNumber = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPortCardNumber.setStatus('mandatory')
grPortCardTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5), )
if mibBuilder.loadTexts: grPortCardTable.setStatus('mandatory')
grPortCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1), ).setIndexNames((0, "NETSTAR-MIB", "grPortCardSlot"))
if mibBuilder.loadTexts: grPortCardEntry.setStatus('mandatory')
grPortCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPortCardSlot.setStatus('mandatory')
grPortCardHWtype = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("none", 0), ("hippi", 3), ("fddi", 4), ("rmb", 6), ("atm", 7), ("hssi", 8), ("ibmSP", 9), ("atmq-oc3", 10), ("fddiq", 11), ("atm-oc12", 12), ("ethernet", 13), ("sonet-oc3", 14), ("cddi", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPortCardHWtype.setStatus('mandatory')
grPortCardCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99))).clone(namedValues=NamedValues(("empty", 1), ("power-up", 2), ("boot-requested", 3), ("dumping", 4), ("loading", 5), ("configuring", 6), ("running", 7), ("not-responding", 8), ("panic", 9), ("held-reset", 10), ("other", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPortCardCurrentState.setStatus('mandatory')
grGatedStatus = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("not-running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grGatedStatus.setStatus('mandatory')
grTransportMethod = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ftp", 0), ("tftp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grTransportMethod.setStatus('mandatory')
grFTPUserName = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grFTPUserName.setStatus('mandatory')
grFTPPassword = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grFTPPassword.setStatus('mandatory')
grServerName = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grServerName.setStatus('mandatory')
grFileName = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grFileName.setStatus('mandatory')
grLastOperation = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grLastOperation.setStatus('mandatory')
grStatusMsg = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grStatusMsg.setStatus('mandatory')
grBackup = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grBackup.setStatus('mandatory')
grCompare = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grCompare.setStatus('mandatory')
grRestore = MibScalar((1, 3, 6, 1, 4, 1, 1080, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grRestore.setStatus('mandatory')
grAtmV1VcTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1), )
if mibBuilder.loadTexts: grAtmV1VcTable.setStatus('mandatory')
grAtmV1VcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1), ).setIndexNames((0, "NETSTAR-MIB", "grAtmV1VcIfIndex"), (0, "NETSTAR-MIB", "grAtmV1VcVpi"), (0, "NETSTAR-MIB", "grAtmV1VcVci"))
if mibBuilder.loadTexts: grAtmV1VcEntry.setStatus('mandatory')
grAtmV1VcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcIfIndex.setStatus('mandatory')
grAtmV1VcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcVpi.setStatus('mandatory')
grAtmV1VcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcVci.setStatus('mandatory')
grAtmV1VcAal = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aal3", 1), ("aal5", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcAal.setStatus('mandatory')
grAtmV1VcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ip-llc", 1), ("ip-null", 2), ("uni", 3), ("diag0", 4), ("diag1", 5), ("raw", 6), ("other", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcProtocol.setStatus('mandatory')
grAtmV1VcDestIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcDestIfIndex.setStatus('mandatory')
grAtmV1VcDestVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcDestVpi.setStatus('mandatory')
grAtmV1VcDestVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcDestVci.setStatus('mandatory')
grAtmV1VcRateq = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcRateq.setStatus('mandatory')
grAtmV1VcType = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("switched", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1VcType.setStatus('mandatory')
grAtmV1RateqTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3), )
if mibBuilder.loadTexts: grAtmV1RateqTable.setStatus('mandatory')
grAtmV1RateqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1), ).setIndexNames((0, "NETSTAR-MIB", "grAtmV1RateqIfIndex"), (0, "NETSTAR-MIB", "grAtmV1RateqIndex"))
if mibBuilder.loadTexts: grAtmV1RateqEntry.setStatus('mandatory')
grAtmV1RateqIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1RateqIfIndex.setStatus('mandatory')
grAtmV1RateqIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1RateqIndex.setStatus('mandatory')
grAtmV1RateqRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1RateqRate.setStatus('mandatory')
grAtmV1RateqState = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1RateqState.setStatus('mandatory')
grAtmV1NetToVcTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4), )
if mibBuilder.loadTexts: grAtmV1NetToVcTable.setStatus('mandatory')
grAtmV1NetToVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1), ).setIndexNames((0, "NETSTAR-MIB", "grAtmV1NetToVcIfIndex"), (0, "NETSTAR-MIB", "grAtmV1NetToVcNetAddress"))
if mibBuilder.loadTexts: grAtmV1NetToVcEntry.setStatus('mandatory')
grAtmV1NetToVcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1NetToVcIfIndex.setStatus('mandatory')
grAtmV1NetToVcNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1NetToVcNetAddress.setStatus('mandatory')
grAtmV1NetToVcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1NetToVcVpi.setStatus('mandatory')
grAtmV1NetToVcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1NetToVcVci.setStatus('mandatory')
grAtmV1NetToVcState = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: grAtmV1NetToVcState.setStatus('mandatory')
grThreshPollTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3), )
if mibBuilder.loadTexts: grThreshPollTable.setStatus('mandatory')
grThreshPollEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: grThreshPollEntry.setStatus('mandatory')
grTPCurrentCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grTPCurrentCount.setStatus('mandatory')
grTPPreviousCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grTPPreviousCount.setStatus('mandatory')
grTPCurrentCountUpper = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grTPCurrentCountUpper.setStatus('mandatory')
grTPPreviousCountUpper = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 6, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: grTPPreviousCountUpper.setStatus('mandatory')
grPingLogTable = MibTable((1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1), )
if mibBuilder.loadTexts: grPingLogTable.setStatus('mandatory')
grPingLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: grPingLogEntry.setStatus('mandatory')
grPLDevDownMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 1080, 1, 1, 7, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: grPLDevDownMsg.setStatus('mandatory')
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4))
grPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,1)).setObjects(("NETSTAR-MIB", "grPowerSupplyStatus"))
grOverTemp = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,2)).setObjects(("NETSTAR-MIB", "grTempStatus"))
grFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,3)).setObjects(("NETSTAR-MIB", "grFanStatus"))
grCardDown = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,4)).setObjects(("NETSTAR-MIB", "grPortCardSlot"), ("NETSTAR-MIB", "grPortCardCurrentState"))
grCardUp = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,5)).setObjects(("NETSTAR-MIB", "grPortCardSlot"))
grSONETLossOfFrame = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,6)).setObjects(("IF-MIB", "ifIndex"))
grSONETLossOfSignal = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
grSONETSTSPathLossOfPointer = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,8)).setObjects(("IF-MIB", "ifIndex"))
grSONETVTLossOfPointer = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,9)).setObjects(("IF-MIB", "ifIndex"))
grSONETLineAlarmIndicationSignal = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,10)).setObjects(("IF-MIB", "ifIndex"))
grSONETSTSPathAlarmIndicationSignal = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,11)).setObjects(("IF-MIB", "ifIndex"))
grSONETVTPathAlarmIndicationSignal = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,12)).setObjects(("IF-MIB", "ifIndex"))
grSONETLineRemoteDefectIndication = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,13)).setObjects(("IF-MIB", "ifIndex"))
grSONETVTPathRemoteDefectIndication = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,14)).setObjects(("IF-MIB", "ifIndex"))
grSONETTCLossOfCellDelineation = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,15)).setObjects(("IF-MIB", "ifIndex"))
grAtmPVCUp = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,16)).setObjects(("IF-MIB", "ifIndex"), ("NETSTAR-MIB", "grAtmV1VcVpi"), ("NETSTAR-MIB", "grAtmV1VcVci"))
grAtmPVCDown = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,17)).setObjects(("IF-MIB", "ifIndex"), ("NETSTAR-MIB", "grAtmV1VcVpi"), ("NETSTAR-MIB", "grAtmV1VcVci"))
grInterfaceDown = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,18)).setObjects(("NETSTAR-MIB", "grPLDevDownMsg"))
grIfInOctetsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,19)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInOctetsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,20)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutOctetsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,21)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutOctetsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,22)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInUcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,23)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInUcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,24)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutUcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,25)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutUcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,26)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInErrorsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,27)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInErrorsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,28)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutErrorsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,29)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutErrorsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,30)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInDiscardsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,31)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfInDiscardsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,32)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutDiscardsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,33)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfOutDiscardsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,34)).setObjects(("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCount"))
grGatedDown = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,35))
grSnmpReset = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,36))
grIfHCInOctetsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,37)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInOctetsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,38)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInUcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,39)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInUcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,40)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInMulticastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,41)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInMulticastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,42)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInBroadcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,43)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCInBroadcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,44)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutOctetsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,45)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutOctetsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,46)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutUcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,47)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutUcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,48)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutMulticastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,49)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutMulticastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,50)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutBroadcastPktsHigh = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,51)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grIfHCOutBroadcastPktsLow = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,52)).setObjects(("NETSTAR-MIB", "grTPPreviousCountUpper"), ("NETSTAR-MIB", "grTPPreviousCount"), ("NETSTAR-MIB", "grTPCurrentCountUpper"), ("NETSTAR-MIB", "grTPCurrentCount"))
grBackupRestoreMessages = NotificationType((1, 3, 6, 1, 4, 1, 1080, 1, 1) + (0,53)).setObjects(("NETSTAR-MIB", "grStatusMsg"))
mibBuilder.exportSymbols("NETSTAR-MIB", grAtmV1=grAtmV1, grIfHCOutOctetsLow=grIfHCOutOctetsLow, grFDDI4=grFDDI4, grCompare=grCompare, grFTPUserName=grFTPUserName, grIfInOctetsHigh=grIfInOctetsHigh, grIfHCInBroadcastPktsLow=grIfHCInBroadcastPktsLow, grIfHCInUcastPktsLow=grIfHCInUcastPktsLow, grIfHCInMulticastPktsHigh=grIfHCInMulticastPktsHigh, grAtmUNI=grAtmUNI, mib2Daemon=mib2Daemon, grAtmV1NetToVcVpi=grAtmV1NetToVcVpi, grPortCardCurrentState=grPortCardCurrentState, grIfHCOutMulticastPktsHigh=grIfHCOutMulticastPktsHigh, grBackupRestoreMessages=grBackupRestoreMessages, grThreshPoll=grThreshPoll, grPortCardTable=grPortCardTable, grStatusMsg=grStatusMsg, grAtmV1NetToVcIfIndex=grAtmV1NetToVcIfIndex, grOverTemp=grOverTemp, grSONETTCLossOfCellDelineation=grSONETTCLossOfCellDelineation, grIfOutUcastPktsLow=grIfOutUcastPktsLow, grSONETLossOfSignal=grSONETLossOfSignal, grf400=grf400, grPowerSupplyFailure=grPowerSupplyFailure, grPowerSupplyStatus=grPowerSupplyStatus, grGatedStatus=grGatedStatus, grIfInErrorsLow=grIfInErrorsLow, grAtmV1VcDestVpi=grAtmV1VcDestVpi, grIfOutErrorsHigh=grIfOutErrorsHigh, grTPPreviousCountUpper=grTPPreviousCountUpper, grAtmV1VcType=grAtmV1VcType, linkUp=linkUp, grIfHCInMulticastPktsLow=grIfHCInMulticastPktsLow, grIfOutOctetsLow=grIfOutOctetsLow, grInterfaceDown=grInterfaceDown, grIfOutUcastPktsHigh=grIfOutUcastPktsHigh, grIfInOctetsLow=grIfInOctetsLow, grTempStatus=grTempStatus, grServerName=grServerName, grSONETSTSPathLossOfPointer=grSONETSTSPathLossOfPointer, grAtmV1VcDestVci=grAtmV1VcDestVci, netstar=netstar, grIfHCOutMulticastPktsLow=grIfHCOutMulticastPktsLow, grAtmp=grAtmp, grLastOperation=grLastOperation, grTransportMethod=grTransportMethod, grAtmV1VcAal=grAtmV1VcAal, grPingLog=grPingLog, grAtmV1RateqIndex=grAtmV1RateqIndex, grTPCurrentCountUpper=grTPCurrentCountUpper, grAtmV1NetToVcTable=grAtmV1NetToVcTable, grAtmV1NetToVcVci=grAtmV1NetToVcVci, grHIPPI=grHIPPI, grIfOutOctetsHigh=grIfOutOctetsHigh, grIfInErrorsHigh=grIfInErrorsHigh, grIfHCInOctetsHigh=grIfHCInOctetsHigh, grIfOutDiscardsHigh=grIfOutDiscardsHigh, grIfInUcastPktsLow=grIfInUcastPktsLow, grTPCurrentCount=grTPCurrentCount, grAtmV1VcTable=grAtmV1VcTable, atmpDaemon=atmpDaemon, grFileName=grFileName, grPingLogEntry=grPingLogEntry, netstar_products=netstar_products, grGatedDown=grGatedDown, grFanFailure=grFanFailure, grSONETLossOfFrame=grSONETLossOfFrame, grIfHCOutBroadcastPktsHigh=grIfHCOutBroadcastPktsHigh, grAtmV1NetToVcState=grAtmV1NetToVcState, grSONETVTLossOfPointer=grSONETVTLossOfPointer, gigarouter=gigarouter, grAtmPVCUp=grAtmPVCUp, frameRelayDaemon=frameRelayDaemon, grBackup=grBackup, authenticationFailure=authenticationFailure, grPortCardHWtype=grPortCardHWtype, grThreshPollTable=grThreshPollTable, mibmgrDaemon=mibmgrDaemon, clusterswitch=clusterswitch, grCardDown=grCardDown, grIfHCOutUcastPktsHigh=grIfHCOutUcastPktsHigh, grIfHCInUcastPktsHigh=grIfHCInUcastPktsHigh, grAtmV1RateqEntry=grAtmV1RateqEntry, grAtmV1VcIfIndex=grAtmV1VcIfIndex, grIfInUcastPktsHigh=grIfInUcastPktsHigh, grSONETVTPathAlarmIndicationSignal=grSONETVTPathAlarmIndicationSignal, grIfHCOutOctetsHigh=grIfHCOutOctetsHigh, grIfOutErrorsLow=grIfOutErrorsLow, dynamicRoutingDaemon=dynamicRoutingDaemon, grIfHCInBroadcastPktsHigh=grIfHCInBroadcastPktsHigh, grSONETLineAlarmIndicationSignal=grSONETLineAlarmIndicationSignal, grIfOutDiscardsLow=grIfOutDiscardsLow, grIfInDiscardsLow=grIfInDiscardsLow, grPortCardNumber=grPortCardNumber, grAtmV1RateqIfIndex=grAtmV1RateqIfIndex, grSONETLineRemoteDefectIndication=grSONETLineRemoteDefectIndication, linkDown=linkDown, grf1600=grf1600, grTPPreviousCount=grTPPreviousCount, grPLDevDownMsg=grPLDevDownMsg, grSONETVTPathRemoteDefectIndication=grSONETVTPathRemoteDefectIndication, grIfInDiscardsHigh=grIfInDiscardsHigh, warmStart=warmStart, grAtmPVCDown=grAtmPVCDown, grAtmV1NetToVcNetAddress=grAtmV1NetToVcNetAddress, grRestore=grRestore, grFanStatus=grFanStatus, grIfHCOutUcastPktsLow=grIfHCOutUcastPktsLow, grFTPPassword=grFTPPassword, grAtmV1VcDestIfIndex=grAtmV1VcDestIfIndex, grAtmV1RateqRate=grAtmV1RateqRate, grIfHCOutBroadcastPktsLow=grIfHCOutBroadcastPktsLow, grAtmV1NetToVcEntry=grAtmV1NetToVcEntry, grPortCardSlot=grPortCardSlot, grAtmV1RateqState=grAtmV1RateqState, grCardUp=grCardUp, coldStart=coldStart, grf=grf, grAtmV1RateqTable=grAtmV1RateqTable, grPortCardEntry=grPortCardEntry, grAtmV1VcProtocol=grAtmV1VcProtocol, grThreshPollEntry=grThreshPollEntry, grAtmV1VcEntry=grAtmV1VcEntry, grAtmV1VcVpi=grAtmV1VcVpi, grAtmV1VcVci=grAtmV1VcVci, grAtmV1VcRateq=grAtmV1VcRateq, grIfHCInOctetsLow=grIfHCInOctetsLow, netstar_daemons=netstar_daemons, grPingLogTable=grPingLogTable, grChassis=grChassis, grSONETSTSPathAlarmIndicationSignal=grSONETSTSPathAlarmIndicationSignal, grSnmpReset=grSnmpReset, gr2=gr2)
