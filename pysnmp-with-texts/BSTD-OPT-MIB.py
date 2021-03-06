#
# PySNMP MIB module BSTD-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSTD-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, enterprises, IpAddress, iso, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, ObjectIdentity, NotificationType, Unsigned32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "enterprises", "IpAddress", "iso", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500PCTBSTDDeviceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
class DisplayString(OctetString):
    pass

cdx6500PPCTBSTDPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14), )
if mibBuilder.loadTexts: cdx6500PPCTBSTDPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTBSTDPortTable.setDescription('A table of BSTD Port configuration parameters.')
cdx6500PPCTBSTDPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1), ).setIndexNames((0, "BSTD-OPT-MIB", "cdx6500BSTDCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTBSTDPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTBSTDPortEntry.setDescription('A BSTD Configuration Table entry. Each entry contains the configuration parameters for a single BSTD port. ')
cdx6500BSTDCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgPortNumber.setDescription('The BSTD port number described by this entry.')
cdx6500BSTDCfgPADType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("tpad", 0), ("hpad", 1), ("newvalTpad", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgPADType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgPADType.setDescription("Indicates whether the port is functioning as a Terminal PAD (tpad) or a Host PAD (hpad). newvalTpad - same functionality as 'tpad', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgLineInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("sync", 0), ("async", 1), ("newvalSync", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgLineInterface.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgLineInterface.setDescription("Selects the line interface to use. sync - synchronous operation. async - asynchronous operation. newvalSync - same functionality as 'sync', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("int", 0), ("ext", 1), ("newvalInt", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgClockSource.setDescription("int - internal clock source ext - external clock source. newvalInt - same functionality as 'int', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgClockSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1200, 192000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgClockSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgClockSpeed.setDescription('This is the speed of the port in bits per second, when using internal clocking.')
cdx6500BSTDCfgSyncContention = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("hdx", 0), ("fdx", 1), ("newvalHdx", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgSyncContention.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgSyncContention.setDescription("Indicates whether Half Duplex (hdx) or Full Duplex (fdx) modem signals are being generated. Full Duplex indicates communication is occuring in both directions simultaneously between devices. Half Duplex indicates transmission is occuring in both directions, but only in one direction at a time. newvalHdx - same functionality as 'hdx', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgAsyncConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 15, 50))).clone(namedValues=NamedValues(("simp", 0), ("simpa", 15), ("newvalSimp", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgAsyncConnType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgAsyncConnType.setDescription("Specify the control signal handshake required for a connection to be made to this port: simp - simple, no control signals required simpa - CTS follows RTS, but no control signals required Note: applicable for asynchronous operation only. newvalSimp - same functionality as 'simp', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgNumDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgNumDevices.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgNumDevices.setDescription('Specifies the number of physical devices on this line.')
cdx6500BSTDCfgServTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgServTimer.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgServTimer.setDescription('The Service Timer specifies the interval of time in seconds between periodic servicing. Such servicing includes intervals between the time the PAD will attempt to poll devices that previously failed to respond and intervals between failures in attempts to establish a connection from a device configured for Autocall.')
cdx6500BSTDCfgErrThreshCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgErrThreshCount.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgErrThreshCount.setDescription('Indicates number of consecutive errors that can occur before a device is considered down.')
cdx6500BSTDCfgResponseTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(400, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgResponseTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgResponseTimeout.setDescription("Specifies the amount of time in msec the PAD allows a terminal, printer or host to respond. As a result, the TPAD may re-transmit the previous message or abort the current procedure. The HPAD aborts the current procedure as though EOT was received, allowing this HPAD station to disconnect it's X.25 circuit if the host malfunctions. An HPAD with a response timeout shorter than the hosts ability to respond may result in Inbound Errors.")
cdx6500BSTDCfgPadProtTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgPadProtTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgPadProtTimeout.setDescription('Specifies the maximum amount of time in seconds the PAD will wait for the end of a multi-packet message from the network. If this time limit is exceeded, the PAD will initiate the clearing of the circuit.')
cdx6500BSTDCfgTranNumbers = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("disable", 0), ("modulo2", 1), ("newvalDisable", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgTranNumbers.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgTranNumbers.setDescription("This parameter is used to select the BSTD Transmission Numbering's mode of operation. disable - Disable Transmission Numbering modulo2 - Alternating '0' and '1' scheme. newvalDisable - same functionality as 'disable', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgContentionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1), ("newvalDisable", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgContentionMode.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgContentionMode.setDescription("For a TPAD port only : This parameter enables or disables a TPAD port to use BSTD Contention Mode. Note that an HPAD must have this option set to Enable. disable - Disable Contention Mode enable - Enable Contention Mode. newvalDisable - same functionality as 'disable', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDCfgPortSubAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgPortSubAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgPortSubAddr.setDescription('0 - 3 Decimal digits Calls addressed to this node and with this subaddress will be routed to this port.')
cdx6500BSTDCfgPortOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deprecatedObj", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgPortOptions.setStatus('deprecated')
if mibBuilder.loadTexts: cdx6500BSTDCfgPortOptions.setDescription('This object has been deprecated, It is replaced by cdx6500BSTDPortOptString.')
cdx6500BSTDCfgRestrictConnDest = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgRestrictConnDest.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgRestrictConnDest.setDescription('0 - 3 Decimal digits or a single blank All calls originating from this port will be routed to the destination specified in this parameter, irrespective of route selection table entries. For example, to route calls to port 1, use P1. To route calls to port 2, station 4, use P2S4.')
cdx6500BSTDCfgBillRec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("newvalOff", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgBillRec.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgBillRec.setDescription("This controls whether billing (accounting) records will be created for calls on this Device. newvalOff - same functionality as 'off', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDPortOptString = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortOptString.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortOptString.setDescription('This is the new object for cdx6500BSTDPortOption. Select options on this BSTD port as follows: NONE - no option specified ORG - Controllers on this port will originate the calls ACK - DSP End-to-End Acknowledgements are to be used Any combination of above specified by summing (e.g. ORG+ACK).')
cdx6500BSTDCfgElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgElectricalInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgElectricalInterfaceType.setDescription('Specify the Electrical Interface Type: V.24 - V.24 Electrical Interface Type V.35 - V.35 Electrical Interface Type V.36 - V.36 Electrical Interface Type X.21 - X.21 Electrical Interface Type NONE - Electrically disabled')
cdx6500BSTDCfgV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgV24ElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgV24ElectricalInterfaceOption.setDescription('Specify the Pin 22 option: RI - V.24 uses Pin 22 for Ring Indicator output signal TM - V.24 uses Pin 22 for Test Mode input signal')
cdx6500BSTDCfgHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCfgHighSpeedElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCfgHighSpeedElectricalInterfaceOption.setDescription('Specify the cable type: NONE - V.35/V.36/X.21 DCE with straight through cable XOVER - V.35/V.36/X.21 DCE with crossover adapter cable')
cdx6500PBCTBSTDDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1), )
if mibBuilder.loadTexts: cdx6500PBCTBSTDDeviceTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PBCTBSTDDeviceTable.setDescription('A table of BSTD device configuration parameters.')
cdx6500PBCTBSTDDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1), ).setIndexNames((0, "BSTD-OPT-MIB", "cdx6500BSTDDevPortNumber"), (0, "BSTD-OPT-MIB", "cdx6500BSTDDevEntry"))
if mibBuilder.loadTexts: cdx6500PBCTBSTDDeviceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PBCTBSTDDeviceEntry.setDescription('A BSTD Configuration Table entry. Each entry contains the configuration parameters for a single BSTD device.')
cdx6500BSTDDevPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDDevPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDDevPortNumber.setDescription('The BSTD port accessing this device')
cdx6500BSTDDevEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDDevEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDDevEntry.setDescription('The unique number for this specific port.')
cdx6500BSTDStationAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDStationAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDStationAddr1.setDescription("This is the first byte of this Station's address. The Station address consists of two hexadecimal digits. The valid range for a digit is 20-7F.")
cdx6500BSTDStationAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDStationAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDStationAddr2.setDescription("This is the second byte of this Station's address. The Station address consists of two hexadecimal digits. The valid range for a digit is 20-7F.")
cdx6500BSTDDestStationAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDDestStationAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDDestStationAddr1.setDescription('This is the first byte for the Station on the remote PAD. The Destination Station address consists of two hexadecimal digits. The valid range for a digit is 20-7F.')
cdx6500BSTDDesstStationAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDDesstStationAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDDesstStationAddr2.setDescription('This is the first byte for the Station on the remote PAD. The Destination Station address consists of two hexadecimal digits. The valid range for a digit is 20-7F.')
cdx6500BSTDGroupAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDGroupAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDGroupAddr1.setDescription("This is the first byte of this Station's Group address. The Group address consists of two hexadecimal digits. The valid range for a digit is 20-7F.")
cdx6500BSTDGroupAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDGroupAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDGroupAddr2.setDescription("This is the second byte of this Station's Group address. The Group address consists of two hexadecimal digits. The valid range for a digit is 20-7F.")
cdx6500BSTDCallMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCallMnemonic.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCallMnemonic.setDescription('This mnemonic name is used for originating calls from this Station.')
cdx6500BSTDStationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("no", 0), ("yes", 1), ("newvalNo", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDStationEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDStationEnabled.setDescription("This parameter is used to enable or disable the operation of this Station. no - Disable Station. yes - Enable Station. newvalNo - same functionality as 'no', new enumeration introduced for RFC1155 compatibility.")
cdx6500PPSTBSTDPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14), )
if mibBuilder.loadTexts: cdx6500PPSTBSTDPortStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPSTBSTDPortStatTable.setDescription('A table of BSTD port statistics.')
cdx6500BSTDPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1), ).setIndexNames((0, "BSTD-OPT-MIB", "cdx6500BSTDStatPortNumber"))
if mibBuilder.loadTexts: cdx6500BSTDPortStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortStatEntry.setDescription('A BSTD Port Statistic Table entry. Each entry contains the statistics for a single BSTD port.')
cdx6500BSTDStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDStatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDStatPortNumber.setDescription('The BSTD port number described by this entry.')
cdx6500BSTDPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 50))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("busyOut", 2), ("up", 3), ("down", 4), ("newvalDisabled", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortStatus.setDescription("Port Status indicates whether or not the port is switched on and is ready for operation. This value may be one of : up - Port is up and running. down - port is down. disabled - port has been disabled. enabled - port has been enabled, but is not yet Up busyOut - port has been set to be disabled as soon as last active session is disestablished. No new sessions will be established. newvalDisabled - same functionality as 'disabled', new enumeration introduced for RFC1155 compatibility.")
cdx6500BSTDPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortState.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortState.setDescription('Port State indicates what the port is actually in the process of doing. This value may be one of : INACTIVE - H/TPAD port inactive entered during boot WTPOLSERVE - TPAD is waiting for response to a poll WTSELRESP - TPAD is waiting for the response to a select WTDATARESP - H/TPAD is waiting for data to be acknowledged DATA - H/TPAD is in the process of sending/receiving data SEL/POL - TPAD is about to select or poll a controller. This is the most common state for a TPAD SELECT - TPAD is about to select a device POLL - TPAD is about to poll a device WTENQRESP - H/TPAD is waiting for a NAK response to an ENQ sent IDLE - HPAD is waiting for the host to send commands. This is the most common state of the HPAD WTEOT - HPAD is waiting for an expected EOT from the host FLUSHINGDATA - HPAD encountered an error in the message received from the host. As a result, the data is being flushed WTLCM - HPAD received a read/modify and is waiting for the response from the TPAD.')
cdx6500BSTDPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortSpeed.setDescription('This is the speed of the port if clock is internal. If clock is external, this is the detected clock speed. If Port Speed is 0, clock is external, but clocking is not being received from attatched device.')
cdx6500BSTDPortUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortUtilIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortUtilIn.setDescription('Percentage of Port input bandwidth in use.')
cdx6500BSTDPortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDPortUtilOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDPortUtilOut.setDescription('Percentage of Port output bandwidth in use.')
cdx6500BSTDInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDInMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDInMsgs.setDescription('Number of message received since last node, port, or statistics reset.')
cdx6500BSTDOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDOutMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDOutMsgs.setDescription('Number of message sent since last node, port, or statistics reset.')
cdx6500BSTDInChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDInChars.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDInChars.setDescription('Number of characters received since last node, port, or statistics reset.')
cdx6500BSTDOutChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDOutChars.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDOutChars.setDescription('Number of characters sent since last node, port, or statistics reset.')
cdx6500BSTDCharRateIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCharRateIn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCharRateIn.setDescription('Number of characters received per second.')
cdx6500BSTDCharRateOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCharRateOut.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCharRateOut.setDescription('Number of characters sent per second.')
cdx6500BSTDCrcBccErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500BSTDCrcBccErrs.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500BSTDCrcBccErrs.setDescription('Number of CRC errors since last node, port, or statistics reset.')
mibBuilder.exportSymbols("BSTD-OPT-MIB", cdx6500BSTDCfgResponseTimeout=cdx6500BSTDCfgResponseTimeout, cdx6500BSTDCfgContentionMode=cdx6500BSTDCfgContentionMode, cdx6500BSTDStationAddr1=cdx6500BSTDStationAddr1, cdx6500BSTDPortState=cdx6500BSTDPortState, cdx6500BSTDCfgSyncContention=cdx6500BSTDCfgSyncContention, cdx6500BSTDCfgPortSubAddr=cdx6500BSTDCfgPortSubAddr, cdx6500BSTDCharRateIn=cdx6500BSTDCharRateIn, cdx6500PPCTBSTDPortTable=cdx6500PPCTBSTDPortTable, cdx6500BSTDCfgRestrictConnDest=cdx6500BSTDCfgRestrictConnDest, cdx6500Configuration=cdx6500Configuration, cdx6500BSTDStationAddr2=cdx6500BSTDStationAddr2, cdx6500BSTDOutChars=cdx6500BSTDOutChars, cdx6500BSTDDevEntry=cdx6500BSTDDevEntry, cdx6500BSTDPortOptString=cdx6500BSTDPortOptString, cdx6500BSTDOutMsgs=cdx6500BSTDOutMsgs, cdx6500BSTDInMsgs=cdx6500BSTDInMsgs, cdx6500BSTDGroupAddr2=cdx6500BSTDGroupAddr2, cdx6500PBCTBSTDDeviceEntry=cdx6500PBCTBSTDDeviceEntry, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500BSTDCfgPortNumber=cdx6500BSTDCfgPortNumber, cdx6500BSTDCrcBccErrs=cdx6500BSTDCrcBccErrs, cdx6500BSTDCfgClockSource=cdx6500BSTDCfgClockSource, cdx6500BSTDCharRateOut=cdx6500BSTDCharRateOut, cdx6500BSTDCallMnemonic=cdx6500BSTDCallMnemonic, cdx6500BSTDPortUtilOut=cdx6500BSTDPortUtilOut, cdx6500BSTDInChars=cdx6500BSTDInChars, cdx6500BSTDCfgServTimer=cdx6500BSTDCfgServTimer, cdx6500BSTDCfgElectricalInterfaceType=cdx6500BSTDCfgElectricalInterfaceType, cdx6500BSTDPortUtilIn=cdx6500BSTDPortUtilIn, DisplayString=DisplayString, cdx6500BSTDCfgHighSpeedElectricalInterfaceOption=cdx6500BSTDCfgHighSpeedElectricalInterfaceOption, cdx6500BSTDDesstStationAddr2=cdx6500BSTDDesstStationAddr2, cdx6500BSTDDestStationAddr1=cdx6500BSTDDestStationAddr1, cdxProductSpecific=cdxProductSpecific, cdx6500BSTDGroupAddr1=cdx6500BSTDGroupAddr1, cdx6500BSTDCfgPADType=cdx6500BSTDCfgPADType, cdx6500BSTDCfgLineInterface=cdx6500BSTDCfgLineInterface, cdx6500BSTDPortStatus=cdx6500BSTDPortStatus, cdx6500BSTDDevPortNumber=cdx6500BSTDDevPortNumber, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500BSTDCfgPadProtTimeout=cdx6500BSTDCfgPadProtTimeout, cdx6500BSTDCfgBillRec=cdx6500BSTDCfgBillRec, cdx6500BSTDCfgTranNumbers=cdx6500BSTDCfgTranNumbers, cdx6500BSTDPortStatEntry=cdx6500BSTDPortStatEntry, cdx6500Statistics=cdx6500Statistics, cdx6500BSTDCfgV24ElectricalInterfaceOption=cdx6500BSTDCfgV24ElectricalInterfaceOption, cdx6500BSTDStationEnabled=cdx6500BSTDStationEnabled, cdx6500BSTDStatPortNumber=cdx6500BSTDStatPortNumber, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500PBCTBSTDDeviceTable=cdx6500PBCTBSTDDeviceTable, cdx6500PPSTBSTDPortStatTable=cdx6500PPSTBSTDPortStatTable, codex=codex, cdx6500=cdx6500, cdx6500BSTDCfgAsyncConnType=cdx6500BSTDCfgAsyncConnType, cdx6500PPCTBSTDPortEntry=cdx6500PPCTBSTDPortEntry, cdx6500BSTDCfgErrThreshCount=cdx6500BSTDCfgErrThreshCount, cdx6500BSTDCfgPortOptions=cdx6500BSTDCfgPortOptions, cdx6500PCTBSTDDeviceGroup=cdx6500PCTBSTDDeviceGroup, cdx6500BSTDPortSpeed=cdx6500BSTDPortSpeed, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500BSTDCfgNumDevices=cdx6500BSTDCfgNumDevices, cdx6500BSTDCfgClockSpeed=cdx6500BSTDCfgClockSpeed)
