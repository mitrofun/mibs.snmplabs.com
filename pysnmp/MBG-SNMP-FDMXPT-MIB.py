#
# PySNMP MIB module MBG-SNMP-FDMXPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MBG-SNMP-FDMXPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:00:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, TimeTicks, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Unsigned32, Counter64, IpAddress, Integer32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "TimeTicks", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "IpAddress", "Integer32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mbgFDM = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597, 15))
mbgFDM.setRevisions(('2012-01-25 00:00', '2006-01-20 00:00',))
if mibBuilder.loadTexts: mbgFDM.setLastUpdated('201201250000Z')
if mibBuilder.loadTexts: mbgFDM.setOrganization('www.meinberg.de')
mbgFDMData = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 2))
mbgFDMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 3))
mbgFDMMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMMode.setStatus('current')
mbgFDMModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMModeVal.setStatus('current')
mbgFDMFrequency = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFrequency.setStatus('current')
mbgFDMFrequencyVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFrequencyVal.setStatus('current')
mbgFDMRefTime = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMRefTime.setStatus('current')
mbgFDMPLTime = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMPLTime.setStatus('current')
mbgFDMFreqDev = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFreqDev.setStatus('current')
mbgFDMFreqDevVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFreqDevVal.setStatus('current')
mbgFDMTimeDev = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMTimeDev.setStatus('current')
mbgFDMTimeDevVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMTimeDevVal.setStatus('current')
mbgFDMErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMErrorStatus.setStatus('current')
mbgFDMTrapInternalError = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 1))
if mibBuilder.loadTexts: mbgFDMTrapInternalError.setStatus('current')
mbgFDMTrapNoTimeString = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 2))
if mibBuilder.loadTexts: mbgFDMTrapNoTimeString.setStatus('current')
mbgFDMTrapNo10Mhz = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 3))
if mibBuilder.loadTexts: mbgFDMTrapNo10Mhz.setStatus('current')
mbgFDMTrapNoPPS = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 4))
if mibBuilder.loadTexts: mbgFDMTrapNoPPS.setStatus('current')
mbgFDMTrapNoPowerline = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 5))
if mibBuilder.loadTexts: mbgFDMTrapNoPowerline.setStatus('current')
mbgFDMTrapTimeDeviationOverflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 6))
if mibBuilder.loadTexts: mbgFDMTrapTimeDeviationOverflow.setStatus('current')
mbgFDMTrapA1Overflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 7))
if mibBuilder.loadTexts: mbgFDMTrapA1Overflow.setStatus('current')
mbgFDMTrapA2Overflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 8))
if mibBuilder.loadTexts: mbgFDMTrapA2Overflow.setStatus('current')
mbgFDMTrapFreqLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 9))
if mibBuilder.loadTexts: mbgFDMTrapFreqLimitExceeded.setStatus('current')
mbgFDMXPTReboot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 10))
if mibBuilder.loadTexts: mbgFDMXPTReboot.setStatus('current')
mbgFDMNormalOperation = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 99))
if mibBuilder.loadTexts: mbgFDMNormalOperation.setStatus('current')
mbgFDMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90))
mbgFDMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90, 1))
mbgFDMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2))
mbgFDMCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5597, 15, 90, 1, 1)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMObjectsGroup"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMCompliance = mbgFDMCompliance.setStatus('current')
mbgFDMObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 1)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMMode"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMModeVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequency"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequencyVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMRefTime"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMPLTime"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDev"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDevVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDev"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDevVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMErrorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMObjectsGroup = mbgFDMObjectsGroup.setStatus('current')
mbgFDMTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 2)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapInternalError"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoTimeString"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNo10Mhz"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPPS"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPowerline"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapTimeDeviationOverflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA1Overflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA2Overflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapFreqLimitExceeded"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMXPTReboot"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMNormalOperation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMTrapsGroup = mbgFDMTrapsGroup.setStatus('current')
mibBuilder.exportSymbols("MBG-SNMP-FDMXPT-MIB", mbgFDMFrequency=mbgFDMFrequency, mbgFDMMode=mbgFDMMode, mbgFDMNormalOperation=mbgFDMNormalOperation, mbgFDMTrapA2Overflow=mbgFDMTrapA2Overflow, mbgFDMErrorStatus=mbgFDMErrorStatus, mbgFDMModeVal=mbgFDMModeVal, mbgFDMXPTReboot=mbgFDMXPTReboot, mbgFDMTraps=mbgFDMTraps, mbgFDMFreqDevVal=mbgFDMFreqDevVal, mbgFDMTrapFreqLimitExceeded=mbgFDMTrapFreqLimitExceeded, PYSNMP_MODULE_ID=mbgFDM, mbgFDMTrapNoTimeString=mbgFDMTrapNoTimeString, mbgFDMTrapNoPPS=mbgFDMTrapNoPPS, mbgFDMCompliances=mbgFDMCompliances, mbgFDMCompliance=mbgFDMCompliance, mbgFDMTrapsGroup=mbgFDMTrapsGroup, mbgFDMTrapA1Overflow=mbgFDMTrapA1Overflow, mbgFDMTrapNoPowerline=mbgFDMTrapNoPowerline, mbgFDM=mbgFDM, mbgFDMData=mbgFDMData, mbgFDMTrapInternalError=mbgFDMTrapInternalError, mbgFDMTrapTimeDeviationOverflow=mbgFDMTrapTimeDeviationOverflow, mbgFDMTrapNo10Mhz=mbgFDMTrapNo10Mhz, mbgFDMTimeDevVal=mbgFDMTimeDevVal, mbgFDMPLTime=mbgFDMPLTime, mbgFDMGroups=mbgFDMGroups, mbgFDMTimeDev=mbgFDMTimeDev, mbgFDMConformance=mbgFDMConformance, mbgFDMFrequencyVal=mbgFDMFrequencyVal, mbgFDMObjectsGroup=mbgFDMObjectsGroup, mbgFDMFreqDev=mbgFDMFreqDev, mbgFDMRefTime=mbgFDMRefTime)
