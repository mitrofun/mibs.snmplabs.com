#
# PySNMP MIB module TPLINK-PORTLOOPBACKDETECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PORTLOOPBACKDETECTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ModuleIdentity, IpAddress, Counter32, Gauge32, ObjectIdentity, MibIdentifier, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ModuleIdentity", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkLoopbackDetectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 80))
tplinkLoopbackDetectionMIB.setRevisions(('2009-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkLoopbackDetectionMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkLoopbackDetectionMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkLoopbackDetectionMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkLoopbackDetectionMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkLoopbackDetectionMIB.setDescription('The config of loopback Detection.')
tplinkLoopbackDetectionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1))
tplinkLoopbackDetectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 80, 2))
loopbackStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 80, 2, 1))
if mibBuilder.loadTexts: loopbackStatusChange.setStatus('current')
if mibBuilder.loadTexts: loopbackStatusChange.setDescription('When loopbackDetection is enabled ,A loopback detection notification is sent while port loop status is changed.')
loopbackDetectionEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionEnable.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionEnable.setDescription('Select Enable/Disable LOOPBACK detection function globally on the Switch. 0. disable 1. enable')
loopbackDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionInterval.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionInterval.setDescription('The interval time of loopback detection')
loopbackDetectionRecoveryTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionRecoveryTime.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionRecoveryTime.setDescription('The recovery time of loopback detection')
loopbackDetectionCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4), )
if mibBuilder.loadTexts: loopbackDetectionCtrlTable.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionCtrlTable.setDescription('A list of port loopback detection.')
loopbackDetectionCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: loopbackDetectionCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionCtrlEntry.setDescription('The entry of the port loopback detection list .')
loopbackDetectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopbackDetectionPort.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionPort.setDescription('Display port number')
loopbackDetectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionState.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionState.setDescription('The state of the port.')
loopbackDetectionProcessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("alert", 0), ("portbased", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionProcessMode.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionProcessMode.setDescription('The process mode of the port.')
loopbackDetectionRecoverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("auto", 0), ("manual", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionRecoverMode.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionRecoverMode.setDescription('The recover mode of the port.')
loopbackDetectionLoopState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopbackDetectionLoopState.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionLoopState.setDescription('The loop state of the port.')
loopbackDetectionBlockState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopbackDetectionBlockState.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionBlockState.setDescription('The block state of the port.')
loopbackDetectionLagState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loopbackDetectionLagState.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionLagState.setDescription('The LAG of the port.')
loopbackDetectionRecoverPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 80, 1, 4, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loopbackDetectionRecoverPort.setStatus('current')
if mibBuilder.loadTexts: loopbackDetectionRecoverPort.setDescription('You can recover the block port with this.')
mibBuilder.exportSymbols("TPLINK-PORTLOOPBACKDETECTION-MIB", loopbackStatusChange=loopbackStatusChange, loopbackDetectionLagState=loopbackDetectionLagState, loopbackDetectionEnable=loopbackDetectionEnable, tplinkLoopbackDetectionNotifications=tplinkLoopbackDetectionNotifications, tplinkLoopbackDetectionMIBObjects=tplinkLoopbackDetectionMIBObjects, loopbackDetectionPort=loopbackDetectionPort, loopbackDetectionState=loopbackDetectionState, loopbackDetectionRecoveryTime=loopbackDetectionRecoveryTime, loopbackDetectionCtrlEntry=loopbackDetectionCtrlEntry, loopbackDetectionLoopState=loopbackDetectionLoopState, loopbackDetectionProcessMode=loopbackDetectionProcessMode, loopbackDetectionRecoverPort=loopbackDetectionRecoverPort, loopbackDetectionCtrlTable=loopbackDetectionCtrlTable, tplinkLoopbackDetectionMIB=tplinkLoopbackDetectionMIB, loopbackDetectionRecoverMode=loopbackDetectionRecoverMode, PYSNMP_MODULE_ID=tplinkLoopbackDetectionMIB, loopbackDetectionInterval=loopbackDetectionInterval, loopbackDetectionBlockState=loopbackDetectionBlockState)
