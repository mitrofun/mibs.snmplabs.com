#
# PySNMP MIB module HP-ICF-MACNOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-MACNOTIFY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanId, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ModuleIdentity, iso, Bits, ObjectIdentity, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Counter32", "Gauge32", "Integer32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
hpicfMacNotifyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66))
hpicfMacNotifyMIB.setRevisions(('2013-07-18 00:00', '2011-07-21 00:00', '2010-02-08 00:00', '2009-12-11 10:00',))
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setLastUpdated('201307180000Z')
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setOrganization('HP Networking')
hpicfMacCountNotifyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5))
hpicfMacNotifyClearObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4))
hpicfMacNotifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3))
hpicfMacNotifyStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2))
hpicfMacNotifyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1))
hpicfMacNotifyNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0))
hpicfMacNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyEnable.setStatus('current')
hpicfMacNotifyTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 2), Unsigned32().clone(30)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyTrapInterval.setStatus('current')
hpicfMacNotifyMoveEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyMoveEnable.setStatus('current')
hpicfMacNotifyLearnedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyLearnedPortConfig.setStatus('current')
hpicfMacNotifyRemovedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyRemovedPortConfig.setStatus('current')
hpicfMacNotifyAction = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("learned", 1), ("moved", 2), ("removed", 3), ("aged", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyAction.setStatus('current')
hpicfMacNotifyMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 7), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyMacAddress.setStatus('current')
hpicfMacNotifyFromPortId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 8), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyFromPortId.setStatus('current')
hpicfMacNotifyToPortId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyToPortId.setStatus('current')
hpicfMacNotifyVlanId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyVlanId.setStatus('current')
hpicfMacNotifyAgedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 11), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyAgedPortConfig.setStatus('current')
hpicfMacNotifyPortLearnedCountEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountEnable.setStatus('current')
hpicfMacNotifyPortLearnedCountConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfig.setStatus('current')
hpicfMacNotifyPortLearnedCountConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3), )
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigTable.setStatus('current')
hpicfMacNotifyPortLearnedCountConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1), ).setIndexNames((0, "HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortIndex"))
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigEntry.setStatus('current')
hpicfMacNotifyPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfMacNotifyPortIndex.setStatus('current')
hpicfMacNotifyPortLearnedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCount.setStatus('current')
hpicfMacNotifyLearnedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyLearnedCount.setStatus('current')
hpicfMacNotifyRemovedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyRemovedCount.setStatus('current')
hpicfMacNotifyMoveCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyMoveCount.setStatus('current')
hpicfMacNotifyCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyCount.setStatus('current')
hpicfMacNotifyAgedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyAgedCount.setStatus('current')
hpicfMacNotifyMacAddressTableChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
if mibBuilder.loadTexts: hpicfMacNotifyMacAddressTableChange.setStatus('current')
hpicfMacNotifyPortMacAddressCount = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"))
if mibBuilder.loadTexts: hpicfMacNotifyPortMacAddressCount.setStatus('current')
hpicfMacNotifyClearMacTableOnPorts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnPorts.setStatus('current')
hpicfMacNotifyClearMacTableOnVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnVlan.setStatus('current')
hpicfMacNotifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1))
hpicfMacNotifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2))
hpicfMacNotifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyGlobalConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyStatsGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyNotifications"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyCompliance = hpicfMacNotifyCompliance.setStatus('deprecated')
hpicfMacCountNotifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacCountNotifyConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacCountNotifyNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyCompliance = hpicfMacCountNotifyCompliance.setStatus('current')
hpicfMacNotifyCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 3)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyGlobalConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyConfigGroup2"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyStatsGroup2"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyNotifications"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyCompliance2 = hpicfMacNotifyCompliance2.setStatus('current')
hpicfMacNotifyGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyGlobalConfigGroup = hpicfMacNotifyGlobalConfigGroup.setStatus('current')
hpicfMacNotifyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyConfigGroup = hpicfMacNotifyConfigGroup.setStatus('deprecated')
hpicfMacNotifyStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 3)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyStatsGroup = hpicfMacNotifyStatsGroup.setStatus('deprecated')
hpicfMacNotifyNotifications = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 4)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddressTableChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyNotifications = hpicfMacNotifyNotifications.setStatus('current')
hpicfMacNotifyClearGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 5)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnPorts"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyClearGroup = hpicfMacNotifyClearGroup.setStatus('current')
hpicfMacCountNotifyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 6)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyConfigGroup = hpicfMacCountNotifyConfigGroup.setStatus('current')
hpicfMacCountNotifyNotifications = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 7)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortMacAddressCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyNotifications = hpicfMacCountNotifyNotifications.setStatus('current')
hpicfMacNotifyStatsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 8)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyStatsGroup2 = hpicfMacNotifyStatsGroup2.setStatus('current')
hpicfMacNotifyConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 9)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedPortConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyConfigGroup2 = hpicfMacNotifyConfigGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-MACNOTIFY-MIB", hpicfMacNotifyRemovedCount=hpicfMacNotifyRemovedCount, hpicfMacNotifyGlobalConfigGroup=hpicfMacNotifyGlobalConfigGroup, hpicfMacNotifyRemovedPortConfig=hpicfMacNotifyRemovedPortConfig, hpicfMacNotifyMacAddressTableChange=hpicfMacNotifyMacAddressTableChange, hpicfMacNotifyMoveEnable=hpicfMacNotifyMoveEnable, hpicfMacNotifyConfigObjects=hpicfMacNotifyConfigObjects, hpicfMacNotifyLearnedCount=hpicfMacNotifyLearnedCount, hpicfMacNotifyCompliances=hpicfMacNotifyCompliances, hpicfMacNotifyPortLearnedCountEnable=hpicfMacNotifyPortLearnedCountEnable, hpicfMacNotifyFromPortId=hpicfMacNotifyFromPortId, hpicfMacNotifyConfigGroup=hpicfMacNotifyConfigGroup, hpicfMacNotifyAgedCount=hpicfMacNotifyAgedCount, hpicfMacCountNotifyConfigObjects=hpicfMacCountNotifyConfigObjects, hpicfMacNotifyVlanId=hpicfMacNotifyVlanId, hpicfMacNotifyAgedPortConfig=hpicfMacNotifyAgedPortConfig, hpicfMacNotifyAction=hpicfMacNotifyAction, hpicfMacNotifyStats=hpicfMacNotifyStats, hpicfMacNotifyCompliance=hpicfMacNotifyCompliance, hpicfMacNotifyPortLearnedCountConfig=hpicfMacNotifyPortLearnedCountConfig, hpicfMacNotifyMIB=hpicfMacNotifyMIB, hpicfMacNotifyPortLearnedCountConfigEntry=hpicfMacNotifyPortLearnedCountConfigEntry, hpicfMacNotifyPortLearnedCount=hpicfMacNotifyPortLearnedCount, hpicfMacNotifyClearMacTableOnPorts=hpicfMacNotifyClearMacTableOnPorts, hpicfMacNotifyGroups=hpicfMacNotifyGroups, hpicfMacNotifyClearObjects=hpicfMacNotifyClearObjects, hpicfMacNotifyConformance=hpicfMacNotifyConformance, hpicfMacCountNotifyConfigGroup=hpicfMacCountNotifyConfigGroup, PYSNMP_MODULE_ID=hpicfMacNotifyMIB, hpicfMacNotifyLearnedPortConfig=hpicfMacNotifyLearnedPortConfig, hpicfMacNotifyStatsGroup=hpicfMacNotifyStatsGroup, hpicfMacNotifyCompliance2=hpicfMacNotifyCompliance2, hpicfMacNotifyTrapInterval=hpicfMacNotifyTrapInterval, hpicfMacNotifyNotificationObjects=hpicfMacNotifyNotificationObjects, hpicfMacNotifyCount=hpicfMacNotifyCount, hpicfMacNotifyClearGroup=hpicfMacNotifyClearGroup, hpicfMacNotifyConfigGroup2=hpicfMacNotifyConfigGroup2, hpicfMacNotifyMacAddress=hpicfMacNotifyMacAddress, hpicfMacNotifyPortLearnedCountConfigTable=hpicfMacNotifyPortLearnedCountConfigTable, hpicfMacNotifyClearMacTableOnVlan=hpicfMacNotifyClearMacTableOnVlan, hpicfMacNotifyEnable=hpicfMacNotifyEnable, hpicfMacNotifyNotifications=hpicfMacNotifyNotifications, hpicfMacNotifyPortIndex=hpicfMacNotifyPortIndex, hpicfMacNotifyStatsGroup2=hpicfMacNotifyStatsGroup2, hpicfMacNotifyMoveCount=hpicfMacNotifyMoveCount, hpicfMacCountNotifyCompliance=hpicfMacCountNotifyCompliance, hpicfMacNotifyToPortId=hpicfMacNotifyToPortId, hpicfMacNotifyPortMacAddressCount=hpicfMacNotifyPortMacAddressCount, hpicfMacCountNotifyNotifications=hpicfMacCountNotifyNotifications)
