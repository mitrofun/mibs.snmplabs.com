#
# PySNMP MIB module XGCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XGCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:44:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, MibIdentifier, NotificationType, IpAddress, Counter32, experimental, Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "IpAddress", "Counter32", "experimental", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Bits", "Integer32")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
xgcpMIB = ModuleIdentity((1, 3, 6, 1, 3, 90))
xgcpMIB.setRevisions(('1999-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: xgcpMIB.setRevisionsDescriptions(('This is initial version of XGCP MIB.',))
if mibBuilder.loadTexts: xgcpMIB.setLastUpdated('9904010000Z')
if mibBuilder.loadTexts: xgcpMIB.setOrganization('Submitting this new XGCP-MIB to IETF-DRAFT')
if mibBuilder.loadTexts: xgcpMIB.setContactInfo(' Dinh D. Nguyen Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US Phone: +1 408 525 1624 Email: dinhn@cisco.com Rick N. Chen Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US Phone: +1 408 525 6367 Email: richen@cisco.com')
if mibBuilder.loadTexts: xgcpMIB.setDescription('The MIB module for managing XGCP implementations.')
xgcpObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1))
xgcpCoreObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 1))
xgcpExtensionObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 2))
xgcpPackageObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 3))
xgcpVoiceQualityObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 4))
xgcpDefaultMGCObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 5))
xgcpInBadVersions = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 1), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpInBadVersions.setStatus('current')
if mibBuilder.loadTexts: xgcpInBadVersions.setDescription('The total number of incoming messages which were delivered to the protocol entity and were for an unsupported protocol version. ')
xgcpRequestTimeOut = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRequestTimeOut.setStatus('current')
if mibBuilder.loadTexts: xgcpRequestTimeOut.setDescription('The request timeout is used to determine the timeout value used for retransmitting unacknowledged message. It is the responsibility of the requesting entity to provide suitable timeouts for all outstanding commands, and to retry commands when timeouts exceeded. The default value of this object is 500 milliseconds. ')
xgcpRequestRetries = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRequestRetries.setStatus('current')
if mibBuilder.loadTexts: xgcpRequestRetries.setDescription('This object specifies the number of retries for a request that exceeds timeout. It is the responsibility of the requesting entity to provide suitable timeouts for all outstanding commands, and to retry when times out. The default value of this object is 3. ')
xgcpAdminStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("gracefulDown", 3))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpAdminStatus.setDescription('The desired state of the protocol entity. The possible admin status are: up - bring up protocol entity administratively down - bring down protocol entity adiministratively gracefulDown - gracefully shut down protocol entity administratively. A graceful shutdown indicates that the protocol will be taken out of service after the restart delay timer timeouts or all connections are torn down. When in graceDown, the xgcpOperStatus goes from up to down via shutDownInProgress. If there is no connection or restart delay timer timeouts then xgcpOperStatus moves from shutDownInProgress to down. ')
xgcpOperStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("shutDownInProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpOperStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpOperStatus.setDescription("This object indicates the current operational status of the protocol entity. The possible operating status are: up - protocol up down - protocol down shutDownInProgress - Shut down in progress. The operating status - shutDownInProgress indicates that the Media Gateway is in a transition state from up to down. This state happens when resources are in the process of being cleaned up and new resource can't be allocated. ")
xgcpUnRecognizedPackets = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpUnRecognizedPackets.setStatus('current')
if mibBuilder.loadTexts: xgcpUnRecognizedPackets.setDescription(' This refers to the count of unrecognized packets since reset. ')
xgcpMsgStatTable = MibTable((1, 3, 6, 1, 3, 90, 1, 1, 7), )
if mibBuilder.loadTexts: xgcpMsgStatTable.setStatus('current')
if mibBuilder.loadTexts: xgcpMsgStatTable.setDescription('This table contains XGCP statistics information since reset. XGCP statistics are kept in this table, with each table entry containing the statistics of XGCP that communicates with a Media Gateway Controller (MGC) at a specific IP address of the MGC. Each table entry is composed of the following information: 1) Messages successfully received/transmitted per IP device 2) Messages failed to be received/transmitted per IP device ')
xgcpMsgStatEntry = MibTableRow((1, 3, 6, 1, 3, 90, 1, 1, 7, 1), ).setIndexNames((0, "XGCP-MIB", "xgcpIPAddress"))
if mibBuilder.loadTexts: xgcpMsgStatEntry.setStatus('current')
if mibBuilder.loadTexts: xgcpMsgStatEntry.setDescription('The row of the xgcpMsgStatTable contains information about XGCP message statistics per IP address of the Media Gateway Controller. An entry is created when a request messge with new IP address is received from Medida Gateway Controller. When the table is full, an entry is deleted if it is LRU (Least Recently Used). ')
xgcpIPAddress = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: xgcpIPAddress.setStatus('current')
if mibBuilder.loadTexts: xgcpIPAddress.setDescription(' This object specifies the IP address of the Media Gateway Controller. ')
xgcpSuccessMessages = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpSuccessMessages.setStatus('current')
if mibBuilder.loadTexts: xgcpSuccessMessages.setDescription('This object specifies the count of successful messages that communicate with the Media Gateway Controller on that IP address. Successful messages apply to both transmit and receive messages. Transmit: Positive ACK is received from the Media Gateway Controller Receive: Positive ACK is sent to the Media Gateway Controller. This implies that the format of the message is correct and the request can be fulfilled. ')
xgcpFailMessages = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpFailMessages.setStatus('current')
if mibBuilder.loadTexts: xgcpFailMessages.setDescription('This object specifies the count of failed messages that communicate with the Media Gateway Controller on that IP address. Failed messages apply to both transmit and receive messages. Transmit: Either NAK is received from the MGC or message times out waiting for ACK. Receive: Format of the received message is bad or the request can not be fulfilled. ')
xgcpRestartInProgressMWD = MibScalar((1, 3, 6, 1, 3, 90, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setReference(' Media Gateway Control Protocol (MGCP), version 0.1 draft, Feb 1, 1999 : Section 4.3.4 ')
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setStatus('current')
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setDescription('The maximum waiting delay (MWD) timeout value is used for the Media Gateway to send the Restart In Progress to the Media Gateway Controller. The default value of this object is chosen in an implementation-dependent manner by the MGCP functionality based on the call volume of the system. ')
xgcpRestartDelay = MibScalar((1, 3, 6, 1, 3, 90, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRestartDelay.setReference(' Media Gateway Control Protocol (MGCP), version 0.1 draft, Feb 1, 1999 : Section 4.3.4 ')
if mibBuilder.loadTexts: xgcpRestartDelay.setStatus('current')
if mibBuilder.loadTexts: xgcpRestartDelay.setDescription('This object specifies the Restart Delay Timeout for the restart process. The purpose of setting the restart timer before sending the Restart In Progress notification to the media gateway controller is to avoid the network congestion during the critical period of service restoration. -1: infinity which indicates no timeout. 0: immediate timeout which indicates immediate shutdown. The default value of this object is -1. ')
xgcpMGCCfgAddress = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpMGCCfgAddress.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgAddress.setDescription('This object is used to configure either the domain name or the IP address of the Default Media Gateway Controller in standard dot notation. The complete address of a default MGC is cmposed of IP address/Domain Name and UDP port. xgcpMGCCfgaddress specifies address of the default Media Gateway Controller to which RSIP(RestartInProgress) message is sent whenever system starts up or line goes up. If DNS name is entered and the IP address is found, MG will send RSIP to the desired MGC. If no IP address is found or no such DNS name exists, no RSIP will be sent. If IP address is entered, MG will send RSIP to that address. If there is no response, it could be that the network is down or user misconfigures the address (IP address, Domain Name or UDP port number) ')
xgcpMGCCfgUDPPort = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpMGCCfgUDPPort.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgUDPPort.setDescription('This object is used to configure the UDP port of the Media Gateway Controller. The UDP port is used together with xgcpMGCCfgAddress to specify the destination address of the default Media Gateway Controller to which RSIP message is sent when system starts up or line goes up. ')
xgcpMGCCfgConnStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("connected", 2), ("connecting", 3), ("noSuchName", 4), ("noResponse", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpMGCCfgConnStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgConnStatus.setDescription('This object is used to specify the connection status of the Default Media Gateway Controller. When sending RSIP to default Media Gateway Controller, there could be the following status: unknown - undefined stauts. connected - RSIP sent and response to it is received. connecting - RSIP is sent and waiting for response. noSuchName - no domain name/ip address is found when checking the DNS for the domain name entered in xgcpMGCCfgAddress. No RSIP message is sent. noResponse - timeout on RSIP message. The possible casues for no response on RSIP message: 1) Address(IP Address/Domain Name and UDP) for the default MGC is correct but MGC in not up or network is down. 2) MGC is up but at a different address (IP Address/ Domain Name) 3) MGC is up and at the same address(IP address/ Domain Name) but wrong UDP port. 4) MGC is down and address is wrong. ')
xgcpMGCCfgTimeStamp = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpMGCCfgTimeStamp.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgTimeStamp.setDescription('This object contains the time stamp of state transition of xgcpMGCCfgConnStatus. ')
xgcpCapabilityPackageTable = MibTable((1, 3, 6, 1, 3, 90, 1, 3, 1), )
if mibBuilder.loadTexts: xgcpCapabilityPackageTable.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageTable.setDescription('This table contains XGCP capability packages. The Capability Package table - This table is used to specify the availability of the packages. The Capabality Package Name is used as the index for the table. Each entry contains a CapabilityPackageEnable object. It is used to enable/disable a package on the Media Gateway. ')
xgcpCapabilityPackageEntry = MibTableRow((1, 3, 6, 1, 3, 90, 1, 3, 1, 1), ).setIndexNames((1, "XGCP-MIB", "xgcpCapabilityPackageName"))
if mibBuilder.loadTexts: xgcpCapabilityPackageEntry.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageEntry.setDescription('The entry specifies the availability of the XGCP package. Each entry is created when the MGCP software detects a new package. The entry goes away only if the package is removed. ')
xgcpCapabilityPackageName = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setReference(' Media Gateway Control Protocol (MGCP), version 0.1 draft, Feb 1, 1999 : Section 6.1 ')
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setDescription(' This object specifies the Name of the Capability Package. The list of basic packages includes the following: _________________________________________ | Package | name | |______________________________|_________| | Generic Media Package | G | | DTMF package | D | | MF Package | M | | Trunk Package | T | | Line Package | L | | Handset Package | H | | RTP Package | R | | Netwark Access Server Package| N | | Announcement Server Package | A | | Script Package | S | |______________________________|_________| ')
xgcpCapabilityPackageEnable = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpCapabilityPackageEnable.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageEnable.setDescription(' This object eables/disables the Package Capability ')
xgcpDefaultPackage = MibScalar((1, 3, 6, 1, 3, 90, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpDefaultPackage.setReference(' Media Gateway Control Protocol (MGCP), version 0.1 draft, Feb 1, 1998 : Section 2.1.6 ')
if mibBuilder.loadTexts: xgcpDefaultPackage.setStatus('current')
if mibBuilder.loadTexts: xgcpDefaultPackage.setDescription(' This object contains the default package name for the MGCP/SGCP protocol and it should have the same value as xgcpCapabilityPackageName. ')
xgcpLowerBoundForPacketLoss = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForPacketLoss.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForPacketLoss.setDescription('This object specifies the lower bound for voice quality packet loss per 100,000 packets. Voice quality packet loss may happen due to network congestion or due to network overload. When packet loss(number of packet per 100,000) is high enough to reach lower bound(e.g. 1500) and then higher bound(e.g. 2500) the first time, a MGCP/SGCP Notify message is sent to the Media Gateway Controller. Subsequent hits of the higher bound results in a MGCP/SGCP Notify message being sent to the Media Gateway Controller only after the lower bound is hit. | Ntfy | Ntfy Ntfy | Ntfy | | | v | | v v * * v + * * * * * * * * <--- higher bound | * * * * * * * * * + * * * * * <---- lower bound | * * | * * |* +------------------------------------ The default value of this object is 1000. ')
xgcpHigherBoundForPacketLoss = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5000, 25000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForPacketLoss.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForPacketLoss.setDescription('This object specifies the higher bound for voice quality packet loss per 100,000 packets. Voice quality packet loss may happen due to network congestion or due to network overload. The default value of this object is 10,000. ')
xgcpLowerBoundForJitter = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 60))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForJitter.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForJitter.setDescription('This object is the lower bound for Quality Alert for Jitter. Jitter is an estimate of the statistical variance of the RTP data packet interval-rival time measured in milliseconds and expressed as an unsigned integer. When jitter(milliseconds) is long enough to reach lower bound(e.g.30 ) and then higher bound(e.g. 150) the first time, a MGCP/SGCP Notify message is sent to the Media Gateway Controller. Subsequent hits of the higher bound results in a MGCP/SGCP Notify message being sent to the Media Gateway Controller only after the lower bound is hit. The default value of this object is 30. ')
xgcpHigherBoundForJitter = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 200))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForJitter.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForJitter.setDescription('This object is the higher bound for Quality Alert for Jitter. Jitter is an estimate of the statistical variance of the RTP data packet interval-rival time measured in milliseconds and expressed as an unsigned integer. The default value of this object is 150. ')
xgcpLowerBoundForLatency = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(125, 200))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForLatency.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForLatency.setDescription('This object is the higher bound for Quality Alert for latency. QA latency is an estimate of the network delay, expressed in milliseconds. This is the average value of the difference between the Network Time Protocol (NTP) timestamp indicated by the senders of the RTCP messages and the NTP timestamp of the receivers, measured when these messages are received. When latency (milliseconds) is long enough to reach lower bound (e.g.150 ) and then higher bound(e.g. 300) the first time, a MGCP/SGCP Notify message is sent to the Media Gateway Controller. Subsequent hits of the higher bound results in a MGCP/SGCP Notify message being sent to the Media Gateway Controller only after the lower bound is hit. The default value of this object is 150. ')
xgcpHigherBoundForLatency = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 400))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForLatency.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForLatency.setDescription('This object is the higher bound for Quality Alert for latency. QA latency is an estimate of the network delay, expressed in milliseconds. This is the average value of the difference between the NTP timestamp indicated by the senders of the RTCP messages and the NTP timestamp of the receivers, measured when these messages are received. The default value of this object is 300. ')
xgcpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 3, 90, 2))
xgcpNotifications = MibIdentifier((1, 3, 6, 1, 3, 90, 2, 0))
xgcpUpDownNotification = NotificationType((1, 3, 6, 1, 3, 90, 2, 0, 1)).setObjects(("XGCP-MIB", "xgcpOperStatus"))
if mibBuilder.loadTexts: xgcpUpDownNotification.setStatus('current')
if mibBuilder.loadTexts: xgcpUpDownNotification.setDescription('This notification is sent when the protocol status changes between up and down. The following information is returned: xgcpOperStatus -> Current operational status of XGCP ')
xgcpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 90, 3))
xgcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 90, 3, 1))
xgcpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 90, 3, 2))
xgcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 90, 3, 1, 1)).setObjects(("XGCP-MIB", "xgcpCoreGroup"), ("XGCP-MIB", "xgcpExtensionGroup"), ("XGCP-MIB", "xgcpPackageGroup"), ("XGCP-MIB", "xgcpVoiceQualityGroup"), ("XGCP-MIB", "xgcpDefaultMGCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpMIBCompliance = xgcpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: xgcpMIBCompliance.setDescription('The compliance statement for the SNMPv2 entities which implement XGCP.')
xgcpCoreGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 1)).setObjects(("XGCP-MIB", "xgcpInBadVersions"), ("XGCP-MIB", "xgcpRequestTimeOut"), ("XGCP-MIB", "xgcpRequestRetries"), ("XGCP-MIB", "xgcpAdminStatus"), ("XGCP-MIB", "xgcpOperStatus"), ("XGCP-MIB", "xgcpUnRecognizedPackets"), ("XGCP-MIB", "xgcpSuccessMessages"), ("XGCP-MIB", "xgcpFailMessages"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpCoreGroup = xgcpCoreGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpCoreGroup.setDescription('This group contains core objects for SGCP/MGCP on the Media Gateway Controller and the Media Gateway. ')
xgcpExtensionGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 2)).setObjects(("XGCP-MIB", "xgcpRestartInProgressMWD"), ("XGCP-MIB", "xgcpRestartDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpExtensionGroup = xgcpExtensionGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpExtensionGroup.setDescription('This group contains extension objects for MGCP on the Media Gateway. ')
xgcpPackageGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 3)).setObjects(("XGCP-MIB", "xgcpCapabilityPackageEnable"), ("XGCP-MIB", "xgcpDefaultPackage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpPackageGroup = xgcpPackageGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpPackageGroup.setDescription('This group contains package objects for MGCP on the Media Gateway or the Media Gateway Controller. ')
xgcpVoiceQualityGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 4)).setObjects(("XGCP-MIB", "xgcpLowerBoundForPacketLoss"), ("XGCP-MIB", "xgcpHigherBoundForPacketLoss"), ("XGCP-MIB", "xgcpLowerBoundForJitter"), ("XGCP-MIB", "xgcpHigherBoundForJitter"), ("XGCP-MIB", "xgcpLowerBoundForLatency"), ("XGCP-MIB", "xgcpHigherBoundForLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpVoiceQualityGroup = xgcpVoiceQualityGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpVoiceQualityGroup.setDescription('This group contains voice quality objects for the Media Gateway .')
xgcpDefaultMGCGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 5)).setObjects(("XGCP-MIB", "xgcpMGCCfgAddress"), ("XGCP-MIB", "xgcpMGCCfgUDPPort"), ("XGCP-MIB", "xgcpMGCCfgConnStatus"), ("XGCP-MIB", "xgcpMGCCfgTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpDefaultMGCGroup = xgcpDefaultMGCGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpDefaultMGCGroup.setDescription('This group contains address objects for default Media Gateway Controller. ')
mibBuilder.exportSymbols("XGCP-MIB", xgcpMIBGroups=xgcpMIBGroups, xgcpNotifications=xgcpNotifications, xgcpInBadVersions=xgcpInBadVersions, xgcpMsgStatTable=xgcpMsgStatTable, xgcpMGCCfgConnStatus=xgcpMGCCfgConnStatus, xgcpDefaultPackage=xgcpDefaultPackage, xgcpCoreObjects=xgcpCoreObjects, xgcpLowerBoundForJitter=xgcpLowerBoundForJitter, xgcpIPAddress=xgcpIPAddress, xgcpRestartInProgressMWD=xgcpRestartInProgressMWD, xgcpHigherBoundForPacketLoss=xgcpHigherBoundForPacketLoss, xgcpAdminStatus=xgcpAdminStatus, xgcpFailMessages=xgcpFailMessages, xgcpVoiceQualityObjects=xgcpVoiceQualityObjects, xgcpCapabilityPackageEntry=xgcpCapabilityPackageEntry, xgcpHigherBoundForJitter=xgcpHigherBoundForJitter, xgcpUpDownNotification=xgcpUpDownNotification, xgcpObjects=xgcpObjects, xgcpExtensionGroup=xgcpExtensionGroup, xgcpLowerBoundForPacketLoss=xgcpLowerBoundForPacketLoss, xgcpRestartDelay=xgcpRestartDelay, xgcpCapabilityPackageEnable=xgcpCapabilityPackageEnable, xgcpSuccessMessages=xgcpSuccessMessages, xgcpDefaultMGCGroup=xgcpDefaultMGCGroup, xgcpCoreGroup=xgcpCoreGroup, xgcpRequestRetries=xgcpRequestRetries, xgcpMIB=xgcpMIB, xgcpMIBCompliances=xgcpMIBCompliances, xgcpMGCCfgTimeStamp=xgcpMGCCfgTimeStamp, xgcpNotificationPrefix=xgcpNotificationPrefix, xgcpDefaultMGCObjects=xgcpDefaultMGCObjects, xgcpMIBConformance=xgcpMIBConformance, PYSNMP_MODULE_ID=xgcpMIB, xgcpPackageObjects=xgcpPackageObjects, xgcpRequestTimeOut=xgcpRequestTimeOut, xgcpMGCCfgAddress=xgcpMGCCfgAddress, xgcpMsgStatEntry=xgcpMsgStatEntry, xgcpMIBCompliance=xgcpMIBCompliance, xgcpCapabilityPackageTable=xgcpCapabilityPackageTable, xgcpMGCCfgUDPPort=xgcpMGCCfgUDPPort, xgcpPackageGroup=xgcpPackageGroup, xgcpUnRecognizedPackets=xgcpUnRecognizedPackets, xgcpExtensionObjects=xgcpExtensionObjects, xgcpLowerBoundForLatency=xgcpLowerBoundForLatency, xgcpHigherBoundForLatency=xgcpHigherBoundForLatency, xgcpOperStatus=xgcpOperStatus, xgcpVoiceQualityGroup=xgcpVoiceQualityGroup, xgcpCapabilityPackageName=xgcpCapabilityPackageName)
