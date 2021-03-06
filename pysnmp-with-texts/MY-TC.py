#
# PySNMP MIB module MY-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:16:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
myModules, = mibBuilder.importSymbols("MY-SMI", "myModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, IpAddress, ModuleIdentity, Counter32, ObjectIdentity, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, TimeTicks, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4, 1))
myTextualConventions.setRevisions(('2002-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: myTextualConventions.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: myTextualConventions.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myTextualConventions.setOrganization('D-Link Crop.')
if mibBuilder.loadTexts: myTextualConventions.setContactInfo(' http://support.dlink.com')
if mibBuilder.loadTexts: myTextualConventions.setDescription('This module defines textual conventions used throughout my enterprise mibs.')
class IfIndex(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the interface index convention. Interface include physical port and aggreate port and switch virtual interface and loopBack interface,etc.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MyTrapType(TextualConvention, Integer32):
    description = 'Private trap(event) type of my switch. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("coldMy", 1), ("warmMy", 2), ("linkDown", 3), ("linkUp", 4), ("authenFailure", 5), ("newRoot", 6), ("topoChange", 7), ("hardChangeDetected", 8), ("portSecurityViolate", 9), ("stormAlarm", 10), ("macNotification", 11), ("vrrpNewMaster", 12), ("vrrpAuthFailure", 13), ("powerStateChange", 14), ("fanStateChange", 15), ("ospf", 16), ("pim", 17), ("igmp", 18), ("dvmrp", 19), ("entity", 20), ("cluster", 21), ("temperatureWarning", 22), ("sysGuard", 23), ("bgp", 24), ("lineDetect", 25), ("bgpReachMaxPrefix", 26), ("hardwareNotSupport", 27))

class ConfigStatus(TextualConvention, Integer32):
    description = "Represents the operational status of an table entry. valid(1) - Indicates this entry's status is valid and active. invalid(2) - Indicates this entry's status is invalid. It is decided by implementatio whether entry is delete"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class MemberMap(TextualConvention, OctetString):
    description = 'Each octet indicate a Logic port, and each octect can have their content means. The lenth of octet string will change along with change of product.'
    status = 'current'

mibBuilder.exportSymbols("MY-TC", PYSNMP_MODULE_ID=myTextualConventions, MemberMap=MemberMap, ConfigStatus=ConfigStatus, MyTrapType=MyTrapType, IfIndex=IfIndex, myTextualConventions=myTextualConventions)
