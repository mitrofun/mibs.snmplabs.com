#
# PySNMP MIB module MARVELL-ProtectedPorts-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-ProtectedPorts-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Counter64, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Gauge32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter64", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Gauge32", "Bits", "Counter32")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
rlProtectedPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 132))
rlProtectedPorts.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlProtectedPorts.setRevisionsDescriptions(('The private MIB module definition for Protected Ports MIB.',))
if mibBuilder.loadTexts: rlProtectedPorts.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlProtectedPorts.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlProtectedPorts.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlProtectedPorts.setDescription('<description>')
rlProtectedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 132, 1), )
if mibBuilder.loadTexts: rlProtectedPortsTable.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortsTable.setDescription('A table containing entries of protected ports configuration information')
rlProtectedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 132, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlProtectedPortsEntry.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortsEntry.setDescription('A table entry of protected ports configuration information')
rlProtectedPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-protected", 1), ("protected", 2))).clone('not-protected')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortType.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortType.setDescription('Set port protected mode: not-protected, protected protected ports filter layer 2 traffic from other protected ports')
rlProtectedPortCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortCommunity.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortCommunity.setDescription('Associate protected port with community number which becoming active only when rlProtectedPortsStatus changed to protected protected community ports filter layer 2 traffic from protected ports and from other protected community ports, but do not filter layer 2 traffic from same community ports. value of 0 disassociate port from its community. ')
rlProtectedPortsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 132, 2), )
if mibBuilder.loadTexts: rlProtectedPortsStatusTable.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortsStatusTable.setDescription('A table containing entries of protected ports status')
rlProtectedPortsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 132, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlProtectedPortsStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortsStatusEntry.setDescription('A table entry containing protected ports DB status information')
rlProtectedPortEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 2, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlProtectedPortEgressPorts.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortEgressPorts.setDescription('list of ports which are not filtered by protected port mechanism when traffic is forwarded from the specified ifIndex')
rlProtectedPortsGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 132, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortsGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: rlProtectedPortsGlobalEnable.setDescription('true - set all system fast ethernet ports to protected state false - set all system fast ethernet ports to not protected state')
mibBuilder.exportSymbols("MARVELL-ProtectedPorts-MIB", rlProtectedPortsTable=rlProtectedPortsTable, rlProtectedPortsStatusTable=rlProtectedPortsStatusTable, rlProtectedPortCommunity=rlProtectedPortCommunity, PYSNMP_MODULE_ID=rlProtectedPorts, rlProtectedPortsGlobalEnable=rlProtectedPortsGlobalEnable, rlProtectedPortType=rlProtectedPortType, rlProtectedPortEgressPorts=rlProtectedPortEgressPorts, rlProtectedPortsStatusEntry=rlProtectedPortsStatusEntry, rlProtectedPorts=rlProtectedPorts, rlProtectedPortsEntry=rlProtectedPortsEntry)
