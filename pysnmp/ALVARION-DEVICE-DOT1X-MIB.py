#
# PySNMP MIB module ALVARION-DEVICE-DOT1X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-DEVICE-DOT1X-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
coDevDisIndex, = mibBuilder.importSymbols("ALVARION-DEVICE-MIB", "coDevDisIndex")
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Gauge32, ObjectIdentity, Counter64, IpAddress, TimeTicks, Bits, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "TimeTicks", "Bits", "MibIdentifier", "NotificationType")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
alvarionDeviceDot1xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32))
if mibBuilder.loadTexts: alvarionDeviceDot1xMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionDeviceDot1xMIB.setOrganization('Alvarion Ltd.')
alvarionDeviceDot1xMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1))
coDeviceDot1xConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 1))
coDeviceDot1xStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2))
coDeviceDot1xStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3))
coDeviceDot1xStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatusTable.setStatus('current')
coDeviceDot1xStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-DEVICE-MIB", "coDevDisIndex"), (0, "ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaIndex"))
if mibBuilder.loadTexts: coDeviceDot1xStatusEntry.setStatus('current')
coDev1xStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDev1xStaIndex.setStatus('current')
coDev1xStaMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaMacAddress.setStatus('current')
coDev1xStaUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaUserName.setStatus('current')
coDev1xStaPaeState = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPaeState.setStatus('current')
coDev1xStaBackendAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthState.setStatus('current')
coDev1xStaPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authorized", 1), ("unauthorized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPortStatus.setStatus('current')
coDev1xStaSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 7), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaSessionTime.setStatus('current')
coDev1xStaTerminateCause = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaTerminateCause.setStatus('current')
coDeviceDot1xStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatsTable.setStatus('current')
coDeviceDot1xStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1), )
coDeviceDot1xStatusEntry.registerAugmentions(("ALVARION-DEVICE-DOT1X-MIB", "coDeviceDot1xStatsEntry"))
coDeviceDot1xStatsEntry.setIndexNames(*coDeviceDot1xStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceDot1xStatsEntry.setStatus('current')
coDev1xStaEapolRxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolRxFrame.setStatus('current')
coDev1xStaEapolTxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolTxFrame.setStatus('current')
coDev1xStaBackendResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendResponses.setStatus('current')
coDev1xStaBackendChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendChallenges.setStatus('current')
coDev1xStaBackendAuthSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthSuccesses.setStatus('current')
coDev1xStaBackendAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthFails.setStatus('current')
alvarionDeviceDot1xMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2))
alvarionDeviceDot1xMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2, 1))
alvarionDeviceDot1xMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2, 2))
alvarionDeviceDot1xMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2, 1, 1)).setObjects(("ALVARION-DEVICE-DOT1X-MIB", "alvarionDeviceDot1xStatusMIBGroup"), ("ALVARION-DEVICE-DOT1X-MIB", "alvarionDeviceDot1xStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceDot1xMIBCompliance = alvarionDeviceDot1xMIBCompliance.setStatus('current')
alvarionDeviceDot1xStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2, 2, 1)).setObjects(("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaMacAddress"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaUserName"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaPaeState"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthState"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaPortStatus"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaSessionTime"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaTerminateCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceDot1xStatusMIBGroup = alvarionDeviceDot1xStatusMIBGroup.setStatus('current')
alvarionDeviceDot1xStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 32, 2, 2, 2)).setObjects(("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaEapolRxFrame"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaEapolTxFrame"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaBackendResponses"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaBackendChallenges"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthSuccesses"), ("ALVARION-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthFails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceDot1xStatsMIBGroup = alvarionDeviceDot1xStatsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-DEVICE-DOT1X-MIB", coDev1xStaBackendAuthState=coDev1xStaBackendAuthState, alvarionDeviceDot1xMIBGroups=alvarionDeviceDot1xMIBGroups, alvarionDeviceDot1xMIBCompliance=alvarionDeviceDot1xMIBCompliance, coDev1xStaUserName=coDev1xStaUserName, coDev1xStaBackendResponses=coDev1xStaBackendResponses, coDev1xStaBackendChallenges=coDev1xStaBackendChallenges, coDev1xStaBackendAuthFails=coDev1xStaBackendAuthFails, coDeviceDot1xStatusGroup=coDeviceDot1xStatusGroup, coDeviceDot1xStatsEntry=coDeviceDot1xStatsEntry, alvarionDeviceDot1xStatsMIBGroup=alvarionDeviceDot1xStatsMIBGroup, coDeviceDot1xStatusTable=coDeviceDot1xStatusTable, coDev1xStaTerminateCause=coDev1xStaTerminateCause, coDev1xStaEapolRxFrame=coDev1xStaEapolRxFrame, coDev1xStaBackendAuthSuccesses=coDev1xStaBackendAuthSuccesses, coDev1xStaPaeState=coDev1xStaPaeState, coDev1xStaMacAddress=coDev1xStaMacAddress, coDev1xStaPortStatus=coDev1xStaPortStatus, coDev1xStaIndex=coDev1xStaIndex, coDev1xStaEapolTxFrame=coDev1xStaEapolTxFrame, coDeviceDot1xConfigGroup=coDeviceDot1xConfigGroup, PYSNMP_MODULE_ID=alvarionDeviceDot1xMIB, alvarionDeviceDot1xStatusMIBGroup=alvarionDeviceDot1xStatusMIBGroup, coDeviceDot1xStatsGroup=coDeviceDot1xStatsGroup, alvarionDeviceDot1xMIB=alvarionDeviceDot1xMIB, coDeviceDot1xStatusEntry=coDeviceDot1xStatusEntry, coDev1xStaSessionTime=coDev1xStaSessionTime, coDeviceDot1xStatsTable=coDeviceDot1xStatsTable, alvarionDeviceDot1xMIBObjects=alvarionDeviceDot1xMIBObjects, alvarionDeviceDot1xMIBCompliances=alvarionDeviceDot1xMIBCompliances, alvarionDeviceDot1xMIBConformance=alvarionDeviceDot1xMIBConformance)
