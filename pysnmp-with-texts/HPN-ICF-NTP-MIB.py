#
# PySNMP MIB module HPN-ICF-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfRhw, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfRhw")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, IpAddress, Bits, ObjectIdentity, iso, ModuleIdentity, Counter32, Counter64, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "IpAddress", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32", "Counter64", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
hpnicfNTP = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22))
hpnicfNTP.setRevisions(('2003-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfNTP.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfNTP.setLastUpdated('200303150000Z')
if mibBuilder.loadTexts: hpnicfNTP.setOrganization('')
if mibBuilder.loadTexts: hpnicfNTP.setContactInfo('')
if mibBuilder.loadTexts: hpnicfNTP.setDescription('This MIB provides mechanisms to monitor a NTP server.')
hpnicfNTPSystemMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1))
hpnicfNTPSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1))
hpnicfNTPSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysLeap.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysLeap.setDescription('Leap Indicator (LI): This is a two-bit code warning of an impending leap second to be inserted/deleted in the last minute of the current day, with bit 0 and bit 1, respectively, coded as follows: 00, no warning 01, last minute has 61 seconds 10, last minute has 59 seconds) 11, alarm condition (clock not synchronized).')
hpnicfNTPSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysStratum.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysStratum.setDescription('This is an eight-bit integer indicating the stratum level of the local clock, with values defined as follows: 0, unspecified 1, primary reference (e.g.,, radio clock) 2-255, secondary reference (via NTP)')
hpnicfNTPSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysPrecision.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysPrecision.setDescription('Precision : This is a signed integer indicating the precision of the various clocks, in seconds to the nearest power of two. The value must be rounded to the next larger power of two; for instance, a 50-Hz (20 ms) or 60-Hz (16.67ms) power-frequency clock would be assigned the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled clock would be assigned the value -9 (1.95 ms).')
hpnicfNTPSysRootdelay = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysRootdelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysRootdelay.setDescription('Root Delay : This is a signed fixed-point number indicating the total roundtrip delay to the primary reference source at the root of the synchronization subnet, in milliseconds. Note that this variable can take on both positive and negative values, depending on clock precision and skew.')
hpnicfNTPSysRootdispersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysRootdispersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysRootdispersion.setDescription('Root Dispersion : This is a signed fixed-point number indicating the maximum error relative to the primary reference source at the root of the synchronization subnet, in milliseconds. Only positive values greater than zero are possible.')
hpnicfNTPSysRefid = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysRefid.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysRefid.setDescription('Reference Clock Identifier : This is a 32-bit code identifying the particular reference clock. In the case of stratum 0 (unspecified) or stratum 1 (primary reference source), this is a four-octet, left-justified, zero-padded ASCII string. Stratum, Code, Meaning 0, DCN, DCN routing protocol 0, TSP, TSP time protocol 1, ATOM, Atomic clock (calibrated) 1, WWVB, WWVB LF (band 5) radio 1, GOES, GOES UHF (band 9) satellite 1, WWV, WWV HF (band 7) radio')
hpnicfNTPSysReftime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysReftime.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysReftime.setDescription('Reference Timestamp : This is the local time, in timestamp format, when the local clock was last updated. If the local clock has never been synchronized, the value is zero.')
hpnicfNTPSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysPoll.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysPoll.setDescription('Poll Interval : This is a signed integer indicating the minimum interval between transmitted messages, in seconds as a power of two. For instance, a value of six indicates a minimum interval of 64 seconds.')
hpnicfNTPSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysPeer.setStatus('obsolete')
if mibBuilder.loadTexts: hpnicfNTPSysPeer.setDescription('This is a selector identifying the current synchronization source. Usually this will be a pointer to a structure containing the peer variables. The special value NULL indicates There is no currently valid synchronization source. hpnicfNTPSysPeer is replaced by hpnicfNTPSysSrcPeer. Reading hpnicfNTPSysPeer might fail because the syntax value range is limited, for example, when the synchronization source IP address is a Class C address.')
hpnicfNTPSysState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noUpdateClock", 0), ("getfreqInfo", 1), ("clockBySet", 2), ("clockBySetAndNoFreq", 3), ("clockBySyns", 4), ("findError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysState.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysState.setDescription('This is a integer indicating the state of local clock.')
hpnicfNTPSysOffset = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysOffset.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysOffset.setDescription('The offset of two clocks is the time difference between them, in milliseconds.')
hpnicfNTPSysDrift = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysDrift.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysDrift.setDescription('Real clocks exhibit some variation in skew (second derivative of offset with time), which is called drift.')
hpnicfNTPSysCompliance = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysCompliance.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysCompliance.setDescription('This is a string indicating the system error.')
hpnicfNTPSysClock = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysClock.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysClock.setDescription('This is the current local time, in timestamp format. Local time is derived from the hardware clock of the particular machine and increments at intervals depending on the design used.')
hpnicfNTPSysStabil = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysStabil.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysStabil.setDescription('This is a indicating that stability of a clock is how well it can maintain a constant frequency.')
hpnicfNTPSysAuthenticate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noAuthenticate", 0), ("authenticate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNTPSysAuthenticate.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysAuthenticate.setDescription('This is a integer indicating that system support authentication.')
hpnicfNTPSysPollSec = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 1048576))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNTPSysPollSec.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysPollSec.setDescription('PollSec Interval : This is a integer indicating the minimum interval between transmitted messages. For instance, a value of six indicates a minimum interval of 6 seconds.')
hpnicfNTPSysClockSec = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysClockSec.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysClockSec.setDescription('This is the current local time, in integer format. Local time is derived from the hardware clock of the particular machine and increments at intervals depending on the design used.')
hpnicfNTPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNTPServerIP.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPServerIP.setDescription('The NTP server ip address. It must be a unicast address, rather than a broadcast address, a multicast address or the IP address of the local clock. To delete a configured NTP server ip address, please set hpnicfNTPServerIP to 0.')
hpnicfNTPSysSrcPeer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPSysSrcPeer.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPSysSrcPeer.setDescription('This is a selector identifying the current synchronization source. Usually this will be a unsigned integer containing the peer variables. The special value 0 indicates There is no currently valid synchronization source. This node will replace hpnicfNTPSysPeer, because its value range is unlimited, and data type is changed from Integer32 to Unsigned32.')
hpnicfNTPPeerMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2))
hpnicfNTPPeerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1))
hpnicfNTPPeerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1), )
if mibBuilder.loadTexts: hpnicfNTPPeerTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerTable.setDescription('This table provides information on the peers with which the local NTP server has associations. The peers are also NTP servers but running on different hosts.')
hpnicfNTPPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-NTP-MIB", "hpnicfNTPPeerRemAdr"), (0, "HPN-ICF-NTP-MIB", "hpnicfNTPPeerHMode"))
if mibBuilder.loadTexts: hpnicfNTPPeerEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerEntry.setDescription("Each peers' entry provides NTP information retrieved from a particular peer NTP server. Each peer is identified by a unique association identifier. Entries are automatically created when the user configures the NTP server to be associated with remote peers. Similarly entries are deleted when the user removes the peer association from the NTP server. Entries can also be created by the management station by setting values for the following objects: hpnicfNTPPeerRemAdr and making the hpnicfNTPPeerRowStatus as 'active'. At the least, the management station has to set a value for hpnicfNTPPeerRemAdr to make the row active.")
hpnicfNTPPeerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerConfig.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerConfig.setDescription('This is a bit indicating that the association was created from configuration information and should not be demobilized if the peer becomes unreachable.')
hpnicfNTPPeerAuthenable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerAuthenable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerAuthenable.setDescription('This is a bit indicating that system support authentication.')
hpnicfNTPPeerAuthentic = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerAuthentic.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerAuthentic.setDescription('This is a bit indicating that massage pass authentication which is authentic.')
hpnicfNTPPeerRemAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: hpnicfNTPPeerRemAdr.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRemAdr.setDescription('The IP address of the peer. When creating a new association, a value for this object should be set before the row is made active.')
hpnicfNTPPeerRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRemPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRemPort.setDescription('The UDP port number on which the peer receives NTP messages.')
hpnicfNTPPeerLocAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerLocAdr.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerLocAdr.setDescription('The IP address of the local host. Multi-homing can be supported using this object.')
hpnicfNTPPeerLocPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerLocPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerLocPort.setDescription('The UDP port number on which the local host receives NTP messages.')
hpnicfNTPPeerLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerLeap.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerLeap.setDescription('This is a two-bit code warning of an impending leap second to be inserted in the NTP timescale. The bits are set before 23:59 on the day of insertion and reset after 00:00 on the following day. This causes the number of seconds (rollover interval) in the day of insertion to be increased or decreased by one. The two bits are coded as below, 00, no warning 01, last minute has 61 seconds 10, last minute has 59 seconds 11, alarm condition (clock not synchronized)')
hpnicfNTPPeerHMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7), ("broadcastclient", 8), ("multicastclient", 9))))
if mibBuilder.loadTexts: hpnicfNTPPeerHMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerHMode.setDescription('This is an integer indicating the association mode, with values coded as follows, 0, unspecified 1, symmetric active - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of its peer. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 2, symmetric passive - This type of association is ordinarily created upon arrival of a message from a peer operating in the symmetric active mode and persists only as long as the peer is reachable and operating at a stratum level less than or equal to the host; otherwise, the association is dissolved. However, the association will always persist until at least one message has been sent in reply. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 3, client - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of its peer. By operating in this mode the host, usually a LAN workstation, announces its willingness to be synchronized by, but not to synchronize the peer 4, server - This type of association is ordinarily created upon arrival of a client request message and exists only in order to reply to that request, after which the association is dissolved. By operating in this mode the host, usually a LAN time server, announces its willingness to synchronize, but not to be synchronized by the peer 5, broadcast - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of the peers. By operating in this mode the host, usually a LAN time server operating on a high-speed broadcast medium, announces its willingness to synchronize all of the peers, but not to be synchronized by any of them 6, reserved for NTP control messages 7, reserved for private use 8, broadcastclient 9, multicastclient')
hpnicfNTPPeerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerStratum.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerStratum.setDescription('This is a integer indicating the stratum level of the peer clock, with values defined as follows: 0, unspecified 1, primary reference (e.g.,, radio clock) 2-255, secondary reference (via NTP)')
hpnicfNTPPeerPPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerPPoll.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerPPoll.setDescription('The interval at which the peer polls the local host.')
hpnicfNTPPeerHPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerHPoll.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerHPoll.setDescription('The interval at which the local host polls the peer.')
hpnicfNTPPeerPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerPrecision.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerPrecision.setDescription('This is a signed integer indicating the precision of the peer clock, in seconds to the nearest power of two. The value must be rounded to the next larger power of two; for instance, a 50-Hz (20 ms) or 60-Hz (16.67 ms) power-frequency clock would be assigned the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled clock would be assigned the value -9 (1.95 ms).')
hpnicfNTPPeerRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRootDelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRootDelay.setDescription('This is a signed fixed-point number indicating the total roundtrip delay to the primary reference source at the root of the synchronization subnet, in milliseconds. Note that this variable can take on both positive and negative values, depending on clock precision and skew.')
hpnicfNTPPeerRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRootDispersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRootDispersion.setDescription('This is a signed fixed-point number indicating the maximum error of the peer clock relative to the primary reference source at the root of the synchronization subnet, in milliseconds. Only positive values greater than zero are possible.')
hpnicfNTPPeerRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRefId.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRefId.setDescription('The reference identifier of the peer. This is a 32-bit code identifying the particular reference clock. In the case of stratum 0 (unspecified) or stratum 1 (primary reference source), this is a four-octet, left-justified, zero-padded ASCII string. Stratum, Code, Meaning 0, DCN, DCN routing protocol 0, TSP, TSP time protocol 1, ATOM, Atomic clock (calibrated) 1, WWVB, WWVB LF (band 5) radio 1, GOES, GOES UHF (band 9) satellite 1, WWV, WWV HF (band 7) radio')
hpnicfNTPPeerRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRefTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRefTime.setDescription('This is the local time at the peer, in timestamp format, when the local clock was last updated. If the local clock has never been synchronized, the value is zero.')
hpnicfNTPPeerOrg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerOrg.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerOrg.setDescription("This is the local time, in timestamp format, at the peer when it's latest NTP message was sent. If the peer becomes unreachable the value is set to zero")
hpnicfNTPPeerRec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerRec.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRec.setDescription('This is the local time, in timestamp format, when the latest NTP message from the peer arrived. If the peer becomes unreachable the value is set to zero.')
hpnicfNTPPeerXmt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerXmt.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerXmt.setDescription('This is the local time, in timestamp format, at which the NTP message departed the sender.')
hpnicfNTPPeerReach = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerReach.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerReach.setDescription('This is a shift register of NTP.WINDOW bits used to determine the reach ability status of the peer, with bits entering from the least significant (rightmost) end. A peer is considered reachable if at least one bit in this register is set to one')
hpnicfNTPPeerValid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerValid.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerValid.setDescription('This is an integer counter indicating the valid samples remaining in the filter register. It is used to determine the reach ability state and when the poll interval should be increased or decreased.')
hpnicfNTPPeerTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerTimer.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerTimer.setDescription('This is an integer counter used to control the interval of transmitted NTP messages from the local host to the peer.')
hpnicfNTPPeerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerDelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerDelay.setDescription('This is a signed fixed-point number indicating the roundtrip delay of the peer clock relative to the local clock over the network path between them, in milliseconds. Note that this variable can take on both positive and negative values, depending on clock precision and skew-error accumulation.')
hpnicfNTPPeerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerOffset.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerOffset.setDescription('This is a signed, fixed-point number indicating the offset of the peer clock relative to the local clock, in milliseconds.')
hpnicfNTPPeerJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerJitter.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerJitter.setDescription('This is an indicating that peer of sample Variance')
hpnicfNTPPeerDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 27), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerDispersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerDispersion.setDescription('This is a signed fixed-point number indicating the maximum error of the peer clock relative to the local clock over the network path between them, in milliseconds. Only positive values greater than zero are possible.')
hpnicfNTPPeerKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerKeyId.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerKeyId.setDescription('This is an unsigned integer identifying the cryptographic key used to generate the message-authentication code.')
hpnicfNTPPeerFiltDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerFiltDelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerFiltDelay.setDescription('Round-trip delay of the peer clock relative to the local clock over the network path between them, in milliseconds. This variable can take on both positive and negative values, depending on clock precision and skew-error accumulation.')
hpnicfNTPPeerFiltOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerFiltOffset.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerFiltOffset.setDescription('The offset of the peer clock relative to the local clock in milliseconds.')
hpnicfNTPPeerFiltError = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerFiltError.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerFiltError.setDescription('The maximum error of the peer clock relative to the local clock over the network path between them, in milliseconds. Only positive values greater than zero are possible.')
hpnicfNTPPeerPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7), ("broadcastclient", 8), ("multicastclient", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerPMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerPMode.setDescription("This is an integer indicating the association mode, with values coded as follows, 0, unspecified 1, symmetric active - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of its peer. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 2, symmetric passive - This type of association is ordinarily created upon arrival of a message from a peer operating in the symmetric active mode and persists only as long as the peer is reachable and operating at a stratum level less than or equal to the host; otherwise, the association is dissolved. However, the association will always persist until at least one message has been sent in reply. By operating in this mode the host announces its willingness to synchronize and be synchronized by the peer 3, client - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of its peer. By operating in this mode the host, usually a LAN workstation, announces its willingness to be synchronized by, but not to synchronize the peer 4, server - This type of association is ordinarily created upon arrival of a client request message and exists only in order to reply to that request, after which the association is dissolved. By operating in this mode the host, usually a LAN time server, announces its willingness to synchronize, but not to be synchronized by the peer 5, broadcast - A host operating in this mode sends periodic messages regardless of the reach ability state or stratum of the peers. By operating in this mode the host, usually a LAN time server operating on a high-speed broadcast medium, announces its willingness to synchronize all of the peers, but not to be synchronized by any of them 6, reserved for NTP control messages 7, reserved for private use 8, broadcastclient 9, multicastclient When creating a new peer association, if no value is specified for this object, it defaults to 'symmetricActive'.")
hpnicfNTPPeerReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerReceived.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerReceived.setDescription('The number of received massages.')
hpnicfNTPPeerSent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerSent.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerSent.setDescription('The number of send massages.')
hpnicfNTPPeerFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 35), Bits().clone(namedValues=NamedValues(("recvRepeatMsg", 0), ("recvremanMsg", 1), ("unSynMsg", 2), ("dispBeyond", 3), ("unauthenticate", 4), ("unSynClock", 5), ("straBeyond", 6), ("rootDispBeyond", 7), ("noAuthen", 8), ("refuOperate", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNTPPeerFlash.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerFlash.setDescription('The information about the massage.')
hpnicfNTPPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 36), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNTPPeerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfNTPPeerRowStatus.setDescription("The status object for this row. When a management station is creating a new row, it should set the value for cntpPeersPeerAddress at least, before the row can be made 'active'.")
mibBuilder.exportSymbols("HPN-ICF-NTP-MIB", hpnicfNTPPeerOrg=hpnicfNTPPeerOrg, hpnicfNTPPeerDispersion=hpnicfNTPPeerDispersion, hpnicfNTPPeerEntry=hpnicfNTPPeerEntry, hpnicfNTPSysLeap=hpnicfNTPSysLeap, hpnicfNTPPeerJitter=hpnicfNTPPeerJitter, hpnicfNTPPeerRefTime=hpnicfNTPPeerRefTime, hpnicfNTPPeerFiltOffset=hpnicfNTPPeerFiltOffset, hpnicfNTPPeerSent=hpnicfNTPPeerSent, hpnicfNTPSysRootdispersion=hpnicfNTPSysRootdispersion, hpnicfNTPSysState=hpnicfNTPSysState, hpnicfNTPPeerMIB=hpnicfNTPPeerMIB, hpnicfNTPPeerReceived=hpnicfNTPPeerReceived, hpnicfNTPSysStratum=hpnicfNTPSysStratum, hpnicfNTPSysClockSec=hpnicfNTPSysClockSec, hpnicfNTPPeerLocAdr=hpnicfNTPPeerLocAdr, hpnicfNTPPeerPrecision=hpnicfNTPPeerPrecision, hpnicfNTPPeerRootDispersion=hpnicfNTPPeerRootDispersion, hpnicfNTPPeerPMode=hpnicfNTPPeerPMode, hpnicfNTPPeerRefId=hpnicfNTPPeerRefId, hpnicfNTPPeerReach=hpnicfNTPPeerReach, hpnicfNTPPeerFiltError=hpnicfNTPPeerFiltError, hpnicfNTP=hpnicfNTP, hpnicfNTPPeerXmt=hpnicfNTPPeerXmt, PYSNMP_MODULE_ID=hpnicfNTP, hpnicfNTPSysRootdelay=hpnicfNTPSysRootdelay, hpnicfNTPSysPoll=hpnicfNTPSysPoll, hpnicfNTPPeerAuthenable=hpnicfNTPPeerAuthenable, hpnicfNTPPeerValid=hpnicfNTPPeerValid, hpnicfNTPSysClock=hpnicfNTPSysClock, hpnicfNTPPeerLocPort=hpnicfNTPPeerLocPort, hpnicfNTPPeerHPoll=hpnicfNTPPeerHPoll, hpnicfNTPPeerTimer=hpnicfNTPPeerTimer, hpnicfNTPPeerKeyId=hpnicfNTPPeerKeyId, hpnicfNTPPeerRemPort=hpnicfNTPPeerRemPort, hpnicfNTPSysAuthenticate=hpnicfNTPSysAuthenticate, hpnicfNTPSysSrcPeer=hpnicfNTPSysSrcPeer, hpnicfNTPPeerFlash=hpnicfNTPPeerFlash, hpnicfNTPServerIP=hpnicfNTPServerIP, hpnicfNTPPeerRowStatus=hpnicfNTPPeerRowStatus, hpnicfNTPSysOffset=hpnicfNTPSysOffset, hpnicfNTPPeerStratum=hpnicfNTPPeerStratum, hpnicfNTPPeerRemAdr=hpnicfNTPPeerRemAdr, hpnicfNTPSysPeer=hpnicfNTPSysPeer, hpnicfNTPPeerTable=hpnicfNTPPeerTable, hpnicfNTPPeerOffset=hpnicfNTPPeerOffset, hpnicfNTPSysStabil=hpnicfNTPSysStabil, hpnicfNTPSystemMIB=hpnicfNTPSystemMIB, hpnicfNTPSysCompliance=hpnicfNTPSysCompliance, hpnicfNTPPeerRootDelay=hpnicfNTPPeerRootDelay, hpnicfNTPPeerRec=hpnicfNTPPeerRec, hpnicfNTPPeerDelay=hpnicfNTPPeerDelay, hpnicfNTPSysPollSec=hpnicfNTPSysPollSec, hpnicfNTPSysReftime=hpnicfNTPSysReftime, hpnicfNTPPeerLeap=hpnicfNTPPeerLeap, hpnicfNTPSysRefid=hpnicfNTPSysRefid, hpnicfNTPPeerConfig=hpnicfNTPPeerConfig, hpnicfNTPSysPrecision=hpnicfNTPSysPrecision, hpnicfNTPSystemMIBObjects=hpnicfNTPSystemMIBObjects, hpnicfNTPPeerPPoll=hpnicfNTPPeerPPoll, hpnicfNTPPeerFiltDelay=hpnicfNTPPeerFiltDelay, hpnicfNTPPeerHMode=hpnicfNTPPeerHMode, hpnicfNTPSysDrift=hpnicfNTPSysDrift, hpnicfNTPPeerAuthentic=hpnicfNTPPeerAuthentic, hpnicfNTPPeerMIBObjects=hpnicfNTPPeerMIBObjects)