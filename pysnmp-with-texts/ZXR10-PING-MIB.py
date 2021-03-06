#
# PySNMP MIB module ZXR10-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-PING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, IpAddress, MibIdentifier, Counter32, mgmt, Unsigned32, ModuleIdentity, iso, Counter64, Bits, experimental, TimeTicks, enterprises, ObjectIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "Counter32", "mgmt", "Unsigned32", "ModuleIdentity", "iso", "Counter64", "Bits", "experimental", "TimeTicks", "enterprises", "ObjectIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
zxr10L2vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L2vpn")
zxr10PingMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2))
class DisplayString(OctetString):
    pass

zxr10PingTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1), )
if mibBuilder.loadTexts: zxr10PingTable.setStatus('current')
if mibBuilder.loadTexts: zxr10PingTable.setDescription('ping information table.')
zxr10pingCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1), ).setIndexNames((0, "ZXR10-PING-MIB", "zxr10PingCommonSerial"))
if mibBuilder.loadTexts: zxr10pingCommonEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10pingCommonEntry.setDescription('')
zxr10PingCommonSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommonSerial.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonSerial.setDescription('')
zxr10PingCommonPingType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("common", 0), ("mng", 1), ("vrf", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonPingType.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonPingType.setDescription('ping type,default:common ')
zxr10PingCommonDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonDestAddr.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonDestAddr.setDescription('target IP address ')
zxr10PingCommonVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonVrfName.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonVrfName.setDescription('vrf name ')
zxr10PingCommonIfOption = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("option", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonIfOption.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonIfOption.setDescription('option,default:none ')
zxr10PingCommonPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonPacketCount.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonPacketCount.setDescription('repeat count,default:5 ')
zxr10PingCommonTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonTimeOut.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonTimeOut.setDescription('timeout in seconds,default:2 ')
zxr10PingCommonDataLen = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(36, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonDataLen.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonDataLen.setDescription('datagram size,default: 100')
zxr10PingCommonIfExtOption = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("extcom", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonIfExtOption.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonIfExtOption.setDescription('extended commands,default:none ')
zxr10PingCommonExtSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtSourceAddr.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtSourceAddr.setDescription('source address ')
zxr10PingCommonExtTos = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtTos.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtTos.setDescription('type of service,default:0 ')
zxr10PingCommonExtTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtTTL.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtTTL.setDescription('time to live,default:255 ')
zxr10PingCommonExtFragement = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtFragement.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtFragement.setDescription("set DONT FRAG(0--may frag,1--don't frag) ")
zxr10PingCommonExtOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("loose", 1), ("record", 2), ("strict", 3), ("timestamp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpType.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpType.setDescription('extended commands ')
zxr10PingCommonExtOpIpAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr1.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr1.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr2.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr2.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr3.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr3.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr4.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr4.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr5.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr5.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr6.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr6.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr7.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr7.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 22), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr8.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr8.setDescription(' ip address ')
zxr10PingCommonExtOpIpAddr9 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 23), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr9.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpIpAddr9.setDescription(' ip address ')
zxr10PingCommonExtOpRecordNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpRecordNum.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpRecordNum.setDescription('number of hops')
zxr10PingCommonExtOpTimestampNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonExtOpTimestampNum.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonExtOpTimestampNum.setDescription('number of hops')
zxr10PingCommonRosStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("not-active", 1), ("start-ping", 2), ("ping-processing", 3), ("ping-completed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonRosStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonRosStatus.setDescription(' port members ')
zxr10PingCommonEntryOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 27), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonEntryOwner.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonEntryOwner.setDescription(' port members ')
zxr10PingCommonTrapOncompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 28), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10PingCommonTrapOncompletion.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommonTrapOncompletion.setDescription(' ')
zxr10PingResultTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2), )
if mibBuilder.loadTexts: zxr10PingResultTable.setStatus('current')
if mibBuilder.loadTexts: zxr10PingResultTable.setDescription('ping result table.')
zxr10pingResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1), ).setIndexNames((0, "ZXR10-PING-MIB", "zxr10PingCommResultSerial"))
if mibBuilder.loadTexts: zxr10pingResultEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10pingResultEntry.setDescription('')
zxr10PingCommResultSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultSerial.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultSerial.setDescription('')
zxr10PingCommResultSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultSentPkts.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultSentPkts.setDescription('send packet')
zxr10PingCommResultRcvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRcvPkts.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRcvPkts.setDescription('receive packet')
zxr10PingCommResultRoundTripMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripMinTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripMinTime.setDescription('min RTT')
zxr10PingCommResultRoundTripMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripMaxTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripMaxTime.setDescription('max RTT')
zxr10PingCommResultRoundTripAvgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripAvgTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundTripAvgTime.setDescription('average RTT')
zxr10PingCommExtResultTimeStampInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommExtResultTimeStampInfo.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommExtResultTimeStampInfo.setDescription('timestamp')
zxr10PingCommExtResultIpAddrInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommExtResultIpAddrInfo.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommExtResultIpAddrInfo.setDescription('ip address')
zxr10PingCommResultEntryOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultEntryOwner.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultEntryOwner.setDescription('')
zxr10PingCommResultRoundWobbleMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleMinTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleMinTime.setDescription('min wobble time')
zxr10PingCommResultRoundWobbleMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleMaxTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleMaxTime.setDescription('max wobble time')
zxr10PingCommResultRoundWobbleAvgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleAvgTime.setStatus('current')
if mibBuilder.loadTexts: zxr10PingCommResultRoundWobbleAvgTime.setDescription('average wobble time')
pingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 3))
pingTrapResult = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 3, 1)).setObjects(("ZXR10-PING-MIB", "zxr10PingCommResultSerial"), ("ZXR10-PING-MIB", "zxr10PingCommResultSentPkts"), ("ZXR10-PING-MIB", "zxr10PingCommResultRcvPkts"), ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripMinTime"), ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripMaxTime"), ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripAvgTime"))
if mibBuilder.loadTexts: pingTrapResult.setStatus('current')
if mibBuilder.loadTexts: pingTrapResult.setDescription("The newMaster trap indicates that the sending agent has transitioned to 'Master' state.")
mibBuilder.exportSymbols("ZXR10-PING-MIB", pingNotifications=pingNotifications, zxr10PingCommonExtOpRecordNum=zxr10PingCommonExtOpRecordNum, zxr10PingCommResultRoundWobbleAvgTime=zxr10PingCommResultRoundWobbleAvgTime, zxr10PingCommResultRoundTripAvgTime=zxr10PingCommResultRoundTripAvgTime, zxr10PingCommonExtOpIpAddr6=zxr10PingCommonExtOpIpAddr6, zxr10PingCommonExtOpIpAddr1=zxr10PingCommonExtOpIpAddr1, zxr10PingResultTable=zxr10PingResultTable, zxr10PingCommExtResultTimeStampInfo=zxr10PingCommExtResultTimeStampInfo, zxr10PingCommonExtOpType=zxr10PingCommonExtOpType, zxr10PingCommResultRoundTripMinTime=zxr10PingCommResultRoundTripMinTime, zxr10PingCommonPacketCount=zxr10PingCommonPacketCount, zxr10PingCommonExtOpIpAddr8=zxr10PingCommonExtOpIpAddr8, zxr10PingCommResultSentPkts=zxr10PingCommResultSentPkts, zxr10PingCommonTimeOut=zxr10PingCommonTimeOut, zxr10PingCommonIfOption=zxr10PingCommonIfOption, zxr10PingCommonExtOpIpAddr9=zxr10PingCommonExtOpIpAddr9, zxr10PingCommResultRoundWobbleMinTime=zxr10PingCommResultRoundWobbleMinTime, zxr10PingCommonIfExtOption=zxr10PingCommonIfExtOption, pingTrapResult=pingTrapResult, zxr10PingCommResultRoundTripMaxTime=zxr10PingCommResultRoundTripMaxTime, zxr10PingCommonExtOpIpAddr3=zxr10PingCommonExtOpIpAddr3, zxr10PingCommonExtOpIpAddr2=zxr10PingCommonExtOpIpAddr2, zxr10PingMIB=zxr10PingMIB, zxr10PingTable=zxr10PingTable, zxr10PingCommonRosStatus=zxr10PingCommonRosStatus, zxr10PingCommonSerial=zxr10PingCommonSerial, zxr10PingCommonExtOpIpAddr4=zxr10PingCommonExtOpIpAddr4, zxr10PingCommonExtOpIpAddr5=zxr10PingCommonExtOpIpAddr5, zxr10PingCommResultSerial=zxr10PingCommResultSerial, zxr10PingCommResultRcvPkts=zxr10PingCommResultRcvPkts, zxr10PingCommonEntryOwner=zxr10PingCommonEntryOwner, zxr10PingCommonExtFragement=zxr10PingCommonExtFragement, zxr10PingCommonExtOpIpAddr7=zxr10PingCommonExtOpIpAddr7, zxr10PingCommonTrapOncompletion=zxr10PingCommonTrapOncompletion, zxr10pingCommonEntry=zxr10pingCommonEntry, zxr10PingCommResultRoundWobbleMaxTime=zxr10PingCommResultRoundWobbleMaxTime, zxr10PingCommResultEntryOwner=zxr10PingCommResultEntryOwner, zxr10PingCommonPingType=zxr10PingCommonPingType, zxr10PingCommonVrfName=zxr10PingCommonVrfName, zxr10PingCommonDataLen=zxr10PingCommonDataLen, zxr10PingCommonExtOpTimestampNum=zxr10PingCommonExtOpTimestampNum, zxr10PingCommonExtTos=zxr10PingCommonExtTos, zxr10PingCommExtResultIpAddrInfo=zxr10PingCommExtResultIpAddrInfo, zxr10PingCommonExtSourceAddr=zxr10PingCommonExtSourceAddr, zxr10PingCommonExtTTL=zxr10PingCommonExtTTL, zxr10pingResultEntry=zxr10pingResultEntry, DisplayString=DisplayString, zxr10PingCommonDestAddr=zxr10PingCommonDestAddr)
