#
# PySNMP MIB module MPLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:04:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, ModuleIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, iso, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "iso", "IpAddress", "Counter64")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
mpls = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 2))
mpls.setRevisions(('2009-02-23 14:45',))
if mibBuilder.loadTexts: mpls.setLastUpdated('200902231445Z')
if mibBuilder.loadTexts: mpls.setOrganization('Juniper Networks, Inc.')
mplsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1))
mplsVersion = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVersion.setStatus('current')
mplsSignalingProto = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("rsvp", 3), ("ldp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsSignalingProto.setStatus('current')
mplsConfiguredLsps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsConfiguredLsps.setStatus('current')
mplsActiveLsps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsActiveLsps.setStatus('current')
mplsTEInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2))
mplsTEDistProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("isis", 2), ("ospf", 3), ("isis-ospf", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTEDistProtocol.setStatus('current')
mplsAdminGroupList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2), )
if mibBuilder.loadTexts: mplsAdminGroupList.setStatus('current')
mplsAdminGroup = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1), ).setIndexNames((0, "MPLS-MIB", "mplsAdminGroupNumber"))
if mibBuilder.loadTexts: mplsAdminGroup.setStatus('current')
mplsAdminGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsAdminGroupNumber.setStatus('current')
mplsAdminGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsAdminGroupName.setStatus('current')
mplsLspList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3), )
if mibBuilder.loadTexts: mplsLspList.setStatus('deprecated')
mplsLspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1), ).setIndexNames((0, "MPLS-MIB", "mplsLspName"))
if mibBuilder.loadTexts: mplsLspEntry.setStatus('deprecated')
mplsLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspName.setStatus('deprecated')
mplsLspState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("notInService", 4), ("backupActive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspState.setStatus('deprecated')
mplsLspOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspOctets.setStatus('deprecated')
mplsLspPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPackets.setStatus('deprecated')
mplsLspAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspAge.setStatus('deprecated')
mplsLspTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTimeUp.setStatus('deprecated')
mplsLspPrimaryTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPrimaryTimeUp.setStatus('deprecated')
mplsLspTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTransitions.setStatus('deprecated')
mplsLspLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspLastTransition.setStatus('deprecated')
mplsLspPathChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspPathChanges.setStatus('deprecated')
mplsLspLastPathChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspLastPathChange.setStatus('deprecated')
mplsLspConfiguredPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspConfiguredPaths.setStatus('deprecated')
mplsLspStandbyPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspStandbyPaths.setStatus('deprecated')
mplsLspOperationalPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspOperationalPaths.setStatus('deprecated')
mplsLspFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspFrom.setStatus('deprecated')
mplsLspTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspTo.setStatus('deprecated')
mplsPathName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathName.setStatus('deprecated')
mplsPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("primary", 2), ("standby", 3), ("secondary", 4), ("bypass", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathType.setStatus('deprecated')
mplsPathExplicitRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathExplicitRoute.setStatus('deprecated')
mplsPathRecordRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathRecordRoute.setStatus('deprecated')
mplsPathBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathBandwidth.setStatus('deprecated')
mplsPathCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathCOS.setStatus('deprecated')
mplsPathInclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInclude.setStatus('deprecated')
mplsPathExclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathExclude.setStatus('deprecated')
mplsPathSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathSetupPriority.setStatus('deprecated')
mplsPathHoldPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathHoldPriority.setStatus('deprecated')
mplsPathProperties = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))).clone(namedValues=NamedValues(("record-route", 1), ("adaptive", 2), ("cspf", 4), ("mergeable", 8), ("preemptable", 16), ("preemptive", 32), ("fast-reroute", 64)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathProperties.setStatus('deprecated')
mplsLspInfoList = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5), )
if mibBuilder.loadTexts: mplsLspInfoList.setStatus('current')
mplsLspInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1), ).setIndexNames((1, "MPLS-MIB", "mplsLspInfoName"))
if mibBuilder.loadTexts: mplsLspInfoEntry.setStatus('current')
mplsLspInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsLspInfoName.setStatus('current')
mplsLspInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("notInService", 4), ("backupActive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoState.setStatus('current')
mplsLspInfoOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoOctets.setStatus('current')
mplsLspInfoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPackets.setStatus('current')
mplsLspInfoAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAge.setStatus('current')
mplsLspInfoTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTimeUp.setStatus('current')
mplsLspInfoPrimaryTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPrimaryTimeUp.setStatus('current')
mplsLspInfoTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTransitions.setStatus('current')
mplsLspInfoLastTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoLastTransition.setStatus('current')
mplsLspInfoPathChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoPathChanges.setStatus('current')
mplsLspInfoLastPathChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoLastPathChange.setStatus('current')
mplsLspInfoConfiguredPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoConfiguredPaths.setStatus('current')
mplsLspInfoStandbyPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoStandbyPaths.setStatus('current')
mplsLspInfoOperationalPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoOperationalPaths.setStatus('current')
mplsLspInfoFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoFrom.setStatus('current')
mplsLspInfoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoTo.setStatus('current')
mplsPathInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoName.setStatus('current')
mplsPathInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("primary", 2), ("standby", 3), ("secondary", 4), ("bypass", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoType.setStatus('current')
mplsPathInfoExplicitRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoExplicitRoute.setStatus('current')
mplsPathInfoRecordRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoRecordRoute.setStatus('current')
mplsPathInfoBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoBandwidth.setStatus('current')
mplsPathInfoCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoCOS.setStatus('current')
mplsPathInfoInclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoInclude.setStatus('current')
mplsPathInfoExclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoExclude.setStatus('current')
mplsPathInfoSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoSetupPriority.setStatus('current')
mplsPathInfoHoldPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoHoldPriority.setStatus('current')
mplsPathInfoProperties = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))).clone(namedValues=NamedValues(("record-route", 1), ("adaptive", 2), ("cspf", 4), ("mergeable", 8), ("preemptable", 16), ("preemptive", 32), ("fast-reroute", 64)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoProperties.setStatus('current')
mplsLspInfoAggrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAggrOctets.setStatus('current')
mplsLspInfoAggrPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLspInfoAggrPackets.setStatus('current')
mplsPathInfoRecordRouteWithLabels = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsPathInfoRecordRouteWithLabels.setStatus('current')
mplsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4))
mplsLspUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 1)).setObjects(("MPLS-MIB", "mplsLspName"), ("MPLS-MIB", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspUp.setStatus('deprecated')
mplsLspDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 2)).setObjects(("MPLS-MIB", "mplsLspName"), ("MPLS-MIB", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspDown.setStatus('deprecated')
mplsLspChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 3)).setObjects(("MPLS-MIB", "mplsLspName"), ("MPLS-MIB", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspChange.setStatus('deprecated')
mplsLspPathDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 4)).setObjects(("MPLS-MIB", "mplsLspName"), ("MPLS-MIB", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspPathDown.setStatus('deprecated')
mplsLspPathUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 5)).setObjects(("MPLS-MIB", "mplsLspName"), ("MPLS-MIB", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspPathUp.setStatus('deprecated')
mplsLspTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0))
mplsLspInfoUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 1)).setObjects(("MPLS-MIB", "mplsLspInfoName"), ("MPLS-MIB", "mplsPathInfoName"))
if mibBuilder.loadTexts: mplsLspInfoUp.setStatus('current')
mplsLspInfoDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 2)).setObjects(("MPLS-MIB", "mplsLspInfoName"), ("MPLS-MIB", "mplsPathInfoName"))
if mibBuilder.loadTexts: mplsLspInfoDown.setStatus('current')
mplsLspInfoChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 3)).setObjects(("MPLS-MIB", "mplsLspInfoName"), ("MPLS-MIB", "mplsPathInfoName"))
if mibBuilder.loadTexts: mplsLspInfoChange.setStatus('current')
mplsLspInfoPathDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 4)).setObjects(("MPLS-MIB", "mplsLspInfoName"), ("MPLS-MIB", "mplsPathInfoName"))
if mibBuilder.loadTexts: mplsLspInfoPathDown.setStatus('current')
mplsLspInfoPathUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 5)).setObjects(("MPLS-MIB", "mplsLspInfoName"), ("MPLS-MIB", "mplsPathInfoName"))
if mibBuilder.loadTexts: mplsLspInfoPathUp.setStatus('current')
mibBuilder.exportSymbols("MPLS-MIB", mplsLspInfoPathUp=mplsLspInfoPathUp, mplsLspAge=mplsLspAge, mplsPathInfoProperties=mplsPathInfoProperties, mplsLspTransitions=mplsLspTransitions, mplsPathExclude=mplsPathExclude, mplsPathInfoType=mplsPathInfoType, mplsLspTraps=mplsLspTraps, mplsLspOperationalPaths=mplsLspOperationalPaths, mplsLspInfoAge=mplsLspInfoAge, mplsLspTo=mplsLspTo, mplsTEDistProtocol=mplsTEDistProtocol, mplsLspInfoAggrOctets=mplsLspInfoAggrOctets, mplsPathRecordRoute=mplsPathRecordRoute, mplsLspInfoStandbyPaths=mplsLspInfoStandbyPaths, mplsLspInfoChange=mplsLspInfoChange, mplsPathType=mplsPathType, mplsPathExplicitRoute=mplsPathExplicitRoute, mplsLspDown=mplsLspDown, mplsLspInfoPackets=mplsLspInfoPackets, mplsAdminGroupList=mplsAdminGroupList, mplsAdminGroupName=mplsAdminGroupName, mplsPathInclude=mplsPathInclude, mplsLspEntry=mplsLspEntry, mplsLspInfoLastPathChange=mplsLspInfoLastPathChange, mplsPathProperties=mplsPathProperties, mplsTEInfo=mplsTEInfo, mplsLspInfoDown=mplsLspInfoDown, mplsPathName=mplsPathName, mplsLspInfoTo=mplsLspInfoTo, mplsVersion=mplsVersion, mplsPathInfoExplicitRoute=mplsPathInfoExplicitRoute, mplsPathInfoHoldPriority=mplsPathInfoHoldPriority, mplsLspState=mplsLspState, mplsPathInfoRecordRouteWithLabels=mplsPathInfoRecordRouteWithLabels, mplsLspFrom=mplsLspFrom, mplsLspInfoTransitions=mplsLspInfoTransitions, mplsPathInfoRecordRoute=mplsPathInfoRecordRoute, mplsActiveLsps=mplsActiveLsps, mplsSignalingProto=mplsSignalingProto, mplsAdminGroupNumber=mplsAdminGroupNumber, mplsPathInfoBandwidth=mplsPathInfoBandwidth, mplsPathInfoExclude=mplsPathInfoExclude, mplsConfiguredLsps=mplsConfiguredLsps, mplsLspPathDown=mplsLspPathDown, mpls=mpls, mplsLspInfoList=mplsLspInfoList, mplsLspInfoState=mplsLspInfoState, mplsLspInfoPathChanges=mplsLspInfoPathChanges, mplsLspTimeUp=mplsLspTimeUp, mplsLspInfoAggrPackets=mplsLspInfoAggrPackets, mplsLspPathUp=mplsLspPathUp, mplsPathHoldPriority=mplsPathHoldPriority, mplsAdminGroup=mplsAdminGroup, mplsPathInfoCOS=mplsPathInfoCOS, mplsPathInfoSetupPriority=mplsPathInfoSetupPriority, mplsLspPrimaryTimeUp=mplsLspPrimaryTimeUp, mplsLspUp=mplsLspUp, mplsLspInfoPrimaryTimeUp=mplsLspInfoPrimaryTimeUp, mplsLspLastTransition=mplsLspLastTransition, mplsTraps=mplsTraps, mplsLspInfoPathDown=mplsLspInfoPathDown, mplsLspOctets=mplsLspOctets, mplsLspInfoConfiguredPaths=mplsLspInfoConfiguredPaths, mplsLspStandbyPaths=mplsLspStandbyPaths, mplsLspPackets=mplsLspPackets, mplsPathBandwidth=mplsPathBandwidth, mplsLspList=mplsLspList, mplsPathSetupPriority=mplsPathSetupPriority, mplsLspInfoFrom=mplsLspInfoFrom, mplsLspLastPathChange=mplsLspLastPathChange, mplsLspInfoName=mplsLspInfoName, mplsLspPathChanges=mplsLspPathChanges, PYSNMP_MODULE_ID=mpls, mplsLspInfoTimeUp=mplsLspInfoTimeUp, mplsLspInfoLastTransition=mplsLspInfoLastTransition, mplsLspInfoUp=mplsLspInfoUp, mplsLspConfiguredPaths=mplsLspConfiguredPaths, mplsPathInfoInclude=mplsPathInfoInclude, mplsLspInfoOctets=mplsLspInfoOctets, mplsLspInfoEntry=mplsLspInfoEntry, mplsInfo=mplsInfo, mplsLspInfoOperationalPaths=mplsLspInfoOperationalPaths, mplsPathCOS=mplsPathCOS, mplsLspChange=mplsLspChange, mplsLspName=mplsLspName, mplsPathInfoName=mplsPathInfoName)
