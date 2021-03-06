#
# PySNMP MIB module VMWARE-ENV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-ENV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter32, Bits, TimeTicks, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Counter64, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
vmwESX, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwESX")
vmwProductSpecific, vmwNotifications = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific", "vmwNotifications")
VmwSubsystemTypes, VmwCimName, VmwLongSnmpAdminString, VmwCIMAlertTypes, VmwSubsystemStatus, VmwCIMAlertFormat, VmwCIMSeverity = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwSubsystemTypes", "VmwCimName", "VmwLongSnmpAdminString", "VmwCIMAlertTypes", "VmwSubsystemStatus", "VmwCIMAlertFormat", "VmwCIMSeverity")
vmwEnvironmentalMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10))
vmwEnvironmentalMIB.setRevisions(('2010-05-12 00:00', '2008-10-30 00:00', '2007-12-27 00:00',))
if mibBuilder.loadTexts: vmwEnvironmentalMIB.setLastUpdated('201005120000Z')
if mibBuilder.loadTexts: vmwEnvironmentalMIB.setOrganization('VMware, Inc')
vmwEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 20))
vmwESXNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0))
if mibBuilder.loadTexts: vmwESXNotifications.setStatus('current')
vmwEnvNumber = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvNumber.setStatus('current')
vmwEnvLastChange = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvLastChange.setStatus('current')
vmwEnvTable = MibTable((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3), )
if mibBuilder.loadTexts: vmwEnvTable.setStatus('current')
vmwEnvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1), ).setIndexNames((0, "VMWARE-ENV-MIB", "vmwEnvIndex"))
if mibBuilder.loadTexts: vmwEnvEntry.setStatus('current')
vmwEnvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: vmwEnvIndex.setStatus('current')
vmwSubsystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 2), VmwSubsystemTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwSubsystemType.setStatus('current')
vmwHardwareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 3), VmwSubsystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwHardwareStatus.setStatus('current')
vmwEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEventDescription.setStatus('current')
vmwEnvHardwareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvHardwareTime.setStatus('current')
vmwEnvHardwareEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 0, 301)).setObjects(("VMWARE-ENV-MIB", "vmwSubsystemType"), ("VMWARE-ENV-MIB", "vmwHardwareStatus"), ("VMWARE-ENV-MIB", "vmwEventDescription"), ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
if mibBuilder.loadTexts: vmwEnvHardwareEvent.setStatus('deprecated')
vmwESXEnvHardwareEvent = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 301)).setObjects(("VMWARE-ENV-MIB", "vmwSubsystemType"), ("VMWARE-ENV-MIB", "vmwHardwareStatus"), ("VMWARE-ENV-MIB", "vmwEventDescription"), ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
if mibBuilder.loadTexts: vmwESXEnvHardwareEvent.setStatus('deprecated')
vmwEnvSource = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("sensors", 2), ("indications", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvSource.setStatus('current')
vmwEnvInIndications = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvInIndications.setStatus('current')
vmwEnvLastIn = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 102), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvLastIn.setStatus('current')
vmwEnvOutNotifications = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 103), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvOutNotifications.setStatus('current')
vmwEnvInErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 104), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvInErrs.setStatus('current')
vmwEnvIndOidErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 105), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvIndOidErrs.setStatus('current')
vmwEnvCvtValueErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 106), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvCvtValueErrs.setStatus('current')
vmwEnvCvtSyntaxErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 107), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvCvtSyntaxErrs.setStatus('current')
vmwEnvCvtOidErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 108), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvCvtOidErrs.setStatus('current')
vmwEnvGetClassErrs = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 109), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvGetClassErrs.setStatus('current')
vmwEnvPropertySkips = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 110), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvPropertySkips.setStatus('current')
vmwEnvIndicationSkips = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 20, 111), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwEnvIndicationSkips.setStatus('current')
vmwEnvCIM = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 30))
vmwEnvDescription = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 1), VmwLongSnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvDescription.setStatus('current')
vmwEnvEventTime = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvEventTime.setStatus('current')
vmwEnvIndicationTime = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvIndicationTime.setStatus('current')
vmwEnvPerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 4), VmwCIMSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvPerceivedSeverity.setStatus('current')
vmwEnvAlertType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 5), VmwCIMAlertTypes()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvAlertType.setStatus('current')
vmwEnvSysCreationClassName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 6), VmwCimName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvSysCreationClassName.setStatus('current')
vmwEnvAlertingElement = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 7), VmwCimName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvAlertingElement.setStatus('current')
vmwEnvAlertingFormat = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 8), VmwCIMAlertFormat()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvAlertingFormat.setStatus('current')
vmwEnvSystemName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 9), VmwCimName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvSystemName.setStatus('current')
vmwEnvProviderName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 30, 10), VmwCimName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwEnvProviderName.setStatus('current')
vmwESXEnvHardwareAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 302)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvHardwareAlert.setStatus('current')
vmwESXEnvBatteryAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 303)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvBatteryAlert.setStatus('current')
vmwESXEnvChassisAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 304)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvChassisAlert.setStatus('current')
vmwESXEnvThermalAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 305)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvThermalAlert.setStatus('current')
vmwESXEnvDiskAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 306)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvDiskAlert.setStatus('current')
vmwESXEnvPowerAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 307)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvPowerAlert.setStatus('current')
vmwESXEnvProcessorAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 308)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvProcessorAlert.setStatus('current')
vmwESXEnvMemoryAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 309)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvMemoryAlert.setStatus('current')
vmwESXEnvBIOSAlert = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 310)).setObjects(("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if mibBuilder.loadTexts: vmwESXEnvBIOSAlert.setStatus('current')
vmwEnvironmentalMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2))
vmwEnvironmentMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1))
vmwEnvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2))
vmwEnvMIBBasicCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 4)).setObjects(("VMWARE-ENV-MIB", "vmwEnvAlertGroup"), ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup2"), ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvMIBBasicCompliance3 = vmwEnvMIBBasicCompliance3.setStatus('current')
vmwEnvMIBBasicCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 3)).setObjects(("VMWARE-ENV-MIB", "vmwEnvironmentGroup"), ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup"), ("VMWARE-ENV-MIB", "vmwEnvNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvMIBBasicCompliance2 = vmwEnvMIBBasicCompliance2.setStatus('deprecated')
vmwEnvMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 2)).setObjects(("VMWARE-ENV-MIB", "vmwEnvironmentGroup"), ("VMWARE-ENV-MIB", "vmwEnvNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvMIBBasicCompliance = vmwEnvMIBBasicCompliance.setStatus('obsolete')
vmwEnvAlertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 5)).setObjects(("VMWARE-ENV-MIB", "vmwEnvSource"), ("VMWARE-ENV-MIB", "vmwEnvInIndications"), ("VMWARE-ENV-MIB", "vmwEnvLastIn"), ("VMWARE-ENV-MIB", "vmwEnvOutNotifications"), ("VMWARE-ENV-MIB", "vmwEnvInErrs"), ("VMWARE-ENV-MIB", "vmwEnvIndOidErrs"), ("VMWARE-ENV-MIB", "vmwEnvCvtValueErrs"), ("VMWARE-ENV-MIB", "vmwEnvCvtSyntaxErrs"), ("VMWARE-ENV-MIB", "vmwEnvCvtOidErrs"), ("VMWARE-ENV-MIB", "vmwEnvGetClassErrs"), ("VMWARE-ENV-MIB", "vmwEnvPropertySkips"), ("VMWARE-ENV-MIB", "vmwEnvIndicationSkips"), ("VMWARE-ENV-MIB", "vmwEnvDescription"), ("VMWARE-ENV-MIB", "vmwEnvEventTime"), ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"), ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"), ("VMWARE-ENV-MIB", "vmwEnvAlertType"), ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"), ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"), ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"), ("VMWARE-ENV-MIB", "vmwEnvSystemName"), ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvAlertGroup = vmwEnvAlertGroup.setStatus('current')
vmwEnvironmentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 1)).setObjects(("VMWARE-ENV-MIB", "vmwEnvNumber"), ("VMWARE-ENV-MIB", "vmwEnvLastChange"), ("VMWARE-ENV-MIB", "vmwSubsystemType"), ("VMWARE-ENV-MIB", "vmwHardwareStatus"), ("VMWARE-ENV-MIB", "vmwEventDescription"), ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvironmentGroup = vmwEnvironmentGroup.setStatus('deprecated')
vmwEnvNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 2)).setObjects(("VMWARE-ENV-MIB", "vmwEnvHardwareEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwEnvNotificationGroup = vmwEnvNotificationGroup.setStatus('deprecated')
vmwESXEnvNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 3)).setObjects(("VMWARE-ENV-MIB", "vmwESXEnvHardwareEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESXEnvNotificationGroup = vmwESXEnvNotificationGroup.setStatus('deprecated')
vmwESXEnvNotificationGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 4)).setObjects(("VMWARE-ENV-MIB", "vmwESXEnvHardwareAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvBatteryAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvChassisAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvThermalAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvDiskAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvPowerAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvProcessorAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvMemoryAlert"), ("VMWARE-ENV-MIB", "vmwESXEnvBIOSAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESXEnvNotificationGroup2 = vmwESXEnvNotificationGroup2.setStatus('current')
mibBuilder.exportSymbols("VMWARE-ENV-MIB", vmwEnvTable=vmwEnvTable, vmwEnvEntry=vmwEnvEntry, vmwEnvNumber=vmwEnvNumber, vmwEnvIndex=vmwEnvIndex, vmwESXEnvNotificationGroup2=vmwESXEnvNotificationGroup2, vmwEnvironmentalMIB=vmwEnvironmentalMIB, vmwEnv=vmwEnv, vmwEnvAlertingFormat=vmwEnvAlertingFormat, vmwESXEnvChassisAlert=vmwESXEnvChassisAlert, vmwESXEnvBIOSAlert=vmwESXEnvBIOSAlert, vmwEnvIndOidErrs=vmwEnvIndOidErrs, vmwEnvMIBBasicCompliance2=vmwEnvMIBBasicCompliance2, vmwEnvCvtSyntaxErrs=vmwEnvCvtSyntaxErrs, vmwEnvIndicationTime=vmwEnvIndicationTime, vmwEnvLastIn=vmwEnvLastIn, vmwESXEnvThermalAlert=vmwESXEnvThermalAlert, vmwESXEnvNotificationGroup=vmwESXEnvNotificationGroup, vmwEventDescription=vmwEventDescription, vmwEnvPropertySkips=vmwEnvPropertySkips, vmwESXEnvHardwareAlert=vmwESXEnvHardwareAlert, vmwEnvCIM=vmwEnvCIM, vmwESXEnvDiskAlert=vmwESXEnvDiskAlert, vmwEnvSource=vmwEnvSource, vmwEnvAlertType=vmwEnvAlertType, vmwEnvAlertingElement=vmwEnvAlertingElement, vmwEnvInIndications=vmwEnvInIndications, vmwEnvOutNotifications=vmwEnvOutNotifications, vmwESXEnvHardwareEvent=vmwESXEnvHardwareEvent, vmwESXEnvPowerAlert=vmwESXEnvPowerAlert, vmwEnvDescription=vmwEnvDescription, vmwESXEnvBatteryAlert=vmwESXEnvBatteryAlert, vmwEnvInErrs=vmwEnvInErrs, vmwESXNotifications=vmwESXNotifications, vmwEnvSysCreationClassName=vmwEnvSysCreationClassName, vmwEnvMIBGroups=vmwEnvMIBGroups, vmwEnvMIBBasicCompliance=vmwEnvMIBBasicCompliance, vmwEnvironmentGroup=vmwEnvironmentGroup, vmwEnvHardwareEvent=vmwEnvHardwareEvent, vmwEnvLastChange=vmwEnvLastChange, vmwEnvironmentMIBCompliances=vmwEnvironmentMIBCompliances, vmwEnvCvtOidErrs=vmwEnvCvtOidErrs, vmwEnvironmentalMIBConformance=vmwEnvironmentalMIBConformance, vmwEnvAlertGroup=vmwEnvAlertGroup, vmwEnvGetClassErrs=vmwEnvGetClassErrs, vmwEnvPerceivedSeverity=vmwEnvPerceivedSeverity, PYSNMP_MODULE_ID=vmwEnvironmentalMIB, vmwEnvMIBBasicCompliance3=vmwEnvMIBBasicCompliance3, vmwEnvCvtValueErrs=vmwEnvCvtValueErrs, vmwEnvNotificationGroup=vmwEnvNotificationGroup, vmwSubsystemType=vmwSubsystemType, vmwHardwareStatus=vmwHardwareStatus, vmwEnvEventTime=vmwEnvEventTime, vmwEnvProviderName=vmwEnvProviderName, vmwESXEnvProcessorAlert=vmwESXEnvProcessorAlert, vmwESXEnvMemoryAlert=vmwESXEnvMemoryAlert, vmwEnvIndicationSkips=vmwEnvIndicationSkips, vmwEnvHardwareTime=vmwEnvHardwareTime, vmwEnvSystemName=vmwEnvSystemName)
