#
# PySNMP MIB module ASTERISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASTERISK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
digium, = mibBuilder.importSymbols("DIGIUM-MIB", "digium")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, MibIdentifier, Counter32, Counter64, Unsigned32, Gauge32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "Gauge32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "TimeTicks")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
asterisk = ModuleIdentity((1, 3, 6, 1, 4, 1, 22736, 1))
asterisk.setRevisions(('2008-06-20 20:25', '2007-08-21 14:50', '2006-03-06 18:40', '2006-02-04 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: asterisk.setRevisionsDescriptions(('smilint police -- Add missing imports; fix initial capitalization of enumeration elements; add missing range restrictions for Integer32 indices, correct spelling of astChanCidANI in its definition. Addresses bug 12905. - jeffg@opennms.org', 'Add total and current call counter statistics.', 'Change audio codec identification from 3kAudio to Audio3k to conform better with specification. Expand on contact information.', 'Initial published revision.',))
if mibBuilder.loadTexts: asterisk.setLastUpdated('200806202025Z')
if mibBuilder.loadTexts: asterisk.setOrganization('Digium, Inc.')
if mibBuilder.loadTexts: asterisk.setContactInfo('Mark A. Spencer Postal: Digium, Inc. 445 Jan Davis Drive Huntsville, AL 35806 USA Tel: +1 256 428 6000 Email: markster@digium.com Thorsten Lockert Postal: Voop AS Boehmergaten 42 NO-5057 Bergen Norway Tel: +47 5598 7200 Email: tholo@voop.no')
if mibBuilder.loadTexts: asterisk.setDescription('Asterisk is an Open Source PBX. This MIB defined objects for managing Asterisk instances.')
asteriskVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 1))
asteriskConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 2))
asteriskModules = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 3))
asteriskIndications = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 4))
asteriskChannels = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 5))
astVersionString = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astVersionString.setStatus('current')
if mibBuilder.loadTexts: astVersionString.setDescription('Text version string of the version of Asterisk that the SNMP Agent was compiled to run against.')
astVersionTag = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astVersionTag.setStatus('current')
if mibBuilder.loadTexts: astVersionTag.setDescription('SubVersion revision of the version of Asterisk that the SNMP Agent was compiled to run against -- this is typically 0 for release-versions of Asterisk.')
astConfigUpTime = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigUpTime.setStatus('current')
if mibBuilder.loadTexts: astConfigUpTime.setDescription('Time ticks since Asterisk was started.')
astConfigReloadTime = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigReloadTime.setStatus('current')
if mibBuilder.loadTexts: astConfigReloadTime.setDescription('Time ticks since Asterisk was last reloaded.')
astConfigPid = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigPid.setStatus('current')
if mibBuilder.loadTexts: astConfigPid.setDescription('The process id of the running Asterisk process.')
astConfigSocket = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigSocket.setStatus('current')
if mibBuilder.loadTexts: astConfigSocket.setDescription('The control socket for giving Asterisk commands.')
astConfigCallsActive = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigCallsActive.setStatus('current')
if mibBuilder.loadTexts: astConfigCallsActive.setDescription('The number of calls currently active on the Asterisk PBX.')
astConfigCallsProcessed = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astConfigCallsProcessed.setStatus('current')
if mibBuilder.loadTexts: astConfigCallsProcessed.setDescription('The total number of calls processed through the Asterisk PBX since last restart.')
astNumModules = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumModules.setStatus('current')
if mibBuilder.loadTexts: astNumModules.setDescription('Number of modules currently loaded into Asterisk.')
astNumIndications = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumIndications.setStatus('current')
if mibBuilder.loadTexts: astNumIndications.setDescription('Number of indications currently defined in Asterisk.')
astCurrentIndication = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astCurrentIndication.setStatus('current')
if mibBuilder.loadTexts: astCurrentIndication.setDescription('Default indication zone to use.')
astIndicationsTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3), )
if mibBuilder.loadTexts: astIndicationsTable.setStatus('current')
if mibBuilder.loadTexts: astIndicationsTable.setDescription('Table with all the indication zones currently know to the running Asterisk instance.')
astIndicationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1), ).setIndexNames((0, "ASTERISK-MIB", "astIndIndex"))
if mibBuilder.loadTexts: astIndicationsEntry.setStatus('current')
if mibBuilder.loadTexts: astIndicationsEntry.setDescription('Information about a single indication zone.')
astIndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndIndex.setStatus('current')
if mibBuilder.loadTexts: astIndIndex.setDescription('Numerical index into the table of indication zones.')
astIndCountry = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndCountry.setStatus('current')
if mibBuilder.loadTexts: astIndCountry.setDescription('Country for which the indication zone is valid, typically this is the ISO 2-letter code of the country.')
astIndAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndAlias.setStatus('current')
if mibBuilder.loadTexts: astIndAlias.setDescription('')
astIndDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 4, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astIndDescription.setStatus('current')
if mibBuilder.loadTexts: astIndDescription.setDescription('Description of the indication zone, usually the full name of the country it is valid for.')
astNumChannels = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChannels.setStatus('current')
if mibBuilder.loadTexts: astNumChannels.setDescription('Current number of active channels.')
astChanTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2), )
if mibBuilder.loadTexts: astChanTable.setStatus('current')
if mibBuilder.loadTexts: astChanTable.setDescription('Table with details of the currently active channels in the Asterisk instance.')
astChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1), ).setIndexNames((0, "ASTERISK-MIB", "astChanIndex"))
if mibBuilder.loadTexts: astChanEntry.setStatus('current')
if mibBuilder.loadTexts: astChanEntry.setDescription('Details of a single channel.')
astChanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanIndex.setStatus('current')
if mibBuilder.loadTexts: astChanIndex.setDescription('Index into the channel table.')
astChanName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanName.setStatus('current')
if mibBuilder.loadTexts: astChanName.setDescription('Name of the current channel.')
astChanLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanLanguage.setStatus('current')
if mibBuilder.loadTexts: astChanLanguage.setDescription('Which language the current channel is configured to use -- used mainly for prompts.')
astChanType = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanType.setStatus('current')
if mibBuilder.loadTexts: astChanType.setDescription('Underlying technology for the current channel.')
astChanMusicClass = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMusicClass.setStatus('current')
if mibBuilder.loadTexts: astChanMusicClass.setDescription('Music class to be used for Music on Hold for this channel.')
astChanBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanBridge.setStatus('current')
if mibBuilder.loadTexts: astChanBridge.setDescription('Which channel this channel is currently bridged (in a conversation) with.')
astChanMasq = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMasq.setStatus('current')
if mibBuilder.loadTexts: astChanMasq.setDescription('Channel masquerading for us.')
astChanMasqr = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMasqr.setStatus('current')
if mibBuilder.loadTexts: astChanMasqr.setDescription('Channel we are masquerading for.')
astChanWhenHangup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanWhenHangup.setStatus('current')
if mibBuilder.loadTexts: astChanWhenHangup.setDescription('How long until this channel will be hung up.')
astChanApp = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanApp.setStatus('current')
if mibBuilder.loadTexts: astChanApp.setDescription('Current application for the channel.')
astChanData = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanData.setStatus('current')
if mibBuilder.loadTexts: astChanData.setDescription('Arguments passed to the current application.')
astChanContext = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanContext.setStatus('current')
if mibBuilder.loadTexts: astChanContext.setDescription('Current extension context.')
astChanMacroContext = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroContext.setStatus('current')
if mibBuilder.loadTexts: astChanMacroContext.setDescription('Current macro context.')
astChanMacroExten = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroExten.setStatus('current')
if mibBuilder.loadTexts: astChanMacroExten.setDescription('Current macro extension.')
astChanMacroPri = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMacroPri.setStatus('current')
if mibBuilder.loadTexts: astChanMacroPri.setDescription('Current macro priority.')
astChanExten = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanExten.setStatus('current')
if mibBuilder.loadTexts: astChanExten.setDescription('Current extension.')
astChanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanPri.setStatus('current')
if mibBuilder.loadTexts: astChanPri.setDescription('Current priority.')
astChanAccountCode = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanAccountCode.setStatus('current')
if mibBuilder.loadTexts: astChanAccountCode.setDescription('Account Code for billing.')
astChanForwardTo = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanForwardTo.setStatus('current')
if mibBuilder.loadTexts: astChanForwardTo.setDescription('Where to forward to if asked to dial on this interface.')
astChanUniqueId = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanUniqueId.setStatus('current')
if mibBuilder.loadTexts: astChanUniqueId.setDescription('Unique Channel Identifier.')
astChanCallGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCallGroup.setStatus('current')
if mibBuilder.loadTexts: astChanCallGroup.setDescription('Call Group.')
astChanPickupGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanPickupGroup.setStatus('current')
if mibBuilder.loadTexts: astChanPickupGroup.setDescription('Pickup Group.')
astChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("stateDown", 0), ("stateReserved", 1), ("stateOffHook", 2), ("stateDialing", 3), ("stateRing", 4), ("stateRinging", 5), ("stateUp", 6), ("stateBusy", 7), ("stateDialingOffHook", 8), ("statePreRing", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanState.setStatus('current')
if mibBuilder.loadTexts: astChanState.setDescription('Channel state.')
astChanMuted = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanMuted.setStatus('current')
if mibBuilder.loadTexts: astChanMuted.setDescription('Transmission of voice data has been muted.')
astChanRings = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanRings.setStatus('current')
if mibBuilder.loadTexts: astChanRings.setDescription('Number of rings so far.')
astChanCidDNID = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidDNID.setStatus('current')
if mibBuilder.loadTexts: astChanCidDNID.setDescription('Dialled Number ID.')
astChanCidNum = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidNum.setStatus('current')
if mibBuilder.loadTexts: astChanCidNum.setDescription('Caller Number.')
astChanCidName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidName.setStatus('current')
if mibBuilder.loadTexts: astChanCidName.setDescription('Caller Name.')
astChanCidANI = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidANI.setStatus('current')
if mibBuilder.loadTexts: astChanCidANI.setDescription('ANI')
astChanCidRDNIS = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidRDNIS.setStatus('current')
if mibBuilder.loadTexts: astChanCidRDNIS.setDescription('Redirected Dialled Number Service.')
astChanCidPresentation = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidPresentation.setStatus('current')
if mibBuilder.loadTexts: astChanCidPresentation.setDescription('Number Presentation/Screening.')
astChanCidANI2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidANI2.setStatus('current')
if mibBuilder.loadTexts: astChanCidANI2.setDescription('ANI 2 (info digit).')
astChanCidTON = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidTON.setStatus('current')
if mibBuilder.loadTexts: astChanCidTON.setDescription('Type of Number.')
astChanCidTNS = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanCidTNS.setStatus('current')
if mibBuilder.loadTexts: astChanCidTNS.setDescription('Transit Network Select.')
astChanAMAFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("default", 0), ("omit", 1), ("billing", 2), ("documentation", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanAMAFlags.setStatus('current')
if mibBuilder.loadTexts: astChanAMAFlags.setDescription('AMA Flags.')
astChanADSI = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("available", 1), ("unavailable", 2), ("offHookOnly", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanADSI.setStatus('current')
if mibBuilder.loadTexts: astChanADSI.setDescription('Whether or not ADSI is detected on CPE.')
astChanToneZone = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanToneZone.setStatus('current')
if mibBuilder.loadTexts: astChanToneZone.setDescription('Indication zone to use for channel.')
astChanHangupCause = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 16, 17, 19, 34, 38, 66))).clone(namedValues=NamedValues(("notDefined", 0), ("unregistered", 3), ("normal", 16), ("busy", 17), ("noAnswer", 19), ("congestion", 34), ("failure", 38), ("noSuchDriver", 66)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanHangupCause.setStatus('current')
if mibBuilder.loadTexts: astChanHangupCause.setDescription('Why is the channel hung up.')
astChanVariables = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanVariables.setStatus('current')
if mibBuilder.loadTexts: astChanVariables.setDescription('Channel Variables defined for this channel.')
astChanFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 40), Bits().clone(namedValues=NamedValues(("wantsJitter", 0), ("deferDTMF", 1), ("writeInterrupt", 2), ("blocking", 3), ("zombie", 4), ("exception", 5), ("musicOnHold", 6), ("spying", 7), ("nativeBridge", 8), ("autoIncrementingLoop", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanFlags.setStatus('current')
if mibBuilder.loadTexts: astChanFlags.setDescription('Flags set on this channel.')
astChanTransferCap = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 2, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8, 9, 16, 17, 24))).clone(namedValues=NamedValues(("speech", 0), ("digital", 8), ("restrictedDigital", 9), ("audio3k", 16), ("digitalWithTones", 17), ("video", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTransferCap.setStatus('current')
if mibBuilder.loadTexts: astChanTransferCap.setDescription('Transfer Capabilities for this channel.')
astNumChanTypes = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChanTypes.setStatus('current')
if mibBuilder.loadTexts: astNumChanTypes.setDescription('Number of channel types (technologies) supported.')
astChanTypeTable = MibTable((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4), )
if mibBuilder.loadTexts: astChanTypeTable.setStatus('current')
if mibBuilder.loadTexts: astChanTypeTable.setDescription('Table with details of the supported channel types.')
astChanTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1), ).setIndexNames((0, "ASTERISK-MIB", "astChanTypeIndex"))
if mibBuilder.loadTexts: astChanTypeEntry.setStatus('current')
if mibBuilder.loadTexts: astChanTypeEntry.setDescription('Information about a technology we support, including how many channels are currently using this technology.')
astChanTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeIndex.setStatus('current')
if mibBuilder.loadTexts: astChanTypeIndex.setDescription('Index into the table of channel types.')
astChanTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeName.setStatus('current')
if mibBuilder.loadTexts: astChanTypeName.setDescription('Unique name of the technology we are describing.')
astChanTypeDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeDesc.setStatus('current')
if mibBuilder.loadTexts: astChanTypeDesc.setDescription('Description of the channel type (technology).')
astChanTypeDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeDeviceState.setStatus('current')
if mibBuilder.loadTexts: astChanTypeDeviceState.setDescription('Whether the current technology can hold device states.')
astChanTypeIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeIndications.setStatus('current')
if mibBuilder.loadTexts: astChanTypeIndications.setDescription('Whether the current technology supports progress indication.')
astChanTypeTransfer = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeTransfer.setStatus('current')
if mibBuilder.loadTexts: astChanTypeTransfer.setDescription('Whether the current technology supports transfers, where Asterisk can get out from inbetween two bridged channels.')
astChanTypeChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 22736, 1, 5, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astChanTypeChannels.setStatus('current')
if mibBuilder.loadTexts: astChanTypeChannels.setDescription('Number of active channels using the current technology.')
astChanScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 22736, 1, 5, 5))
astNumChanBridge = MibScalar((1, 3, 6, 1, 4, 1, 22736, 1, 5, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: astNumChanBridge.setStatus('current')
if mibBuilder.loadTexts: astNumChanBridge.setDescription('Number of channels currently in a bridged state.')
mibBuilder.exportSymbols("ASTERISK-MIB", astChanFlags=astChanFlags, astChanHangupCause=astChanHangupCause, astChanTypeDeviceState=astChanTypeDeviceState, astChanTypeTable=astChanTypeTable, astChanMusicClass=astChanMusicClass, astChanADSI=astChanADSI, astChanCidANI2=astChanCidANI2, astConfigPid=astConfigPid, astChanType=astChanType, asteriskVersion=asteriskVersion, astIndCountry=astIndCountry, astChanCidNum=astChanCidNum, astChanTransferCap=astChanTransferCap, astChanPickupGroup=astChanPickupGroup, astChanCidPresentation=astChanCidPresentation, astConfigCallsProcessed=astConfigCallsProcessed, astIndicationsEntry=astIndicationsEntry, astChanBridge=astChanBridge, astChanForwardTo=astChanForwardTo, astNumChanBridge=astNumChanBridge, astChanName=astChanName, astNumChanTypes=astNumChanTypes, asteriskChannels=asteriskChannels, astChanCidTNS=astChanCidTNS, astChanAccountCode=astChanAccountCode, astChanRings=astChanRings, astChanIndex=astChanIndex, astChanTypeName=astChanTypeName, astChanCidRDNIS=astChanCidRDNIS, astChanCallGroup=astChanCallGroup, asterisk=asterisk, astChanCidDNID=astChanCidDNID, astChanTypeTransfer=astChanTypeTransfer, astNumIndications=astNumIndications, astChanTypeIndications=astChanTypeIndications, astConfigSocket=astConfigSocket, astChanApp=astChanApp, astIndDescription=astIndDescription, astChanWhenHangup=astChanWhenHangup, astChanCidTON=astChanCidTON, astVersionString=astVersionString, astChanMacroExten=astChanMacroExten, astChanTypeEntry=astChanTypeEntry, astIndAlias=astIndAlias, astChanMasq=astChanMasq, astChanMacroContext=astChanMacroContext, astChanMuted=astChanMuted, astChanCidANI=astChanCidANI, astChanCidName=astChanCidName, astChanToneZone=astChanToneZone, astNumModules=astNumModules, astChanMasqr=astChanMasqr, astChanEntry=astChanEntry, astCurrentIndication=astCurrentIndication, astConfigUpTime=astConfigUpTime, asteriskIndications=asteriskIndications, astChanTable=astChanTable, astConfigReloadTime=astConfigReloadTime, astNumChannels=astNumChannels, astChanPri=astChanPri, astChanUniqueId=astChanUniqueId, asteriskConfiguration=asteriskConfiguration, astChanTypeDesc=astChanTypeDesc, astChanTypeIndex=astChanTypeIndex, astChanData=astChanData, astChanScalars=astChanScalars, astChanVariables=astChanVariables, astChanState=astChanState, astChanLanguage=astChanLanguage, astChanAMAFlags=astChanAMAFlags, astChanTypeChannels=astChanTypeChannels, asteriskModules=asteriskModules, astChanContext=astChanContext, astIndIndex=astIndIndex, astVersionTag=astVersionTag, astChanExten=astChanExten, PYSNMP_MODULE_ID=asterisk, astChanMacroPri=astChanMacroPri, astConfigCallsActive=astConfigCallsActive, astIndicationsTable=astIndicationsTable)