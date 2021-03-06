#
# PySNMP MIB module NIMBLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NIMBLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:21:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, IpAddress, iso, Counter32, Bits, NotificationType, Gauge32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "iso", "Counter32", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
nimble = ModuleIdentity((1, 3, 6, 1, 4, 1, 37447))
nimble.setRevisions(('2012-08-31 00:00', '2012-06-12 00:00', '2011-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nimble.setRevisionsDescriptions(('Nimble Storage 2.0.3.0 MIB', 'Nimble Storage 1.3.0.0 MIB', 'Initial revision',))
if mibBuilder.loadTexts: nimble.setLastUpdated('201208310000Z')
if mibBuilder.loadTexts: nimble.setOrganization('Nimble Storage, Inc.')
if mibBuilder.loadTexts: nimble.setContactInfo('Nimble Storage support@nimblestorage.com')
if mibBuilder.loadTexts: nimble.setDescription('SMI Information for Nimble')
variables = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 1))
volNumberOfVolumes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volNumberOfVolumes.setStatus('obsolete')
if mibBuilder.loadTexts: volNumberOfVolumes.setDescription('This variable has been obsoleted')
volTable = MibTable((1, 3, 6, 1, 4, 1, 37447, 1, 2), )
if mibBuilder.loadTexts: volTable.setStatus('current')
if mibBuilder.loadTexts: volTable.setDescription('Volume information table.')
volEntry = MibTableRow((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1), ).setIndexNames((0, "NIMBLE-MIB", "volIndex"))
if mibBuilder.loadTexts: volEntry.setStatus('current')
if mibBuilder.loadTexts: volEntry.setDescription('A row of volume information.')
volIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: volIndex.setStatus('current')
if mibBuilder.loadTexts: volIndex.setDescription('Volume Index.')
volID = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volID.setStatus('current')
if mibBuilder.loadTexts: volID.setDescription('Volume ID.')
volName = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volName.setStatus('current')
if mibBuilder.loadTexts: volName.setDescription('Volume Name.')
volSizeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volSizeLow.setStatus('current')
if mibBuilder.loadTexts: volSizeLow.setDescription('Maximum defined size of a volume in bytes - low order bytes.')
volSizeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volSizeHigh.setStatus('current')
if mibBuilder.loadTexts: volSizeHigh.setDescription('Maximum defined size of a volume in bytes - high order bytes.')
volUsageLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volUsageLow.setStatus('current')
if mibBuilder.loadTexts: volUsageLow.setDescription('Current number of bytes a volume is using - low order bytes.')
volUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volUsageHigh.setStatus('current')
if mibBuilder.loadTexts: volUsageHigh.setDescription('Current number of bytes a volume is using - high order bytes.')
volReserveLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volReserveLow.setStatus('current')
if mibBuilder.loadTexts: volReserveLow.setDescription('Number of bytes reserved for a volume - low order bytes.')
volReserveHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volReserveHigh.setStatus('current')
if mibBuilder.loadTexts: volReserveHigh.setDescription('Number of bytes reserved for a volume - high order bytes.')
volOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volOnline.setStatus('current')
if mibBuilder.loadTexts: volOnline.setDescription('Volume Online (true or false).')
volNumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volNumConnections.setStatus('current')
if mibBuilder.loadTexts: volNumConnections.setDescription('Number of iSCSI connections to the volume.')
volStatTimeEpochSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volStatTimeEpochSeconds.setStatus('current')
if mibBuilder.loadTexts: volStatTimeEpochSeconds.setDescription('Time at which the sample was taken, measured in seconds since UNIX epoch.')
volIoReads = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReads.setStatus('current')
if mibBuilder.loadTexts: volIoReads.setDescription('Total cumulative number of Read I/Os (sequential and random).')
volIoReadTimeMicrosec = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadTimeMicrosec.setStatus('current')
if mibBuilder.loadTexts: volIoReadTimeMicrosec.setDescription('Total cumulative time for Read operation (sequential and random).')
volIoReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadBytes.setStatus('current')
if mibBuilder.loadTexts: volIoReadBytes.setDescription('Total cumulative number of Read I/O bytes (sequential and random).')
volIoSeqReads = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqReads.setStatus('current')
if mibBuilder.loadTexts: volIoSeqReads.setDescription('Total Number of Sequential Read I/O operations.')
volIoSeqReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqReadBytes.setStatus('current')
if mibBuilder.loadTexts: volIoSeqReadBytes.setDescription('Total cumulative number of Sequential Read I/O bytes.')
volIoNonseqReadTotalHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadTotalHits.setStatus('current')
if mibBuilder.loadTexts: volIoNonseqReadTotalHits.setDescription('Total number of Nonsequential Read I/O hits (to Memory and SSD).')
volIoNonseqReadMemHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadMemHits.setStatus('current')
if mibBuilder.loadTexts: volIoNonseqReadMemHits.setDescription('Total number of Nonsequential Read I/O hits to Memory.')
volIoNonseqReadSSDHits = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoNonseqReadSSDHits.setStatus('current')
if mibBuilder.loadTexts: volIoNonseqReadSSDHits.setDescription('Total number of Nonsequential Read I/O hits to SSD.')
volIoReadLatency0uTo100u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency0uTo100u.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency0uTo100u.setDescription('Number of Read I/O operations with latency between 0 and 100 microseconds.')
volIoReadLatency100uTo200u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency100uTo200u.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency100uTo200u.setDescription('Number of Read I/O operations with latency between 100 and 200 microseconds.')
volIoReadLatency200uTo500u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency200uTo500u.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency200uTo500u.setDescription('Number of Read I/O operations with latency between 200 and 500 microseconds.')
volIoReadLatency500uTo1m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency500uTo1m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency500uTo1m.setDescription('Number of Read I/O operations with latency between 1/2 and 1 milliseconds.')
volIoReadLatency1mTo2m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency1mTo2m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency1mTo2m.setDescription('Number of Read I/O operations with latency between 1 and 2 milliseconds.')
volIoReadLatency2mTo5m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency2mTo5m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency2mTo5m.setDescription('Number of Read I/O operations with latency between 2 and 5 milliseconds.')
volIoReadLatency5mTo10m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency5mTo10m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency5mTo10m.setDescription('Number of Read I/O operations with latency between 5 and 10 milliseconds.')
volIoReadLatency10mTo20m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency10mTo20m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency10mTo20m.setDescription('Number of Read I/O operations with latency between 10 and 20 milliseconds.')
volIoReadLatency20mTo50m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency20mTo50m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency20mTo50m.setDescription('Number of Read I/O operations with latency between 20 and 50 milliseconds.')
volIoReadLatency50mTo100m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency50mTo100m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency50mTo100m.setDescription('Number of Read I/O operations with latency between 50 and 100 milliseconds.')
volIoReadLatency100mTo200m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency100mTo200m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency100mTo200m.setDescription('Number of Read I/O operations with latency between 100 and 200 milliseconds.')
volIoReadLatency200mTo500m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency200mTo500m.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency200mTo500m.setDescription('Number of Read I/O operations with latency between 200 and 500 milliseconds.')
volIoReadLatency500mTomax = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoReadLatency500mTomax.setStatus('current')
if mibBuilder.loadTexts: volIoReadLatency500mTomax.setDescription('Number of Read I/O operations with latency above 500 milliseconds.')
volIoWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWrites.setStatus('current')
if mibBuilder.loadTexts: volIoWrites.setDescription('Total cumulative number of Write I/Os.')
volIoWriteTimeMicrosec = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteTimeMicrosec.setStatus('current')
if mibBuilder.loadTexts: volIoWriteTimeMicrosec.setDescription('Total cumulative time for Write operation (sequential and random).')
volIoWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteBytes.setStatus('current')
if mibBuilder.loadTexts: volIoWriteBytes.setDescription('Total cumulative number of Write I/O bytes (sequential and random).')
volIoSeqWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqWrites.setStatus('current')
if mibBuilder.loadTexts: volIoSeqWrites.setDescription('Total Number of Sequential Write I/O operations.')
volIoSeqWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoSeqWriteBytes.setStatus('current')
if mibBuilder.loadTexts: volIoSeqWriteBytes.setDescription('Number of Sequential Write I/O bytes.')
volIoWriteLatency0uTo100u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency0uTo100u.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency0uTo100u.setDescription('Number of Write I/O operations with latency between 0 and 100 microseconds.')
volIoWriteLatency100uTo200u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency100uTo200u.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency100uTo200u.setDescription('Number of Write I/O operations with latency between 100 and 200 microseconds.')
volIoWriteLatency200uTo500u = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency200uTo500u.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency200uTo500u.setDescription('Number of Write I/O operations with latency between 200 and 500 microseconds.')
volIoWriteLatency500uTo1m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency500uTo1m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency500uTo1m.setDescription('Number of Write I/O operations with latency between 1/2 and 1 milliseconds.')
volIoWriteLatency1mTo2m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency1mTo2m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency1mTo2m.setDescription('Number of Write I/O operations with latency between 1 and 2 milliseconds.')
volIoWriteLatency2mTo5m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency2mTo5m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency2mTo5m.setDescription('Number of Write I/O operations with latency between 2 and 5 milliseconds.')
volIoWriteLatency5mTo10m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency5mTo10m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency5mTo10m.setDescription('Number of Write I/O operations with latency between 5 and 10 milliseconds.')
volIoWriteLatency10mTo20m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency10mTo20m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency10mTo20m.setDescription('Number of Write I/O operations with latency between 10 and 20 milliseconds.')
volIoWriteLatency20mTo50m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency20mTo50m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency20mTo50m.setDescription('Number of Write I/O operations with latency between 20 and 50 milliseconds.')
volIoWriteLatency50mTo100m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency50mTo100m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency50mTo100m.setDescription('Number of Write I/O operations with latency between 50 and 100 milliseconds.')
volIoWriteLatency100mTo200m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency100mTo200m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency100mTo200m.setDescription('Number of Write I/O operations with latency between 100 and 200 milliseconds.')
volIoWriteLatency200mTo500m = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency200mTo500m.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency200mTo500m.setDescription('Number of Write I/O operations with latency between 200 and 500 milliseconds.')
volIoWriteLatency500mTomax = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volIoWriteLatency500mTomax.setStatus('current')
if mibBuilder.loadTexts: volIoWriteLatency500mTomax.setDescription('Number of Write I/O operations with latency above 500 milliseconds.')
volDiskVolBytesUsedLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 52), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskVolBytesUsedLow.setStatus('current')
if mibBuilder.loadTexts: volDiskVolBytesUsedLow.setDescription('Total number of bytes used on disk for volumes - low order bytes.')
volDiskVolBytesUsedHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 53), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskVolBytesUsedHigh.setStatus('current')
if mibBuilder.loadTexts: volDiskVolBytesUsedHigh.setDescription('Total number of bytes used on disk for volumes - high order bytes.')
volDiskSnapBytesUsedLow = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskSnapBytesUsedLow.setStatus('current')
if mibBuilder.loadTexts: volDiskSnapBytesUsedLow.setDescription('Total number of bytes used on disk for snapshots - low order bytes.')
volDiskSnapBytesUsedHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 55), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volDiskSnapBytesUsedHigh.setStatus('current')
if mibBuilder.loadTexts: volDiskSnapBytesUsedHigh.setDescription('Total number of bytes used on disk for snapshots - high order bytes.')
globalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 1, 3))
statTimeEpochSeconds = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statTimeEpochSeconds.setStatus('current')
if mibBuilder.loadTexts: statTimeEpochSeconds.setDescription('Time at which the sample was taken, measured in seconds since UNIX epoch.')
ioReads = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReads.setStatus('current')
if mibBuilder.loadTexts: ioReads.setDescription('Total cumulative number of Read I/Os (sequential and random).')
ioSeqReads = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqReads.setStatus('current')
if mibBuilder.loadTexts: ioSeqReads.setDescription('Total cumulative number of Sequential Read I/Os.')
ioWrites = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWrites.setStatus('current')
if mibBuilder.loadTexts: ioWrites.setDescription('Total cumulative number of Write I/Os.')
ioSeqWrites = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqWrites.setStatus('current')
if mibBuilder.loadTexts: ioSeqWrites.setDescription('Total cumulative number of Sequential Write I/Os.')
ioReadTimeMicrosec = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReadTimeMicrosec.setStatus('current')
if mibBuilder.loadTexts: ioReadTimeMicrosec.setDescription('Total cumulative microseconds the system has spent processing Read I/Os. This includes system and disk latency, but not any network latency back to the initiator.')
ioWriteTimeMicrosec = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWriteTimeMicrosec.setStatus('current')
if mibBuilder.loadTexts: ioWriteTimeMicrosec.setDescription('Total cumulative microseconds the system has spent processing Write I/Os. This includes system and disk latency, but not any network latency back to the initiator.')
ioReadBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioReadBytes.setStatus('current')
if mibBuilder.loadTexts: ioReadBytes.setDescription('Total cumulative number of Read I/O bytes (sequential and random).')
ioSeqReadBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqReadBytes.setStatus('current')
if mibBuilder.loadTexts: ioSeqReadBytes.setDescription('Total cumulative number of Sequential Read I/O bytes.')
ioWriteBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioWriteBytes.setStatus('current')
if mibBuilder.loadTexts: ioWriteBytes.setDescription('Total cumulative number of Write I/O bytes (sequential and random).')
ioSeqWriteBytes = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioSeqWriteBytes.setStatus('current')
if mibBuilder.loadTexts: ioSeqWriteBytes.setDescription('Total cumulative number of Sequential Write I/O bytes.')
diskVolBytesUsedLow = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVolBytesUsedLow.setStatus('current')
if mibBuilder.loadTexts: diskVolBytesUsedLow.setDescription('Total number of bytes used on disk for volumes - low order bytes.')
diskVolBytesUsedHigh = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskVolBytesUsedHigh.setStatus('current')
if mibBuilder.loadTexts: diskVolBytesUsedHigh.setDescription('Total number of bytes used on disk for volumes - high order bytes.')
diskSnapBytesUsedLow = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSnapBytesUsedLow.setStatus('current')
if mibBuilder.loadTexts: diskSnapBytesUsedLow.setDescription('Total number of bytes used on disk for snapshots - low order bytes.')
diskSnapBytesUsedHigh = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSnapBytesUsedHigh.setStatus('current')
if mibBuilder.loadTexts: diskSnapBytesUsedHigh.setDescription('Total number of bytes used on disk for snapshots - high order bytes.')
ioNonseqReadHits = MibScalar((1, 3, 6, 1, 4, 1, 37447, 1, 3, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioNonseqReadHits.setStatus('current')
if mibBuilder.loadTexts: ioNonseqReadHits.setDescription('Total cumulative number of cache hits for Non-Sequential Read I/Os.')
arrays = MibIdentifier((1, 3, 6, 1, 4, 1, 37447, 3))
arrayEntry = MibScalar((1, 3, 6, 1, 4, 1, 37447, 3, 1), DisplayString())
if mibBuilder.loadTexts: arrayEntry.setStatus('current')
if mibBuilder.loadTexts: arrayEntry.setDescription('Nimble Array.')
mibBuilder.exportSymbols("NIMBLE-MIB", ioReadTimeMicrosec=ioReadTimeMicrosec, volIoReadLatency200mTo500m=volIoReadLatency200mTo500m, volID=volID, ioWrites=ioWrites, ioWriteTimeMicrosec=ioWriteTimeMicrosec, diskSnapBytesUsedHigh=diskSnapBytesUsedHigh, volDiskVolBytesUsedHigh=volDiskVolBytesUsedHigh, ioWriteBytes=ioWriteBytes, volIoWriteLatency100mTo200m=volIoWriteLatency100mTo200m, volIoWrites=volIoWrites, volIoReadBytes=volIoReadBytes, volIoReadLatency0uTo100u=volIoReadLatency0uTo100u, ioSeqReadBytes=ioSeqReadBytes, volIoWriteLatency50mTo100m=volIoWriteLatency50mTo100m, volIoWriteLatency200mTo500m=volIoWriteLatency200mTo500m, volDiskVolBytesUsedLow=volDiskVolBytesUsedLow, diskSnapBytesUsedLow=diskSnapBytesUsedLow, volIoSeqWrites=volIoSeqWrites, volNumConnections=volNumConnections, arrayEntry=arrayEntry, volOnline=volOnline, volIoSeqReads=volIoSeqReads, volIoWriteLatency500uTo1m=volIoWriteLatency500uTo1m, volIoWriteLatency5mTo10m=volIoWriteLatency5mTo10m, ioReadBytes=ioReadBytes, volStatTimeEpochSeconds=volStatTimeEpochSeconds, volIoReadLatency500uTo1m=volIoReadLatency500uTo1m, ioNonseqReadHits=ioNonseqReadHits, volIoReads=volIoReads, ioSeqWriteBytes=ioSeqWriteBytes, volIoWriteLatency200uTo500u=volIoWriteLatency200uTo500u, volSizeHigh=volSizeHigh, volIoReadLatency50mTo100m=volIoReadLatency50mTo100m, volIoWriteLatency2mTo5m=volIoWriteLatency2mTo5m, ioReads=ioReads, volUsageLow=volUsageLow, volIoReadLatency2mTo5m=volIoReadLatency2mTo5m, variables=variables, volIoReadLatency10mTo20m=volIoReadLatency10mTo20m, arrays=arrays, volIndex=volIndex, diskVolBytesUsedLow=diskVolBytesUsedLow, volIoReadLatency500mTomax=volIoReadLatency500mTomax, volIoWriteLatency0uTo100u=volIoWriteLatency0uTo100u, volDiskSnapBytesUsedHigh=volDiskSnapBytesUsedHigh, volTable=volTable, volIoWriteLatency500mTomax=volIoWriteLatency500mTomax, diskVolBytesUsedHigh=diskVolBytesUsedHigh, volIoNonseqReadSSDHits=volIoNonseqReadSSDHits, volIoSeqWriteBytes=volIoSeqWriteBytes, volIoWriteLatency20mTo50m=volIoWriteLatency20mTo50m, volIoWriteTimeMicrosec=volIoWriteTimeMicrosec, volIoWriteLatency10mTo20m=volIoWriteLatency10mTo20m, volReserveLow=volReserveLow, nimble=nimble, globalStats=globalStats, volIoWriteLatency100uTo200u=volIoWriteLatency100uTo200u, statTimeEpochSeconds=statTimeEpochSeconds, volIoReadLatency100mTo200m=volIoReadLatency100mTo200m, volUsageHigh=volUsageHigh, PYSNMP_MODULE_ID=nimble, volIoReadTimeMicrosec=volIoReadTimeMicrosec, ioSeqWrites=ioSeqWrites, volIoWriteBytes=volIoWriteBytes, volDiskSnapBytesUsedLow=volDiskSnapBytesUsedLow, volIoNonseqReadTotalHits=volIoNonseqReadTotalHits, ioSeqReads=ioSeqReads, volIoSeqReadBytes=volIoSeqReadBytes, volIoReadLatency100uTo200u=volIoReadLatency100uTo200u, volIoWriteLatency1mTo2m=volIoWriteLatency1mTo2m, volIoReadLatency200uTo500u=volIoReadLatency200uTo500u, volNumberOfVolumes=volNumberOfVolumes, volSizeLow=volSizeLow, volName=volName, volIoReadLatency1mTo2m=volIoReadLatency1mTo2m, volIoReadLatency5mTo10m=volIoReadLatency5mTo10m, volIoNonseqReadMemHits=volIoNonseqReadMemHits, volIoReadLatency20mTo50m=volIoReadLatency20mTo50m, volEntry=volEntry, volReserveHigh=volReserveHigh)
