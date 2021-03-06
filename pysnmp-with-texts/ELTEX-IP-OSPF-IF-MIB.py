#
# PySNMP MIB module ELTEX-IP-OSPF-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-IP-OSPF-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
eltMesOspf, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesOspf")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, iso, TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Gauge32, Counter32, Counter64, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "iso", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "Bits", "IpAddress")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
eltIpOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2), )
if mibBuilder.loadTexts: eltIpOspfIfTable.setReference('OSPF Version 2, Appendix C.3 Router interface parameters')
if mibBuilder.loadTexts: eltIpOspfIfTable.setStatus('current')
if mibBuilder.loadTexts: eltIpOspfIfTable.setDescription('The OSPF Interface Table describes the inter- faces from the viewpoint of OSPF.')
eltIpOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1), ).setIndexNames((0, "ELTEX-IP-OSPF-IF-MIB", "eltOspfIfAddress"))
if mibBuilder.loadTexts: eltIpOspfIfEntry.setStatus('current')
if mibBuilder.loadTexts: eltIpOspfIfEntry.setDescription('The OSPF Interface Entry describes one inter- face from the viewpoint of OSPF.')
eltOspfIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfAddress.setStatus('current')
if mibBuilder.loadTexts: eltOspfIfAddress.setDescription('The IP address of this OSPF interface.')
eltOspfIfPassiveDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveDefault.setStatus('current')
if mibBuilder.loadTexts: eltOspfIfPassiveDefault.setDescription(' ')
eltOspfIfPassiveList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltOspfIfPassiveList.setStatus('current')
if mibBuilder.loadTexts: eltOspfIfPassiveList.setDescription('Indicates whether the OSPF interface on this Vlan is Passive or not. Passive interfaces do not send routing updates. A true value indicates that the interface is passive.')
eltOspfIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltOspfIfStatus.setStatus('current')
if mibBuilder.loadTexts: eltOspfIfStatus.setDescription('This variable displays the status of the en- try.')
mibBuilder.exportSymbols("ELTEX-IP-OSPF-IF-MIB", eltOspfIfPassiveDefault=eltOspfIfPassiveDefault, eltIpOspfIfTable=eltIpOspfIfTable, eltIpOspfIfEntry=eltIpOspfIfEntry, eltOspfIfStatus=eltOspfIfStatus, eltOspfIfPassiveList=eltOspfIfPassiveList, eltOspfIfAddress=eltOspfIfAddress)
