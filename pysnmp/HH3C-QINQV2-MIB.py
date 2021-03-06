#
# PySNMP MIB module HH3C-QINQV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-QINQV2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, ObjectIdentity, NotificationType, Bits, Counter32, Gauge32, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ObjectIdentity", "NotificationType", "Bits", "Counter32", "Gauge32", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hh3cQinQv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 137))
hh3cQinQv2.setRevisions(('2013-03-08 00:00',))
if mibBuilder.loadTexts: hh3cQinQv2.setLastUpdated('201303080000Z')
if mibBuilder.loadTexts: hh3cQinQv2.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cQinQv2MibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1))
hh3cQinQv2ScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1))
hh3cQinQv2ServiceTPID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2ServiceTPID.setStatus('current')
hh3cQinQv2CustomerTPID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2CustomerTPID.setStatus('current')
hh3cQinQv2IfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2), )
if mibBuilder.loadTexts: hh3cQinQv2IfCfgTable.setStatus('current')
hh3cQinQv2IfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cQinQv2IfCfgEntry.setStatus('current')
hh3cQinQv2IfState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2IfState.setStatus('current')
hh3cQinQv2IfServiceTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2IfServiceTPID.setStatus('current')
hh3cQinQv2IfCustomerTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2IfCustomerTPID.setStatus('current')
hh3cQinQv2IfTransVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(512, 512)).setFixedLength(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cQinQv2IfTransVlanList.setStatus('current')
mibBuilder.exportSymbols("HH3C-QINQV2-MIB", hh3cQinQv2IfCfgTable=hh3cQinQv2IfCfgTable, hh3cQinQv2IfServiceTPID=hh3cQinQv2IfServiceTPID, hh3cQinQv2IfTransVlanList=hh3cQinQv2IfTransVlanList, hh3cQinQv2IfCfgEntry=hh3cQinQv2IfCfgEntry, hh3cQinQv2CustomerTPID=hh3cQinQv2CustomerTPID, hh3cQinQv2IfState=hh3cQinQv2IfState, hh3cQinQv2ScalarObjects=hh3cQinQv2ScalarObjects, PYSNMP_MODULE_ID=hh3cQinQv2, hh3cQinQv2MibObject=hh3cQinQv2MibObject, hh3cQinQv2=hh3cQinQv2, hh3cQinQv2IfCustomerTPID=hh3cQinQv2IfCustomerTPID, hh3cQinQv2ServiceTPID=hh3cQinQv2ServiceTPID)
