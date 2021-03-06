#
# PySNMP MIB module REDSTONE-RADIUS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-RADIUS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, Counter32, Integer32, Bits, IpAddress, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter32", "Integer32", "Bits", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rsRadiusClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 19))
rsRadiusClientMIB.setRevisions(('1999-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsRadiusClientMIB.setRevisionsDescriptions(('Initial version of this MIB module, derived from IETF Internet Drafts of RADIUS Client MIBs for Authentication and Accounting.',))
if mibBuilder.loadTexts: rsRadiusClientMIB.setLastUpdated('9906010000Z')
if mibBuilder.loadTexts: rsRadiusClientMIB.setOrganization('Redstone Communications Inc.')
if mibBuilder.loadTexts: rsRadiusClientMIB.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsRadiusClientMIB.setDescription('The RADIUS Client MIB for the Redstone Communications Inc. enterprise.')
rsRadiusClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1))
rsRadiusGeneralClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1))
rsRadiusAuthClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2))
rsRadiusAcctClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3))
rsRadiusClientIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusClientIdentifier.setStatus('current')
if mibBuilder.loadTexts: rsRadiusClientIdentifier.setDescription('The NAS-Identifier of the RADIUS client.')
rsRadiusClientAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("direct", 0), ("roundRobin", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRadiusClientAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rsRadiusClientAlgorithm.setDescription('The algorithm used by the client when multiple authentication/accounting servers are configured: direct Use servers in order of precedence, each time beginning with the highest precedence server and proceeding to lower precedence servers if the the RADIUS request fails, until the request succeeds or all servers have been tried. roundRobin Use servers in round-robin order, each time beginning with the next round-robin-ordered server and proceeding cyclically through servers if the RADIUS request fails, until the request succeeds or all servers have been tried.')
rsRadiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientInvalidServerAddresses.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientInvalidServerAddresses.setDescription('The number of RADIUS Access-Response packets received from unknown addresses.')
rsRadiusAuthClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2), )
if mibBuilder.loadTexts: rsRadiusAuthClientServerTable.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientServerTable.setDescription('The (conceptual) table listing the RADIUS authentication servers with which the client shares a secret.')
rsRadiusAuthClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAuthClientServerEntry.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientServerEntry.setDescription('An entry (conceptual row) representing a RADIUS authentication server with which the client shares a secret.')
rsRadiusAuthClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAuthClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientServerAddress.setDescription('The IP address of the RADIUS authentication server referred to in this table entry. A value of 0.0.0.0 indicates this entry is not in use.')
rsRadiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientServerPortNumber.setDescription('The UDP port the client is using to send requests to this server.')
rsRadiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientRoundTripTime.setDescription('The time interval (in hundredths of a second) between the most recent Access-Reply/Access-Challenge and the Access-Request that matched it from this RADIUS authentication server.')
rsRadiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRequests.setDescription('The number of RADIUS Access-Request packets sent to this server. This does not include retransmissions.')
rsRadiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRetransmissions.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRetransmissions.setDescription('The number of RADIUS Access-Request packets retransmitted to this RADIUS authentication server.')
rsRadiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessAccepts.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientAccessAccepts.setDescription('The number of RADIUS Access-Accept packets (valid or invalid) received from this server.')
rsRadiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRejects.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRejects.setDescription('The number of RADIUS Access-Reject packets (valid or invalid) received from this server.')
rsRadiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessChallenges.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientAccessChallenges.setDescription('The number of RADIUS Access-Challenge packets (valid or invalid) received from this server.')
rsRadiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientMalformedAccessResponses.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientMalformedAccessResponses.setDescription('The number of malformed RADIUS Access-Response packets received from this server. Malformed packets include packets with an invalid length. Bad authenticators or Signature attributes or unknown types are not included as malformed access responses.')
rsRadiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientBadAuthenticators.setDescription('The number of RADIUS Access-Response packets containing invalid authenticators or Signature attributes received from this server.')
rsRadiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientPendingRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientPendingRequests.setDescription('The number of RADIUS Access-Request packets destined for this server that have not yet timed out or received a response. This variable is incremented when an Access-Request is sent and decremented due to receipt of an Acess-Accept, Access-Reject or Access-Challenge, a timeout or retransmission.')
rsRadiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientTimeouts.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientTimeouts.setDescription('The number of authentication timeouts to this server. After a timeout the client may retry to the same server, send to a different server, or give up. A retry to the same server is counted as a retransmit as well as a timeout. A send to a different server is counted as a Request as well as a timeout.')
rsRadiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientUnknownTypes.setDescription('The number of RADIUS packets of unknown type which were received from this server on the authentication port.')
rsRadiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientPacketsDropped.setDescription('The number of RADIUS packets of which were received from this server on the authentication port and dropped for some other reason.')
rsRadiusAuthClientCfgServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3), )
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerTable.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerTable.setDescription('The (conceptual) table listing the RADIUS authentication servers with which the client shares a secret.')
rsRadiusAuthClientCfgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerEntry.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerEntry.setDescription('An entry (conceptual row) representing a RADIUS authentication server with which the client shares a secret.')
rsRadiusAuthClientCfgServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerAddress.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerAddress.setDescription('The IP address of the RADIUS authentication server referred to in this table entry.')
rsRadiusAuthClientCfgServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerPortNumber.setDescription('The UDP port the client is using to send requests to this server. Default is 1812.')
rsRadiusAuthClientCfgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgKey.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgKey.setDescription('The secret (RADIUS authenticator) used by the client during exchanges with this authentication server. The default is a zero-length string, indicating no authenticator is used.')
rsRadiusAuthClientCfgTimeoutInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgTimeoutInterval.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgTimeoutInterval.setDescription('The interval between retransmissions of a request to this authentication server. The default is 3.')
rsRadiusAuthClientCfgRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRetries.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRetries.setDescription('The maximum number of times to resend a request to this authentication server (in addition to the original request), before resorting to the server specified in the next entry. The default is 3.')
rsRadiusAuthClientCfgMaxPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgMaxPendingRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgMaxPendingRequests.setDescription('The maximum number of outstanding requests this server can support. The default is 255.')
rsRadiusAuthClientCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRowStatus.setDescription("Supports 'createAndGo' and 'destroy' only.")
rsRadiusAuthClientCfgPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgPrecedence.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgPrecedence.setDescription('Relative precedence of this server with respect to other servers configured in this table. Lower values correspond to higher precedence. Precedence is assigned by the device, in order of entry creation, from higher to lower precedence.')
rsRadiusAuthClientCfgDeadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgDeadTime.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCfgDeadTime.setDescription('The period of time, in minutes, to ignore this server after a request to the server times out (thereby avoiding additional request timeouts for this period, if the server failure persists).')
rsRadiusAcctClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientInvalidServerAddresses.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientInvalidServerAddresses.setDescription('The number of RADIUS Accounting-Response packets received from unknown addresses.')
rsRadiusAcctClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2), )
if mibBuilder.loadTexts: rsRadiusAcctClientServerTable.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientServerTable.setDescription('The (conceptual) table listing the RADIUS accounting servers with which the client shares a secret.')
rsRadiusAcctClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAcctClientServerEntry.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientServerEntry.setDescription('An entry (conceptual row) representing a RADIUS accounting server with which the client shares a secret.')
rsRadiusAcctClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAcctClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientServerAddress.setDescription('The IP address of the RADIUS accounting server referred to in this table entry. A value of 0.0.0.0 indicates this entry is not in use.')
rsRadiusAcctClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientServerPortNumber.setDescription('The UDP port the client is using to send requests to this server.')
rsRadiusAcctClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientRoundTripTime.setDescription('The time interval between the most recent Accounting-Response and the Accounting-Request that matched it from this RADIUS accounting server.')
rsRadiusAcctClientRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientRequests.setDescription('The number of RADIUS Accounting-Request packets sent. This does not include retransmissions.')
rsRadiusAcctClientRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRetransmissions.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientRetransmissions.setDescription('The number of RADIUS Accounting-Request packets retransmitted to this RADIUS accounting server. Retransmissions include retries where the Identifier and Acct-Delay have been updated, as well as those in which they remain the same.')
rsRadiusAcctClientResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientResponses.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientResponses.setDescription('The number of RADIUS packets received on the accounting port from this server.')
rsRadiusAcctClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientMalformedResponses.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientMalformedResponses.setDescription('The number of malformed RADIUS Accounting-Response packets received from this server. Malformed packets include packets with an invalid length. Bad authenticators and unknown types are not included as malformed accounting responses.')
rsRadiusAcctClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientBadAuthenticators.setDescription('The number of RADIUS Accounting-Response packets which contained invalid authenticators received from this server.')
rsRadiusAcctClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientPendingRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientPendingRequests.setDescription('The number of RADIUS Accounting-Request packets sent to this server that have not yet timed out or received a response. This variable is incremented when an Accounting-Request is sent and decremented due to receipt of an Accounting-Response, a timeout or a retransmission.')
rsRadiusAcctClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientTimeouts.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientTimeouts.setDescription('The number of accounting timeouts to this server. After a timeout the client may retry to the same server, send to a different server, or give up. A retry to the same server is counted as a retransmit as well as a timeout. A send to a different server is counted as an Accounting-Request as well as a timeout.')
rsRadiusAcctClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientUnknownTypes.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientUnknownTypes.setDescription('The number of RADIUS packets of unknown type which were received from this server on the accounting port.')
rsRadiusAcctClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientPacketsDropped.setDescription('The number of RADIUS packets which were received from this server on the accounting port and dropped for some other reason.')
rsRadiusAcctClientCfgServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3), )
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerTable.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerTable.setDescription('The (conceptual) table listing the RADIUS accounting servers with which the client shares a secret.')
rsRadiusAcctClientCfgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerEntry.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerEntry.setDescription('An entry (conceptual row) representing a RADIUS accounting server with which the client shares a secret.')
rsRadiusAcctClientCfgServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerAddress.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerAddress.setDescription('The IP address of the RADIUS accounting server referred to in this table entry.')
rsRadiusAcctClientCfgServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerPortNumber.setDescription('The UDP port the client is using to send requests to this server. Default is 1813.')
rsRadiusAcctClientCfgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgKey.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgKey.setDescription('The secret (RADIUS authenticator) used by the client during exchanges with this accounting server. The default is a zero-length string, indicating no authenticator is used.')
rsRadiusAcctClientCfgTimeoutInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgTimeoutInterval.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgTimeoutInterval.setDescription('The interval between retransmissions of a request to this accounting server. The default is 3.')
rsRadiusAcctClientCfgRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRetries.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRetries.setDescription('The maximum number of times to resend a request to this accounting server (in addition to the original request), before resorting to the server specified in the next entry. The default is 3.')
rsRadiusAcctClientCfgMaxPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgMaxPendingRequests.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgMaxPendingRequests.setDescription('The maximum number of outstanding requests this server can support. The default is 255.')
rsRadiusAcctClientCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRowStatus.setDescription("Supports 'createAndGo' and 'destroy' only.")
rsRadiusAcctClientCfgPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgPrecedence.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgPrecedence.setDescription('Relative precedence of this server with respect to other servers configured in this table. Lower values correspond to higher precedence. Precedence is assigned by the device, in order of entry creation, from higher to lower precedence.')
rsRadiusAcctClientCfgDeadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgDeadTime.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCfgDeadTime.setDescription('The period of time, in minutes, to ignore this server after a request to the server times out (thereby avoiding additional request timeouts for this period, if the server failure persists).')
rsRadiusClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2))
rsRadiusClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1))
rsRadiusClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2))
rsRadiusAuthClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 1)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusGeneralClientGroup"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAuthClientCompliance = rsRadiusAuthClientCompliance.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientCompliance.setDescription('The compliance statement for authentication clients implementing the Redstone RADIUS Client MIB authentication functionality.')
rsRadiusAcctClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 2)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusGeneralClientGroup"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAcctClientCompliance = rsRadiusAcctClientCompliance.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientCompliance.setDescription('The compliance statement for accounting clients implementing the Redstone RADIUS Client MIB accounting functionality.')
rsRadiusGeneralClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 1)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientIdentifier"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientAlgorithm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusGeneralClientGroup = rsRadiusGeneralClientGroup.setStatus('current')
if mibBuilder.loadTexts: rsRadiusGeneralClientGroup.setDescription('The basic collection of objects providing management of RADIUS Clients.')
rsRadiusAuthClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 2)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientInvalidServerAddresses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientRoundTripTime"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRetransmissions"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessAccepts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRejects"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessChallenges"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientMalformedAccessResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientBadAuthenticators"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientTimeouts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientUnknownTypes"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPacketsDropped"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgKey"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgTimeoutInterval"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRetries"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgMaxPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRowStatus"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgPrecedence"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgDeadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAuthClientGroup = rsRadiusAuthClientGroup.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAuthClientGroup.setDescription('The basic collection of objects providing management of RADIUS Authentication Clients.')
rsRadiusAcctClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 3)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientInvalidServerAddresses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRoundTripTime"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRetransmissions"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientMalformedResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientBadAuthenticators"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientTimeouts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientUnknownTypes"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPacketsDropped"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgKey"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgTimeoutInterval"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRetries"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgMaxPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRowStatus"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgPrecedence"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgDeadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAcctClientGroup = rsRadiusAcctClientGroup.setStatus('current')
if mibBuilder.loadTexts: rsRadiusAcctClientGroup.setDescription('The basic collection of objects providing management of RADIUS Accounting Clients.')
mibBuilder.exportSymbols("REDSTONE-RADIUS-CLIENT-MIB", rsRadiusAcctClientCfgTimeoutInterval=rsRadiusAcctClientCfgTimeoutInterval, rsRadiusClientMIBConformance=rsRadiusClientMIBConformance, rsRadiusAcctClientMalformedResponses=rsRadiusAcctClientMalformedResponses, rsRadiusAcctClientUnknownTypes=rsRadiusAcctClientUnknownTypes, rsRadiusAuthClientServerAddress=rsRadiusAuthClientServerAddress, rsRadiusAcctClientCfgKey=rsRadiusAcctClientCfgKey, rsRadiusAuthClientCfgDeadTime=rsRadiusAuthClientCfgDeadTime, rsRadiusClientAlgorithm=rsRadiusClientAlgorithm, rsRadiusAuthClientPacketsDropped=rsRadiusAuthClientPacketsDropped, rsRadiusGeneralClientGroup=rsRadiusGeneralClientGroup, rsRadiusAuthClientTimeouts=rsRadiusAuthClientTimeouts, rsRadiusAcctClientCfgServerPortNumber=rsRadiusAcctClientCfgServerPortNumber, rsRadiusAuthClientCfgRowStatus=rsRadiusAuthClientCfgRowStatus, rsRadiusAuthClientServerTable=rsRadiusAuthClientServerTable, rsRadiusAuthClientAccessChallenges=rsRadiusAuthClientAccessChallenges, rsRadiusAcctClientServerTable=rsRadiusAcctClientServerTable, rsRadiusClientMIBCompliances=rsRadiusClientMIBCompliances, rsRadiusAuthClient=rsRadiusAuthClient, rsRadiusAuthClientServerEntry=rsRadiusAuthClientServerEntry, rsRadiusAuthClientInvalidServerAddresses=rsRadiusAuthClientInvalidServerAddresses, rsRadiusAuthClientCfgRetries=rsRadiusAuthClientCfgRetries, rsRadiusAuthClientCompliance=rsRadiusAuthClientCompliance, rsRadiusAcctClientCfgMaxPendingRequests=rsRadiusAcctClientCfgMaxPendingRequests, rsRadiusAcctClientCfgRetries=rsRadiusAcctClientCfgRetries, rsRadiusClientObjects=rsRadiusClientObjects, rsRadiusAcctClientCfgPrecedence=rsRadiusAcctClientCfgPrecedence, rsRadiusClientMIBGroups=rsRadiusClientMIBGroups, rsRadiusAuthClientUnknownTypes=rsRadiusAuthClientUnknownTypes, rsRadiusAuthClientGroup=rsRadiusAuthClientGroup, rsRadiusAcctClientResponses=rsRadiusAcctClientResponses, rsRadiusAcctClient=rsRadiusAcctClient, rsRadiusAcctClientPacketsDropped=rsRadiusAcctClientPacketsDropped, rsRadiusAcctClientServerAddress=rsRadiusAcctClientServerAddress, rsRadiusAuthClientCfgMaxPendingRequests=rsRadiusAuthClientCfgMaxPendingRequests, rsRadiusAuthClientCfgTimeoutInterval=rsRadiusAuthClientCfgTimeoutInterval, rsRadiusAuthClientBadAuthenticators=rsRadiusAuthClientBadAuthenticators, rsRadiusAcctClientCompliance=rsRadiusAcctClientCompliance, rsRadiusAcctClientCfgRowStatus=rsRadiusAcctClientCfgRowStatus, PYSNMP_MODULE_ID=rsRadiusClientMIB, rsRadiusAuthClientAccessAccepts=rsRadiusAuthClientAccessAccepts, rsRadiusAuthClientCfgServerPortNumber=rsRadiusAuthClientCfgServerPortNumber, rsRadiusAcctClientTimeouts=rsRadiusAcctClientTimeouts, rsRadiusAuthClientAccessRequests=rsRadiusAuthClientAccessRequests, rsRadiusGeneralClient=rsRadiusGeneralClient, rsRadiusAcctClientRetransmissions=rsRadiusAcctClientRetransmissions, rsRadiusAcctClientCfgDeadTime=rsRadiusAcctClientCfgDeadTime, rsRadiusAcctClientInvalidServerAddresses=rsRadiusAcctClientInvalidServerAddresses, rsRadiusAcctClientCfgServerEntry=rsRadiusAcctClientCfgServerEntry, rsRadiusAcctClientPendingRequests=rsRadiusAcctClientPendingRequests, rsRadiusAuthClientCfgServerAddress=rsRadiusAuthClientCfgServerAddress, rsRadiusAuthClientRoundTripTime=rsRadiusAuthClientRoundTripTime, rsRadiusAuthClientAccessRetransmissions=rsRadiusAuthClientAccessRetransmissions, rsRadiusClientIdentifier=rsRadiusClientIdentifier, rsRadiusAuthClientCfgServerEntry=rsRadiusAuthClientCfgServerEntry, rsRadiusAcctClientServerEntry=rsRadiusAcctClientServerEntry, rsRadiusAcctClientServerPortNumber=rsRadiusAcctClientServerPortNumber, rsRadiusAuthClientAccessRejects=rsRadiusAuthClientAccessRejects, rsRadiusAcctClientRoundTripTime=rsRadiusAcctClientRoundTripTime, rsRadiusAuthClientPendingRequests=rsRadiusAuthClientPendingRequests, rsRadiusAcctClientGroup=rsRadiusAcctClientGroup, rsRadiusAuthClientMalformedAccessResponses=rsRadiusAuthClientMalformedAccessResponses, rsRadiusAcctClientCfgServerAddress=rsRadiusAcctClientCfgServerAddress, rsRadiusAuthClientServerPortNumber=rsRadiusAuthClientServerPortNumber, rsRadiusAcctClientCfgServerTable=rsRadiusAcctClientCfgServerTable, rsRadiusAcctClientRequests=rsRadiusAcctClientRequests, rsRadiusClientMIB=rsRadiusClientMIB, rsRadiusAuthClientCfgKey=rsRadiusAuthClientCfgKey, rsRadiusAuthClientCfgPrecedence=rsRadiusAuthClientCfgPrecedence, rsRadiusAcctClientBadAuthenticators=rsRadiusAcctClientBadAuthenticators, rsRadiusAuthClientCfgServerTable=rsRadiusAuthClientCfgServerTable)
