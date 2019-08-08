#
# PySNMP MIB module CISCOSB-EEE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-EEE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, ifOperStatus = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifOperStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, IpAddress, iso, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, Bits, Counter64, TimeTicks, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "IpAddress", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Bits", "Counter64", "TimeTicks", "Counter32", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlEee = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149))
rlEee.setRevisions(('2010-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlEee.setRevisionsDescriptions(('Add Energy Efficient Ethernet support per port and per system',))
if mibBuilder.loadTexts: rlEee.setLastUpdated('201003150000Z')
if mibBuilder.loadTexts: rlEee.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlEee.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlEee.setDescription('The private MIB module definition for Energy Efficient Ethernet feature.')
rlEeeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEeeEnable.setStatus('current')
if mibBuilder.loadTexts: rlEeeEnable.setDescription('Enable the EEE mode globally')
rlEeePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2), )
if mibBuilder.loadTexts: rlEeePortTable.setStatus('current')
if mibBuilder.loadTexts: rlEeePortTable.setDescription('A table of EEE state of ports')
rlEeePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlEeePortEntry.setStatus('current')
if mibBuilder.loadTexts: rlEeePortEntry.setDescription('An entry of EEE state of bridge port')
rlEeePortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEeePortAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rlEeePortAdminStatus.setDescription('Enable/Disable EEE on ifindex')
rlEeePortSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2, 1, 2), Bits().clone(namedValues=NamedValues(("rlEeePortSupported10M", 0), ("rlEeePortSupported100M", 1), ("rlEeePortSupported1G", 2), ("rlEeePortSupported10G", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortSupported.setStatus('current')
if mibBuilder.loadTexts: rlEeePortSupported.setDescription('Bit map that indicates whether EEE supported on the phy of the ifindex per speed 0 - speed 10m; 1 - 100m; 2 - 1g; 3 - 10g')
rlEeePortRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortRemoteStatus.setStatus('current')
if mibBuilder.loadTexts: rlEeePortRemoteStatus.setDescription("Indicates whether EEE active on remote link on current port's speed")
rlEeePortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortOperStatus.setStatus('current')
if mibBuilder.loadTexts: rlEeePortOperStatus.setDescription('Indicates whether EEE active on ifindex - ifoper is up, rlEeePortSupported BIT is on in current port speed rlEeePortLldpRemoteStatus is true, rlEeeEnable is true, rlEeePortAdminStatus is true')
rlEeePortLldpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 3), )
if mibBuilder.loadTexts: rlEeePortLldpTable.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpTable.setDescription('A table of EEE LLDP')
rlEeePortLldpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlEeePortLldpEntry.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpEntry.setDescription('An entry of EEE LLDP')
rlEeePortLldpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEeePortLldpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpAdminStatus.setDescription('Enable/Disable EEE LLDP on ifindex')
rlEeePortLldpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpOperStatus.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpOperStatus.setDescription('Indicates whether EEE LLDP active on ifindex - rlEeePortLldpAdminStatus is true lldpPortConfigAdminStatus is txAndRx, rlLldpEnabled is true, recieve a synch lldp packet')
rlEeePortLldpLocalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4), )
if mibBuilder.loadTexts: rlEeePortLldpLocalTable.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalTable.setDescription('A table of EEE Local ports')
rlEeePortLldpLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlEeePortLldpLocalEntry.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalEntry.setDescription('An entry of EEE Local port')
rlEeePortLldpLocalResolvedTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 1), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalResolvedTx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalResolvedTx.setDescription('Indicates the current Tw_sys_tx configured in the local system, in micro-seconds')
rlEeePortLldpLocalTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 2), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalTx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalTx.setDescription('Indicates the value of Tw_sys_tx that the local system can support, in micro-seconds')
rlEeePortLldpLocalTxEcho = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 3), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalTxEcho.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalTxEcho.setDescription("Indicates the remote system's Transmit Tw_sys_tx that was used by the local system to compute the Tw_sys_tx that it wants to request from the remote system, in micro-seconds")
rlEeePortLldpLocalResolvedRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 4), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalResolvedRx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalResolvedRx.setDescription('Indicates the current Tw_sys_tx configured by the remote system, in micro-seconds')
rlEeePortLldpLocalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 5), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalRx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalRx.setDescription('Indicates the value of Tw_sys_tx that the local system requests from the remote system, in micro-seconds')
rlEeePortLldpLocalRxEcho = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 4, 1, 6), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpLocalRxEcho.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpLocalRxEcho.setDescription('Indicates the remote system Receive Tw_sys_tx that was used by the local system to compute the Tw_sys_tx that it can support, in micro-seconds')
rlEeePortLldpRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5), )
if mibBuilder.loadTexts: rlEeePortLldpRemoteTable.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteTable.setDescription('A table of EEE remote ports')
rlEeePortLldpRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlEeePortLldpRemoteEntry.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteEntry.setDescription('An entry of EEE remote port')
rlEeePortLldpRemoteTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5, 1, 1), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpRemoteTx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteTx.setDescription('Indicates the value of Tw_sys_tx that the remote system can support, in micro-seconds')
rlEeePortLldpRemoteRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5, 1, 2), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpRemoteRx.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteRx.setDescription('Indicates the value of Tw_sys_tx that the remote system requests from the local system, in micro-seconds')
rlEeePortLldpRemoteTxEcho = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5, 1, 3), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpRemoteTxEcho.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteTxEcho.setDescription('Indicates the value of transmit Tw_sys_tx echoed back by the remote system, in micro-seconds')
rlEeePortLldpRemoteRxEcho = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149, 5, 1, 4), Unsigned32()).setUnits('uSec').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEeePortLldpRemoteRxEcho.setStatus('current')
if mibBuilder.loadTexts: rlEeePortLldpRemoteRxEcho.setDescription('Indicates the value Receive Tw_sys_tx echoed back by the remote system, in micro-seconds')
mibBuilder.exportSymbols("CISCOSB-EEE-MIB", rlEeePortLldpRemoteRxEcho=rlEeePortLldpRemoteRxEcho, rlEeePortTable=rlEeePortTable, rlEeePortLldpLocalTx=rlEeePortLldpLocalTx, rlEeePortLldpLocalResolvedTx=rlEeePortLldpLocalResolvedTx, rlEeePortLldpRemoteTxEcho=rlEeePortLldpRemoteTxEcho, rlEeePortLldpOperStatus=rlEeePortLldpOperStatus, rlEeePortRemoteStatus=rlEeePortRemoteStatus, rlEeePortLldpLocalResolvedRx=rlEeePortLldpLocalResolvedRx, rlEeePortLldpRemoteRx=rlEeePortLldpRemoteRx, rlEeePortLldpRemoteEntry=rlEeePortLldpRemoteEntry, rlEeePortLldpAdminStatus=rlEeePortLldpAdminStatus, rlEeePortLldpLocalTxEcho=rlEeePortLldpLocalTxEcho, rlEeePortLldpLocalEntry=rlEeePortLldpLocalEntry, rlEeePortAdminStatus=rlEeePortAdminStatus, rlEeePortLldpLocalRx=rlEeePortLldpLocalRx, rlEeePortLldpRemoteTx=rlEeePortLldpRemoteTx, rlEeePortLldpEntry=rlEeePortLldpEntry, rlEeePortLldpLocalTable=rlEeePortLldpLocalTable, rlEeePortLldpTable=rlEeePortLldpTable, rlEeePortLldpLocalRxEcho=rlEeePortLldpLocalRxEcho, PYSNMP_MODULE_ID=rlEee, rlEeeEnable=rlEeeEnable, rlEeePortOperStatus=rlEeePortOperStatus, rlEee=rlEee, rlEeePortSupported=rlEeePortSupported, rlEeePortEntry=rlEeePortEntry, rlEeePortLldpRemoteTable=rlEeePortLldpRemoteTable)