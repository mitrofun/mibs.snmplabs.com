#
# PySNMP MIB module PROXDBEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PROXDBEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:42:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
proxDbExt, = mibBuilder.importSymbols("APENT-MIB", "proxDbExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, Unsigned32, ObjectIdentity, Counter32, NotificationType, Counter64, Bits, MibIdentifier, ModuleIdentity, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter32", "NotificationType", "Counter64", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apProxDbExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 54, 1))
if mibBuilder.loadTexts: apProxDbExtMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: apProxDbExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apProxDbExtMib.setContactInfo(' Customer Support Postal: ArrowPoint Communications, Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978 206 3000 E-Mail: mibsupport@arrowpoint.com')
if mibBuilder.loadTexts: apProxDbExtMib.setDescription('The MIB module used to describe the ArrowPoint Communications Tiered Proximity Database functionality. This MIB contains all configuration, statistic, and metric objects. ')
apProxDbTTLProbed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 54, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProxDbTTLProbed.setStatus('current')
if mibBuilder.loadTexts: apProxDbTTLProbed.setDescription('This object controls the response TTL associated with probed blocks')
apProxDbTTLAssigned = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 54, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProxDbTTLAssigned.setStatus('current')
if mibBuilder.loadTexts: apProxDbTTLAssigned.setDescription('This object controls the response TTL associated with assigned blocks')
apProxDb8StatTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 6), )
if mibBuilder.loadTexts: apProxDb8StatTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb8StatTable.setDescription('This table is used to expose the /8 database statistics')
apProxDb8StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx8StatIpAddress"))
if mibBuilder.loadTexts: apProxDb8StatEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb8StatEntry.setDescription('')
apProx8StatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8StatIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx8StatIpAddress.setDescription('The IP address associated with this /8 database entry')
apProx8StatHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8StatHitCount.setStatus('current')
if mibBuilder.loadTexts: apProx8StatHitCount.setDescription('The number of hits on this /8 database entry. This is an aggregation of all hits occuring within the address space encompassed by this /8 entry.')
apProx8StatAdvMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8StatAdvMask.setStatus('current')
if mibBuilder.loadTexts: apProx8StatAdvMask.setDescription('The state of advertisement of entries contained under this /8. Each bit corresponds to a zone index, bit 0 - zone 0, bit 1 - zone 1. When the bit is CLR all entries contained under this /8 are synchronized. When the bit is SET entries exist under this /8 that are NOT synchronized.')
apProxDb16StatTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 7), )
if mibBuilder.loadTexts: apProxDb16StatTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb16StatTable.setDescription('This table is used to expose the /16 database statistics')
apProxDb16StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx16StatIpAddress"))
if mibBuilder.loadTexts: apProxDb16StatEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb16StatEntry.setDescription('')
apProx16StatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16StatIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx16StatIpAddress.setDescription('The IP address associated with this /16 database entry')
apProx16StatHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16StatHitCount.setStatus('current')
if mibBuilder.loadTexts: apProx16StatHitCount.setDescription('The number of hits on this /16 database entry. This is an aggregation of all hits occuring within the address space encompassed by this /16 entry.')
apProx16StatAdvMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16StatAdvMask.setStatus('current')
if mibBuilder.loadTexts: apProx16StatAdvMask.setDescription('The state of advertisement of entries contained under this /16. Each bit corresponds to a zone index, bit 0 - zone 0, bit 1 - zone 1. When the bit is CLR all entries contained under this /16 are synchronized. When the bit is SET entries exist under this /16 that are NOT synchronized.')
apProxDb24StatTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 8), )
if mibBuilder.loadTexts: apProxDb24StatTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb24StatTable.setDescription('This table is used to expose the /24 database statistics')
apProxDb24StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx24StatIpAddress"))
if mibBuilder.loadTexts: apProxDb24StatEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb24StatEntry.setDescription('')
apProx24StatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24StatIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx24StatIpAddress.setDescription('The IP address associated with this /24 database entry')
apProx24StatHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24StatHitCount.setStatus('current')
if mibBuilder.loadTexts: apProx24StatHitCount.setDescription('The number of hits on this /24 database entry. This is an aggregation of all hits occuring within the address space encompassed by this /24 entry.')
apProx24StatAdvMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24StatAdvMask.setStatus('current')
if mibBuilder.loadTexts: apProx24StatAdvMask.setDescription('The state of advertisement of entries contained under this /24. Each bit corresponds to a zone index, bit 0 - zone 0, bit 1 - zone 1. When the bit is SET all entries contained under this /24 are synchronized. When the bit is CLEAR entries exist under this /24 that are NOT synchronized.')
apProxDbVplStatTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9), )
if mibBuilder.loadTexts: apProxDbVplStatTable.setStatus('current')
if mibBuilder.loadTexts: apProxDbVplStatTable.setDescription('This table is used to expose the /Vpl database statistics')
apProxDbVplStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProxVplStatIpAddress"), (0, "PROXDBEXT-MIB", "apProxVplStatIpPrefix"))
if mibBuilder.loadTexts: apProxDbVplStatEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDbVplStatEntry.setDescription('')
apProxVplStatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplStatIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProxVplStatIpAddress.setDescription('The IP address associated with this /Vpl database entry')
apProxVplStatIpPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplStatIpPrefix.setStatus('current')
if mibBuilder.loadTexts: apProxVplStatIpPrefix.setDescription('The IP prefix associated with this /Vpl database entry')
apProxVplStatHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplStatHitCount.setStatus('current')
if mibBuilder.loadTexts: apProxVplStatHitCount.setDescription('The number of hits on this /Vpl database entry. This is an aggregation of all hits occuring within the address space encompassed by this /Vpl entry.')
apProxVplStatAdvMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplStatAdvMask.setStatus('current')
if mibBuilder.loadTexts: apProxVplStatAdvMask.setDescription('The state of advertisement of entries contained under this /Vpl. Each bit corresponds to a zone index, bit 0 - zone 0, bit 1 - zone 1. When the bit is SET all entries contained under this /Vpl are synchronized. When the bit is CLEAR entries exist under this /Vpl that are NOT synchronized.')
apProxDb8MetricTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 10), )
if mibBuilder.loadTexts: apProxDb8MetricTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb8MetricTable.setDescription('This database is used to expose the /8 database metrics')
apProxDb8MetricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx8MetricIpAddress"), (0, "PROXDBEXT-MIB", "apProx8MetricZoneIndex"))
if mibBuilder.loadTexts: apProxDb8MetricEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb8MetricEntry.setDescription('')
apProx8MetricIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8MetricIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx8MetricIpAddress.setDescription('The IP address associated with this /8 database entry')
apProx8MetricZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8MetricZoneIndex.setStatus('current')
if mibBuilder.loadTexts: apProx8MetricZoneIndex.setDescription('The zone index associated with this /8 database entry')
apProx8MetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx8MetricValue.setStatus('current')
if mibBuilder.loadTexts: apProx8MetricValue.setDescription('The metric associated with this /8 database entry')
apProxDb16MetricTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 11), )
if mibBuilder.loadTexts: apProxDb16MetricTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb16MetricTable.setDescription('This database is used to expose the /16 database metrics')
apProxDb16MetricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx16MetricIpAddress"), (0, "PROXDBEXT-MIB", "apProx16MetricZoneIndex"))
if mibBuilder.loadTexts: apProxDb16MetricEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb16MetricEntry.setDescription('')
apProx16MetricIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16MetricIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx16MetricIpAddress.setDescription('The IP address associated with this /16 database entry')
apProx16MetricZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16MetricZoneIndex.setStatus('current')
if mibBuilder.loadTexts: apProx16MetricZoneIndex.setDescription('The zone index associated with this /16 database entry')
apProx16MetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx16MetricValue.setStatus('current')
if mibBuilder.loadTexts: apProx16MetricValue.setDescription('The metric associated with this /16 database entry')
apProxDb24MetricTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 12), )
if mibBuilder.loadTexts: apProxDb24MetricTable.setStatus('current')
if mibBuilder.loadTexts: apProxDb24MetricTable.setDescription('This table is used to expose the /24 database metrics')
apProxDb24MetricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProx24MetricIpAddress"), (0, "PROXDBEXT-MIB", "apProx24MetricZoneIndex"))
if mibBuilder.loadTexts: apProxDb24MetricEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDb24MetricEntry.setDescription('')
apProx24MetricIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24MetricIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProx24MetricIpAddress.setDescription('The IP address associated with this /24 database entry')
apProx24MetricZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24MetricZoneIndex.setStatus('current')
if mibBuilder.loadTexts: apProx24MetricZoneIndex.setDescription('The zone index associated with this /24 database entry')
apProx24MetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProx24MetricValue.setStatus('current')
if mibBuilder.loadTexts: apProx24MetricValue.setDescription('The metric associated with this /24 database entry')
apProxDbVplMetricTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13), )
if mibBuilder.loadTexts: apProxDbVplMetricTable.setStatus('current')
if mibBuilder.loadTexts: apProxDbVplMetricTable.setDescription('This table is used to expose the /Vpl database metrics')
apProxDbVplMetricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1), ).setIndexNames((0, "PROXDBEXT-MIB", "apProxVplMetricIpAddress"), (0, "PROXDBEXT-MIB", "apProxVplMetricIpPrefix"), (0, "PROXDBEXT-MIB", "apProxVplMetricZoneIndex"))
if mibBuilder.loadTexts: apProxDbVplMetricEntry.setStatus('current')
if mibBuilder.loadTexts: apProxDbVplMetricEntry.setDescription('')
apProxVplMetricIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplMetricIpAddress.setStatus('current')
if mibBuilder.loadTexts: apProxVplMetricIpAddress.setDescription('The IP address associated with this /Vpl database entry')
apProxVplMetricIpPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplMetricIpPrefix.setStatus('current')
if mibBuilder.loadTexts: apProxVplMetricIpPrefix.setDescription('The IP prefix associated with this /Vpl database entry')
apProxVplMetricZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplMetricZoneIndex.setStatus('current')
if mibBuilder.loadTexts: apProxVplMetricZoneIndex.setDescription('The zone index associated with this /Vpl database entry')
apProxVplMetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProxVplMetricValue.setStatus('current')
if mibBuilder.loadTexts: apProxVplMetricValue.setDescription('The metric associated with this /Vpl database entry')
mibBuilder.exportSymbols("PROXDBEXT-MIB", apProxVplMetricIpAddress=apProxVplMetricIpAddress, apProx16MetricValue=apProx16MetricValue, apProxDbVplStatTable=apProxDbVplStatTable, apProx16MetricZoneIndex=apProx16MetricZoneIndex, apProxDb24MetricEntry=apProxDb24MetricEntry, apProxDb8MetricTable=apProxDb8MetricTable, apProx8StatHitCount=apProx8StatHitCount, apProx8StatIpAddress=apProx8StatIpAddress, apProxDb16StatTable=apProxDb16StatTable, apProxDbExtMib=apProxDbExtMib, apProx8StatAdvMask=apProx8StatAdvMask, apProxVplStatIpPrefix=apProxVplStatIpPrefix, apProxDb16MetricTable=apProxDb16MetricTable, apProxVplMetricZoneIndex=apProxVplMetricZoneIndex, apProxDb16MetricEntry=apProxDb16MetricEntry, apProx24MetricValue=apProx24MetricValue, apProx8MetricZoneIndex=apProx8MetricZoneIndex, apProx24StatIpAddress=apProx24StatIpAddress, apProx24MetricZoneIndex=apProx24MetricZoneIndex, apProxDb24StatEntry=apProxDb24StatEntry, apProxDbVplMetricEntry=apProxDbVplMetricEntry, apProx16StatHitCount=apProx16StatHitCount, apProxVplStatAdvMask=apProxVplStatAdvMask, apProxDb24StatTable=apProxDb24StatTable, apProx16StatIpAddress=apProx16StatIpAddress, apProx24MetricIpAddress=apProx24MetricIpAddress, apProxDbTTLProbed=apProxDbTTLProbed, apProxDb8StatEntry=apProxDb8StatEntry, apProx16MetricIpAddress=apProx16MetricIpAddress, apProxDb8StatTable=apProxDb8StatTable, apProxVplMetricIpPrefix=apProxVplMetricIpPrefix, apProxDbTTLAssigned=apProxDbTTLAssigned, apProx8MetricValue=apProx8MetricValue, apProxDbVplMetricTable=apProxDbVplMetricTable, apProxDbVplStatEntry=apProxDbVplStatEntry, apProx16StatAdvMask=apProx16StatAdvMask, apProxVplStatIpAddress=apProxVplStatIpAddress, apProxVplMetricValue=apProxVplMetricValue, PYSNMP_MODULE_ID=apProxDbExtMib, apProxDb24MetricTable=apProxDb24MetricTable, apProx24StatHitCount=apProx24StatHitCount, apProx24StatAdvMask=apProx24StatAdvMask, apProxDb16StatEntry=apProxDb16StatEntry, apProxVplStatHitCount=apProxVplStatHitCount, apProxDb8MetricEntry=apProxDb8MetricEntry, apProx8MetricIpAddress=apProx8MetricIpAddress)