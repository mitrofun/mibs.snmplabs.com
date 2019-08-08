#
# PySNMP MIB module TMS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TMS-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
PortList, dot1qStaticMulticastEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qStaticMulticastEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Counter64, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Counter64", "Integer32", "Gauge32")
RowStatus, DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
tmsGeneric, = mibBuilder.importSymbols("WRS-MASTER-MIB", "tmsGeneric")
tmsCommonMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 731, 2, 2, 1))
tmsCommonMib.setRevisions(('2000-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tmsCommonMib.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: tmsCommonMib.setLastUpdated('200011020000Z')
if mibBuilder.loadTexts: tmsCommonMib.setOrganization('Wind River Systems, Inc.')
if mibBuilder.loadTexts: tmsCommonMib.setContactInfo('Wind River Systems, Inc. E-mail: support@windriver.com')
if mibBuilder.loadTexts: tmsCommonMib.setDescription('TMS Common Enterprise MIB definition.')
tmsCommonNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 0))
tmsCommonVer = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1))
tmsCommonIP = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2))
tmsCommonLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5))
tmsCommonMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6))
tmsCommonCommToView = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7))
tmsCommonIgmpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8))
tmsCommonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9))
tmsCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1))
tmsCommonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 2))
tmsCommonVerMIBMajor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerMIBMajor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerMIBMajor.setDescription("Get this MIB Major version number. This number should match the Major version given in the documentation header at the beginning text of this MIB. Note that the '.c' file corresponding to this MIB has to be manually edited to change the version number if this file is modified and the version number is therefore changed.")
tmsCommonVerMIBMinor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerMIBMinor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerMIBMinor.setDescription("Get this MIB Minor version number. This number should match the Minor version given in the documentation header at the beginning text of this MIB. Note that the '.c' file corresponding to this MIB has to be manually edited to change the version number if this file is modified and the version number is therefore changed.")
tmsCommonVerBootSWMajor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerBootSWMajor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerBootSWMajor.setDescription('Get the Boot Software Major version number. This number references the VxWorks TMS Boot ROM module.')
tmsCommonVerBootSWMinor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerBootSWMinor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerBootSWMinor.setDescription('Get the Boot Software Minor version number. This number references the VxWorks TMS Boot ROM module.')
tmsCommonVerAppSWMajor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerAppSWMajor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerAppSWMajor.setDescription('Get the Application Software Major version number. This number references the core TMS modules as a whole.')
tmsCommonVerAppSWMinor = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonVerAppSWMinor.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerAppSWMinor.setDescription('Get the Application Software Minor version number. This number references the core TMS modules as a whole.')
tmsCommonIPMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIPMACAddr.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPMACAddr.setDescription("DURABLE: { '000000000000'H } The base (i.e., first) MAC address used by the TMS agent for its in-band ports.")
tmsCommonIPIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIPIpAddress.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPIpAddress.setDescription("DURABLE: { '00000000'H } The IP Address for sw0 (swEND 0); only applies after reset - see 'tmsCommonMiscReset'.")
tmsCommonIPGateAddress = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIPGateAddress.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPGateAddress.setDescription("DURABLE: { '00000000'H } The default Gateway Address (i.e., next hop router) for sw0 (swEND 0); only applies after reset - see 'tmsCommonMiscReset'.")
tmsCommonIPNetMask = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIPNetMask.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPNetMask.setDescription("DURABLE: { 'ffffff00'H } The IP NetMask for sw0 (swEND 0); only applies after reset - see 'tmsCommonMiscReset'.")
tmsCommonIPStatus = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notModified", 1), ("modified", 2), ("restore", 3), ("apply", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIPStatus.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPStatus.setDescription('This object is used to synchronize the modification of the IP parameters used by the protocol stack based on the tmsCommonIP MIB objects. This allows the user to change tmsCommonIPMACAddr, tmsCommonIPIpAddress, tmsCommonIPGateAddress, and tmsCommonIPNetMask, and then apply the changes to the unit using apply(4). If tmsCommonIPStatus returns notModified(1), no modifications were made to any tmsCommonIP MIB objects. If tmsCommonIPStatus returns modified(2), one or more objects were changed, but have not been applied. Both notModified(1) and modified(2) are read-only values; the agent returns a SNMP_BADVALUE for sets using these values. Both restore(3) and apply(4) are valid SET values. If one or more of the tmsCommonIP objects were modified, the user can restore the parameters to a mirror of the NVM values using restore(3).')
tmsCommonLoadTftpAddress = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonLoadTftpAddress.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadTftpAddress.setDescription('DURABLE: The IP Address for the TFTP server used for downloading and/or uploading files.')
tmsCommonLoadTftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonLoadTftpFileName.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadTftpFileName.setDescription('DURABLE: The TFTP file path and name.')
tmsCommonLoadType = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("application", 1), ("boot", 2), ("configuration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonLoadType.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadType.setDescription("DURABLE: { application } The type of file to download or upload upon an 'tmsCommonLoadExecute'. WARNING: The boot should only be downloaded when absolutely required (e.g., if power is removed during the boot Flash write operation, the agent cannot be recovered).")
tmsCommonLoadExecute = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("download", 2), ("upload", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonLoadExecute.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadExecute.setDescription("Execute file download or upload procedure. A SET of this object starts the load procedure. Note that the Application and Boot images can only be downloaded. The NVM Configuration file can be uploaded and downloaded. A GET of this object will return the status of the executed operation. Use 'tmsCommonLoadExecuteStatus' to determine the status of the executed load.")
tmsCommonLoadExecuteStatus = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notStarted", 1), ("inProgress", 2), ("success", 3), ("errorConnection", 4), ("errorFilename", 5), ("errorFault", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonLoadExecuteStatus.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadExecuteStatus.setDescription('Provides status on the execute file load progress.')
tmsCommonMiscSaveToNvm = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("save", 2), ("saveInProgress", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscSaveToNvm.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscSaveToNvm.setDescription("When set to 'save(2)', all nonvolatile configuration parameters are saved to NVM (Nonvolatile Memory). NVM save operations may be slow (e.g., erasing/writing Flash device). Consequently, all or many updates should be made before saving to NVM. Note that the SNMP set to 'save(2)' returns immediately to the caller. Gets on this object then return 'saveInProgress(3)' until the save operation completes, at which time 'noop(1)' is returned. Consequently, a get operation always returns 'noop(1)' or 'saveInProgress(3)' depending on the current state. The agent returns 'badValue' for SNMPv1 or 'inconsistentValue' for SNMPv2c/v3 for a set to 'Save(2)' while the current get state is 'saveInProgress(3)'. Attempts to set this object to 'saveInProgress(3)' returns 'badValue' for SNMPv1 or 'wrongValue' for SNMPv2c/v3.")
tmsCommonMiscSnmpSecurityOnOff = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscSnmpSecurityOnOff.setStatus('obsolete')
if mibBuilder.loadTexts: tmsCommonMiscSnmpSecurityOnOff.setDescription('Enable/Disable SNMPv1 Security. This object is now obsolete and is not implemented.')
tmsCommonMiscSpanOnOff = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscSpanOnOff.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscSpanOnOff.setDescription("DURABLE: { enable } Enable/Disable Spanning Tree for the bridge. When 'disable(2)', all ports of the device are placed in the forwarding mode, regardless of current Spanning Tree state. When 'enable(1)', the normal STP state transitions take place.")
tmsCommonMiscBOOTPOnOff = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscBOOTPOnOff.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscBOOTPOnOff.setDescription("DURABLE: { disable } Enable/Disable BOOTP operation for the TMS agent. When 'disable(2)', no BOOTPs are transmitted by the Application. When 'enable(1)', the Application sends BOOTP requests during system startup.")
tmsCommonMiscDHCPOnOff = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscDHCPOnOff.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscDHCPOnOff.setDescription("DURABLE: { disable } Enable/Disable DHCP operation for the TMS agent. When 'disable(2)', no DHCPs are transmitted by the Application. When enabled, the Application sends DHCP requests during system startup.")
tmsCommonMiscBaud = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("baud2400", 1), ("baud9600", 2), ("baud19200", 3), ("baud38400", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscBaud.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscBaud.setDescription('DURABLE: { baud38400 } The serial port baud rate. Attributes include 8 data bits, no parity and 1 stop bit (8N1) with hardware flow control. Valid values are 2400, 9600, 19200, and 38400 baud.')
tmsCommonMiscPassword = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscPassword.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscPassword.setDescription("DURABLE: { 'password' } The system password used for serial console, Telnet console and Web page login.")
tmsCommonMiscProductName = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscProductName.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscProductName.setDescription("DURABLE: { 'WindRiver TMS Agent' } The product name associated with this agent. This name is displayed on the console screens and Web pages.")
tmsCommonMiscReset = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("reset", 2), ("resetToDefaults", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscReset.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscReset.setDescription("Physically performs a hardware reset of the unit. Use with care. A 'reset(2)' resets the unit, a 'resetToDefaults(3)' resets the NVM configuration to factory defaults and then resets the unit, and 'noop(1)' does nothing. A value of 'noop(1)' is always returned for a GET operation.")
tmsCommonMiscTrapTest = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noop", 1), ("coldstart", 2), ("linkdown", 3), ("linkup", 4), ("authentication", 5), ("tmsTestTrap", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonMiscTrapTest.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscTrapTest.setDescription("This object sends a specific SNMP Trap, as selected by the type, to the SNMP manager(s) to verify proper operation of the Notify Subsystem. Note that the specific SNMP Message Processing Model (SNMP v1, v2c or v3) is specified using 'snmpTargetParamsMPModel' in the 'snmpTargetParamsTable' in RFC2573 (Target MIB). To distinguish the linkdown(3) and linkup(4) test traps from the actual link down and up traps, both trap types use '0' for the ifIndex value. Note that tmsTestTrap(6) generates a 'tmsCommonSnmpV2TestTrap'. A GET always returns the 'noop(1)' value.")
tmsCommonCommunityToViewTable = MibTable((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1), )
if mibBuilder.loadTexts: tmsCommonCommunityToViewTable.setStatus('current')
if mibBuilder.loadTexts: tmsCommonCommunityToViewTable.setDescription('A table of SNMPv1/v2c community string to view name mappings.')
tmsCommonCommunityToViewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1), ).setIndexNames((0, "TMS-COMMON-MIB", "tmsCommonComm2ViewIndex"))
if mibBuilder.loadTexts: tmsCommonCommunityToViewEntry.setStatus('current')
if mibBuilder.loadTexts: tmsCommonCommunityToViewEntry.setDescription('A list of community-to-view parameters.')
tmsCommonComm2ViewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: tmsCommonComm2ViewIndex.setStatus('current')
if mibBuilder.loadTexts: tmsCommonComm2ViewIndex.setDescription("A simple index into 'tmsCommonCommunityToViewTable'.")
tmsCommonComm2ViewCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmsCommonComm2ViewCommName.setStatus('current')
if mibBuilder.loadTexts: tmsCommonComm2ViewCommName.setDescription("DURABLE: { 'public','':all } The SNMPv1/v2c community name string. Duplicate community names are not allowed in this table. Note that a null string is not a valid community name (i.e., a null string forces 'tmsCommonComm2ViewRowStatus' to 'notReady(3)').")
tmsCommonComm2ViewViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmsCommonComm2ViewViewName.setStatus('current')
if mibBuilder.loadTexts: tmsCommonComm2ViewViewName.setDescription("DURABLE: { 'internet':all } At runtime (i.e., not when this object is SET), this view name is compared to the 'vacmViewTreeFamilyViewName' in the 'vacmViewTreeFamilyTable' (see RFC2575). If a match is found and the varbind(s) specify valid object type and instance, the 'tmsCommonComm2ViewPermission' privilege is permitted. Note that a null string is not a valid view name value. Also note that the value of this object does not have to match an existing entry in the 'vacmViewTreeFamilyTable' (if no match, no access is allowed). Note that the factory default value for this object is 'internet', which allows access to the subtree under '1.3.6.1'.")
tmsCommonComm2ViewPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmsCommonComm2ViewPermission.setStatus('current')
if mibBuilder.loadTexts: tmsCommonComm2ViewPermission.setDescription("DURABLE: { readWrite:all } This object specifies the type of access allowed. 'readOnly(1)' allows GET operations (i.e., GET, GET-NEXT, GET-BULK) and 'readWrite(2)' allows both GET and SET operations.")
tmsCommonComm2ViewRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 7, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmsCommonComm2ViewRowStatus.setStatus('current')
if mibBuilder.loadTexts: tmsCommonComm2ViewRowStatus.setDescription("DURABLE: This object indicates the status of this entry. A row in this table can be created using the 'createAndGo(4)' (i.e., all parameters must be valid - supplied in a single SNMP PDU or have default values) or the 'createAndWait(5)' action states. Until all parameters are valid for a conceptual row, this object is 'notReady(3)'. All parameters must be valid before this object can be set to 'active(1)'. Any object in a conceptual row can be modified independent of the value of this object (e.g., can be changed while 'active(1)').")
tmsCommonIgmpSnoopEnabled = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEnabled.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEnabled.setDescription('DURABLE: { false ) Setting this object to true(1) enables IGMP Snooping. Setting it to false(2) disables IGMP Snooping. Note that IGMP Snooping can function with or without GVRP and GMRP enabled.')
tmsCommonIgmpSnoopAlerts = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIgmpSnoopAlerts.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopAlerts.setDescription('DURABLE: { false ) Setting this object to true(1) enables the IP Router Alert Option (as defined in RFC2113) for transmitted IGMP packets. Setting it to false(2) disables this option.')
tmsCommonIgmpSnoopAging = MibScalar((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmsCommonIgmpSnoopAging.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopAging.setDescription('DURABLE: { 300 ) The timeout period in seconds for aging out Multicast Groups dynamically learned with IGMP Snooping. Note that aging operates on a per interface per VLAN per multicast group basis.')
tmsCommonIgmpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4), )
if mibBuilder.loadTexts: tmsCommonIgmpSnoopTable.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopTable.setDescription("This table, which provides IGMP Snooping information, augments the 'dot1qStaticMulticastTable' in the Q-MIB (RFC2674).")
tmsCommonIgmpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4, 1), )
dot1qStaticMulticastEntry.registerAugmentions(("TMS-COMMON-MIB", "tmsCommonIgmpSnoopEntry"))
tmsCommonIgmpSnoopEntry.setIndexNames(*dot1qStaticMulticastEntry.getIndexNames())
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEntry.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEntry.setDescription('Displays by VLAN, Multicast Group, and Multicast receive port the set of ports enabled to forward Multicast Group traffic as determined by the IGMP Snooping task.')
tmsCommonIgmpSnoopEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 8, 4, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEgressPorts.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopEgressPorts.setDescription("This read-only object displays the set of ports enabled to forward specific Multicast Group traffic as determined by the IGMP Snooping task. It should be noted that the IGMP Snooping task generates a pseudo- static (i.e., not saved in NVM) port list similar to the RFC2674 Q-MIB 'dot1qStaticMulticastStaticEgressPorts' object. Consequently, a port will not be a member of 'tmsCommonIgmpSnoopEgressPorts' if it is a member of 'dot1qStaticMulticastForbiddenEgressPorts'.")
tmsCommonVerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 1)).setObjects(("TMS-COMMON-MIB", "tmsCommonVerMIBMajor"), ("TMS-COMMON-MIB", "tmsCommonVerMIBMinor"), ("TMS-COMMON-MIB", "tmsCommonVerBootSWMajor"), ("TMS-COMMON-MIB", "tmsCommonVerBootSWMinor"), ("TMS-COMMON-MIB", "tmsCommonVerAppSWMajor"), ("TMS-COMMON-MIB", "tmsCommonVerAppSWMinor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonVerGroup = tmsCommonVerGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonVerGroup.setDescription('This group retrieves system component versions.')
tmsCommonIPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 2)).setObjects(("TMS-COMMON-MIB", "tmsCommonIPMACAddr"), ("TMS-COMMON-MIB", "tmsCommonIPIpAddress"), ("TMS-COMMON-MIB", "tmsCommonIPGateAddress"), ("TMS-COMMON-MIB", "tmsCommonIPNetMask"), ("TMS-COMMON-MIB", "tmsCommonIPStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonIPGroup = tmsCommonIPGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIPGroup.setDescription('This group configures and retrieves IP related objects.')
tmsCommonLoadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 3)).setObjects(("TMS-COMMON-MIB", "tmsCommonLoadTftpAddress"), ("TMS-COMMON-MIB", "tmsCommonLoadTftpFileName"), ("TMS-COMMON-MIB", "tmsCommonLoadType"), ("TMS-COMMON-MIB", "tmsCommonLoadExecute"), ("TMS-COMMON-MIB", "tmsCommonLoadExecuteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonLoadGroup = tmsCommonLoadGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonLoadGroup.setDescription('This group configures and retrieves TFTP download and upload objects.')
tmsCommonMiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 4)).setObjects(("TMS-COMMON-MIB", "tmsCommonMiscSaveToNvm"), ("TMS-COMMON-MIB", "tmsCommonMiscSpanOnOff"), ("TMS-COMMON-MIB", "tmsCommonMiscBOOTPOnOff"), ("TMS-COMMON-MIB", "tmsCommonMiscDHCPOnOff"), ("TMS-COMMON-MIB", "tmsCommonMiscBaud"), ("TMS-COMMON-MIB", "tmsCommonMiscPassword"), ("TMS-COMMON-MIB", "tmsCommonMiscProductName"), ("TMS-COMMON-MIB", "tmsCommonMiscReset"), ("TMS-COMMON-MIB", "tmsCommonMiscTrapTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonMiscGroup = tmsCommonMiscGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonMiscGroup.setDescription('This group configures and retrieves misc. switch objects.')
tmsCommonCommToViewGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 5)).setObjects(("TMS-COMMON-MIB", "tmsCommonComm2ViewCommName"), ("TMS-COMMON-MIB", "tmsCommonComm2ViewViewName"), ("TMS-COMMON-MIB", "tmsCommonComm2ViewPermission"), ("TMS-COMMON-MIB", "tmsCommonComm2ViewRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonCommToViewGroup = tmsCommonCommToViewGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonCommToViewGroup.setDescription('This group configures and retrieves community-to-view SNMP information.')
tmsCommonIgmpSnoopGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 1, 6)).setObjects(("TMS-COMMON-MIB", "tmsCommonIgmpSnoopEnabled"), ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopAlerts"), ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopAging"), ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopEgressPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonIgmpSnoopGroup = tmsCommonIgmpSnoopGroup.setStatus('current')
if mibBuilder.loadTexts: tmsCommonIgmpSnoopGroup.setDescription('This group configures and retrieves IGMP Snooping information.')
tmsCommonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 9, 2, 1)).setObjects(("TMS-COMMON-MIB", "tmsCommonVerGroup"), ("TMS-COMMON-MIB", "tmsCommonIPGroup"), ("TMS-COMMON-MIB", "tmsCommonLoadGroup"), ("TMS-COMMON-MIB", "tmsCommonMiscGroup"), ("TMS-COMMON-MIB", "tmsCommonCommToViewGroup"), ("TMS-COMMON-MIB", "tmsCommonIgmpSnoopGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmsCommonCompliance = tmsCommonCompliance.setStatus('current')
if mibBuilder.loadTexts: tmsCommonCompliance.setDescription('The compliance statement.')
tmsCommonSnmpV2TestTrap = NotificationType((1, 3, 6, 1, 4, 1, 731, 2, 2, 1, 0, 1)).setObjects(("TMS-COMMON-MIB", "tmsCommonMiscProductName"))
if mibBuilder.loadTexts: tmsCommonSnmpV2TestTrap.setStatus('current')
if mibBuilder.loadTexts: tmsCommonSnmpV2TestTrap.setDescription("This trap is used for the sample SNMP enterprise trap in the 'tmsCommonMiscTrapTest' object. Note that it includes the 'tmsCommonMiscProductName' object as a varbind.")
mibBuilder.exportSymbols("TMS-COMMON-MIB", tmsCommonIgmpSnoopEgressPorts=tmsCommonIgmpSnoopEgressPorts, tmsCommonComm2ViewViewName=tmsCommonComm2ViewViewName, tmsCommonLoad=tmsCommonLoad, tmsCommonIPNetMask=tmsCommonIPNetMask, tmsCommonCommunityToViewTable=tmsCommonCommunityToViewTable, tmsCommonIPGateAddress=tmsCommonIPGateAddress, tmsCommonMiscBOOTPOnOff=tmsCommonMiscBOOTPOnOff, tmsCommonVer=tmsCommonVer, tmsCommonVerBootSWMinor=tmsCommonVerBootSWMinor, tmsCommonComm2ViewCommName=tmsCommonComm2ViewCommName, tmsCommonComm2ViewRowStatus=tmsCommonComm2ViewRowStatus, tmsCommonCommToViewGroup=tmsCommonCommToViewGroup, tmsCommonCommunityToViewEntry=tmsCommonCommunityToViewEntry, tmsCommonVerMIBMinor=tmsCommonVerMIBMinor, tmsCommonLoadType=tmsCommonLoadType, tmsCommonMiscBaud=tmsCommonMiscBaud, tmsCommonMib=tmsCommonMib, tmsCommonMiscSnmpSecurityOnOff=tmsCommonMiscSnmpSecurityOnOff, tmsCommonMiscReset=tmsCommonMiscReset, tmsCommonNotify=tmsCommonNotify, tmsCommonMiscDHCPOnOff=tmsCommonMiscDHCPOnOff, tmsCommonIgmpSnoopEnabled=tmsCommonIgmpSnoopEnabled, PYSNMP_MODULE_ID=tmsCommonMib, tmsCommonIP=tmsCommonIP, tmsCommonIPMACAddr=tmsCommonIPMACAddr, tmsCommonMiscProductName=tmsCommonMiscProductName, tmsCommonVerAppSWMinor=tmsCommonVerAppSWMinor, tmsCommonVerGroup=tmsCommonVerGroup, tmsCommonIPIpAddress=tmsCommonIPIpAddress, tmsCommonGroups=tmsCommonGroups, tmsCommonLoadTftpAddress=tmsCommonLoadTftpAddress, tmsCommonComm2ViewIndex=tmsCommonComm2ViewIndex, tmsCommonCompliances=tmsCommonCompliances, tmsCommonMisc=tmsCommonMisc, tmsCommonMiscTrapTest=tmsCommonMiscTrapTest, tmsCommonIgmpSnoopGroup=tmsCommonIgmpSnoopGroup, tmsCommonLoadExecute=tmsCommonLoadExecute, tmsCommonVerAppSWMajor=tmsCommonVerAppSWMajor, tmsCommonIgmpSnoopEntry=tmsCommonIgmpSnoopEntry, tmsCommonIgmpSnoopTable=tmsCommonIgmpSnoopTable, tmsCommonMiscPassword=tmsCommonMiscPassword, tmsCommonIgmpSnoop=tmsCommonIgmpSnoop, tmsCommonCompliance=tmsCommonCompliance, tmsCommonConformance=tmsCommonConformance, tmsCommonLoadExecuteStatus=tmsCommonLoadExecuteStatus, tmsCommonIPGroup=tmsCommonIPGroup, tmsCommonMiscSaveToNvm=tmsCommonMiscSaveToNvm, tmsCommonComm2ViewPermission=tmsCommonComm2ViewPermission, tmsCommonLoadTftpFileName=tmsCommonLoadTftpFileName, tmsCommonMiscSpanOnOff=tmsCommonMiscSpanOnOff, tmsCommonMiscGroup=tmsCommonMiscGroup, tmsCommonVerMIBMajor=tmsCommonVerMIBMajor, tmsCommonSnmpV2TestTrap=tmsCommonSnmpV2TestTrap, tmsCommonIgmpSnoopAlerts=tmsCommonIgmpSnoopAlerts, tmsCommonIgmpSnoopAging=tmsCommonIgmpSnoopAging, tmsCommonLoadGroup=tmsCommonLoadGroup, tmsCommonCommToView=tmsCommonCommToView, tmsCommonIPStatus=tmsCommonIPStatus, tmsCommonVerBootSWMajor=tmsCommonVerBootSWMajor)