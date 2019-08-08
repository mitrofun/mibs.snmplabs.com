#
# PySNMP MIB module SEC-FLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SEC-FLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
nbSwitchG1, = mibBuilder.importSymbols("NBASE-G1-MIB", "nbSwitchG1")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter32, NotificationType, Gauge32, MibIdentifier, enterprises, NotificationType, ModuleIdentity, IpAddress, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "enterprises", "NotificationType", "ModuleIdentity", "IpAddress", "iso", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbsAccelerouter = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10))
nbsArSecFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8))
nbsArSecFlowTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1), )
if mibBuilder.loadTexts: nbsArSecFlowTable.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowTable.setDescription('.')
nbsArSecFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1), ).setIndexNames((0, "SEC-FLOW-MIB", "nbsArSecFlowIndex"))
if mibBuilder.loadTexts: nbsArSecFlowEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowEntry.setDescription('.')
nbsArSecFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowIndex.setDescription('.')
nbsArSecFlowValid = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowValid.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowValid.setDescription('.')
nbsArSecFlowState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowState.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowState.setDescription('.')
nbsArSecFlowLastUsedTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowLastUsedTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowLastUsedTimestamp.setDescription('.')
nbsArSecFlowServTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowServTypes.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowServTypes.setDescription('.')
nbsArSecFlowServId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowServId.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowServId.setDescription('.')
nbsArFlowID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowID.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowID.setDescription('.')
nbsArFlowQoSSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowQoSSpec.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowQoSSpec.setDescription('Type of quality of service supplied.')
nbsArSecFlowNumOfServices = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowNumOfServices.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowNumOfServices.setDescription('The number of service specs defined.')
nbsArSecFlowDriverData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowDriverData.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowDriverData.setDescription('.')
nbsArSecFlowActions = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowActions.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowActions.setDescription('.')
nbsArSecFlowCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 12), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowCounters.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowCounters.setDescription('.')
nbsArSecFlowAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("add", 2), ("delete", 3), ("modify", 4), ("activate", 5), ("deactivate", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowAdminStatus.setDescription('What action to perform.')
nbsArFlowServiceSpecTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2), )
if mibBuilder.loadTexts: nbsArFlowServiceSpecTable.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecTable.setDescription('Specific service data entries attached to each flow entry.')
nbsArFlowServiceSpecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1), ).setIndexNames((0, "SEC-FLOW-MIB", "nbsArFlowServiceFlowIndex"), (0, "SEC-FLOW-MIB", "nbsArFlowServiceSpecsServiceId"))
if mibBuilder.loadTexts: nbsArFlowServiceSpecEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecEntry.setDescription('.')
nbsArFlowServiceFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceFlowIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceFlowIndex.setDescription('.')
nbsArFlowServiceSpecsServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceId.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceId.setDescription('.')
nbsArFlowServiceSpecsServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceType.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceType.setDescription('.')
nbsArFlowServiceSpecsServiceFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceFlowIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsServiceFlowIndex.setDescription("A reference to the service's table (installed by the service).")
nbsArFlowServiceSpecsFlowIDExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowIDExtension.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowIDExtension.setDescription('.')
nbsArFlowServiceSpecsFlowModifier = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowModifier.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowModifier.setDescription('.')
nbsArFlowServiceSpecsFlowSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowSpec.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsFlowSpec.setDescription('.')
nbsArFlowServiceSpecsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("add", 2), ("delete", 3), ("modify", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServiceSpecsAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServiceSpecsAdminStatus.setDescription('The action to perform.')
nbsArFlowServicePortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3), )
if mibBuilder.loadTexts: nbsArFlowServicePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServicePortTable.setDescription('.')
nbsArFlowServicePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1), ).setIndexNames((0, "SEC-FLOW-MIB", "nbsArFlowServicePortNumber"))
if mibBuilder.loadTexts: nbsArFlowServicePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServicePortEntry.setDescription('.')
nbsArFlowServicePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServicePortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServicePortNumber.setDescription('The port number for which the configuration relates. ')
nbsArFlowServicePortData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServicePortData.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServicePortData.setDescription('The data describing port attributes. ')
nbsArFlowServicePortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("add", 2), ("delete", 3), ("modify", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArFlowServicePortAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArFlowServicePortAdminStatus.setDescription('Port configuration status.')
nbsArSecFlowFwdStatus = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 8, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsArSecFlowFwdStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nbsArSecFlowFwdStatus.setDescription('.')
mibBuilder.exportSymbols("SEC-FLOW-MIB", nbsArSecFlow=nbsArSecFlow, nbsArFlowServiceSpecTable=nbsArFlowServiceSpecTable, nbsArFlowServiceSpecsFlowSpec=nbsArFlowServiceSpecsFlowSpec, nbsArSecFlowTable=nbsArSecFlowTable, nbsArFlowServicePortNumber=nbsArFlowServicePortNumber, MacAddress=MacAddress, nbsArFlowServiceSpecsServiceFlowIndex=nbsArFlowServiceSpecsServiceFlowIndex, nbsArFlowQoSSpec=nbsArFlowQoSSpec, nbsArFlowServicePortTable=nbsArFlowServicePortTable, nbsArSecFlowIndex=nbsArSecFlowIndex, nbsArFlowServiceSpecEntry=nbsArFlowServiceSpecEntry, nbsArSecFlowDriverData=nbsArSecFlowDriverData, nbsAccelerouter=nbsAccelerouter, nbsArFlowServiceSpecsFlowModifier=nbsArFlowServiceSpecsFlowModifier, nbsArSecFlowEntry=nbsArSecFlowEntry, nbsArFlowServicePortEntry=nbsArFlowServicePortEntry, nbsArFlowServiceSpecsFlowIDExtension=nbsArFlowServiceSpecsFlowIDExtension, nbsArSecFlowNumOfServices=nbsArSecFlowNumOfServices, nbsArSecFlowCounters=nbsArSecFlowCounters, nbsArSecFlowServId=nbsArSecFlowServId, nbsArSecFlowState=nbsArSecFlowState, nbsArFlowServiceFlowIndex=nbsArFlowServiceFlowIndex, nbsArFlowServicePortAdminStatus=nbsArFlowServicePortAdminStatus, nbsArSecFlowLastUsedTimestamp=nbsArSecFlowLastUsedTimestamp, nbsArFlowServiceSpecsServiceId=nbsArFlowServiceSpecsServiceId, nbsArFlowServiceSpecsAdminStatus=nbsArFlowServiceSpecsAdminStatus, nbsArSecFlowFwdStatus=nbsArSecFlowFwdStatus, nbsArFlowServicePortData=nbsArFlowServicePortData, nbsArSecFlowAdminStatus=nbsArSecFlowAdminStatus, nbsArSecFlowServTypes=nbsArSecFlowServTypes, nbsArSecFlowActions=nbsArSecFlowActions, nbSwitchG1Il=nbSwitchG1Il, nbsArSecFlowValid=nbsArSecFlowValid, nbsArFlowServiceSpecsServiceType=nbsArFlowServiceSpecsServiceType, nbsArFlowID=nbsArFlowID)