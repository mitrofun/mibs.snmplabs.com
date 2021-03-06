#
# PySNMP MIB module HH3C-USERLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-USERLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, ObjectIdentity, iso, NotificationType, IpAddress, Counter64, Bits, MibIdentifier, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "ObjectIdentity", "iso", "NotificationType", "IpAddress", "Counter64", "Bits", "MibIdentifier", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cUserLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 18))
if mibBuilder.loadTexts: hh3cUserLogMIB.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hh3cUserLogMIB.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cUserlogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1))
hh3cUserlogNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1))
hh3cUserlogNatVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatVersion.setStatus('current')
hh3cUserlogNatSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatSyslog.setStatus('current')
hh3cUserlogNatSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatSourceIP.setStatus('current')
hh3cUserlogNatFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatFlowBegin.setStatus('current')
hh3cUserlogNatActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatActiveTime.setStatus('current')
hh3cUserlogNatSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6), )
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoTable.setStatus('current')
hh3cUserlogNatSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoEntry.setStatus('current')
hh3cUserlogNatCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatCfgSlotNumber.setStatus('current')
hh3cUserlogNatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatEnable.setStatus('current')
hh3cUserlogNatAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatAclNumber.setStatus('current')
hh3cUserlogNatHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatHostAddress.setStatus('current')
hh3cUserlogNatUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatUdpPort.setStatus('current')
hh3cUserlogNatSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7), )
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoTable.setStatus('current')
hh3cUserlogNatSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogNatRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoEntry.setStatus('current')
hh3cUserlogNatRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatRunSlotNumber.setStatus('current')
hh3cUserlogNatTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatTotalEntries.setStatus('current')
hh3cUserlogNatTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatTotalPackets.setStatus('current')
hh3cUserlogNatFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatFailedEntries.setStatus('current')
hh3cUserlogNatFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatFailedPackets.setStatus('current')
hh3cUserlogNatClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatClearRunStat.setStatus('current')
hh3cUserlogFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2))
hh3cUserlogFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowVersion.setStatus('current')
hh3cUserlogFlowSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowSyslog.setStatus('current')
hh3cUserlogFlowSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowSourceIP.setStatus('current')
hh3cUserlogFlowFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowFlowBegin.setStatus('current')
hh3cUserlogFlowActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowActiveTime.setStatus('current')
hh3cUserlogFlowSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6), )
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoTable.setStatus('current')
hh3cUserlogFlowSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoEntry.setStatus('current')
hh3cUserlogFlowCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowCfgSlotNumber.setStatus('current')
hh3cUserlogFlowEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowEnable.setStatus('current')
hh3cUserlogFlowAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowAclNumber.setStatus('current')
hh3cUserlogFlowHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowHostAddress.setStatus('current')
hh3cUserlogFlowUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowUdpPort.setStatus('current')
hh3cUserlogFlowSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7), )
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoTable.setStatus('current')
hh3cUserlogFlowSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoEntry.setStatus('current')
hh3cUserlogFlowRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowRunSlotNumber.setStatus('current')
hh3cUserlogFlowTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowTotalEntries.setStatus('current')
hh3cUserlogFlowTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowTotalPackets.setStatus('current')
hh3cUserlogFlowFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowFailedEntries.setStatus('current')
hh3cUserlogFlowFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowFailedPackets.setStatus('current')
hh3cUserlogFlowClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowClearRunStat.setStatus('current')
hh3cUserlogAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3))
hh3cUserlogAccessVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessVersion.setStatus('current')
hh3cUserlogAccessSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessSyslog.setStatus('current')
hh3cUserlogAccessSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessSourceIP.setStatus('current')
hh3cUserlogAccessSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4), )
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoTable.setStatus('current')
hh3cUserlogAccessSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoEntry.setStatus('current')
hh3cUserlogAccessCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessCfgSlotNumber.setStatus('current')
hh3cUserlogAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessEnable.setStatus('current')
hh3cUserlogAccessHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessHostAddress.setStatus('current')
hh3cUserlogAccessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessUdpPort.setStatus('current')
hh3cUserlogAccessSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5), )
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoTable.setStatus('current')
hh3cUserlogAccessSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoEntry.setStatus('current')
hh3cUserlogAccessRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessRunSlotNumber.setStatus('current')
hh3cUserlogAccessTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessTotalEntries.setStatus('current')
hh3cUserlogAccessTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessTotalPackets.setStatus('current')
hh3cUserlogAccessFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessFailedEntries.setStatus('current')
hh3cUserlogAccessFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessFailedPackets.setStatus('current')
hh3cUserlogAccessClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessClearRunStat.setStatus('current')
hh3cUserlogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 2))
hh3cUserlogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3))
hh3cUserlogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1))
hh3cUserlogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1, 1)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogCompliance = hh3cUserlogCompliance.setStatus('current')
hh3cUserlogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2))
hh3cUserlogMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 1)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogMandatoryGroup = hh3cUserlogMandatoryGroup.setStatus('current')
hh3cUserlogConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 2)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFlowBegin"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatActiveTime"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatAclNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFlowBegin"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowActiveTime"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowAclNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogConfigGroup = hh3cUserlogConfigGroup.setStatus('current')
hh3cUserlogInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 3)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogInfoGroup = hh3cUserlogInfoGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-USERLOG-MIB", hh3cUserlogNatSlotCfgInfoTable=hh3cUserlogNatSlotCfgInfoTable, hh3cUserlogAccessObjects=hh3cUserlogAccessObjects, hh3cUserlogConformance=hh3cUserlogConformance, hh3cUserlogNatFlowBegin=hh3cUserlogNatFlowBegin, hh3cUserlogAccessRunSlotNumber=hh3cUserlogAccessRunSlotNumber, hh3cUserlogCompliance=hh3cUserlogCompliance, hh3cUserlogFlowUdpPort=hh3cUserlogFlowUdpPort, hh3cUserlogNatRunSlotNumber=hh3cUserlogNatRunSlotNumber, hh3cUserlogFlowTotalEntries=hh3cUserlogFlowTotalEntries, hh3cUserlogNatClearRunStat=hh3cUserlogNatClearRunStat, hh3cUserlogAccessEnable=hh3cUserlogAccessEnable, hh3cUserlogNatAclNumber=hh3cUserlogNatAclNumber, hh3cUserlogFlowSyslog=hh3cUserlogFlowSyslog, hh3cUserlogNatUdpPort=hh3cUserlogNatUdpPort, hh3cUserlogNatActiveTime=hh3cUserlogNatActiveTime, hh3cUserlogConfigGroup=hh3cUserlogConfigGroup, hh3cUserLogMIB=hh3cUserLogMIB, hh3cUserlogNatSlotCfgInfoEntry=hh3cUserlogNatSlotCfgInfoEntry, hh3cUserlogFlowFailedPackets=hh3cUserlogFlowFailedPackets, hh3cUserlogGroups=hh3cUserlogGroups, hh3cUserlogNatHostAddress=hh3cUserlogNatHostAddress, hh3cUserlogFlowActiveTime=hh3cUserlogFlowActiveTime, hh3cUserlogFlowFlowBegin=hh3cUserlogFlowFlowBegin, hh3cUserlogAccessHostAddress=hh3cUserlogAccessHostAddress, hh3cUserlogAccessSlotRunInfoTable=hh3cUserlogAccessSlotRunInfoTable, hh3cUserlogNatCfgSlotNumber=hh3cUserlogNatCfgSlotNumber, hh3cUserlogFlowSlotCfgInfoEntry=hh3cUserlogFlowSlotCfgInfoEntry, hh3cUserlogFlowClearRunStat=hh3cUserlogFlowClearRunStat, hh3cUserlogAccessSlotRunInfoEntry=hh3cUserlogAccessSlotRunInfoEntry, hh3cUserlogMandatoryGroup=hh3cUserlogMandatoryGroup, hh3cUserlogObjects=hh3cUserlogObjects, hh3cUserlogAccessSyslog=hh3cUserlogAccessSyslog, hh3cUserlogNatSlotRunInfoEntry=hh3cUserlogNatSlotRunInfoEntry, hh3cUserlogNatSourceIP=hh3cUserlogNatSourceIP, hh3cUserlogAccessVersion=hh3cUserlogAccessVersion, hh3cUserlogNatSyslog=hh3cUserlogNatSyslog, hh3cUserlogFlowSlotRunInfoTable=hh3cUserlogFlowSlotRunInfoTable, hh3cUserlogFlowSlotCfgInfoTable=hh3cUserlogFlowSlotCfgInfoTable, hh3cUserlogNatTotalPackets=hh3cUserlogNatTotalPackets, hh3cUserlogAccessSourceIP=hh3cUserlogAccessSourceIP, PYSNMP_MODULE_ID=hh3cUserLogMIB, hh3cUserlogAccessSlotCfgInfoTable=hh3cUserlogAccessSlotCfgInfoTable, hh3cUserlogNotifications=hh3cUserlogNotifications, hh3cUserlogAccessTotalEntries=hh3cUserlogAccessTotalEntries, hh3cUserlogNatFailedEntries=hh3cUserlogNatFailedEntries, hh3cUserlogNatFailedPackets=hh3cUserlogNatFailedPackets, hh3cUserlogNatTotalEntries=hh3cUserlogNatTotalEntries, hh3cUserlogFlowHostAddress=hh3cUserlogFlowHostAddress, hh3cUserlogNatEnable=hh3cUserlogNatEnable, hh3cUserlogAccessFailedPackets=hh3cUserlogAccessFailedPackets, hh3cUserlogCompliances=hh3cUserlogCompliances, hh3cUserlogFlowAclNumber=hh3cUserlogFlowAclNumber, hh3cUserlogFlowTotalPackets=hh3cUserlogFlowTotalPackets, hh3cUserlogAccessCfgSlotNumber=hh3cUserlogAccessCfgSlotNumber, hh3cUserlogFlowCfgSlotNumber=hh3cUserlogFlowCfgSlotNumber, hh3cUserlogAccessUdpPort=hh3cUserlogAccessUdpPort, hh3cUserlogInfoGroup=hh3cUserlogInfoGroup, hh3cUserlogNatObjects=hh3cUserlogNatObjects, hh3cUserlogFlowSourceIP=hh3cUserlogFlowSourceIP, hh3cUserlogFlowEnable=hh3cUserlogFlowEnable, hh3cUserlogFlowVersion=hh3cUserlogFlowVersion, hh3cUserlogFlowSlotRunInfoEntry=hh3cUserlogFlowSlotRunInfoEntry, hh3cUserlogNatVersion=hh3cUserlogNatVersion, hh3cUserlogAccessTotalPackets=hh3cUserlogAccessTotalPackets, hh3cUserlogAccessFailedEntries=hh3cUserlogAccessFailedEntries, hh3cUserlogFlowFailedEntries=hh3cUserlogFlowFailedEntries, hh3cUserlogAccessSlotCfgInfoEntry=hh3cUserlogAccessSlotCfgInfoEntry, hh3cUserlogNatSlotRunInfoTable=hh3cUserlogNatSlotRunInfoTable, hh3cUserlogAccessClearRunStat=hh3cUserlogAccessClearRunStat, hh3cUserlogFlowRunSlotNumber=hh3cUserlogFlowRunSlotNumber, hh3cUserlogFlowObjects=hh3cUserlogFlowObjects)
