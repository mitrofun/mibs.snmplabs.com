#
# PySNMP MIB module PPPOE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PPPOE-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Counter32, Unsigned32, MibIdentifier, Counter64, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swPPPoEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 79))
if mibBuilder.loadTexts: swPPPoEMIB.setLastUpdated('0904020000Z')
if mibBuilder.loadTexts: swPPPoEMIB.setOrganization('D-Link Corp')
if mibBuilder.loadTexts: swPPPoEMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swPPPoEMIB.setDescription('The structure of PPPoE management for the proprietary enterprise.')
swPPPoEMgmtCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 79, 1))
swPPPoECirIDInsertState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertState.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertState.setDescription('This object indicates the status of the PPPoE circuit ID insertion state of the switch.')
swPPPoECirIDInsertPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2))
swPPPoECirIDInsertPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1), )
if mibBuilder.loadTexts: swPPPoECirIDInsertPortTable.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortTable.setDescription('The table specifies the PPPoE circuit ID insertion function specified by the port.')
swPPPoECirIDInsertPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1), ).setIndexNames((0, "PPPOE-MGMT-MIB", "swPPPoECirIDInsertPortIndex"))
if mibBuilder.loadTexts: swPPPoECirIDInsertPortEntry.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortEntry.setDescription('A list of information contained in swPPPoECirIDInsertPortTable.')
swPPPoECirIDInsertPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: swPPPoECirIDInsertPortIndex.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortIndex.setDescription("This object indicates the module's port number. The range is from 1 to the maximum port number specified in the module")
swPPPoECirIDInsertPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortState.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortState.setDescription('This object indicates the PPPoE circuit ID insertion function state on the port.')
swPPPoECirIDInsertPortCirID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("switch-ip", 1), ("switch-mac", 2), ("udf-string", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortCirID.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortCirID.setDescription('This object indicates the port circuit ID.')
swPPPoECirIDInsertPortUDFString = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPPPoECirIDInsertPortUDFString.setStatus('current')
if mibBuilder.loadTexts: swPPPoECirIDInsertPortUDFString.setDescription('This object indicates the user define string when the circuit ID is UDF string.')
mibBuilder.exportSymbols("PPPOE-MGMT-MIB", swPPPoECirIDInsertPortIndex=swPPPoECirIDInsertPortIndex, swPPPoECirIDInsertPortMgmt=swPPPoECirIDInsertPortMgmt, swPPPoECirIDInsertPortCirID=swPPPoECirIDInsertPortCirID, PYSNMP_MODULE_ID=swPPPoEMIB, swPPPoECirIDInsertPortEntry=swPPPoECirIDInsertPortEntry, swPPPoEMgmtCtrl=swPPPoEMgmtCtrl, swPPPoECirIDInsertPortUDFString=swPPPoECirIDInsertPortUDFString, swPPPoECirIDInsertState=swPPPoECirIDInsertState, swPPPoECirIDInsertPortState=swPPPoECirIDInsertPortState, swPPPoEMIB=swPPPoEMIB, swPPPoECirIDInsertPortTable=swPPPoECirIDInsertPortTable)
