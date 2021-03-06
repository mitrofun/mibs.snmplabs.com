#
# PySNMP MIB module SBFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SBFC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, iso, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, private, enterprises, Integer32, Gauge32, IpAddress, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "private", "enterprises", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stonesoft = MibIdentifier((1, 3, 6, 1, 4, 1, 1369))
stoneSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2))
fullCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2))
sbfcModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4))
sbfcDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5))
agentDescr = MibScalar((1, 3, 6, 1, 4, 1, 1369, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDescr.setStatus('mandatory')
if mibBuilder.loadTexts: agentDescr.setDescription("The SNMP agent's description of itself.")
agentVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentVersion.setStatus('mandatory')
if mibBuilder.loadTexts: agentVersion.setDescription('The SNMP agent mib version.')
sbfcClusterID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcClusterID.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcClusterID.setDescription('The StoneBeat cluster ID.')
sbfcMemberID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcMemberID.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcMemberID.setDescription('The ID of this node in the StoneBeat FullCluster.')
sbfcModuleVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcModuleVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcModuleVersion.setDescription('The version of the StoneBeat FullCluster module on this host.')
sbfcModulePatchLevel = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcModulePatchLevel.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcModulePatchLevel.setDescription('The patch level of the StoneBeat FullCluster module')
sbfcDriverPatchLevel = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcDriverPatchLevel.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcDriverPatchLevel.setDescription('The patch level of the StoneBeat FullCluster driver')
sbfcDriverVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcDriverVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcDriverVersion.setDescription('The version of the StoneBeat FullCluster driver on this host.')
sbfcMaxNodeID = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcMaxNodeID.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcMaxNodeID.setDescription('The maximum number of nodes in this cluster and at the same time the highes possible index in the status sequences.')
sbfcOSName = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcOSName.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcOSName.setDescription('Name of the operating system')
sbfcOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcOSVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcOSVersion.setDescription('Operating system version')
sbfcAgeOfStatus = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcAgeOfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcAgeOfStatus.setDescription('Time in seconds since we got the cluster status')
sbfcNodeTable = MibTable((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9), )
if mibBuilder.loadTexts: sbfcNodeTable.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeTable.setDescription('A list of node entries. The number of entries is given by sbfcMaxNodeID.')
sbfcNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1), )
if mibBuilder.loadTexts: sbfcNodeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeEntry.setDescription('A node entry containing object describing each node in the cluster.')
sbfcNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeID.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeID.setDescription('A unique value for each node. Its value ranges between 1 and the value of sbfcMaxNodeID.')
sbfcNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("offline", 1), ("going-online", 2), ("online", 3), ("going-offline", 4), ("unknown", 5), ("offline-ready-for-restart", 6), ("online-ready-for-restart", 7), ("locked-offline", 8), ("going-locked-offline", 9), ("locked-online", 10), ("going-locked-online", 11), ("locked-offline-ready-for-restart", 12), ("locked-online-ready-for-restart", 13), ("standby", 14), ("going-standby", 15), ("standby-ready-for-restart", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeStatus.setDescription('The node status')
sbfcNodeLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeLoad.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeLoad.setDescription('The load level of this node. The value is a percentage of the capacity of the node.')
sbfcNodeCapacity = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeCapacity.setDescription('The capacity of this node')
sbfcNodeControlIp = MibScalar((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeControlIp.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeControlIp.setDescription('The control IP address of this node')
sbfcNodeControlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbfcNodeControlPort.setStatus('mandatory')
if mibBuilder.loadTexts: sbfcNodeControlPort.setDescription('The control port number of this node 0 denotes NULL')
mibBuilder.exportSymbols("SBFC-MIB", fullCluster=fullCluster, sbfcDriverPatchLevel=sbfcDriverPatchLevel, sbfcModuleVersion=sbfcModuleVersion, sbfcNodeEntry=sbfcNodeEntry, sbfcNodeControlPort=sbfcNodeControlPort, sbfcMaxNodeID=sbfcMaxNodeID, sbfcNodeTable=sbfcNodeTable, sbfcNodeLoad=sbfcNodeLoad, products=products, sbfcClusterID=sbfcClusterID, sbfcOSVersion=sbfcOSVersion, agentVersion=agentVersion, sbfcAgeOfStatus=sbfcAgeOfStatus, sbfcMemberID=sbfcMemberID, sbfcNodeID=sbfcNodeID, sbfcNodeStatus=sbfcNodeStatus, agentDescr=agentDescr, sbfcModulePatchLevel=sbfcModulePatchLevel, sbfcOSName=sbfcOSName, sbfcNodeControlIp=sbfcNodeControlIp, stoneSystem=stoneSystem, sbfcDriver=sbfcDriver, sbfcNodeCapacity=sbfcNodeCapacity, sbfcDriverVersion=sbfcDriverVersion, stonesoft=stonesoft, sbfcModule=sbfcModule)
