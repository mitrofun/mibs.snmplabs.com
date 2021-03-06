#
# PySNMP MIB module RAPTOR-SNMPv1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPTOR-SNMPv1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, TimeTicks, Integer32, Unsigned32, ModuleIdentity, Counter32, Gauge32, IpAddress, enterprises, NotificationType, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "TimeTicks", "Integer32", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress", "enterprises", "NotificationType", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
raptorSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 1294))
raptorModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 1))
raptorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 2))
raptorTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 3))
raptorNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 1294, 2, 1), OctetString())
if mibBuilder.loadTexts: raptorNotifyMessage.setStatus('mandatory')
if mibBuilder.loadTexts: raptorNotifyMessage.setDescription('An alert message generated by a Raptor Firewall.')
raptorNotifyTrap = NotificationType((1, 3, 6, 1, 4, 1, 1294) + (0,1)).setObjects(("RAPTOR-SNMPv1-MIB", "raptorNotifyMessage"))
if mibBuilder.loadTexts: raptorNotifyTrap.setDescription('An alert generated by a Raptor Firewall.')
mibBuilder.exportSymbols("RAPTOR-SNMPv1-MIB", raptorNotifyMessage=raptorNotifyMessage, raptorModules=raptorModules, raptorSystems=raptorSystems, raptorTraps=raptorTraps, raptorObjects=raptorObjects, raptorNotifyTrap=raptorNotifyTrap)
