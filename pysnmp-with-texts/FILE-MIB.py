#
# PySNMP MIB module FILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, NotificationType, Bits, MibIdentifier, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, IpAddress, Unsigned32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "Bits", "MibIdentifier", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraFileMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 120))
if mibBuilder.loadTexts: tiaraFileMib.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: tiaraFileMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraFileMib.setContactInfo(' Tiara Networks Customer Service Postal: 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraFileMib.setDescription('')
fileTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1), )
if mibBuilder.loadTexts: fileTable.setStatus('current')
if mibBuilder.loadTexts: fileTable.setDescription('File Table')
fileTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1), ).setIndexNames((0, "FILE-MIB", "fileOwnerString"), (0, "FILE-MIB", "fileSequenceNumber"))
if mibBuilder.loadTexts: fileTableEntry.setStatus('current')
if mibBuilder.loadTexts: fileTableEntry.setDescription(' An Entry in File Table')
fileOwnerString = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: fileOwnerString.setStatus('current')
if mibBuilder.loadTexts: fileOwnerString.setDescription(' owner String: a unique name for identify the owner')
fileSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: fileSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: fileSequenceNumber.setDescription(' Whenever the Mgr has to create a Row. He has to provide a invalid Numeric Index (0XFFFF). This will result in appending the row to the table. When the row is created, a unique numeric Index for the row is internally generated. For querying any variable in the table for a particular row or to know number of rows exisiting in the table the Mgr can do a SNMP walk.')
fileSrcFile = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileSrcFile.setStatus('current')
if mibBuilder.loadTexts: fileSrcFile.setDescription('Source File ')
fileDestFile = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileDestFile.setStatus('current')
if mibBuilder.loadTexts: fileDestFile.setDescription('Destnation File ')
fileHostIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileHostIpAddr.setStatus('current')
if mibBuilder.loadTexts: fileHostIpAddr.setDescription(' host Ip Address')
fileLocationOfFile = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ic", 1), ("ncm", 2), ("none", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileLocationOfFile.setStatus('current')
if mibBuilder.loadTexts: fileLocationOfFile.setDescription(' Location of the File that has to be downloaded')
fileSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileSlotNumber.setStatus('current')
if mibBuilder.loadTexts: fileSlotNumber.setDescription(' The Slot within NCM or IC')
fileUploadFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("eventlog", 1), ("flashfile", 2), ("none", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileUploadFileType.setStatus('current')
if mibBuilder.loadTexts: fileUploadFileType.setDescription(' Name of teh file to be uploaded')
filePerformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("copy", 1), ("download", 2), ("format", 3), ("list", 4), ("remove", 5), ("upload", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: filePerformAction.setStatus('current')
if mibBuilder.loadTexts: filePerformAction.setDescription(' Action to be performed')
fileActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("inProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileActionStatus.setStatus('current')
if mibBuilder.loadTexts: fileActionStatus.setDescription(' Status of the action')
fileListData = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileListData.setStatus('current')
if mibBuilder.loadTexts: fileListData.setDescription(' This lists the file for a list command ')
fileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fileRowStatus.setStatus('current')
if mibBuilder.loadTexts: fileRowStatus.setDescription(' Used to Add or Delete a row in the table')
mibBuilder.exportSymbols("FILE-MIB", fileUploadFileType=fileUploadFileType, fileHostIpAddr=fileHostIpAddr, fileOwnerString=fileOwnerString, tiaraFileMib=tiaraFileMib, fileSlotNumber=fileSlotNumber, fileTable=fileTable, fileLocationOfFile=fileLocationOfFile, PYSNMP_MODULE_ID=tiaraFileMib, fileListData=fileListData, fileActionStatus=fileActionStatus, fileRowStatus=fileRowStatus, filePerformAction=filePerformAction, fileTableEntry=fileTableEntry, fileSequenceNumber=fileSequenceNumber, fileDestFile=fileDestFile, fileSrcFile=fileSrcFile)
