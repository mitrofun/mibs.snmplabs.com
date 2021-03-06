#
# PySNMP MIB module DOCS-BPI2EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOCS-BPI2EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
DocsX509ASN1DEREncodedCertificate, = mibBuilder.importSymbols("DOCS-IETF-BPI2-MIB", "DocsX509ASN1DEREncodedCertificate")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, NotificationType, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, MibIdentifier, Integer32, IpAddress, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "MibIdentifier", "Integer32", "IpAddress", "Bits", "ObjectIdentity")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
docsBpi2Ext31Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29))
docsBpi2Ext31Mib.setRevisions(('2017-04-13 00:00', '2016-10-20 00:00', '2016-05-05 00:00', '2016-01-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: docsBpi2Ext31Mib.setRevisionsDescriptions(('Revised Version includes ECN DOCS-BPI2EXT-MIB-N-17.1710-1.', 'Revised Version includes ECN DOCS-BPI2EXT-MIB-N-16.1611-2.', 'Revised Version includes ECN CCAP-OSSIv3.1-N-16.1505-2.', 'Initial version, per ECN CM-OSSIv3.1-N-15.1393-6.',))
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setLastUpdated('201704130000Z')
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setContactInfo(' Postal: Cable Television Laboratories, Inc. 858 Coal Creek Circle Louisville, Colorado 80027-9750 U.S.A. Phone: +1 303-661-9100 Fax: +1 303-661-9199 E-mail: mibs@cablelabs.com')
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setDescription('This MIB module adds to the BPI management objects that are defined in the DOCS-IETF-BPI2-MIB (RFC 4131). These objects are in addition to and the DOCS-IETF-BPI2-MIB (RFC 4131). These objects are in addition to and separate from RFC 4131 and provide management support for new DOCSIS 3.1 features. The following MIBs from RFC 4131 are used to support legacy PKI CM certificate functions defined in the DOCSIS 3.0 security specification: docsBpi2CmDeviceCertTable, docsBpi2CodeMfgOrgName, docsBpi2CodeMfgCodeAccessStart, docsBpi2CodeMfgCvcAccessStart, docsBpi2CodeCoSignerOrgName, docsBpi2CodeCoSignerCodeAccessStart, docsBpi2CodeCoSignerCvcAccessStart, docsBpi2CodeCvcUpdate. The following MIBs defined in this MIB module are used to support new PKI CM certificate functions defined in the DOCSIS 3.1 security specification: docsBpi2Ext31CmDeviceCmCert, docsBpi2Ext31CodeUpdateCvcChain, docsBpi2Ext31CodeMfgOrgName, docsBpi2Ext31CodeMfgCodeAccessStart, docsBpi2Ext31CodeMfgCvcAccessStart, docsBpi2Ext31CodeCoSignerOrgName, docsBpi2Ext31CodeCoSignerCodeAccessStart, docsBpi2Ext31CodeCoSignerCvcAccessStart. Copyright 2015-2017 Cable Television Laboratories, Inc. All rights reserved.')
class DocsCvcCaCertificateChain(TextualConvention, OctetString):
    description = 'A degenerate PKCS7 signedData structure that contains the CVC and the CVC CA certificate chain in the certificates field.'
    status = 'current'
    displayHint = '50x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8192)

docsBpi2Ext31Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 0))
docsBpi2Ext31MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1))
docsBpi2Ext31Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2))
docsBpi2Ext31Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1))
docsBpi2Ext31Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2))
docsBpi2Ext31CmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1))
docsBpi2Ext31CmCertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1))
docsBpi2Ext31CodeDownloadControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2))
docsBpi2Ext31CmDeviceCertTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1), )
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertTable.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertTable.setDescription('This table describes the Baseline Privacy Plus device certificates issued from the new PKI defined in DOCSIS 3.1 for each CM MAC interface.')
docsBpi2Ext31CmDeviceCertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertEntry.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertEntry.setDescription('Each entry contains the device certificates of one CM MAC interface. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127).')
docsBpi2Ext31CmDeviceCmCert = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 1), DocsX509ASN1DEREncodedCertificate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCmCert.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCmCert.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCmCert.setDescription("The X509 DER-encoded cable modem certificate. Note: This object can be set only when the value is the zero-length OCTET STRING; otherwise, an error of 'inconsistentValue' is returned. Once the object contains the certificate, its access MUST be read-only and persists after re-initialization of the managed system.")
docsBpi2Ext31CmDeviceManufCert = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 2), DocsX509ASN1DEREncodedCertificate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceManufCert.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceManufCert.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceManufCert.setDescription('The X509 DER-encoded manufacturer certificate that signed the cable modem certificate.')
docsBpi2Ext31CodeUpdateCvcChain = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 1), DocsCvcCaCertificateChain()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsBpi2Ext31CodeUpdateCvcChain.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section')
if mibBuilder.loadTexts: docsBpi2Ext31CodeUpdateCvcChain.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeUpdateCvcChain.setDescription('The value of this object is a degenerate PKCS7 signedData structure that contains the CVC and the CVC CA certificate chain in the certificates field. Setting this object triggers the device to verify the CVC and update the cvcAccessStart values associated with the new PKI defined by DOCSIS 3.1. The content of this object is then discarded. If the device is not enabled to upgrade codefiles, or if the CVC verification fails, the CVC will be rejected. Reading this object always returns the zero-length OCTET STRING.')
docsBpi2Ext31CodeMfgOrgName = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgOrgName.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgOrgName.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgOrgName.setDescription("The value of this object is the device manufacturer's organizationName used to validate the code verification certificate issued from the new PKI defined in DOCSIS 3.1.")
docsBpi2Ext31CodeMfgCodeAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 3), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCodeAccessStart.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section ')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCodeAccessStart.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCodeAccessStart.setDescription("The value of this object is the device manufacturer's current codeAccessStart value used with the new PKI defined in DOCSIS 3.1. This value will always refer to Greenwich Mean Time (GMT), and the value format must contain TimeZone information (fields 8-10).")
docsBpi2Ext31CodeMfgCvcAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 4), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCvcAccessStart.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section ')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCvcAccessStart.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCvcAccessStart.setDescription("The value of this object is the device manufacturer's current cvcAccessStart value used with the new PKI defined in DOCSIS 3.1. This value will always refer to Greenwich Mean Time (GMT), and the value format must contain TimeZone information (fields 8-10).")
docsBpi2Ext31CodeCoSignerOrgName = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerOrgName.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section ')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerOrgName.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerOrgName.setDescription("The value of this object is the co-signer's organizationName used to validate the code verification certificate issued from the new PKI defined in DOCSIS 3.1. The value is a zero length string if the co-signer is not specified.")
docsBpi2Ext31CodeCoSignerCodeAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCodeAccessStart.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section ')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCodeAccessStart.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCodeAccessStart.setDescription("The value of this object is the co-signer's current codeAccessStart value used with the new PKI defined in DOCSIS 3.1. This value will always refer to Greenwich Mean Time (GMT), and the value format must contain TimeZone information (fields 8-10). If docsBpi2CodeCoSignerOrgName is a zero length string, the value of this object is meaningless.")
docsBpi2Ext31CodeCoSignerCvcAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 7), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCvcAccessStart.setReference('DOCSIS 3.1 Security Specification, CM-SP-SECv3.1-I02-150326, Secure Software Download Section ')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCvcAccessStart.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCvcAccessStart.setDescription("The value of this object is the co-signer's current cvcAccessStart value used with the new PKI defined in DOCSIS 3.1. This value will always refer to Greenwich Mean Time (GMT), and the value format must contain TimeZone information (fields 8-10). If docsBpi2CodeCoSignerOrgName is a zero-length string, the value of this object is meaningless.")
docsBpi2Ext31MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1, 1)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmGroup"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31BaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31MIBCompliance = docsBpi2Ext31MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31MIBCompliance.setDescription('The compliance statement for implementations of the DOC-BPI2EXT-MIB.')
docsBpi2Ext31CmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 1)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceCmCert"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceManufCert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31CmGroup = docsBpi2Ext31CmGroup.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31CmGroup.setDescription('The group of objects implemented by the CM.')
docsBpi2Ext31BaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 2)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeUpdateCvcChain"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgOrgName"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCodeAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCvcAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerOrgName"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCodeAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCvcAccessStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31BaseGroup = docsBpi2Ext31BaseGroup.setStatus('current')
if mibBuilder.loadTexts: docsBpi2Ext31BaseGroup.setDescription('The group of objects implemented by the CM and open to implementation by other devices.')
mibBuilder.exportSymbols("DOCS-BPI2EXT-MIB", docsBpi2Ext31CmDeviceCmCert=docsBpi2Ext31CmDeviceCmCert, docsBpi2Ext31Mib=docsBpi2Ext31Mib, docsBpi2Ext31CodeCoSignerCvcAccessStart=docsBpi2Ext31CodeCoSignerCvcAccessStart, PYSNMP_MODULE_ID=docsBpi2Ext31Mib, docsBpi2Ext31CmDeviceCertEntry=docsBpi2Ext31CmDeviceCertEntry, docsBpi2Ext31CodeCoSignerCodeAccessStart=docsBpi2Ext31CodeCoSignerCodeAccessStart, docsBpi2Ext31CodeDownloadControl=docsBpi2Ext31CodeDownloadControl, docsBpi2Ext31CodeMfgOrgName=docsBpi2Ext31CodeMfgOrgName, docsBpi2Ext31Compliances=docsBpi2Ext31Compliances, docsBpi2Ext31CodeCoSignerOrgName=docsBpi2Ext31CodeCoSignerOrgName, docsBpi2Ext31CmObjects=docsBpi2Ext31CmObjects, docsBpi2Ext31CodeMfgCodeAccessStart=docsBpi2Ext31CodeMfgCodeAccessStart, docsBpi2Ext31CodeUpdateCvcChain=docsBpi2Ext31CodeUpdateCvcChain, docsBpi2Ext31BaseGroup=docsBpi2Ext31BaseGroup, DocsCvcCaCertificateChain=DocsCvcCaCertificateChain, docsBpi2Ext31CodeMfgCvcAccessStart=docsBpi2Ext31CodeMfgCvcAccessStart, docsBpi2Ext31Groups=docsBpi2Ext31Groups, docsBpi2Ext31Conformance=docsBpi2Ext31Conformance, docsBpi2Ext31CmCertObjects=docsBpi2Ext31CmCertObjects, docsBpi2Ext31CmDeviceCertTable=docsBpi2Ext31CmDeviceCertTable, docsBpi2Ext31MibObjects=docsBpi2Ext31MibObjects, docsBpi2Ext31CmDeviceManufCert=docsBpi2Ext31CmDeviceManufCert, docsBpi2Ext31MIBCompliance=docsBpi2Ext31MIBCompliance, docsBpi2Ext31Notifications=docsBpi2Ext31Notifications, docsBpi2Ext31CmGroup=docsBpi2Ext31CmGroup)
