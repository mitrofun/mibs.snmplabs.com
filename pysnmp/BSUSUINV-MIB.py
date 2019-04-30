#
# PySNMP MIB module BSUSUINV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUSUINV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aniBsuSuGroup, = mibBuilder.importSymbols("ANIROOT-MIB", "aniBsuSuGroup")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, Unsigned32, MibIdentifier, ModuleIdentity, ObjectIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "iso", "IpAddress")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
aniBsuSuInventory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1))
if mibBuilder.loadTexts: aniBsuSuInventory.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuSuInventory.setOrganization('Aperto Networks')
aniBsuSuInvTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1), )
if mibBuilder.loadTexts: aniBsuSuInvTable.setStatus('current')
aniBsuSuInvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1), ).setIndexNames((0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"), (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"))
if mibBuilder.loadTexts: aniBsuSuInvEntry.setStatus('current')
aniBsuSuMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuMacAddr.setStatus('current')
aniBsuSuIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuIpAddr.setStatus('current')
aniBsuSuName = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuName.setStatus('current')
aniBsuSuCustomerName = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuCustomerName.setStatus('current')
aniBsuSuLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 255))).clone(namedValues=NamedValues(("initial", 1), ("ulm-req-rcvd", 2), ("ulm-rsp-sent", 3), ("dhcp-req-rcvd", 4), ("dhcp-rsp-sent", 5), ("tod-req-rcvd", 6), ("tod-rsp-sent", 7), ("config-file-req-rcvd", 8), ("config-file-req-sent", 9), ("reg-req-rcvd", 10), ("lic-rsp-recd", 11), ("reg-rsp-sent", 12), ("reg-ack-rcvd", 13), ("operational", 14), ("stand-by", 15), ("delete", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuSuLinkStatus.setStatus('current')
aniBsuSuModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuModelNumber.setStatus('current')
mibBuilder.exportSymbols("BSUSUINV-MIB", aniBsuSuLinkStatus=aniBsuSuLinkStatus, aniBsuSuIpAddr=aniBsuSuIpAddr, aniBsuSuCustomerName=aniBsuSuCustomerName, aniBsuSuInventory=aniBsuSuInventory, aniBsuSuModelNumber=aniBsuSuModelNumber, aniBsuSuInvTable=aniBsuSuInvTable, aniBsuSuMacAddr=aniBsuSuMacAddr, aniBsuSuName=aniBsuSuName, aniBsuSuInvEntry=aniBsuSuInvEntry, PYSNMP_MODULE_ID=aniBsuSuInventory)