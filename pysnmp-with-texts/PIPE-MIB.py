#
# PySNMP MIB module PIPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PIPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
neStatistics, = mibBuilder.importSymbols("NE-STAT-MIB", "neStatistics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, ObjectIdentity, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress, Bits, Counter64, NotificationType, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ObjectIdentity", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress", "Bits", "Counter64", "NotificationType", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pipeStatMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 2))
pipeStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1))
pipeStatTable = MibTable((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1), )
if mibBuilder.loadTexts: pipeStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: pipeStatTable.setDescription('A list of pipe entries.')
pipeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1), ).setIndexNames((0, "PIPE-MIB", "pipePosition"), (0, "PIPE-MIB", "pipeInstancePosition"))
if mibBuilder.loadTexts: pipeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pipeEntry.setDescription('A pipe entry contains statistical objects for one pipe.')
pipePosition = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePosition.setStatus('mandatory')
if mibBuilder.loadTexts: pipePosition.setDescription('Position of pipe in table')
pipeInstancePosition = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeInstancePosition.setStatus('mandatory')
if mibBuilder.loadTexts: pipeInstancePosition.setDescription('Position of pipe instance in group')
pipeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeName.setStatus('mandatory')
if mibBuilder.loadTexts: pipeName.setDescription('pipe name')
pipeByteCountIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountIn.setStatus('mandatory')
if mibBuilder.loadTexts: pipeByteCountIn.setDescription('Bytes in per pipe')
pipeByteCountOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountOut.setStatus('mandatory')
if mibBuilder.loadTexts: pipeByteCountOut.setDescription('Bytes out per pipe')
pipeByteCountTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeByteCountTotal.setStatus('mandatory')
if mibBuilder.loadTexts: pipeByteCountTotal.setDescription('Total Bytes per pipe')
pipeLiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeLiveConnections.setStatus('mandatory')
if mibBuilder.loadTexts: pipeLiveConnections.setDescription('Live Connections per pipe')
pipeNewConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipeNewConnections.setStatus('mandatory')
if mibBuilder.loadTexts: pipeNewConnections.setDescription('New Connections per pipe')
pipePacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsIn.setStatus('mandatory')
if mibBuilder.loadTexts: pipePacketsIn.setDescription('Packets in per pipe')
pipePacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsOut.setStatus('mandatory')
if mibBuilder.loadTexts: pipePacketsOut.setDescription('Packets out per pipe')
pipePacketsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pipePacketsTotal.setStatus('mandatory')
if mibBuilder.loadTexts: pipePacketsTotal.setDescription('Total Packets per pipe')
mibBuilder.exportSymbols("PIPE-MIB", pipeNewConnections=pipeNewConnections, pipePacketsTotal=pipePacketsTotal, pipeEntry=pipeEntry, pipePosition=pipePosition, pipeByteCountOut=pipeByteCountOut, pipeName=pipeName, pipeByteCountTotal=pipeByteCountTotal, pipePacketsIn=pipePacketsIn, pipeLiveConnections=pipeLiveConnections, pipeInstancePosition=pipeInstancePosition, pipeStat=pipeStat, pipeByteCountIn=pipeByteCountIn, pipeStatMIB=pipeStatMIB, pipeStatTable=pipeStatTable, pipePacketsOut=pipePacketsOut)