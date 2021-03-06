#
# PySNMP MIB module D3I-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/D3I-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, iso, experimental, enterprises, ModuleIdentity, TimeTicks, MibIdentifier, Integer32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "iso", "experimental", "enterprises", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Integer32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
d3i = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43))
d3iID = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43, 1))
d3iIDTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1), )
if mibBuilder.loadTexts: d3iIDTable.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDTable.setDescription('This table contains an entry for each of the manageable DS3 Ingress Cards in the chassis. It contains objects that reflect the current configuration of parameters that affect the operation of all the entities that reside on the given card.')
d3iIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1), ).setIndexNames((0, "D3I-MIB", "d3iIDIndex"))
if mibBuilder.loadTexts: d3iIDEntry.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDEntry.setDescription('There is one Identification table entry per DS3 Card in the chassis.')
d3iIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDIndex.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDIndex.setDescription('A unique value for each card in the chassis. The value of d3iIdIndex matches the value of the index for the corresponding card entity in the entity table of the chassis MIB.')
d3iIDNACHardwareSerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDNACHardwareSerNum.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDNACHardwareSerNum.setDescription('This object contains DS3 NAC module hardware serial number as stored in EEPROM.')
d3iIDNICHardwareSerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDNICHardwareSerNum.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDNICHardwareSerNum.setDescription('This object contains DS3 NIC module hardware serial number as stored in EEPROM.')
d3iIDNACHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDNACHardwareRev.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDNACHardwareRev.setDescription('This object contains DS3 NAC module hardware revision as stored in EEPROM.')
d3iIDNICHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDNICHardwareRev.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDNICHardwareRev.setDescription('This object contains DS3 NIC module hardware revision as stored in EEPROM.')
d3iIDBoardManagerSwRev = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDBoardManagerSwRev.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDBoardManagerSwRev.setDescription('This object contains revision of the software being executed by the DS3 NAC board manager processor.')
d3iIDBoardManagerDate = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iIDBoardManagerDate.setStatus('mandatory')
if mibBuilder.loadTexts: d3iIDBoardManagerDate.setDescription('This object contains board manager build date.')
d3iCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43, 2))
d3iCfgTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1), )
if mibBuilder.loadTexts: d3iCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgTable.setDescription('This table contains an entry for each of the manageable DS3 Ingress Cards in the chassis. It contains objects that reflect the current configuration of parameters that affect the operation of all the entities that reside on the given card.')
d3iCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1), ).setIndexNames((0, "D3I-MIB", "d3iCfgIndex"))
if mibBuilder.loadTexts: d3iCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgEntry.setDescription('There is one Configuration table entry per DS3 Card in the chassis.')
d3iCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iCfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgIndex.setDescription('A unique value for each card in the chassis. The value of d3iCfgIndex matches the value of the index for the corresponding card entity in the entity table of the chassis MIB.')
d3iCfgPrimaryTimeSource = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(128, 129, 130, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("spanBITS", 128), ("internal", 129), ("throughTDM", 130), ("span1", 1), ("span2", 2), ("span3", 3), ("span4", 4), ("span5", 5), ("span6", 6), ("span7", 7), ("span8", 8), ("span9", 9), ("span10", 10), ("span11", 11), ("span12", 12), ("span13", 13), ("span14", 14), ("span15", 15), ("span16", 16), ("span17", 17), ("span18", 18), ("span19", 19), ("span20", 20), ("span21", 21), ("span22", 22), ("span23", 23), ("span24", 24), ("span25", 25), ("span26", 26), ("span27", 27), ("span28", 28)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCfgPrimaryTimeSource.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgPrimaryTimeSource.setDescription('This object contains Designation of primary system clock timing reference source.')
d3iCfgSecondaryTimeSource = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(128, 129, 130, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("spanBITS", 128), ("internal", 129), ("throughTDM", 130), ("span1", 1), ("span2", 2), ("span3", 3), ("span4", 4), ("span5", 5), ("span6", 6), ("span7", 7), ("span8", 8), ("span9", 9), ("span10", 10), ("span11", 11), ("span12", 12), ("span13", 13), ("span14", 14), ("span15", 15), ("span16", 16), ("span17", 17), ("span18", 18), ("span19", 19), ("span20", 20), ("span21", 21), ("span22", 22), ("span23", 23), ("span24", 24), ("span25", 25), ("span26", 26), ("span27", 27), ("span28", 28)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCfgSecondaryTimeSource.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgSecondaryTimeSource.setDescription('This object contains Designation of secondary system clock timing reference source.')
d3iCfgTimeSourceSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCfgTimeSourceSwitchMode.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgTimeSourceSwitchMode.setDescription('If a clock failure occurs on the currently active clock timing reference, this object specifies whether the switchover to the backup reference will be performed automatically or manually.')
d3iCfgCLIPromptName = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCfgCLIPromptName.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCfgCLIPromptName.setDescription("This object is used to identify DS3 module's console prompt name.")
d3iStat = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43, 3))
d3iStatTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1), )
if mibBuilder.loadTexts: d3iStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatTable.setDescription('The Status table contains an entry for each DS3 card in the chassis.')
d3iStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1), ).setIndexNames((0, "D3I-MIB", "d3iStatIndex"))
if mibBuilder.loadTexts: d3iStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatEntry.setDescription('There is one entry for each DS3 card in the chassis.')
d3iStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatIndex.setDescription("A unique value for each DS3 card in the chassis. The value of this object matches the value of the index of the corresponding DS3 card's entry in the entity table of the chassis MIB.")
d3iStatSigPBusTxPktOkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatSigPBusTxPktOkCnt.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatSigPBusTxPktOkCnt.setDescription('The number of successful packets transmitted over the signaling packet bus connection.')
d3iStatSigPBusTxPktFldCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatSigPBusTxPktFldCnt.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatSigPBusTxPktFldCnt.setDescription('The number of packets failed to transmit over the signaling packet bus connection.')
d3iStatSigPBusRxPktOkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatSigPBusRxPktOkCnt.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatSigPBusRxPktOkCnt.setDescription('The number of successful packets received over the signaling packet bus connection.')
d3iStatSigPBusRxPktRjtCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatSigPBusRxPktRjtCnt.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatSigPBusRxPktRjtCnt.setDescription('The number of packets rejected by the DS3 NAC module message handling application.')
d3iStatSigPBusConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("closed", 1), ("opening", 2), ("opened", 3), ("configuring", 4), ("ready", 5), ("closing", 6), ("loopback", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatSigPBusConnState.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatSigPBusConnState.setDescription('The state of the signaling packet bus connection to the JHDM NAC. The loopback state means the DS3 has been requested, over the signaling packet bus link, to loopback all of its signaling channel received data. It will stay in this state until the DS3 sends an call control message to remove the loopback on this signaling connection.')
d3iStatEnfasLinkDownCause = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("discCmd", 2), ("nacRemoval", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatEnfasLinkDownCause.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatEnfasLinkDownCause.setDescription('The reason for the E-NFAS signaling link going down. DisCmd: A DISC command was received over the packet bus signaling link. NACRemoval: A chassis awareness message indicated that the NAC connected to the E-NFAS link has been removed.')
d3iStatPbClock = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("clockMaster", 2), ("clockSlave", 3), ("noClockPresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatPbClock.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatPbClock.setDescription('This object defines the current status of the packet bus clock.')
d3iStatTdmClock = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("clockMaster", 2), ("clockSlave", 3), ("noClockPresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iStatTdmClock.setStatus('mandatory')
if mibBuilder.loadTexts: d3iStatTdmClock.setDescription('This object defines the current status of the TDM bus system clock.')
d3iCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43, 4))
d3iCmdTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1), )
if mibBuilder.loadTexts: d3iCmdTable.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdTable.setDescription('The DS3 card command table contains an entry for each of the manageable DS3 card in the chassis. It provides a means through which to take specific actions on the DS3 card in the chassis.')
d3iCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1), ).setIndexNames((0, "D3I-MIB", "d3iCmdIndex"))
if mibBuilder.loadTexts: d3iCmdEntry.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdEntry.setDescription('There is one DS3 card command entry per DS3 card in the chassis.')
d3iCmdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iCmdIndex.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdIndex.setDescription("A unique value for each DS3 card in the chassis. The value of this object matches the value of the index of the corresponding DS3 card's entry in the entity table of the chassis MIB.")
d3iCmdMgtStationId = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCmdMgtStationId.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdMgtStationId.setDescription('This object is a generic read-write variable that a Management Station (MS) can use to guarantee that the results from a command are the results of a command issued by that specific MS. Each MS must SET a unique value to this object when doing commands and GET the value of this object together with d3iCmdReqId and d3iCmdResult to detect interference from other MSs.')
d3iCmdReqId = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iCmdReqId.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdReqId.setDescription('This object contains the value of the request-id field in the SNMP PDU which invoked the current or most recent command or test on this DS3 card. If the request-id is unknown or undefined, this object contains the value zero.')
d3iCmdFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noCommand", 1), ("restoreCfgFromNvram", 2), ("softwareReset", 3), ("restoreDefaultUIPassword", 4), ("restoreCfgFromDefaults", 5), ("saveCfgtoNvram", 6), ("d3iNICReset", 7), ("d3iNICResetHold", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCmdFunction.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdFunction.setDescription('This object contains a value which describes the command which is being invoked.')
d3iCmdForce = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("force", 1), ("noForce", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCmdForce.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdForce.setDescription('In some cases the DS3 card may be in a state such that certain commands could adversely affect connections. In such cases, a command request with this object not present or set to noForce will result in a warning. If the operator elects to ignore such warnings, this object can be set to force in a subsequent issue of the command to cause the command to be carried out regardless of its potentially hazzardous effects.')
d3iCmdParam = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iCmdParam.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdParam.setDescription('This object contains parameters that are specific to the particular command being issued. In some cases, there will be no addtional parameters required.')
d3iCmdResult = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("notSupported", 4), ("unAbleToRun", 5), ("aborted", 6), ("failed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iCmdResult.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdResult.setDescription('This object contains the result of the most recently requested command or test, or the value none(1) if no commands have been requested since the last reset.')
d3iCmdCode = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(58, 73))).clone(namedValues=NamedValues(("userInterfaceActive", 58), ("pendingSoftwareDownload", 73)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iCmdCode.setStatus('mandatory')
if mibBuilder.loadTexts: d3iCmdCode.setDescription('The value of this object upon commad completion indicates a futher description of what went wrong if the command was unsuccessful. In the case of tests, a bit mapped result of each of the sub-tests performed can be found in the status table.')
d3iTe = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 43, 5))
d3iTeTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1), )
if mibBuilder.loadTexts: d3iTeTable.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeTable.setDescription('The trap table containing an enable for each that the card is capable of generating. Some of these events occur often and traps may flood the network if care is not taken to avoid such conditions. These traps should be enabled sparingly.')
d3iTeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1), ).setIndexNames((0, "D3I-MIB", "d3iTeIndex"))
if mibBuilder.loadTexts: d3iTeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeEntry.setDescription('There is one entry for each DS3 card in the chassis.')
d3iTeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: d3iTeIndex.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeIndex.setDescription("A unique value for each DS3 card in the chassis. The value of this object matches the value of the index of the corresponding DS3 card's entry in the entity table of the chassis MIB.")
d3iTePbActive = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTePbActive.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTePbActive.setDescription('Enables the Packet Bus Active Trap. Default is disableAll(2).')
d3iTePbLost = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTePbLost.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTePbLost.setDescription('Enables the Packet Bus lost Trap. Default is disableAll(2).')
d3iTePbClockLossEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTePbClockLossEvent.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTePbClockLossEvent.setDescription('This object is used to disable the ability for a NAC to report when the packet bus clock has been lost. Defaule is diableAll(2).')
d3iTePbClockRestoreEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTePbClockRestoreEvent.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTePbClockRestoreEvent.setDescription('This object is used to disable the ability for a NAC to report when the packet bus clock has been restored. Defaule is diableAll(2).')
d3iTeTdmClockLost = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTeTdmClockLost.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeTdmClockLost.setDescription('Enables generation of an SNMP trap upon detection of TDM bus system clock lost. Default is disableAll(2).')
d3iTeTdmClockRestored = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTeTdmClockRestored.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeTdmClockRestored.setDescription('Enables generation of an SNMP trap upon detection of TDM bus system clock restored. Default is disableAll(2).')
d3iTeEnfasLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTeEnfasLinkUp.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeEnfasLinkUp.setDescription('The trap enable for ENFAS link coming up trap. Default is disable.')
d3iTeEnfasLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTeEnfasLinkDown.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeEnfasLinkDown.setDescription('The trap enable for ENFAS link coming down trap. Default is disable.')
d3iTeSystemReset = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: d3iTeSystemReset.setStatus('mandatory')
if mibBuilder.loadTexts: d3iTeSystemReset.setDescription('The trap enable disable for the DS3 system reset')
mibBuilder.exportSymbols("D3I-MIB", d3iCmdMgtStationId=d3iCmdMgtStationId, d3iCmdReqId=d3iCmdReqId, d3iTeTdmClockLost=d3iTeTdmClockLost, nas=nas, d3iStat=d3iStat, d3iIDBoardManagerDate=d3iIDBoardManagerDate, d3iCfgCLIPromptName=d3iCfgCLIPromptName, d3iStatIndex=d3iStatIndex, d3iStatSigPBusConnState=d3iStatSigPBusConnState, d3iTe=d3iTe, d3iStatEnfasLinkDownCause=d3iStatEnfasLinkDownCause, d3iCmdIndex=d3iCmdIndex, d3iStatSigPBusRxPktOkCnt=d3iStatSigPBusRxPktOkCnt, d3i=d3i, d3iIDTable=d3iIDTable, d3iTeEnfasLinkUp=d3iTeEnfasLinkUp, d3iIDBoardManagerSwRev=d3iIDBoardManagerSwRev, d3iCfgIndex=d3iCfgIndex, d3iTeIndex=d3iTeIndex, d3iCmdParam=d3iCmdParam, d3iIDNICHardwareSerNum=d3iIDNICHardwareSerNum, d3iID=d3iID, d3iTeTdmClockRestored=d3iTeTdmClockRestored, d3iStatPbClock=d3iStatPbClock, d3iIDNACHardwareSerNum=d3iIDNACHardwareSerNum, d3iTeTable=d3iTeTable, d3iCmdEntry=d3iCmdEntry, d3iCmdResult=d3iCmdResult, d3iStatSigPBusRxPktRjtCnt=d3iStatSigPBusRxPktRjtCnt, d3iTeEnfasLinkDown=d3iTeEnfasLinkDown, d3iTePbLost=d3iTePbLost, d3iTeSystemReset=d3iTeSystemReset, d3iCmdTable=d3iCmdTable, d3iStatTdmClock=d3iStatTdmClock, d3iCfgTable=d3iCfgTable, d3iTePbActive=d3iTePbActive, d3iCfgSecondaryTimeSource=d3iCfgSecondaryTimeSource, d3iCfgPrimaryTimeSource=d3iCfgPrimaryTimeSource, d3iCfg=d3iCfg, d3iIDIndex=d3iIDIndex, d3iTeEntry=d3iTeEntry, d3iTePbClockLossEvent=d3iTePbClockLossEvent, d3iCfgEntry=d3iCfgEntry, d3iStatTable=d3iStatTable, d3iStatEntry=d3iStatEntry, d3iCmdForce=d3iCmdForce, d3iIDNACHardwareRev=d3iIDNACHardwareRev, d3iIDEntry=d3iIDEntry, d3iCmd=d3iCmd, d3iTePbClockRestoreEvent=d3iTePbClockRestoreEvent, d3iCmdCode=d3iCmdCode, d3iStatSigPBusTxPktOkCnt=d3iStatSigPBusTxPktOkCnt, d3iIDNICHardwareRev=d3iIDNICHardwareRev, usr=usr, d3iStatSigPBusTxPktFldCnt=d3iStatSigPBusTxPktFldCnt, d3iCmdFunction=d3iCmdFunction, d3iCfgTimeSourceSwitchMode=d3iCfgTimeSourceSwitchMode)
