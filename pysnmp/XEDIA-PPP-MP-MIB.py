#
# PySNMP MIB module XEDIA-PPP-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-PPP-MP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, iso, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, Counter64, NotificationType, Gauge32, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaPppMpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 21))
if mibBuilder.loadTexts: xediaPppMpMIB.setLastUpdated('9809171500Z')
if mibBuilder.loadTexts: xediaPppMpMIB.setOrganization('Xedia Corp.')
xediaPppMpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 1))
xediaPppMpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2))
mpBundle = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1))
class Unsigned32(Gauge32):
    pass

mpBundleStatusTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1), )
if mibBuilder.loadTexts: mpBundleStatusTable.setStatus('current')
mpBundleStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mpBundleStatusEntry.setStatus('current')
mpBundleStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusPacketTooLongs.setStatus('current')
mpBundleStatusLocalMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusLocalMRRU.setStatus('current')
mpBundleStatusRemoteMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRemoteMRRU.setStatus('current')
mpBundleStatusLocalEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(21, 21)).setFixedLength(21)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusLocalEndptDiscr.setStatus('current')
mpBundleStatusRemoteEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRemoteEndptDiscr.setStatus('current')
mpBundleStatusRcvShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvShortSeq.setStatus('current')
mpBundleStatusXmtShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusXmtShortSeq.setStatus('current')
mpBundleStatusSmallPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSmallPktMaxSize.setStatus('current')
mpBundleStatusMediumPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusMediumPktMaxSize.setStatus('current')
mpBundleStatusSingleFragsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSingleFragsRcvd.setStatus('current')
mpBundleStatusReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmReqds.setStatus('current')
mpBundleStatusReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmFails.setStatus('current')
mpBundleStatusReasmOks = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmOks.setStatus('current')
mpBundleStatusRcvdFragsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsDiscarded.setStatus('current')
mpBundleStatusDropTooManyFrags = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusDropTooManyFrags.setStatus('current')
mpBundleStatusSingleFragsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSingleFragsSent.setStatus('current')
mpBundleStatusFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragCreates.setStatus('current')
mpBundleStatusFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragFails.setStatus('current')
mpBundleStatusFragOks = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragOks.setStatus('current')
mpBundleStatusRcvdFragsBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsBuffered.setStatus('current')
mpBundleConfigTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2), )
if mibBuilder.loadTexts: mpBundleConfigTable.setStatus('current')
mpBundleConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mpBundleConfigEntry.setStatus('current')
mpBundleConfigLocalMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigLocalMRRU.setStatus('current')
mpBundleConfigLocalEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 21)).clone(hexValue="0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigLocalEndptDiscr.setStatus('current')
mpBundleConfigRcvShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigRcvShortSeq.setStatus('current')
mpBundleConfigSmallPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigSmallPktMaxSize.setStatus('current')
mpBundleConfigMediumPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigMediumPktMaxSize.setStatus('current')
mpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1))
mpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2))
mpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1, 1)).setObjects(("XEDIA-PPP-MP-MIB", "mpAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpCompliance = mpCompliance.setStatus('current')
mpAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2, 1)).setObjects(("XEDIA-PPP-MP-MIB", "mpBundleStatusPacketTooLongs"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusXmtShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSmallPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusMediumPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsRcvd"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmReqds"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmFails"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmOks"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsDiscarded"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusDropTooManyFrags"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsSent"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragCreates"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragFails"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragOks"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsBuffered"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigRcvShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigSmallPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigMediumPktMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpAllGroup = mpAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-PPP-MP-MIB", mpBundleConfigRcvShortSeq=mpBundleConfigRcvShortSeq, mpBundleStatusTable=mpBundleStatusTable, mpBundleStatusPacketTooLongs=mpBundleStatusPacketTooLongs, mpCompliances=mpCompliances, mpBundleConfigMediumPktMaxSize=mpBundleConfigMediumPktMaxSize, mpBundleStatusReasmOks=mpBundleStatusReasmOks, mpBundleStatusRemoteMRRU=mpBundleStatusRemoteMRRU, mpBundleStatusSingleFragsRcvd=mpBundleStatusSingleFragsRcvd, mpBundleConfigTable=mpBundleConfigTable, mpBundleConfigEntry=mpBundleConfigEntry, PYSNMP_MODULE_ID=xediaPppMpMIB, xediaPppMpObjects=xediaPppMpObjects, mpBundleStatusRemoteEndptDiscr=mpBundleStatusRemoteEndptDiscr, mpBundleStatusLocalMRRU=mpBundleStatusLocalMRRU, mpBundleStatusFragOks=mpBundleStatusFragOks, mpBundleStatusFragCreates=mpBundleStatusFragCreates, mpBundleConfigLocalEndptDiscr=mpBundleConfigLocalEndptDiscr, mpBundleStatusRcvShortSeq=mpBundleStatusRcvShortSeq, mpAllGroup=mpAllGroup, mpBundleStatusSmallPktMaxSize=mpBundleStatusSmallPktMaxSize, mpBundleStatusReasmFails=mpBundleStatusReasmFails, Unsigned32=Unsigned32, mpBundleConfigSmallPktMaxSize=mpBundleConfigSmallPktMaxSize, mpBundleStatusSingleFragsSent=mpBundleStatusSingleFragsSent, mpBundleStatusLocalEndptDiscr=mpBundleStatusLocalEndptDiscr, mpBundleStatusDropTooManyFrags=mpBundleStatusDropTooManyFrags, mpCompliance=mpCompliance, mpBundleStatusReasmReqds=mpBundleStatusReasmReqds, mpBundleStatusMediumPktMaxSize=mpBundleStatusMediumPktMaxSize, mpBundleStatusRcvdFragsBuffered=mpBundleStatusRcvdFragsBuffered, mpBundleStatusEntry=mpBundleStatusEntry, mpBundleStatusRcvdFragsDiscarded=mpBundleStatusRcvdFragsDiscarded, mpBundle=mpBundle, mpBundleStatusXmtShortSeq=mpBundleStatusXmtShortSeq, mpBundleStatusFragFails=mpBundleStatusFragFails, mpGroups=mpGroups, mpBundleConfigLocalMRRU=mpBundleConfigLocalMRRU, xediaPppMpConformance=xediaPppMpConformance, xediaPppMpMIB=xediaPppMpMIB)
