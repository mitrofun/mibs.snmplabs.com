#
# PySNMP MIB module DGS-1248T-B1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-1248T-B1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:28:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, iso, Gauge32, TimeTicks, Bits, NotificationType, Counter64, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "iso", "Gauge32", "TimeTicks", "Bits", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "enterprises")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
d_link = MibIdentifier((1, 3, 6, 1, 4, 1, 171)).setLabel("d-link")
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_DGS12XXTSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76)).setLabel("dlink-DGS12XXTSeriesProd")
dgs_1248tb1 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6)).setLabel("dgs-1248tb1")
class OwnerString(DisplayString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class PortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

companyCommGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1))
companyMiscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 3))
companySpanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 4))
companyConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11))
companyTVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13))
companyPortTrunkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14))
companyStaticGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21))
companyIgsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22))
companyDot1xGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23))
commSetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 1), )
if mibBuilder.loadTexts: commSetTable.setStatus('mandatory')
commSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 1, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "commSetIndex"))
if mibBuilder.loadTexts: commSetEntry.setStatus('mandatory')
commSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commSetIndex.setStatus('mandatory')
commSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commSetName.setStatus('mandatory')
commSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commSetStatus.setStatus('mandatory')
commGetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 2), )
if mibBuilder.loadTexts: commGetTable.setStatus('mandatory')
commGetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 2, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "commGetIndex"))
if mibBuilder.loadTexts: commGetEntry.setStatus('mandatory')
commGetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commGetIndex.setStatus('mandatory')
commGetName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commGetName.setStatus('mandatory')
commGetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commGetStatus.setStatus('mandatory')
commTrapTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3), )
if mibBuilder.loadTexts: commTrapTable.setStatus('mandatory')
commTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "commTrapIndex"))
if mibBuilder.loadTexts: commTrapEntry.setStatus('mandatory')
commTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commTrapIndex.setStatus('mandatory')
commTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapName.setStatus('mandatory')
commTrapIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapIpAddress.setStatus('mandatory')
commTrapSNMPBootup = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPBootup.setStatus('mandatory')
commTrapSNMPTPLinkUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPTPLinkUpDown.setStatus('mandatory')
commTrapSNMPFiberLinkUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPFiberLinkUpDown.setStatus('mandatory')
commTrapTrapAbnormalTPRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapTrapAbnormalTPRXError.setStatus('mandatory')
commTrapTrapAbnormalTPTXError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapTrapAbnormalTPTXError.setStatus('mandatory')
commTrapTrapAbnormalFiberRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapTrapAbnormalFiberRXError.setStatus('mandatory')
commTrapTrapAbnormalFiberTXError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapTrapAbnormalFiberTXError.setStatus('mandatory')
commTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 1, 3, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapStatus.setStatus('mandatory')
miscReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscReset.setStatus('mandatory')
miscStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscStatisticsReset.setStatus('mandatory')
spanOnOff = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spanOnOff.setStatus('mandatory')
configVerSwPrimary = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerSwPrimary.setStatus('mandatory')
configVerHwChipSet = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerHwChipSet.setStatus('mandatory')
configPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6), )
if mibBuilder.loadTexts: configPortTable.setStatus('mandatory')
configPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "configPort"))
if mibBuilder.loadTexts: configPortEntry.setStatus('mandatory')
configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPort.setStatus('mandatory')
configPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 1), ("auto", 2), ("rate10M-Half", 3), ("rate10M-Full", 4), ("rate100M-Half", 5), ("rate100M-Full", 6), ("rate1000M-Full", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortSpeed.setStatus('mandatory')
configPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("down", 1), ("rate10M-Half", 2), ("rate10M-Full", 3), ("rate100M-Half", 4), ("rate100M-Full", 5), ("rate1000M-Full", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortOperStatus.setStatus('mandatory')
configPortFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortFlowControl.setStatus('mandatory')
configPortFlowControlOper = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortFlowControlOper.setStatus('mandatory')
configPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("middle", 2), ("high", 3), ("highest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortPriority.setStatus('mandatory')
configVLANMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("modeTagBased", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configVLANMode.setStatus('mandatory')
configMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8), )
if mibBuilder.loadTexts: configMirrorTable.setStatus('mandatory')
configMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "configMirrorId"))
if mibBuilder.loadTexts: configMirrorEntry.setStatus('mandatory')
configMirrorId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configMirrorId.setStatus('mandatory')
configMirrorMon = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorMon.setStatus('mandatory')
configMirrorTXSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorTXSrc.setStatus('mandatory')
configMirrorRXSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorRXSrc.setStatus('mandatory')
configMirrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 8, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorStatus.setStatus('mandatory')
configSNMPEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSNMPEnable.setStatus('mandatory')
configIpAssignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcp", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAssignmentMode.setStatus('mandatory')
configPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPhysAddress.setStatus('mandatory')
configPasswordAdmin = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: configPasswordAdmin.setStatus('mandatory')
configIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAddress.setStatus('mandatory')
configNetMask = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configNetMask.setStatus('mandatory')
configGateway = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configGateway.setStatus('mandatory')
configSave = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("save", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSave.setStatus('mandatory')
configRestoreDefaults = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 11, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restore", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRestoreDefaults.setStatus('mandatory')
tvlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1), )
if mibBuilder.loadTexts: tvlanTable.setStatus('mandatory')
tvlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "tvlanId"))
if mibBuilder.loadTexts: tvlanEntry.setStatus('mandatory')
tvlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tvlanId.setStatus('mandatory')
tvlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanName.setStatus('mandatory')
tvlanMember = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanMember.setStatus('mandatory')
tvlanUntaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanUntaggedPorts.setStatus('mandatory')
tvlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notready", 3), ("createAndwait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanStatus.setStatus('mandatory')
portTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14, 1), )
if mibBuilder.loadTexts: portTrunkTable.setStatus('mandatory')
portTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14, 1, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "portTrunkId"), (0, "DGS-1248T-B1-MIB", "portTrunkMember"))
if mibBuilder.loadTexts: portTrunkEntry.setStatus('mandatory')
portTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTrunkId.setStatus('mandatory')
portTrunkName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrunkName.setStatus('mandatory')
portTrunkMember = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 14, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrunkMember.setStatus('mandatory')
staticOnOff = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticOnOff.setStatus('mandatory')
staticAutoLearning = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticAutoLearning.setStatus('mandatory')
staticTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3), )
if mibBuilder.loadTexts: staticTable.setStatus('mandatory')
staticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "staticId"))
if mibBuilder.loadTexts: staticEntry.setStatus('mandatory')
staticId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: staticId.setStatus('mandatory')
staticMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticMac.setStatus('mandatory')
staticPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticPort.setStatus('mandatory')
staticVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticVlanID.setStatus('mandatory')
staticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 21, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notready", 3), ("createAndwait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticStatus.setStatus('mandatory')
igsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1))
igsVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3))
igsStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsStatus.setStatus('mandatory')
igsv3Processing = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsv3Processing.setStatus('mandatory')
igsRouterPortPurgeInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsRouterPortPurgeInterval.setStatus('mandatory')
igsHostPortPurgeInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(130, 153025)).clone(260)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsHostPortPurgeInterval.setStatus('mandatory')
igsReportForwardInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25)).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsReportForwardInterval.setStatus('mandatory')
igsLeaveProcessInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsLeaveProcessInterval.setStatus('mandatory')
igsMcastEntryAgeingInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600)).clone(600)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsMcastEntryAgeingInterval.setStatus('mandatory')
igsSharedSegmentAggregationInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsSharedSegmentAggregationInterval.setStatus('mandatory')
igsGblReportFwdOnAllPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allports", 1), ("rtrports", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsGblReportFwdOnAllPorts.setStatus('mandatory')
igsNextMcastFwdMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipbased", 1), ("macbased", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsNextMcastFwdMode.setStatus('mandatory')
igsQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600)).clone(125)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsQueryInterval.setStatus('mandatory')
igsQueryMaxResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 25)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsQueryMaxResponseTime.setStatus('mandatory')
igsRobustnessValue = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 255)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsRobustnessValue.setStatus('mandatory')
igsLastMembQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsLastMembQueryInterval.setStatus('mandatory')
igsVlanMcastFwdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 1), )
if mibBuilder.loadTexts: igsVlanMcastFwdTable.setStatus('mandatory')
igsVlanMcastFwdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 1, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "igsVlanMcastFwdVlanIdMac"), (0, "DGS-1248T-B1-MIB", "igsVlanMcastFwdGroupAddress"))
if mibBuilder.loadTexts: igsVlanMcastFwdEntry.setStatus('mandatory')
igsVlanMcastFwdVlanIdMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: igsVlanMcastFwdVlanIdMac.setStatus('mandatory')
igsVlanMcastFwdGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: igsVlanMcastFwdGroupAddress.setStatus('mandatory')
igsVlanMcastFwdPortListMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 1, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsVlanMcastFwdPortListMac.setStatus('mandatory')
igsVlanRouterPortListTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 3), )
if mibBuilder.loadTexts: igsVlanRouterPortListTable.setStatus('mandatory')
igsVlanRouterPortListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 3, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "igsVlanRouterPortListVlanId"))
if mibBuilder.loadTexts: igsVlanRouterPortListEntry.setStatus('mandatory')
igsVlanRouterPortListVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: igsVlanRouterPortListVlanId.setStatus('mandatory')
igsVlanRouterPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 3, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igsVlanRouterPortList.setStatus('mandatory')
igsVlanFilterTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 4), )
if mibBuilder.loadTexts: igsVlanFilterTable.setStatus('mandatory')
igsVlanFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 4, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "igsVlanId"))
if mibBuilder.loadTexts: igsVlanFilterEntry.setStatus('mandatory')
igsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: igsVlanId.setStatus('mandatory')
igsVlanFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 22, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igsVlanFilterStatus.setStatus('mandatory')
radius = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 1))
dot1xAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2))
radiusServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusServerAddress.setStatus('mandatory')
radiusServerPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusServerPort.setStatus('mandatory')
radiusServerSharedSecret = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusServerSharedSecret.setStatus('mandatory')
dot1xAuthSystemControl = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthSystemControl.setStatus('mandatory')
dot1xAuthQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthQuietPeriod.setStatus('mandatory')
dot1xAuthTxPeriod = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthTxPeriod.setStatus('mandatory')
dot1xAuthSuppTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthSuppTimeout.setStatus('mandatory')
dot1xAuthServerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthServerTimeout.setStatus('mandatory')
dot1xAuthMaxReq = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthMaxReq.setStatus('mandatory')
dot1xAuthReAuthPeriod = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(3600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthPeriod.setStatus('mandatory')
dot1xAuthReAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthEnabled.setStatus('mandatory')
dot1xAuthConfigPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9), )
if mibBuilder.loadTexts: dot1xAuthConfigPortTable.setStatus('mandatory')
dot1xAuthConfigPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1), ).setIndexNames((0, "DGS-1248T-B1-MIB", "dot1xAuthConfigPortNumber"))
if mibBuilder.loadTexts: dot1xAuthConfigPortEntry.setStatus('mandatory')
dot1xAuthConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthConfigPortNumber.setStatus('mandatory')
dot1xAuthConfigPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthConfigPortControl.setStatus('mandatory')
dot1xAuthConfigPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("authnull", 0), ("authorized", 1), ("unauthorized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthConfigPortStatus.setStatus('mandatory')
dot1xAuthConfigPortSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthConfigPortSessionTime.setStatus('mandatory')
dot1xAuthConfigPortSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 76, 6, 23, 2, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthConfigPortSessionUserName.setStatus('mandatory')
swFiberInsert = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,1))
swFiberRemove = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,2))
swFiberAbnormalRXError = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,3))
swFiberAbnormalTXError = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,4))
swTPAbnormalRXError = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,5))
swTPAbnormalTXError = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 76, 6) + (0,6))
mibBuilder.exportSymbols("DGS-1248T-B1-MIB", configPhysAddress=configPhysAddress, igsSharedSegmentAggregationInterval=igsSharedSegmentAggregationInterval, swFiberAbnormalRXError=swFiberAbnormalRXError, dot1xAuthReAuthEnabled=dot1xAuthReAuthEnabled, companyCommGroup=companyCommGroup, commGetStatus=commGetStatus, commSetName=commSetName, miscReset=miscReset, portTrunkEntry=portTrunkEntry, igsVlanId=igsVlanId, dot1xAuthConfigPortTable=dot1xAuthConfigPortTable, companySpanGroup=companySpanGroup, d_link=d_link, igsReportForwardInterval=igsReportForwardInterval, miscStatisticsReset=miscStatisticsReset, igsGblReportFwdOnAllPorts=igsGblReportFwdOnAllPorts, dot1xAuth=dot1xAuth, radiusServerSharedSecret=radiusServerSharedSecret, igsRouterPortPurgeInterval=igsRouterPortPurgeInterval, commTrapTrapAbnormalFiberRXError=commTrapTrapAbnormalFiberRXError, tvlanEntry=tvlanEntry, dot1xAuthConfigPortSessionUserName=dot1xAuthConfigPortSessionUserName, tvlanId=tvlanId, swFiberInsert=swFiberInsert, configMirrorId=configMirrorId, commSetIndex=commSetIndex, staticMac=staticMac, igsMcastEntryAgeingInterval=igsMcastEntryAgeingInterval, staticPort=staticPort, commSetTable=commSetTable, dlink_products=dlink_products, commSetEntry=commSetEntry, dot1xAuthReAuthPeriod=dot1xAuthReAuthPeriod, PortList=PortList, igsRobustnessValue=igsRobustnessValue, commTrapTrapAbnormalTPTXError=commTrapTrapAbnormalTPTXError, configVerHwChipSet=configVerHwChipSet, commTrapIndex=commTrapIndex, igsSystem=igsSystem, dgs_1248tb1=dgs_1248tb1, commTrapStatus=commTrapStatus, staticVlanID=staticVlanID, igsLeaveProcessInterval=igsLeaveProcessInterval, configMirrorStatus=configMirrorStatus, igsVlanFilterTable=igsVlanFilterTable, commTrapIpAddress=commTrapIpAddress, commGetIndex=commGetIndex, configPortPriority=configPortPriority, configIpAssignmentMode=configIpAssignmentMode, commGetTable=commGetTable, igsVlanMcastFwdVlanIdMac=igsVlanMcastFwdVlanIdMac, commTrapTable=commTrapTable, igsVlanFilterEntry=igsVlanFilterEntry, configPortSpeed=configPortSpeed, companyTVlanGroup=companyTVlanGroup, spanOnOff=spanOnOff, companyPortTrunkGroup=companyPortTrunkGroup, tvlanStatus=tvlanStatus, staticId=staticId, tvlanMember=tvlanMember, igsVlanMcastFwdPortListMac=igsVlanMcastFwdPortListMac, configGateway=configGateway, swTPAbnormalRXError=swTPAbnormalRXError, configMirrorRXSrc=configMirrorRXSrc, portTrunkId=portTrunkId, igsVlanMcastFwdGroupAddress=igsVlanMcastFwdGroupAddress, commTrapSNMPBootup=commTrapSNMPBootup, configPortOperStatus=configPortOperStatus, dot1xAuthQuietPeriod=dot1xAuthQuietPeriod, staticEntry=staticEntry, dot1xAuthConfigPortControl=dot1xAuthConfigPortControl, configSave=configSave, commTrapEntry=commTrapEntry, commSetStatus=commSetStatus, dot1xAuthSuppTimeout=dot1xAuthSuppTimeout, MacAddress=MacAddress, commTrapSNMPTPLinkUpDown=commTrapSNMPTPLinkUpDown, companyIgsGroup=companyIgsGroup, configPortFlowControlOper=configPortFlowControlOper, igsVlanRouterPortListVlanId=igsVlanRouterPortListVlanId, swTPAbnormalTXError=swTPAbnormalTXError, igsVlan=igsVlan, igsStatus=igsStatus, staticTable=staticTable, igsQueryMaxResponseTime=igsQueryMaxResponseTime, dot1xAuthSystemControl=dot1xAuthSystemControl, configPort=configPort, tvlanUntaggedPorts=tvlanUntaggedPorts, igsVlanRouterPortListTable=igsVlanRouterPortListTable, swFiberRemove=swFiberRemove, configRestoreDefaults=configRestoreDefaults, companyDot1xGroup=companyDot1xGroup, igsVlanFilterStatus=igsVlanFilterStatus, dot1xAuthConfigPortEntry=dot1xAuthConfigPortEntry, configSNMPEnable=configSNMPEnable, configMirrorMon=configMirrorMon, igsNextMcastFwdMode=igsNextMcastFwdMode, companyMiscGroup=companyMiscGroup, companyConfigGroup=companyConfigGroup, tvlanTable=tvlanTable, commTrapTrapAbnormalTPRXError=commTrapTrapAbnormalTPRXError, igsLastMembQueryInterval=igsLastMembQueryInterval, companyStaticGroup=companyStaticGroup, configNetMask=configNetMask, tvlanName=tvlanName, igsVlanRouterPortListEntry=igsVlanRouterPortListEntry, configPasswordAdmin=configPasswordAdmin, dot1xAuthTxPeriod=dot1xAuthTxPeriod, dot1xAuthConfigPortNumber=dot1xAuthConfigPortNumber, configPortEntry=configPortEntry, portTrunkName=portTrunkName, configIpAddress=configIpAddress, dot1xAuthConfigPortStatus=dot1xAuthConfigPortStatus, igsv3Processing=igsv3Processing, swFiberAbnormalTXError=swFiberAbnormalTXError, configMirrorTable=configMirrorTable, radius=radius, configMirrorEntry=configMirrorEntry, configPortTable=configPortTable, igsVlanRouterPortList=igsVlanRouterPortList, commGetName=commGetName, igsVlanMcastFwdEntry=igsVlanMcastFwdEntry, dlink_DGS12XXTSeriesProd=dlink_DGS12XXTSeriesProd, RowStatus=RowStatus, commTrapTrapAbnormalFiberTXError=commTrapTrapAbnormalFiberTXError, portTrunkTable=portTrunkTable, OwnerString=OwnerString, commGetEntry=commGetEntry, configMirrorTXSrc=configMirrorTXSrc, portTrunkMember=portTrunkMember, dot1xAuthMaxReq=dot1xAuthMaxReq, commTrapName=commTrapName, configPortFlowControl=configPortFlowControl, igsQueryInterval=igsQueryInterval, configVerSwPrimary=configVerSwPrimary, radiusServerAddress=radiusServerAddress, configVLANMode=configVLANMode, radiusServerPort=radiusServerPort, dot1xAuthServerTimeout=dot1xAuthServerTimeout, staticOnOff=staticOnOff, dot1xAuthConfigPortSessionTime=dot1xAuthConfigPortSessionTime, commTrapSNMPFiberLinkUpDown=commTrapSNMPFiberLinkUpDown, igsHostPortPurgeInterval=igsHostPortPurgeInterval, staticStatus=staticStatus, staticAutoLearning=staticAutoLearning, igsVlanMcastFwdTable=igsVlanMcastFwdTable)