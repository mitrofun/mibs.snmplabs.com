#
# PySNMP MIB module ALCATEL-IND1-IPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-IPSEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1IPsec, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1IPsec")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ObjectIdentity, IpAddress, Counter32, ModuleIdentity, Counter64, Gauge32, Unsigned32, iso, Bits, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ObjectIdentity", "IpAddress", "Counter32", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "iso", "Bits", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
alcatelIND1IPsecMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1))
alcatelIND1IPsecMIB.setRevisions(('2010-07-20 00:00',))
if mibBuilder.loadTexts: alcatelIND1IPsecMIB.setLastUpdated('201007200000Z')
if mibBuilder.loadTexts: alcatelIND1IPsecMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1IPsecMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1))
class IPsecDescription(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class IPsecPortNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IPsecPrefixLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 128)

class IPsecULProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class IPsecAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class IPsecSAType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("ah", 2), ("esp", 3))

class IPsecESPAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 11, 12, 13))
    namedValues = NamedValues(("none", 0), ("descbc", 2), ("des3cbc", 3), ("null", 11), ("aescbc", 12), ("aesctr", 13))

class IPsecAHAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 9))
    namedValues = NamedValues(("none", 0), ("hmacmd5", 2), ("hmacsha1", 3), ("aesxcbcmac", 9))

class IPsecOperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("dnspending", 3))

alaIPsecConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1))
alaIPsecSecurityKeyTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaIPsecSecurityKeyTable.setStatus('current')
alaIPsecSecurityKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyID"))
if mibBuilder.loadTexts: alaIPsecSecurityKeyEntry.setStatus('current')
alaIPsecSecurityKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaIPsecSecurityKeyID.setStatus('current')
alaIPsecSecurityKeyCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIPsecSecurityKeyCurrent.setStatus('current')
alaIPsecSecurityKeyNew = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIPsecSecurityKeyNew.setStatus('current')
alaIPsecStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2), )
if mibBuilder.loadTexts: alaIPsecStatisticsTable.setStatus('deprecated')
alaIPsecStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsProtocol"))
if mibBuilder.loadTexts: alaIPsecStatisticsEntry.setStatus('deprecated')
alaIPsecStatisticsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6))).clone(namedValues=NamedValues(("ipv6", 6))))
if mibBuilder.loadTexts: alaIPsecStatisticsProtocol.setStatus('deprecated')
alaIPsecStatisticsInSuccessful = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInSuccessful.setStatus('deprecated')
alaIPsecStatisticsInPolicyViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInPolicyViolation.setStatus('deprecated')
alaIPsecStatisticsInNoSA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInNoSA.setStatus('deprecated')
alaIPsecStatisticsInUnknownSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInUnknownSPI.setStatus('deprecated')
alaIPsecStatisticsInAHReplay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInAHReplay.setStatus('deprecated')
alaIPsecStatisticsInESPReplay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInESPReplay.setStatus('deprecated')
alaIPsecStatisticsInAHAuthenticationSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInAHAuthenticationSuccess.setStatus('deprecated')
alaIPsecStatisticsInAHAuthenticationFail = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInAHAuthenticationFail.setStatus('deprecated')
alaIPsecStatisticsInESPAuthenticationSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInESPAuthenticationSuccess.setStatus('deprecated')
alaIPsecStatisticsInESPAuthenticationFail = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInESPAuthenticationFail.setStatus('deprecated')
alaIPsecStatisticsInBadPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInBadPacket.setStatus('deprecated')
alaIPsecStatisticsInNoMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInNoMemory.setStatus('deprecated')
alaIPsecStatisticsOutSuccessful = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutSuccessful.setStatus('deprecated')
alaIPsecStatisticsOutPolicyViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutPolicyViolation.setStatus('deprecated')
alaIPsecStatisticsOutNoSA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutNoSA.setStatus('deprecated')
alaIPsecStatisticsOutBadPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutBadPacket.setStatus('deprecated')
alaIPsecStatisticsOutNoMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutNoMemory.setStatus('deprecated')
alaIPsecStatisticsInDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsInDiscarded.setStatus('deprecated')
alaIPsecStatisticsOutDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecStatisticsOutDiscarded.setStatus('deprecated')
alaIPsecSecurityPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2), )
if mibBuilder.loadTexts: alaIPsecSecurityPolicyTable.setStatus('current')
alaIPsecSecurityPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyID"))
if mibBuilder.loadTexts: alaIPsecSecurityPolicyEntry.setStatus('current')
alaIPsecSecurityPolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaIPsecSecurityPolicyID.setStatus('current')
alaIPsecSecurityPolicySourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicySourceType.setStatus('current')
alaIPsecSecurityPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicySource.setStatus('current')
alaIPsecSecurityPolicySourcePrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 4), IPsecPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicySourcePrefixLength.setStatus('current')
alaIPsecSecurityPolicySourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 5), IPsecPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicySourcePort.setStatus('current')
alaIPsecSecurityPolicyDestinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDestinationType.setStatus('current')
alaIPsecSecurityPolicyDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDestination.setStatus('current')
alaIPsecSecurityPolicyDestinationPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 8), IPsecPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDestinationPrefixLength.setStatus('current')
alaIPsecSecurityPolicyDestinationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 9), IPsecPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDestinationPort.setStatus('current')
alaIPsecSecurityPolicyULProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 10), IPsecULProtocol().clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyULProtocol.setStatus('current')
alaIPsecSecurityPolicyICMPv6Type = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyICMPv6Type.setStatus('current')
alaIPsecSecurityPolicyDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDirection.setStatus('current')
alaIPsecSecurityPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyName.setStatus('current')
alaIPsecSecurityPolicyDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 14), IPsecDescription()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyDescription.setStatus('current')
alaIPsecSecurityPolicyAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("discard", 0), ("none", 1), ("ipsec", 2))).clone('ipsec')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyAction.setStatus('current')
alaIPsecSecurityPolicyAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 16), IPsecAdminState().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyAdminState.setStatus('current')
alaIPsecSecurityPolicyOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 17), IPsecOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyOperationalState.setStatus('current')
alaIPsecSecurityPolicyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyPriority.setStatus('current')
alaIPsecSecurityPolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 2, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRowStatus.setStatus('current')
alaIPsecSecurityPolicyRuleTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3), )
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleTable.setStatus('current')
alaIPsecSecurityPolicyRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyID"), (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleIndex"))
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleEntry.setStatus('current')
alaIPsecSecurityPolicyRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleIndex.setStatus('current')
alaIPsecSecurityPolicyRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ah", 1), ("esp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleProtocol.setStatus('current')
alaIPsecSecurityPolicyRuleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("transport", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleMode.setStatus('current')
alaIPsecSecurityPolicyRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSecurityPolicyRuleRowStatus.setStatus('current')
alaIPsecSAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4), )
if mibBuilder.loadTexts: alaIPsecSAConfigTable.setStatus('current')
alaIPsecSAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigID"))
if mibBuilder.loadTexts: alaIPsecSAConfigEntry.setStatus('current')
alaIPsecSAConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaIPsecSAConfigID.setStatus('current')
alaIPsecSAConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 2), IPsecSAType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigType.setStatus('current')
alaIPsecSAConfigSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigSourceType.setStatus('current')
alaIPsecSAConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigSource.setStatus('current')
alaIPsecSAConfigDestinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigDestinationType.setStatus('current')
alaIPsecSAConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigDestination.setStatus('current')
alaIPsecSAConfigSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigSPI.setStatus('current')
alaIPsecSAConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigName.setStatus('current')
alaIPsecSAConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 9), IPsecDescription()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigDescription.setStatus('current')
alaIPsecSAConfigEncryptionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 10), IPsecESPAlgorithm().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigEncryptionAlgorithm.setStatus('current')
alaIPsecSAConfigEncryptionKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 11), Unsigned32()).setUnits('bits').setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigEncryptionKeyLength.setStatus('current')
alaIPsecSAConfigAuthenticationAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 12), IPsecAHAlgorithm().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigAuthenticationAlgorithm.setStatus('current')
alaIPsecSAConfigAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 13), IPsecAdminState().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigAdminState.setStatus('current')
alaIPsecSAConfigOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 14), IPsecOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecSAConfigOperationalState.setStatus('current')
alaIPsecSAConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 4, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecSAConfigRowStatus.setStatus('current')
alaIPsecKeyTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5), )
if mibBuilder.loadTexts: alaIPsecKeyTable.setStatus('current')
alaIPsecKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyID"))
if mibBuilder.loadTexts: alaIPsecKeyEntry.setStatus('current')
alaIPsecKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaIPsecKeyID.setStatus('current')
alaIPsecKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("saAuthentication", 1), ("saEncryption", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecKeyType.setStatus('current')
alaIPsecKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecKeyName.setStatus('current')
alaIPsecKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecKey.setStatus('current')
alaIPsecKeyEncrypted = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecKeyEncrypted.setStatus('current')
alaIPsecKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIPsecKeyRowStatus.setStatus('current')
alaIPsecErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6), )
if mibBuilder.loadTexts: alaIPsecErrorsTable.setStatus('current')
alaIPsecErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1), ).setIndexNames((0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsProtocol"))
if mibBuilder.loadTexts: alaIPsecErrorsEntry.setStatus('current')
alaIPsecErrorsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6))).clone(namedValues=NamedValues(("ipv6", 6))))
if mibBuilder.loadTexts: alaIPsecErrorsProtocol.setStatus('current')
alaIPsecErrorsInPolicyViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInPolicyViolation.setStatus('current')
alaIPsecErrorsInNoSA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInNoSA.setStatus('current')
alaIPsecErrorsInReplay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInReplay.setStatus('current')
alaIPsecErrorsInAuthenticationFail = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInAuthenticationFail.setStatus('current')
alaIPsecErrorsInDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInDiscarded.setStatus('current')
alaIPsecErrorsInOther = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsInOther.setStatus('current')
alaIPsecErrorsOutNoSA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsOutNoSA.setStatus('current')
alaIPsecErrorsOutDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsOutDiscarded.setStatus('current')
alaIPsecErrorsOutOther = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIPsecErrorsOutOther.setStatus('current')
alcatelIND1IPsecMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2))
alcatelIND1IPsecMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 1))
alcatelIND1IPsecMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2))
alaIPsecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecConfigGroup"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyGroup"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigGroup"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyGroup"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecCountersGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecCompliance = alaIPsecCompliance.setStatus('current')
alaIPsecConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyCurrent"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyNew"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecConfigGroup = alaIPsecConfigGroup.setStatus('current')
alaIPsecSecurityPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 2)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySource"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourceType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourcePrefixLength"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourcePort"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestination"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationPrefixLength"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationPort"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyULProtocol"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyICMPv6Type"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDirection"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyName"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDescription"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyAction"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyAdminState"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyOperationalState"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyPriority"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRowStatus"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleProtocol"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleMode"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecSecurityPolicyGroup = alaIPsecSecurityPolicyGroup.setStatus('current')
alaIPsecSAConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 3)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSource"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSourceType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDestination"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDestinationType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSPI"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigName"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDescription"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigEncryptionAlgorithm"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigEncryptionKeyLength"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigAuthenticationAlgorithm"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigAdminState"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigOperationalState"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecSAConfigGroup = alaIPsecSAConfigGroup.setStatus('current')
alaIPsecKeyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 4)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyType"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyName"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKey"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyEncrypted"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecKeyGroup = alaIPsecKeyGroup.setStatus('current')
alaIPsecCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 5)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInPolicyViolation"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInNoSA"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInReplay"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInAuthenticationFail"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInDiscarded"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsInOther"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsOutNoSA"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsOutDiscarded"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecErrorsOutOther"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecCountersGroup = alaIPsecCountersGroup.setStatus('current')
alaIPsecStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43, 1, 2, 2, 6)).setObjects(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInSuccessful"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInPolicyViolation"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInNoSA"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInUnknownSPI"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHReplay"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPReplay"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHAuthenticationSuccess"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHAuthenticationFail"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPAuthenticationSuccess"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPAuthenticationFail"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInBadPacket"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInNoMemory"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutSuccessful"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutPolicyViolation"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutNoSA"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutBadPacket"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutNoMemory"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInDiscarded"), ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutDiscarded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIPsecStatisticsGroup = alaIPsecStatisticsGroup.setStatus('deprecated')
mibBuilder.exportSymbols("ALCATEL-IND1-IPSEC-MIB", alaIPsecSecurityPolicySourcePort=alaIPsecSecurityPolicySourcePort, alaIPsecSecurityPolicyPriority=alaIPsecSecurityPolicyPriority, alaIPsecSecurityPolicyOperationalState=alaIPsecSecurityPolicyOperationalState, alaIPsecStatisticsOutPolicyViolation=alaIPsecStatisticsOutPolicyViolation, alaIPsecErrorsOutOther=alaIPsecErrorsOutOther, alaIPsecSecurityPolicyDestinationPrefixLength=alaIPsecSecurityPolicyDestinationPrefixLength, alaIPsecSecurityKeyEntry=alaIPsecSecurityKeyEntry, alaIPsecConfigGroup=alaIPsecConfigGroup, alaIPsecStatisticsInESPReplay=alaIPsecStatisticsInESPReplay, alaIPsecCompliance=alaIPsecCompliance, alaIPsecErrorsInAuthenticationFail=alaIPsecErrorsInAuthenticationFail, alaIPsecStatisticsInAHAuthenticationFail=alaIPsecStatisticsInAHAuthenticationFail, alaIPsecConfig=alaIPsecConfig, alaIPsecStatisticsInUnknownSPI=alaIPsecStatisticsInUnknownSPI, alaIPsecSAConfigAuthenticationAlgorithm=alaIPsecSAConfigAuthenticationAlgorithm, IPsecOperationalState=IPsecOperationalState, alaIPsecSecurityPolicyGroup=alaIPsecSecurityPolicyGroup, alaIPsecSecurityKeyNew=alaIPsecSecurityKeyNew, alaIPsecKeyName=alaIPsecKeyName, alaIPsecSecurityKeyTable=alaIPsecSecurityKeyTable, alaIPsecErrorsProtocol=alaIPsecErrorsProtocol, alaIPsecSAConfigEncryptionAlgorithm=alaIPsecSAConfigEncryptionAlgorithm, alaIPsecSAConfigGroup=alaIPsecSAConfigGroup, alcatelIND1IPsecMIB=alcatelIND1IPsecMIB, alaIPsecSecurityPolicyDestinationType=alaIPsecSecurityPolicyDestinationType, alaIPsecStatisticsTable=alaIPsecStatisticsTable, alaIPsecSecurityPolicyDescription=alaIPsecSecurityPolicyDescription, alaIPsecSecurityPolicyRowStatus=alaIPsecSecurityPolicyRowStatus, IPsecULProtocol=IPsecULProtocol, alaIPsecSecurityPolicyDestinationPort=alaIPsecSecurityPolicyDestinationPort, PYSNMP_MODULE_ID=alcatelIND1IPsecMIB, IPsecPortNumber=IPsecPortNumber, alaIPsecKeyRowStatus=alaIPsecKeyRowStatus, alaIPsecStatisticsInPolicyViolation=alaIPsecStatisticsInPolicyViolation, alaIPsecKeyID=alaIPsecKeyID, IPsecDescription=IPsecDescription, alaIPsecKeyEncrypted=alaIPsecKeyEncrypted, alaIPsecSecurityPolicyAdminState=alaIPsecSecurityPolicyAdminState, alaIPsecSAConfigRowStatus=alaIPsecSAConfigRowStatus, alaIPsecStatisticsGroup=alaIPsecStatisticsGroup, alaIPsecStatisticsInESPAuthenticationFail=alaIPsecStatisticsInESPAuthenticationFail, alaIPsecSecurityPolicyAction=alaIPsecSecurityPolicyAction, alaIPsecSecurityPolicySourceType=alaIPsecSecurityPolicySourceType, alaIPsecKeyTable=alaIPsecKeyTable, alaIPsecSecurityKeyCurrent=alaIPsecSecurityKeyCurrent, alaIPsecStatisticsInNoMemory=alaIPsecStatisticsInNoMemory, IPsecESPAlgorithm=IPsecESPAlgorithm, alaIPsecStatisticsOutDiscarded=alaIPsecStatisticsOutDiscarded, alaIPsecStatisticsInDiscarded=alaIPsecStatisticsInDiscarded, alaIPsecSecurityPolicyRuleIndex=alaIPsecSecurityPolicyRuleIndex, alaIPsecErrorsOutNoSA=alaIPsecErrorsOutNoSA, alaIPsecSecurityPolicyDestination=alaIPsecSecurityPolicyDestination, alaIPsecSecurityPolicyULProtocol=alaIPsecSecurityPolicyULProtocol, alaIPsecStatisticsOutSuccessful=alaIPsecStatisticsOutSuccessful, alaIPsecSAConfigType=alaIPsecSAConfigType, alaIPsecSAConfigOperationalState=alaIPsecSAConfigOperationalState, alaIPsecStatisticsInBadPacket=alaIPsecStatisticsInBadPacket, alcatelIND1IPsecMIBGroups=alcatelIND1IPsecMIBGroups, alaIPsecSAConfigEncryptionKeyLength=alaIPsecSAConfigEncryptionKeyLength, alaIPsecStatisticsInAHAuthenticationSuccess=alaIPsecStatisticsInAHAuthenticationSuccess, alaIPsecStatisticsOutBadPacket=alaIPsecStatisticsOutBadPacket, alaIPsecSAConfigID=alaIPsecSAConfigID, alaIPsecSAConfigAdminState=alaIPsecSAConfigAdminState, alaIPsecKeyType=alaIPsecKeyType, alaIPsecStatisticsEntry=alaIPsecStatisticsEntry, alaIPsecErrorsOutDiscarded=alaIPsecErrorsOutDiscarded, alaIPsecSecurityPolicyID=alaIPsecSecurityPolicyID, alaIPsecSAConfigTable=alaIPsecSAConfigTable, alaIPsecSAConfigSourceType=alaIPsecSAConfigSourceType, alaIPsecSAConfigSource=alaIPsecSAConfigSource, alcatelIND1IPsecMIBCompliances=alcatelIND1IPsecMIBCompliances, alaIPsecSecurityPolicyName=alaIPsecSecurityPolicyName, alaIPsecSecurityKeyID=alaIPsecSecurityKeyID, alaIPsecErrorsInDiscarded=alaIPsecErrorsInDiscarded, alcatelIND1IPsecMIBConformance=alcatelIND1IPsecMIBConformance, alaIPsecSecurityPolicyRuleTable=alaIPsecSecurityPolicyRuleTable, alaIPsecErrorsInPolicyViolation=alaIPsecErrorsInPolicyViolation, alaIPsecStatisticsOutNoSA=alaIPsecStatisticsOutNoSA, alaIPsecSAConfigName=alaIPsecSAConfigName, alaIPsecSecurityPolicySourcePrefixLength=alaIPsecSecurityPolicySourcePrefixLength, alaIPsecKeyGroup=alaIPsecKeyGroup, alaIPsecStatisticsInAHReplay=alaIPsecStatisticsInAHReplay, alaIPsecKeyEntry=alaIPsecKeyEntry, alaIPsecErrorsInOther=alaIPsecErrorsInOther, alaIPsecErrorsEntry=alaIPsecErrorsEntry, alaIPsecStatisticsInNoSA=alaIPsecStatisticsInNoSA, alaIPsecSAConfigEntry=alaIPsecSAConfigEntry, alaIPsecStatisticsInSuccessful=alaIPsecStatisticsInSuccessful, alaIPsecSecurityPolicyICMPv6Type=alaIPsecSecurityPolicyICMPv6Type, alaIPsecErrorsTable=alaIPsecErrorsTable, alaIPsecErrorsInNoSA=alaIPsecErrorsInNoSA, alaIPsecCountersGroup=alaIPsecCountersGroup, alaIPsecErrorsInReplay=alaIPsecErrorsInReplay, IPsecAHAlgorithm=IPsecAHAlgorithm, alaIPsecStatisticsProtocol=alaIPsecStatisticsProtocol, alaIPsecSecurityPolicyRuleMode=alaIPsecSecurityPolicyRuleMode, alaIPsecSAConfigDescription=alaIPsecSAConfigDescription, alaIPsecSecurityPolicyTable=alaIPsecSecurityPolicyTable, alaIPsecSAConfigDestination=alaIPsecSAConfigDestination, alaIPsecSecurityPolicySource=alaIPsecSecurityPolicySource, alaIPsecSecurityPolicyDirection=alaIPsecSecurityPolicyDirection, IPsecSAType=IPsecSAType, alaIPsecSAConfigDestinationType=alaIPsecSAConfigDestinationType, alaIPsecSAConfigSPI=alaIPsecSAConfigSPI, alaIPsecStatisticsOutNoMemory=alaIPsecStatisticsOutNoMemory, alaIPsecSecurityPolicyRuleProtocol=alaIPsecSecurityPolicyRuleProtocol, alaIPsecSecurityPolicyRuleEntry=alaIPsecSecurityPolicyRuleEntry, IPsecAdminState=IPsecAdminState, IPsecPrefixLength=IPsecPrefixLength, alcatelIND1IPsecMIBObjects=alcatelIND1IPsecMIBObjects, alaIPsecStatisticsInESPAuthenticationSuccess=alaIPsecStatisticsInESPAuthenticationSuccess, alaIPsecSecurityPolicyEntry=alaIPsecSecurityPolicyEntry, alaIPsecSecurityPolicyRuleRowStatus=alaIPsecSecurityPolicyRuleRowStatus, alaIPsecKey=alaIPsecKey)