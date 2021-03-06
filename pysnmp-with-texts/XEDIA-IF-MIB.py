#
# PySNMP MIB module XEDIA-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Gauge32, ModuleIdentity, NotificationType, TimeTicks, Counter64, ObjectIdentity, IpAddress, Unsigned32, Bits, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "Bits", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 40))
if mibBuilder.loadTexts: xediaIfMIB.setLastUpdated('9911112155Z')
if mibBuilder.loadTexts: xediaIfMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaIfMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaIfMIB.setDescription("This module defines additional objects for management of Interfaces in Xedia devices, beyond what is defined in the IETF's ifMib.")
xifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 1))
xifNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 2))
xifConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 3))
class Unsigned32(Gauge32):
    pass

xifNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xifNextIndex.setStatus('current')
if mibBuilder.loadTexts: xifNextIndex.setDescription('Variable indicating what ifIndex value to use in a row create operation in the ifTable (using the Xedia rowStatus extension).')
xifTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2), )
if mibBuilder.loadTexts: xifTable.setStatus('current')
if mibBuilder.loadTexts: xifTable.setDescription('A table that allows add/deletes of ifEntries.')
xifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xifEntry.setStatus('current')
if mibBuilder.loadTexts: xifEntry.setDescription('.')
xifRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xifRowStatus.setReference('RFC1903: Textual Conventions for Version 2 of the Simple Network Management Protocol (SNMPv2).')
if mibBuilder.loadTexts: xifRowStatus.setStatus('current')
if mibBuilder.loadTexts: xifRowStatus.setDescription("This object is used to add entries to the ifTable. The object ifStackStatus, from the standard ifStack table is covered here as well. It is used to connect and disconnect ifEntries. When creating a new entry, the value of xifRowStatus must be createAndGo(4). In addition, the ifName object must be supplied in the same PDU. Choosing the ifIndex value: While any ifIndex value may be supplied, in order to avoid an error and choose the best value for ifIndex, the xifNextIndex object should be used. It is a test-and-increment variable which means that the client must first get the present value and then do a set (on xifNextIndex) with that same value. If that sequence is succesfull then the client owns that value (until the next reset of the system unless the value is actually used to create an entry). Choosing the ifName value: The choice for ifName must conform to the format: <component-name>.<instance-number>.[<sub-interface-number>] Special cases: To create the next correct ifName <instance-number> or <sub-interface-number> the keyword 'new' may be used. For physical slots (the bottom of a physical the stack) the name format is slot.<slot-number>.<port-number> The bottom of the ipsec stack (virtual in the stack command) is ipsec-transform.1 Example names are: eth.1 frame-relay.new, frame-relay.1.new Example SNMP sequence to create a new CBQ interface: get xifNextIndex.0 value = 32 set xifNextIndex.0 32 <no-error> set ifName.32 'cbq.new' xifRowStatus.32 'CreateAndGo(4)' NOTE: A new layer and sub-interface may not be created in the same request since two ifIndex values are required. If both a new layer and sub-interface are offered, only the layer is created and no warning is given. Connecting and disconnecting ifEntries: In order to connect or disconnect created ifEntries, the ifStack table must be used. Each entry in the stack table indicates a connection between two ifEntries. For example, to connect an interface with ifName of eth.1 and the other with the name ip.1, the following would be done. If the ifIndex values are not known, the xsysIfNameIndexTable should be used. It has an index of ifName and returns the associated ifIndex. Once the ifIndex values of the two ifEntries to be connected are known, then create or remove an entry in the stack table. Example SNMP sequence to connect eth.1 to ip.1 get xsysIfIndex.'eth.1' (note instance value is a string) value = 20 get xsysIfIndex.'ip.1' value = 24 set ifStackStatus.24.20 'CreateAndGo(4)' To disconnect: set ifStackStatus.24.20 'Destroy(6)' Restrictions: To be consistent with the cli 'stack' command in most cases the stack can be built from the bottom. However, when connecting CBQ layers, there are some cases where it must be conneceted to its upper layer before connected to its lower layer. For instance, when connecting eth.1 cbq.1 ip.1 cbq.1 must be connected to ip.1 before eth.1 is connected to cbq.1.")
mibBuilder.exportSymbols("XEDIA-IF-MIB", xifTable=xifTable, xifRowStatus=xifRowStatus, xifEntry=xifEntry, xifNotifications=xifNotifications, Unsigned32=Unsigned32, xediaIfMIB=xediaIfMIB, xifNextIndex=xifNextIndex, xifConformance=xifConformance, PYSNMP_MODULE_ID=xediaIfMIB, xifObjects=xifObjects)
