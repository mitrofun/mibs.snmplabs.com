#
# PySNMP MIB module FR-ATM-PVC-SERVICE-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FR-ATM-PVC-SERVICE-IWF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
atmVclEntry, = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ModuleIdentity, IpAddress, TimeTicks, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, mib_2, Integer32, Counter32, MibIdentifier, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "mib-2", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity")
RowStatus, DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TimeStamp")
frAtmIwfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 86))
frAtmIwfMIB.setRevisions(('2000-09-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: frAtmIwfMIB.setRevisionsDescriptions(('Published as RFC 2955',))
if mibBuilder.loadTexts: frAtmIwfMIB.setLastUpdated('200009280000Z')
if mibBuilder.loadTexts: frAtmIwfMIB.setOrganization('IETF Frame Relay Service MIB Working Group')
if mibBuilder.loadTexts: frAtmIwfMIB.setContactInfo('WG Charter: http://www.ietf.org/html.charters/frnetmib-charter WG-email: frnetmib@sunroof.eng.sun.com Subscribe: frnetmib-request@sunroof.eng.sun.com Email Archive: ftp://ftp.ietf.org/ietf-mail-archive/frnetmib Chair: Andy Malis Vivace Networks, Inc. Email: Andy.Malis@vivacenetworks.com WG editor: Kenneth Rehbehn Megisto Systems, Inc. Email: krehbehn@megisto.com Co-author: Orly Nicklass RAD Data Communications Ltd. EMail: orly_n@rad.co.il Co-author: George Mouradian AT&T Labs EMail: gvm@att.com')
if mibBuilder.loadTexts: frAtmIwfMIB.setDescription('The MIB module for monitoring and controlling the Frame Relay/ATM PVC Service Interworking Function.')
frAtmIwfMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 1))
frAtmIwfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2))
frAtmIwfTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2, 0))
frAtmIwfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3))
frAtmIwfGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 1))
frAtmIwfCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 2))
frAtmIwfConnIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 86, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnIndexNext.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnIndexNext.setDescription('This object contains an appropriate value to be used for frAtmIwfConnIndex when creating entries in the frAtmIwfConnectionTable. The value 0 indicates that no unassigned entries are available. To obtain the frAtmIwfConnIndexNext value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object. After each retrieval, the agent should modify the value to the next unassigned index.')
frAtmIwfConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 2), )
if mibBuilder.loadTexts: frAtmIwfConnectionTable.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionTable.setDescription('A table in which each row represents a Frame Relay/ATM interworking connection.')
frAtmIwfConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 2, 1), ).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndex"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtmPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVpi"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVci"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFrPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDlci"))
if mibBuilder.loadTexts: frAtmIwfConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionEntry.setDescription("The FrAtmIwfConnectionEntry provides an entry for an interworking connection between a frame relay PVC and one or more ATM PVCs, or an ATM PVC and one or more frame relay PVCs. A single frame relay PVC connected to a single ATM PVC is referred to as a `point-to-point' connection and is represented by a single row in the FR/ATM IWF Connection Table. The case of a single frame relay PVC connected to multiple ATM PVCs (or single ATM PVC connected to multiple frame relay PVCs) is referred to as a `point-to-multipoint' connection and is represented by multiple rows in the FR/ATM IWF Connection Table. The object frAtmIwfConnIndex uniquely identifies each point-to-point or point-to-multipoint connection. The manager obtains the frAtmIwfConnIndex value by reading the frAtmIwfConnIndexNext object. After a frAtmIwfConnIndex is assigned for the connection, the manager creates one or more rows in the Cross Connect Table; one for each cross- connection between the frame relay PVC and an ATM PVC. In the case of `point-to-multipoint' connections, all rows are indexed by the same frAtmIwfConnIndex value and MUST refer to the same frame relay PVC or ATM PVC respectively. An entry can be created only when at least one pair of frame relay and ATM PVCs exist. A row can be established by one-step set-request with all required parameter values and frAtmIwfConnRowStatus set to createAndGo(4). The Agent should perform all error checking as needed. A pair of cross-connected PVCs, as identified by a particular value of the indexes, is released by setting frAtmIwfConnRowStatus to destroy(6). The Agent may release all associated resources. The manager may remove the related PVCs thereafter. Indexes are persistent across reboots of the system.")
frAtmIwfConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: frAtmIwfConnIndex.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnIndex.setDescription('A unique value for each point-to-point or point- to-multipoint connection. The manager obtains the frAtmIwfConnIndex value by reading the frAtmIwfConnIndexNext object. A point-to- multipoint connection will be represented in the frAtmIwfConnectionTable with multiple entries that share the same frAtmIwfConnIndex value.')
frAtmIwfConnAtmPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: frAtmIwfConnAtmPort.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnAtmPort.setDescription('The index in the ifTable that identifies the ATM port for this interworking connection.')
frAtmIwfConnVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 3), AtmVpIdentifier())
if mibBuilder.loadTexts: frAtmIwfConnVpi.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnVpi.setDescription('The VPI of the ATM PVC end point for this interworking connection.')
frAtmIwfConnVci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 4), AtmVcIdentifier())
if mibBuilder.loadTexts: frAtmIwfConnVci.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnVci.setDescription('The VCI of the ATM PVC end point for this interworking connection.')
frAtmIwfConnFrPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 5), InterfaceIndex())
if mibBuilder.loadTexts: frAtmIwfConnFrPort.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFrPort.setDescription('The index in the ifTable that identifies the frame relay port for this interworking connection.')
frAtmIwfConnDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 4194303)))
if mibBuilder.loadTexts: frAtmIwfConnDlci.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnDlci.setDescription('The DLCI that identifies the frame relay PVC end point for this interworking connection.')
frAtmIwfConnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnRowStatus.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnRowStatus.setDescription("The table row may be created with 'createAndWait(5)' or 'createAndGo(4)'. To activate a connection entry, a valid connection descriptor MUST be established in the frAtmIwfConnectionDescriptor object. This object is set to 'destroy(6)' to delete the table row. Before the table row is destroyed, the OperStatus/AdminStatus of the corresponding endpoints MUST be 'down(2)'. The deactivation of the ATM endpoint MAY occur as a side-effect of deleting the FR/ATM IWF cross-connection table row. Otherwise, 'destroy(6)' operation MUST fail (error code 'inconsistentValue').")
frAtmIwfConnAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnAdminStatus.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnAdminStatus.setDescription("The desired operational state for this FR/ATM interworked connection. up(1) = Activate the connection. Before the activation can be completed, the OperStatus/AdminStatus of the corresponding endpoints MUST be 'up(1)'. The activation of the corresponding endpoints MAY occur as a side-effect of activating the FR/ATM IWF cross-connection. down(2) = Deactivate the connection. Before the deactivation can be completed, the atmVclAdminStatus of the corresponding ATM endpoint MUST be 'down(2)'. The deactivation of the ATM endpoint MAY occur as a side-effect of deactivating the FR/ATM IWF cross-connection.")
frAtmIwfConnAtm2FrOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrOperStatus.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrOperStatus.setDescription('The current operational state of this interworking connection in the ATM to frame relay direction.')
frAtmIwfConnAtm2FrLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrLastChange.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrLastChange.setDescription('The value of sysUpTime at the time this interworking connection entered its current operational state in the ATM to FR direction. If the current state was entered prior to the last re-initialization of the local network management subsystem, then this object contains a zero value.')
frAtmIwfConnFr2AtmOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmOperStatus.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmOperStatus.setDescription('The current operational state of this interworking connection in the frame relay to ATM direction.')
frAtmIwfConnFr2AtmLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmLastChange.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmLastChange.setDescription('The value of sysUpTime at the time this interworking connection entered its current operational state in the FR to ATM direction. If the current state was entered prior to the last re-initialization of the local network management subsystem, then this object contains a zero value.')
frAtmIwfConnectionDescriptor = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptor.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptor.setDescription("The value represents a pointer to the relevant descriptor in the IWF descriptor table. An attempt to set this value to an inactive or non- existent row in the Connection Descriptor Table MUST fail (error code 'inconsistentValue').")
frAtmIwfConnFailedFrameTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 14), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFailedFrameTranslate.setReference('FRF.8 [17], Section 5.3.1')
if mibBuilder.loadTexts: frAtmIwfConnFailedFrameTranslate.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFailedFrameTranslate.setDescription('This object counts the number of frames discarded by the IWF because, while operating in Translation Mode, the IWF is unable to decode the incoming frame payload header according to the mapping rules. (i.e., payload header not recognized by the IWF). Frame relay frames are received in the frame relay to ATM direction of the PVC. When operating in Transparent Mode, the IWF MUST return noSuchInstance.')
frAtmIwfConnOverSizedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 15), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnOverSizedFrames.setReference('ATM MIB [21], atmVclTable FRF.8 [17], 5.3.1.4')
if mibBuilder.loadTexts: frAtmIwfConnOverSizedFrames.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnOverSizedFrames.setDescription('Count of frames discarded by the IWF because the frame is too large to be processed by the AAL5 segmentation procedure. Specifically, the frame does not conform to the size specified in the atmVccAal5CpcsTransmitSduSize object associated with the atmVclEntry at the ATM endpoint. Frame relay frames are received in the frame relay to ATM direction of the PVC.')
frAtmIwfConnFailedAal5PduTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 16), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFailedAal5PduTranslate.setReference('FRF.8 [17], Section 5.3.1')
if mibBuilder.loadTexts: frAtmIwfConnFailedAal5PduTranslate.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFailedAal5PduTranslate.setDescription('This attribute counts the number of AAL5 PDUs discarded by the IWF because, while operating in Translation Mode, the IWF is unable to decode the incoming AAL5 PDU payload header according to the mapping rules. (i.e., payload header not recognized by the IWF). AAL5 PDUs are received in the ATM to frame relay direction of the PVC. When operating in Transparent Mode, the IWF MUST return noSuchInstance.')
frAtmIwfConnOverSizedSDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 17), Counter32()).setUnits('SDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnOverSizedSDUs.setReference('FRS MIB [19], frLportTable FRF.8 [17], 5.3.1.4')
if mibBuilder.loadTexts: frAtmIwfConnOverSizedSDUs.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnOverSizedSDUs.setDescription('Count of AAL5 SDUs discarded by the IWF because the SDU is too large to be forwarded on the frame relay segment of the connection. Specifically, the frame does not conform to the size specified in the frLportFragSize object of the FRS MIB [19]. AAL5 PDUs are received in the ATM to frame relay direction of the PVC.')
frAtmIwfConnCrcErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 18), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnCrcErrors.setReference('ATM MIB [21], atmVclTable')
if mibBuilder.loadTexts: frAtmIwfConnCrcErrors.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnCrcErrors.setDescription('The number of AAL5 CPCS PDUs received with CRC-32 errors on this AAL5 VCC at the IWF. AAL5 PDUs are received in the ATM to frame relay direction of the PVC.')
frAtmIwfConnSarTimeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 19), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnSarTimeOuts.setReference('ATM MIB [21], atmVclTable')
if mibBuilder.loadTexts: frAtmIwfConnSarTimeOuts.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnSarTimeOuts.setDescription('The number of partially re-assembled AAL5 CPCS PDUs which were discarded on this AAL5 VCC at the IWF because they were not fully re-assembled within the required time period. If the re- assembly timer is not supported, then this object contains a zero value. AAL5 PDUs are received in the ATM to frame relay direction of the PVC.')
frAtmIwfConnectionDescriptorIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 86, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndexNext.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndexNext.setDescription('This object contains an appropriate value to be used for frAtmIwfConnectionDescriptorIndex when creating entries in the frAtmIwfConnectionDescriptorTable. The value 0 indicates that no unassigned entries are available. To obtain the frAtmIwfConnectionDescriptorIndexNext value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object. After each retrieval, the agent should modify the value to the next unassigned index.')
frAtmIwfConnectionDescriptorTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 4), )
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorTable.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorTable.setDescription('A table in which each row represents a descriptor for one type of Frame Relay/ATM interworking connection. A descriptor may be assigned to zero or more FR/ATM PVC service IWF connections.')
frAtmIwfConnectionDescriptorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 4, 1), ).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndex"))
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorEntry.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorEntry.setDescription('An entry for a descriptor in an interworking connection between a frame relay PVC and an ATM PVC.')
frAtmIwfConnectionDescriptorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndex.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndex.setDescription('A unique value to identify a descriptor in the table ')
frAtmIwfConnDescriptorRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnDescriptorRowStatus.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnDescriptorRowStatus.setDescription("The status of this table row. This object is used to create or delete an entry in the descriptor table. Creation of the row requires a row index (see frAtmIwfConnectionDescriptorIndexNext). If not explicitly set or in existence, all other columns of the row will be created and initialized to the default value. During creation, this object MAY be set to 'createAndGo(4)' or 'createAndWait(5)'. The object MUST contain the value 'active(1)' before any connection table entry references the row. To destroy a row in this table, this object is set to the 'destroy(6)' action. Row destruction MUST fail (error code 'inconsistentValue') if any connection references the row.")
frAtmIwfConnDeToClpMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3))).clone('mode1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnDeToClpMappingMode.setReference('FRF.8 [17], Section 4.2.1')
if mibBuilder.loadTexts: frAtmIwfConnDeToClpMappingMode.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnDeToClpMappingMode.setDescription('This object describes which mode of translation is in use for loss priority mapping in the frame relay to ATM direction. mode1(1) = the DE field in the Q.922 core frame shall be mapped to the ATM CLP field of every cell generated by the segmentation process of the AAL5 PDU containing the information of that frame. mode2Contst0(2) = the ATM CLP field of every cell generated by the segmentation process of the AAL5 PDU containing the information of that frame shall be set to constant 0. mode2Contst1(3) = the ATM CLP field of every cell generated by the segmentation process of the AAL5 PDU containing the information of that frame shall be set to constant 1.')
frAtmIwfConnClpToDeMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3))).clone('mode1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnClpToDeMappingMode.setReference('FRF.8 [17], Section 4.2.2')
if mibBuilder.loadTexts: frAtmIwfConnClpToDeMappingMode.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnClpToDeMappingMode.setDescription('This object describes which mode of translation is in use for loss priority mapping in the ATM to frame relay direction. mode1(1) = if one or more cells in a frame has its CLP field set, the DE field of the Q.922 core frame should be set. mode2Const0(2) = the DE field of the Q.922 core frame should be set to the constant 0. mode2Const1(3) = the DE field of the Q.922 core frame should be set to the constant 1.')
frAtmIwfConnCongestionMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("mode2", 2))).clone('mode1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnCongestionMappingMode.setReference('FRF.8 [17], Section 4.3.1.1')
if mibBuilder.loadTexts: frAtmIwfConnCongestionMappingMode.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnCongestionMappingMode.setDescription("This object describes which mode of translation is in use for forward congestion indication mapping in the frame relay to ATM direction. mode1(1) = The FECN field in the Q.922 core frame shall be mapped to the ATM EFCI field of every cell generated by the segmentation process of the AAL5 PDU containing the information of that frame. mode2(2) = The FECN field in the Q.922 core frame shall not be mapped to the ATM EFCI field of cells generated by the segmentation process of the AAL5 PDU containing the information of that frame. The EFCI field is always set to 'congestion not experienced'. In both of the modes above, if there is congestion in the forward direction in the ATM layer within the IWF, then the IWF can set the EFCI field to 'congestion experienced'.")
frAtmIwfConnEncapsulationMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transparentMode", 1), ("translationMode", 2), ("translationModeAll", 3))).clone('transparentMode')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappingMode.setReference('FRF.8 [17], Section 5.3')
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappingMode.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappingMode.setDescription('This object indicates whether the mapping of upper layer protocol encapsulation is enabled on this interworking connection. transparentMode(1) = Forward the encapsulations unaltered. translationMode(2) = Perform mapping between the two encapsulations due to the incompatibilities of the two methods. Mapping is provided for a subset of the potential encapsulations as itemized in frAtmIwfConnEncapsulationMapp ings. translationModeAll(3) = Perform mapping between the two encapsulations due to the incompatibilities of the two methods. All encapsulations are translated.')
frAtmIwfConnEncapsulationMappings = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 7), Bits().clone(namedValues=NamedValues(("none", 0), ("bridgedPdus", 1), ("bridged802dot6", 2), ("bPdus", 3), ("routedIp", 4), ("routedOsi", 5), ("otherRouted", 6), ("x25Iso8202", 7), ("q933q2931", 8))).clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappings.setReference('FRF.8 [17], Section 5.3.1')
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappings.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappings.setDescription('If upper layer protocol encapsulation mapping is enabled on this interworking connection, then this attribute enumerates which of the encapsulation mappings are supported. none(0) = Transparent mode operation bridgedPdus(1) = PID: 0x00-01,-07,-02 or -08 bridged802dot6(2) = PID: 0x00-0B bPdus(3) = PID: 0x00-0E or -0F routedIp(4) = NLPID: OxCC routedOsi(5) = NLPID: Ox81, 0x82 or 0x83 otherRouted(6) = Other routed protocols x25Iso8202(7) = X25 q933q2931(8) = Q.933 and Q.2931')
frAtmIwfConnFragAndReassEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnFragAndReassEnabled.setReference('FRF.8 [17], Section 5.3.1.4')
if mibBuilder.loadTexts: frAtmIwfConnFragAndReassEnabled.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnFragAndReassEnabled.setDescription('The attribute indicates whether fragmentation and reassembly is enabled for this connection.')
frAtmIwfConnArpTranslationEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnArpTranslationEnabled.setReference('FRF.8 [17], Section 5.4')
if mibBuilder.loadTexts: frAtmIwfConnArpTranslationEnabled.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnArpTranslationEnabled.setDescription('The attribute indicates whether ARP translation is enabled for this connection.')
frAtmIwfVclTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 5), )
if mibBuilder.loadTexts: frAtmIwfVclTable.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfVclTable.setDescription('The FR/ATM IWF VCL Table augments the ATM MIB VCL Endpoint table.')
frAtmIwfVclEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 5, 1), )
atmVclEntry.registerAugmentions(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclEntry"))
frAtmIwfVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
if mibBuilder.loadTexts: frAtmIwfVclEntry.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfVclEntry.setDescription('Entries in this table are created only by the agent. One entry exists for each ATM VCL managed by the agent.')
frAtmIwfVclCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfVclCrossConnectIdentifier.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfVclCrossConnectIdentifier.setDescription('This object contains the index value of the FR/ATM cross-connect table entry used to link the ATM VCL with a frame relay PVC. Each row of the atmVclTable that is not cross- connected with a frame relay PVC MUST return the value zero when this object is read. In the case of (frame relay) point to (ATM) multipoint, multiple ATM VCLs will have the same value of this object, and all their cross- connections are identified by entries that are indexed by the same value of frAtmIwfVclCrossConnectIdentifier in the frAtmIwfConnectionTable of this MIB module. The value of this object is initialized by the agent after the associated entries in the frAtmIwfConnectionTable have been created.')
frAtmIwfConnStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 86, 2, 0, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"))
if mibBuilder.loadTexts: frAtmIwfConnStatusChange.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnStatusChange.setDescription('An indication that the status of this interworking connection has changed.')
frAtmIwfEquipmentCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 86, 3, 2, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfBasicGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfAtmVclTableAugmentGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfEquipmentCompliance = frAtmIwfEquipmentCompliance.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfEquipmentCompliance.setDescription('The compliance statement for equipment that implements the FR/ATM Interworking MIB.')
frAtmIwfServiceCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 86, 3, 2, 2)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfBasicGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfAtmVclTableAugmentGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfServiceCompliance = frAtmIwfServiceCompliance.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfServiceCompliance.setDescription('The compliance statement for a CNM interface that implements the FR/ATM Interworking MIB.')
frAtmIwfBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndexNext"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptor"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedFrameTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedFrames"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedAal5PduTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedSDUs"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCrcErrors"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnSarTimeOuts"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfBasicGroup = frAtmIwfBasicGroup.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfBasicGroup.setDescription('The collection of basic objects for configuration and control of FR/ATM interworking connections.')
frAtmIwfConnectionDescriptorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 2)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndexNext"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDeToClpMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnClpToDeMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCongestionMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappings"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFragAndReassEnabled"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnArpTranslationEnabled"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDescriptorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfConnectionDescriptorGroup = frAtmIwfConnectionDescriptorGroup.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorGroup.setDescription('The collection of basic objects for specification of FR/ATM interworking connection descriptors.')
frAtmIwfAtmVclTableAugmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 3)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclCrossConnectIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfAtmVclTableAugmentGroup = frAtmIwfAtmVclTableAugmentGroup.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfAtmVclTableAugmentGroup.setDescription('The ATM MIB VCL Endpoint Table AUGMENT object contained in the FR/ATM PVC Service Interworking MIB.')
frAtmIwfNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 4)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frAtmIwfNotificationsGroup = frAtmIwfNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: frAtmIwfNotificationsGroup.setDescription('The notification for FR/ATM interworking status change.')
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfConnAdminStatus=frAtmIwfConnAdminStatus, frAtmIwfConnectionDescriptorIndexNext=frAtmIwfConnectionDescriptorIndexNext, frAtmIwfConnRowStatus=frAtmIwfConnRowStatus, frAtmIwfConnFailedFrameTranslate=frAtmIwfConnFailedFrameTranslate, frAtmIwfConnEncapsulationMappingMode=frAtmIwfConnEncapsulationMappingMode, frAtmIwfMIB=frAtmIwfMIB, frAtmIwfConnOverSizedFrames=frAtmIwfConnOverSizedFrames, frAtmIwfConformance=frAtmIwfConformance, frAtmIwfConnFr2AtmLastChange=frAtmIwfConnFr2AtmLastChange, frAtmIwfConnOverSizedSDUs=frAtmIwfConnOverSizedSDUs, frAtmIwfConnClpToDeMappingMode=frAtmIwfConnClpToDeMappingMode, frAtmIwfConnAtmPort=frAtmIwfConnAtmPort, frAtmIwfVclEntry=frAtmIwfVclEntry, frAtmIwfBasicGroup=frAtmIwfBasicGroup, frAtmIwfConnectionDescriptorGroup=frAtmIwfConnectionDescriptorGroup, frAtmIwfAtmVclTableAugmentGroup=frAtmIwfAtmVclTableAugmentGroup, PYSNMP_MODULE_ID=frAtmIwfMIB, frAtmIwfMIBObjects=frAtmIwfMIBObjects, frAtmIwfConnDlci=frAtmIwfConnDlci, frAtmIwfConnFailedAal5PduTranslate=frAtmIwfConnFailedAal5PduTranslate, frAtmIwfConnDescriptorRowStatus=frAtmIwfConnDescriptorRowStatus, frAtmIwfConnSarTimeOuts=frAtmIwfConnSarTimeOuts, frAtmIwfCompliances=frAtmIwfCompliances, frAtmIwfConnArpTranslationEnabled=frAtmIwfConnArpTranslationEnabled, frAtmIwfConnCrcErrors=frAtmIwfConnCrcErrors, frAtmIwfConnDeToClpMappingMode=frAtmIwfConnDeToClpMappingMode, frAtmIwfConnIndexNext=frAtmIwfConnIndexNext, frAtmIwfConnIndex=frAtmIwfConnIndex, frAtmIwfEquipmentCompliance=frAtmIwfEquipmentCompliance, frAtmIwfConnAtm2FrLastChange=frAtmIwfConnAtm2FrLastChange, frAtmIwfVclCrossConnectIdentifier=frAtmIwfVclCrossConnectIdentifier, frAtmIwfConnAtm2FrOperStatus=frAtmIwfConnAtm2FrOperStatus, frAtmIwfConnectionDescriptor=frAtmIwfConnectionDescriptor, frAtmIwfConnVci=frAtmIwfConnVci, frAtmIwfConnectionDescriptorTable=frAtmIwfConnectionDescriptorTable, frAtmIwfTrapsPrefix=frAtmIwfTrapsPrefix, frAtmIwfConnectionDescriptorIndex=frAtmIwfConnectionDescriptorIndex, frAtmIwfConnVpi=frAtmIwfConnVpi, frAtmIwfConnFrPort=frAtmIwfConnFrPort, frAtmIwfConnEncapsulationMappings=frAtmIwfConnEncapsulationMappings, frAtmIwfServiceCompliance=frAtmIwfServiceCompliance, frAtmIwfNotificationsGroup=frAtmIwfNotificationsGroup, frAtmIwfConnFragAndReassEnabled=frAtmIwfConnFragAndReassEnabled, frAtmIwfConnectionTable=frAtmIwfConnectionTable, frAtmIwfConnectionEntry=frAtmIwfConnectionEntry, frAtmIwfConnectionDescriptorEntry=frAtmIwfConnectionDescriptorEntry, frAtmIwfGroups=frAtmIwfGroups, frAtmIwfVclTable=frAtmIwfVclTable, frAtmIwfConnFr2AtmOperStatus=frAtmIwfConnFr2AtmOperStatus, frAtmIwfConnStatusChange=frAtmIwfConnStatusChange, frAtmIwfConnCongestionMappingMode=frAtmIwfConnCongestionMappingMode, frAtmIwfTraps=frAtmIwfTraps)
