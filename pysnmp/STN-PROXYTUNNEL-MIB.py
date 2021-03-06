#
# PySNMP MIB module STN-PROXYTUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-PROXYTUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Unsigned32, iso, TimeTicks, IpAddress, Integer32, NotificationType, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "IpAddress", "Integer32", "NotificationType", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnPMProxyTunnel, = mibBuilder.importSymbols("STN-POLICY-MIB", "stnPMProxyTunnel")
stnProxyTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1))
if mibBuilder.loadTexts: stnProxyTunnel.setLastUpdated('0001160000Z')
if mibBuilder.loadTexts: stnProxyTunnel.setOrganization('Spring Tide Networks')
stnProxyTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1))
stnProxyTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1), )
if mibBuilder.loadTexts: stnProxyTunnelTable.setStatus('current')
stnProxyTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1), ).setIndexNames((0, "STN-PROXYTUNNEL-MIB", "stnProxyTunnelSerialNumber"), (0, "STN-PROXYTUNNEL-MIB", "stnProxyTunnelRouterInstance"))
if mibBuilder.loadTexts: stnProxyTunnelEntry.setStatus('current')
stnProxyTunnelSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelSerialNumber.setStatus('current')
stnProxyTunnelRouterInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelRouterInstance.setStatus('current')
stnProxyTunnelConnIdleTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelConnIdleTimeOut.setStatus('current')
stnProxyTunnelPolicyInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelPolicyInstance.setStatus('current')
stnProxyTunnelPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelPolicyName.setStatus('current')
stnProxyTunnelEncapsType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stnProxyTunEncapsIpIp", 1), ("stnProxyTunEncapsIpGre", 2), ("stnProxyTunEncapsIpsec", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelEncapsType.setStatus('current')
stnProxyTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelState.setStatus('current')
stnProxyTunnelL3IfaceTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 8), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelL3IfaceTx.setStatus('current')
stnProxyTunnelLocalTunnelAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelLocalTunnelAddr.setStatus('current')
stnProxyTunnelRemoteTunnelAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelRemoteTunnelAddr.setStatus('current')
stnProxyTunnelInESPSPIs = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelInESPSPIs.setStatus('current')
stnProxyTunnelOutESPSPIs = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelOutESPSPIs.setStatus('current')
stnProxyTunnelInAHSPIs = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelInAHSPIs.setStatus('current')
stnProxyTunnelOutAHSPIs = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelOutAHSPIs.setStatus('current')
stnProxyTunnelEncapsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelEncapsIndex.setStatus('current')
stnProxyTunnelInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelInPkts.setStatus('current')
stnProxyTunnelInErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelInErrPkts.setStatus('current')
stnProxyTunnelOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelOutPkts.setStatus('current')
stnProxyTunnelOutErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnProxyTunnelOutErrPkts.setStatus('current')
mibBuilder.exportSymbols("STN-PROXYTUNNEL-MIB", stnProxyTunnelInAHSPIs=stnProxyTunnelInAHSPIs, stnProxyTunnelOutAHSPIs=stnProxyTunnelOutAHSPIs, stnProxyTunnelInESPSPIs=stnProxyTunnelInESPSPIs, stnProxyTunnelState=stnProxyTunnelState, stnProxyTunnelRemoteTunnelAddr=stnProxyTunnelRemoteTunnelAddr, stnProxyTunnelOutErrPkts=stnProxyTunnelOutErrPkts, stnProxyTunnelLocalTunnelAddr=stnProxyTunnelLocalTunnelAddr, stnProxyTunnelConnIdleTimeOut=stnProxyTunnelConnIdleTimeOut, stnProxyTunnelPolicyName=stnProxyTunnelPolicyName, stnProxyTunnelEntry=stnProxyTunnelEntry, stnProxyTunnel=stnProxyTunnel, stnProxyTunnelTable=stnProxyTunnelTable, stnProxyTunnelEncapsType=stnProxyTunnelEncapsType, stnProxyTunnelRouterInstance=stnProxyTunnelRouterInstance, stnProxyTunnelInErrPkts=stnProxyTunnelInErrPkts, PYSNMP_MODULE_ID=stnProxyTunnel, stnProxyTunnelEncapsIndex=stnProxyTunnelEncapsIndex, stnProxyTunnelSerialNumber=stnProxyTunnelSerialNumber, stnProxyTunnelOutPkts=stnProxyTunnelOutPkts, stnProxyTunnelInPkts=stnProxyTunnelInPkts, stnProxyTunnelL3IfaceTx=stnProxyTunnelL3IfaceTx, stnProxyTunnelPolicyInstance=stnProxyTunnelPolicyInstance, stnProxyTunnelObjects=stnProxyTunnelObjects, stnProxyTunnelOutESPSPIs=stnProxyTunnelOutESPSPIs)
