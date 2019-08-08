#
# PySNMP MIB module ALVARION-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-AAA-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionServerIndex, AlvarionProfileIndex, AlvarionServerIndexOrZero = mibBuilder.importSymbols("ALVARION-TC", "AlvarionServerIndex", "AlvarionProfileIndex", "AlvarionServerIndexOrZero")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, ObjectIdentity, IpAddress, iso, MibIdentifier, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Integer32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "IpAddress", "iso", "MibIdentifier", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Integer32", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5))
if mibBuilder.loadTexts: alvarionAAAClientMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionAAAClientMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionAAAClientMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionAAAClientMIB.setDescription('Alvarion AAA Client MIB file.')
alvarionAAAClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1))
alvarionAAAProfileGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1))
alvarionAAAServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2))
alvarionAAAProfileTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1), )
if mibBuilder.loadTexts: alvarionAAAProfileTable.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileTable.setDescription('A table defining the AAA server profiles currently configured on the device.')
alvarionAAAProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileIndex"))
if mibBuilder.loadTexts: alvarionAAAProfileEntry.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileEntry.setDescription('A AAA server profile configured in the device. alvarionAAAProfileIndex - Uniquely identifies the profile within the profile table.')
alvarionAAAProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 1), AlvarionProfileIndex())
if mibBuilder.loadTexts: alvarionAAAProfileIndex.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileIndex.setDescription('Specifies the index of the AAA server profile.')
alvarionAAAProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alvarionAAAProfileName.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileName.setDescription('Specifies the name of the AAA server profile.')
alvarionAAAProfilePrimaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 3), AlvarionServerIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAProfilePrimaryServerIndex.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfilePrimaryServerIndex.setDescription('Indicates the index number of the primary server profile in the table. A value of zero indicates that no AAA server is defined.')
alvarionAAAProfileSecondaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 1, 1, 1, 4), AlvarionServerIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAProfileSecondaryServerIndex.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileSecondaryServerIndex.setDescription('Indicates the index number of the secondary server profile in the table. A value of zero indicates that no AAA server is defined.')
alvarionAAAServerTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1), )
if mibBuilder.loadTexts: alvarionAAAServerTable.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAServerTable.setDescription('A table containing the AAA servers currently configured on the device.')
alvarionAAAServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-AAA-CLIENT-MIB", "alvarionAAAServerIndex"))
if mibBuilder.loadTexts: alvarionAAAServerEntry.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAServerEntry.setDescription('An AAA server configured on the device. alvarionAAAServerIndex - Uniquely identifies a server inside the server table.')
alvarionAAAServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 1), AlvarionServerIndex())
if mibBuilder.loadTexts: alvarionAAAServerIndex.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAServerIndex.setDescription('Specifies the index of the AAA server in the table.')
alvarionAAAAuthenProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("radius", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAAuthenProtocol.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAAuthenProtocol.setDescription('Indicates the protocol used by the AAA client to communicate with the AAA server.')
alvarionAAAAuthenMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("pap", 1), ("chap", 2), ("mschap", 3), ("mschapv2", 4), ("eapMd5", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAAuthenMethod.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAAuthenMethod.setDescription('Indicates the authentication method used by the AAA client to authenticate users via the AAA server.')
alvarionAAAServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alvarionAAAServerName.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAServerName.setDescription("Specifies the IP address of the AAA server. The string must be a valid IP address in the format 'nnn.nnn.nnn.nnn' Where 'nnn' is a number in the range [0..255]. The '.' character is mandatory between the fields.")
alvarionAAASharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alvarionAAASharedSecret.setStatus('current')
if mibBuilder.loadTexts: alvarionAAASharedSecret.setDescription('Specifies the shared secret used by the AAA client and the AAA server. This attribute should only be set if AAA traffic between the AAA client and server is sent through a VPN tunnel. Reading this attribute will always return a zero-length string.')
alvarionAAAAuthenticationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAAuthenticationPort.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAAuthenticationPort.setDescription('Indicates the port number used by the AAA client to send authentication requests to the AAA server.')
alvarionAAAAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAAAccountingPort.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAAccountingPort.setDescription('Indicates the port number used by the AAA client to send accounting information to the AAA server.')
alvarionAAATimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 100))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAATimeout.setStatus('current')
if mibBuilder.loadTexts: alvarionAAATimeout.setDescription('Indicates how long the AAA client will wait for an answer to an authentication request.')
alvarionAAANASId = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alvarionAAANASId.setStatus('current')
if mibBuilder.loadTexts: alvarionAAANASId.setDescription('Indicates the network access server ID to be sent by the AAA client in each authentication request sent to the AAA server.')
alvarionAAAClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2))
alvarionAAAClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 1))
alvarionAAAClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2))
alvarionAAAClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 1, 1)).setObjects(("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileMIBGroup"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionAAAClientMIBCompliance = alvarionAAAClientMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAClientMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion AAA client MIB.')
alvarionAAAProfileMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2, 1)).setObjects(("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileName"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfilePrimaryServerIndex"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAProfileSecondaryServerIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionAAAProfileMIBGroup = alvarionAAAProfileMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAProfileMIBGroup.setDescription('A collection of objects providing the AAA profile capability.')
alvarionAAAClientMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 5, 2, 2, 2)).setObjects(("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenProtocol"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenMethod"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAServerName"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAASharedSecret"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAuthenticationPort"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAAAccountingPort"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAATimeout"), ("ALVARION-AAA-CLIENT-MIB", "alvarionAAANASId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionAAAClientMIBGroup = alvarionAAAClientMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionAAAClientMIBGroup.setDescription('A collection of objects providing the AAA client MIB capability.')
mibBuilder.exportSymbols("ALVARION-AAA-CLIENT-MIB", alvarionAAAProfilePrimaryServerIndex=alvarionAAAProfilePrimaryServerIndex, alvarionAAAServerTable=alvarionAAAServerTable, alvarionAAAClientMIBGroup=alvarionAAAClientMIBGroup, alvarionAAAAuthenMethod=alvarionAAAAuthenMethod, alvarionAAAAuthenticationPort=alvarionAAAAuthenticationPort, alvarionAAAClientObjects=alvarionAAAClientObjects, PYSNMP_MODULE_ID=alvarionAAAClientMIB, alvarionAAAAccountingPort=alvarionAAAAccountingPort, alvarionAAAServerIndex=alvarionAAAServerIndex, alvarionAAANASId=alvarionAAANASId, alvarionAAAClientMIBConformance=alvarionAAAClientMIBConformance, alvarionAAAClientMIB=alvarionAAAClientMIB, alvarionAAAProfileIndex=alvarionAAAProfileIndex, alvarionAAASharedSecret=alvarionAAASharedSecret, alvarionAAAClientMIBCompliance=alvarionAAAClientMIBCompliance, alvarionAAAClientMIBGroups=alvarionAAAClientMIBGroups, alvarionAAAClientMIBCompliances=alvarionAAAClientMIBCompliances, alvarionAAAProfileEntry=alvarionAAAProfileEntry, alvarionAAAAuthenProtocol=alvarionAAAAuthenProtocol, alvarionAAAProfileTable=alvarionAAAProfileTable, alvarionAAAProfileName=alvarionAAAProfileName, alvarionAAAServerEntry=alvarionAAAServerEntry, alvarionAAAServerName=alvarionAAAServerName, alvarionAAATimeout=alvarionAAATimeout, alvarionAAAProfileMIBGroup=alvarionAAAProfileMIBGroup, alvarionAAAProfileGroup=alvarionAAAProfileGroup, alvarionAAAServerGroup=alvarionAAAServerGroup, alvarionAAAProfileSecondaryServerIndex=alvarionAAAProfileSecondaryServerIndex)