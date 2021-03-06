#
# PySNMP MIB module T11-FC-SP-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T11-FC-SP-AUTHENTICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
FcNameIdOrZero, fcmInstanceIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "fcmInstanceIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Counter32, MibIdentifier, NotificationType, ObjectIdentity, mib_2, Unsigned32, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity", "mib-2", "Unsigned32", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Integer32")
StorageType, TextualConvention, TimeStamp, AutonomousType, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "TimeStamp", "AutonomousType", "DisplayString", "TruthValue")
t11FamLocalSwitchWwn, = mibBuilder.importSymbols("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn")
T11FcSpLifetimeLeft, T11FcSpHashFunctions, T11FcSpLifetimeLeftUnits, T11FcSpDhGroups, T11FcSpSignFunctions, T11FcSpAuthRejectReasonCode, T11FcSpAuthRejReasonCodeExp = mibBuilder.importSymbols("T11-FC-SP-TC-MIB", "T11FcSpLifetimeLeft", "T11FcSpHashFunctions", "T11FcSpLifetimeLeftUnits", "T11FcSpDhGroups", "T11FcSpSignFunctions", "T11FcSpAuthRejectReasonCode", "T11FcSpAuthRejReasonCodeExp")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcSpAuthenticationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 176))
t11FcSpAuthenticationMIB.setRevisions(('2008-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcSpAuthenticationMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 5324.',))
if mibBuilder.loadTexts: t11FcSpAuthenticationMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: t11FcSpAuthenticationMIB.setOrganization('This MIB module was developed through the coordinated effort of two organizations: T11 began the development and the IETF (in the IMSS Working Group) finished it.')
if mibBuilder.loadTexts: t11FcSpAuthenticationMIB.setContactInfo(' Claudio DeSanti Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA EMail: cds@cisco.com Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcSpAuthenticationMIB.setDescription("This MIB module specifies the management information required to manage the Authentication Protocols defined by Fibre Channel's FC-SP specification. This MIB module defines three tables: - t11FcSpAuEntityTable is a table of Fibre Channel entities that can be authenticated using FC-SP's Authentication Protocols. - t11FcSpAuIfStatTable is a table with one row for each mapping of an Authentication entity onto an interface, containing statistics information. - t11FcSpAuRejectTable is a table of volatile information about FC-SP Authentication Protocol transactions that were most recently rejected. Copyright (C) The IETF Trust (2008). This version of this MIB module is part of RFC 5324; see the RFC itself for full legal notices.")
t11FcSpAuMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 0))
t11FcSpAuMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 1))
t11FcSpAuMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 2))
t11FcSpAuMIBIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 3))
t11FcSpAuServerProtocolRadius = ObjectIdentity((1, 3, 6, 1, 2, 1, 176, 3, 1))
if mibBuilder.loadTexts: t11FcSpAuServerProtocolRadius.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolRadius.setDescription('This OID identifies RADIUS as the protocol used to communicate with an External Server as part of the process by which identities are verified. In this case, information about the RADIUS Servers is likely to be provided in radiusAuthServerExtTable defined in the RADIUS-AUTH-CLIENT-MIB.')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolRadius.setReference("radiusAuthServerExtTable in 'RADIUS Authentication Client MIB', RFC 4668, August 2006.")
t11FcSpAuServerProtocolDiameter = ObjectIdentity((1, 3, 6, 1, 2, 1, 176, 3, 2))
if mibBuilder.loadTexts: t11FcSpAuServerProtocolDiameter.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolDiameter.setDescription('This OID identifies Diameter as the protocol used to communicate with an External Server as part of the process by which identities are verified.')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolDiameter.setReference('RFC 3588, September 2003.')
t11FcSpAuServerProtocolTacacs = ObjectIdentity((1, 3, 6, 1, 2, 1, 176, 3, 3))
if mibBuilder.loadTexts: t11FcSpAuServerProtocolTacacs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolTacacs.setDescription('This OID identifies TACACS as the protocol used to communicate with an External Server as part of the process by which identities are verified.')
if mibBuilder.loadTexts: t11FcSpAuServerProtocolTacacs.setReference('RFC 1492, July 1993.')
t11FcSpAuEntityTable = MibTable((1, 3, 6, 1, 2, 1, 176, 1, 1), )
if mibBuilder.loadTexts: t11FcSpAuEntityTable.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 3.2.25.')
if mibBuilder.loadTexts: t11FcSpAuEntityTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuEntityTable.setDescription("A table of Fibre Channel entities that can be authenticated using FC-SP's Authentication Protocols. The purpose of an FC-SP Authentication Protocol is to verify that a claimed name is associated with the claiming entity. The Authentication Protocols can be used to authenticate Nx_Ports, B_Ports, or Switches.")
t11FcSpAuEntityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 176, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFabricIndex"))
if mibBuilder.loadTexts: t11FcSpAuEntityEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuEntityEntry.setDescription("Information about the configuration and capabilities of an FC-SP entity (which is managed within the Fibre Channel management instance identified by fcmInstanceIndex) on a particular Fabric with respect to FC-SP's Authentication Protocols.")
t11FcSpAuEntityName = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: t11FcSpAuEntityName.setReference("- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.3.3. - fcmInstanceWwn & fcmSwitchWWN, 'Fibre Channel Management MIB', RFC 4044, May 2005.")
if mibBuilder.loadTexts: t11FcSpAuEntityName.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuEntityName.setDescription("The name used to identify the FC-SP entity. For entities that are Fibre Channel Switches, this value corresponds to the Switch's value of fcmSwitchWWN. For entities other than Fibre Channel Switches, this value corresponds to the value of fcmInstanceWwn for the corresponding Fibre Channel management instance.")
t11FcSpAuFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: t11FcSpAuFabricIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFabricIndex.setDescription('An index value that uniquely identifies a particular Fabric to which the entity is attached.')
t11FcSpAuServerProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuServerProtocol.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuServerProtocol.setDescription('The protocol, if any, used by the entity to communicate with a third party (i.e., an External Server) as part of the process by which it verifies DH-CHAP responses. For example, if the entity is using an external RADIUS server to verify DH-CHAP responses, then this object will have the value t11FcSpAuServerProtocolRadius. The value, zeroDotZero, is used to indicate that no protocol is being used to communicate with a third party to verify DH-CHAP responses. When no protocol is being used, or if the third party is unreachable via the specified protocol, then locally configured information (if any) may be used instead.')
t11FcSpAuStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 4), StorageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuStorageType.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuStorageType.setDescription("This object specifies the memory realization of configuration information related to an FC-SP Entity on a particular Fabric: specifically, for MIB objects in the row containing this object. Even if an instance of this object has the value 'permanent(4)', none of the information in the corresponding row of this table needs to be writable.")
t11FcSpAuSendRejNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuSendRejNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuSendRejNotifyEnable.setDescription("An indication of whether or not the entity should issue t11FcSpAuRejectSentNotify notifications when sending AUTH_Reject/SW_RJT/LS_RJT to reject an AUTH message. If the value of the object is 'true', then this type of notification is generated. If the value is 'false', this type of notification is not generated.")
t11FcSpAuRcvRejNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuRcvRejNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRcvRejNotifyEnable.setDescription("An indication of whether or not the entity should issue t11FcSpAuRejectReceivedNotify notifications on the receipt of AUTH_Reject/SW_RJT/LS_RJT messages. If the value of the object is 'true', then this type of notification is generated. If the value is 'false', this type of notification is not generated.")
t11FcSpAuDefaultLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 7), T11FcSpLifetimeLeft().clone(28800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuDefaultLifetime.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuDefaultLifetime.setDescription("When the value of this object is non-zero, it specifies the default value of a lifetime, specified in units given by the corresponding instance of t11FcSpAuDefaultLifetimeUnits. This default lifetime is to be used for any Security Association that has no explicitly specified value for its lifetime. An SA's lifetime is either the time interval or the number of passed bytes, after which the SA has to be terminated and (if necessary) replaced with a new SA. If this object is zero, then there is no default value for lifetime.")
t11FcSpAuDefaultLifetimeUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 8), T11FcSpLifetimeLeftUnits().clone('seconds')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuDefaultLifetimeUnits.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuDefaultLifetimeUnits.setDescription('The units in which the value of the corresponding instance of t11FcSpAuDefaultLifetime specifies a default lifetime for a Security Association that has no explicitly-specified value for its lifetime.')
t11FcSpAuRejectMaxRows = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpAuRejectMaxRows.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectMaxRows.setDescription('The maximum number of rows in the t11FcSpAuRejectTable for this entity on this Fabric. If and when an AUTH message is rejected, and the t11FcSpAuRejectTable already contains this maximum number of rows for the specific entity and Fabric, the row containing the oldest information is discarded and replaced by a row containing information about the new rejection. There will be less than this maximum number of rows in the t11FcSpAuRejectTable in exceptional circumstances, e.g., after an agent restart. In an implementation that does not support the t11FcSpAuRejectTable, this object will always be zero.')
t11FcSpAuDhChapHashFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 10), T11FcSpHashFunctions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuDhChapHashFunctions.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuDhChapHashFunctions.setDescription('The hash functions that the entity supports when using the DH-CHAP algorithm.')
t11FcSpAuDhChapDhGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 11), T11FcSpDhGroups()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuDhChapDhGroups.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuDhChapDhGroups.setDescription('The DH Groups that the entity supports when using the DH-CHAP algorithm in FC-SP.')
t11FcSpAuFcapHashFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 12), T11FcSpHashFunctions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuFcapHashFunctions.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.5.2.1 and table 28.')
if mibBuilder.loadTexts: t11FcSpAuFcapHashFunctions.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFcapHashFunctions.setDescription('The hash functions that the entity supports when specified as Protocol Parameters in the AUTH_Negotiate message for FCAP in FC-SP.')
t11FcSpAuFcapCertsSignFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 13), T11FcSpSignFunctions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuFcapCertsSignFunctions.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.5.4.2 and tables 38 & 39.')
if mibBuilder.loadTexts: t11FcSpAuFcapCertsSignFunctions.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFcapCertsSignFunctions.setDescription('The signature functions used within certificates that the entity supports when using FCAP in FC-SP.')
t11FcSpAuFcapDhGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 14), T11FcSpDhGroups()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuFcapDhGroups.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFcapDhGroups.setDescription('The DH Groups that the entity supports when using the FCAP algorithm in FC-SP.')
t11FcSpAuFcpapHashFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 15), T11FcSpHashFunctions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuFcpapHashFunctions.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFcpapHashFunctions.setDescription('The hash functions that the entity supports when using the FCPAP algorithm in FC-SP.')
t11FcSpAuFcpapDhGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 1, 1, 16), T11FcSpDhGroups()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuFcpapDhGroups.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuFcpapDhGroups.setDescription('The DH Groups that the entity supports when using the FCPAP algorithm in FC-SP.')
t11FcSpAuIfStatTable = MibTable((1, 3, 6, 1, 2, 1, 176, 1, 2), )
if mibBuilder.loadTexts: t11FcSpAuIfStatTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatTable.setDescription("Each FC-SP Authentication entity can operate on one or more interfaces, but at most one of them can operate on each interface. A row in this table exists for each interface to each Fabric on which each Authentication entity operates. The objects within this table contain statistics information related to FC-SP's Authentication Protocols.")
t11FcSpAuIfStatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 176, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInterfaceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatFabricIndex"))
if mibBuilder.loadTexts: t11FcSpAuIfStatEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatEntry.setDescription('A set of Authentication Protocols statistics for an FC-SP Authentication entity (identified by t11FcSpAuEntityName) on one of its interfaces to a particular Fabric, which is managed within the Fibre Channel management instance identified by fcmInstanceIndex.')
t11FcSpAuIfStatInterfaceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: t11FcSpAuIfStatInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatInterfaceIndex.setDescription('The interface on which the FC-SP Authentication entity operates and for which the statistics are collected.')
t11FcSpAuIfStatFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: t11FcSpAuIfStatFabricIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatFabricIndex.setDescription('An index value identifying the particular Fabric for which the statistics are collected.')
t11FcSpAuIfStatTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatTimeouts.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.11.')
if mibBuilder.loadTexts: t11FcSpAuIfStatTimeouts.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatTimeouts.setDescription("The number of FC-SP Authentication Protocol messages sent by the particular entity on the particular Fabric on the particular interface, for which no response was received within a timeout period. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatInAcceptedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatInAcceptedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatInAcceptedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatInAcceptedMsgs.setDescription("The number of FC-SP Authentication Protocol messages received and accepted by the particular entity on the particular Fabric on the particular interface. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatInLsSwRejectedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatInLsSwRejectedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatInLsSwRejectedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatInLsSwRejectedMsgs.setDescription("The number of FC-SP Authentication Protocol messages received by the particular entity on the particular Fabric on the particular interface, and rejected by a lower-level (SW_RJT or LS_RJT) reject. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatInAuthRejectedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatInAuthRejectedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatInAuthRejectedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatInAuthRejectedMsgs.setDescription("The number of FC-SP Authentication Protocol messages received by the particular entity on the particular Fabric on the particular interface, and rejected by an AUTH_Reject message. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatOutAcceptedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAcceptedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAcceptedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAcceptedMsgs.setDescription("The number of FC-SP Authentication Protocol messages sent by the particular entity on the particular Fabric on the particular interface, which were accepted by the neighboring entity, i.e., not rejected by an AUTH_Reject message, nor by a lower-level (SW_RJT or LS_RJT) reject. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatOutLsSwRejectedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatOutLsSwRejectedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutLsSwRejectedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutLsSwRejectedMsgs.setDescription("The number of FC-SP Authentication Protocol messages sent by the particular entity on the particular Fabric on the particular interface, which were rejected by a lower-level (SW_RJT or LS_RJT) reject. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuIfStatOutAuthRejectedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAuthRejectedMsgs.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 5.1.')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAuthRejectedMsgs.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatOutAuthRejectedMsgs.setDescription("The number of FC-SP Authentication Protocol messages sent by the particular entity on the particular Fabric on the particular interface, which were rejected by an AUTH_Reject message. This counter has no discontinuities other than those that all Counter32's have when sysUpTime=0.")
t11FcSpAuRejectTable = MibTable((1, 3, 6, 1, 2, 1, 176, 1, 3), )
if mibBuilder.loadTexts: t11FcSpAuRejectTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectTable.setDescription("A table of volatile information about FC-SP Authentication Protocol transactions that were recently rejected with an AUTH_Reject message, or with an SW_RJT/LS_RJT. The maximum number of rows in this table for a specific entity on a specific Fabric is given by the value of the corresponding instance of t11FcSpAuRejectMaxRows. The syntax of t11FcSpAuRejTimestamp is TimeStamp, and thus its value rolls over to zero after approximately 497 days. To avoid any confusion due to such a rollover, rows should be deleted from this table before they are 497 days old. This table will be empty if no AUTH_Reject messages, nor any SW_RJT/LS_RJT's rejecting an AUTH message, have been sent or received since the last re-initialization of the agent.")
t11FcSpAuRejectEntry = MibTableRow((1, 3, 6, 1, 2, 1, 176, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejInterfaceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejFabricIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejTimestamp"))
if mibBuilder.loadTexts: t11FcSpAuRejectEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectEntry.setDescription('Information about one AUTH message (either an AUTH_ELS or an AUTH_ILS) that was rejected with an AUTH_Reject, SW_RJT or LS_RJT message, sent/received by the entity identified by values of fcmInstanceIndex and t11FcSpAuEntityName, on an interface to a particular Fabric.')
t11FcSpAuRejInterfaceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: t11FcSpAuRejInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejInterfaceIndex.setDescription('The interface on which the rejected AUTH message was sent or received.')
t11FcSpAuRejFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: t11FcSpAuRejFabricIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejFabricIndex.setDescription('An index value identifying the particular Fabric on which the rejected AUTH message was sent or received.')
t11FcSpAuRejTimestamp = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 3), TimeStamp())
if mibBuilder.loadTexts: t11FcSpAuRejTimestamp.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejTimestamp.setDescription('The time at which the AUTH message was rejected. If two rows have the same value of this object for the same entity on the same interface and Fabric, the value of this object for the later one is incremented by one.')
t11FcSpAuRejDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sent", 1), ("received", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuRejDirection.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejDirection.setDescription("An indication of whether the rejection was sent or received by the identified entity. The value 'sent(1)' corresponds to a notification of type t11FcSpAuRejectSentNotify; the value 'received(2)' corresponds to t11FcSpAuRejectReceivedNotify.")
t11FcSpAuRejType = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authReject", 1), ("swRjt", 2), ("lsRjt", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuRejType.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejType.setDescription('An indication of whether the rejection was an AUTH_Reject, an SW_RJT or an LS_RJT.')
t11FcSpAuRejAuthMsgString = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuRejAuthMsgString.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Tables 3, 5 and 6.')
if mibBuilder.loadTexts: t11FcSpAuRejAuthMsgString.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejAuthMsgString.setDescription("The binary content of the AUTH message that was rejected, formatted as an octet string (in network byte order) containing the content of the message. If the binary content is unavailable, then the length is zero. Otherwise, the first octet of the message identifies the type of message: '90'h - an AUTH_ELS, see Table 6 in FC-SP, '40'h - an AUTH_ILS, see Table 3 in FC-SP, or '41'h - an B_AUTH_ILS, see Table 5 in FC-SP. and the remainder of the message may be truncated.")
t11FcSpAuRejReasonCode = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 7), T11FcSpAuthRejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuRejReasonCode.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 17, 48, 52.')
if mibBuilder.loadTexts: t11FcSpAuRejReasonCode.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejReasonCode.setDescription('The reason code with which this AUTH message was rejected.')
t11FcSpAuRejReasonCodeExp = MibTableColumn((1, 3, 6, 1, 2, 1, 176, 1, 3, 1, 8), T11FcSpAuthRejReasonCodeExp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpAuRejReasonCodeExp.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 17, 48, 52.')
if mibBuilder.loadTexts: t11FcSpAuRejReasonCodeExp.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejReasonCodeExp.setDescription('The reason code explanation with which this AUTH message was rejected.')
t11FcSpAuRejectSentNotify = NotificationType((1, 3, 6, 1, 2, 1, 176, 0, 1)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
if mibBuilder.loadTexts: t11FcSpAuRejectSentNotify.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectSentNotify.setDescription('This notification indicates that a Switch (identified by the value of t11FamLocalSwitchWwn) has sent a reject message of the type indicated by t11FcSpAuRejType in response to an AUTH message. The content of the rejected AUTH message is given by the value of t11FcSpAuRejAuthMsgString. The values of the Reason Code and Reason Code Explanation in the AUTH_Reject/SW_RJT/LS_RJT are indicated by the values of t11FcSpAuRejReasonCode and t11FcSpAuRejReasonCodeExp.')
t11FcSpAuRejectReceivedNotify = NotificationType((1, 3, 6, 1, 2, 1, 176, 0, 2)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
if mibBuilder.loadTexts: t11FcSpAuRejectReceivedNotify.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectReceivedNotify.setDescription('This notification indicates that a Switch (identified by the value of t11FamLocalSwitchWwn) has received a reject message of the type indicated by t11FcSpAuRejType in response to an AUTH message. The content of the rejected AUTH message is given by the value of t11FcSpAuRejAuthMsgString. The values of the Reason Code and Reason Code Explanation in the AUTH_Reject/SW_RJT/LS_RJT are indicated by the values of t11FcSpAuRejReasonCode and t11FcSpAuRejReasonCodeExp.')
t11FcSpAuMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 2, 1))
t11FcSpAuMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 176, 2, 2))
t11FcSpAuMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 176, 2, 1, 1)).setObjects(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuGeneralGroup"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectedGroup"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuNotificationGroup"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpAuMIBCompliance = t11FcSpAuMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuMIBCompliance.setDescription('The compliance statement for entities that implement one or more of the Authentication Protocols defined in FC-SP.')
t11FcSpAuGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 176, 2, 2, 1)).setObjects(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuServerProtocol"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuStorageType"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuSendRejNotifyEnable"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRcvRejNotifyEnable"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDefaultLifetime"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDefaultLifetimeUnits"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectMaxRows"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDhChapHashFunctions"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuDhChapDhGroups"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapHashFunctions"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapCertsSignFunctions"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcapDhGroups"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcpapHashFunctions"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuFcpapDhGroups"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatTimeouts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpAuGeneralGroup = t11FcSpAuGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuGeneralGroup.setDescription("A collection of objects for the capabilities and configuration parameters of FC-SP's Authentication Protocols. The inclusion of t11FcSpAuIfStatTimeouts in this group provides information on mappings of Authentication entities onto interfaces.")
t11FcSpAuIfStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 176, 2, 2, 2)).setObjects(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInAcceptedMsgs"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInLsSwRejectedMsgs"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatInAuthRejectedMsgs"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutAcceptedMsgs"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutLsSwRejectedMsgs"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuIfStatOutAuthRejectedMsgs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpAuIfStatsGroup = t11FcSpAuIfStatsGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuIfStatsGroup.setDescription("A collection of objects for monitoring the operations of FC-SP's Authentication Protocols.")
t11FcSpAuRejectedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 176, 2, 2, 3)).setObjects(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejDirection"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejType"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejAuthMsgString"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCode"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejReasonCodeExp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpAuRejectedGroup = t11FcSpAuRejectedGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuRejectedGroup.setDescription('A collection of objects holding information concerning FC-SP Authentication Protocol transactions that were recently rejected with an AUTH_Reject, with an SW_RJT, or with an LS_RJT.')
t11FcSpAuNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 176, 2, 2, 4)).setObjects(("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectSentNotify"), ("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuRejectReceivedNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpAuNotificationGroup = t11FcSpAuNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuNotificationGroup.setDescription("A collection of notifications for use in the management of FC-SP's Authentication Protocols.")
mibBuilder.exportSymbols("T11-FC-SP-AUTHENTICATION-MIB", t11FcSpAuRejInterfaceIndex=t11FcSpAuRejInterfaceIndex, t11FcSpAuFcpapHashFunctions=t11FcSpAuFcpapHashFunctions, t11FcSpAuServerProtocolDiameter=t11FcSpAuServerProtocolDiameter, t11FcSpAuRejReasonCodeExp=t11FcSpAuRejReasonCodeExp, t11FcSpAuIfStatEntry=t11FcSpAuIfStatEntry, t11FcSpAuIfStatFabricIndex=t11FcSpAuIfStatFabricIndex, t11FcSpAuRejectMaxRows=t11FcSpAuRejectMaxRows, t11FcSpAuFcapHashFunctions=t11FcSpAuFcapHashFunctions, t11FcSpAuMIBCompliance=t11FcSpAuMIBCompliance, t11FcSpAuNotificationGroup=t11FcSpAuNotificationGroup, t11FcSpAuRejectSentNotify=t11FcSpAuRejectSentNotify, t11FcSpAuDhChapDhGroups=t11FcSpAuDhChapDhGroups, t11FcSpAuRcvRejNotifyEnable=t11FcSpAuRcvRejNotifyEnable, t11FcSpAuFcapCertsSignFunctions=t11FcSpAuFcapCertsSignFunctions, t11FcSpAuMIBConformance=t11FcSpAuMIBConformance, t11FcSpAuIfStatTimeouts=t11FcSpAuIfStatTimeouts, t11FcSpAuMIBCompliances=t11FcSpAuMIBCompliances, t11FcSpAuGeneralGroup=t11FcSpAuGeneralGroup, t11FcSpAuServerProtocolRadius=t11FcSpAuServerProtocolRadius, t11FcSpAuDefaultLifetimeUnits=t11FcSpAuDefaultLifetimeUnits, t11FcSpAuRejDirection=t11FcSpAuRejDirection, t11FcSpAuEntityName=t11FcSpAuEntityName, t11FcSpAuIfStatInLsSwRejectedMsgs=t11FcSpAuIfStatInLsSwRejectedMsgs, t11FcSpAuRejFabricIndex=t11FcSpAuRejFabricIndex, t11FcSpAuIfStatInAcceptedMsgs=t11FcSpAuIfStatInAcceptedMsgs, t11FcSpAuMIBIdentities=t11FcSpAuMIBIdentities, t11FcSpAuEntityTable=t11FcSpAuEntityTable, t11FcSpAuFabricIndex=t11FcSpAuFabricIndex, t11FcSpAuIfStatOutAcceptedMsgs=t11FcSpAuIfStatOutAcceptedMsgs, t11FcSpAuMIBGroups=t11FcSpAuMIBGroups, t11FcSpAuMIBObjects=t11FcSpAuMIBObjects, t11FcSpAuRejReasonCode=t11FcSpAuRejReasonCode, t11FcSpAuDhChapHashFunctions=t11FcSpAuDhChapHashFunctions, t11FcSpAuFcapDhGroups=t11FcSpAuFcapDhGroups, t11FcSpAuFcpapDhGroups=t11FcSpAuFcpapDhGroups, t11FcSpAuthenticationMIB=t11FcSpAuthenticationMIB, t11FcSpAuIfStatInterfaceIndex=t11FcSpAuIfStatInterfaceIndex, t11FcSpAuRejectEntry=t11FcSpAuRejectEntry, t11FcSpAuStorageType=t11FcSpAuStorageType, t11FcSpAuRejTimestamp=t11FcSpAuRejTimestamp, t11FcSpAuRejAuthMsgString=t11FcSpAuRejAuthMsgString, PYSNMP_MODULE_ID=t11FcSpAuthenticationMIB, t11FcSpAuRejectTable=t11FcSpAuRejectTable, t11FcSpAuRejType=t11FcSpAuRejType, t11FcSpAuServerProtocolTacacs=t11FcSpAuServerProtocolTacacs, t11FcSpAuIfStatOutLsSwRejectedMsgs=t11FcSpAuIfStatOutLsSwRejectedMsgs, t11FcSpAuServerProtocol=t11FcSpAuServerProtocol, t11FcSpAuSendRejNotifyEnable=t11FcSpAuSendRejNotifyEnable, t11FcSpAuIfStatTable=t11FcSpAuIfStatTable, t11FcSpAuDefaultLifetime=t11FcSpAuDefaultLifetime, t11FcSpAuMIBNotifications=t11FcSpAuMIBNotifications, t11FcSpAuIfStatInAuthRejectedMsgs=t11FcSpAuIfStatInAuthRejectedMsgs, t11FcSpAuRejectReceivedNotify=t11FcSpAuRejectReceivedNotify, t11FcSpAuEntityEntry=t11FcSpAuEntityEntry, t11FcSpAuIfStatsGroup=t11FcSpAuIfStatsGroup, t11FcSpAuRejectedGroup=t11FcSpAuRejectedGroup, t11FcSpAuIfStatOutAuthRejectedMsgs=t11FcSpAuIfStatOutAuthRejectedMsgs)
