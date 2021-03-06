#
# PySNMP MIB module TPLINK-ETHERNETOAMDISCINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMDISCINFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, Counter64, iso, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "Counter64", "iso", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ethernetOamDiscoveryInfo, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamDiscoveryInfo")
ethernetOamDiscInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1), )
if mibBuilder.loadTexts: ethernetOamDiscInfoTable.setStatus('current')
ethernetOamDiscInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamDiscInfoEntry.setStatus('current')
ethernetOamDiscInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoPort.setStatus('current')
ethernetOamDiscInfoLocOAM = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocOAM.setStatus('current')
ethernetOamDiscInfoLocMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocMode.setStatus('current')
ethernetOamDiscInfoLocMaxOAMPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocMaxOAMPDU.setStatus('current')
ethernetOamDiscInfoLocRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocRemoteLoopback.setStatus('current')
ethernetOamDiscInfoLocUnidirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocUnidirection.setStatus('current')
ethernetOamDiscInfoLocLinkMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocLinkMonitoring.setStatus('current')
ethernetOamDiscInfoLocVariableRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocVariableRequest.setStatus('current')
ethernetOamDiscInfoLocPduRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocPduRevision.setStatus('current')
ethernetOamDiscInfoLocOperationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocOperationStatus.setStatus('current')
ethernetOamDiscInfoLocLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoLocLoopbackStatus.setStatus('current')
ethernetOamDiscInfoRmtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtMode.setStatus('current')
ethernetOamDiscInfoRmtMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtMacAddress.setStatus('current')
ethernetOamDiscInfoRmtVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtVendorOUI.setStatus('current')
ethernetOamDiscInfoRmtMaxOAMPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtMaxOAMPDU.setStatus('current')
ethernetOamDiscInfoRmtRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtRemoteLoopback.setStatus('current')
ethernetOamDiscInfoRmtUnidirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtUnidirection.setStatus('current')
ethernetOamDiscInfoRmtLinkMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtLinkMonitoring.setStatus('current')
ethernetOamDiscInfoRmtVariableRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-supported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtVariableRequest.setStatus('current')
ethernetOamDiscInfoRmtPduRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtPduRevision.setStatus('current')
ethernetOamDiscInfoRmtVendorInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamDiscInfoRmtVendorInfo.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMDISCINFO-MIB", ethernetOamDiscInfoLocPduRevision=ethernetOamDiscInfoLocPduRevision, ethernetOamDiscInfoRmtUnidirection=ethernetOamDiscInfoRmtUnidirection, ethernetOamDiscInfoLocRemoteLoopback=ethernetOamDiscInfoLocRemoteLoopback, ethernetOamDiscInfoRmtVendorInfo=ethernetOamDiscInfoRmtVendorInfo, ethernetOamDiscInfoEntry=ethernetOamDiscInfoEntry, ethernetOamDiscInfoRmtRemoteLoopback=ethernetOamDiscInfoRmtRemoteLoopback, ethernetOamDiscInfoRmtMode=ethernetOamDiscInfoRmtMode, ethernetOamDiscInfoLocOperationStatus=ethernetOamDiscInfoLocOperationStatus, ethernetOamDiscInfoRmtVariableRequest=ethernetOamDiscInfoRmtVariableRequest, ethernetOamDiscInfoRmtMaxOAMPDU=ethernetOamDiscInfoRmtMaxOAMPDU, ethernetOamDiscInfoLocUnidirection=ethernetOamDiscInfoLocUnidirection, ethernetOamDiscInfoLocVariableRequest=ethernetOamDiscInfoLocVariableRequest, ethernetOamDiscInfoLocLoopbackStatus=ethernetOamDiscInfoLocLoopbackStatus, ethernetOamDiscInfoRmtVendorOUI=ethernetOamDiscInfoRmtVendorOUI, ethernetOamDiscInfoRmtLinkMonitoring=ethernetOamDiscInfoRmtLinkMonitoring, ethernetOamDiscInfoRmtPduRevision=ethernetOamDiscInfoRmtPduRevision, ethernetOamDiscInfoLocMode=ethernetOamDiscInfoLocMode, ethernetOamDiscInfoLocOAM=ethernetOamDiscInfoLocOAM, ethernetOamDiscInfoLocMaxOAMPDU=ethernetOamDiscInfoLocMaxOAMPDU, ethernetOamDiscInfoTable=ethernetOamDiscInfoTable, ethernetOamDiscInfoLocLinkMonitoring=ethernetOamDiscInfoLocLinkMonitoring, ethernetOamDiscInfoRmtMacAddress=ethernetOamDiscInfoRmtMacAddress, ethernetOamDiscInfoPort=ethernetOamDiscInfoPort)
