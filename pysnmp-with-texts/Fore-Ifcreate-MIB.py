#
# PySNMP MIB module Fore-Ifcreate-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Ifcreate-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifExtensions, = mibBuilder.importSymbols("Fore-Common-MIB", "ifExtensions")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter64, iso, NotificationType, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, Bits, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter64", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention, RowStatus, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TestAndIncr")
foreIfcreateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 17, 5))
if mibBuilder.loadTexts: foreIfcreateMIB.setLastUpdated('9704011044-0400')
if mibBuilder.loadTexts: foreIfcreateMIB.setOrganization('FORE')
if mibBuilder.loadTexts: foreIfcreateMIB.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreIfcreateMIB.setDescription('This MIB module defines an ifCreateTable to facilitates the creation of FR/ATM and FUNI services. It also defines an ifConversionTable to allow the conversion between service id and service ifindex.')
ifReserveNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 17, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifReserveNextIndex.setStatus('current')
if mibBuilder.loadTexts: ifReserveNextIndex.setDescription('The next available IfIndex for service creation.')
ifCreateTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 17, 2), )
if mibBuilder.loadTexts: ifCreateTable.setStatus('current')
if mibBuilder.loadTexts: ifCreateTable.setDescription('The Interface creation table')
ifCreateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1), ).setIndexNames((0, "Fore-Ifcreate-MIB", "ifCreateIfIndex"))
if mibBuilder.loadTexts: ifCreateEntry.setStatus('current')
if mibBuilder.loadTexts: ifCreateEntry.setDescription('Entry associated with IfCreate table entry.')
ifCreateIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCreateIfIndex.setStatus('current')
if mibBuilder.loadTexts: ifCreateIfIndex.setDescription('The interface index of this service.')
ifCreateIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107))).clone(namedValues=NamedValues(("otherIfType", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10), ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1e1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54), ("ieee80212", 55), ("fibreChannel", 56), ("hippiInterface", 57), ("frameRelayInterconnect", 58), ("aflane8023", 59), ("aflane8025", 60), ("cctEmul", 61), ("fastEther", 62), ("isdn", 63), ("v11", 64), ("v36", 65), ("g703at64k", 66), ("g703at2mb", 67), ("qllc", 68), ("fastEtherFX", 69), ("channel", 70), ("ieee80211", 71), ("ibm370parChan", 72), ("escon", 73), ("dlsw", 74), ("isdns", 75), ("isdnu", 76), ("lapd", 77), ("ipSwitch", 78), ("rsrb", 79), ("atmLogical", 80), ("ds0", 81), ("ds0Bundle", 82), ("bsc", 83), ("async", 84), ("cnr", 85), ("iso88025Dtr", 86), ("eplrs", 87), ("arap", 88), ("propCnls", 89), ("hostPad", 90), ("termPad", 91), ("frameRelayMPI", 92), ("x213", 93), ("adsl", 94), ("radsl", 95), ("sdsl", 96), ("vdsl", 97), ("iso88025CRFPInt", 98), ("myrinet", 99), ("voiceEM", 100), ("voiceFXO", 101), ("voiceFXS", 102), ("voiceEncap", 103), ("voiceOverIp", 104), ("atmDxi", 105), ("atmFuni", 106), ("pppMultilinkBundle", 107)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateIfType.setStatus('current')
if mibBuilder.loadTexts: ifCreateIfType.setDescription('The type of the interface to be created.')
ifCreateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateRowStatus.setStatus('current')
if mibBuilder.loadTexts: ifCreateRowStatus.setDescription('This object is used to create new rows in this table, and to delete existing rows.')
ifCreateServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("underConfig", 1), ("active", 2), ("inactive", 3))).clone('inactive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateServiceStatus.setStatus('current')
if mibBuilder.loadTexts: ifCreateServiceStatus.setDescription('This object specifies the status of the service under creation. The service status is set to underConfig at the beginning of the service creation process. The service creation process is not considered completed until all the related MIB objects are set up properly. Then the service status is set to active. The default status is inactive.')
ifCreateName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateName.setStatus('current')
if mibBuilder.loadTexts: ifCreateName.setDescription('The object specifies the name assigned to the interface.')
ifCreateIfTrapSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateIfTrapSupport.setStatus('current')
if mibBuilder.loadTexts: ifCreateIfTrapSupport.setDescription('The object specifies whether interface traps should be generated for this interface.')
ifCreateServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifCreateServiceId.setStatus('current')
if mibBuilder.loadTexts: ifCreateServiceId.setDescription('The object specifies the serviceID assigned to the interface.')
ifConvertToIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 17, 3), )
if mibBuilder.loadTexts: ifConvertToIfIndexTable.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexTable.setDescription('The Interface conversion table for converting service id (i.e. board id, netmod id, port id, channel id) into service ifindex.')
ifConvertToIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1), ).setIndexNames((0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexBoardId"), (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexNetmodId"), (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexPortId"), (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexChannelId"))
if mibBuilder.loadTexts: ifConvertToIfIndexEntry.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexEntry.setDescription('An entry associated with ifConvertToIfIndex table.')
ifConvertToIfIndexBoardId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertToIfIndexBoardId.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexBoardId.setDescription('This object identifies the board id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertToIfIndexNetmodId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertToIfIndexNetmodId.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexNetmodId.setDescription('This object identifies the netmod id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertToIfIndexPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertToIfIndexPortId.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexPortId.setDescription('This object identifies the port id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertToIfIndexChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertToIfIndexChannelId.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexChannelId.setDescription('This object identifies the channel id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertToIfIndexIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertToIfIndexIfIndex.setStatus('current')
if mibBuilder.loadTexts: ifConvertToIfIndexIfIndex.setDescription('The service ifindex that is associated with this service id.')
ifConvertFmIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 17, 4), )
if mibBuilder.loadTexts: ifConvertFmIfIndexTable.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexTable.setDescription('The Interface conversion table for converting service ifindex into service id (i.e. board id, netmod id, port id, channel id).')
ifConvertFmIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1), ).setIndexNames((0, "Fore-Ifcreate-MIB", "ifConvertFmIfIndexIfIndex"))
if mibBuilder.loadTexts: ifConvertFmIfIndexEntry.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexEntry.setDescription('An entry associated with ifConvertFmIfIndex table.')
ifConvertFmIfIndexIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertFmIfIndexIfIndex.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexIfIndex.setDescription('The service ifindex that is associated with this service id.')
ifConvertFmIfIndexBoardId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertFmIfIndexBoardId.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexBoardId.setDescription('This object identifies the board id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertFmIfIndexNetmodId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertFmIfIndexNetmodId.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexNetmodId.setDescription('This object identifies the netmod id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertFmIfIndexPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertFmIfIndexPortId.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexPortId.setDescription('This object identifies the port id associated with a FUNI or FRATM service id in BNPC notation.')
ifConvertFmIfIndexChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifConvertFmIfIndexChannelId.setStatus('current')
if mibBuilder.loadTexts: ifConvertFmIfIndexChannelId.setDescription('This object identifies the channel id associated with a FUNI or FRATM service id in BNPC notation.')
mibBuilder.exportSymbols("Fore-Ifcreate-MIB", ifConvertFmIfIndexTable=ifConvertFmIfIndexTable, ifConvertToIfIndexChannelId=ifConvertToIfIndexChannelId, ifConvertFmIfIndexEntry=ifConvertFmIfIndexEntry, ifConvertToIfIndexIfIndex=ifConvertToIfIndexIfIndex, ifCreateIfType=ifCreateIfType, ifCreateIfIndex=ifCreateIfIndex, PYSNMP_MODULE_ID=foreIfcreateMIB, ifCreateIfTrapSupport=ifCreateIfTrapSupport, ifConvertToIfIndexPortId=ifConvertToIfIndexPortId, ifConvertFmIfIndexNetmodId=ifConvertFmIfIndexNetmodId, ifCreateRowStatus=ifCreateRowStatus, foreIfcreateMIB=foreIfcreateMIB, ifCreateServiceStatus=ifCreateServiceStatus, ifCreateEntry=ifCreateEntry, ifConvertToIfIndexBoardId=ifConvertToIfIndexBoardId, ifCreateName=ifCreateName, ifReserveNextIndex=ifReserveNextIndex, ifConvertFmIfIndexBoardId=ifConvertFmIfIndexBoardId, ifConvertToIfIndexEntry=ifConvertToIfIndexEntry, ifCreateTable=ifCreateTable, ifConvertFmIfIndexPortId=ifConvertFmIfIndexPortId, ifConvertFmIfIndexChannelId=ifConvertFmIfIndexChannelId, ifCreateServiceId=ifCreateServiceId, ifConvertToIfIndexNetmodId=ifConvertToIfIndexNetmodId, ifConvertToIfIndexTable=ifConvertToIfIndexTable, ifConvertFmIfIndexIfIndex=ifConvertFmIfIndexIfIndex)
