#
# PySNMP MIB module CTRON-SFPS-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:31:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
vlanTestAPI, vlanAMRStats, vlanName, vlanAMRSubnets, vlanSystem, vlanPort, vlanAMRRules, vlanCountAPI, vlanAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "vlanTestAPI", "vlanAMRStats", "vlanName", "vlanAMRSubnets", "vlanSystem", "vlanPort", "vlanAMRRules", "vlanCountAPI", "vlanAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, Gauge32, TimeTicks, Unsigned32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Counter32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Gauge32", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Counter32", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class VlanSwitchInstance(Integer32):
    pass

class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class HexInteger(Integer32):
    pass

class SfpsSwitchPort(Integer32):
    pass

sfpsVAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("add-vlan", 2), ("delete-vlan", 3), ("enable-vlan", 4), ("disable-vlan", 5), ("map-port", 6), ("unmap-port", 7), ("enable-port", 8), ("disable-port", 9), ("map-user", 10), ("unmap-user", 11), ("tap-vlan", 12), ("untap-vlan", 13), ("auto-register", 14), ("auto-unregister", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIVerb.setDescription('Specifies the action to be initiated as a result of setting this leaf.')
sfpsVAPIInPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 2), SfpsSwitchPort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIInPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIInPort.setDescription('Specifies the ingress port of the Virtual LAN if mapping a connection. Specifies the source port of a user when mapping a user')
sfpsVAPIVlanName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIVlanName.setDescription('Specifies the Virtual LAN ID.')
sfpsVAPIOutPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 4), SfpsSwitchPort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIOutPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIOutPort.setDescription('Specifies the egress port of the Virtual LAN if mapping a connection.')
sfpsVAPIUserMAC = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 5), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserMAC.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIUserMAC.setDescription("Specifies the actual user's MAC value for the action.")
sfpsVAPIUserAliasTag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("aoMacDx", 1), ("aoIpxSap", 2), ("aoIpxRIP", 3), ("aoInetYP", 4), ("aoInetUDP", 5), ("aoIpxIpx", 6), ("aoInetIP", 7), ("aoInetRPC", 8), ("aoInetRIP", 9), ("aoMacDXMcast", 10), ("aoAtDDP", 11), ("aoEmpty", 12), ("aoVlan", 13), ("aoHostName", 14), ("aoNetBiosName", 15), ("aoInetIPMask", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserAliasTag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIUserAliasTag.setDescription('Indicates the Alias Value of the user. Not yet supported.')
sfpsVAPIUserAlias = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUserAlias.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIUserAlias.setDescription('Indicates the Alias Value of the user.')
sfpsVAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIAdminStatus.setDescription('Sets the administrative state of the object.')
sfpsVAPIAutoRegisterRule = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("ether-type", 2), ("ip-subnet", 3), ("netBIOS", 4), ("ipx-Server", 5), ("appleTalk", 6), ("decNET", 7), ("vines", 8), ("bpdu", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegisterRule.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIAutoRegisterRule.setDescription('Specifies the AMR rule in which to perform the action on.')
sfpsVAPIAutoRegMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIAutoRegMask.setDescription('Indicates the mask to apply when the IP-Subnet rule is invoked.')
sfpsVAPIAutoRegValue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIAutoRegValue.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIAutoRegValue.setDescription('Indicates the Alias Value of the user.')
sfpsVAPIUnicastPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3))).clone('open')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIUnicastPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIUnicastPolicy.setDescription('Sets the vlan policy type.')
sfpsVAPIPortPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("locked", 3))).clone('locked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIPortPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIPortPolicy.setDescription('Sets the port mode type.')
sfpsVAPIFloodPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("flooding-on", 2), ("flooding-off", 3))).clone('flooding-on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIFloodPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIFloodPolicy.setDescription('Sets the flood mode type.')
sfpsVAPIRouterPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIRouterPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIRouterPort.setDescription('Sets router port')
sfpsVAPIVlanId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIVlanId.setDescription('Indicates the Vlan Id.')
sfpsVAPINvramId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPINvramId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPINvramId.setDescription('Indicates the Nvram Id')
sfpsVAPIRelayAgent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPIRelayAgent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPIRelayAgent.setDescription('Indicates the Relay Agent.')
sfpsVAPILayer3Learning = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("learning-enabled", 2), ("learning-disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsVAPILayer3Learning.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsVAPILayer3Learning.setDescription('Indicates layer 3 learning enabled/disabled')
vlanNameTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1), )
if mibBuilder.loadTexts: vlanNameTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameTable.setDescription('This table contains information of each SFVlan instance. Essentially, a separate SFVlan instance exists for each Vlan. If SFVlan is not configured on a module, than an entry will not exist.')
vlanNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanNameNHash"), (0, "CTRON-SFPS-VLAN-MIB", "vlanNameIndex"))
if mibBuilder.loadTexts: vlanNameEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameEntry.setDescription('Each entry specifies the configuration for the Vlan instance.')
vlanNameNHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameNHash.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameNHash.setDescription('The primary index to the VlanName table.')
vlanNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameIndex.setDescription('The secondary index to the VlanName table.')
vlanNameVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameVlanName.setDescription('The Virual LAN ID.')
vlanNameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameAdminStatus.setDescription('The administrative state of the Vlan.')
vlanNameOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("shutdown-pending", 4), ("startup-pending", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameOperStatus.setDescription('The operational state of the Vlan.')
vlanNameUniPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameUniPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameUniPolicy.setDescription('The communication policy with respect to other Vlans.')
vlanNameFloodPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 2))).clone(namedValues=NamedValues(("other", 1), ("flood-on", 3), ("flood-off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameFloodPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameFloodPolicy.setDescription('The multicast and unknown destination flood policy.')
vlanNameStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameStatusTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameStatusTime.setDescription('The amount of time that this Vlan has been in its current operational state.')
vlanNameNumUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameNumUsers.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameNumUsers.setDescription('The number of users per port')
vlanNameEnabledPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameEnabledPorts.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameEnabledPorts.setDescription('The list of ports which have are enabled for this Vlan.')
vlanNameMappedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameMappedPorts.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameMappedPorts.setDescription('The list of ports which have this Vlan mapped to it.')
vlanNameVlanRule = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanRule.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameVlanRule.setDescription('.')
vlanNameFloodPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameFloodPorts.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameFloodPorts.setDescription('')
vlanNameVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameVlanId.setDescription('')
vlanNameRelayAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameRelayAgent.setStatus('mandatory')
if mibBuilder.loadTexts: vlanNameRelayAgent.setDescription('')
vlanSystemTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1), )
if mibBuilder.loadTexts: vlanSystemTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemTable.setDescription('This table contains the configuration and administrative information of each SFVlan switch instance. Essentially, a separate SFVlan switch instance exists for each switch module. If SFVlan is not configured on a module, than an entry will not exist.')
vlanSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanSystemSwitchInstance"))
if mibBuilder.loadTexts: vlanSystemEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemEntry.setDescription('Each entry specifies the VLAN configuration for the VLAN instance.')
vlanSystemSwitchInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 1), VlanSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemSwitchInstance.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemSwitchInstance.setDescription('The primary index to the VLAN switch table. This identifies the VLAN switch for which the entry exists.')
vlanSystemAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemAdminStatus.setDescription('Sets the administrative state of the VLAN switching services for this VLAN instance. This controls the VLAN state at a module level. Regardless of the per-port state of each VLAN switching port and the state of active connections, writing the value disabled(2) will cause the VLAN to immediately shutdown. A gracefull shutdown will be attempted.')
vlanSystemAdminReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAdminReset.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemAdminReset.setDescription('Resets this VLAN switch instance. Writing a vlue of reset(2) will force a soft restart of the VLAN without any graceful shutdown. Any active connections or services will be interrupted.')
vlanSystemOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemOperStatus.setDescription('Indicates the current operating condition of the VLAN instance.')
vlanSystemOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemOperTime.setDescription('Indicates the amount of time (# of time ticks) that this VLAN switch instance has been in its current operational state.')
vlanSystemLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemLastChange.setDescription('Indicates the last time a change was made to the configuration entry for this VLAN switch instance.')
vlanSystemVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemVersion.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemVersion.setDescription('Indicates the current revision level of the VLAN firmware for this VLAN switch instance.')
vlanSystemMibRev = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemMibRev.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemMibRev.setDescription('Indicates in textual format the current revision level of the Cabletron VLAN MIB implemeted by the agent for this VLAN switch instance.')
vlanSystemAgentIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemAgentIP.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemAgentIP.setDescription('IP Address of VLAN Manager who owns this switch.')
vlanSystemDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSystemDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemDomainName.setDescription('Indicates domain name')
vlanSystemPollCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemPollCount.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemPollCount.setDescription('Number of polls')
vlanSystemFirstPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemFirstPollTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemFirstPollTime.setDescription('System time when first polled')
vlanSystemLastPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemLastPollTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemLastPollTime.setDescription('Last time polled')
vlanSystemPriorPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemPriorPollTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemPriorPollTime.setDescription('Poll time one before the last poll time')
vlanSystemDeltaPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSystemDeltaPollTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSystemDeltaPollTime.setDescription('Time difference between last poll time and prior poll time')
vlanTestAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("other", 1), ("add-vlan", 2), ("delete-vlan", 3), ("enable-vlan", 4), ("disable-vlan", 5), ("open-vlan", 6), ("secure-vlan", 7), ("enable-vlan-port", 8), ("disable-vlan-port", 9), ("map-vlan-port", 10), ("unmap-vlan-port", 11), ("tap-vlan-port", 12), ("untap-vlan-port", 13), ("get-vlan-info", 14), ("get-port-info", 15), ("fill-table", 16), ("empty-table", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIVerb.setDescription('Specifies the action to be initiated as a result of setting this leaf.')
vlanTestAPIVlanName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIVlanName.setDescription('Specifies the Virtual LAN to be acted upon.')
vlanTestAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIPort.setDescription('Specifies the Port to be acted upon.')
vlanTestAPIVlanId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTestAPIVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIVlanId.setDescription('Specifies the ID.')
vlanTestAPIOutputTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4), )
if mibBuilder.loadTexts: vlanTestAPIOutputTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputTable.setDescription('This table contains the output results of the VlanAPI action.')
vlanTestAPIOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanTestAPIOutputIndex"))
if mibBuilder.loadTexts: vlanTestAPIOutputEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputEntry.setDescription('Each entry specifies one output result of the VlanAPI action.')
vlanTestAPIOutputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputIndex.setDescription('The primary index to the VLAN Test API Output table.')
vlanTestAPIOutputVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputVlanName.setDescription('Specifies the Virtual LAN by name.')
vlanTestAPIOutputUserCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputUserCnt.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputUserCnt.setDescription('Specifies the number of users on this Vlan.')
vlanTestAPIOutputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputStatus.setDescription('Specifies the operational state of this Vlan.')
vlanTestAPIOutputPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputPolicy.setDescription('Specifies the uni-cast policy of this Vlan.')
vlanTestAPIOutputPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputPort.setDescription('Specifies the Vlan port.')
vlanTestAPIOutputMap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("unmapped", 2), ("mapped", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputMap.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputMap.setDescription('Specifies whether the Vlan is mapped.')
vlanTestAPIOutputAble = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputAble.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputAble.setDescription('Specifies whether the Vlan is enabled.')
vlanTestAPIOutputTap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("untapped", 2), ("tapped", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputTap.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputTap.setDescription('Specifies whether the Vlan is tapped.')
vlanTestAPIOutputVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTestAPIOutputVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: vlanTestAPIOutputVlanId.setDescription('Specifies the Vlan Id.')
vlanCountAPITotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPITotal.setStatus('mandatory')
if mibBuilder.loadTexts: vlanCountAPITotal.setDescription('')
vlanCountAPIAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPIAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: vlanCountAPIAdmin.setDescription('')
vlanCountAPIAutoreg = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanCountAPIAutoreg.setStatus('mandatory')
if mibBuilder.loadTexts: vlanCountAPIAutoreg.setDescription('')
vlanAMRRulesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1), )
if mibBuilder.loadTexts: vlanAMRRulesTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRRulesTable.setDescription('This table displays the on/off status of each individual AMR Rule.')
vlanAMRRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanAMRRulesRule"))
if mibBuilder.loadTexts: vlanAMRRulesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRRulesEntry.setDescription('')
vlanAMRRulesRule = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("etherType", 2), ("ipSubNet", 3), ("netBIOS", 4), ("ipxServer", 5), ("appleTalk", 6), ("decNET", 7), ("vines", 8), ("bpdu", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRRulesRule.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRRulesRule.setDescription('Refers to the enumerated value corresponding to each AMR rule')
vlanAMRRulesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRRulesStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRRulesStatus.setDescription('Displays whether the rule is currently on or off')
vlanAMRStatsNumRulesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRStatsNumRulesEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRStatsNumRulesEnabled.setDescription('Refers to the number of rules that are on in the AmrRules')
vlanAMRStatsSingleMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRStatsSingleMask.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRStatsSingleMask.setDescription('Displays the mask that is used with the IP-Subnet AMR rule')
vlanAMRSubnetsPrefix = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRSubnetsPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRSubnetsPrefix.setDescription('')
vlanAMRSubnetsMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanAMRSubnetsMask.setStatus('mandatory')
if mibBuilder.loadTexts: vlanAMRSubnetsMask.setDescription('')
vlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1), )
if mibBuilder.loadTexts: vlanPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortTable.setDescription('')
vlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VLAN-MIB", "vlanPortPortNum"))
if mibBuilder.loadTexts: vlanPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortEntry.setDescription('')
vlanPortPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortPortNum.setDescription('The primary index to the VlanPort table.')
vlanPortPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortPortStatus.setDescription('')
vlanPortPortPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("locked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortPortPolicy.setDescription('')
vlanPortVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortVlanName.setDescription('')
vlanPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortAdminStatus.setDescription('')
vlanPortUniPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("open", 2), ("secure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortUniPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortUniPolicy.setDescription('')
vlanPortFloodPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("floodOn", 2), ("floodOff", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortFloodPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortFloodPolicy.setDescription('')
vlanPortRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("routerPort", 2), ("noRouter", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortRouterPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortRouterPort.setDescription('')
vlanPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortVlanId.setDescription('')
vlanPortRelayAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortRelayAgent.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortRelayAgent.setDescription('')
vlanPortLayer3Learning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortLayer3Learning.setStatus('mandatory')
if mibBuilder.loadTexts: vlanPortLayer3Learning.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-VLAN-MIB", vlanTestAPIOutputPolicy=vlanTestAPIOutputPolicy, sfpsVAPIPortPolicy=sfpsVAPIPortPolicy, vlanSystemVersion=vlanSystemVersion, sfpsVAPIUserAliasTag=sfpsVAPIUserAliasTag, SfpsAddress=SfpsAddress, vlanTestAPIOutputVlanId=vlanTestAPIOutputVlanId, vlanAMRRulesTable=vlanAMRRulesTable, vlanSystemSwitchInstance=vlanSystemSwitchInstance, vlanAMRStatsNumRulesEnabled=vlanAMRStatsNumRulesEnabled, sfpsVAPIUserAlias=sfpsVAPIUserAlias, vlanCountAPIAdmin=vlanCountAPIAdmin, vlanNameEntry=vlanNameEntry, vlanTestAPIVerb=vlanTestAPIVerb, vlanTestAPIOutputUserCnt=vlanTestAPIOutputUserCnt, vlanPortVlanName=vlanPortVlanName, vlanTestAPIOutputTable=vlanTestAPIOutputTable, sfpsVAPIRouterPort=sfpsVAPIRouterPort, vlanNameStatusTime=vlanNameStatusTime, SfpsSwitchPort=SfpsSwitchPort, sfpsVAPIUnicastPolicy=sfpsVAPIUnicastPolicy, vlanPortRelayAgent=vlanPortRelayAgent, vlanCountAPITotal=vlanCountAPITotal, vlanPortUniPolicy=vlanPortUniPolicy, vlanTestAPIOutputAble=vlanTestAPIOutputAble, vlanNameMappedPorts=vlanNameMappedPorts, vlanNameTable=vlanNameTable, vlanSystemLastChange=vlanSystemLastChange, vlanNameFloodPolicy=vlanNameFloodPolicy, vlanTestAPIOutputTap=vlanTestAPIOutputTap, sfpsVAPINvramId=sfpsVAPINvramId, vlanNameUniPolicy=vlanNameUniPolicy, vlanSystemDeltaPollTime=vlanSystemDeltaPollTime, vlanSystemAgentIP=vlanSystemAgentIP, HexInteger=HexInteger, vlanPortLayer3Learning=vlanPortLayer3Learning, vlanNameAdminStatus=vlanNameAdminStatus, vlanNameNumUsers=vlanNameNumUsers, vlanAMRSubnetsPrefix=vlanAMRSubnetsPrefix, sfpsVAPIAutoRegisterRule=sfpsVAPIAutoRegisterRule, sfpsVAPIVlanName=sfpsVAPIVlanName, vlanTestAPIOutputPort=vlanTestAPIOutputPort, vlanNameIndex=vlanNameIndex, sfpsVAPIVlanId=sfpsVAPIVlanId, vlanPortPortPolicy=vlanPortPortPolicy, vlanTestAPIOutputStatus=vlanTestAPIOutputStatus, vlanPortTable=vlanPortTable, vlanTestAPIOutputIndex=vlanTestAPIOutputIndex, vlanNameVlanId=vlanNameVlanId, vlanSystemOperTime=vlanSystemOperTime, vlanSystemMibRev=vlanSystemMibRev, sfpsVAPIAdminStatus=sfpsVAPIAdminStatus, vlanSystemEntry=vlanSystemEntry, vlanSystemOperStatus=vlanSystemOperStatus, sfpsVAPIRelayAgent=sfpsVAPIRelayAgent, vlanSystemPollCount=vlanSystemPollCount, vlanNameVlanName=vlanNameVlanName, sfpsVAPIVerb=sfpsVAPIVerb, vlanPortVlanId=vlanPortVlanId, vlanNameFloodPorts=vlanNameFloodPorts, vlanAMRRulesRule=vlanAMRRulesRule, sfpsVAPIFloodPolicy=sfpsVAPIFloodPolicy, vlanNameRelayAgent=vlanNameRelayAgent, vlanTestAPIVlanId=vlanTestAPIVlanId, vlanTestAPIOutputEntry=vlanTestAPIOutputEntry, vlanCountAPIAutoreg=vlanCountAPIAutoreg, vlanSystemLastPollTime=vlanSystemLastPollTime, vlanSystemPriorPollTime=vlanSystemPriorPollTime, sfpsVAPIAutoRegMask=sfpsVAPIAutoRegMask, vlanTestAPIVlanName=vlanTestAPIVlanName, vlanPortEntry=vlanPortEntry, sfpsVAPIAutoRegValue=sfpsVAPIAutoRegValue, vlanSystemFirstPollTime=vlanSystemFirstPollTime, sfpsVAPILayer3Learning=sfpsVAPILayer3Learning, vlanNameEnabledPorts=vlanNameEnabledPorts, vlanSystemAdminStatus=vlanSystemAdminStatus, vlanAMRRulesEntry=vlanAMRRulesEntry, vlanNameNHash=vlanNameNHash, vlanPortFloodPolicy=vlanPortFloodPolicy, vlanNameVlanRule=vlanNameVlanRule, vlanTestAPIOutputVlanName=vlanTestAPIOutputVlanName, vlanAMRRulesStatus=vlanAMRRulesStatus, sfpsVAPIUserMAC=sfpsVAPIUserMAC, vlanPortPortNum=vlanPortPortNum, sfpsVAPIInPort=sfpsVAPIInPort, vlanTestAPIOutputMap=vlanTestAPIOutputMap, sfpsVAPIOutPort=sfpsVAPIOutPort, vlanAMRStatsSingleMask=vlanAMRStatsSingleMask, vlanSystemDomainName=vlanSystemDomainName, vlanSystemAdminReset=vlanSystemAdminReset, vlanPortAdminStatus=vlanPortAdminStatus, VlanSwitchInstance=VlanSwitchInstance, vlanNameOperStatus=vlanNameOperStatus, vlanSystemTable=vlanSystemTable, vlanTestAPIPort=vlanTestAPIPort, vlanAMRSubnetsMask=vlanAMRSubnetsMask, vlanPortRouterPort=vlanPortRouterPort, vlanPortPortStatus=vlanPortPortStatus)
