#
# PySNMP MIB module JUNIPER-MOBILE-GW-SGW-MFWD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MOBILE-GW-SGW-MFWD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
jnxMobileGatewaySgw, = mibBuilder.importSymbols("JUNIPER-MBG-SMI", "jnxMobileGatewaySgw")
EnabledStatus, = mibBuilder.importSymbols("JUNIPER-MIMSTP-MIB", "EnabledStatus")
jnxMbgGwName, = mibBuilder.importSymbols("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, Counter64, iso, Counter32, MibIdentifier, ObjectIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter64", "iso", "Counter32", "MibIdentifier", "ObjectIdentity", "NotificationType", "Integer32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
jnxMbgSgwMfwdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7))
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setLastUpdated('201108041200Z')
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setOrganization('Juniper Networks, Inc.')
jnxMbgSgwMfwdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0))
jnxMbgSgwMfwdNotificationVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1))
jnxMbgSgwMfwdServicePicName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 15))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgSgwMfwdServicePicName.setStatus('current')
jnxMbgSgwMfwdBufMemLimit = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 2), Gauge32()).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemLimit.setStatus('current')
jnxMbgSgwMfwdBufMemThresRaise = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 1)).setObjects(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresRaise.setStatus('current')
jnxMbgSgwMfwdBufMemThresClear = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 2)).setObjects(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresClear.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", jnxMbgSgwMfwdNotificationVars=jnxMbgSgwMfwdNotificationVars, jnxMbgSgwMfwdServicePicName=jnxMbgSgwMfwdServicePicName, jnxMbgSgwMfwdMib=jnxMbgSgwMfwdMib, jnxMbgSgwMfwdBufMemThresRaise=jnxMbgSgwMfwdBufMemThresRaise, jnxMbgSgwMfwdNotifications=jnxMbgSgwMfwdNotifications, jnxMbgSgwMfwdBufMemLimit=jnxMbgSgwMfwdBufMemLimit, PYSNMP_MODULE_ID=jnxMbgSgwMfwdMib, jnxMbgSgwMfwdBufMemThresClear=jnxMbgSgwMfwdBufMemThresClear)
