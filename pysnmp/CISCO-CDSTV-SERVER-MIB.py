#
# PySNMP MIB module CISCO-CDSTV-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Dscp, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, MibIdentifier, Gauge32, TimeTicks, Counter64, ObjectIdentity, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Gauge32", "TimeTicks", "Counter64", "ObjectIdentity", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ModuleIdentity", "Bits", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoCdstvServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 754))
ciscoCdstvServerMIB.setRevisions(('2012-12-12 00:00', '2010-07-13 00:00',))
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setLastUpdated('201212120000Z')
if mibBuilder.loadTexts: ciscoCdstvServerMIB.setOrganization('Cisco Systems, Inc.')
class CiscoCdstvEcn(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ect1", 1), ("ect0", 2), ("congestion", 3), ("disabled", 4))

ciscoCdstvServerMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 0))
ciscoCdstvServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1))
ciscoCdstvServerMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2))
ciscoCdstvServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1))
cdstvServerCommonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1))
cdstvServerStreamingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2))
cdstvServerStorageObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3))
cdstvServerCachingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4))
cdstvServerRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("isv", 1), ("vault", 2), ("streamer", 3), ("controller", 4), ("cachingserver", 5), ("recorder", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerRole.setStatus('current')
cdstvServerPartNo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerPartNo.setStatus('current')
cdstvServerID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerID.setStatus('current')
cdstvServerGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerGroupID.setStatus('current')
cdstvServerHostname = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerHostname.setStatus('current')
cdstvServerTTL = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(16)).setUnits('hops').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTTL.setStatus('current')
cdstvServerDefaultStreamCacheSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7))
cdstvCacheJumboFramesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvCacheJumboFramesEnable.setStatus('current')
cdstvServerOffloadEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerOffloadEnable.setStatus('current')
cdstvServerTransportCacheIPPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10))
cdstvServerNullStreamingEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerNullStreamingEnable.setStatus('current')
cdstvServerStartingTransportPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 1), InetPortNumber().clone(48879)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerStartingTransportPort.setStatus('current')
cdstvServerEndingTransportPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 2), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerEndingTransportPort.setStatus('current')
cdstvStreamJumboFramesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvStreamJumboFramesEnable.setStatus('current')
cdstvServerStreamGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4))
cdstvServerStreamGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerStreamGroupName.setStatus('current')
cdstvServerStreamGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerStreamGroupID.setStatus('current')
cdstvServerStreamerIsCache = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerStreamerIsCache.setStatus('current')
cdstvVaultMirrorCopies = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setUnits('copies').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvVaultMirrorCopies.setStatus('current')
cdstvServerCacheGroupInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1))
cdstvServerCacheGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerCacheGroupName.setStatus('current')
cdstvServerCacheGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerCacheGroupID.setStatus('current')
cdstvVaultLocalCopies = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setUnits('copies').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvVaultLocalCopies.setStatus('current')
cdstvServerFTPOutSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3))
cdstvServerVaultGroupInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4))
cdstvServerFTPOutInterface = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("management", 1), ("ingest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutInterface.setStatus('current')
cdstvServerFTPOutBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('Mbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutBandwidth.setStatus('current')
cdstvServerFTPOutSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('sessions').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerFTPOutSessions.setStatus('current')
cdstvServerVaultGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerVaultGroupName.setStatus('current')
cdstvServerVaultGroupID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServerVaultGroupID.setStatus('current')
cdstvServerSourceAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 1), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSourceAddressType.setStatus('current')
cdstvServerSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 2), InetAddress().clone('192.168.207.65')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSourceAddress.setStatus('current')
cdstvServerCachePort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 3), InetPortNumber().clone(48879)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCachePort.setStatus('current')
cdstvServerTransportDSCP = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 1), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTransportDSCP.setStatus('current')
cdstvServerTransportECN = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 2), CiscoCdstvEcn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerTransportECN.setStatus('current')
cdstvServerCacheDSCP = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 3), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCacheDSCP.setStatus('current')
cdstvServerCacheECN = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 4), CiscoCdstvEcn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerCacheECN.setStatus('current')
ciscoCdstvServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2))
ciscoCdstvServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1, 1)).setObjects(("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBMainObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBStreamingObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBStorageObjectGroup"), ("CISCO-CDSTV-SERVER-MIB", "ciscoCdstvServerMIBCachingObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBCompliance = ciscoCdstvServerMIBCompliance.setStatus('current')
ciscoCdstvServerMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 1)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerRole"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerPartNo"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerGroupID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerHostname"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTTL"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddress"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCachePort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvCacheJumboFramesEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerOffloadEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportDSCP"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportECN"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheDSCP"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheECN"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddressType"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerNullStreamingEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBMainObjectGroup = ciscoCdstvServerMIBMainObjectGroup.setStatus('current')
ciscoCdstvServerMIBStreamingObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 2)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerStartingTransportPort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerEndingTransportPort"), ("CISCO-CDSTV-SERVER-MIB", "cdstvStreamJumboFramesEnable"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupID"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamerIsCache"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBStreamingObjectGroup = ciscoCdstvServerMIBStreamingObjectGroup.setStatus('current')
ciscoCdstvServerMIBStorageObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 3)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvVaultMirrorCopies"), ("CISCO-CDSTV-SERVER-MIB", "cdstvVaultLocalCopies"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutInterface"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutBandwidth"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutSessions"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBStorageObjectGroup = ciscoCdstvServerMIBStorageObjectGroup.setStatus('current')
ciscoCdstvServerMIBCachingObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 4)).setObjects(("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupName"), ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServerMIBCachingObjectGroup = ciscoCdstvServerMIBCachingObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-SERVER-MIB", cdstvServerCacheGroupID=cdstvServerCacheGroupID, cdstvServerCachingObjects=cdstvServerCachingObjects, cdstvServerDefaultStreamCacheSettings=cdstvServerDefaultStreamCacheSettings, cdstvServerCacheGroupInformation=cdstvServerCacheGroupInformation, cdstvVaultMirrorCopies=cdstvVaultMirrorCopies, cdstvServerCachePort=cdstvServerCachePort, cdstvServerStreamerIsCache=cdstvServerStreamerIsCache, cdstvCacheJumboFramesEnable=cdstvCacheJumboFramesEnable, cdstvServerNullStreamingEnable=cdstvServerNullStreamingEnable, cdstvServerOffloadEnable=cdstvServerOffloadEnable, ciscoCdstvServerMIBCachingObjectGroup=ciscoCdstvServerMIBCachingObjectGroup, cdstvServerTransportCacheIPPkts=cdstvServerTransportCacheIPPkts, cdstvServerID=cdstvServerID, CiscoCdstvEcn=CiscoCdstvEcn, cdstvServerStreamGroupID=cdstvServerStreamGroupID, cdstvServerFTPOutInterface=cdstvServerFTPOutInterface, cdstvServerVaultGroupID=cdstvServerVaultGroupID, ciscoCdstvServerMIBObjects=ciscoCdstvServerMIBObjects, cdstvServerTransportDSCP=cdstvServerTransportDSCP, cdstvServerCacheECN=cdstvServerCacheECN, cdstvServerTTL=cdstvServerTTL, ciscoCdstvServerMIBGroups=ciscoCdstvServerMIBGroups, cdstvServerHostname=cdstvServerHostname, ciscoCdstvServerMIBNotifs=ciscoCdstvServerMIBNotifs, ciscoCdstvServerMIBCompliances=ciscoCdstvServerMIBCompliances, cdstvServerStorageObjects=cdstvServerStorageObjects, cdstvServerVaultGroupInformation=cdstvServerVaultGroupInformation, ciscoCdstvServerMIBStreamingObjectGroup=ciscoCdstvServerMIBStreamingObjectGroup, ciscoCdstvServerMIB=ciscoCdstvServerMIB, ciscoCdstvServerMIBConform=ciscoCdstvServerMIBConform, cdstvServerFTPOutBandwidth=cdstvServerFTPOutBandwidth, cdstvServerCacheGroupName=cdstvServerCacheGroupName, cdstvServerSourceAddress=cdstvServerSourceAddress, cdstvServerStreamingObjects=cdstvServerStreamingObjects, cdstvServerPartNo=cdstvServerPartNo, cdstvServerFTPOutSessions=cdstvServerFTPOutSessions, cdstvServerVaultGroupName=cdstvServerVaultGroupName, cdstvServerGroupID=cdstvServerGroupID, cdstvServerStartingTransportPort=cdstvServerStartingTransportPort, cdstvServerTransportECN=cdstvServerTransportECN, cdstvServerSourceAddressType=cdstvServerSourceAddressType, cdstvServerStreamGroupName=cdstvServerStreamGroupName, cdstvVaultLocalCopies=cdstvVaultLocalCopies, ciscoCdstvServerMIBStorageObjectGroup=ciscoCdstvServerMIBStorageObjectGroup, cdstvServerCacheDSCP=cdstvServerCacheDSCP, cdstvServerCommonObjects=cdstvServerCommonObjects, cdstvServerEndingTransportPort=cdstvServerEndingTransportPort, cdstvServerFTPOutSettings=cdstvServerFTPOutSettings, PYSNMP_MODULE_ID=ciscoCdstvServerMIB, cdstvServerRole=cdstvServerRole, cdstvStreamJumboFramesEnable=cdstvStreamJumboFramesEnable, cdstvServerStreamGroupInfo=cdstvServerStreamGroupInfo, ciscoCdstvServerMIBCompliance=ciscoCdstvServerMIBCompliance, ciscoCdstvServerMIBMainObjectGroup=ciscoCdstvServerMIBMainObjectGroup)
