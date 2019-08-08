#
# PySNMP MIB module SQUID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SQUID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, ObjectIdentity, Bits, Gauge32, iso, IpAddress, NotificationType, Integer32, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Bits", "Gauge32", "iso", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
squid = ModuleIdentity((1, 3, 6, 1, 4, 1, 3495, 1))
squid.setRevisions(('2008-12-24 02:00', '2007-12-14 00:00', '1999-01-01 00:00', '1998-09-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: squid.setRevisionsDescriptions(('Corrected MIB strictness requirements. Mapped valid port ranges', 'Added support for IPv6 Technology.', 'Added objects and corrected asn.1 syntax and descriptions.', 'Move to SMIv2. Prepare to split into proxy/squid.',))
if mibBuilder.loadTexts: squid.setLastUpdated('200812240200Z')
if mibBuilder.loadTexts: squid.setOrganization('National Laboratory for Applied Network Research')
if mibBuilder.loadTexts: squid.setContactInfo(' Squid Developers E-mail: squid@squid-cache.org')
if mibBuilder.loadTexts: squid.setDescription('Squid MIB defined for the management of the Squid proxy server. See http://www.squid-cache.org/.')
nlanr = MibIdentifier((1, 3, 6, 1, 4, 1, 3495))
cacheSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 1))
cacheConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 2))
cachePerf = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 3))
cacheNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 4))
cacheMesh = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 5))
cacheSysVMsize = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSysVMsize.setStatus('current')
if mibBuilder.loadTexts: cacheSysVMsize.setDescription(' Storage Mem size in KB ')
cacheSysStorage = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSysStorage.setStatus('current')
if mibBuilder.loadTexts: cacheSysStorage.setDescription(' Storage Swap size in KB ')
cacheUptime = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheUptime.setStatus('current')
if mibBuilder.loadTexts: cacheUptime.setDescription(' The Uptime of the cache in timeticks ')
cacheAdmin = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheAdmin.setStatus('current')
if mibBuilder.loadTexts: cacheAdmin.setDescription(' Cache Administrator E-Mail address ')
cacheSoftware = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSoftware.setStatus('current')
if mibBuilder.loadTexts: cacheSoftware.setDescription(' Cache Software Name ')
cacheVersionId = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheVersionId.setStatus('current')
if mibBuilder.loadTexts: cacheVersionId.setDescription(' Cache Software Version ')
cacheLoggingFacility = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacheLoggingFacility.setStatus('current')
if mibBuilder.loadTexts: cacheLoggingFacility.setDescription(' Logging Facility. An informational string indicating logging info like debug level, local/syslog/remote logging etc ')
cacheStorageConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 2, 5))
cacheMemMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheMemMaxSize.setStatus('current')
if mibBuilder.loadTexts: cacheMemMaxSize.setDescription(' The value of the cache_mem parameter in MB ')
cacheSwapMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSwapMaxSize.setStatus('current')
if mibBuilder.loadTexts: cacheSwapMaxSize.setDescription(' The total of the cache_dir space allocated in MB ')
cacheSwapHighWM = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSwapHighWM.setStatus('current')
if mibBuilder.loadTexts: cacheSwapHighWM.setDescription(' Cache Swap High Water Mark ')
cacheSwapLowWM = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSwapLowWM.setStatus('current')
if mibBuilder.loadTexts: cacheSwapLowWM.setDescription(' Cache Swap Low Water Mark ')
cacheUniqName = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheUniqName.setStatus('current')
if mibBuilder.loadTexts: cacheUniqName.setDescription(' Cache unique host name ')
cacheSysPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1))
cacheProtoStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2))
cacheSysPageFaults = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSysPageFaults.setStatus('current')
if mibBuilder.loadTexts: cacheSysPageFaults.setDescription(' Page faults with physical i/o ')
cacheSysNumReads = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheSysNumReads.setStatus('current')
if mibBuilder.loadTexts: cacheSysNumReads.setDescription(' HTTP I/O number of reads ')
cacheMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheMemUsage.setStatus('current')
if mibBuilder.loadTexts: cacheMemUsage.setDescription(' Total memory accounted for KB ')
cacheCpuTime = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCpuTime.setStatus('current')
if mibBuilder.loadTexts: cacheCpuTime.setDescription(' Amount of cpu seconds consumed ')
cacheCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCpuUsage.setStatus('current')
if mibBuilder.loadTexts: cacheCpuUsage.setDescription(' The percentage use of the CPU ')
cacheMaxResSize = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheMaxResSize.setStatus('current')
if mibBuilder.loadTexts: cacheMaxResSize.setDescription(' Maximum Resident Size in KB ')
cacheNumObjCount = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheNumObjCount.setStatus('current')
if mibBuilder.loadTexts: cacheNumObjCount.setDescription(' Number of objects stored by the cache ')
cacheCurrentLRUExpiration = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentLRUExpiration.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentLRUExpiration.setDescription(' Storage LRU Expiration Age ')
cacheCurrentUnlinkRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentUnlinkRequests.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentUnlinkRequests.setDescription(' Requests given to unlinkd ')
cacheCurrentUnusedFDescrCnt = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentUnusedFDescrCnt.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentUnusedFDescrCnt.setDescription(' Available number of file descriptors ')
cacheCurrentResFileDescrCnt = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentResFileDescrCnt.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentResFileDescrCnt.setDescription(' Reserved number of file descriptors ')
cacheCurrentFileDescrCnt = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentFileDescrCnt.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentFileDescrCnt.setDescription(' Number of file descriptors in use ')
cacheCurrentFileDescrMax = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentFileDescrMax.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentFileDescrMax.setDescription(' Highest file descriptors in use ')
cacheProtoAggregateStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1))
cacheProtoClientHttpRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheProtoClientHttpRequests.setStatus('current')
if mibBuilder.loadTexts: cacheProtoClientHttpRequests.setDescription(' Number of HTTP requests received ')
cacheHttpHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpHits.setStatus('current')
if mibBuilder.loadTexts: cacheHttpHits.setDescription(' Number of HTTP Hits ')
cacheHttpErrors = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpErrors.setStatus('current')
if mibBuilder.loadTexts: cacheHttpErrors.setDescription(' Number of HTTP Errors ')
cacheHttpInKb = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpInKb.setStatus('current')
if mibBuilder.loadTexts: cacheHttpInKb.setDescription(" Number of HTTP KB's received ")
cacheHttpOutKb = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpOutKb.setStatus('current')
if mibBuilder.loadTexts: cacheHttpOutKb.setDescription(" Number of HTTP KB's transmitted ")
cacheIcpPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpPktsSent.setStatus('current')
if mibBuilder.loadTexts: cacheIcpPktsSent.setDescription(' Number of ICP messages sent ')
cacheIcpPktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpPktsRecv.setStatus('current')
if mibBuilder.loadTexts: cacheIcpPktsRecv.setDescription(' Number of ICP messages received ')
cacheIcpKbSent = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpKbSent.setStatus('current')
if mibBuilder.loadTexts: cacheIcpKbSent.setDescription(" Number of ICP KB's transmitted ")
cacheIcpKbRecv = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpKbRecv.setStatus('current')
if mibBuilder.loadTexts: cacheIcpKbRecv.setDescription(" Number of ICP KB's received ")
cacheServerRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheServerRequests.setStatus('current')
if mibBuilder.loadTexts: cacheServerRequests.setDescription(' All requests from the client for the cache server ')
cacheServerErrors = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheServerErrors.setStatus('current')
if mibBuilder.loadTexts: cacheServerErrors.setDescription(' All errors for the cache server from client requests ')
cacheServerInKb = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheServerInKb.setStatus('current')
if mibBuilder.loadTexts: cacheServerInKb.setDescription(" KB's of traffic received from servers ")
cacheServerOutKb = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheServerOutKb.setStatus('current')
if mibBuilder.loadTexts: cacheServerOutKb.setDescription(" KB's of traffic sent to servers ")
cacheCurrentSwapSize = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheCurrentSwapSize.setStatus('current')
if mibBuilder.loadTexts: cacheCurrentSwapSize.setDescription(' Storage Swap size ')
cacheClients = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClients.setStatus('current')
if mibBuilder.loadTexts: cacheClients.setDescription(' Number of clients accessing cache ')
cacheMedianSvcTable = MibTable((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2), )
if mibBuilder.loadTexts: cacheMedianSvcTable.setStatus('current')
if mibBuilder.loadTexts: cacheMedianSvcTable.setDescription(' CacheMedianSvcTable ')
cacheMedianSvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1), ).setIndexNames((0, "SQUID-MIB", "cacheMedianTime"))
if mibBuilder.loadTexts: cacheMedianSvcEntry.setStatus('current')
if mibBuilder.loadTexts: cacheMedianSvcEntry.setDescription(' An entry in cacheMedianSvcTable ')
cacheMedianTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(5, 5), ValueRangeConstraint(60, 60), )))
if mibBuilder.loadTexts: cacheMedianTime.setStatus('current')
if mibBuilder.loadTexts: cacheMedianTime.setDescription(' The value used to index the table 1/5/60')
cacheHttpAllSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpAllSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheHttpAllSvcTime.setDescription(' HTTP all service time ')
cacheHttpMissSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpMissSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheHttpMissSvcTime.setDescription(' HTTP miss service time ')
cacheHttpNmSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpNmSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheHttpNmSvcTime.setDescription(' HTTP hit not-modified service time ')
cacheHttpHitSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpHitSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheHttpHitSvcTime.setDescription(' HTTP hit service time ')
cacheIcpQuerySvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpQuerySvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheIcpQuerySvcTime.setDescription(' ICP query service time ')
cacheIcpReplySvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIcpReplySvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheIcpReplySvcTime.setDescription(' ICP reply service time ')
cacheDnsSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheDnsSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheDnsSvcTime.setDescription(' DNS service time ')
cacheRequestHitRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheRequestHitRatio.setStatus('current')
if mibBuilder.loadTexts: cacheRequestHitRatio.setDescription(' Request Hit Ratios ')
cacheRequestByteRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheRequestByteRatio.setStatus('current')
if mibBuilder.loadTexts: cacheRequestByteRatio.setDescription(' Byte Hit Ratios ')
cacheHttpNhSvcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheHttpNhSvcTime.setStatus('current')
if mibBuilder.loadTexts: cacheHttpNhSvcTime.setDescription(' HTTP refresh hit service time ')
cacheIpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1))
cacheFqdnCache = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2))
cacheDns = MibIdentifier((1, 3, 6, 1, 4, 1, 3495, 1, 4, 3))
cacheIpEntries = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpEntries.setStatus('current')
if mibBuilder.loadTexts: cacheIpEntries.setDescription(' IP Cache Entries ')
cacheIpRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpRequests.setStatus('current')
if mibBuilder.loadTexts: cacheIpRequests.setDescription(' Number of IP Cache requests ')
cacheIpHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpHits.setStatus('current')
if mibBuilder.loadTexts: cacheIpHits.setDescription(' Number of IP Cache hits ')
cacheIpPendingHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpPendingHits.setStatus('current')
if mibBuilder.loadTexts: cacheIpPendingHits.setDescription(' Number of IP Cache pending hits ')
cacheIpNegativeHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpNegativeHits.setStatus('current')
if mibBuilder.loadTexts: cacheIpNegativeHits.setDescription(' Number of IP Cache negative hits ')
cacheIpMisses = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheIpMisses.setStatus('current')
if mibBuilder.loadTexts: cacheIpMisses.setDescription(' Number of IP Cache misses ')
cacheBlockingGetHostByName = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheBlockingGetHostByName.setStatus('current')
if mibBuilder.loadTexts: cacheBlockingGetHostByName.setDescription(' Number of blocking gethostbyname requests ')
cacheAttemptReleaseLckEntries = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheAttemptReleaseLckEntries.setStatus('current')
if mibBuilder.loadTexts: cacheAttemptReleaseLckEntries.setDescription(' Number of attempts to release locked IP Cache entries ')
cacheFqdnEntries = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnEntries.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnEntries.setDescription(' FQDN Cache entries ')
cacheFqdnRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnRequests.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnRequests.setDescription(' Number of FQDN Cache requests ')
cacheFqdnHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnHits.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnHits.setDescription(' Number of FQDN Cache hits ')
cacheFqdnPendingHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnPendingHits.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnPendingHits.setDescription(' Number of FQDN Cache pending hits ')
cacheFqdnNegativeHits = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnNegativeHits.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnNegativeHits.setDescription(' Number of FQDN Cache negative hits ')
cacheFqdnMisses = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheFqdnMisses.setStatus('current')
if mibBuilder.loadTexts: cacheFqdnMisses.setDescription(' Number of FQDN Cache misses ')
cacheBlockingGetHostByAddr = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheBlockingGetHostByAddr.setStatus('current')
if mibBuilder.loadTexts: cacheBlockingGetHostByAddr.setDescription(' Number of blocking gethostbyaddr requests ')
cacheDnsRequests = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheDnsRequests.setStatus('current')
if mibBuilder.loadTexts: cacheDnsRequests.setDescription(' Number of external DNS server requests ')
cacheDnsReplies = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheDnsReplies.setStatus('current')
if mibBuilder.loadTexts: cacheDnsReplies.setDescription(' Number of external DNS server replies ')
cacheDnsNumberServers = MibScalar((1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheDnsNumberServers.setStatus('current')
if mibBuilder.loadTexts: cacheDnsNumberServers.setDescription(' Number of external DNS server processes ')
cachePeerTable = MibTable((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1), )
if mibBuilder.loadTexts: cachePeerTable.setStatus('current')
if mibBuilder.loadTexts: cachePeerTable.setDescription(' This table contains an enumeration of the peer caches, complete with info ')
cachePeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3), ).setIndexNames((0, "SQUID-MIB", "cachePeerIndex"))
if mibBuilder.loadTexts: cachePeerEntry.setStatus('current')
if mibBuilder.loadTexts: cachePeerEntry.setDescription(' An entry in cachePeerTable (version 3) ')
class ValidPort(TextualConvention, Integer32):
    description = 'A integer value from 1 to 65535 to indicate the appropriate port number for the connection.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class CachePeerTableIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero for each cache peer instance in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each cache peer index must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

cachePeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 1), CachePeerTableIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerIndex.setStatus('current')
if mibBuilder.loadTexts: cachePeerIndex.setDescription('A unique non-zero value identifying the particular cache Peer.')
cachePeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerName.setStatus('current')
if mibBuilder.loadTexts: cachePeerName.setDescription(' The FQDN name or internal alias for the peer cache ')
cachePeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerAddressType.setStatus('current')
if mibBuilder.loadTexts: cachePeerAddressType.setDescription('The type of Internet address by which the peer cache is reachable.')
cachePeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 4), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerAddress.setStatus('current')
if mibBuilder.loadTexts: cachePeerAddress.setDescription('The Internet address for the peer cache. The type of this address is determined by the value of the peerAddressType object. Note that implementations must limit themselves to a single entry in this table per reachable peer. The peerAddress may not be empty due to the SIZE restriction. If a row is created administratively by an SNMP operation and the address type value is dns(16), then the agent stores the DNS name internally. A DNS name lookup must be performed on the internally stored DNS name whenever it is being used to contact the peer. If a row is created by the managed entity itself and the address type value is dns(16), then the agent stores the IP address internally. A DNS reverse lookup must be performed on the internally stored IP address whenever the value is retrieved via SNMP.')
cachePeerPortHttp = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 5), ValidPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerPortHttp.setStatus('current')
if mibBuilder.loadTexts: cachePeerPortHttp.setDescription(' The port the peer listens for HTTP requests ')
cachePeerPortIcp = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 6), ValidPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerPortIcp.setStatus('current')
if mibBuilder.loadTexts: cachePeerPortIcp.setDescription(' The port the peer listens for ICP requests should be 0 if not configured to send ICP requests ')
cachePeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerType.setStatus('current')
if mibBuilder.loadTexts: cachePeerType.setDescription(' Peer Type ')
cachePeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerState.setStatus('current')
if mibBuilder.loadTexts: cachePeerState.setDescription(' The operational state of this peer ')
cachePeerPingsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerPingsSent.setStatus('current')
if mibBuilder.loadTexts: cachePeerPingsSent.setDescription(' Number of pings sent to peer ')
cachePeerPingsAcked = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerPingsAcked.setStatus('current')
if mibBuilder.loadTexts: cachePeerPingsAcked.setDescription(' Number of pings received from peer ')
cachePeerFetches = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerFetches.setStatus('current')
if mibBuilder.loadTexts: cachePeerFetches.setDescription(' Number of times this peer was selected ')
cachePeerRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerRtt.setStatus('current')
if mibBuilder.loadTexts: cachePeerRtt.setDescription(' Last known round-trip time to the peer (in ms) ')
cachePeerIgnored = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerIgnored.setStatus('current')
if mibBuilder.loadTexts: cachePeerIgnored.setDescription(' How many times this peer was ignored ')
cachePeerKeepAlSent = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerKeepAlSent.setStatus('current')
if mibBuilder.loadTexts: cachePeerKeepAlSent.setDescription(' Number of keepalives sent ')
cachePeerKeepAlRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cachePeerKeepAlRecv.setStatus('current')
if mibBuilder.loadTexts: cachePeerKeepAlRecv.setDescription(' Number of keepalives received ')
cacheClientTable = MibTable((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2), )
if mibBuilder.loadTexts: cacheClientTable.setStatus('current')
if mibBuilder.loadTexts: cacheClientTable.setDescription('A list of cache client entries.')
cacheClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2), ).setIndexNames((0, "SQUID-MIB", "cacheClientAddress"))
if mibBuilder.loadTexts: cacheClientEntry.setStatus('current')
if mibBuilder.loadTexts: cacheClientEntry.setDescription('An IP entry in cacheClientTable ')
cacheClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientAddressType.setStatus('current')
if mibBuilder.loadTexts: cacheClientAddressType.setDescription("The client's IP address ")
cacheClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientAddress.setStatus('current')
if mibBuilder.loadTexts: cacheClientAddress.setDescription('The Internet address for the client. The type of this address is determined by the value of the peerAddressType object. Note that implementations must limit themselves to a single entry in this table per reachable peer. The peerAddress may not be empty due to the SIZE restriction. If a row is created administratively by an SNMP operation and the address type value is dns(16), then the agent stores the DNS name internally. A DNS name lookup must be performed on the internally stored DNS name whenever it is being used to contact the peer. If a row is created by the managed entity itself and the address type value is dns(16), then the agent stores the IP address internally. A DNS reverse lookup must be performed on the internally stored IP address whenever the value is retrieved via SNMP.')
cacheClientHttpRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientHttpRequests.setStatus('current')
if mibBuilder.loadTexts: cacheClientHttpRequests.setDescription(' Number of HTTP requests received from client ')
cacheClientHttpKb = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientHttpKb.setStatus('current')
if mibBuilder.loadTexts: cacheClientHttpKb.setDescription(' Amount of total HTTP traffic to this client ')
cacheClientHttpHits = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientHttpHits.setStatus('current')
if mibBuilder.loadTexts: cacheClientHttpHits.setDescription(" Number of hits in response to this client's HTTP requests ")
cacheClientHTTPHitKb = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientHTTPHitKb.setStatus('current')
if mibBuilder.loadTexts: cacheClientHTTPHitKb.setDescription(' Amount of HTTP hit traffic in KB ')
cacheClientIcpRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientIcpRequests.setStatus('current')
if mibBuilder.loadTexts: cacheClientIcpRequests.setDescription(' Number of ICP requests received from client ')
cacheClientIcpKb = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientIcpKb.setStatus('current')
if mibBuilder.loadTexts: cacheClientIcpKb.setDescription(' Amount of total ICP traffic to this client (child) ')
cacheClientIcpHits = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientIcpHits.setStatus('current')
if mibBuilder.loadTexts: cacheClientIcpHits.setDescription(" Number of hits in response to this client's ICP requests ")
cacheClientIcpHitKb = MibTableColumn((1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacheClientIcpHitKb.setStatus('current')
if mibBuilder.loadTexts: cacheClientIcpHitKb.setDescription(' Amount of ICP hit traffic in KB ')
mibBuilder.exportSymbols("SQUID-MIB", PYSNMP_MODULE_ID=squid, cacheClientEntry=cacheClientEntry, cachePeerIgnored=cachePeerIgnored, cacheClientAddress=cacheClientAddress, cacheIpHits=cacheIpHits, cachePeerPortIcp=cachePeerPortIcp, cacheFqdnNegativeHits=cacheFqdnNegativeHits, cacheMedianTime=cacheMedianTime, cacheProtoClientHttpRequests=cacheProtoClientHttpRequests, cacheCurrentUnusedFDescrCnt=cacheCurrentUnusedFDescrCnt, cacheSystem=cacheSystem, cacheIcpReplySvcTime=cacheIcpReplySvcTime, cacheIcpQuerySvcTime=cacheIcpQuerySvcTime, cacheIcpPktsRecv=cacheIcpPktsRecv, cacheMesh=cacheMesh, cachePeerPingsAcked=cachePeerPingsAcked, cacheSoftware=cacheSoftware, cacheStorageConfig=cacheStorageConfig, cacheSysPerf=cacheSysPerf, cachePeerType=cachePeerType, cacheCpuTime=cacheCpuTime, cacheAttemptReleaseLckEntries=cacheAttemptReleaseLckEntries, CachePeerTableIndex=CachePeerTableIndex, cacheConfig=cacheConfig, cacheCurrentUnlinkRequests=cacheCurrentUnlinkRequests, cacheDnsNumberServers=cacheDnsNumberServers, cachePeerKeepAlSent=cachePeerKeepAlSent, cacheIpNegativeHits=cacheIpNegativeHits, cacheCurrentFileDescrCnt=cacheCurrentFileDescrCnt, cacheNumObjCount=cacheNumObjCount, cacheClients=cacheClients, cachePeerFetches=cachePeerFetches, cacheHttpNmSvcTime=cacheHttpNmSvcTime, cacheMaxResSize=cacheMaxResSize, cacheFqdnCache=cacheFqdnCache, cacheFqdnEntries=cacheFqdnEntries, cacheIpPendingHits=cacheIpPendingHits, cacheUniqName=cacheUniqName, cacheClientHttpKb=cacheClientHttpKb, cacheServerInKb=cacheServerInKb, ValidPort=ValidPort, cacheDnsSvcTime=cacheDnsSvcTime, cachePeerTable=cachePeerTable, cachePeerPortHttp=cachePeerPortHttp, cacheIpEntries=cacheIpEntries, cacheIcpKbRecv=cacheIcpKbRecv, cacheClientHttpRequests=cacheClientHttpRequests, cacheSysPageFaults=cacheSysPageFaults, cacheLoggingFacility=cacheLoggingFacility, cacheClientHTTPHitKb=cacheClientHTTPHitKb, cacheCurrentResFileDescrCnt=cacheCurrentResFileDescrCnt, cacheCurrentSwapSize=cacheCurrentSwapSize, cachePeerEntry=cachePeerEntry, cacheMemUsage=cacheMemUsage, cacheMedianSvcTable=cacheMedianSvcTable, cacheBlockingGetHostByAddr=cacheBlockingGetHostByAddr, cacheAdmin=cacheAdmin, cacheClientIcpRequests=cacheClientIcpRequests, cacheHttpAllSvcTime=cacheHttpAllSvcTime, cachePeerAddress=cachePeerAddress, cacheClientTable=cacheClientTable, cacheCpuUsage=cacheCpuUsage, cacheHttpMissSvcTime=cacheHttpMissSvcTime, cachePeerRtt=cachePeerRtt, cacheFqdnPendingHits=cacheFqdnPendingHits, cacheSwapHighWM=cacheSwapHighWM, cacheHttpNhSvcTime=cacheHttpNhSvcTime, cacheRequestHitRatio=cacheRequestHitRatio, cacheIpRequests=cacheIpRequests, cacheClientAddressType=cacheClientAddressType, cacheClientHttpHits=cacheClientHttpHits, cacheSysStorage=cacheSysStorage, nlanr=nlanr, cacheProtoStats=cacheProtoStats, cacheHttpInKb=cacheHttpInKb, cacheCurrentFileDescrMax=cacheCurrentFileDescrMax, cacheBlockingGetHostByName=cacheBlockingGetHostByName, cacheMemMaxSize=cacheMemMaxSize, cachePerf=cachePerf, cacheIcpPktsSent=cacheIcpPktsSent, cacheIcpKbSent=cacheIcpKbSent, cacheMedianSvcEntry=cacheMedianSvcEntry, cacheUptime=cacheUptime, cacheServerErrors=cacheServerErrors, cacheClientIcpHitKb=cacheClientIcpHitKb, cacheHttpHits=cacheHttpHits, cacheServerOutKb=cacheServerOutKb, cacheFqdnRequests=cacheFqdnRequests, cacheSwapMaxSize=cacheSwapMaxSize, cacheClientIcpKb=cacheClientIcpKb, cachePeerPingsSent=cachePeerPingsSent, cacheRequestByteRatio=cacheRequestByteRatio, cacheCurrentLRUExpiration=cacheCurrentLRUExpiration, cacheFqdnHits=cacheFqdnHits, cacheNetwork=cacheNetwork, cacheHttpOutKb=cacheHttpOutKb, cachePeerName=cachePeerName, cachePeerKeepAlRecv=cachePeerKeepAlRecv, squid=squid, cachePeerState=cachePeerState, cacheDnsRequests=cacheDnsRequests, cacheIpCache=cacheIpCache, cacheDnsReplies=cacheDnsReplies, cachePeerIndex=cachePeerIndex, cacheHttpHitSvcTime=cacheHttpHitSvcTime, cachePeerAddressType=cachePeerAddressType, cacheIpMisses=cacheIpMisses, cacheProtoAggregateStats=cacheProtoAggregateStats, cacheDns=cacheDns, cacheSwapLowWM=cacheSwapLowWM, cacheSysNumReads=cacheSysNumReads, cacheHttpErrors=cacheHttpErrors, cacheFqdnMisses=cacheFqdnMisses, cacheClientIcpHits=cacheClientIcpHits, cacheServerRequests=cacheServerRequests, cacheVersionId=cacheVersionId, cacheSysVMsize=cacheSysVMsize)