#
# PySNMP MIB module HH3C-PPP-OVER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-PPP-OVER-SONET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, iso, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, IpAddress, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hh3cPos = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 19))
hh3cPos.setRevisions(('2013-10-10 17:00', '2010-05-19 17:00', '2007-07-19 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cPos.setRevisionsDescriptions(('Update the version of this MIB module', 'Update the version of this MIB module', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: hh3cPos.setLastUpdated('201310101700Z')
if mibBuilder.loadTexts: hh3cPos.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cPos.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cPos.setDescription('This MIB manages POS(PPP Over Sonet)interfaces by providing an operational table which controls parameters of each POS interface and reports alarm conditions. ')
hh3cPosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1))
hh3cPosParamTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1), )
if mibBuilder.loadTexts: hh3cPosParamTable.setStatus('current')
if mibBuilder.loadTexts: hh3cPosParamTable.setDescription('The pos parameter table.')
hh3cPosParamTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosParamTableEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cPosParamTableEntry.setDescription('The entry of pos table.')
hh3cPosCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc32", 1), ("crc16", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosCRC.setStatus('current')
if mibBuilder.loadTexts: hh3cPosCRC.setDescription('The length of CRC')
hh3cPosMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosMTU.setStatus('current')
if mibBuilder.loadTexts: hh3cPosMTU.setDescription('Maximum Transfer Unit (MTU) of POS interface')
hh3cPosScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosScramble.setStatus('current')
if mibBuilder.loadTexts: hh3cPosScramble.setDescription('Scrambling is used to avoid continuous 0 or 1 in signals. This object is to decide whether to scramble or not')
hh3cPosClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("system", 1), ("line", 2))).clone('line')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosClockSource.setStatus('current')
if mibBuilder.loadTexts: hh3cPosClockSource.setDescription('The value indicates the source of clock signal. System indicates that clock signals are from device itself and line for clock signals from remote')
hh3cPosSdhFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosSdhFlagJ0.setStatus('current')
if mibBuilder.loadTexts: hh3cPosSdhFlagJ0.setDescription('The section trace byte. This node is used when the frame type is sdh.')
hh3cPosSdhFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosSdhFlagJ1.setStatus('current')
if mibBuilder.loadTexts: hh3cPosSdhFlagJ1.setDescription('The path trace byte. This node is used when the frame type is sdh.')
hh3cPosSonetFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosSonetFlagJ0.setStatus('current')
if mibBuilder.loadTexts: hh3cPosSonetFlagJ0.setDescription('The section trace byte. This node is used when the frame type is sonet.')
hh3cPosSonetFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosSonetFlagJ1.setStatus('current')
if mibBuilder.loadTexts: hh3cPosSonetFlagJ1.setDescription('The path trace byte. This node is used when the frame type is sonet.')
hh3cPosFlagC2 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosFlagC2.setStatus('current')
if mibBuilder.loadTexts: hh3cPosFlagC2.setDescription('The parameter for the channel signal value of C2 byte')
hh3cPosFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosFrameType.setStatus('current')
if mibBuilder.loadTexts: hh3cPosFrameType.setDescription('The frame type that encapsulates the packet. Default frame type is sdh(Synchronous Digital Hierarchy) It also can be configured using sonet type(Synchronous Optical Network).')
hh3cPosBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosBindVlanId.setStatus('current')
if mibBuilder.loadTexts: hh3cPosBindVlanId.setDescription('The vlan that this pos port binds. The vlan can not include any other port, otherwise error will be returned. If the vlan has a virtual interface, the status of virtual interface will be up or down according to the link status or this pos.')
hh3cPosEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ppp", 1), ("hdlc", 2), ("fr", 3))).clone('ppp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosEncapsulation.setStatus('current')
if mibBuilder.loadTexts: hh3cPosEncapsulation.setDescription('The type of encapsulation ')
hh3cPoskeepaliveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPoskeepaliveTimeout.setStatus('current')
if mibBuilder.loadTexts: hh3cPoskeepaliveTimeout.setDescription('The keeplive of ppp, hdlc or fr. It is the query interval of link status. Two members of a link should have same keeplive. The default 0 prohibits detecting status of link.')
hh3cPosBERthresholdSF = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosBERthresholdSF.setStatus('current')
if mibBuilder.loadTexts: hh3cPosBERthresholdSF.setDescription('The bit-error rate threshold for Signal Fault. SF threshold should be greater than SD threshold.')
hh3cPosBERthresholdSD = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosBERthresholdSD.setStatus('current')
if mibBuilder.loadTexts: hh3cPosBERthresholdSD.setDescription('The bit-error rate threshold for Signal Degrade. SD threshold should be less than SF threshold.')
hh3cPosB1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosB1Error.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB1Error.setDescription('Counter for SBIPE(Section Bit Interleave Parity Error)')
hh3cPosB2Error = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosB2Error.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB2Error.setDescription('Counter for LBIPE(Line Bit Interleave Parity Error)')
hh3cPosB3Error = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosB3Error.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB3Error.setDescription('Counter for PBIPE(Path Bit Interleave Parity Error)')
hh3cPosM1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosM1Error.setStatus('current')
if mibBuilder.loadTexts: hh3cPosM1Error.setDescription('How many times does LREI(Line Remote Error Indication) occur')
hh3cPosG1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPosG1Error.setStatus('current')
if mibBuilder.loadTexts: hh3cPosG1Error.setDescription('How many times does PREI(Path Remote Error Indication) occur')
hh3cPosFlagJ0Type = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosFlagJ0Type.setStatus('current')
if mibBuilder.loadTexts: hh3cPosFlagJ0Type.setDescription('The frame type that encapsulates the flag J0. Default frame type is sdh(Synchronous Digital Hierarchy). It also can be configured using sonet(Synchronous Optical Network) type.')
hh3cPosFlagJ1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosFlagJ1Type.setStatus('current')
if mibBuilder.loadTexts: hh3cPosFlagJ1Type.setDescription('The frame type that encapsulates the flag J1. Default frame type is sdh(Synchronous Digital Hierarchy). It also can be configured using sonet(Synchronous Optical Network) type.')
hh3cPosB1TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB1TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB1TCAThreshold.setDescription('Threshold for B1 TCA.')
hh3cPosB2TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB2TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB2TCAThreshold.setDescription('Threshold for B2 TCA.')
hh3cPosB3TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB3TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB3TCAThreshold.setDescription('Threshold for B3 TCA.')
hh3cPosB1TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB1TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB1TCAEnable.setDescription('Enable traps of B1 TCA.')
hh3cPosB2TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB2TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB2TCAEnable.setDescription('Enable traps of B2 TCA.')
hh3cPosB3TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 19, 1, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPosB3TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB3TCAEnable.setDescription('Enable traps of B3 TCA.')
hh3cPosMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2))
hh3cPosMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0))
hh3cPosLOSAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLOSAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLOSAlarm.setDescription('Alarm indicates loss of signal')
hh3cPosLOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLOFAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLOFAlarm.setDescription('Alarm indicates loss of frame')
hh3cPosOOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosOOFAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosOOFAlarm.setDescription('Alarm indicates out of frame')
hh3cPosLAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLAISAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLAISAlarm.setDescription('Alarm when LAIS(Line Alarm Indication Signal) arrives')
hh3cPosLRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLRDIAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLRDIAlarm.setDescription('Alarm when LRDI(Line Remote Defect Indication) arrives')
hh3cPosPRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosPRDIAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosPRDIAlarm.setDescription('Alarm when PRDI(Path Remote Defect Indication) arrives')
hh3cPosPAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosPAISAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosPAISAlarm.setDescription('Alarm when PAIS(Path Alarm Indication Signal) arrives')
hh3cPosLOPAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLOPAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLOPAlarm.setDescription('Alarm indicates loss of pointer')
hh3cPosSTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 9)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosSTIMAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosSTIMAlarm.setDescription('Alarm indicates inconsistency between sent and received J0 bytes.')
hh3cPosPTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 10)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosPTIMAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosPTIMAlarm.setDescription('Alarm indicates inconsistency between sent and received J1 bytes.')
hh3cPosPSLMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosPSLMAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosPSLMAlarm.setDescription('Alarm indicates a mismatched C2 byte.')
hh3cPosLSDAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLSDAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLSDAlarm.setDescription('Alarm indicates that the B2 bit-error rate exceeds SD threshold.')
hh3cPosLSFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosLSFAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosLSFAlarm.setDescription('Alarm indicates that the B2 bit-error rate exceeds SF threshold.')
hh3cPosNormalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPosNormalAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosNormalAlarm.setDescription('Alarm indicates that the Pos interface state returns normal.')
hh3cPosB1TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosB1TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB1TCAlarm.setDescription('Threshold crossing alarms for B1.')
hh3cPosB2TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosB2TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB2TCAlarm.setDescription('Threshold crossing alarms for B2.')
hh3cPosB3TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 19, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cPosB3TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPosB3TCAlarm.setDescription('Threshold crossing alarms for B3.')
mibBuilder.exportSymbols("HH3C-PPP-OVER-SONET-MIB", hh3cPosParamTable=hh3cPosParamTable, hh3cPosLSDAlarm=hh3cPosLSDAlarm, PYSNMP_MODULE_ID=hh3cPos, hh3cPosLSFAlarm=hh3cPosLSFAlarm, hh3cPosLOSAlarm=hh3cPosLOSAlarm, hh3cPosB1TCAThreshold=hh3cPosB1TCAThreshold, hh3cPosScramble=hh3cPosScramble, hh3cPosBindVlanId=hh3cPosBindVlanId, hh3cPosParamTableEntry=hh3cPosParamTableEntry, hh3cPosPAISAlarm=hh3cPosPAISAlarm, hh3cPosNormalAlarm=hh3cPosNormalAlarm, hh3cPosB2TCAThreshold=hh3cPosB2TCAThreshold, hh3cPosMIBNotifications=hh3cPosMIBNotifications, hh3cPos=hh3cPos, hh3cPosLRDIAlarm=hh3cPosLRDIAlarm, hh3cPosB2TCAlarm=hh3cPosB2TCAlarm, hh3cPosSonetFlagJ1=hh3cPosSonetFlagJ1, hh3cPosFrameType=hh3cPosFrameType, hh3cPosBERthresholdSF=hh3cPosBERthresholdSF, hh3cPosB2Error=hh3cPosB2Error, hh3cPosG1Error=hh3cPosG1Error, hh3cPosFlagJ1Type=hh3cPosFlagJ1Type, hh3cPosSTIMAlarm=hh3cPosSTIMAlarm, hh3cPosMTU=hh3cPosMTU, hh3cPosLOFAlarm=hh3cPosLOFAlarm, hh3cPosSdhFlagJ1=hh3cPosSdhFlagJ1, hh3cPosSonetFlagJ0=hh3cPosSonetFlagJ0, hh3cPosSdhFlagJ0=hh3cPosSdhFlagJ0, hh3cPosLOPAlarm=hh3cPosLOPAlarm, hh3cPosB1Error=hh3cPosB1Error, hh3cPoskeepaliveTimeout=hh3cPoskeepaliveTimeout, hh3cPosLAISAlarm=hh3cPosLAISAlarm, hh3cPosPTIMAlarm=hh3cPosPTIMAlarm, hh3cPosB1TCAlarm=hh3cPosB1TCAlarm, hh3cPosPRDIAlarm=hh3cPosPRDIAlarm, hh3cPosOOFAlarm=hh3cPosOOFAlarm, hh3cPosMIBObjects=hh3cPosMIBObjects, hh3cPosPSLMAlarm=hh3cPosPSLMAlarm, hh3cPosFlagC2=hh3cPosFlagC2, hh3cPosB3TCAlarm=hh3cPosB3TCAlarm, hh3cPosB3TCAEnable=hh3cPosB3TCAEnable, hh3cPosEncapsulation=hh3cPosEncapsulation, hh3cPosCRC=hh3cPosCRC, hh3cPosClockSource=hh3cPosClockSource, hh3cPosM1Error=hh3cPosM1Error, hh3cPosMIBNotificationsPrefix=hh3cPosMIBNotificationsPrefix, hh3cPosB1TCAEnable=hh3cPosB1TCAEnable, hh3cPosB3Error=hh3cPosB3Error, hh3cPosFlagJ0Type=hh3cPosFlagJ0Type, hh3cPosB2TCAEnable=hh3cPosB2TCAEnable, hh3cPosBERthresholdSD=hh3cPosBERthresholdSD, hh3cPosB3TCAThreshold=hh3cPosB3TCAThreshold)