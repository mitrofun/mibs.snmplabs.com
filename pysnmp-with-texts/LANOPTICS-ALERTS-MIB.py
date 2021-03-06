#
# PySNMP MIB module LANOPTICS-ALERTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANOPTICS-ALERTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, MibIdentifier, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, ModuleIdentity, enterprises, TimeTicks, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "ModuleIdentity", "enterprises", "TimeTicks", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
alerts = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 9))
alerts_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 9, 2)).setLabel("alerts-mgmt")
lanOpticsAlertsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 224, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsAlertsEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertsEnabled.setDescription('A boolean variable that defines if the agent is sending alerts (traps) or alerts are disabled due to high frequency of alerts generation (see RFC-1224), regarding this manager enabled - 1 , disabled - 0.')
lanOpticsMaxAlertsPerTime = MibScalar((1, 3, 6, 1, 4, 1, 224, 9, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsMaxAlertsPerTime.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsMaxAlertsPerTime.setDescription("Defines the maximum alerts allowed in lanOpticsWindowTime interval before an 'lanOpticsAlertsDisabled' trap is issued and 'lanOpticsAlertsEnabled' is set to 0 (see RFC-1224).")
lanOpticsWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 224, 9, 2, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsWindowTime.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsWindowTime.setDescription("Defines the time interval in centiseconds, in which no more than 'lanOpticsMaxAlertsPerTime' may be sent before a 'lanOpticsAlertsDisabled' trap is issued and 'lanOpticsAlertsEnabled' is set to 0 (see RFC-1224).")
lanOpticsMaxLogTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 224, 9, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsMaxLogTableEntries.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsMaxLogTableEntries.setDescription('Defines the number of alerts saved in the lanOpticsAlertsTable below.')
lanOpticsCurrentAlertId = MibScalar((1, 3, 6, 1, 4, 1, 224, 9, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsCurrentAlertId.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsCurrentAlertId.setDescription('Holds the last alert ID in the lanOpticsAlertsTable')
lanOpticsAlertsRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 224, 9, 2, 10), )
if mibBuilder.loadTexts: lanOpticsAlertsRegisterTable.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertsRegisterTable.setDescription('Each entry in this table, designated by the four digits of an IP address, defines if this address is registered to receive traps by the agent.')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1) + (1000, ), Integer32())
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1) + (1001, ), Integer32())
pysmiFakeCol1002 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1) + (1002, ), Integer32())
pysmiFakeCol1003 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1) + (1003, ), Integer32())
lanOpticsAlertsRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1), ).setIndexNames((0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol1000"), (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol1001"), (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol1002"), (0, "LANOPTICS-ALERTS-MIB", "pysmiFakeCol1003"))
if mibBuilder.loadTexts: lanOpticsAlertsRegisterEntry.setStatus('mandatory')
lanOpticsAlertsRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("register", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsAlertsRegister.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertsRegister.setDescription('A boolean variable that is set (to 1) if the manager wants to be registered to receive SNMP traps, and is set to 0 if not.')
lanOpticsAlertsTable = MibTable((1, 3, 6, 1, 4, 1, 224, 9, 2, 11), )
if mibBuilder.loadTexts: lanOpticsAlertsTable.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertsTable.setDescription("This table contains the last lanOpticsMaxLogTableEntries alerts that have been issued by the agent. Some of these alerts may have not been sent if lanOpticsAlertsEnabled is FALSE. The table is used to enable the manager to poll alerts. The first alertId can be retrieved by get-next on the table's object ID, and the next by get-next on the first one and so on.")
lanOpticsAlertsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1), ).setIndexNames((0, "LANOPTICS-ALERTS-MIB", "lanOpticsAlertId"))
if mibBuilder.loadTexts: lanOpticsAlertsEntry.setStatus('mandatory')
lanOpticsAlertId = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsAlertId.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertId.setDescription('Give the manager a mean to get the first alertId by a GET-NEXT (see RFC 1224).')
lanOpticsAlertData = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 9, 2, 11, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsAlertData.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsAlertData.setDescription('An Internal description of the alert to be polled by a StarNet Trapper.')
mibBuilder.exportSymbols("LANOPTICS-ALERTS-MIB", alerts=alerts, alerts_mgmt=alerts_mgmt, lanOpticsAlertsEntry=lanOpticsAlertsEntry, lanOpticsAlertsRegisterEntry=lanOpticsAlertsRegisterEntry, lanOpticsWindowTime=lanOpticsWindowTime, lanOpticsAlertsEnabled=lanOpticsAlertsEnabled, lanOpticsAlertId=lanOpticsAlertId, pysmiFakeCol1003=pysmiFakeCol1003, lanOpticsAlertsTable=lanOpticsAlertsTable, lanOpticsAlertData=lanOpticsAlertData, pysmiFakeCol1000=pysmiFakeCol1000, lanOpticsAlertsRegister=lanOpticsAlertsRegister, lanOpticsAlertsRegisterTable=lanOpticsAlertsRegisterTable, lanOpticsCurrentAlertId=lanOpticsCurrentAlertId, lanOpticsMaxAlertsPerTime=lanOpticsMaxAlertsPerTime, lanOptics=lanOptics, lanOpticsMaxLogTableEntries=lanOpticsMaxLogTableEntries, pysmiFakeCol1001=pysmiFakeCol1001, pysmiFakeCol1002=pysmiFakeCol1002)
