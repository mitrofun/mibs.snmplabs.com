#
# PySNMP MIB module MITEL-IPLOGICAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPLOGICAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, Gauge32, enterprises, NotificationType, IpAddress, Counter32, MibIdentifier, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "Gauge32", "enterprises", "NotificationType", "IpAddress", "Counter32", "MibIdentifier", "Bits", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
mitelIpGrpLogicalGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5))
mitelIpGrpLogicalGroup.setRevisions(('2003-03-24 09:13', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setLastUpdated('200303240913Z')
if mibBuilder.loadTexts: mitelIpGrpLogicalGroup.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelIpLogGrpLogicalTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1), )
if mibBuilder.loadTexts: mitelIpLogGrpLogicalTable.setStatus('current')
mitelIpLogGrpLogicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIpLogGrpLogicalEntry.setStatus('current')
mitelIpLogAdvertisementAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogAdvertisementAddress.setStatus('current')
mitelIpLogMaxAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 1800)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogMaxAdvertisementInterval.setStatus('current')
mitelIpLogMinAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1800)).clone(450)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogMinAdvertisementInterval.setStatus('current')
mitelIpLogAdvertisementLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 9000)).clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogAdvertisementLifetime.setStatus('current')
mitelIpLogPerformRouterDiscovery = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogPerformRouterDiscovery.setStatus('current')
mitelIpLogSolicitationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpLogSolicitationAddress.setStatus('current')
mitelIpLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIpLogStatus.setStatus('current')
mibBuilder.exportSymbols("MITEL-IPLOGICAL-MIB", mitelIpLogGrpLogicalEntry=mitelIpLogGrpLogicalEntry, mitelIpLogMaxAdvertisementInterval=mitelIpLogMaxAdvertisementInterval, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup, mitelPropIpNetworking=mitelPropIpNetworking, PYSNMP_MODULE_ID=mitelIpGrpLogicalGroup, mitelProprietary=mitelProprietary, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpLogGrpLogicalTable=mitelIpLogGrpLogicalTable, mitelIpLogAdvertisementLifetime=mitelIpLogAdvertisementLifetime, mitelIpLogPerformRouterDiscovery=mitelIpLogPerformRouterDiscovery, mitelIpLogMinAdvertisementInterval=mitelIpLogMinAdvertisementInterval, mitelIpLogStatus=mitelIpLogStatus, mitelIpNetRouter=mitelIpNetRouter, mitelIpLogAdvertisementAddress=mitelIpLogAdvertisementAddress, mitelIpLogSolicitationAddress=mitelIpLogSolicitationAddress, mitel=mitel)
