#
# PySNMP MIB module HPN-ICF-VOICE-CALL-ACTIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VOICE-CALL-ACTIVE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
callActiveIndex, callActiveSetupTime = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "callActiveIndex", "callActiveSetupTime")
hpnicfVoice, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfVoice")
HpnicfCodecType, = mibBuilder.importSymbols("HPN-ICF-VOICE-DIAL-CONTROL-MIB", "HpnicfCodecType")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, IpAddress, Bits, Counter64, Unsigned32, NotificationType, Counter32, Integer32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "IpAddress", "Bits", "Counter64", "Unsigned32", "NotificationType", "Counter32", "Integer32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfVoCallActive = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15))
hpnicfVoCallActive.setRevisions(('2008-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfVoCallActive.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hpnicfVoCallActive.setLastUpdated('200802170000Z')
if mibBuilder.loadTexts: hpnicfVoCallActive.setOrganization('')
if mibBuilder.loadTexts: hpnicfVoCallActive.setContactInfo('')
if mibBuilder.loadTexts: hpnicfVoCallActive.setDescription('This MIB file is to provide the definition of voice call active record information.')
class HpnicfGUid(TextualConvention, OctetString):
    description = 'Represents a global call identifier. The global call identifier is used as an unique identifier for an end-to-end call. A zero length HpnicfGUid indicates no value for the global call identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

hpnicfVoiceCallActiveObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1))
hpnicfVoiceCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1), )
if mibBuilder.loadTexts: hpnicfVoiceCallActiveTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoiceCallActiveTable.setDescription('This table is the voice extension to the call active table of DIAL-CONTROL-MIB. It contains voice encapsulation call leg information that is derived from the statistics of lower layer telephony interface.')
hpnicfVoiceCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: hpnicfVoiceCallActiveEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoiceCallActiveEntry.setDescription('The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by call active table of DIAL-CONTROL-MIB to identify the call. An entry of this table is created when its associated call active entry in the DIAL-CONTROL-MIB is created and call active entry contains the call establishment to a voice over telephony network peer. The entry is deleted when its associated call active entry in the DIAL-CONTROL-MIB is deleted.')
hpnicfVoCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 1), HpnicfGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveConnectionId.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveConnectionId.setDescription('The global call identifier for the gateway call.')
hpnicfVoCallActiveTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveTxDuration.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveTxDuration.setDescription('Duration of transmit path open from this peer to the voice gateway for the call. The units is milliseconds.')
hpnicfVoCallActiveVoiceTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveVoiceTxDuration.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveVoiceTxDuration.setDescription('Duration of voice transmitted from this peer to voice gateway for this call. The voice utilization rate can be obtained by dividing this by hpnicfVoCallActiveTXDuration object. The units is milliseconds.')
hpnicfVoCallActiveFaxTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveFaxTxDuration.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveFaxTxDuration.setDescription('Duration of fax transmitted from this peer to voice gateway for this call. The fax utilization rate can be obtained by dividing this by hpnicfVoCallActiveTXDuration object. The units is milliseconds.')
hpnicfVoCallActiveCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 5), HpnicfCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveCoderType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveCoderType.setDescription('The negotiated coder type. It specifies the encode type to the PSTN leg of a call.')
hpnicfVoCallActiveImgPageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallActiveImgPageCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoCallActiveImgPageCount.setDescription('The number of fax related image pages are received or transmitted via the peer for the call. The units is pages.')
hpnicfVoiceVoIPCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2), )
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallActiveTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallActiveTable.setDescription('This table is the VoIP extension to the call active table of DIAL-CONTROL-MIB. It contains VoIP call leg information about specific VoIP call destination.')
hpnicfVoiceVoIPCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallActiveEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallActiveEntry.setDescription('The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by call active table of DIAL-CONTROL-MIB to identify the call. An entry of this table is created when its associated call active entry in the DIAL-CONTROL-MIB is created and the call active entry contains information for the call establishment to the peer on the IP backbone via a voice over IP peer. The entry is deleted when its associated call active entry in the DIAL-CONTROL-MIB is deleted.')
hpnicfVoVoIPCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 1), HpnicfGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveConnectionId.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveConnectionId.setDescription('The global call identifier for the gateway call.')
hpnicfVoVoIPCallActiveRemSigIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigIPType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigIPType.setDescription('The type of remote system signalling IP address for the VoIP call.')
hpnicfVoVoIPCallActiveRemSigIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigIPAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigIPAddr.setDescription('Remote system signalling IP address for the VoIP call.')
hpnicfVoVoIPCallActiveRemSigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemSigPort.setDescription('Remote system UDP listener signalling port to which to transmit voice packets.')
hpnicfVoVoIPCallActiveRemMedIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedIPType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedIPType.setDescription('The type of remote system media IP address for the VoIP call.')
hpnicfVoVoIPCallActiveRemMedIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedIPAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedIPAddr.setDescription('Remote system media IP address for the VoIP call.')
hpnicfVoVoIPCallActiveRemMedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveRemMedPort.setDescription('Remote system UDP listener media port to which to transmit voice packets.')
hpnicfVoVoIPCallActiveSessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("h323", 2), ("sip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveSessProtocol.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveSessProtocol.setDescription('The object specifies the session protocol to be used for internet call between local and remote router via IP backbone.')
hpnicfVoVoIPCallActiveCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 15, 1, 2, 1, 9), HpnicfCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveCoderType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVoVoIPCallActiveCoderType.setDescription('The negotiated coder type. It specifies the encode type to the VoIP leg of a call.')
mibBuilder.exportSymbols("HPN-ICF-VOICE-CALL-ACTIVE-MIB", hpnicfVoCallActiveTxDuration=hpnicfVoCallActiveTxDuration, hpnicfVoCallActiveVoiceTxDuration=hpnicfVoCallActiveVoiceTxDuration, hpnicfVoCallActive=hpnicfVoCallActive, hpnicfVoiceCallActiveEntry=hpnicfVoiceCallActiveEntry, hpnicfVoVoIPCallActiveSessProtocol=hpnicfVoVoIPCallActiveSessProtocol, hpnicfVoVoIPCallActiveCoderType=hpnicfVoVoIPCallActiveCoderType, hpnicfVoVoIPCallActiveRemSigIPType=hpnicfVoVoIPCallActiveRemSigIPType, hpnicfVoiceCallActiveObjects=hpnicfVoiceCallActiveObjects, hpnicfVoVoIPCallActiveRemSigIPAddr=hpnicfVoVoIPCallActiveRemSigIPAddr, hpnicfVoVoIPCallActiveRemMedPort=hpnicfVoVoIPCallActiveRemMedPort, hpnicfVoCallActiveImgPageCount=hpnicfVoCallActiveImgPageCount, hpnicfVoVoIPCallActiveRemMedIPAddr=hpnicfVoVoIPCallActiveRemMedIPAddr, hpnicfVoiceVoIPCallActiveTable=hpnicfVoiceVoIPCallActiveTable, PYSNMP_MODULE_ID=hpnicfVoCallActive, hpnicfVoVoIPCallActiveRemMedIPType=hpnicfVoVoIPCallActiveRemMedIPType, HpnicfGUid=HpnicfGUid, hpnicfVoCallActiveConnectionId=hpnicfVoCallActiveConnectionId, hpnicfVoVoIPCallActiveConnectionId=hpnicfVoVoIPCallActiveConnectionId, hpnicfVoCallActiveFaxTxDuration=hpnicfVoCallActiveFaxTxDuration, hpnicfVoCallActiveCoderType=hpnicfVoCallActiveCoderType, hpnicfVoiceCallActiveTable=hpnicfVoiceCallActiveTable, hpnicfVoVoIPCallActiveRemSigPort=hpnicfVoVoIPCallActiveRemSigPort, hpnicfVoiceVoIPCallActiveEntry=hpnicfVoiceVoIPCallActiveEntry)
