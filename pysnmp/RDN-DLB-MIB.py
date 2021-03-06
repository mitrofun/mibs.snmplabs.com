#
# PySNMP MIB module RDN-DLB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-DLB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, Gauge32, MibIdentifier, TimeTicks, ModuleIdentity, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
rdnLoadBalance = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 8))
rdnLoadBalance.setRevisions(('2008-08-08 00:00', '2004-09-15 00:00', '2004-09-15 00:00',))
if mibBuilder.loadTexts: rdnLoadBalance.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnLoadBalance.setOrganization('Motorola')
rdnLoadBalBasicRuleTable = MibTable((1, 3, 6, 1, 4, 1, 4981, 8, 1), )
if mibBuilder.loadTexts: rdnLoadBalBasicRuleTable.setStatus('current')
rdnLoadBalBasicRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1), ).setIndexNames((0, "RDN-DLB-MIB", "rdnLoadBalBasicRuleId"))
if mibBuilder.loadTexts: rdnLoadBalBasicRuleEntry.setStatus('current')
rdnLoadBalBasicRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rdnLoadBalBasicRuleId.setStatus('current')
rdnLoadBalBasicRuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("upstream", 1), ("downstream", 2), ("interval", 3), ("registration", 4), ("rem-dsx", 5), ("spec-trig", 6), ("ds-reg", 7), ("us-reg-bonding", 8), ("ds-reg-bonding", 9)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleEnable.setStatus('current')
rdnLoadBalBasicRuleMinThres = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleMinThres.setStatus('current')
rdnLoadBalBasicRuleDeltaThres = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleDeltaThres.setStatus('current')
rdnLoadBalBasicRuleStopThres = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleStopThres.setStatus('current')
rdnLoadBalBasicRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleRowStatus.setStatus('current')
rdnLoadBalBasicRuleModemCountThres = MibTableColumn((1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalBasicRuleModemCountThres.setStatus('current')
rdnLoadBalOperations = ObjectGroup((1, 3, 6, 1, 4, 1, 4981, 8, 2)).setObjects(("RDN-DLB-MIB", "rdnLoadBalanceUpstreamModemCount"), ("RDN-DLB-MIB", "rdnLoadBalanceDnstreamModemCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rdnLoadBalOperations = rdnLoadBalOperations.setStatus('current')
rdnLoadBalanceUpstreamModemCount = MibScalar((1, 3, 6, 1, 4, 1, 4981, 8, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('Load-Balance Group ID [0-255]').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnLoadBalanceUpstreamModemCount.setStatus('current')
rdnLoadBalanceDnstreamModemCount = MibScalar((1, 3, 6, 1, 4, 1, 4981, 8, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('Load-Balance Group ID [0-255]').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdnLoadBalanceDnstreamModemCount.setStatus('current')
rdnLoadBalGroupInterval = MibScalar((1, 3, 6, 1, 4, 1, 4981, 8, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 480))).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdnLoadBalGroupInterval.setStatus('current')
mibBuilder.exportSymbols("RDN-DLB-MIB", rdnLoadBalOperations=rdnLoadBalOperations, PYSNMP_MODULE_ID=rdnLoadBalance, rdnLoadBalBasicRuleEntry=rdnLoadBalBasicRuleEntry, rdnLoadBalance=rdnLoadBalance, rdnLoadBalBasicRuleDeltaThres=rdnLoadBalBasicRuleDeltaThres, rdnLoadBalBasicRuleStopThres=rdnLoadBalBasicRuleStopThres, rdnLoadBalBasicRuleRowStatus=rdnLoadBalBasicRuleRowStatus, rdnLoadBalanceDnstreamModemCount=rdnLoadBalanceDnstreamModemCount, rdnLoadBalanceUpstreamModemCount=rdnLoadBalanceUpstreamModemCount, rdnLoadBalBasicRuleId=rdnLoadBalBasicRuleId, rdnLoadBalBasicRuleModemCountThres=rdnLoadBalBasicRuleModemCountThres, rdnLoadBalGroupInterval=rdnLoadBalGroupInterval, rdnLoadBalBasicRuleTable=rdnLoadBalBasicRuleTable, rdnLoadBalBasicRuleMinThres=rdnLoadBalBasicRuleMinThres, rdnLoadBalBasicRuleEnable=rdnLoadBalBasicRuleEnable)
