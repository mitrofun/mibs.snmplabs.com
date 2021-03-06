#
# PySNMP MIB module STN-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, IpAddress, TimeTicks, Gauge32, NotificationType, MibIdentifier, Counter32, iso, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "iso", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
stnSystems, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnSystems")
stnSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 4))
if mibBuilder.loadTexts: stnSystemMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnSystemMIB.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnSystemMIB.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnSystemMIB.setDescription('STN System MIB.')
stnSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1))
stnSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 2))
stnSysTimeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1))
stnSysAttrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2))
stnSysServersGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3))
stnSysCfgCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4))
stnUTCOffset = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnUTCOffset.setStatus('current')
if mibBuilder.loadTexts: stnUTCOffset.setDescription('Specifies the number of hours to add or subtract from the universal time constant (UTC) when converting to local time.')
stnDaylightTime = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 2), TruthValue().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnDaylightTime.setStatus('current')
if mibBuilder.loadTexts: stnDaylightTime.setDescription('Specifies whether the system should adjust local time to compensate for daylight savings time.')
stnTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("internal", 1), ("external-NTP", 2), ("external-RC868", 3), ("all", 4))).clone('all')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnTimeSource.setStatus('current')
if mibBuilder.loadTexts: stnTimeSource.setDescription('Specifies which sources the system should use attempting to obtain the current time.')
stnRFC868Server = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRFC868Server.setStatus('current')
if mibBuilder.loadTexts: stnRFC868Server.setDescription('If an NTP server is to be used as a time source, this value specifies the IP address of the server to query.')
stnNTPServer = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnNTPServer.setStatus('current')
if mibBuilder.loadTexts: stnNTPServer.setDescription('If an RFC-868 server is to be used as a time source this value specifies the IP address of the server to query.')
stnQueryTime = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(300)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnQueryTime.setStatus('current')
if mibBuilder.loadTexts: stnQueryTime.setDescription('Specifies the time in seconds that the ETS should continue an external query for a network based time server.')
stnDeviceIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnDeviceIPAddress.setStatus('current')
if mibBuilder.loadTexts: stnDeviceIPAddress.setDescription('The main IP address of the ETS.')
stnDeviceSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnDeviceSubnetMask.setStatus('current')
if mibBuilder.loadTexts: stnDeviceSubnetMask.setDescription('The IP subnet mask of the ETS.')
stnSocketDelay = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSocketDelay.setStatus('current')
if mibBuilder.loadTexts: stnSocketDelay.setDescription('The number of seconds that the ETS will wait on a socket while sending and receiving data to or from the management application before considering the socket dead.')
stnDumpMode = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("core", 2), ("context", 3), ("log", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnDumpMode.setStatus('current')
if mibBuilder.loadTexts: stnDumpMode.setDescription('Specifies the type of crash dump to execute following a crash.')
stnTelnetServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnTelnetServerEnabled.setStatus('current')
if mibBuilder.loadTexts: stnTelnetServerEnabled.setDescription('Enable Telnet support for external communications.')
stnFTPServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 2), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnFTPServerEnabled.setStatus('current')
if mibBuilder.loadTexts: stnFTPServerEnabled.setDescription('Enable FTP support for external communications.')
stnDNSServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnDNSServerEnabled.setStatus('current')
if mibBuilder.loadTexts: stnDNSServerEnabled.setDescription('Enable DNS support.')
stnSysCfgCtrlNfsHost = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSysCfgCtrlNfsHost.setStatus('current')
if mibBuilder.loadTexts: stnSysCfgCtrlNfsHost.setDescription('Specifies the IP address of an NFS server which can optionally be used for automatic backup of configuration files.')
stnSysCfgCtrlNfsPath = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSysCfgCtrlNfsPath.setStatus('current')
if mibBuilder.loadTexts: stnSysCfgCtrlNfsPath.setDescription('Specifies the path to an NFS server which can optionally be used for automatic backup of configuration files.')
stnSysCfgCtrlCommitToFlashTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 3), Integer32().clone(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSysCfgCtrlCommitToFlashTimeout.setStatus('current')
if mibBuilder.loadTexts: stnSysCfgCtrlCommitToFlashTimeout.setDescription('Specifies the amount of time in seconds the system will wait before saving committed configuration changes to flash disk.')
mibBuilder.exportSymbols("STN-SYSTEM-MIB", stnSystemMIBObjects=stnSystemMIBObjects, stnSysTimeGroup=stnSysTimeGroup, stnSysCfgCtrlCommitToFlashTimeout=stnSysCfgCtrlCommitToFlashTimeout, stnSysCfgCtrlNfsHost=stnSysCfgCtrlNfsHost, stnDNSServerEnabled=stnDNSServerEnabled, stnFTPServerEnabled=stnFTPServerEnabled, stnTimeSource=stnTimeSource, stnDumpMode=stnDumpMode, stnSystemMIBConformance=stnSystemMIBConformance, stnSysAttrGroup=stnSysAttrGroup, stnUTCOffset=stnUTCOffset, stnSysCfgCtrlNfsPath=stnSysCfgCtrlNfsPath, stnTelnetServerEnabled=stnTelnetServerEnabled, stnQueryTime=stnQueryTime, stnDeviceSubnetMask=stnDeviceSubnetMask, stnSysCfgCtrlGroup=stnSysCfgCtrlGroup, stnDeviceIPAddress=stnDeviceIPAddress, stnRFC868Server=stnRFC868Server, PYSNMP_MODULE_ID=stnSystemMIB, stnSystemMIB=stnSystemMIB, stnDaylightTime=stnDaylightTime, stnNTPServer=stnNTPServer, stnSocketDelay=stnSocketDelay, stnSysServersGroup=stnSysServersGroup)
