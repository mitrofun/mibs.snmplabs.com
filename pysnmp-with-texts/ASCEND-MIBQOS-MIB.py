#
# PySNMP MIB module ASCEND-MIBQOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBQOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, Integer32, Counter64, Counter32, MibIdentifier, NotificationType, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "Integer32", "Counter64", "Counter32", "MibIdentifier", "NotificationType", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibqosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 169))
mibqosProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 169, 1), )
if mibBuilder.loadTexts: mibqosProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibqosProfileTable.setDescription('A list of mibqosProfile profile entries.')
mibqosProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1), ).setIndexNames((0, "ASCEND-MIBQOS-MIB", "qosProfile-Index-o"))
if mibBuilder.loadTexts: mibqosProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibqosProfileEntry.setDescription('A mibqosProfile entry containing objects that maps to the parameters of mibqosProfile profile.')
qosProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 1), Integer32()).setLabel("qosProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: qosProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_Index_o.setDescription('')
qosProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("qosProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_Enabled.setDescription('System QoS support Enabled/Disabled')
qosProfile_AllowClientDscp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("qosProfile-AllowClientDscp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_AllowClientDscp.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_AllowClientDscp.setDescription('System QoS support Enabled/Disabled')
qosProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("qosProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_Action_o.setDescription('')
mibqosProfile_TagMapTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 169, 2), ).setLabel("mibqosProfile-TagMapTable")
if mibBuilder.loadTexts: mibqosProfile_TagMapTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibqosProfile_TagMapTable.setDescription('A list of mibqosProfile__tag_map profile entries.')
mibqosProfile_TagMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1), ).setLabel("mibqosProfile-TagMapEntry").setIndexNames((0, "ASCEND-MIBQOS-MIB", "qosProfile-TagMap-Index-o"), (0, "ASCEND-MIBQOS-MIB", "qosProfile-TagMap-Index1-o"))
if mibBuilder.loadTexts: mibqosProfile_TagMapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibqosProfile_TagMapEntry.setDescription('A mibqosProfile__tag_map entry containing objects that maps to the parameters of mibqosProfile__tag_map profile.')
qosProfile_TagMap_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 1), Integer32()).setLabel("qosProfile-TagMap-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: qosProfile_TagMap_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_TagMap_Index_o.setDescription('')
qosProfile_TagMap_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 2), Integer32()).setLabel("qosProfile-TagMap-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: qosProfile_TagMap_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_TagMap_Index1_o.setDescription('')
qosProfile_TagMap_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("qosProfile-TagMap-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_TagMap_Active.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_TagMap_Active.setDescription('Mapping Enabled/Disabled.')
qosProfile_TagMap_Dscp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 4), DisplayString()).setLabel("qosProfile-TagMap-Dscp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_TagMap_Dscp.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_TagMap_Dscp.setDescription('Match DSCP value to be used to set the QOS Tag.')
qosProfile_TagMap_QosTag = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 169, 2, 1, 5), Integer32()).setLabel("qosProfile-TagMap-QosTag").setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosProfile_TagMap_QosTag.setStatus('mandatory')
if mibBuilder.loadTexts: qosProfile_TagMap_QosTag.setDescription('QOS Tag to be used with the matche IP TOS byte.')
mibBuilder.exportSymbols("ASCEND-MIBQOS-MIB", mibqosProfileEntry=mibqosProfileEntry, qosProfile_TagMap_Active=qosProfile_TagMap_Active, mibqosProfile_TagMapTable=mibqosProfile_TagMapTable, mibqosProfileTable=mibqosProfileTable, qosProfile_Index_o=qosProfile_Index_o, mibqosProfile_TagMapEntry=mibqosProfile_TagMapEntry, qosProfile_TagMap_Index1_o=qosProfile_TagMap_Index1_o, DisplayString=DisplayString, mibqosProfile=mibqosProfile, qosProfile_Enabled=qosProfile_Enabled, qosProfile_AllowClientDscp=qosProfile_AllowClientDscp, qosProfile_TagMap_QosTag=qosProfile_TagMap_QosTag, qosProfile_TagMap_Index_o=qosProfile_TagMap_Index_o, qosProfile_TagMap_Dscp=qosProfile_TagMap_Dscp, qosProfile_Action_o=qosProfile_Action_o)
