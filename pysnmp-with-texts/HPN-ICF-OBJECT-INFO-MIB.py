#
# PySNMP MIB module HPN-ICF-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Unsigned32, iso, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Unsigned32", "iso", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55))
hpnicfObjectInfo.setRevisions(('2004-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfObjectInfo.setRevisionsDescriptions((' The initial revision of this MIB module. ',))
if mibBuilder.loadTexts: hpnicfObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: hpnicfObjectInfo.setOrganization('')
if mibBuilder.loadTexts: hpnicfObjectInfo.setContactInfo('')
if mibBuilder.loadTexts: hpnicfObjectInfo.setDescription(' This MIB is used to acquire information from the agent. Before a NMS takes some actions, it is not sure whether the agent supports it or not. This MIB is used to solve this problem. ')
hpnicfObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1))
hpnicfObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1), )
if mibBuilder.loadTexts: hpnicfObjectInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoTable.setDescription(' MIB objects information query table. ')
hpnicfObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoOID"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoType"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTypeExtension"))
if mibBuilder.loadTexts: hpnicfObjectInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoEntry.setDescription(' The entry of hpnicfObjectInfoTable. ')
hpnicfObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: hpnicfObjectInfoOID.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoOID.setDescription(' The OID of the MIB object which is queried. If the user has no privilege accessing to the object referred by this OID, get operation on hpnicfObjectInfoValue will be failed. ')
hpnicfObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: hpnicfObjectInfoType.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoType.setDescription(" The object's properties type to be queried. The queried result will be returned by hpnicfObjectInfoValue. The format of the result will be different according to different hpnicfObjectInfoType. ")
hpnicfObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hpnicfObjectInfoTypeExtension.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoTypeExtension.setDescription(" The object's property type extension to be queried. This object's value is relative to the value of hpnicfObjectInfoType. ")
hpnicfObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfObjectInfoValue.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoValue.setDescription(" Return property value of the queried object. Zero length string is the default value of this object which means no value is returned. If the request is invalid, then the result should be the default value. If the value of hpnicfObjectInfoType is accessType, the rules below should be followed. 1) The returned value must have prefix 'A', and followed by some nonnegative integers. The format is like 'A2'. 2) The nonnegative integers and the meaning of them are as follow: 0 means 'not-accessible'. 1 means 'notification'. 2 means 'read-only'. 3 means 'read-write'. 4 means 'read-create'. 5 means 'write-only'. 6 means 'accessible-for-notify'. 7 means 'error'. --the above values are defined by standard protocol 101 means 'not implemented'. -- The queried node is not implemented by agent. 102 means 'unknown error'. -- Query failed for unknown reason. If the value of hpnicfObjectInfoType is dataType, the rules below should be followed. 1) The returned value must have prefix 'T', and followed by string which has format like 2), such as 'T1', the character '1' means INTEGER. 2) The following data types are defined in standard protocol, the values in brackets will be returned to indicate these data types. INTEGER(1) Integer32(2) Unsigned32(4) Gauge(6) Counter(7) Counter32(8) Counter64(9) TimeTicks(10) OCTET STRING(11) OBJECT IDENTIFIER(12) IpAddress(13) NetworkAddress(14) Opaque(15) BITS(16) If the value of hpnicfObjectInfoType is dataRange, the rules below should be followed. 1) The returned value must have prefix 'R', and followed by string which has the format like 2) to 5), such as 'R[1,1]'. 2) If hpnicfObjectInfoValue returns Integer32, the format is as followed. Suppose A is a MIB object. If SYNTAX of A is 'Integer32{1|2|3|5|6|7}', the format is 'R[1,3],[5,7]'. If SYNTAX of A is 'Integer32{1|3}', the format is 'R[1,1],[3,3]'. If SYNTAX of A is 'Integer32', the format is 'R[]' which means the default value range of Integer32 between -2147483648 and 2147483647. 3) The process of Counter, Counter32, Counter64, Unsigned32, Gauge32, INTEGER is the same as that of Integer32. 4) If SYNTAX of A is other types such as OCTET STRING, then this object returns default value 'R[]'. 5) If SYNTAX of A is 'BITS{a(0),b(1)}', the format is 'R[0,0],[1,1]'. If the value of hpnicfObjectInfoType is dataLength, the rules below should be followed. 1) The returned value must have prefix 'L', and followed by string which has the format like 2) to 4), such as 'L[6,6]'. 2) If SYNTAX of A is 'OCTET STRING(SIZE (6|10..255))', the format is 'L[6,6],[10,255]'. If SYNTAX of A is 'OCTET STRING', the format is like 'L[]' which means the default length of OCTET STRING between 0 and 65535. 3) If SYNTAX of A is BITS, the format of it is the same as OCTET STIRNG. But its unit is in bit, not in byte. 4) If SYNTAX of A is other types such as INTEGER and IpAddress, this object returns 'L[]'. ")
hpnicfObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2))
hpnicfObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1))
hpnicfObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoMIBCompliance = hpnicfObjectInfoMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoMIBCompliance.setDescription(' The compliance statement for implementing ObjectInfo MIB. ')
hpnicfObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2))
hpnicfObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoTableGroup = hpnicfObjectInfoTableGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfObjectInfoTableGroup.setDescription(' The basic collection of hpnicfObjectInfo table objects. ')
mibBuilder.exportSymbols("HPN-ICF-OBJECT-INFO-MIB", PYSNMP_MODULE_ID=hpnicfObjectInfo, hpnicfObjectInfoTable=hpnicfObjectInfoTable, hpnicfObjectInformation=hpnicfObjectInformation, hpnicfObjectInfoMIBCompliances=hpnicfObjectInfoMIBCompliances, hpnicfObjectInfoTypeExtension=hpnicfObjectInfoTypeExtension, hpnicfObjectInfoValue=hpnicfObjectInfoValue, hpnicfObjectInfoMIBCompliance=hpnicfObjectInfoMIBCompliance, hpnicfObjectInfoMIBGroups=hpnicfObjectInfoMIBGroups, hpnicfObjectInfo=hpnicfObjectInfo, hpnicfObjectInfoTableGroup=hpnicfObjectInfoTableGroup, hpnicfObjectInfoType=hpnicfObjectInfoType, hpnicfObjectInfoMIBConformance=hpnicfObjectInfoMIBConformance, hpnicfObjectInfoEntry=hpnicfObjectInfoEntry, hpnicfObjectInfoOID=hpnicfObjectInfoOID)
