#
# PySNMP MIB module DLINK-3100-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:49:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, Counter64, NotificationType, TimeTicks, iso, MibIdentifier, Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Counter64", "NotificationType", "TimeTicks", "iso", "MibIdentifier", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107))
rlStack.setRevisions(('2005-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlStack.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlStack.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlStack.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: rlStack.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlStack.setDescription('The private MIB module definition for stack.')
rlStackActiveUnitIdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 1), )
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setDescription(' The table listing the active unit id of the requested unit.')
rlStackActiveUnitIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 1, 1), ).setIndexNames((0, "DLINK-3100-STACK-MIB", "rlStackCurrentUnitId"))
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setDescription(' An entry in the rlStackActiveUnitIdTable.')
rlStackCurrentUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlStackCurrentUnitId.setStatus('current')
if mibBuilder.loadTexts: rlStackCurrentUnitId.setDescription('The unit number device, which is the active unit id')
rlStackActiveUnitIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setDescription('Indicates the unit id that will be after reset.')
rlStackUnitModeAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setDescription('set unit type that will be after reset, standalone or stack.')
rlStackUnitMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 107, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackUnitMode.setStatus('current')
if mibBuilder.loadTexts: rlStackUnitMode.setDescription('show unit type standalone or stack.')
mibBuilder.exportSymbols("DLINK-3100-STACK-MIB", rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackUnitMode=rlStackUnitMode, rlStackCurrentUnitId=rlStackCurrentUnitId, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, PYSNMP_MODULE_ID=rlStack, rlStack=rlStack, rlStackUnitModeAfterReset=rlStackUnitModeAfterReset)