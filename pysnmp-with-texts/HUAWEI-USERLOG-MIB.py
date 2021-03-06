#
# PySNMP MIB module HUAWEI-USERLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-USERLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, iso, MibIdentifier, Bits, Counter32, TimeTicks, ObjectIdentity, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "MibIdentifier", "Bits", "Counter32", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwUserLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18))
if mibBuilder.loadTexts: hwUserLogMIB.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hwUserLogMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwUserLogMIB.setContactInfo(' R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwUserLogMIB.setDescription('The HUAWEI-USERLOG-MIB contains objects to manage configuration and monitor running state for userlog feature. For users who access network through NAT and BAS equipments, their IP addresses are generally unfixed, and so it is hard to exactly locate which host a certain access comes from and which user initiates it. This decreases the network security. User log is designed to solve the problem. User log can record Network Address Translation (NAT) flow information, and login/ logout information and flow information of Broadband Access Server (BAS) user, thus enabling the administrator know address information before NAT, access record of BAS user, etc. Then, network activities and operations can be queried and tracked, and network availability and security are improved accordingly.')
hwUserlogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1))
hwUserlogNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1))
hwUserlogNatVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatVersion.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatVersion.setDescription('NAT LOG version. Currently only version 1 is developed.')
hwUserlogNatSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSyslog.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSyslog.setDescription('NAT LOG format. If 1, LOG format is sysLog. If 0, LOG format is UDP packet. UDP packet is the default format and is recommended. Syslog can be used in the case that log amount is not too large.')
hwUserlogNatSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSourceIP.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSourceIP.setDescription('The Source IP address of NAT LOG UDP packet. By default, the source IP address of the UDP packet is the IP address of the interface through which the router outputs the user log packet. On the user log server side, the source of log information can be located rapidly through identifying the source IP address of the log. You are recommended to configure a loopback address or router ID to function as the source IP address of the UDP packet.')
hwUserlogNatFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatFlowBegin.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatFlowBegin.setDescription('Log the NAT flow when it is created. If 1, this function is enabled. If 0, this function is disabled. This function will be used when real-time monitor is required. The default value 0 means this function is disabled.')
hwUserlogNatActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatActiveTime.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatActiveTime.setDescription('The active time for long-time existed NAT flow. Unit: minute. Range: 10 minutes ~ 120 minutes. When setting it, NAT flow can be logged after an interval of active time. This function will be used when real-time monitor is required. The default value 0 means real-time monitor function is disabled. ')
hwUserlogNatSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6), )
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoTable.setDescription('A table of NAT LOG configuration information for the specified slot. By default, user log function is disabled on the interface board. Only after user log function is enabled, the other configurations related to user log take effect.')
hwUserlogNatSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoEntry.setDescription('NAT LOG configuration information entry for a slot.')
hwUserlogNatCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatCfgSlotNumber.setDescription('Slot number. The object specifies which slot is configured with NAT LOG. For NAT LOG, it is the slot of the egress interface configured with NAT.')
hwUserlogNatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatEnable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatEnable.setDescription('The NAT LOG feature status. If 1, NAT LOG is enabled. If 0, NAT LOG is disabled. The default value 0 means NAT LOG is disabled.')
hwUserlogNatAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatAclNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatAclNumber.setDescription('Access-list number. Its range is 2000 ~ 3999. The value 0 means no ACL is specified. Only when NAT LOG is enabled, and ACL is configured. Only NAT flow which match the ACL will be logged. ')
hwUserlogNatHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatHostAddress.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatHostAddress.setDescription('The IP address of NAT LOG server. If user log is output in UDP packet mode, user log server must be configured and user log server address must be specified correctly. Otherwise, user log function cannot work normally. The address of the destination server must be a valid unicast address rather than a loop address or multicast address. In principle, it should be the address of the user log server that can communicate normally.')
hwUserlogNatUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatUdpPort.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatUdpPort.setDescription('The UDP Port Number of NAT LOG server. Its range is 1 ~ 65535. In order to avoid confliction with general UDP port numbers, you are recommended to use the UDP port number above 1024.')
hwUserlogNatSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7), )
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoTable.setDescription('A table of NAT LOG running information for the specified slot.')
hwUserlogNatSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogNatRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoEntry.setDescription('NAT LOG running information entry for a slot.')
hwUserlogNatRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatRunSlotNumber.setDescription('Slot number. The object specifies on which slot the NAT LOG statistics are calculated.')
hwUserlogNatTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatTotalEntries.setDescription('The total number of NAT flow entries which are logged.')
hwUserlogNatTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatTotalPackets.setDescription('The total number of NAT LOG UDP packets generated by the device.')
hwUserlogNatFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatFailedEntries.setDescription('The total number of NAT flow entries failed in outputting.')
hwUserlogNatFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatFailedPackets.setDescription('The total number of NAT LOG UDP packets failed in outputting.')
hwUserlogNatClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hwUserlogNatClearRunStat.setDescription('Clears the running statistics for NAT LOG. Its access is write-only. If 1, the running statistics for NAT LOG is resetted. Other value is invalid.')
hwUserlogFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2))
hwUserlogFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowVersion.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowVersion.setDescription('BAS FLOW LOG version. Currently only version 1 is developed.')
hwUserlogFlowSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSyslog.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSyslog.setDescription('BAS FLOW LOG format. If 1, LOG format is sysLog. If 0, LOG format is UDP packet. UDP packet is the default format, and is recommended. Syslog can be used in the case that log amount is not too large.')
hwUserlogFlowSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSourceIP.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSourceIP.setDescription('The Source IP address of BAS FLOW LOG UDP packet. By default, the source IP address of the UDP packet is the IP address of the interface through which the router outputs the user log packet. On the user log server side, the source of log information can be located rapidly through identifying the source IP address of the log. You are recommended to configure a loopback address or router ID to function as the source IP address of the UDP packet.')
hwUserlogFlowFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowFlowBegin.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowFlowBegin.setDescription('Log the BAS flow when it is created. If 1, this function is enabled. If 0, this function is disabled. This function will be used when real-time monitor is required. The default value 0 means this function is disabled.')
hwUserlogFlowActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowActiveTime.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowActiveTime.setDescription('The active time for long-time existed BAS flow. Its unit is minute. Its range is 10 minutes ~ 120 minutes. When setting it, BAS flow can be logged after an internal of active time. This function will be used when real-time monitor is required. The default value 0 means real-time monitor function is disabled. ')
hwUserlogFlowSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6), )
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoTable.setDescription('A table of BAS FLOW LOG configuration information for the specified slot. By default, user log function is disabled on the interface board. Only after user log function is enabled, the other configurations related to user log take effect.')
hwUserlogFlowSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoEntry.setDescription('BAS FLOW LOG configuration information entry for a slot.')
hwUserlogFlowCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowCfgSlotNumber.setDescription('Slot number. The ojects specifies which slot is configured with BAS FLOW LOG. ')
hwUserlogFlowEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowEnable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowEnable.setDescription('The BAS FLOW LOG feature status. If 1, BAS FLOW LOG is enabled. If 0, BAS FLOW LOG is disabled. The default value 0 means BAS FLOW LOG is disabled.')
hwUserlogFlowAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowAclNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowAclNumber.setDescription('Access-list number. Its range is 2000 ~ 3999. The value 0 means no ACL is specified. Only when BAS FLOW LOG is enabled, the ACL be configured. Only BAS flow which match the ACL will be logged. ')
hwUserlogFlowHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowHostAddress.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowHostAddress.setDescription('The IP address of BAS FLOW LOG server. If user log is output in UDP packet mode, user log server must be configured and user log server address must be specified correctly. Otherwise, user log function cannot work normally. The address of the destination server must be a valid unicast address rather than a loop address or multicast address. In principle, it should be the address of the user log server that can communicate normally.')
hwUserlogFlowUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowUdpPort.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowUdpPort.setDescription('The UDP Port Number of BAS FLOW LOG server. Its range is 1 ~ 65535. In order to avoid confliction with general UDP port numbers, you are recommended to use the UDP port number above 1024.')
hwUserlogFlowSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7), )
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoTable.setDescription('A table of BAS FLOW LOG running information for the specified slot.')
hwUserlogFlowSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogFlowRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoEntry.setDescription('Running Information Entry for a slot.')
hwUserlogFlowRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowRunSlotNumber.setDescription('Slot number. The object specifies on which slot the BAS FLOW LOG statistics are calculated.')
hwUserlogFlowTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowTotalEntries.setDescription('The total number of BAS FLOW Entries which are logged. ')
hwUserlogFlowTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowTotalPackets.setDescription('The total number of FLOW LOG UDP packet generated by the device. ')
hwUserlogFlowFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowFailedEntries.setDescription('The total number of BAS FLOW entries failed in outputting. ')
hwUserlogFlowFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowFailedPackets.setDescription('The total number of BAS FLOW LOG UDP packet failed in outputting.')
hwUserlogFlowClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 2, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hwUserlogFlowClearRunStat.setDescription('Clears the running statistics for FLOW LOG. Its access is write-only. If 1, the running statistics for FLOW LOG is resetted. Other value is invalid.')
hwUserlogAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3))
hwUserlogAccessVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessVersion.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessVersion.setDescription('BAS ACCESS LOG version. Currently only version 1 is developed.')
hwUserlogAccessSyslog = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSyslog.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSyslog.setDescription('BAS ACCESS LOG format. If 1, LOG format is sysLog; If 0, LOG format is UDP packet. UDP packet is the default format, and is recommended. Syslog can be used in the case that log amount is not too large.')
hwUserlogAccessSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSourceIP.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSourceIP.setDescription('The Source IP address of BAS ACCESS LOG UDP packet. By default, the source IP address of the UDP packet is the IP address of the interface through which the router outputs the user log packet. On the user log server side, the source of log information can be located rapidly through identifying the source IP address of the log. You are recommended to configure a loopback address or router ID to function as the source IP address of the UDP packet.')
hwUserlogAccessSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4), )
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoTable.setDescription('A table of BAS ACCESS LOG configuration information for the specified slot.')
hwUserlogAccessSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoEntry.setDescription('BAS ACCESS LOG configuration information entry for a slot.')
hwUserlogAccessCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessCfgSlotNumber.setDescription('Slot number. The object specifies which slot is configured with BAS ACCESS LOG. ')
hwUserlogAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessEnable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessEnable.setDescription('The BAS ACCESS LOG feature status. If 1, BAS ACCESS LOG is enabled. If 0, BAS ACCESS LOG is disabled. The default value 0 means BAS ACCESS LOG is disabled.')
hwUserlogAccessHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessHostAddress.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessHostAddress.setDescription('The IP address of BAS ACCESS LOG server. If user log is output in UDP packet mode, user log server must be configured and user log server address must be specified correctly. Otherwise, user log function cannot work normally. The address of the destination server must be a valid unicast address rather than a loop address or multicast address. In principle, it should be the address of the user log server that can communicate normally.')
hwUserlogAccessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessUdpPort.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessUdpPort.setDescription('The UDP Port Number of BAS ACCESS LOG server. Its range is 1 ~ 65535. In order to avoid confliction with general UDP port numbers, you are recommended to use the UDP port number above 1024.')
hwUserlogAccessSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5), )
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoTable.setDescription('A table of BAS ACCESS LOG running information for the specified slot.')
hwUserlogAccessSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1), ).setIndexNames((0, "HUAWEI-USERLOG-MIB", "hwUserlogAccessRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoEntry.setDescription('Running Information Entry for a slot.')
hwUserlogAccessRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessRunSlotNumber.setDescription('Slot number. The object specifies on which slot the BAS ACCESS LOG statistics are calculated.')
hwUserlogAccessTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessTotalEntries.setDescription('The total number of BAS ACCESS records which are logged. ')
hwUserlogAccessTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessTotalPackets.setDescription('The total number of ACCESS LOG UDP packet generated by the router.')
hwUserlogAccessFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessFailedEntries.setDescription('The total number of BAS ACCESS entries failed in outputting.')
hwUserlogAccessFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessFailedPackets.setDescription('The total number of BAS ACCESS LOG UDP packet failed in outputting.')
hwUserlogAccessClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 1, 3, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hwUserlogAccessClearRunStat.setDescription('Clear the running statistics for ACCESS LOG. Its access is write-only. If 1, the running statistics for ACCESS LOG is resetted, the other value is invalid.')
hwUserlogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 2))
hwUserlogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3))
hwUserlogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 1))
hwUserlogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 1, 1)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogCompliance = hwUserlogCompliance.setStatus('current')
if mibBuilder.loadTexts: hwUserlogCompliance.setDescription('The compliance statement for entities which implement the Huawei Userlog mib.')
hwUserlogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2))
hwUserlogMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 1)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogMandatoryGroup = hwUserlogMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: hwUserlogMandatoryGroup.setDescription('A collection of objects providing mandatory Userlog information.')
hwUserlogConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 2)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFlowBegin"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatActiveTime"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatAclNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFlowBegin"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowActiveTime"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowAclNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessVersion"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessSyslog"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessSourceIP"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogConfigGroup = hwUserlogConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hwUserlogConfigGroup.setDescription('All configurable parameters of Userlog feature.')
hwUserlogInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 18, 3, 2, 3)).setObjects(("HUAWEI-USERLOG-MIB", "hwUserlogNatTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogNatFailedPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalPackets"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedEntries"), ("HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogInfoGroup = hwUserlogInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwUserlogInfoGroup.setDescription('All running information of Userlog feature.')
mibBuilder.exportSymbols("HUAWEI-USERLOG-MIB", hwUserlogAccessRunSlotNumber=hwUserlogAccessRunSlotNumber, hwUserlogAccessHostAddress=hwUserlogAccessHostAddress, hwUserlogCompliances=hwUserlogCompliances, hwUserlogFlowSlotRunInfoTable=hwUserlogFlowSlotRunInfoTable, hwUserlogAccessTotalEntries=hwUserlogAccessTotalEntries, hwUserlogFlowVersion=hwUserlogFlowVersion, hwUserlogFlowFlowBegin=hwUserlogFlowFlowBegin, hwUserlogMandatoryGroup=hwUserlogMandatoryGroup, hwUserlogConfigGroup=hwUserlogConfigGroup, hwUserlogNatRunSlotNumber=hwUserlogNatRunSlotNumber, hwUserlogNatFailedEntries=hwUserlogNatFailedEntries, hwUserlogAccessSlotCfgInfoTable=hwUserlogAccessSlotCfgInfoTable, hwUserlogAccessUdpPort=hwUserlogAccessUdpPort, hwUserlogFlowSlotRunInfoEntry=hwUserlogFlowSlotRunInfoEntry, hwUserlogObjects=hwUserlogObjects, hwUserlogNatSourceIP=hwUserlogNatSourceIP, hwUserlogFlowHostAddress=hwUserlogFlowHostAddress, hwUserlogFlowSourceIP=hwUserlogFlowSourceIP, hwUserlogCompliance=hwUserlogCompliance, hwUserlogFlowSyslog=hwUserlogFlowSyslog, hwUserlogFlowSlotCfgInfoTable=hwUserlogFlowSlotCfgInfoTable, hwUserlogConformance=hwUserlogConformance, hwUserlogNotifications=hwUserlogNotifications, hwUserlogAccessTotalPackets=hwUserlogAccessTotalPackets, hwUserlogFlowActiveTime=hwUserlogFlowActiveTime, hwUserlogFlowTotalEntries=hwUserlogFlowTotalEntries, PYSNMP_MODULE_ID=hwUserLogMIB, hwUserlogNatAclNumber=hwUserlogNatAclNumber, hwUserlogFlowAclNumber=hwUserlogFlowAclNumber, hwUserlogFlowUdpPort=hwUserlogFlowUdpPort, hwUserlogFlowFailedEntries=hwUserlogFlowFailedEntries, hwUserlogAccessObjects=hwUserlogAccessObjects, hwUserlogAccessSyslog=hwUserlogAccessSyslog, hwUserlogAccessEnable=hwUserlogAccessEnable, hwUserlogNatFailedPackets=hwUserlogNatFailedPackets, hwUserlogNatSlotRunInfoTable=hwUserlogNatSlotRunInfoTable, hwUserlogAccessSlotRunInfoEntry=hwUserlogAccessSlotRunInfoEntry, hwUserlogNatClearRunStat=hwUserlogNatClearRunStat, hwUserlogAccessSlotRunInfoTable=hwUserlogAccessSlotRunInfoTable, hwUserlogFlowRunSlotNumber=hwUserlogFlowRunSlotNumber, hwUserlogNatObjects=hwUserlogNatObjects, hwUserlogNatCfgSlotNumber=hwUserlogNatCfgSlotNumber, hwUserlogNatHostAddress=hwUserlogNatHostAddress, hwUserlogNatActiveTime=hwUserlogNatActiveTime, hwUserlogFlowCfgSlotNumber=hwUserlogFlowCfgSlotNumber, hwUserlogFlowSlotCfgInfoEntry=hwUserlogFlowSlotCfgInfoEntry, hwUserlogAccessFailedEntries=hwUserlogAccessFailedEntries, hwUserlogAccessFailedPackets=hwUserlogAccessFailedPackets, hwUserlogNatSlotRunInfoEntry=hwUserlogNatSlotRunInfoEntry, hwUserlogNatTotalEntries=hwUserlogNatTotalEntries, hwUserlogNatTotalPackets=hwUserlogNatTotalPackets, hwUserlogFlowTotalPackets=hwUserlogFlowTotalPackets, hwUserlogAccessClearRunStat=hwUserlogAccessClearRunStat, hwUserlogFlowObjects=hwUserlogFlowObjects, hwUserlogNatUdpPort=hwUserlogNatUdpPort, hwUserlogNatSlotCfgInfoEntry=hwUserlogNatSlotCfgInfoEntry, hwUserlogAccessCfgSlotNumber=hwUserlogAccessCfgSlotNumber, hwUserlogInfoGroup=hwUserlogInfoGroup, hwUserlogFlowEnable=hwUserlogFlowEnable, hwUserlogFlowFailedPackets=hwUserlogFlowFailedPackets, hwUserlogNatSyslog=hwUserlogNatSyslog, hwUserlogNatSlotCfgInfoTable=hwUserlogNatSlotCfgInfoTable, hwUserlogNatFlowBegin=hwUserlogNatFlowBegin, hwUserlogNatEnable=hwUserlogNatEnable, hwUserLogMIB=hwUserLogMIB, hwUserlogAccessSourceIP=hwUserlogAccessSourceIP, hwUserlogGroups=hwUserlogGroups, hwUserlogNatVersion=hwUserlogNatVersion, hwUserlogAccessSlotCfgInfoEntry=hwUserlogAccessSlotCfgInfoEntry, hwUserlogFlowClearRunStat=hwUserlogFlowClearRunStat, hwUserlogAccessVersion=hwUserlogAccessVersion)
