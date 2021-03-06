#
# PySNMP MIB module IBM-FRAMERELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-FRAMERELAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
frCircuitDlci, frCircuitIfIndex = mibBuilder.importSymbols("RFC1315-MIB", "frCircuitDlci", "frCircuitIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, MibIdentifier, TimeTicks, iso, ObjectIdentity, IpAddress, NotificationType, Counter32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibmIROCfrcircuit = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5))
ibmframerelayPVCTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1), )
if mibBuilder.loadTexts: ibmframerelayPVCTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTable.setDescription('A table providing PVC information and the capabiilty to clear counters.')
ibmframerelayPVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1), ).setIndexNames((0, "RFC1315-MIB", "frCircuitIfIndex"), (0, "RFC1315-MIB", "frCircuitDlci"))
if mibBuilder.loadTexts: ibmframerelayPVCEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCEntry.setDescription('Entry identifying a particular permanent virtual circuit.')
ibmframerelayPVCCircName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCCircName.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCCircName.setDescription('The name string assigned to this PVC.')
ibmframerelayPVCTimesActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCTimesActive.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTimesActive.setDescription('The times this PVC entered active state as reported by frCircuitState.')
ibmframerelayPVCTimesInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCTimesInactive.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTimesInactive.setDescription('The times this PVC entered inactive state as reported by frCircuitState.')
ibmframerelayPVCTimesCongested = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCTimesCongested.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTimesCongested.setDescription('The times this PVC has become congested.')
ibmframerelayPVCTxQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCTxQueued.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTxQueued.setDescription('The current number of frames queued for transmission and waiting for space on the device transmit queue.')
ibmframerelayPVCTxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmframerelayPVCTxDropped.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCTxDropped.setDescription('The number of frames discarded because they could not be transmitted due to output queue overflow.')
ibmframerelayPVCClearAll = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmframerelayPVCClearAll.setStatus('mandatory')
if mibBuilder.loadTexts: ibmframerelayPVCClearAll.setDescription('When SET to a value of 0, all the frame relay counters for this PVC are cleared. When READ, this object always returns a value of 0, since this object is intended as a trigger, rather than providing information.')
mibBuilder.exportSymbols("IBM-FRAMERELAY-MIB", ibmframerelayPVCCircName=ibmframerelayPVCCircName, ibmframerelayPVCTxQueued=ibmframerelayPVCTxQueued, ibmframerelayPVCEntry=ibmframerelayPVCEntry, ibmframerelayPVCTimesInactive=ibmframerelayPVCTimesInactive, ibmIROCfrcircuit=ibmIROCfrcircuit, ibmframerelayPVCTimesCongested=ibmframerelayPVCTimesCongested, ibmframerelayPVCTimesActive=ibmframerelayPVCTimesActive, ibmframerelayPVCTxDropped=ibmframerelayPVCTxDropped, ibmframerelayPVCClearAll=ibmframerelayPVCClearAll, ibmframerelayPVCTable=ibmframerelayPVCTable)
