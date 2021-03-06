#
# PySNMP MIB module SUNMANAGEMENTCENTER-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUNMANAGEMENTCENTER-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, TimeTicks, enterprises, Gauge32, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "enterprises", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "Counter32", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
traps = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0))
traps.setRevisions(('1999-07-20 15:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: traps.setRevisionsDescriptions(('Rev 1.0 20th July 1999 15:05, Initial version Of MIB.',))
if mibBuilder.loadTexts: traps.setLastUpdated('9907201505Z')
if mibBuilder.loadTexts: traps.setOrganization('Sun Microsystems Inc.')
if mibBuilder.loadTexts: traps.setContactInfo(' Sun Microsystems Inc. Customer Support Postal: 901 San Antonio Road Palo Alto, CA-94303-4900 USA Tel: 650-960-1300 E-mail: service@sun.com')
if mibBuilder.loadTexts: traps.setDescription('This mib defines all the traps forwarded by the Sun Management Center agent, with their variable bindings. Any outside entity can subscribe for these traps.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
sunsymon = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12))
agent = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2))
base = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1))
trapInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3)).setObjects(("SUNMANAGEMENTCENTER-TRAP-MIB", "statusOID"), ("SUNMANAGEMENTCENTER-TRAP-MIB", "refreshOID"), ("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapInfoGroup = trapInfoGroup.setStatus('current')
if mibBuilder.loadTexts: trapInfoGroup.setDescription('Varbinds of traps')
statusChange = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 1)).setObjects(("SUNMANAGEMENTCENTER-TRAP-MIB", "statusOID"))
if mibBuilder.loadTexts: statusChange.setStatus('current')
if mibBuilder.loadTexts: statusChange.setDescription('A statusChange trap signifies that the status of an object has changed.')
valueRefresh = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 2)).setObjects(("SUNMANAGEMENTCENTER-TRAP-MIB", "refreshOID"))
if mibBuilder.loadTexts: valueRefresh.setStatus('current')
if mibBuilder.loadTexts: valueRefresh.setDescription('A valueRefresh trap signifies that the value of an object has been manually refreshed.')
moduleLoaded = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 4)).setObjects(("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo"))
if mibBuilder.loadTexts: moduleLoaded.setStatus('current')
if mibBuilder.loadTexts: moduleLoaded.setDescription('A moduleLoaded trap signifies that a module has been loaded.')
moduleUnloaded = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 5)).setObjects(("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo"))
if mibBuilder.loadTexts: moduleUnloaded.setStatus('current')
if mibBuilder.loadTexts: moduleUnloaded.setDescription('A moduleUnloaded trap signifies that a module has been unloaded.')
statusOID = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: statusOID.setStatus('current')
if mibBuilder.loadTexts: statusOID.setDescription('The identification of the object for which the status changed. This occurs as the first trap-specific varbind in a statusChangeTrap.')
refreshOID = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 2), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: refreshOID.setStatus('current')
if mibBuilder.loadTexts: refreshOID.setDescription('The identification of the object for which the value was refreshed. This occurs as the first trap-specific varbind in a valueRefreshTrap.')
moduleInfo = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: moduleInfo.setStatus('current')
if mibBuilder.loadTexts: moduleInfo.setDescription('The module specification and module version of the module that is being loaded or unloaded. This occurs as the first trap-specific varbind in a moduleLoaded and moduleUnloaded traps.')
mibBuilder.exportSymbols("SUNMANAGEMENTCENTER-TRAP-MIB", agent=agent, trapInfoGroup=trapInfoGroup, moduleLoaded=moduleLoaded, prod=prod, PYSNMP_MODULE_ID=traps, sunsymon=sunsymon, valueRefresh=valueRefresh, moduleUnloaded=moduleUnloaded, refreshOID=refreshOID, statusChange=statusChange, traps=traps, base=base, sun=sun, moduleInfo=moduleInfo, statusOID=statusOID)
