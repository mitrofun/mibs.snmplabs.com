#
# PySNMP MIB module SALIX-ANNOUNCEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-ANNOUNCEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
atmfM4TrapAlarmSeverity, = mibBuilder.importSymbols("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
DateAndTime, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "DateAndTime")
salixGeneric, = mibBuilder.importSymbols("SALIX-MIB", "salixGeneric")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ModuleIdentity, Integer32, Bits, ObjectIdentity, Gauge32, TimeTicks, Unsigned32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ModuleIdentity", "Integer32", "Bits", "ObjectIdentity", "Gauge32", "TimeTicks", "Unsigned32", "Counter64", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
salixAnnouncementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 6))
if mibBuilder.loadTexts: salixAnnouncementMIB.setLastUpdated('9903310000Z')
if mibBuilder.loadTexts: salixAnnouncementMIB.setOrganization('SALIX Technologies')
if mibBuilder.loadTexts: salixAnnouncementMIB.setContactInfo('904 Wind River Lane Suite 101 Gaithersburg, MD 20878 (301)-417-0017')
if mibBuilder.loadTexts: salixAnnouncementMIB.setDescription('The MIB describing objects relating to Announcements, Tones, and Continuity Tests for SALIX products')
salixAnnouncementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1))
salixAnnouncementMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 2))
salixAnnouncementMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3))
salixAnnouncementMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0))
salixAnnouncementTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1), )
if mibBuilder.loadTexts: salixAnnouncementTable.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementTable.setDescription('The announcement download table. This table provides a mechanism for downloading announcements to the system. Announcements that are successfully downloaded are installed on the system and occupy an entry in the salixAnnouncementTable. An entry in the salixAnnouncementTable exists for each bin on the system.')
salixAnnouncementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1), ).setIndexNames((0, "SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"))
if mibBuilder.loadTexts: salixAnnouncementEntry.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementEntry.setDescription('An entry in the salixAnnouncementTable that identifies the parameters necessary to download announcements to the system.')
salixAnnouncementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementIndex.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementIndex.setDescription('The unique index (bin) that the announcement is stored in.')
salixAnnouncementIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementIpAddress.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementIpAddress.setDescription('The Ip Address where the salixAnnouncementFilename object resides.')
salixAnnouncementFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementFilename.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementFilename.setDescription('The fully qualified filename found at the specified Ip Address (salixAnnouncementIpAddress) that is to be downloaded to the entry in the Table.')
salixAnnouncementUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementUsername.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementUsername.setDescription('The username to be used when getting a file from the computer at the IP address indicated by the salixAnnouncementIpAddress attribute. For security reasons, reading this field will return an empty string.')
salixAnnouncementPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementPassword.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementPassword.setDescription('The password to be used when getting a file from the computer at the IP address indicated by the salixAnnouncementIpAddress attribute. For security reasons, reading this field will return an empty string.')
salixAnnouncementRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("start", 1), ("update", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementRequest.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementRequest.setDescription('The announcement request for this row. Writing values to this object has the following side effects (depending on the value written: none(0) - no effect. Default value for this object. start(1) - start the FTP download and installation for the given announcement file. update(2) - Do not start the FTP download, just update system with the given version of the announcement that already exists.')
salixAnnouncementState = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("success", 3), ("aborted", 4), ("failed", 5), ("locked", 6), ("installInProgress", 7))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementState.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementState.setDescription('The state of the download software request. none(1) - download not started or not supported inProgress(2) - download in progress success(3) - download to the announcement table was successful. aborted(4) - download aborted failed(5) - download to at least one plug-in unit failed locked(6) - the filename in the installed software entry is locked by the management processor software. installInProgress(7) - the bin is currently being installed to modules in the system and is not available for download')
salixAnnouncementDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixAnnouncementDescription.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementDescription.setDescription('A Description for the announcement. Should be something that uniqely describes this announcement on the system, so that the operator can determine the difference between all the installed announcements on the system')
salixAnnouncementInstall = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementInstall.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementInstall.setDescription('The time the announcement was installed on the system. This time is acutally the time that the download completes.')
salixAnnouncementFull = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementFull.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementFull.setDescription('This value indicates whether the announcement bin is full or not. True: an announcement file is present in this bin False: no announcement file is present in this bin ')
salixAnnouncementStatusMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementStatusMessage.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementStatusMessage.setDescription("Status message that describes the current state of the download as indicated by the 'salixAnnouncementState' attribute.")
salixAnnouncementMappingTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2), )
if mibBuilder.loadTexts: salixAnnouncementMappingTable.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementMappingTable.setDescription('The announcement mapping table is used to map salixAnnouncementIndex [bins] to the entPhysicalIndex that the announcement is installed on. When used in conjunction with the salixAnnouncementTable, it can be seen which boards in the system contain which announcements. An entry in this table exists for each announcement on each board that the announcement is installed on.')
salixAnnouncementMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"))
if mibBuilder.loadTexts: salixAnnouncementMappingEntry.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementMappingEntry.setDescription('An entry in the salixAnnouncementMappingEntry that maps an salixAnnouncementIndex to an entPhysicalIndex.')
salixAnnouncementMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("downloadInProgress", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixAnnouncementMappingStatus.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementMappingStatus.setDescription('Describes the current state of the announcement on the board in the system. ready (1) - The announcement is installed on the board and ready for use downloadInProgress(2) - The announcement is being installed on the board and is not ready for use')
salixAnnouncementInstallFailure = NotificationType((1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalIndex"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"), ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
if mibBuilder.loadTexts: salixAnnouncementInstallFailure.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementInstallFailure.setDescription("Indicates thats the installation of the announcement has failed. This notification is generated when the salixAnnouncementState for this download transitions from inProgress to failed. The default alarm severity for this alarm is 'major'.")
salixAnnouncementInstallSuccess = NotificationType((1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0, 2)).setObjects(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"), ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
if mibBuilder.loadTexts: salixAnnouncementInstallSuccess.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementInstallSuccess.setDescription("Indicates thats the installation of the announcement to all the Transcoders have succeeded. This notification is generated when the salixAnnouncementState for the download transitions from inProgress to success. The default alarm severity for this alarm is 'minor'.")
salixAnnouncementGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1))
salixAnnouncementCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 2))
salixAnnouncementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1, 1)).setObjects(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIpAddress"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementFilename"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementUsername"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementPassword"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementRequest"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementState"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementDescription"), ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementInstall"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixAnnouncementGroup = salixAnnouncementGroup.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementGroup.setDescription('Salix Announcement Objects Group')
salixAnnouncementMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1, 2)).setObjects(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementMappingStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixAnnouncementMappingGroup = salixAnnouncementMappingGroup.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementMappingGroup.setDescription('Salix Announcement Mapping Objects Group')
salixAnnouncementCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 2, 1)).setObjects(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixAnnouncementCompliance = salixAnnouncementCompliance.setStatus('current')
if mibBuilder.loadTexts: salixAnnouncementCompliance.setDescription('The basic implementation requirements for the SALIX-ANNOUNCEMENT-MIB.')
mibBuilder.exportSymbols("SALIX-ANNOUNCEMENT-MIB", salixAnnouncementInstall=salixAnnouncementInstall, salixAnnouncementInstallSuccess=salixAnnouncementInstallSuccess, salixAnnouncementFilename=salixAnnouncementFilename, salixAnnouncementMappingGroup=salixAnnouncementMappingGroup, salixAnnouncementMIB=salixAnnouncementMIB, salixAnnouncementMIBTraps=salixAnnouncementMIBTraps, salixAnnouncementTable=salixAnnouncementTable, salixAnnouncementGroups=salixAnnouncementGroups, salixAnnouncementGroup=salixAnnouncementGroup, salixAnnouncementCompliance=salixAnnouncementCompliance, salixAnnouncementUsername=salixAnnouncementUsername, salixAnnouncementMappingTable=salixAnnouncementMappingTable, salixAnnouncementDescription=salixAnnouncementDescription, salixAnnouncementMIBObjects=salixAnnouncementMIBObjects, salixAnnouncementFull=salixAnnouncementFull, salixAnnouncementIpAddress=salixAnnouncementIpAddress, salixAnnouncementMIBCompliance=salixAnnouncementMIBCompliance, salixAnnouncementMappingStatus=salixAnnouncementMappingStatus, salixAnnouncementStatusMessage=salixAnnouncementStatusMessage, salixAnnouncementIndex=salixAnnouncementIndex, salixAnnouncementState=salixAnnouncementState, salixAnnouncementCompliances=salixAnnouncementCompliances, salixAnnouncementPassword=salixAnnouncementPassword, salixAnnouncementRequest=salixAnnouncementRequest, PYSNMP_MODULE_ID=salixAnnouncementMIB, salixAnnouncementInstallFailure=salixAnnouncementInstallFailure, salixAnnouncementMIBTrapPrefix=salixAnnouncementMIBTrapPrefix, salixAnnouncementMappingEntry=salixAnnouncementMappingEntry, salixAnnouncementEntry=salixAnnouncementEntry)
