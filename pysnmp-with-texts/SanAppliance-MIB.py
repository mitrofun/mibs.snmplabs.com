#
# PySNMP MIB module SanAppliance-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SanAppliance-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:14:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, enterprises, Bits, TimeTicks, Counter32, Counter64, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "enterprises", "Bits", "TimeTicks", "Counter32", "Counter64", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893))
sanRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2))
sanAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1))
sanApplGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("critical", 1), ("warning", 2), ("normal", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sanApplGlobalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sanApplGlobalStatus.setDescription('Global health information for the Dell San Appliance.')
sanApplEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200))
sanApplName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sanApplName.setStatus('mandatory')
if mibBuilder.loadTexts: sanApplName.setDescription('Dell San Appliance')
sanApplFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,1)).setObjects(("SanAppliance-MIB", "sanApplName"))
if mibBuilder.loadTexts: sanApplFailed.setDescription('The Dell PowerVault 530F SAN Appliance named $1 is in a critical state.')
sanApplNormal = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,2)).setObjects(("SanAppliance-MIB", "sanApplName"))
if mibBuilder.loadTexts: sanApplNormal.setDescription('The Dell PowerVault 530F SAN Appliance named $1 is back in a normal state.')
sanApplStarted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,3)).setObjects(("SanAppliance-MIB", "sanApplName"))
if mibBuilder.loadTexts: sanApplStarted.setDescription('The Dell PowerVault 530F SAN Appliance named $1 is operational.')
sanApplStopped = NotificationType((1, 3, 6, 1, 4, 1, 674, 10893, 2, 1, 200) + (0,4)).setObjects(("SanAppliance-MIB", "sanApplName"))
if mibBuilder.loadTexts: sanApplStopped.setDescription('The Dell PowerVault 530F SAN Appliance named $1 is no longer running.')
mibBuilder.exportSymbols("SanAppliance-MIB", sanApplStopped=sanApplStopped, storage=storage, sanApplEvts=sanApplEvts, sanAppliance=sanAppliance, dell=dell, sanApplGlobalStatus=sanApplGlobalStatus, sanApplFailed=sanApplFailed, sanApplNormal=sanApplNormal, sanApplStarted=sanApplStarted, sanApplName=sanApplName, sanRoot=sanRoot)
