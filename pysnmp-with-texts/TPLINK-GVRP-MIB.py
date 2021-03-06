#
# PySNMP MIB module TPLINK-GVRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-GVRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, TimeTicks, Unsigned32, iso, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "TimeTicks", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkGvrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 20))
tplinkGvrpMIB.setRevisions(('2012-12-06 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkGvrpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkGvrpMIB.setLastUpdated('201212060930Z')
if mibBuilder.loadTexts: tplinkGvrpMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkGvrpMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkGvrpMIB.setDescription('GVRP (GARP VLAN registration protocol) is an implementation of GARP (generic attribute registration protocol). GVRP allows the switch to automatically add or remove the VLANs via the dynamic VLAN registration information and propagate the local VLAN registration information to other switches, without having to individually configure each VLAN.')
tplinkGvrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1))
tpGvrpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 1))
tpGvrpGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: tpGvrpGlobalEnable.setDescription('Allows you to Enable/Disable the GVRP function. 0. disable 1. enable')
tpGvrpPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2))
tpGvrpPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1), )
if mibBuilder.loadTexts: tpGvrpPortTable.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortTable.setDescription('Here you can set the GVRP parameters for each port.')
tpGvrpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpGvrpPortEntry.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortEntry.setDescription('An entry contains of the information of a port.')
tpGvrpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpGvrpPortNumber.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortNumber.setDescription('Displays the port number.')
tpGvrpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpPortEnable.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortEnable.setDescription('Enable/Disable the GVRP feature for the port. The port type should be set to TRUNK before enabling the GVRP feature. 0. Disable 1. Enable')
tpGvrpPortRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("fixed", 1), ("forbidden", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpPortRegistration.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortRegistration.setDescription('Select the Registration Mode for the port. 0. NORMAL:In this mode, a port can dynamically register/deregister a VLAN and propagate the dynamic/static VLAN information. 1. FIXED:In this mode, a port cannot register/deregister a VLAN dynamically. It only propagates static VLAN information. 2. FORBIDDEN:In this mode, a port cannot register/deregister VLANs. It only propagates VLAN 1 information.')
tpGvrpLeaveAllTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 30000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpLeaveAllTimer.setStatus('current')
if mibBuilder.loadTexts: tpGvrpLeaveAllTimer.setDescription('Once the LeaveAll Timer is set, the port with GVRP enabled can send a LeaveAll message after the timer times out, so that other GARP ports can re-register all the attribute information. After that, the LeaveAll timer will start to begin a new cycle. The LeaveAll Timer ranges from 1000 to 30000 centiseconds and could be devided exactly by 5.')
tpGvrpJoinTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpJoinTimer.setStatus('current')
if mibBuilder.loadTexts: tpGvrpJoinTimer.setDescription('To guarantee the transmission of the Join messages, a GARP port sends each Join message two times. The Join Timer is used to define the interval between the two sending operations of each Join message. The Join Timer ranges from 20 to 1000 centiseconds and could be devided exactly by 5.')
tpGvrpLeaveTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGvrpLeaveTimer.setStatus('current')
if mibBuilder.loadTexts: tpGvrpLeaveTimer.setDescription('Once the Leave Timer is set, the GARP port receiving a Leave message will start its Leave timer, and unregister the attribute information if it does not receive a Join message again before the timer times out. The Leave Timer ranges from 60 to 3000 centiseconds and could be devided exactly by 5. (leave timer)*10 <= leaveAll timer, (join timer)*2 <= leave timer.')
tpGvrpPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 20, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpGvrpPortLag.setStatus('current')
if mibBuilder.loadTexts: tpGvrpPortLag.setDescription('Displays the LAG to which the port belongs.')
tplinkGvrpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 20, 2))
mibBuilder.exportSymbols("TPLINK-GVRP-MIB", tpGvrpPortEnable=tpGvrpPortEnable, tpGvrpGlobalEnable=tpGvrpGlobalEnable, tpGvrpPortConfig=tpGvrpPortConfig, tpGvrpPortRegistration=tpGvrpPortRegistration, tplinkGvrpMIBObjects=tplinkGvrpMIBObjects, tpGvrpLeaveTimer=tpGvrpLeaveTimer, tpGvrpLeaveAllTimer=tpGvrpLeaveAllTimer, tplinkGvrpMIB=tplinkGvrpMIB, tpGvrpPortTable=tpGvrpPortTable, tpGvrpJoinTimer=tpGvrpJoinTimer, PYSNMP_MODULE_ID=tplinkGvrpMIB, tpGvrpPortLag=tpGvrpPortLag, tplinkGvrpNotifications=tplinkGvrpNotifications, tpGvrpPortNumber=tpGvrpPortNumber, tpGvrpGlobalConfig=tpGvrpGlobalConfig, tpGvrpPortEntry=tpGvrpPortEntry)
