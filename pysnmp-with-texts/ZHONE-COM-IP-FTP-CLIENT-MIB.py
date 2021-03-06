#
# PySNMP MIB module ZHONE-COM-IP-FTP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-FTP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
zhoneModules, zhoneIp = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneIp")
ZhoneAdminString, ZhoneFileName, ZhoneRowStatus = mibBuilder.importSymbols("Zhone-TC", "ZhoneAdminString", "ZhoneFileName", "ZhoneRowStatus")
comIpFtpClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 68))
comIpFtpClient.setRevisions(('2001-01-11 15:59', '2000-09-18 11:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comIpFtpClient.setRevisionsDescriptions(('V01.01.00 - Added zhoneModules and markup language', 'V01.00.00 - Initial Release',))
if mibBuilder.loadTexts: comIpFtpClient.setLastUpdated('200101081559Z')
if mibBuilder.loadTexts: comIpFtpClient.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: comIpFtpClient.setContactInfo('Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: comIpFtpClient.setDescription('This MIB defines the fields use by a manager to create a ftp request. The mib equates those fields in the command line request to an equivalent table entry. The system allows for up to 20 FTP requests to be concurrently executing.')
ftpClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18))
if mibBuilder.loadTexts: ftpClient.setStatus('current')
if mibBuilder.loadTexts: ftpClient.setDescription('FTP Client Objects.')
ftpClientNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientNextIndex.setStatus('current')
if mibBuilder.loadTexts: ftpClientNextIndex.setDescription('The next available index to be used for an FTP request. The manager performs a get on this variable to determine which index to utilize for its request. The agent controls this value and tracks which are in use and how many current requests are outstanding. An okay return is indicated by a value of 1-20 for which the manager can use for creating an ftp row/request. A value of 0 indicates there are no entries available (20 ftp requests are currently in progress. When this occurs, the ftpClientIndexFailures is incremented.')
ftpClientHighRequests = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientHighRequests.setStatus('current')
if mibBuilder.loadTexts: ftpClientHighRequests.setDescription('The highest number of requests that the agent has processed at one time. Because it is up to the manager to delete a ftp request, even after completion, this number may be artificially high as it only tracks the number of index values in use.')
ftpClientAutoRemovals = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientAutoRemovals.setStatus('current')
if mibBuilder.loadTexts: ftpClientAutoRemovals.setDescription('The number of times a manager tried to initiate an ftp request (get of ftpClientNextIndex), and there were not available indexes. In this case, the agent deletes the oldest completed ftp request and increments this object by 1.')
ftpClientIndexFailures = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientIndexFailures.setStatus('current')
if mibBuilder.loadTexts: ftpClientIndexFailures.setDescription('The number of times a get was performed on the ftpClientNextIndex field and all indexes were in use (all had ftp requests in progress)')
ftpClientRequestTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5), )
if mibBuilder.loadTexts: ftpClientRequestTable.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestTable.setDescription("The table of ftp requests. An FTP request is initiated by a manager by setting the required values and setting the ftpClientRequestRowStatus to 'createAndGo'. An FTP request is stopped and deleted by setting the ftpClientRequestRowStatus to 'destroy'. The manager obtains the index to utilize by getting the next available index (get to ftpClientNextIndex).")
ftpClientRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1), ).setIndexNames((0, "ZHONE-COM-IP-FTP-CLIENT-MIB", "ftpClientRequestIndex"))
if mibBuilder.loadTexts: ftpClientRequestEntry.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestEntry.setDescription('Each row of this table represents an ftp request that may either be in progress or completed (see ftpClientRequestResult). The manager both creates and deletes entries utilizing the ftpClientRequestRowStatus field. Entries are not deleted by the agent unless a new request is made (get to ftpClientNextIndex) and all indexes are utilized. In this case, the oldest completed request is auto-deleted and then made available for the manager.')
ftpClientRequestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: ftpClientRequestIndex.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestIndex.setDescription('The index of this FTP request in this table. There is a maximum number of 20 outstanding requests in the system.')
ftpClientRequestCode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("putBinary", 1), ("putAscii", 2), ("getBinary", 3), ("getAscii", 4))).clone('putBinary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestCode.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestCode.setDescription("The operation requested by the manager with the default being a 'put' of a file in binary mode. These are the normal ftp operations allowed in being able to transfer a file in either binary or ASCII modes.")
ftpClientRequestLocalFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 3), ZhoneFileName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestLocalFileName.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestLocalFileName.setDescription('The local file name to be used in the ftp operation. No default value is specified and this field must be specified on a row creation.')
ftpClientRequestRemoteFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 4), ZhoneFileName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestRemoteFileName.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestRemoteFileName.setDescription('The remote filename used in the ftp operation. This value must be specified when the row is created and there is no default value.')
ftpClientRequestServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 5), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestServerAddress.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestServerAddress.setDescription('Either the ip address or name specifying the location of the FTP server. This value must be specified on the row create and there is no default value.')
ftpClientRequestUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 6), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestUserName.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestUserName.setDescription('The user name to be used during the authentication process with the FTP server. This field must be specified on the row create and there is no default value.')
ftpClientRequestPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 7), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestPassword.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestPassword.setDescription('The password associated with this user named which is used during the authentication process with the FTP server. This value must be present during the row create and there is no default value. When this variable is read (get), a null string is always returned.')
ftpClientRequestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inProgress", 1), ("success", 2), ("stoppedByUser", 3), ("localFileNameError", 4), ("remoteFileNameError", 5), ("unreachableDestination", 6), ("invalidUserNamePassword", 7), ("tooManyOpenFiles", 8), ("readError", 9), ("writeError", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientRequestResult.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestResult.setDescription('The results of the FTP operation. The possible values are: inProgress - currently executing the request success - file has been transferred stoppedByUser - operation was aborted localFileNameError - File could not be read or written on the local system. remoteFileNameError - File could not be read or written on the remote system unreachableDestination - the ip address or server name could not be reached. invalidUserNamePassword - The user name/password combination could not be authenticated by the ftp server. tooManyOpenFiles - File could not be opened due to too many files already opened. readError - Transfer not completed due to a file read error. writeError - Transfer not completed due to a file write error. ')
ftpClientRequestAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2))).clone('start')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestAction.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestAction.setDescription("The action requested by the user. The normal operation is for a 'start' to be specified and this is the default value. Specifying 'stop' aborts the current operation in the current state. Specifying 'stop' with 'createAndGo' rowStatus results in the creation of the row. But the ftp transfer does not start until the row is specified to 'start'. Specifying multiple successive mstops or starts has no impact on the current operation. When read, the value returned is the last action requested.")
ftpClientRequestCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientRequestCompletionTime.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestCompletionTime.setDescription('The time when the operation completed. This includes if the operation was aborted. While the operation is in progress, a value of 0 is returned.')
ftpClientRequestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 11), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestRowStatus.setStatus('current')
if mibBuilder.loadTexts: ftpClientRequestRowStatus.setDescription("The rowstatus is used by the manager to create or destroy a ftp request. Required fields on a create_and_go are: - local and remote filenames - server address or name - user name - password A get on this field always return 'active'.")
mibBuilder.exportSymbols("ZHONE-COM-IP-FTP-CLIENT-MIB", comIpFtpClient=comIpFtpClient, ftpClientHighRequests=ftpClientHighRequests, ftpClientRequestServerAddress=ftpClientRequestServerAddress, PYSNMP_MODULE_ID=comIpFtpClient, ftpClientAutoRemovals=ftpClientAutoRemovals, ftpClientRequestEntry=ftpClientRequestEntry, ftpClientRequestLocalFileName=ftpClientRequestLocalFileName, ftpClientRequestAction=ftpClientRequestAction, ftpClientRequestPassword=ftpClientRequestPassword, ftpClientIndexFailures=ftpClientIndexFailures, ftpClientRequestRemoteFileName=ftpClientRequestRemoteFileName, ftpClientRequestCompletionTime=ftpClientRequestCompletionTime, ftpClientNextIndex=ftpClientNextIndex, ftpClient=ftpClient, ftpClientRequestIndex=ftpClientRequestIndex, ftpClientRequestUserName=ftpClientRequestUserName, ftpClientRequestResult=ftpClientRequestResult, ftpClientRequestCode=ftpClientRequestCode, ftpClientRequestTable=ftpClientRequestTable, ftpClientRequestRowStatus=ftpClientRequestRowStatus)
