#
# PySNMP MIB module IB-CA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-CA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
infinibandMIB, IbPhysPort = mibBuilder.importSymbols("IB-TC-MIB", "infinibandMIB", "IbPhysPort")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Counter32, Gauge32, iso, Bits, TimeTicks, MibIdentifier, IpAddress, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "iso", "Bits", "TimeTicks", "MibIdentifier", "IpAddress", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ibCaMIB = ModuleIdentity((1, 3, 6, 1, 3, 117, 4))
ibCaMIB.setRevisions(('2006-10-10 12:00',))
if mibBuilder.loadTexts: ibCaMIB.setLastUpdated('200610101200Z')
if mibBuilder.loadTexts: ibCaMIB.setOrganization('IETF IP Over IB (IPOIB) Working Group')
ibCaObjects = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 1))
ibCaConformance = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 2))
ibCaGeneralInfo = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 1, 1))
ibCaGeneralInfoTable = MibTable((1, 3, 6, 1, 3, 117, 4, 1, 1, 1), )
if mibBuilder.loadTexts: ibCaGeneralInfoTable.setStatus('current')
ibCaGeneralInfoEntry = MibTableRow((1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1), ).setIndexNames((0, "IB-CA-MIB", "ibCaIndex"))
if mibBuilder.loadTexts: ibCaGeneralInfoEntry.setStatus('current')
ibCaIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254)))
if mibBuilder.loadTexts: ibCaIndex.setStatus('current')
ibCaType = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("hca", 2), ("tca", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaType.setStatus('current')
ibCaNodeGuid = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaNodeGuid.setStatus('current')
ibCaNumPorts = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaNumPorts.setStatus('current')
ibCaAttrInfo = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 1, 2))
ibCaAttributeTable = MibTable((1, 3, 6, 1, 3, 117, 4, 1, 2, 1), )
if mibBuilder.loadTexts: ibCaAttributeTable.setStatus('current')
ibCaAttributeEntry = MibTableRow((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1), ).setIndexNames((0, "IB-CA-MIB", "ibCaIndex"))
if mibBuilder.loadTexts: ibCaAttributeEntry.setStatus('current')
ibCaHasReliableConnection = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaHasReliableConnection.setStatus('current')
ibCaHasUnreliableConnection = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaHasUnreliableConnection.setStatus('current')
ibCaHasReliableDatagram = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaHasReliableDatagram.setStatus('current')
ibCaHasUnreliableDatagram = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaHasUnreliableDatagram.setStatus('current')
ibCaSupportsAtomicOperations = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsAtomicOperations.setStatus('current')
ibCaSupportsOtherOperations = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsOtherOperations.setStatus('current')
ibCaSupportsSolicitedEvents = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsSolicitedEvents.setStatus('current')
ibCaPathMtuSetSupport = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("mtu256", 1), ("mtu256n512", 2), ("mtu256n512n1024", 3), ("mtu256n512n1024n2048", 4), ("mtu256n512n1024n2048n4096", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaPathMtuSetSupport.setStatus('current')
ibCaGenEndToEndFlowControl = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaGenEndToEndFlowControl.setStatus('current')
ibCaSupportsMulticast = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsMulticast.setStatus('current')
ibCaSupportsAutoPathMigration = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsAutoPathMigration.setStatus('current')
ibCaSupportsMemoryProtection = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsMemoryProtection.setStatus('current')
ibCaSupportsLoopback = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsLoopback.setStatus('current')
ibCaSupportsSubnetManager = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 2, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsSubnetManager.setStatus('current')
ibCaPortAttrInfo = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 1, 3))
ibCaPortAttributeTable = MibTable((1, 3, 6, 1, 3, 117, 4, 1, 3, 1), )
if mibBuilder.loadTexts: ibCaPortAttributeTable.setStatus('current')
ibCaPortAttributeEntry = MibTableRow((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1), ).setIndexNames((0, "IB-CA-MIB", "ibCaIndex"), (0, "IB-CA-MIB", "ibCaPortIndex"))
if mibBuilder.loadTexts: ibCaPortAttributeEntry.setStatus('current')
ibCaPortIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 1), IbPhysPort())
if mibBuilder.loadTexts: ibCaPortIndex.setStatus('current')
ibCaPortGuid = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaPortGuid.setStatus('current')
ibCaPhysicalInterface = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cable", 1), ("fiber", 2), ("backplane", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaPhysicalInterface.setStatus('current')
ibCaSupportsStaticRateControl = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsStaticRateControl.setStatus('current')
ibCaInterpacketDelayValue = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaInterpacketDelayValue.setStatus('current')
ibCaSupportsMultipathing = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaSupportsMultipathing.setStatus('current')
ibCaValidatesInPktDlid = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaValidatesInPktDlid.setStatus('current')
ibCaMaxGidsPerPort = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaMaxGidsPerPort.setStatus('current')
ibCaPortGidTable = MibTable((1, 3, 6, 1, 3, 117, 4, 1, 3, 2), )
if mibBuilder.loadTexts: ibCaPortGidTable.setStatus('current')
ibCaPortGidEntry = MibTableRow((1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1), ).setIndexNames((0, "IB-CA-MIB", "ibCaIndex"), (0, "IB-CA-MIB", "ibCaPortIndex"), (0, "IB-CA-MIB", "ibCaPortGidIndex"))
if mibBuilder.loadTexts: ibCaPortGidEntry.setStatus('current')
ibCaPortGidIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ibCaPortGidIndex.setStatus('current')
ibCaPortGidValue = MibTableColumn((1, 3, 6, 1, 3, 117, 4, 1, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCaPortGidValue.setStatus('current')
ibCaCompliances = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 2, 1))
ibCaGroups = MibIdentifier((1, 3, 6, 1, 3, 117, 4, 2, 2))
ibCaBasicCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 4, 2, 1, 1)).setObjects(("IB-CA-MIB", "ibCaGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaBasicCompliance = ibCaBasicCompliance.setStatus('current')
ibCaFullCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 4, 2, 1, 2)).setObjects(("IB-CA-MIB", "ibCaGeneralGroup"), ("IB-CA-MIB", "ibCaAttrGroup"), ("IB-CA-MIB", "ibCaPortAttrGroup"), ("IB-CA-MIB", "ibCaPortGidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaFullCompliance = ibCaFullCompliance.setStatus('current')
ibCaGeneralGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 4, 2, 2, 1)).setObjects(("IB-CA-MIB", "ibCaType"), ("IB-CA-MIB", "ibCaNodeGuid"), ("IB-CA-MIB", "ibCaNumPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaGeneralGroup = ibCaGeneralGroup.setStatus('current')
ibCaAttrGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 4, 2, 2, 2)).setObjects(("IB-CA-MIB", "ibCaHasReliableConnection"), ("IB-CA-MIB", "ibCaHasUnreliableConnection"), ("IB-CA-MIB", "ibCaHasReliableDatagram"), ("IB-CA-MIB", "ibCaHasUnreliableDatagram"), ("IB-CA-MIB", "ibCaSupportsAtomicOperations"), ("IB-CA-MIB", "ibCaSupportsOtherOperations"), ("IB-CA-MIB", "ibCaSupportsSolicitedEvents"), ("IB-CA-MIB", "ibCaPathMtuSetSupport"), ("IB-CA-MIB", "ibCaGenEndToEndFlowControl"), ("IB-CA-MIB", "ibCaSupportsMulticast"), ("IB-CA-MIB", "ibCaSupportsAutoPathMigration"), ("IB-CA-MIB", "ibCaSupportsMemoryProtection"), ("IB-CA-MIB", "ibCaSupportsLoopback"), ("IB-CA-MIB", "ibCaSupportsSubnetManager"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaAttrGroup = ibCaAttrGroup.setStatus('current')
ibCaPortAttrGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 4, 2, 2, 3)).setObjects(("IB-CA-MIB", "ibCaPortGuid"), ("IB-CA-MIB", "ibCaPhysicalInterface"), ("IB-CA-MIB", "ibCaSupportsStaticRateControl"), ("IB-CA-MIB", "ibCaInterpacketDelayValue"), ("IB-CA-MIB", "ibCaSupportsMultipathing"), ("IB-CA-MIB", "ibCaValidatesInPktDlid"), ("IB-CA-MIB", "ibCaMaxGidsPerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaPortAttrGroup = ibCaPortAttrGroup.setStatus('current')
ibCaPortGidGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 4, 2, 2, 4)).setObjects(("IB-CA-MIB", "ibCaPortGidValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibCaPortGidGroup = ibCaPortGidGroup.setStatus('current')
mibBuilder.exportSymbols("IB-CA-MIB", ibCaSupportsStaticRateControl=ibCaSupportsStaticRateControl, PYSNMP_MODULE_ID=ibCaMIB, ibCaSupportsAtomicOperations=ibCaSupportsAtomicOperations, ibCaPortAttrInfo=ibCaPortAttrInfo, ibCaPortIndex=ibCaPortIndex, ibCaPhysicalInterface=ibCaPhysicalInterface, ibCaPortGidIndex=ibCaPortGidIndex, ibCaCompliances=ibCaCompliances, ibCaGeneralInfoTable=ibCaGeneralInfoTable, ibCaNumPorts=ibCaNumPorts, ibCaHasUnreliableConnection=ibCaHasUnreliableConnection, ibCaAttrGroup=ibCaAttrGroup, ibCaPortAttrGroup=ibCaPortAttrGroup, ibCaValidatesInPktDlid=ibCaValidatesInPktDlid, ibCaAttributeEntry=ibCaAttributeEntry, ibCaBasicCompliance=ibCaBasicCompliance, ibCaSupportsMemoryProtection=ibCaSupportsMemoryProtection, ibCaGeneralInfoEntry=ibCaGeneralInfoEntry, ibCaPortAttributeTable=ibCaPortAttributeTable, ibCaGeneralGroup=ibCaGeneralGroup, ibCaAttrInfo=ibCaAttrInfo, ibCaSupportsMulticast=ibCaSupportsMulticast, ibCaIndex=ibCaIndex, ibCaPortAttributeEntry=ibCaPortAttributeEntry, ibCaAttributeTable=ibCaAttributeTable, ibCaSupportsSubnetManager=ibCaSupportsSubnetManager, ibCaPortGuid=ibCaPortGuid, ibCaHasReliableConnection=ibCaHasReliableConnection, ibCaHasUnreliableDatagram=ibCaHasUnreliableDatagram, ibCaPortGidTable=ibCaPortGidTable, ibCaPortGidEntry=ibCaPortGidEntry, ibCaPortGidGroup=ibCaPortGidGroup, ibCaType=ibCaType, ibCaObjects=ibCaObjects, ibCaPathMtuSetSupport=ibCaPathMtuSetSupport, ibCaMaxGidsPerPort=ibCaMaxGidsPerPort, ibCaConformance=ibCaConformance, ibCaFullCompliance=ibCaFullCompliance, ibCaPortGidValue=ibCaPortGidValue, ibCaNodeGuid=ibCaNodeGuid, ibCaGenEndToEndFlowControl=ibCaGenEndToEndFlowControl, ibCaGroups=ibCaGroups, ibCaInterpacketDelayValue=ibCaInterpacketDelayValue, ibCaSupportsLoopback=ibCaSupportsLoopback, ibCaHasReliableDatagram=ibCaHasReliableDatagram, ibCaSupportsOtherOperations=ibCaSupportsOtherOperations, ibCaMIB=ibCaMIB, ibCaSupportsAutoPathMigration=ibCaSupportsAutoPathMigration, ibCaSupportsSolicitedEvents=ibCaSupportsSolicitedEvents, ibCaSupportsMultipathing=ibCaSupportsMultipathing, ibCaGeneralInfo=ibCaGeneralInfo)
