#
# PySNMP MIB module DVMRP-STD-MIB-JUNI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DVMRP-STD-MIB-JUNI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
juniDvmrpExperiment, = mibBuilder.importSymbols("Juniper-Experiment", "juniDvmrpExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Integer32, ObjectIdentity, Counter64, Bits, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ObjectIdentity", "Counter64", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Gauge32", "Unsigned32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
junidDvmrpStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1))
junidDvmrpStdMIB.setRevisions(('1999-10-19 12:00',))
if mibBuilder.loadTexts: junidDvmrpStdMIB.setLastUpdated('9910191200Z')
if mibBuilder.loadTexts: junidDvmrpStdMIB.setOrganization('IETF IDMR Working Group.')
junidDvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1))
junidDvmrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1))
junidDvmrpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1))
junidDvmrpVersionString = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpVersionString.setStatus('current')
junidDvmrpGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpGenerationId.setStatus('current')
junidDvmrpNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNumRoutes.setStatus('current')
junidDvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpReachableRoutes.setStatus('current')
junidDvmrpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: junidDvmrpInterfaceTable.setStatus('current')
junidDvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: junidDvmrpInterfaceEntry.setStatus('current')
junidDvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: junidDvmrpInterfaceIfIndex.setStatus('current')
junidDvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: junidDvmrpInterfaceLocalAddress.setStatus('current')
junidDvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: junidDvmrpInterfaceMetric.setStatus('current')
junidDvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: junidDvmrpInterfaceStatus.setStatus('current')
junidDvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpInterfaceRcvBadPkts.setStatus('current')
junidDvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpInterfaceRcvBadRoutes.setStatus('current')
junidDvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpInterfaceSentRoutes.setStatus('current')
junidDvmrpInterfaceInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: junidDvmrpInterfaceInterfaceKey.setStatus('current')
junidDvmrpInterfaceInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: junidDvmrpInterfaceInterfaceKeyVersion.setStatus('current')
junidDvmrpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3), )
if mibBuilder.loadTexts: junidDvmrpNeighborTable.setStatus('current')
junidDvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborIfIndex"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborAddress"))
if mibBuilder.loadTexts: junidDvmrpNeighborEntry.setStatus('current')
junidDvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: junidDvmrpNeighborIfIndex.setStatus('current')
junidDvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: junidDvmrpNeighborAddress.setStatus('current')
junidDvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborUpTime.setStatus('current')
junidDvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborExpiryTime.setStatus('current')
junidDvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborGenerationId.setStatus('current')
junidDvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborMajorVersion.setStatus('current')
junidDvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborMinorVersion.setStatus('current')
junidDvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborCapabilities.setStatus('current')
junidDvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborRcvRoutes.setStatus('current')
junidDvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborRcvBadPkts.setStatus('current')
junidDvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborRcvBadRoutes.setStatus('current')
junidDvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpNeighborState.setStatus('current')
junidDvmrpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4), )
if mibBuilder.loadTexts: junidDvmrpRouteTable.setStatus('current')
junidDvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteSource"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteSourceMask"))
if mibBuilder.loadTexts: junidDvmrpRouteEntry.setStatus('current')
junidDvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: junidDvmrpRouteSource.setStatus('current')
junidDvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: junidDvmrpRouteSourceMask.setStatus('current')
junidDvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteUpstreamNeighbor.setStatus('current')
junidDvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteIfIndex.setStatus('current')
junidDvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteMetric.setStatus('current')
junidDvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteExpiryTime.setStatus('current')
junidDvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteUpTime.setStatus('current')
junidDvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5), )
if mibBuilder.loadTexts: junidDvmrpRouteNextHopTable.setStatus('current')
junidDvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopSource"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopSourceMask"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: junidDvmrpRouteNextHopEntry.setStatus('current')
junidDvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: junidDvmrpRouteNextHopSource.setStatus('current')
junidDvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: junidDvmrpRouteNextHopSourceMask.setStatus('current')
junidDvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: junidDvmrpRouteNextHopIfIndex.setStatus('current')
junidDvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpRouteNextHopType.setStatus('current')
junidDvmrpPruneTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6), )
if mibBuilder.loadTexts: junidDvmrpPruneTable.setStatus('current')
junidDvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneGroup"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneSource"), (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneSourceMask"))
if mibBuilder.loadTexts: junidDvmrpPruneEntry.setStatus('current')
junidDvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: junidDvmrpPruneGroup.setStatus('current')
junidDvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: junidDvmrpPruneSource.setStatus('current')
junidDvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: junidDvmrpPruneSourceMask.setStatus('current')
junidDvmrpPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: junidDvmrpPruneExpiryTime.setStatus('current')
junidDvmrpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0))
junidDvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 1)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborState"))
if mibBuilder.loadTexts: junidDvmrpNeighborLoss.setStatus('current')
junidDvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 2)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborCapabilities"))
if mibBuilder.loadTexts: junidDvmrpNeighborNotPruning.setStatus('current')
junidDvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2))
junidDvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1))
junidDvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2))
junidDvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1, 1)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpGeneralGroup"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceGroup"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborGroup"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRoutingGroup"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpTreeGroup"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpMIBCompliance = junidDvmrpMIBCompliance.setStatus('current')
junidDvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 2)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpVersionString"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpGenerationId"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNumRoutes"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpGeneralGroup = junidDvmrpGeneralGroup.setStatus('current')
junidDvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 3)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceMetric"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceStatus"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceRcvBadPkts"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceRcvBadRoutes"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpInterfaceGroup = junidDvmrpInterfaceGroup.setStatus('current')
junidDvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 4)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborUpTime"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborExpiryTime"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborGenerationId"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborMajorVersion"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborMinorVersion"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborCapabilities"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvRoutes"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvBadPkts"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvBadRoutes"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpNeighborGroup = junidDvmrpNeighborGroup.setStatus('current')
junidDvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 5)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteUpstreamNeighbor"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteIfIndex"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteMetric"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteExpiryTime"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteUpTime"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpRoutingGroup = junidDvmrpRoutingGroup.setStatus('current')
junidDvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 6)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceInterfaceKey"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpSecurityGroup = junidDvmrpSecurityGroup.setStatus('current')
junidDvmrpTreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 7)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpTreeGroup = junidDvmrpTreeGroup.setStatus('current')
junidDvmrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 8)).setObjects(("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborLoss"), ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    junidDvmrpNotificationGroup = junidDvmrpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DVMRP-STD-MIB-JUNI", junidDvmrpInterfaceIfIndex=junidDvmrpInterfaceIfIndex, junidDvmrpRouteNextHopTable=junidDvmrpRouteNextHopTable, junidDvmrpRouteNextHopSourceMask=junidDvmrpRouteNextHopSourceMask, junidDvmrpPruneTable=junidDvmrpPruneTable, junidDvmrpTreeGroup=junidDvmrpTreeGroup, junidDvmrpInterfaceLocalAddress=junidDvmrpInterfaceLocalAddress, junidDvmrpInterfaceInterfaceKeyVersion=junidDvmrpInterfaceInterfaceKeyVersion, junidDvmrpReachableRoutes=junidDvmrpReachableRoutes, junidDvmrpNeighborState=junidDvmrpNeighborState, junidDvmrpNeighborLoss=junidDvmrpNeighborLoss, junidDvmrpStdMIB=junidDvmrpStdMIB, junidDvmrpNeighborTable=junidDvmrpNeighborTable, junidDvmrpGeneralGroup=junidDvmrpGeneralGroup, junidDvmrpSecurityGroup=junidDvmrpSecurityGroup, junidDvmrpMIBCompliance=junidDvmrpMIBCompliance, junidDvmrpScalar=junidDvmrpScalar, junidDvmrpRouteExpiryTime=junidDvmrpRouteExpiryTime, junidDvmrpNeighborMajorVersion=junidDvmrpNeighborMajorVersion, junidDvmrpPruneGroup=junidDvmrpPruneGroup, junidDvmrpRouteNextHopEntry=junidDvmrpRouteNextHopEntry, junidDvmrpNotificationGroup=junidDvmrpNotificationGroup, junidDvmrpInterfaceRcvBadRoutes=junidDvmrpInterfaceRcvBadRoutes, junidDvmrpNeighborRcvRoutes=junidDvmrpNeighborRcvRoutes, junidDvmrpNeighborGroup=junidDvmrpNeighborGroup, junidDvmrpInterfaceSentRoutes=junidDvmrpInterfaceSentRoutes, PYSNMP_MODULE_ID=junidDvmrpStdMIB, junidDvmrpRouteTable=junidDvmrpRouteTable, junidDvmrpNeighborIfIndex=junidDvmrpNeighborIfIndex, junidDvmrpRoutingGroup=junidDvmrpRoutingGroup, junidDvmrpRouteIfIndex=junidDvmrpRouteIfIndex, junidDvmrpRouteEntry=junidDvmrpRouteEntry, junidDvmrpNeighborExpiryTime=junidDvmrpNeighborExpiryTime, junidDvmrpMIBObjects=junidDvmrpMIBObjects, junidDvmrpPruneSourceMask=junidDvmrpPruneSourceMask, junidDvmrpInterfaceEntry=junidDvmrpInterfaceEntry, junidDvmrpRouteUpstreamNeighbor=junidDvmrpRouteUpstreamNeighbor, junidDvmrpInterfaceInterfaceKey=junidDvmrpInterfaceInterfaceKey, junidDvmrpPruneSource=junidDvmrpPruneSource, junidDvmrpNumRoutes=junidDvmrpNumRoutes, junidDvmrpNeighborAddress=junidDvmrpNeighborAddress, junidDvmrpMIBGroups=junidDvmrpMIBGroups, junidDvmrpNeighborEntry=junidDvmrpNeighborEntry, junidDvmrpNeighborGenerationId=junidDvmrpNeighborGenerationId, junidDvmrpGenerationId=junidDvmrpGenerationId, junidDvmrpInterfaceGroup=junidDvmrpInterfaceGroup, junidDvmrpNeighborUpTime=junidDvmrpNeighborUpTime, junidDvmrpRouteSource=junidDvmrpRouteSource, junidDvmrpRouteMetric=junidDvmrpRouteMetric, junidDvmrpPruneEntry=junidDvmrpPruneEntry, junidDvmrpNeighborCapabilities=junidDvmrpNeighborCapabilities, junidDvmrpTraps=junidDvmrpTraps, junidDvmrpMIBConformance=junidDvmrpMIBConformance, junidDvmrpPruneExpiryTime=junidDvmrpPruneExpiryTime, junidDvmrpInterfaceTable=junidDvmrpInterfaceTable, junidDvmrpNeighborNotPruning=junidDvmrpNeighborNotPruning, junidDvmrpRouteSourceMask=junidDvmrpRouteSourceMask, junidDvmrpRouteUpTime=junidDvmrpRouteUpTime, junidDvmrpMIBCompliances=junidDvmrpMIBCompliances, junidDvmrpVersionString=junidDvmrpVersionString, junidDvmrpNeighborRcvBadPkts=junidDvmrpNeighborRcvBadPkts, junidDvmrpNeighborRcvBadRoutes=junidDvmrpNeighborRcvBadRoutes, junidDvmrpRouteNextHopIfIndex=junidDvmrpRouteNextHopIfIndex, junidDvmrp=junidDvmrp, junidDvmrpInterfaceMetric=junidDvmrpInterfaceMetric, junidDvmrpRouteNextHopType=junidDvmrpRouteNextHopType, junidDvmrpRouteNextHopSource=junidDvmrpRouteNextHopSource, junidDvmrpInterfaceRcvBadPkts=junidDvmrpInterfaceRcvBadPkts, junidDvmrpNeighborMinorVersion=junidDvmrpNeighborMinorVersion, junidDvmrpInterfaceStatus=junidDvmrpInterfaceStatus)
