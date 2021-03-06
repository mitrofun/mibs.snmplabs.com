#
# PySNMP MIB module CXVMFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXVMFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
cxMcVox, = mibBuilder.importSymbols("CXMCVOX-MIB", "cxMcVox")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Unsigned32, NotificationType, Gauge32, iso, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Unsigned32", "NotificationType", "Gauge32", "iso", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxVMFC = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22))
vmfcOutRegCallerCategory = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("subscriber-without-priority", 1), ("subscriber-with-priority", 2), ("maintenance-equipment", 3), ("charge-meter", 4), ("operator", 5), ("data-tx", 6))).clone('subscriber-without-priority')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcOutRegCallerCategory.setStatus('mandatory')
vmfcOutRegCallerCatGrpII3 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal-subscriber", 1), ("atme-equipment", 2), ("maintenance-equipment", 3), ("operator-with-transfer-capability", 4), ("operator-with-intercept-capability", 5))).clone('normal-subscriber')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcOutRegCallerCatGrpII3.setStatus('mandatory')
vmfcOutRegCallerCatGrpII6 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("normal-subscriber", 1), ("atme-equipment", 2), ("maintenance-equipment", 3), ("collect-call", 4), ("time-and-charges", 5), ("subscriber1-on-shared-line", 6), ("subscriber2-on-shared-line", 7), ("subscriber3-on-shared-line", 8), ("operator-without-transfer-capability", 9))).clone('normal-subscriber')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcOutRegCallerCatGrpII6.setStatus('mandatory')
vmfcOutRegExchangeType = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("national-exchange", 1), ("international-exchange", 2))).clone('national-exchange')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcOutRegExchangeType.setStatus('mandatory')
vmfcOutRegCallingID = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 5), DisplayString().clone('0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcOutRegCallingID.setStatus('mandatory')
vmfcInRegNationalAddressSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcInRegNationalAddressSize.setStatus('mandatory')
vmfcInRegInfoRequest = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 7), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcInRegInfoRequest.setStatus('mandatory')
vmfcInRegPulsePeriod = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(150)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcInRegPulsePeriod.setStatus('mandatory')
vmfcCountry = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("mexico", 1), ("philippines", 2), ("nicaragua", 3), ("korea", 4), ("china", 5), ("argentina", 6))).clone('mexico')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcCountry.setStatus('mandatory')
vmfcTimeOutBackwardSignal = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(15000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcTimeOutBackwardSignal.setStatus('mandatory')
vmfcTimeOutForwardSignal = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(24000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmfcTimeOutForwardSignal.setStatus('mandatory')
mibBuilder.exportSymbols("CXVMFC-MIB", vmfcTimeOutForwardSignal=vmfcTimeOutForwardSignal, cxVMFC=cxVMFC, vmfcTimeOutBackwardSignal=vmfcTimeOutBackwardSignal, vmfcOutRegCallingID=vmfcOutRegCallingID, vmfcOutRegCallerCategory=vmfcOutRegCallerCategory, vmfcInRegPulsePeriod=vmfcInRegPulsePeriod, vmfcCountry=vmfcCountry, vmfcOutRegCallerCatGrpII6=vmfcOutRegCallerCatGrpII6, vmfcInRegNationalAddressSize=vmfcInRegNationalAddressSize, vmfcInRegInfoRequest=vmfcInRegInfoRequest, vmfcOutRegCallerCatGrpII3=vmfcOutRegCallerCatGrpII3, vmfcOutRegExchangeType=vmfcOutRegExchangeType)
