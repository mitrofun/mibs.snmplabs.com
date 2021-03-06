#
# PySNMP MIB module QoS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, IpAddress, Gauge32, Integer32, MibIdentifier, ModuleIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "IpAddress", "Gauge32", "Integer32", "MibIdentifier", "ModuleIdentity", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swQoSMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 61))
if mibBuilder.loadTexts: swQoSMIB.setLastUpdated('0904090000Z')
if mibBuilder.loadTexts: swQoSMIB.setOrganization('D-Link Corp.')
swQoSCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 61, 1))
swQoSInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 61, 2))
swQoSMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 61, 3))
swCoSBandwidthControlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 61, 3, 9), )
if mibBuilder.loadTexts: swCoSBandwidthControlTable.setStatus('current')
swCoSBandwidthControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 61, 3, 9, 1), ).setIndexNames((0, "QoS-MIB", "swCoSBandwidthPort"), (0, "QoS-MIB", "swCoSBandwidthCoSID"))
if mibBuilder.loadTexts: swCoSBandwidthControlEntry.setStatus('current')
swCoSBandwidthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 61, 3, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: swCoSBandwidthPort.setStatus('current')
swCoSBandwidthCoSID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 61, 3, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: swCoSBandwidthCoSID.setStatus('current')
swCoSBandwidthMaxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 61, 3, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 1024000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCoSBandwidthMaxRate.setStatus('current')
mibBuilder.exportSymbols("QoS-MIB", swCoSBandwidthControlTable=swCoSBandwidthControlTable, swQoSCtrl=swQoSCtrl, swCoSBandwidthMaxRate=swCoSBandwidthMaxRate, swQoSMgmt=swQoSMgmt, swCoSBandwidthPort=swCoSBandwidthPort, swCoSBandwidthControlEntry=swCoSBandwidthControlEntry, PYSNMP_MODULE_ID=swQoSMIB, swQoSMIB=swQoSMIB, swQoSInfo=swQoSInfo, swCoSBandwidthCoSID=swCoSBandwidthCoSID)
