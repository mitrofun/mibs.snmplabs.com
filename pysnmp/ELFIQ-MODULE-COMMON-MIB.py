#
# PySNMP MIB module ELFIQ-MODULE-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELFIQ-MODULE-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
common, commonConformance = mibBuilder.importSymbols("ELFIQ-INC-MIB", "common", "commonConformance")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ModuleIdentity, Integer32, Counter64, TimeTicks, NotificationType, iso, MibIdentifier, Unsigned32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "NotificationType", "iso", "MibIdentifier", "Unsigned32", "Bits", "Counter32")
VariablePointer, RowStatus, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString")
commonComponent = ModuleIdentity((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1))
if mibBuilder.loadTexts: commonComponent.setLastUpdated('0902190000Z')
if mibBuilder.loadTexts: commonComponent.setOrganization('Elfiq Inc.')
systInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1))
class SystIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

systNumber = MibScalar((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systNumber.setStatus('current')
systTable = MibTable((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: systTable.setStatus('current')
systEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "ELFIQ-MODULE-COMMON-MIB", "systIndex"))
if mibBuilder.loadTexts: systEntry.setStatus('current')
systIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 1), SystIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systIndex.setStatus('current')
systModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systModel.setStatus('current')
systHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systHostname.setStatus('current')
systVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systVersion.setStatus('current')
systRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systRevision.setStatus('current')
systRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systRelease.setStatus('current')
systBuild = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systBuild.setStatus('current')
systTypeDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systTypeDesc.setStatus('current')
systTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systTime.setStatus('current')
systLicenceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 1), ("notVerified", 2), ("keyActivated", 3), ("readKeyFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systLicenceStatus.setStatus('current')
systLicenceType = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("endUser", 1), ("demo", 2), ("nfr", 3), ("hrl", 4), ("isp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systLicenceType.setStatus('current')
systNbVfiActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systNbVfiActivated.setStatus('current')
systCpuUsePct = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systCpuUsePct.setStatus('current')
systRamUsePct = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systRamUsePct.setStatus('current')
systFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systFanSpeed.setStatus('current')
systCpuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systCpuTemp.setStatus('current')
systSmptSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("alert", 1), ("warning", 2), ("notice", 3), ("info", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmptSeverity.setStatus('current')
systSmtpReciptient1 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient1.setStatus('current')
systSmtpReciptient2 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient2.setStatus('current')
systSmtpReciptient3 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient3.setStatus('current')
systSmtpReciptient4 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient4.setStatus('current')
systSmtpReciptient5 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient5.setStatus('current')
systSmtpReciptient6 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient6.setStatus('current')
systSmtpReciptient7 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient7.setStatus('current')
systSmtpReciptient8 = MibTableColumn((1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systSmtpReciptient8.setStatus('current')
commonNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2))
systNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1))
systEOSStart = NotificationType((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 1)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systHostname"))
if mibBuilder.loadTexts: systEOSStart.setStatus('current')
systCPUTemp = NotificationType((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 2)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systHostname"), ("ELFIQ-MODULE-COMMON-MIB", "systCpuTemp"))
if mibBuilder.loadTexts: systCPUTemp.setStatus('current')
systCPUUsage = NotificationType((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 3)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systHostname"))
if mibBuilder.loadTexts: systCPUUsage.setStatus('current')
systCPUFan = NotificationType((1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 4)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systHostname"))
if mibBuilder.loadTexts: systCPUFan.setStatus('current')
systGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2, 1, 1))
systInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19713, 2, 1, 1, 1)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systNumber"), ("ELFIQ-MODULE-COMMON-MIB", "systIndex"), ("ELFIQ-MODULE-COMMON-MIB", "systModel"), ("ELFIQ-MODULE-COMMON-MIB", "systHostname"), ("ELFIQ-MODULE-COMMON-MIB", "systVersion"), ("ELFIQ-MODULE-COMMON-MIB", "systRevision"), ("ELFIQ-MODULE-COMMON-MIB", "systRelease"), ("ELFIQ-MODULE-COMMON-MIB", "systBuild"), ("ELFIQ-MODULE-COMMON-MIB", "systTypeDesc"), ("ELFIQ-MODULE-COMMON-MIB", "systTime"), ("ELFIQ-MODULE-COMMON-MIB", "systLicenceStatus"), ("ELFIQ-MODULE-COMMON-MIB", "systLicenceType"), ("ELFIQ-MODULE-COMMON-MIB", "systNbVfiActivated"), ("ELFIQ-MODULE-COMMON-MIB", "systCpuUsePct"), ("ELFIQ-MODULE-COMMON-MIB", "systFanSpeed"), ("ELFIQ-MODULE-COMMON-MIB", "systCpuTemp"), ("ELFIQ-MODULE-COMMON-MIB", "systRamUsePct"), ("ELFIQ-MODULE-COMMON-MIB", "systSmptSeverity"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient1"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient2"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient3"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient4"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient5"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient6"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient7"), ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient8"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systInfoGroup = systInfoGroup.setStatus('current')
systNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19713, 2, 1, 1, 2)).setObjects(("ELFIQ-MODULE-COMMON-MIB", "systEOSStart"), ("ELFIQ-MODULE-COMMON-MIB", "systCPUTemp"), ("ELFIQ-MODULE-COMMON-MIB", "systCPUUsage"), ("ELFIQ-MODULE-COMMON-MIB", "systCPUFan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systNotificationGroup = systNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ELFIQ-MODULE-COMMON-MIB", systSmtpReciptient1=systSmtpReciptient1, systSmtpReciptient3=systSmtpReciptient3, systCPUFan=systCPUFan, systIndex=systIndex, systModel=systModel, systTable=systTable, systCpuTemp=systCpuTemp, systGroups=systGroups, systTypeDesc=systTypeDesc, systEntry=systEntry, systCPUUsage=systCPUUsage, systSmptSeverity=systSmptSeverity, systInfoGroup=systInfoGroup, systLicenceStatus=systLicenceStatus, systRamUsePct=systRamUsePct, commonComponent=commonComponent, systNumber=systNumber, systRevision=systRevision, systCpuUsePct=systCpuUsePct, systNotificationGroup=systNotificationGroup, systSmtpReciptient7=systSmtpReciptient7, systVersion=systVersion, systNbVfiActivated=systNbVfiActivated, SystIndex=SystIndex, PYSNMP_MODULE_ID=commonComponent, systSmtpReciptient4=systSmtpReciptient4, systCPUTemp=systCPUTemp, commonNotification=commonNotification, systNotification=systNotification, systSmtpReciptient6=systSmtpReciptient6, systFanSpeed=systFanSpeed, systHostname=systHostname, systBuild=systBuild, systLicenceType=systLicenceType, systEOSStart=systEOSStart, systSmtpReciptient8=systSmtpReciptient8, systInfo=systInfo, systTime=systTime, systRelease=systRelease, systSmtpReciptient2=systSmtpReciptient2, systSmtpReciptient5=systSmtpReciptient5)
