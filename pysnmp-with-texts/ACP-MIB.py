#
# PySNMP MIB module ACP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
giproducts, = mibBuilder.importSymbols("BCS-IDENT-MIB", "giproducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter32, ModuleIdentity, NotificationType, Integer32, iso, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter32", "ModuleIdentity", "NotificationType", "Integer32", "iso", "Gauge32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acpStatus = ModuleIdentity((1, 3, 6, 1, 4, 1, 1166, 1, 11))
acpStatus.setRevisions(('2003-06-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acpStatus.setRevisionsDescriptions(('Rev 1.40 make SMIv2 compliant by adding MODULE-IDENTITY clause',))
if mibBuilder.loadTexts: acpStatus.setLastUpdated('200306100000Z')
if mibBuilder.loadTexts: acpStatus.setOrganization('Motorola')
if mibBuilder.loadTexts: acpStatus.setContactInfo('Charles Zimmerman Motorola Broadband Communications Sector 101 Tournament Drive Horsham, PA 19044 Tel: +1 215 323 1524 E-mail: czimmerman@gic.gi.com')
if mibBuilder.loadTexts: acpStatus.setDescription('The MIB module for the Access Control Processor (TSODA, MC1). Revision Number 1.40')
acpNumberofEncryptTypes = MibScalar((1, 3, 6, 1, 4, 1, 1166, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpNumberofEncryptTypes.setReference(' -- ')
if mibBuilder.loadTexts: acpNumberofEncryptTypes.setStatus('current')
if mibBuilder.loadTexts: acpNumberofEncryptTypes.setDescription('The total number of encrypt type ACPs in the system. ')
acpNumberofDecryptTypes = MibScalar((1, 3, 6, 1, 4, 1, 1166, 1, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpNumberofDecryptTypes.setReference(' -- ')
if mibBuilder.loadTexts: acpNumberofDecryptTypes.setStatus('current')
if mibBuilder.loadTexts: acpNumberofDecryptTypes.setDescription('The total number of decrypt type ACPs in the system. ')
acpStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3), )
if mibBuilder.loadTexts: acpStatusTable.setReference(' -- ')
if mibBuilder.loadTexts: acpStatusTable.setStatus('current')
if mibBuilder.loadTexts: acpStatusTable.setDescription('A table of ACP entries giving health, status and mode')
acpStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1), ).setIndexNames((0, "ACP-MIB", "acpEncryptType"), (0, "ACP-MIB", "acpUnitIndex"), (0, "ACP-MIB", "acpServiceIndex"))
if mibBuilder.loadTexts: acpStatusEntry.setStatus('current')
if mibBuilder.loadTexts: acpStatusEntry.setDescription('A row in the ACP Entry Table')
acpEncryptType = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("encryptAcp", 1), ("decryptAcp", 2))))
if mibBuilder.loadTexts: acpEncryptType.setReference(' -- ')
if mibBuilder.loadTexts: acpEncryptType.setStatus('current')
if mibBuilder.loadTexts: acpEncryptType.setDescription('The type of ACP in the system. It is either an encryptAcp or decryptAcp device. ')
acpUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: acpUnitIndex.setReference(' -- ')
if mibBuilder.loadTexts: acpUnitIndex.setStatus('current')
if mibBuilder.loadTexts: acpUnitIndex.setDescription('The ACP unit index for this encrypt/decrypt type. For each type of ACP, encryptAcp or decryptAcp, the physical unit number of the ACP in the containing product, starting at 1.')
acpServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: acpServiceIndex.setStatus('current')
if mibBuilder.loadTexts: acpServiceIndex.setDescription('For a specified ACP, identified by the both acpEncryptType and acpUnitIndex, this index specifies the sequential service capabilities of this ACP, found in the following objects: acpServNumber acpServAuthorization acpServAuthReaCode acpServEncryption The maximum limit on the value of this index is determined by the Max number of services supported by this ACP (for a TSODA, it is 2). For all other objects in the acpStatusTable, this index is not used. (it must be valid, but will not be used to access the object uniquely specified by acpEncryptType and acpUnitIndex) REFERENCE ')
acpScramblingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("des", 1), ("csa", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpScramblingMode.setReference(' -- ')
if mibBuilder.loadTexts: acpScramblingMode.setStatus('current')
if mibBuilder.loadTexts: acpScramblingMode.setDescription('The Scrambling Mode of the ACP 1 - North American DES 2 - DVB Common Scrambling Algorithm ')
acpUnitAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpUnitAddress.setReference(' -- ')
if mibBuilder.loadTexts: acpUnitAddress.setStatus('current')
if mibBuilder.loadTexts: acpUnitAddress.setDescription('The 40 bit ACP address in Human-readable format 3-5-5-3')
acpInputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("acpInterfaceSerial", 1), ("acpInterfaceParallel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpInputInterface.setReference(' -- ')
if mibBuilder.loadTexts: acpInputInterface.setStatus('current')
if mibBuilder.loadTexts: acpInputInterface.setDescription('The interface for MPEG input to this ACP.')
acpOutputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("acpInterfaceSerial", 1), ("acpInterfaceParallel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpOutputInterface.setReference(' -- ')
if mibBuilder.loadTexts: acpOutputInterface.setStatus('current')
if mibBuilder.loadTexts: acpOutputInterface.setDescription('The interface for MPEG output from this ACP.')
acpServNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpServNumber.setReference(' -- ')
if mibBuilder.loadTexts: acpServNumber.setStatus('current')
if mibBuilder.loadTexts: acpServNumber.setDescription('MPEG service number (0=unknown) for encrypted service N, where N is specified by acpServiceIndex.')
acpServAuthorization = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("unauthorized", 1), ("authorized", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpServAuthorization.setReference(' -- ')
if mibBuilder.loadTexts: acpServAuthorization.setStatus('current')
if mibBuilder.loadTexts: acpServAuthorization.setDescription('ACP authorization status for service specified by acpServiceIndex')
acpServAuthReaCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpServAuthReaCode.setReference(' -- ')
if mibBuilder.loadTexts: acpServAuthReaCode.setStatus('current')
if mibBuilder.loadTexts: acpServAuthReaCode.setDescription('ACP authorization reason code for service specified By acpServiceIndex.')
acpServEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(255, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 255), ("fixedwk", 1), ("fixedpk", 2), ("unencrypted", 3), ("fullencryption", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpServEncryption.setReference(' -- ')
if mibBuilder.loadTexts: acpServEncryption.setStatus('current')
if mibBuilder.loadTexts: acpServEncryption.setDescription('ACP encryption status for service specified by The index acpServiceIndex.')
acpCatSeqNums = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpCatSeqNums.setReference(' -- ')
if mibBuilder.loadTexts: acpCatSeqNums.setStatus('current')
if mibBuilder.loadTexts: acpCatSeqNums.setDescription('The current and next Category Sequence Numbers')
acpEmmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpEmmCount.setReference(' -- ')
if mibBuilder.loadTexts: acpEmmCount.setStatus('current')
if mibBuilder.loadTexts: acpEmmCount.setDescription('The number of Category Rekey messages sent to this ACP.')
acpProgramEpochNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpProgramEpochNumber.setReference(' -- ')
if mibBuilder.loadTexts: acpProgramEpochNumber.setStatus('current')
if mibBuilder.loadTexts: acpProgramEpochNumber.setDescription('The current program epoch number for the service on this side of the ACP.')
acpNextProgramEpochNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpNextProgramEpochNumber.setReference(' -- ')
if mibBuilder.loadTexts: acpNextProgramEpochNumber.setStatus('current')
if mibBuilder.loadTexts: acpNextProgramEpochNumber.setDescription('The next program epoch number for the service on this side of the ACP.')
acpNextServAuthorization = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("unauthorized", 1), ("authorized", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpNextServAuthorization.setReference(' -- ')
if mibBuilder.loadTexts: acpNextServAuthorization.setStatus('current')
if mibBuilder.loadTexts: acpNextServAuthorization.setDescription('ACP authorization status for the next Program Epoch for the service specified by acpServiceIndex')
acpNextServAuthReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpNextServAuthReasonCode.setReference(' -- ')
if mibBuilder.loadTexts: acpNextServAuthReasonCode.setStatus('current')
if mibBuilder.loadTexts: acpNextServAuthReasonCode.setDescription('ACP authorization reason code for the next Program Epoch for the service specified By acpServiceIndex.')
acpInputSourceIdA = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpInputSourceIdA.setReference(' -- ')
if mibBuilder.loadTexts: acpInputSourceIdA.setStatus('current')
if mibBuilder.loadTexts: acpInputSourceIdA.setDescription('The Input Source Id is used to identify the input source for this ACP in different products. One or both parts of the Id may be used in identifying where the input for the ACP comes from. When the Input Source Id A is set to 255 then the Id is invalid. If Id A is invalid the Id B is assumed invalid also. For example, the MPS uses the input source id to designate the location of the physical connector that is mapped to the ACP. In the case of the decrypt ACPs, InputSourceIdA is used to indicate the slot, and InputSourceIdB is used to indicate the port. Only decrypt ACPs have their source identified in this way. Encrypt ACPs do not have an identified source and their IdA is always set to Invalid (255). ')
acpInputSourceIdB = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpInputSourceIdB.setReference(' -- ')
if mibBuilder.loadTexts: acpInputSourceIdB.setStatus('current')
if mibBuilder.loadTexts: acpInputSourceIdB.setDescription('The Input Source Id is used to identify the input source for this ACP in different products. One or both parts of the Id may be used in identifying where the input for the ACP comes from. For example, the MPS uses the input source id to designate the location of the physical connector that is mapped to the ACP. In the case of the decrypt ACPs, InputSourceIdA is used to indicate the slot, and InputSourceIdB is used to indicate the port. Only decrypt ACPs have their source identified in this way. Encrypt ACPs do not have an identified source. ')
acpPidTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4), )
if mibBuilder.loadTexts: acpPidTable.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTable.setStatus('current')
if mibBuilder.loadTexts: acpPidTable.setDescription('A table of ACP entries giving assigned pid values')
acpPidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1), ).setIndexNames((0, "ACP-MIB", "acpPidTblEncryptType"), (0, "ACP-MIB", "acpPidTblUnitIndex"), (0, "ACP-MIB", "acpPidTblServiceIndex"), (0, "ACP-MIB", "acpPidTblPidIndex"))
if mibBuilder.loadTexts: acpPidEntry.setStatus('current')
if mibBuilder.loadTexts: acpPidEntry.setDescription('A row in the ACP Pid Table')
acpPidTblEncryptType = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("encryptAcp", 1), ("decryptAcp", 2))))
if mibBuilder.loadTexts: acpPidTblEncryptType.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblEncryptType.setStatus('current')
if mibBuilder.loadTexts: acpPidTblEncryptType.setDescription('The type of ACP in the system. It is either an encryptAcp or decryptAcp device. ')
acpPidTblUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: acpPidTblUnitIndex.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblUnitIndex.setStatus('current')
if mibBuilder.loadTexts: acpPidTblUnitIndex.setDescription('The ACP unit index for this encrypt/decrypt type. For each type of ACP, encryptAcp or decryptAcp, the physical unit number of the ACP in the containing product, starting at 1.')
acpPidTblServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: acpPidTblServiceIndex.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblServiceIndex.setStatus('current')
if mibBuilder.loadTexts: acpPidTblServiceIndex.setDescription('For a specified ACP, identified by the both acpEncryptType and acpUnitIndex. The maximum limit on the value of this index is determined by the Max number of services supported by this ACP (for a TSODA, it is 2). For all other objects in the acpStatusTable, this index is not used. (it must be valid, but will not be used to access the object uniquely specified by acpEncryptType and acpUnitIndex)')
acpPidTblPidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 4), Integer32())
if mibBuilder.loadTexts: acpPidTblPidIndex.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblPidIndex.setStatus('current')
if mibBuilder.loadTexts: acpPidTblPidIndex.setDescription('The PID index of the requested assigned PID value. multiple PIDs can be assigned per service')
acpPidTblAssignedPid = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpPidTblAssignedPid.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblAssignedPid.setStatus('current')
if mibBuilder.loadTexts: acpPidTblAssignedPid.setDescription('The PID assigned. If 0x1fff is returned then no PID is assigned.')
acpPidTblEcmPid = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpPidTblEcmPid.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblEcmPid.setStatus('current')
if mibBuilder.loadTexts: acpPidTblEcmPid.setDescription('The ECM PID cooresponding to the assigned PID. Value set to 0x1fff when no ECM PID is programmed.')
acpPidTblPidMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 1, 11, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpPidTblPidMask.setReference(' -- ')
if mibBuilder.loadTexts: acpPidTblPidMask.setStatus('current')
if mibBuilder.loadTexts: acpPidTblPidMask.setDescription("The PID mask used in conjunction with the assigned PID. Bits that are set in the PID Mask field of the ACP are 'dont cares' when comparing the PID of a received packet to the PID value configured in the ACP. For example, if the PID 0x0040 is configured in the ACP and the PID Mask is set to 0x000F, then any received packet with a PID from 0x0040 to 0x004F inclusive will be processed by the ACP. ")
acpMibRevision = MibScalar((1, 3, 6, 1, 4, 1, 1166, 1, 11, 99), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acpMibRevision.setReference(' -- ')
if mibBuilder.loadTexts: acpMibRevision.setStatus('current')
if mibBuilder.loadTexts: acpMibRevision.setDescription('The current revision number of acp.mib multiplied by 100. To extract the major revision number divide by 100. The remainder is the minor revision number. The major rev number should be bumped whenever structural changes occur that require coresponding manager changes. Small changes like editing a description should bump the minor rev. The mib revision is matches the one found at the top of acp.mib')
mibBuilder.exportSymbols("ACP-MIB", PYSNMP_MODULE_ID=acpStatus, acpNextProgramEpochNumber=acpNextProgramEpochNumber, acpNextServAuthorization=acpNextServAuthorization, acpPidTblServiceIndex=acpPidTblServiceIndex, acpCatSeqNums=acpCatSeqNums, acpInputSourceIdA=acpInputSourceIdA, acpPidTblEcmPid=acpPidTblEcmPid, acpInputSourceIdB=acpInputSourceIdB, acpServEncryption=acpServEncryption, acpPidTblPidIndex=acpPidTblPidIndex, acpUnitAddress=acpUnitAddress, acpServAuthReaCode=acpServAuthReaCode, acpEmmCount=acpEmmCount, acpStatusEntry=acpStatusEntry, acpServiceIndex=acpServiceIndex, acpInputInterface=acpInputInterface, acpPidEntry=acpPidEntry, acpOutputInterface=acpOutputInterface, acpStatusTable=acpStatusTable, acpProgramEpochNumber=acpProgramEpochNumber, acpPidTblUnitIndex=acpPidTblUnitIndex, acpScramblingMode=acpScramblingMode, acpNextServAuthReasonCode=acpNextServAuthReasonCode, acpNumberofEncryptTypes=acpNumberofEncryptTypes, acpMibRevision=acpMibRevision, acpNumberofDecryptTypes=acpNumberofDecryptTypes, acpServAuthorization=acpServAuthorization, acpPidTblAssignedPid=acpPidTblAssignedPid, acpPidTable=acpPidTable, acpEncryptType=acpEncryptType, acpServNumber=acpServNumber, acpPidTblEncryptType=acpPidTblEncryptType, acpStatus=acpStatus, acpUnitIndex=acpUnitIndex, acpPidTblPidMask=acpPidTblPidMask)
