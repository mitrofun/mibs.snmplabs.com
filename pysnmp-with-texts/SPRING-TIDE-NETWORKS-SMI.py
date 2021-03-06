#
# PySNMP MIB module SPRING-TIDE-NETWORKS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPRING-TIDE-NETWORKS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:10:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Gauge32, Integer32, Unsigned32, ObjectIdentity, Bits, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
springtidenet = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551))
if mibBuilder.loadTexts: springtidenet.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: springtidenet.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: springtidenet.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: springtidenet.setDescription('The Structure of Management Information for the Spring Tide Networks enterprise MIBs.')
stnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3551, 1))
if mibBuilder.loadTexts: stnProducts.setStatus('current')
if mibBuilder.loadTexts: stnProducts.setDescription('stnProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in stn-products-mib.')
stnSystems = ObjectIdentity((1, 3, 6, 1, 4, 1, 3551, 2))
if mibBuilder.loadTexts: stnSystems.setStatus('current')
if mibBuilder.loadTexts: stnSystems.setDescription('stnSystems is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in stn-???-mib.')
stnExtensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 3551, 3))
if mibBuilder.loadTexts: stnExtensions.setStatus('current')
if mibBuilder.loadTexts: stnExtensions.setDescription('stnExtensions is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in stn-???-mib.')
stnTemporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 3551, 4))
if mibBuilder.loadTexts: stnTemporary.setStatus('current')
if mibBuilder.loadTexts: stnTemporary.setDescription('stnTemporary provides a root object identifier from which temporary mibs may be based. MIBs are typicially based here if they fall in one of two categories: 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are stn work-in-process which has not been assigned a permanent object identifier by the stn assigned number authority, typicially because the mib is not ready for deployment. NOTE WELL: support for mibs in the stnTemporary subtree will be deleted when a permanent object identifier assignment is made.')
stnMibModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3551, 5))
if mibBuilder.loadTexts: stnMibModules.setStatus('current')
if mibBuilder.loadTexts: stnMibModules.setDescription('stnModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
stnConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 99))
stnNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 100))
stnNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0))
stnTmpProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 4, 1))
mibBuilder.exportSymbols("SPRING-TIDE-NETWORKS-SMI", stnExtensions=stnExtensions, stnProducts=stnProducts, stnSystems=stnSystems, stnTemporary=stnTemporary, springtidenet=springtidenet, stnConfig=stnConfig, stnMibModules=stnMibModules, stnNotificationPrefix=stnNotificationPrefix, PYSNMP_MODULE_ID=springtidenet, stnTmpProtocols=stnTmpProtocols, stnNotification=stnNotification)
