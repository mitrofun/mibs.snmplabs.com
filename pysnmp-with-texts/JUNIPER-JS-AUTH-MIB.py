#
# PySNMP MIB module JUNIPER-JS-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-AUTH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
jnxJsAuth, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsAuth")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, IpAddress, iso, Integer32, MibIdentifier, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "IpAddress", "iso", "Integer32", "MibIdentifier", "Counter32", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxJsAuthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1))
jnxJsAuthMIB.setRevisions(('2007-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJsAuthMIB.setRevisionsDescriptions(('Creation Date',))
if mibBuilder.loadTexts: jnxJsAuthMIB.setLastUpdated('200705142022Z')
if mibBuilder.loadTexts: jnxJsAuthMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsAuthMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxJsAuthMIB.setDescription('Firewall and security features restrict the accessing of protected resources (ideally on different zones) behind a firewall based on their source ip and other credentials. This module defines the objects pertain to access authentication.')
jnxJsAuthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0))
jnxJsAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1))
jnxJsFwAuthStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1))
jnxJsAuthTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2))
jnxJsFwAuthNumPendingUsers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsFwAuthNumPendingUsers.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthNumPendingUsers.setDescription('Number of users currently waiting to be authenticated by the firewall user authentication mechanism.')
jnxJsFwAuthNumSuccUsers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsFwAuthNumSuccUsers.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthNumSuccUsers.setDescription('Number of users currently allowed access by the firewall user authentication mechanism.')
jnxJsFwAuthNumFailedUsers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsFwAuthNumFailedUsers.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthNumFailedUsers.setDescription('Number of users currently failed to be authenticated by the firewall user authentication mechanism.')
jnxJsFwAuthTotalUsers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsFwAuthTotalUsers.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthTotalUsers.setDescription('Total number of users that are accessing or attempting to access resources managed by the firewall user authentication mechanism.')
jnxJsFwAuthUserName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsFwAuthUserName.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthUserName.setDescription('The name of the user who is attempting or has been authenticated.')
jnxJsFwAuthServiceDesc = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsFwAuthServiceDesc.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthServiceDesc.setDescription('The service or application name that the enthentication is performed for: telnet, ftp, http.')
jnxJsFwAuthReason = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsFwAuthReason.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthReason.setDescription('The reason for the trap being generated: authentication failure due to: timeout, invalid password, invalid username, etc.')
jnxJsFwAuthClientIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxJsFwAuthClientIpAddr.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthClientIpAddr.setDescription("The authentication client's IP Address.")
jnxJsFwAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 1)).setObjects(("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthUserName"), ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthClientIpAddr"), ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthServiceDesc"), ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthReason"))
if mibBuilder.loadTexts: jnxJsFwAuthFailure.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthFailure.setDescription('A firewall user authentication status trap signifies whether a user using the pass-through firewall authentication mechanism has been rejected due to reason specified in the trap. jnxJsFwAuthUserName is the user. jnxClientIPAddress is the ip address the user came from. jnxJsFwAuthServiceDesc specifies the application by which the authentication was performed. jnxJsFwAuthReason indicates the reason for failure.')
jnxJsFwAuthServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 2))
if mibBuilder.loadTexts: jnxJsFwAuthServiceUp.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthServiceUp.setDescription('Firewall user authentication service has started.')
jnxJsFwAuthServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 3))
if mibBuilder.loadTexts: jnxJsFwAuthServiceDown.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthServiceDown.setDescription('Firewall user authentication service has stopped.')
jnxJsFwAuthCapacityExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 4))
if mibBuilder.loadTexts: jnxJsFwAuthCapacityExceeded.setStatus('current')
if mibBuilder.loadTexts: jnxJsFwAuthCapacityExceeded.setDescription('Firewall user authentication maximum capacity has been exceeded. jnxJsFwAuthTotalUsers indicates the total number of users being authenticated. And it has exceeds the maximum allowable users. ')
mibBuilder.exportSymbols("JUNIPER-JS-AUTH-MIB", jnxJsAuthTrapVars=jnxJsAuthTrapVars, jnxJsFwAuthTotalUsers=jnxJsFwAuthTotalUsers, jnxJsFwAuthFailure=jnxJsFwAuthFailure, jnxJsFwAuthStats=jnxJsFwAuthStats, jnxJsFwAuthNumSuccUsers=jnxJsFwAuthNumSuccUsers, jnxJsFwAuthCapacityExceeded=jnxJsFwAuthCapacityExceeded, jnxJsFwAuthReason=jnxJsFwAuthReason, jnxJsFwAuthUserName=jnxJsFwAuthUserName, jnxJsFwAuthServiceDown=jnxJsFwAuthServiceDown, PYSNMP_MODULE_ID=jnxJsAuthMIB, jnxJsFwAuthServiceUp=jnxJsFwAuthServiceUp, jnxJsFwAuthNumFailedUsers=jnxJsFwAuthNumFailedUsers, jnxJsFwAuthServiceDesc=jnxJsFwAuthServiceDesc, jnxJsFwAuthClientIpAddr=jnxJsFwAuthClientIpAddr, jnxJsAuthNotifications=jnxJsAuthNotifications, jnxJsAuthObjects=jnxJsAuthObjects, jnxJsAuthMIB=jnxJsAuthMIB, jnxJsFwAuthNumPendingUsers=jnxJsFwAuthNumPendingUsers)
