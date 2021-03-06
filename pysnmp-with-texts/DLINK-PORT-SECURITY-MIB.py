#
# PySNMP MIB module DLINK-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-PORT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:49:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Gauge32, NotificationType, TimeTicks, IpAddress, MibIdentifier, Counter64, ModuleIdentity, Integer32, Bits, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "ModuleIdentity", "Integer32", "Bits", "Unsigned32", "iso")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
swPortSecMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 63))
if mibBuilder.loadTexts: swPortSecMIB.setLastUpdated('1210161030Z')
if mibBuilder.loadTexts: swPortSecMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swPortSecMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swPortSecMIB.setDescription('The structure of port security for the proprietary enterprise.')
swPortSecCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 1))
swPortSecInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 2))
swPortSecMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 3))
swPortSecTrapLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecTrapLogState.setStatus('current')
if mibBuilder.loadTexts: swPortSecTrapLogState.setDescription("When enabled(1), whenever there's a new MAC address that violates the pre-defined port security configuration, traps will be sent out and the relevant information will be logged into the system.")
swPortSecSysMaxLernAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecSysMaxLernAddr.setStatus('current')
if mibBuilder.loadTexts: swPortSecSysMaxLernAddr.setDescription('Indicates the maximum number of addresses to be authorized by port security on the system. A value of -1 means no-limit. The default value is no-limit. The max entry range is (1..N). The value N means the max number and is determined by the project itself.')
swPortSecTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecTrapState.setStatus('current')
if mibBuilder.loadTexts: swPortSecTrapState.setDescription("When enabled(1), whenever there's a new MAC address that violates the pre-defined port security configuration, trap will be sent out.")
swPortSecLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecLogState.setStatus('current')
if mibBuilder.loadTexts: swPortSecLogState.setDescription("When enabled(1), whenever there's a new MAC address that violates the pre-defined port security configuration, the relevant information will be logged into the system.")
swPortSecMgmtByPort = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1))
swPortSecPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1), )
if mibBuilder.loadTexts: swPortSecPortTable.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortTable.setDescription('A port security feature which controls the address learning capability and traffic forwarding decisions. Each port can be enabled or disabled for this function. When it is enabled and a number is given said N, which allows N addresses to be learned on this port, the first N learned addresses are locked at this port as static entries. When the learned addresses number reaches N, any incoming packet without learned source addresses are discarded (e.g. dropped) and no more new addresses can be learned on this port.')
swPortSecPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1), ).setIndexNames((0, "DLINK-PORT-SECURITY-MIB", "swPortSecPortIndex"))
if mibBuilder.loadTexts: swPortSecPortEntry.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortEntry.setDescription('A list of information contained in the swPortSecPortTable.')
swPortSecPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: swPortSecPortIndex.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortIndex.setDescription('Indicates the secured port to lock address learning.')
swPortSecPortMaxLernAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecPortMaxLernAddr.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortMaxLernAddr.setDescription('Indicates the allowable number of addresses to be learned on this port. The max entry range is (0..N). The value N means the max number and is determined by the project itself.')
swPortSecPortLockAddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("permanent", 1), ("deleteOnTimeout", 2), ("deleteOnReset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecPortLockAddrMode.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortLockAddrMode.setDescription('Indicates the mode of locking address. In deleteOnTimeout(2) mode, the locked addresses can be aged out after the aging timer expires. In this mode, when the locked address is aged out, the number of addresses that can be learned has to be increased by one. In deleteOnReset (3) mode, locked addresses never age out unless the system restarts which will prevent port movement or intrusion.')
swPortSecPortAdmState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecPortAdmState.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortAdmState.setDescription('Indicates the administration state of the locking address.')
swPortSecPortClearCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecPortClearCtrl.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortClearCtrl.setDescription("Used to clear port security entries by port. Setting this value to 'start' will execute the clear action. Once cleared, the value returns to 'other'.")
swPortSecPortViolationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("shutdown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecPortViolationAction.setStatus('current')
if mibBuilder.loadTexts: swPortSecPortViolationAction.setDescription('Used to indicates the action when violation occurs. When the number of secure MAC address reaches the maximum learning number on the port, for drop action, new entry will be dropped and for shutdown action, the port will be shut down and enter error-disabled state immediately.')
swPortSecMgmtByVLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2))
swPortSecVLANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1), )
if mibBuilder.loadTexts: swPortSecVLANTable.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANTable.setDescription('A port security feature which controls the address leaning capability. When number is given said N, which allows N addresses to be learned on this VLAN, the first N learned addresses are locked at this VLAN as static entries. When the learned addresses number reaches N, any incoming packet without learned source addresses are discarded (e.g. dropped) and no more new addresses can be learned on this VLAN.')
swPortSecVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1), ).setIndexNames((0, "DLINK-PORT-SECURITY-MIB", "swPortSecVLANID"))
if mibBuilder.loadTexts: swPortSecVLANEntry.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANEntry.setDescription('A list of information contained in the swPortSecVLANTable.')
swPortSecVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: swPortSecVLANID.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANID.setDescription('Indicates the secured VLAN to lock address learning.')
swPortSecVLANMaxLernAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecVLANMaxLernAddr.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANMaxLernAddr.setDescription('Indicates allowable number of addresses to be learned on this VLAN. A value of -1 means no-limit. The default value is no-limit. The max entry range is (0..N). The value N means the max number and is determined by the project itself.')
swPortSecVLANClearCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecVLANClearCtrl.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANClearCtrl.setDescription("Used to clear port security entries by VLAN. Setting this value to 'start' will execute the clear action. Once cleared, the value returns to 'other'. ")
swPortSecMgmtByVLANOnPort = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3))
swPortSecVLANOnPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1), )
if mibBuilder.loadTexts: swPortSecVLANOnPortTable.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANOnPortTable.setDescription('A port security feature which controls the address learning capability. When number is given said N, which allows N addresses to be learned on this VLAN from the special port, the first N learned addresses are locked at this VLAN from the special port as static entries. When the learned addresses number reaches N, any incoming packet without learned source addresses are discarded (e.g. dropped) and no more new addresses can be learned on this VLAN from the special port.')
swPortSecVLANOnPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1), ).setIndexNames((0, "DLINK-PORT-SECURITY-MIB", "swPortSecPortIndex"), (0, "DLINK-PORT-SECURITY-MIB", "swPortSecVLANID"))
if mibBuilder.loadTexts: swPortSecVLANOnPortEntry.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANOnPortEntry.setDescription('A list of information contained in the swPortSecVLANOnPortTable.')
swPortSecVLANOnPortMaxLernAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecVLANOnPortMaxLernAddr.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANOnPortMaxLernAddr.setDescription('Indicates allowable number of addresses to be learned on this VLAN from the special port. A value of -1 means no-limit. The default value is no-limit. Only VLANs with limitations will be displayed in this table. The max entry range is (0..N). The value N means the max number and is determined by the project itself.')
swPortSecVLANOnPortAddCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("add", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortSecVLANOnPortAddCtrl.setStatus('current')
if mibBuilder.loadTexts: swPortSecVLANOnPortAddCtrl.setDescription("other (1): When user gets this object, it always returns other(1). add (2): Used to configure the VLAN limit from the special port. If 'add' is selected, swPortSecVLANOnPortMaxLernAddr must be set to a valid value except -1. ")
swPortSecMgmtByVLANOnPortClearCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2))
swPortSecMgmtByVLANOnPortClearPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearPort.setStatus('current')
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearPort.setDescription('Indicates the port.')
swPortSecMgmtByVLANOnPortClearVID = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearVID.setStatus('current')
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearVID.setDescription('Indicates the VID.')
swPortSecMgmtByVLANOnPortClearAction = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearAction.setStatus('current')
if mibBuilder.loadTexts: swPortSecMgmtByVLANOnPortClearAction.setDescription('other(1): When user gets this object, it always returns other(1). start(2): Used to clear port security entries by VLAN on the special port.')
swPortSecEntriesTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4), )
if mibBuilder.loadTexts: swPortSecEntriesTable.setStatus('current')
if mibBuilder.loadTexts: swPortSecEntriesTable.setDescription('This table is used to show port security entries.')
swPortSecEntriesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1), ).setIndexNames((0, "DLINK-PORT-SECURITY-MIB", "swPortSecMac"), (0, "DLINK-PORT-SECURITY-MIB", "swPortSecVID"))
if mibBuilder.loadTexts: swPortSecEntriesEntry.setStatus('current')
if mibBuilder.loadTexts: swPortSecEntriesEntry.setDescription('A list of information contained in the swPortSecEntriesTable.')
swPortSecMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortSecMac.setStatus('current')
if mibBuilder.loadTexts: swPortSecMac.setDescription('Specifies a MAC address.')
swPortSecVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortSecVID.setStatus('current')
if mibBuilder.loadTexts: swPortSecVID.setDescription('Indicates the VLAN ID.')
swPortSecPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortSecPort.setStatus('current')
if mibBuilder.loadTexts: swPortSecPort.setDescription('Indicates the port.')
swPortSecDelCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 63, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortSecDelCtrl.setStatus('current')
if mibBuilder.loadTexts: swPortSecDelCtrl.setDescription("Used to delete this port security entry. Setting this value to 'start' will execute the delete action. Once deleted, the value returns to 'other'.")
mibBuilder.exportSymbols("DLINK-PORT-SECURITY-MIB", swPortSecPortLockAddrMode=swPortSecPortLockAddrMode, swPortSecMgmtByPort=swPortSecMgmtByPort, PYSNMP_MODULE_ID=swPortSecMIB, swPortSecMgmtByVLANOnPortClearVID=swPortSecMgmtByVLANOnPortClearVID, swPortSecInfo=swPortSecInfo, swPortSecPortViolationAction=swPortSecPortViolationAction, swPortSecVLANID=swPortSecVLANID, swPortSecEntriesTable=swPortSecEntriesTable, swPortSecEntriesEntry=swPortSecEntriesEntry, swPortSecCtrl=swPortSecCtrl, swPortSecDelCtrl=swPortSecDelCtrl, swPortSecLogState=swPortSecLogState, swPortSecVLANClearCtrl=swPortSecVLANClearCtrl, swPortSecMIB=swPortSecMIB, swPortSecPortClearCtrl=swPortSecPortClearCtrl, swPortSecMgmt=swPortSecMgmt, swPortSecSysMaxLernAddr=swPortSecSysMaxLernAddr, swPortSecTrapState=swPortSecTrapState, swPortSecPortIndex=swPortSecPortIndex, swPortSecMgmtByVLANOnPort=swPortSecMgmtByVLANOnPort, swPortSecPortAdmState=swPortSecPortAdmState, swPortSecMgmtByVLANOnPortClearPort=swPortSecMgmtByVLANOnPortClearPort, swPortSecVLANEntry=swPortSecVLANEntry, swPortSecVLANOnPortMaxLernAddr=swPortSecVLANOnPortMaxLernAddr, swPortSecVLANOnPortEntry=swPortSecVLANOnPortEntry, swPortSecTrapLogState=swPortSecTrapLogState, swPortSecPortMaxLernAddr=swPortSecPortMaxLernAddr, swPortSecVLANOnPortTable=swPortSecVLANOnPortTable, swPortSecPortTable=swPortSecPortTable, swPortSecVLANTable=swPortSecVLANTable, swPortSecMgmtByVLAN=swPortSecMgmtByVLAN, swPortSecVID=swPortSecVID, swPortSecPort=swPortSecPort, swPortSecMgmtByVLANOnPortClearCtrl=swPortSecMgmtByVLANOnPortClearCtrl, swPortSecMac=swPortSecMac, swPortSecPortEntry=swPortSecPortEntry, swPortSecVLANMaxLernAddr=swPortSecVLANMaxLernAddr, swPortSecVLANOnPortAddCtrl=swPortSecVLANOnPortAddCtrl, swPortSecMgmtByVLANOnPortClearAction=swPortSecMgmtByVLANOnPortClearAction)
