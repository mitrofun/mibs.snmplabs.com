#
# PySNMP MIB module CXISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXISDN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
SapIndex, Alias, cxISDN = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "Alias", "cxISDN")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, TimeTicks, iso, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, Bits, NotificationType, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "iso", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "Bits", "NotificationType", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
isdnSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: isdnSoftwareVersion.setDescription('Identifies the main version and revision numbers (separated by a period) of the ISDN software layer. Default Value: none')
isdnTraps = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnTraps.setStatus('mandatory')
if mibBuilder.loadTexts: isdnTraps.setDescription('Indicates whether this software layer produces the isdnCCSapStatusIndication and isdnL3SapStatusIndication traps. Options: disabled(1): software layer does not produce CC and L3 status indication traps enabled (1): software layer produces CC and L3 status indication traps Default Value: disabled Configuration Changed: administrative ')
isdnL3SapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20), )
if mibBuilder.loadTexts: isdnL3SapTable.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapTable.setDescription('A table containing configuration, controls, status and statistics information about each ISDN layer lower service access point.')
isdnL3SapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1), ).setIndexNames((0, "CXISDN-MIB", "isdnL3SapNumber"))
if mibBuilder.loadTexts: isdnL3SapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapEntry.setDescription('The parameters for a specific lower service access point.')
isdnL3SapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnL3SapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapNumber.setDescription('Indicates the row containing objects for configuring (or monitoring) a SAP that is associated with another SAP in the LAPD software layers. Note: The SAP number has to be the same than the Digital Subscriber Line number used in the BCM software layer. Range of Values: 1-6 Default Value: none')
isdnL3SapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapRowStatus.setDescription('Determines whether this SAP is to be removed from service (i.e. invalidated) within the ISDN software layer. Options: invalid (1): row is flagged; after next reset values will be disabled and row will be deleted from table valid (2): values are enabled Default Value: none Configuration Changed: administrative ')
isdnL3SapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapAlias.setDescription('Determines the textual name identifying this lower SAP. Range of Values: 0-16 alphanumeric characters beginning with a non-numeric character Default Value: none Configuration Changed: administrative ')
isdnL3SapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapCompanionAlias.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapCompanionAlias.setDescription('Determines the textual name identifying this SAPs companion SAP in the LAPD software layer. Range of Values: 0-16 alphanumeric characters beginning with a non-numeric character Default Value: none Configuration Changed: administrative ')
isdnL3SapUserNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("network", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapUserNetType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapUserNetType.setDescription('Determines the Basic Rate Interface emulation for this SAP. Options: user (1): BRI type is User network (2): BRI type is Network (for future use) Default Value: user Configuration Changed: administrative ')
isdnL3SapT303Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT303Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT303Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for an Alerting, Connect, Setup Acknowledge, Call Proceeding, or Release Complete message after sending a Setup message. Range of Values: 0-255 Default Value: 4 Configuration Changed: administrative ')
isdnL3SapT304Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT304Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT304Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Call Proceeding, Alerting, Connect, or Disconnect message after sending an Information message. Range of Values: 0-255 Default Value: 15 Configuration Changed: administrative ')
isdnL3SapT305Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT305Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT305Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Release or Disconnect message after sending a Disconnect message. Range of Values: 0-255 Default Value: 30 Configuration Changed: administrative ')
isdnL3SapT308Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT308Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT308Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Release or Release Complete message after sending a Release message. Range of Values: 0-255 Default Value: 4 Configuration Changed: administrative ')
isdnL3SapT310Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT310Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT310Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for an Alerting, Connect, Disconnect or Progress message after receiving a Call Proceeding message. Range of Values: 0-255 Default Value: 10 Configuration Changed: administrative ')
isdnL3SapT313Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT313Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT313Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Connect Acknowledge message after sending a Connect message. Range of Values: 0-255 Default Value: 4 Configuration Changed: administrative ')
isdnL3SapT318Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT318Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT318Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Resume Acknowledge or Resume Reject message after sending a Resume message. Range of Values: 0-255 Default Value: 4 Configuration Changed: administrative ')
isdnL3SapT319Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapT319Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapT319Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for a Suspend Acknowledge or Suspend Reject message after sending a Suspend message. Range of Values: 0-255 Default Value: 4 Configuration Changed: administrative ')
isdnL3SapDefTimerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noDefCfg", 1), ("defCfg", 2))).clone('defCfg')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnL3SapDefTimerCfg.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapDefTimerCfg.setDescription('Determines whether isdnL3SapT303Timer, isdnL3SapT304Timer, isdnL3SapT305Timer, isdnL3SapT308Timer, isdnL3SapT310Timer, isdnL3SapT313Timer, isdnL3SapT318Timer and isdnL3SapT319Timer will revert immediately to their default values if the value of this object has previously permitted these values to be changed from their defaults. Options: noDefCfg (1): timer values can be or have been modified DefCfg (2): timer value will maintain or return to their defaults Default Value: DefCfg Configuration Changed: administrative ')
isdnL3SapStatusEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noEvent", 1), ("badCfgVersion", 2), ("badDslID", 3), ("dslInUse", 4), ("dslNotInUse", 5), ("noNLCB", 6), ("nlcbInitErr", 7), ("badSwitchType", 8), ("nlcbPoolErr", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnL3SapStatusEvent.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapStatusEvent.setDescription('Indicates a status generated by the isdnL3SapStatusIndication trap. Note: This value will always read noEvent unless isdnTraps has been enabled and an event has been trapped. Options: noEvent (1): no trapped event badCfgVersion (2): configuration template not current badDslID (3): wrong Digital Subscriber Line dslInUse (4): Digital Subscriber Line in use dslNotInUse (5): Digital Subscriber Line not available noNLCB (6): network layer control block not available nlcbInitErr (7): network layer control block initialization error badSwitchType (8): incorrect switch-type configuration nlcbPoolErr (9) no more network layer control blocks Default Value: noEvent')
isdnL3SapDslType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("bri", 2), ("pri", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnL3SapDslType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapDslType.setDescription('Indicates the type of physical interface for this SAP. Options: none (1): SAP has no interface bri (2) SAP uses a Basic Rate Interface pri (3) SAP uses a Primary Rate Interface Default Value: none')
isdnL3SapBRIType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("u", 2), ("s-t", 3))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnL3SapBRIType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnL3SapBRIType.setDescription('Indicates the BRI type for this SAP. Options: none (1): SAP has no BRI interface u (2): BRI type is U s-t (3): BRI type is S/T Default Value: none')
isdnCCSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21), )
if mibBuilder.loadTexts: isdnCCSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapTable.setDescription('A table containing configuration information about each upper service access point.')
isdnCCSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1), ).setIndexNames((0, "CXISDN-MIB", "isdnCCSapNumber"))
if mibBuilder.loadTexts: isdnCCSapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapEntry.setDescription('The parameters for a specific upper service access point.')
isdnCCSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnCCSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapNumber.setDescription('Indicates the row containing objects for configuring (or monitoring) a SAP that is associated with the corresponding SAP in the BCM software layer. Note: The SAP number has to be the same than the Digital Subscriber Line number used in the BCM software layer. Range of Values: 1-6 Default Value: none')
isdnCCSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapRowStatus.setDescription('Determines whether this SAP is to be removed from service (i.e. invalidated) within the ISDN software layer. Options: invalid (1): row is flagged; after next reset values will be disabled and row will be deleted from table valid (2): values are enabled Default Value: none Configuration Changed: administrative ')
isdnCCSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapAlias.setDescription('Determines the textual name identifying this upper SAP. Range of Values:0-16 alphanumeric characters beginning with a non-numeric character Default Value: none Configuration Changed: administrative ')
isdnCCSapSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unspecified", 1), ("bri-1TR6", 2), ("bri-5ESS", 3), ("bri-CCITT", 4), ("bri-DMS100", 5), ("bri-KDD", 6), ("bri-NET3", 7), ("bri-NI1", 8), ("bri-NI2", 9), ("bri-NTT", 10), ("bri-TS013", 11), ("bri-VN", 12))).clone('bri-NI1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapSwitchType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapSwitchType.setDescription('Determines the type of protocol supported by the switch providing the CX 900 with ISDN access. Options: unspecified (1): unspecified bri-1TR6 (2): Germany / 1TR6 bri-5ESS (3): U.S.A / At&T 5ESS bri-CCITT (4): CCITT Q.931 bri-DMS100 (5): U.S.A / Norther Telecom bri-KDD (6): Japan / KDD bri-NET3 (7): Europe / Net3 bri-NI1 (8): U.S.A / National ISDN 1 bri-NI2 (9): U.S.A / National ISDN 2 bri-NTT (10): Japan / NTT bri-TS013 (11): Australia / TS013 bri-VN (12): France / VN Default Value: bri-NI1 Configuration Changed: administrative ')
isdnCCSapInitTerminal = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nit", 1), ("fit", 2))).clone('nit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapInitTerminal.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapInitTerminal.setDescription('Determines the initializing characteristics of the ISDN software layer of the CX 900. Options: nit (1): non-initializing terminal fit (2) fully-initializing terminal (North American Note: FIT requires terminal registration. Default Value: nit Configuration Changed: administrative ')
isdnCCSapDNRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapDNRouting.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapDNRouting.setDescription('Determines whether incoming calls will be checked against End-Point ID (EPID). Options: no (1): incoming call not checked against EPID yes (2): incoming call checked against EPID Note: Incoming call not containing EPID will be checked against Directory Number (DN). Default Value: no Configuration Changed: administrative ')
isdnCCSapBearerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapBearerRouting.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapBearerRouting.setDescription('Determines whether incoming calls will be checked against the bearer-type specified in isdnCCSapBearerType Options: no (1): incoming call not checked against bearer-type yes (2): incoming call checked against bearer-type Default Value: no Configuration Changed: administrative ')
isdnCCSapBearerType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("voice-call", 1), ("circuit-sw-data-call", 2), ("packet-sw-data-call", 3))).clone('circuit-sw-data-call')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapBearerType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapBearerType.setDescription('Determines the bearer-type that will be checked if isdnCCSapBearerType is set to yes. Options: voice call (1): call is voice circuit-sw-data-call (2): call is circuit- switched data packet-sw-data-call (3): call is packet- switched data Default Value: circuit-sw-data-call Configuration Changed: administrative ')
isdnCCSapDirectoryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapDirectoryNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapDirectoryNumber.setDescription('Determines the address or calling number assigned to the subcriber interface of the CX900. Range of Values: 0-16 numeric characters (namely, 0123456789*#) Default Value: none Configuration Changed: administrative ')
isdnCCSapSPID = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapSPID.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapSPID.setDescription('Determines the Service Profile Identifier (SPID) for the subscriber interface of the CX900. This object is meaningful only in North America. SPIDs are required for DMS-100 and NI-1 switches but optional for 5ESS switches. Range of Values: 0-20 Default Value: none Configuration Changed: administrative ')
isdnCCSapSubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapSubAddress.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapSubAddress.setDescription('Determines the subaddress (DSS1) that can be used with object isdnCCSapDirectoryNumber to specify an end-point user to be reached. Range of Values: 0-20 Default Value: none Configuration Changed: administrative ')
isdnCCSapT415Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnCCSapT415Timer.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapT415Timer.setDescription('Determines the interval in seconds that the ISDN software layer will wait for completion of terminal initialization. If the Information and SPID messages fail during this interval, they will be permitted only one retransmission. Range of Values: 0-255 Default Value: 20 Configuration Changed: administrative ')
isdnCCSapStatusEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("noEvent", 1), ("badCfgVersion", 2), ("badDslID", 3), ("badCes", 4), ("badSwitchType", 5), ("cbPollErr", 6), ("dslInUseErr", 7), ("dslNotCfgErr", 8), ("dslNotInUse", 9), ("noHostCB", 10), ("noT415", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnCCSapStatusEvent.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapStatusEvent.setDescription('Indicates a status generated by the isdnCCSapStatusIndication trap. Note: This value will always read noEvent unless isdnTraps has been enabled and an event has been trapped. Options: noEvent (1): no trapped event badCfgVersion (2): configuration template not current badDslID (3): wrong Digital Subscriber Line badCes (4): bad connection end-point badSwitchType (5): incorrect switch-type configuration cbPollErr (6): call control block error dslInUseErr (7): Digital Subscriber Line in use dslNotCfgErr (8): Digital Subscriber Line not configured dslNotInUse (9): Digital Subscriber Line not available noHostCB (10): no host control block noT415 (11): no T415 timer Default Value: noEvent')
isdnCCSapInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnCCSapInUse.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapInUse.setDescription('Indicates whether this upper SAP has been properly initialized and is now in use. Options: no (1): SAP has not been initialized yes (2): SAP is in use Default Value: none')
isdnCCSapActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnCCSapActiveCalls.setStatus('mandatory')
if mibBuilder.loadTexts: isdnCCSapActiveCalls.setDescription('Indicates the current number of active calls at this SAP. Range of Values: 0-2 Default Value: none')
isdnDebugTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22), )
if mibBuilder.loadTexts: isdnDebugTable.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugTable.setDescription('A table containing control to access debugging information.')
isdnDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1), ).setIndexNames((0, "CXISDN-MIB", "isdnDebugNumber"))
if mibBuilder.loadTexts: isdnDebugEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugEntry.setDescription('The parameters for a specific structure debugging information.')
isdnDebugNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDebugNumber.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugNumber.setDescription('Indicates the row containing objects for creating diagnostic files for this upper SAP. Range of Values: 1-6 Default Value: none')
isdnDebugCCB = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 10), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: isdnDebugCCB.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugCCB.setDescription('Creates a file that includes the following Call Control Block information: - DSL = #XX - CCB = #XX - State = 0xXXXX - CallType = 0xXXXX - B-Chan = 0xXXXX - Call-ID = 0xXXXX - CallRef = 0xXXXX - Ces = 0xXX - Sapi = 0xXX - MakePrivateMsg = 0xXX - H cbIndex = 0xXXXX - CallRefLen = 0xXXXX - Cause = 0xXXXX - Host-Specifier = 0xXXXX - Host-ID = 0xXXXX - SendClearConf = 0xXX - Diagnostics = 0xXX - CollectAddress = 0xXX - Service = 0xXXXX')
isdnDebugHCB = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 11), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: isdnDebugHCB.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugHCB.setDescription('Creates a file that includes the following Host Control Block information: - DSL = #XX - HCB = #XX - Directory = XXXXXXXXXXXXXXXXXXXX - SPID = XXXXXXXXXXXXXXXXXXXX epid(0) - epsf = 0xXX - usid = 0xXXXX - tid = 0xXXXX epid[1] - epsf = 0xXX - usid = 0xXXXX - tid = 0xXXXX - Busy[0] = 0xXX, - Busy[1] = 0xXX - Terminal-state = 0xXX - Timer-T415 = 0xXXXX - Bearer-Routing = 0xXX - Host-ID = 0xXXXX - Ces = 0xXX - Initializing-Terminal = 0xXX')
isdnDebugCCDsl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 12), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: isdnDebugCCDsl.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugCCDsl.setDescription('Creates a file that includes the following Call Control DSL information: - DSL = #XX - InUse = 0xXXXX - ActiveCCBs = 0xXXXX - Cause-Location = XXXXXX - Cd-Numb-Plan = XXXXXX - Cd-Numb-Type = XXXXXX - Cd-Sub-Type = XXXXXX - Cr-Numb-Plan = XXXXXX - Cr-Numb-Type = XXXXXX - Cr-Prest-Ind = XXXXXX - Cr-Scrn-Ind = XXXXXX - Cr-Sub-Type = XXXXXX - Facility-Code = XXXXXX - HL-Coding-Std = XXXXXX - HL-Interpret = XXXXXX - HL-Presentat = XXXXXX - HL-Teleservice = XXXXXX - L2-Prot = XXXXXX - L3-Prot = XXXXXX - Sig-Val = XXXXXX - Status = XXXXXX - Transmit-Attr = XXXXXX - Xfer-Cap = XXXXXX - Xfer-Mode = XXXXXX - Xfer-Prot = XXXXXX - Xfer-Rate = XXXXXX - Prog-Coding = XXXXXX - Prog-Loc = XXXXX - Prog-desc = XXXXXX - Ind-Val = XXXXXX')
isdnDebugNLCB = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 13), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: isdnDebugNLCB.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDebugNLCB.setDescription('Creates a file that includes the following Network Link Control Block information: - DSL = #XX - NLCB = #XX - DslID = 0xXXXX - Ces = 0xXX - CallID = 0xXXXX - ChanID = 0xXXXX - CallReflen = 0xXX - CallRef = 0xXXXX - State = 0xXXXX - Event = 0xXXXX - Timer-T304 = 0xXXXX - Timer-T310 = 0xXXXX - T303-First = 0xXX - T308-First = 0xXX - T313-First = 0xXX - UserOriginated = 0xXX - Internal = 0xXX - Cause = 0xXX - PreviousCause = 0xXX')
isdnL3SapStatusIndication = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32) + (0,1)).setObjects(("CXISDN-MIB", "isdnL3SapNumber"), ("CXISDN-MIB", "isdnL3SapStatusEvent"))
if mibBuilder.loadTexts: isdnL3SapStatusIndication.setDescription('Indicates that an event specified in isdnL3SapStatusEvent has occurred.')
isdnCCSapStatusIndication = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32) + (0,2)).setObjects(("CXISDN-MIB", "isdnCCSapNumber"), ("CXISDN-MIB", "isdnCCSapStatusEvent"))
if mibBuilder.loadTexts: isdnCCSapStatusIndication.setDescription('Indicates that an event specified in isdnCCSapStatusEvent has occurred.')
mibBuilder.exportSymbols("CXISDN-MIB", isdnL3SapT319Timer=isdnL3SapT319Timer, isdnCCSapBearerType=isdnCCSapBearerType, isdnCCSapSwitchType=isdnCCSapSwitchType, isdnCCSapInitTerminal=isdnCCSapInitTerminal, isdnL3SapT318Timer=isdnL3SapT318Timer, isdnDebugNLCB=isdnDebugNLCB, isdnL3SapDslType=isdnL3SapDslType, isdnSoftwareVersion=isdnSoftwareVersion, isdnL3SapT305Timer=isdnL3SapT305Timer, isdnL3SapT304Timer=isdnL3SapT304Timer, isdnL3SapDefTimerCfg=isdnL3SapDefTimerCfg, isdnL3SapCompanionAlias=isdnL3SapCompanionAlias, isdnDebugTable=isdnDebugTable, isdnDebugCCDsl=isdnDebugCCDsl, isdnCCSapAlias=isdnCCSapAlias, isdnDebugCCB=isdnDebugCCB, isdnL3SapEntry=isdnL3SapEntry, isdnL3SapTable=isdnL3SapTable, isdnDebugHCB=isdnDebugHCB, isdnCCSapStatusEvent=isdnCCSapStatusEvent, isdnCCSapTable=isdnCCSapTable, isdnCCSapRowStatus=isdnCCSapRowStatus, isdnCCSapT415Timer=isdnCCSapT415Timer, isdnL3SapNumber=isdnL3SapNumber, isdnL3SapStatusEvent=isdnL3SapStatusEvent, isdnCCSapEntry=isdnCCSapEntry, isdnL3SapUserNetType=isdnL3SapUserNetType, isdnDebugEntry=isdnDebugEntry, isdnL3SapT308Timer=isdnL3SapT308Timer, isdnCCSapSPID=isdnCCSapSPID, isdnCCSapStatusIndication=isdnCCSapStatusIndication, isdnCCSapActiveCalls=isdnCCSapActiveCalls, isdnCCSapNumber=isdnCCSapNumber, isdnCCSapDirectoryNumber=isdnCCSapDirectoryNumber, isdnCCSapBearerRouting=isdnCCSapBearerRouting, isdnL3SapT310Timer=isdnL3SapT310Timer, isdnCCSapInUse=isdnCCSapInUse, isdnL3SapT313Timer=isdnL3SapT313Timer, isdnL3SapT303Timer=isdnL3SapT303Timer, isdnDebugNumber=isdnDebugNumber, isdnCCSapDNRouting=isdnCCSapDNRouting, isdnTraps=isdnTraps, isdnCCSapSubAddress=isdnCCSapSubAddress, isdnL3SapAlias=isdnL3SapAlias, isdnL3SapStatusIndication=isdnL3SapStatusIndication, isdnL3SapRowStatus=isdnL3SapRowStatus, isdnL3SapBRIType=isdnL3SapBRIType)
