#
# PySNMP MIB module WWP-LEOS-IP-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-IP-INTERFACE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Integer32, NotificationType, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention, MacAddress, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "TruthValue", "RowStatus")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosIpInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24))
wwpLeosIpInterfaceMIB.setRevisions(('2008-05-14 00:00', '2003-05-02 00:00', '2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpLeosIpInterfaceMIB.setLastUpdated('200805140000Z')
if mibBuilder.loadTexts: wwpLeosIpInterfaceMIB.setOrganization('Ciena, Inc')
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpLeosIpInterfaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1))
wwpLeosIpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1))
wwpLeosIpAclGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2))
wwpLeosIpAclRules = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3))
wwpLeosIpInterfaceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2))
wwpLeosIpInterfaceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0))
wwpLeosIpInterfaceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3))
wwpLeosIpInterfaceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3, 1))
wwpLeosIpInterfaceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3, 2))
wwpLeosIpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1), )
if mibBuilder.loadTexts: wwpLeosIpInterfaceTable.setStatus('current')
wwpLeosIpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1), ).setIndexNames((0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceIndex"))
if mibBuilder.loadTexts: wwpLeosIpInterfaceEntry.setStatus('current')
wwpLeosIpInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpInterfaceIndex.setStatus('current')
wwpLeosIpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpInterfaceName.setStatus('current')
wwpLeosIpInterfaceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceIpAddr.setStatus('current')
wwpLeosIpInterfaceSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceSubnet.setStatus('current')
wwpLeosIpInterfaceIfIndexXref = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpInterfaceIfIndexXref.setStatus('current')
wwpLeosIpExtInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2), )
if mibBuilder.loadTexts: wwpLeosIpExtInterfaceTable.setStatus('current')
wwpLeosIpExtInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1), )
wwpLeosIpInterfaceEntry.registerAugmentions(("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpExtInterfaceEntry"))
wwpLeosIpExtInterfaceEntry.setIndexNames(*wwpLeosIpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: wwpLeosIpExtInterfaceEntry.setStatus('current')
wwpLeosIpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceEnable.setStatus('current')
wwpLeosIpInterfaceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceVlanId.setStatus('current')
wwpLeosIpInterfaceMgmtPktPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceMgmtPktPriority.setStatus('current')
wwpLeosIpInterfaceAddrNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpInterfaceAddrNotifEnabled.setStatus('current')
wwpLeosIpInterfaceAddrChgNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0, 1)).setObjects(("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceName"), ("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceIpAddr"), ("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceSubnet"))
if mibBuilder.loadTexts: wwpLeosIpInterfaceAddrChgNotification.setStatus('current')
wwpLeosIpDataInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4), )
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceTable.setStatus('current')
wwpLeosIpDataInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1), ).setIndexNames((0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpDataInterfaceIndex"))
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceEntry.setStatus('current')
wwpLeosIpDataInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceIndex.setStatus('current')
wwpLeosIpDataInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceName.setStatus('current')
wwpLeosIpDataInterfaceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceIpAddr.setStatus('current')
wwpLeosIpDataInterfaceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceMask.setStatus('current')
wwpLeosIpDataInterfaceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 5), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceVlanId.setStatus('current')
wwpLeosIpDataInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("broadcast", 1), ("pointToPoint", 2), ("loopBack", 3))).clone('broadcast')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceType.setStatus('current')
wwpLeosIpDataInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceIfIndex.setStatus('current')
wwpLeosIpDataInterfaceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceMac.setStatus('current')
wwpLeosIpDataInterfaceIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 9), Integer32().clone(1500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceIfMtu.setStatus('current')
wwpLeosIpDataInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpDataInterfaceRowStatus.setStatus('current')
wwpLeosIpInterfaceOperationalGateway = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpInterfaceOperationalGateway.setStatus('current')
wwpLeosIpInterfaceOperationalGatewayChgNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0, 2)).setObjects(("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceOperationalGateway"))
if mibBuilder.loadTexts: wwpLeosIpInterfaceOperationalGatewayChgNotification.setStatus('current')
wwpLeosIpAclState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpAclState.setStatus('current')
wwpLeosIpAclCacheHit = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclCacheHit.setStatus('current')
wwpLeosIpAclNoHit = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclNoHit.setStatus('current')
wwpLeosIpAclBadPort = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclBadPort.setStatus('current')
wwpLeosIpAclClearStats = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosIpAclClearStats.setStatus('current')
wwpLeosIpAclBadDscp = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclBadDscp.setStatus('current')
wwpLeosIpAclOperState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclOperState.setStatus('current')
wwpLeosIpAclInUseEntries = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclInUseEntries.setStatus('current')
wwpLeosIpAclMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclMaxEntries.setStatus('current')
wwpLeosIpAclTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1), )
if mibBuilder.loadTexts: wwpLeosIpAclTable.setStatus('current')
wwpLeosIpAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1), ).setIndexNames((0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpAclEntryIpAddr"), (0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpAclEntryIpMask"))
if mibBuilder.loadTexts: wwpLeosIpAclEntry.setStatus('current')
wwpLeosIpAclEntryIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryIpAddr.setStatus('current')
wwpLeosIpAclEntryIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryIpMask.setStatus('current')
wwpLeosIpAclEntryPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryPortMask.setStatus('deprecated')
wwpLeosIpAclEntryHits = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclEntryHits.setStatus('current')
wwpLeosIpAclEntryBadPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclEntryBadPort.setStatus('current')
wwpLeosIpAclEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryStatus.setStatus('current')
wwpLeosIpAclEntryDscpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryDscpMask.setStatus('current')
wwpLeosIpAclEntryBadDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosIpAclEntryBadDscp.setStatus('current')
wwpLeosIpAclEntryPortBitMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosIpAclEntryPortBitMask.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-IP-INTERFACE-MIB", wwpLeosIpDataInterfaceVlanId=wwpLeosIpDataInterfaceVlanId, wwpLeosIpDataInterfaceType=wwpLeosIpDataInterfaceType, wwpLeosIpDataInterfaceMask=wwpLeosIpDataInterfaceMask, wwpLeosIpDataInterfaceIndex=wwpLeosIpDataInterfaceIndex, wwpLeosIpAclMaxEntries=wwpLeosIpAclMaxEntries, wwpLeosIpInterfaceOperationalGatewayChgNotification=wwpLeosIpInterfaceOperationalGatewayChgNotification, wwpLeosIpDataInterfaceName=wwpLeosIpDataInterfaceName, wwpLeosIpAclRules=wwpLeosIpAclRules, wwpLeosIpInterfaceMIBNotificationPrefix=wwpLeosIpInterfaceMIBNotificationPrefix, wwpLeosIpAclEntry=wwpLeosIpAclEntry, wwpLeosIpDataInterfaceIfMtu=wwpLeosIpDataInterfaceIfMtu, wwpLeosIpInterfaceMgmtPktPriority=wwpLeosIpInterfaceMgmtPktPriority, wwpLeosIpAclCacheHit=wwpLeosIpAclCacheHit, wwpLeosIpDataInterfaceIpAddr=wwpLeosIpDataInterfaceIpAddr, wwpLeosIpInterfaceEnable=wwpLeosIpInterfaceEnable, wwpLeosIpInterfaceMIBConformance=wwpLeosIpInterfaceMIBConformance, wwpLeosIpInterfaceMIBGroups=wwpLeosIpInterfaceMIBGroups, wwpLeosIpInterfaceName=wwpLeosIpInterfaceName, wwpLeosIpInterfaceAddrNotifEnabled=wwpLeosIpInterfaceAddrNotifEnabled, wwpLeosIpAclEntryIpAddr=wwpLeosIpAclEntryIpAddr, wwpLeosIpDataInterfaceEntry=wwpLeosIpDataInterfaceEntry, wwpLeosIpInterfaceOperationalGateway=wwpLeosIpInterfaceOperationalGateway, wwpLeosIpInterface=wwpLeosIpInterface, wwpLeosIpInterfaceTable=wwpLeosIpInterfaceTable, wwpLeosIpInterfaceMIB=wwpLeosIpInterfaceMIB, PYSNMP_MODULE_ID=wwpLeosIpInterfaceMIB, VlanId=VlanId, wwpLeosIpInterfaceMIBNotifications=wwpLeosIpInterfaceMIBNotifications, wwpLeosIpInterfaceSubnet=wwpLeosIpInterfaceSubnet, wwpLeosIpInterfaceAddrChgNotification=wwpLeosIpInterfaceAddrChgNotification, wwpLeosIpAclTable=wwpLeosIpAclTable, wwpLeosIpAclEntryIpMask=wwpLeosIpAclEntryIpMask, wwpLeosIpAclClearStats=wwpLeosIpAclClearStats, wwpLeosIpInterfaceEntry=wwpLeosIpInterfaceEntry, wwpLeosIpAclGlobal=wwpLeosIpAclGlobal, wwpLeosIpExtInterfaceEntry=wwpLeosIpExtInterfaceEntry, wwpLeosIpInterfaceVlanId=wwpLeosIpInterfaceVlanId, wwpLeosIpDataInterfaceMac=wwpLeosIpDataInterfaceMac, wwpLeosIpDataInterfaceTable=wwpLeosIpDataInterfaceTable, wwpLeosIpDataInterfaceIfIndex=wwpLeosIpDataInterfaceIfIndex, wwpLeosIpAclBadDscp=wwpLeosIpAclBadDscp, wwpLeosIpAclEntryDscpMask=wwpLeosIpAclEntryDscpMask, wwpLeosIpAclBadPort=wwpLeosIpAclBadPort, wwpLeosIpInterfaceIfIndexXref=wwpLeosIpInterfaceIfIndexXref, wwpLeosIpAclEntryHits=wwpLeosIpAclEntryHits, wwpLeosIpAclOperState=wwpLeosIpAclOperState, wwpLeosIpAclEntryPortMask=wwpLeosIpAclEntryPortMask, wwpLeosIpInterfaceMIBObjects=wwpLeosIpInterfaceMIBObjects, wwpLeosIpAclEntryBadDscp=wwpLeosIpAclEntryBadDscp, wwpLeosIpAclEntryPortBitMask=wwpLeosIpAclEntryPortBitMask, wwpLeosIpAclEntryStatus=wwpLeosIpAclEntryStatus, wwpLeosIpAclState=wwpLeosIpAclState, wwpLeosIpDataInterfaceRowStatus=wwpLeosIpDataInterfaceRowStatus, wwpLeosIpInterfaceIpAddr=wwpLeosIpInterfaceIpAddr, wwpLeosIpAclNoHit=wwpLeosIpAclNoHit, wwpLeosIpAclInUseEntries=wwpLeosIpAclInUseEntries, wwpLeosIpAclEntryBadPort=wwpLeosIpAclEntryBadPort, wwpLeosIpInterfaceMIBCompliances=wwpLeosIpInterfaceMIBCompliances, wwpLeosIpExtInterfaceTable=wwpLeosIpExtInterfaceTable, wwpLeosIpInterfaceIndex=wwpLeosIpInterfaceIndex)
