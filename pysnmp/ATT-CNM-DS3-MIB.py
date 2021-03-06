#
# PySNMP MIB module ATT-CNM-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATT-CNM-DS3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, Gauge32, ModuleIdentity, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, Counter64, Bits, TimeTicks, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "Bits", "TimeTicks", "Integer32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_products = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1)).setLabel("att-products")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
att_cnmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1, 9)).setLabel("att-cnmAgent")
att_cnm = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15)).setLabel("att-cnm")
att_cnm_ds3 = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15, 4)).setLabel("att-cnm-ds3")
attCNMds3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1), )
if mibBuilder.loadTexts: attCNMds3ConfigTable.setStatus('mandatory')
attCNMds3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3ConfigIndex"))
if mibBuilder.loadTexts: attCNMds3ConfigEntry.setStatus('mandatory')
attCNMds3ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ConfigIndex.setStatus('mandatory')
attCNMds3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("ds3M23", 2), ("ds3SYNTRAN", 3), ("ds3CbitParity", 4), ("ds3ClearChannel", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LineType.setStatus('mandatory')
attCNMds3ZeroCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3other", 1), ("ds3B3ZS", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ZeroCoding.setStatus('mandatory')
attCNMds3ErrorsMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsMaxIntervals.setStatus('mandatory')
attCNMds3ErrorsIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsIntervalLen.setStatus('mandatory')
attCNMds3StatusTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2), )
if mibBuilder.loadTexts: attCNMds3StatusTable.setStatus('mandatory')
attCNMds3StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3StatusIndex"))
if mibBuilder.loadTexts: attCNMds3StatusEntry.setStatus('mandatory')
attCNMds3StatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3StatusIndex.setStatus('mandatory')
attCNMds3LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LineStatus.setStatus('mandatory')
attCNMds3ErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3), )
if mibBuilder.loadTexts: attCNMds3ErrorsTable.setStatus('mandatory')
attCNMds3ErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1), ).setIndexNames((0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsIndex"), (0, "ATT-CNM-DS3-MIB", "attCNMds3ErrorsInterval"))
if mibBuilder.loadTexts: attCNMds3ErrorsEntry.setStatus('mandatory')
attCNMds3ErrorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsIndex.setStatus('mandatory')
attCNMds3ErrorsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsInterval.setStatus('mandatory')
attCNMds3ErrorsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsTimeStamp.setStatus('mandatory')
attCNMds3ErrorsLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ErrorsLocalTime.setStatus('mandatory')
attCNMds3LCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LCVs.setStatus('mandatory')
attCNMds3LESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LESs.setStatus('mandatory')
attCNMds3LSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3LSESs.setStatus('mandatory')
attCNMds3CVs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3CVs.setStatus('mandatory')
attCNMds3ESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3ESs.setStatus('mandatory')
attCNMds3SESs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3SESs.setStatus('mandatory')
attCNMds3SEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3SEFSs.setStatus('mandatory')
attCNMds3UASs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 4, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMds3UASs.setStatus('mandatory')
mibBuilder.exportSymbols("ATT-CNM-DS3-MIB", attCNMds3StatusIndex=attCNMds3StatusIndex, attCNMds3ErrorsTable=attCNMds3ErrorsTable, attCNMds3ConfigTable=attCNMds3ConfigTable, attCNMds3UASs=attCNMds3UASs, att_2=att_2, att_products=att_products, attCNMds3CVs=attCNMds3CVs, att_cnm=att_cnm, attCNMds3ErrorsTimeStamp=attCNMds3ErrorsTimeStamp, att_cnmAgent=att_cnmAgent, attCNMds3LineType=attCNMds3LineType, attCNMds3StatusEntry=attCNMds3StatusEntry, attCNMds3ErrorsIntervalLen=attCNMds3ErrorsIntervalLen, attCNMds3LESs=attCNMds3LESs, attCNMds3ErrorsIndex=attCNMds3ErrorsIndex, attCNMds3LineStatus=attCNMds3LineStatus, att_cnm_ds3=att_cnm_ds3, att_mgmt=att_mgmt, attCNMds3ErrorsLocalTime=attCNMds3ErrorsLocalTime, attCNMds3ErrorsEntry=attCNMds3ErrorsEntry, attCNMds3ConfigEntry=attCNMds3ConfigEntry, attCNMds3LSESs=attCNMds3LSESs, attCNMds3SESs=attCNMds3SESs, attCNMds3ErrorsMaxIntervals=attCNMds3ErrorsMaxIntervals, attCNMds3LCVs=attCNMds3LCVs, attCNMds3StatusTable=attCNMds3StatusTable, attCNMds3ErrorsInterval=attCNMds3ErrorsInterval, attCNMds3ConfigIndex=attCNMds3ConfigIndex, attCNMds3SEFSs=attCNMds3SEFSs, attCNMds3ESs=attCNMds3ESs, attCNMds3ZeroCoding=attCNMds3ZeroCoding)
