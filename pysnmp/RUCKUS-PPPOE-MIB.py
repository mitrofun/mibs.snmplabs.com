#
# PySNMP MIB module RUCKUS-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-PPPOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ruckusCommonPPPOEModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonPPPOEModule")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, IpAddress, ObjectIdentity, Gauge32, NotificationType, Bits, ModuleIdentity, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "Gauge32", "NotificationType", "Bits", "ModuleIdentity", "Unsigned32", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruckusPPPOEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1))
if mibBuilder.loadTexts: ruckusPPPOEMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusPPPOEMIB.setOrganization('Ruckus Wireless, Inc')
ruckusPPPOEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1))
ruckusPPPOEInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1))
ruckusPPPOEEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 2))
ruckusPPPOEUserName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEUserName.setStatus('current')
ruckusPPPOEPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEPassword.setStatus('current')
ruckusPPPOEConnectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("notConnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusPPPOEConnectionStatus.setStatus('current')
ruckusPPPOEConnection = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("connect", 1), ("disConnect", 2), ("ok", 3), ("disabled", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEConnection.setStatus('current')
ruckusPPPOEIfindex = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusPPPOEIfindex.setStatus('current')
ruckusPPPOEApply = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("apply", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEApply.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-PPPOE-MIB", ruckusPPPOEObjects=ruckusPPPOEObjects, ruckusPPPOEMIB=ruckusPPPOEMIB, ruckusPPPOEInfo=ruckusPPPOEInfo, ruckusPPPOEIfindex=ruckusPPPOEIfindex, ruckusPPPOEApply=ruckusPPPOEApply, ruckusPPPOEEvents=ruckusPPPOEEvents, ruckusPPPOEPassword=ruckusPPPOEPassword, ruckusPPPOEUserName=ruckusPPPOEUserName, ruckusPPPOEConnection=ruckusPPPOEConnection, PYSNMP_MODULE_ID=ruckusPPPOEMIB, ruckusPPPOEConnectionStatus=ruckusPPPOEConnectionStatus)
