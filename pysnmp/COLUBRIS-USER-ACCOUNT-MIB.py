#
# PySNMP MIB module COLUBRIS-USER-ACCOUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-USER-ACCOUNT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Counter64, MibIdentifier, Gauge32, Unsigned32, Bits, NotificationType, TimeTicks, ModuleIdentity, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "Gauge32", "Unsigned32", "Bits", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisUserAccountMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 35))
if mibBuilder.loadTexts: colubrisUserAccountMIB.setLastUpdated('200704180000Z')
if mibBuilder.loadTexts: colubrisUserAccountMIB.setOrganization('Colubris Networks, Inc.')
colubrisUserAccountMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1))
coUserAccountStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1))
coUserAccountStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1), )
if mibBuilder.loadTexts: coUserAccountStatusTable.setStatus('current')
coUserAccountStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-USER-ACCOUNT-MIB", "coUserAccIndex"))
if mibBuilder.loadTexts: coUserAccountStatusEntry.setStatus('current')
coUserAccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coUserAccIndex.setStatus('current')
coUserAccUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccUserName.setStatus('current')
coUserAccPlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccPlanName.setStatus('current')
coUserAccRemainingOnlineTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 4), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccRemainingOnlineTime.setStatus('current')
coUserAccFirstLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccFirstLoginTime.setStatus('current')
coUserAccRemainingSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 6), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccRemainingSessionTime.setStatus('current')
coUserAccStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccStatus.setStatus('current')
coUserAccExpirationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccExpirationTime.setStatus('current')
colubrisUserAccountMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 2))
colubrisUserAccountMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 2, 0))
colubrisUserAccountMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3))
colubrisUserAccountMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1))
colubrisUserAccountMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2))
colubrisUserAccountMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1, 1)).setObjects(("COLUBRIS-USER-ACCOUNT-MIB", "colubrisUserAccountStatusMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserAccountMIBCompliance = colubrisUserAccountMIBCompliance.setStatus('current')
colubrisUserAccountStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2, 1)).setObjects(("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccUserName"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccPlanName"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingOnlineTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccFirstLoginTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingSessionTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccStatus"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccExpirationTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserAccountStatusMIBGroup = colubrisUserAccountStatusMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-USER-ACCOUNT-MIB", colubrisUserAccountMIBNotifications=colubrisUserAccountMIBNotifications, coUserAccountStatusEntry=coUserAccountStatusEntry, colubrisUserAccountMIBNotificationPrefix=colubrisUserAccountMIBNotificationPrefix, colubrisUserAccountStatusMIBGroup=colubrisUserAccountStatusMIBGroup, coUserAccRemainingSessionTime=coUserAccRemainingSessionTime, coUserAccRemainingOnlineTime=coUserAccRemainingOnlineTime, coUserAccStatus=coUserAccStatus, coUserAccountStatusTable=coUserAccountStatusTable, coUserAccPlanName=coUserAccPlanName, coUserAccountStatusGroup=coUserAccountStatusGroup, colubrisUserAccountMIBCompliance=colubrisUserAccountMIBCompliance, colubrisUserAccountMIBGroups=colubrisUserAccountMIBGroups, coUserAccIndex=coUserAccIndex, PYSNMP_MODULE_ID=colubrisUserAccountMIB, colubrisUserAccountMIBObjects=colubrisUserAccountMIBObjects, colubrisUserAccountMIBConformance=colubrisUserAccountMIBConformance, coUserAccUserName=coUserAccUserName, colubrisUserAccountMIB=colubrisUserAccountMIB, colubrisUserAccountMIBCompliances=colubrisUserAccountMIBCompliances, coUserAccFirstLoginTime=coUserAccFirstLoginTime, coUserAccExpirationTime=coUserAccExpirationTime)
