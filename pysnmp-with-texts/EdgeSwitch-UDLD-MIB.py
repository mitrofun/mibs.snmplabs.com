#
# PySNMP MIB module EdgeSwitch-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-UDLD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Gauge32, ModuleIdentity, TimeTicks, NotificationType, IpAddress, Counter64, MibIdentifier, ObjectIdentity, Integer32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "Integer32", "iso", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
fastPathUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54))
fastPathUdld.setRevisions(('2008-02-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathUdld.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: fastPathUdld.setLastUpdated('200712030000Z')
if mibBuilder.loadTexts: fastPathUdld.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathUdld.setContactInfo('')
if mibBuilder.loadTexts: fastPathUdld.setDescription('The Ubiquiti Private MIB for FastPath UDLD.')
agentUdldMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1))
agentUdldGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 1))
agentUdldInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2))
agentUdldGlobalMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldGlobalMode.setStatus('current')
if mibBuilder.loadTexts: agentUdldGlobalMode.setDescription('Indicates the mode of UDLDP feature on the device. enable -- Unidirectional Link Detection Protocol is enabled on the device. disable -- Unidirectional Link Detection Protocol is disabled on the device.')
agentUdldMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 90))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldMessageInterval.setStatus('current')
if mibBuilder.loadTexts: agentUdldMessageInterval.setDescription('Indicates interval in seconds at which each port sends a packet to all of its neighbors at steady state when the link has been identified as bidirectional.')
agentUdldTimeoutInterval = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldTimeoutInterval.setStatus('current')
if mibBuilder.loadTexts: agentUdldTimeoutInterval.setDescription('Indicates Timeout interval in seconds.')
agentUdldReset = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOperation", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldReset.setStatus('current')
if mibBuilder.loadTexts: agentUdldReset.setDescription('Resets all interfaces that have been shutdown by UDLD. On read OID will always be 0.')
agentUdldInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2, 1), )
if mibBuilder.loadTexts: agentUdldInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: agentUdldInterfaceTable.setDescription("The table containing the status of UDLDP on the device's interfaces.")
agentUdldInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: agentUdldInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: agentUdldInterfaceEntry.setDescription(' An entry exists for each interface that supports UDLDP.')
agentUdldInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("shutdown", 1), ("undetermined", 2), ("biDirectional", 3), ("notApplicable", 4), ("undetermined-LinkDown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentUdldInterfaceOperStatus.setStatus('current')
if mibBuilder.loadTexts: agentUdldInterfaceOperStatus.setDescription(" This mib object contains the following values, which has the meaning as: 'shutdown' - An Unidirectional link has been detected and the port has been disabled. 'undetermined' - Unidirectional Link Detection protocol has not collected enough information to determine if the link is bidirectional or not. 'biDirectional' - A bidirectional link has been detected. 'notApplicable' - Unidirectional Link Detection Protocol is disabled. 'undetermined-LinkDown' - The port would transition into this state when the port link physically goes down due to any reasons other than the port been put into D-Disable mode by UDLD protocol on the switch. ")
agentUdldInterfaceAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldInterfaceAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentUdldInterfaceAdminMode.setDescription('Indicates the Administrative mode of Unidirectional Link Detection Protocol Feature configured on this interface. enable -- Unidirectional Link Detection Protocol is enabled on this interface. disable -- Unidirectional Link Detection Protocol is disabled on this interface.')
agentUdldInterfaceAggresiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 54, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUdldInterfaceAggresiveMode.setStatus('current')
if mibBuilder.loadTexts: agentUdldInterfaceAggresiveMode.setDescription('Indicates the mode of UDLDP feature on the interface. TRUE -- Aggressive mode is enabled on the interface. FALSE -- Aggressive mode is disabled on the interface.')
mibBuilder.exportSymbols("EdgeSwitch-UDLD-MIB", agentUdldInterfaceOperStatus=agentUdldInterfaceOperStatus, agentUdldMessageInterval=agentUdldMessageInterval, PYSNMP_MODULE_ID=fastPathUdld, agentUdldGlobalMode=agentUdldGlobalMode, agentUdldTimeoutInterval=agentUdldTimeoutInterval, agentUdldInterfaceAggresiveMode=agentUdldInterfaceAggresiveMode, agentUdldInterface=agentUdldInterface, fastPathUdld=fastPathUdld, agentUdldReset=agentUdldReset, agentUdldInterfaceAdminMode=agentUdldInterfaceAdminMode, agentUdldGlobal=agentUdldGlobal, agentUdldMIBObjects=agentUdldMIBObjects, agentUdldInterfaceTable=agentUdldInterfaceTable, agentUdldInterfaceEntry=agentUdldInterfaceEntry)
