#
# PySNMP MIB module HH3C-POS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-POS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hh3cmlsr, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cmlsr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Bits, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Unsigned32, Integer32, TimeTicks, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Unsigned32", "Integer32", "TimeTicks", "MibIdentifier", "Counter64", "IpAddress")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hh3cpos = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8))
hh3cpos.setRevisions(('2004-10-12 00:00', '2004-07-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cpos.setRevisionsDescriptions(('The lastest version of this MIB module.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: hh3cpos.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: hh3cpos.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cpos.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cpos.setDescription('The POS MIB module is used to manage POS-Access. ')
hh3cposAppTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1), )
if mibBuilder.loadTexts: hh3cposAppTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppTable.setDescription('The table to get and set the application informatin.')
hh3cposAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppEntry.setDescription('The content of hh3cposAppTable.')
hh3cposAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppId.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppId.setDescription('The ID of application.')
hh3cposAppConnectMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tcp", 1), ("flow", 2), ("pad", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppConnectMode.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppConnectMode.setDescription('The connect mode of application. If the router and unix are connected by TCP protocol, the connect mode of application is tcp. If the router and unix are connected by async interface, the connect mode of application is flow. If the router is used as POSPAD device, the connect mode of application is pad.')
hh3cposAppState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noset", 1), ("down", 2), ("up", 3), ("ok", 4), ("kept", 5), ("linking", 6), ("linked", 7))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppState.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppState.setDescription('The state of application.')
hh3cposAppIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppIfIndex.setReference('ifIndex')
if mibBuilder.loadTexts: hh3cposAppIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppIfIndex.setDescription('The interface index of the application whose connect mode is flow or pad.')
hh3cposAppHostIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppHostIP.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppHostIP.setDescription('The destination IP Address of application. Used for the application whose connect mode is tcp.')
hh3cposAppPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppPort.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppPort.setDescription('The destination port of application. Used for the application whose connect mode is tcp.')
hh3cposAppSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppSourceIp.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppSourceIp.setDescription('The source IP Address of application. Used for the application whose connect mode is tcp.')
hh3cposAppRecvPacCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppRecvPacCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppRecvPacCounter.setDescription('The number of packets received by the application.')
hh3cposAppErrPacCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppErrPacCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppErrPacCounter.setDescription('The number of error packets received by the application.')
hh3cposAppDistrErrCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppDistrErrCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDistrErrCounter.setDescription('The number of packets that could not be sent to POS.')
hh3cposAppBuffedCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppBuffedCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppBuffedCounter.setDescription('The number of packets stored in the buffer of application.')
hh3cposAppDiscardedCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppDiscardedCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDiscardedCounter.setDescription('The number of packets discarded by the application.')
hh3cposAppDebug = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("close", 1), ("open", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppDebug.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDebug.setDescription('The debugging switch of application.')
hh3cposAppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppRowStatus.setDescription('The status of row. Only support active, CreateAndGo and destroy.')
hh3cposAppX121Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAppX121Addr.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppX121Addr.setDescription('The destination X121 Address of application which is an octet string made up of numeric. Used for the application whose connect mode is pad.')
hh3cposInterTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2), )
if mibBuilder.loadTexts: hh3cposInterTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterTable.setDescription('The table to get and set the POS-Interface informatin.')
hh3cposInterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposPosId"))
if mibBuilder.loadTexts: hh3cposInterEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterEntry.setDescription('The content of hh3cposInterTable.')
hh3cposPosId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosId.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosId.setDescription('The ID of the POS-Interface.')
hh3cposPosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposPosIfIndex.setReference('ifIndex')
if mibBuilder.loadTexts: hh3cposPosIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosIfIndex.setDescription('The interface index of the POS-Interface whose type is fcm, asy or pad-client.')
hh3cposPosConnectState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noset", 1), ("down", 2), ("up", 3), ("ok", 4))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosConnectState.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosConnectState.setDescription('The state of the POS-Interface.')
hh3cposPosRecvPacCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosRecvPacCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosRecvPacCounter.setDescription('The number of packets received by the POS-Interface.')
hh3cposPosErrPacCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosErrPacCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosErrPacCounter.setDescription('The number of error packets received by the POS-Interface.')
hh3cposPosMapErrCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosMapErrCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosMapErrCounter.setDescription('The number of packets that could not be sent to application.')
hh3cposPosBuffedCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosBuffedCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosBuffedCounter.setDescription('The number of packets stored in the buffer of the POS-Interface.')
hh3cposPosDiscardedCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposPosDiscardedCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosDiscardedCounter.setDescription('The number of packets discarded by the POS-Interface.')
hh3cposPosInterDebug = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("close", 1), ("open", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposPosInterDebug.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosInterDebug.setDescription('The debugging switch of the POS-Interface.')
hh3cposPosInterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposPosInterRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosInterRowStatus.setDescription('The status of row. Only support active, CreateAndGo and destroy.')
hh3cposPosInterType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fcm", 1), ("asy", 2), ("pad-client", 3), ("pad-server", 4))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposPosInterType.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosInterType.setDescription("The type of interface. The POS-Access mode has four types: FCM-Access, ASYNC-Access, simulating POSPAD device, POSPAD-Access. FCM-Access mode means POS and router are connected through PSTN. In this case, hh3cposPosInterType should be set to fcm. ASYNC-Access mode means POS and router are connected by asynchronous cable. In this case, hh3cposPosInterType should be set to asy. Simulating POSPAD device means router connects POS through asynchronous cable and connects another router whose connect mode is pad-server through X.25 network. In this case, hh3cposPosInterType should be set to pad-client. POSPAD-Access mode means router connects POSPAD device through X.25 network. In this case, hh3cposPosInterType is pad-server. The hh3cposPosInterType can't be set to pad-server. It is autogenerated when POSPAD device initiates a connection to the router. ")
hh3cposMapTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3), )
if mibBuilder.loadTexts: hh3cposMapTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposMapTable.setDescription('The table to get and set the informatin of mapping relation of destination and application.')
hh3cposMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposMapDes"))
if mibBuilder.loadTexts: hh3cposMapEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposMapEntry.setDescription('The content of hh3cposMapTable.')
hh3cposMapDes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposMapDes.setStatus('current')
if mibBuilder.loadTexts: hh3cposMapDes.setDescription('The destination code of the mapping item. If the value is -1, it is the default item of mapping relation.')
hh3cposMapAppNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposMapAppNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cposMapAppNumber.setDescription('The application index of the mapping item.')
hh3cposMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cposMapRowStatus.setDescription('The status of row. Only support active, CreateAndGo and destroy.')
hh3cposAsyAppTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4), )
if mibBuilder.loadTexts: hh3cposAsyAppTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposAsyAppTable.setDescription('The table to get and set the asynchronous-application interface information.')
hh3cposAsyAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposAsyAppIfIndex"))
if mibBuilder.loadTexts: hh3cposAsyAppEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposAsyAppEntry.setDescription('The content of hh3cposAsyAppTable.')
hh3cposAsyAppIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAsyAppIfIndex.setReference('ifIndex')
if mibBuilder.loadTexts: hh3cposAsyAppIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cposAsyAppIfIndex.setDescription('The interface index of asynchronous-application.')
hh3cposAsyAppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposAsyAppRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cposAsyAppRowStatus.setDescription('The status of row. Only support active, CreateAndGo and destroy.')
hh3cposFCMTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5), )
if mibBuilder.loadTexts: hh3cposFCMTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMTable.setDescription('The table to get the information of FCM interface.')
hh3cposFCMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposFCMIfIndex"))
if mibBuilder.loadTexts: hh3cposFCMEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMEntry.setDescription('The content of hh3cposFCMTable.')
hh3cposFCMIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposFCMIfIndex.setReference('ifIndex')
if mibBuilder.loadTexts: hh3cposFCMIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMIfIndex.setDescription('The index of FCM interface.')
hh3cposFCMTimeoutCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposFCMTimeoutCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMTimeoutCounter.setDescription('The number that modem was hung up for timeout.')
hh3cposFCMConnectFailCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposFCMConnectFailCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMConnectFailCounter.setDescription('The number that modem could not handshake successfully.')
hh3cposAppSum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposAppSum.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppSum.setDescription('The total of configued applications.')
hh3cposInterSum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cposInterSum.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterSum.setDescription('The total of configued POS-Interfaces.')
hh3cposEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cposEnable.setDescription('To enable or diable pos-server.')
hh3cposAppDebugAll = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("close", 1), ("open", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposAppDebugAll.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDebugAll.setDescription('To open or close the debugging switch of all applications.')
hh3cposPosDebugAll = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("close", 1), ("open", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposPosDebugAll.setStatus('current')
if mibBuilder.loadTexts: hh3cposPosDebugAll.setDescription('To open or close the debugging switch of all POS-Interfaces.')
hh3cposClearPacCounter = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("counting", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposClearPacCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposClearPacCounter.setDescription('To reset all packet counters of all applicaions and POS-Interfaces.')
hh3cposClearFCMCounter = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("counting", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposClearFCMCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposClearFCMCounter.setDescription('To clear all counters of all FCM interfaces.')
hh3cposEnableTrap = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposEnableTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposEnableTrap.setDescription('To enable or disable trap switch.')
hh3cposFCMAnswerTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(500, 2000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposFCMAnswerTime.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMAnswerTime.setDescription('FCM answer time, unit:ms.')
hh3cposFCMTradeTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30000, 1200000)).clone(60000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposFCMTradeTime.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMTradeTime.setDescription('FCM trade time, unit:ms.')
hh3cposFCMPacketInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3500, 10000)).clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposFCMPacketInterval.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMPacketInterval.setDescription('FCM packet interval time, unit:ms.')
hh3cposPadWaitTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposPadWaitTime.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadWaitTime.setDescription('The time that POS-Interface needs to wait to receive another packet, unit:ms. It may be configured when router is used as POSPAD device. In other cases, It is useless.')
hh3cposPadIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposPadIdleTimeout.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadIdleTimeout.setDescription('If these is no packet transmitting through the time, the connection of POSPAD device and router whose connect mode is pad-server will be cut off. Unit:s.')
hh3cposPadPacType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("syn", 1), ("asy", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposPadPacType.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadPacType.setDescription('The type of packet.Between POSPAD device and router whose connect mode is pad-server, there are two types of packet. One is synchronous, the other is asynchronous.')
hh3cposPadCheckSChar = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cposPadCheckSChar.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadCheckSChar.setDescription('To enable or disable the checking of 10 04 characters in packet. It is used for the router which is used as POSPAD device. When the value is disable, it will check packet that just includes 10 04 charaters. If there are 10 04 packet, the router which is used as POSPAD device will disconnect from POSPAD-access router. When the value is enable, it will check 10 04 characters in packet. If there are 10 04 characters in packet, the router which is used as POSPAD device will disconnect from POSPAD-access router.')
hh3cposPadTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22), )
if mibBuilder.loadTexts: hh3cposPadTable.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadTable.setDescription('The table to enable or disable POSPAD-Access function under serial interface.')
hh3cposPadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1), ).setIndexNames((0, "HH3C-POS-MIB", "hh3cposPadIfIndex"))
if mibBuilder.loadTexts: hh3cposPadEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadEntry.setDescription('The content of hh3cposPadTable.')
hh3cposPadIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cposPadIfIndex.setReference('ifIndex')
if mibBuilder.loadTexts: hh3cposPadIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadIfIndex.setDescription('The index of serial interface.')
hh3cposPadRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cposPadRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cposPadRowStatus.setDescription('The status of row. Only support active, CreateAndGo and destroy.')
hh3cposTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17))
hh3cposAppNotReadyTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 1)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppNotReadyTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppNotReadyTrap.setDescription("The agent will send a trap when the application whose state is linked isn't ready to send or receive data. Only used for the application whose connect mode is tcp.")
hh3cposAppConnectFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 2)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppConnectFailTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppConnectFailTrap.setDescription('The agent will send a trap if router can not connect to the application.')
hh3cposAppStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 3)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"), ("HH3C-POS-MIB", "hh3cposAppState"))
if mibBuilder.loadTexts: hh3cposAppStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppStateChangeTrap.setDescription('The agent will send a trap when the state of the application is changed to down or kept.')
hh3cposAppNotConfigedTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 4)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppNotConfigedTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppNotConfigedTrap.setDescription("The agent will send a trap if the application isn't configured.")
hh3cposAppBuffOverFlowTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 5)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppBuffOverFlowTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppBuffOverFlowTrap.setDescription('The agent will send a trap if the application buffer is overflowed.')
hh3cposAppDebugOpenTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 6)).setObjects(("HH3C-POS-MIB", "hh3cposAppId"))
if mibBuilder.loadTexts: hh3cposAppDebugOpenTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDebugOpenTrap.setDescription('The agent will send a trap if the debugging switch of application is open.')
hh3cposAppDebugAllOpenTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 7))
if mibBuilder.loadTexts: hh3cposAppDebugAllOpenTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposAppDebugAllOpenTrap.setDescription('The agent will send a trap if the all debugging switches of application are open.')
hh3cposInterBuffOverFlowTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 8))
if mibBuilder.loadTexts: hh3cposInterBuffOverFlowTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterBuffOverFlowTrap.setDescription('The agent will send a trap if the distributing buffer is overflowed.')
hh3cposInterStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 9)).setObjects(("HH3C-POS-MIB", "hh3cposPosId"), ("HH3C-POS-MIB", "hh3cposPosConnectState"))
if mibBuilder.loadTexts: hh3cposInterStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterStateChangeTrap.setDescription('The agent will send a trap if the state of POS-Interface is changed to down.')
hh3cposInterDebugOpenTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 10)).setObjects(("HH3C-POS-MIB", "hh3cposPosId"))
if mibBuilder.loadTexts: hh3cposInterDebugOpenTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterDebugOpenTrap.setDescription('The agent will send a trap if the debug of POS-Interface is open.')
hh3cposInterDebugAllOpenTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 11))
if mibBuilder.loadTexts: hh3cposInterDebugAllOpenTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposInterDebugAllOpenTrap.setDescription('The agent will send a trap if the all debugs of POS-Interface are open.')
hh3cposFCMTimeoutTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 12)).setObjects(("HH3C-POS-MIB", "hh3cposFCMIfIndex"))
if mibBuilder.loadTexts: hh3cposFCMTimeoutTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMTimeoutTrap.setDescription('The agent will send a trap if the modem is hung up for timeout.')
hh3cposFCMConnectFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 13)).setObjects(("HH3C-POS-MIB", "hh3cposFCMIfIndex"))
if mibBuilder.loadTexts: hh3cposFCMConnectFailTrap.setStatus('current')
if mibBuilder.loadTexts: hh3cposFCMConnectFailTrap.setDescription('The agent will send a trap if the handshaking of modems is not successful.')
hh3cposClearPacketCounter = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 14))
if mibBuilder.loadTexts: hh3cposClearPacketCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposClearPacketCounter.setDescription('The agent will send a trap when the packet counter of the POS application and interface is cleared.')
hh3cposClearFcmCounter = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 15))
if mibBuilder.loadTexts: hh3cposClearFcmCounter.setStatus('current')
if mibBuilder.loadTexts: hh3cposClearFcmCounter.setDescription('The agent will send a trap when the FCM counter is cleared.')
mibBuilder.exportSymbols("HH3C-POS-MIB", hh3cposPosErrPacCounter=hh3cposPosErrPacCounter, hh3cposAppDistrErrCounter=hh3cposAppDistrErrCounter, hh3cposPosInterRowStatus=hh3cposPosInterRowStatus, hh3cposAppDebugAll=hh3cposAppDebugAll, hh3cposPadIdleTimeout=hh3cposPadIdleTimeout, hh3cposEnableTrap=hh3cposEnableTrap, hh3cposAppState=hh3cposAppState, hh3cposInterBuffOverFlowTrap=hh3cposInterBuffOverFlowTrap, hh3cposPadCheckSChar=hh3cposPadCheckSChar, hh3cposAppStateChangeTrap=hh3cposAppStateChangeTrap, hh3cposPadTable=hh3cposPadTable, hh3cposAppBuffedCounter=hh3cposAppBuffedCounter, hh3cposPosRecvPacCounter=hh3cposPosRecvPacCounter, hh3cposAppDebugOpenTrap=hh3cposAppDebugOpenTrap, hh3cposClearPacketCounter=hh3cposClearPacketCounter, hh3cposAppErrPacCounter=hh3cposAppErrPacCounter, hh3cposPadEntry=hh3cposPadEntry, hh3cposPadWaitTime=hh3cposPadWaitTime, hh3cposMapRowStatus=hh3cposMapRowStatus, hh3cposFCMIfIndex=hh3cposFCMIfIndex, hh3cposPosId=hh3cposPosId, hh3cposFCMTradeTime=hh3cposFCMTradeTime, hh3cposEnable=hh3cposEnable, hh3cposPadIfIndex=hh3cposPadIfIndex, hh3cposAppRowStatus=hh3cposAppRowStatus, hh3cposFCMTable=hh3cposFCMTable, hh3cposFCMEntry=hh3cposFCMEntry, hh3cposAppHostIP=hh3cposAppHostIP, hh3cposPosInterType=hh3cposPosInterType, hh3cposAppDiscardedCounter=hh3cposAppDiscardedCounter, hh3cposInterEntry=hh3cposInterEntry, hh3cposAppX121Addr=hh3cposAppX121Addr, hh3cposClearFcmCounter=hh3cposClearFcmCounter, hh3cposAsyAppEntry=hh3cposAsyAppEntry, hh3cposPadPacType=hh3cposPadPacType, hh3cposAppNotConfigedTrap=hh3cposAppNotConfigedTrap, hh3cposFCMConnectFailCounter=hh3cposFCMConnectFailCounter, hh3cposPadRowStatus=hh3cposPadRowStatus, hh3cposAppEntry=hh3cposAppEntry, hh3cposTrap=hh3cposTrap, hh3cposFCMPacketInterval=hh3cposFCMPacketInterval, hh3cposAppDebug=hh3cposAppDebug, hh3cposMapAppNumber=hh3cposMapAppNumber, hh3cposAsyAppTable=hh3cposAsyAppTable, hh3cposFCMTimeoutTrap=hh3cposFCMTimeoutTrap, hh3cposPosBuffedCounter=hh3cposPosBuffedCounter, hh3cposInterDebugOpenTrap=hh3cposInterDebugOpenTrap, hh3cposPosInterDebug=hh3cposPosInterDebug, hh3cposAppTable=hh3cposAppTable, hh3cposAppId=hh3cposAppId, hh3cposMapTable=hh3cposMapTable, hh3cposAppSourceIp=hh3cposAppSourceIp, hh3cposInterTable=hh3cposInterTable, hh3cposAppConnectFailTrap=hh3cposAppConnectFailTrap, hh3cposFCMAnswerTime=hh3cposFCMAnswerTime, hh3cposPosIfIndex=hh3cposPosIfIndex, hh3cposMapEntry=hh3cposMapEntry, hh3cposAsyAppIfIndex=hh3cposAsyAppIfIndex, hh3cposAppPort=hh3cposAppPort, hh3cposAppIfIndex=hh3cposAppIfIndex, hh3cposFCMConnectFailTrap=hh3cposFCMConnectFailTrap, hh3cposClearPacCounter=hh3cposClearPacCounter, hh3cposInterSum=hh3cposInterSum, hh3cposFCMTimeoutCounter=hh3cposFCMTimeoutCounter, hh3cposAppBuffOverFlowTrap=hh3cposAppBuffOverFlowTrap, hh3cposInterDebugAllOpenTrap=hh3cposInterDebugAllOpenTrap, hh3cposAppSum=hh3cposAppSum, hh3cposPosDebugAll=hh3cposPosDebugAll, hh3cposAppDebugAllOpenTrap=hh3cposAppDebugAllOpenTrap, hh3cposPosConnectState=hh3cposPosConnectState, PYSNMP_MODULE_ID=hh3cpos, hh3cposAppConnectMode=hh3cposAppConnectMode, hh3cposPosDiscardedCounter=hh3cposPosDiscardedCounter, hh3cpos=hh3cpos, hh3cposMapDes=hh3cposMapDes, hh3cposAppNotReadyTrap=hh3cposAppNotReadyTrap, hh3cposClearFCMCounter=hh3cposClearFCMCounter, hh3cposInterStateChangeTrap=hh3cposInterStateChangeTrap, hh3cposPosMapErrCounter=hh3cposPosMapErrCounter, hh3cposAsyAppRowStatus=hh3cposAsyAppRowStatus, hh3cposAppRecvPacCounter=hh3cposAppRecvPacCounter)
