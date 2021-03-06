#
# PySNMP MIB module RUCKUS-UPGRADE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-UPGRADE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ruckusCommonUpgradeModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonUpgradeModule")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Counter64, IpAddress, iso, Integer32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "IpAddress", "iso", "Integer32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
ruckusUpgradeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1))
if mibBuilder.loadTexts: ruckusUpgradeMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusUpgradeMIB.setOrganization('Ruckus Wireless Inc.')
ruckusUpgradeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1))
ruckusFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1))
ruckusAutoUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2))
ruckusFileTransferMethod = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("ftp", 2), ("web", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferMethod.setStatus('current')
ruckusFileTransferHostName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferHostName.setStatus('current')
ruckusFileTransferHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferHostAddr.setStatus('current')
ruckusFileTransferControlFileName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferControlFileName.setStatus('current')
ruckusFileTransferFTPUsername = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferFTPUsername.setStatus('current')
ruckusFileTransferFTPPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferFTPPassword.setStatus('current')
ruckusFileTransferUpgradeNow = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferUpgradeNow.setStatus('current')
ruckusFileTransferTakeEffectImmediately = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusFileTransferTakeEffectImmediately.setStatus('current')
ruckusAutoUpgradeInitialCheckInterval = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 1), Unsigned32().clone(5)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusAutoUpgradeInitialCheckInterval.setStatus('current')
ruckusAutoUpgradeCheckInterval = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 2), Unsigned32().clone(720)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusAutoUpgradeCheckInterval.setStatus('current')
ruckusAutoUpgradeStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusAutoUpgradeStatus.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-UPGRADE-MIB", ruckusAutoUpgradeStatus=ruckusAutoUpgradeStatus, ruckusFileTransfer=ruckusFileTransfer, ruckusFileTransferFTPPassword=ruckusFileTransferFTPPassword, ruckusFileTransferFTPUsername=ruckusFileTransferFTPUsername, ruckusFileTransferControlFileName=ruckusFileTransferControlFileName, ruckusFileTransferHostName=ruckusFileTransferHostName, ruckusAutoUpgradeCheckInterval=ruckusAutoUpgradeCheckInterval, ruckusFileTransferUpgradeNow=ruckusFileTransferUpgradeNow, ruckusUpgradeMIB=ruckusUpgradeMIB, ruckusFileTransferHostAddr=ruckusFileTransferHostAddr, PYSNMP_MODULE_ID=ruckusUpgradeMIB, ruckusAutoUpgradeInitialCheckInterval=ruckusAutoUpgradeInitialCheckInterval, ruckusFileTransferMethod=ruckusFileTransferMethod, ruckusUpgradeObjects=ruckusUpgradeObjects, ruckusAutoUpgrade=ruckusAutoUpgrade, ruckusFileTransferTakeEffectImmediately=ruckusFileTransferTakeEffectImmediately)
