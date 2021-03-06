#
# PySNMP MIB module NT-Reference-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NT-Reference-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, IpAddress, Counter32, ModuleIdentity, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Bits, ObjectIdentity, Integer32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Counter32", "ModuleIdentity", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Bits", "ObjectIdentity", "Integer32", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nt = MibIdentifier((1, 3, 6, 1, 4, 1, 562))
meridian = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3))
experimental = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 0))
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2))
smp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 3))
cybele = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 4))
mobility = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 5))
callProcessing = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 6))
iccm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 7))
ngen = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8))
amber = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 9))
entityNaming = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0))
networkID = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 0))
cybeleNaming = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 1))
ngenNaming = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 2))
mailNaming = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 3))
mobilityNmaing = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 2, 0, 4))
mibBuilder.exportSymbols("NT-Reference-MIB", nt=nt, modules=modules, callProcessing=callProcessing, amber=amber, ngenNaming=ngenNaming, cybele=cybele, mobilityNmaing=mobilityNmaing, meridian=meridian, ngen=ngen, experimental=experimental, smp=smp, cybeleNaming=cybeleNaming, mobility=mobility, entityNaming=entityNaming, networkID=networkID, iccm=iccm, common=common, mailNaming=mailNaming)
