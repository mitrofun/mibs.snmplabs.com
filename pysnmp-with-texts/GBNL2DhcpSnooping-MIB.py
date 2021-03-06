#
# PySNMP MIB module GBNL2DhcpSnooping-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNL2DhcpSnooping-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, TimeTicks, IpAddress, Counter32, iso, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Unsigned32, Integer32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "IpAddress", "Counter32", "iso", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "MibIdentifier", "Gauge32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
gbnL3DhcpSnooping = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5))
gbnL3DhcpSnooping.setRevisions(('1901-05-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gbnL3DhcpSnooping.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: gbnL3DhcpSnooping.setLastUpdated('0105030000Z')
if mibBuilder.loadTexts: gbnL3DhcpSnooping.setOrganization('Greentech')
if mibBuilder.loadTexts: gbnL3DhcpSnooping.setContactInfo('Adam Armstrong E-mail: adama@observium.org')
if mibBuilder.loadTexts: gbnL3DhcpSnooping.setDescription('GBN Enterprise MIB definition.')
dhcpsnoopingOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpsnoopingOnOff.setStatus('current')
if mibBuilder.loadTexts: dhcpsnoopingOnOff.setDescription('start/stop dhcpsnooping.Default is off')
dhcpsnoopingPortTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2), )
if mibBuilder.loadTexts: dhcpsnoopingPortTable.setStatus('current')
if mibBuilder.loadTexts: dhcpsnoopingPortTable.setDescription('A table that contains port informations of dhcpsnooping.')
dhcpsnoopingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1), ).setIndexNames((0, "GBNL2DhcpSnooping-MIB", "portIndex"))
if mibBuilder.loadTexts: dhcpsnoopingPortEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpsnoopingPortEntry.setDescription('Port informations of dhcpsnooping. This is indexed by the port number.')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('current')
if mibBuilder.loadTexts: portIndex.setDescription('The Index of the port.')
portTrustMode = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trust", 1), ("untrust", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrustMode.setStatus('current')
if mibBuilder.loadTexts: portTrustMode.setDescription('Port mode of dhcpsnooping.Default is untrust.')
portMaxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMaxNum.setStatus('current')
if mibBuilder.loadTexts: portMaxNum.setDescription('Max clients in this port.Range is from 0 to 2048.Default is 2048.')
portIpSourceGuardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portIpSourceGuardMode.setStatus('current')
if mibBuilder.loadTexts: portIpSourceGuardMode.setDescription('Port IP source guard mode .Default is off.')
dhcpsnoopingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3), )
if mibBuilder.loadTexts: dhcpsnoopingVlanTable.setStatus('current')
if mibBuilder.loadTexts: dhcpsnoopingVlanTable.setDescription('A table that contains vlan informations of dhcpsnooping.')
dhcpsnoopingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1), ).setIndexNames((0, "GBNL2DhcpSnooping-MIB", "vlanIndex"))
if mibBuilder.loadTexts: dhcpsnoopingVlanEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpsnoopingVlanEntry.setDescription('VLAN informations of dhcpsnooping. This is indexed by the vlan number.')
vlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanIndex.setStatus('current')
if mibBuilder.loadTexts: vlanIndex.setDescription('The Index of the port.')
vlanMaxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMaxNum.setStatus('current')
if mibBuilder.loadTexts: vlanMaxNum.setDescription('Max clients in this vlan.Range is from 0 to 2048.Default is 2048.')
mibBuilder.exportSymbols("GBNL2DhcpSnooping-MIB", gbnL3DhcpSnooping=gbnL3DhcpSnooping, portTrustMode=portTrustMode, PYSNMP_MODULE_ID=gbnL3DhcpSnooping, portIndex=portIndex, portIpSourceGuardMode=portIpSourceGuardMode, vlanIndex=vlanIndex, portMaxNum=portMaxNum, dhcpsnoopingPortEntry=dhcpsnoopingPortEntry, dhcpsnoopingVlanTable=dhcpsnoopingVlanTable, vlanMaxNum=vlanMaxNum, dhcpsnoopingVlanEntry=dhcpsnoopingVlanEntry, dhcpsnoopingPortTable=dhcpsnoopingPortTable, dhcpsnoopingOnOff=dhcpsnoopingOnOff)
