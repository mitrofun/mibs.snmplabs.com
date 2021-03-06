#
# PySNMP MIB module BASIS-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BASIS-SERIAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
basisLines, = mibBuilder.importSymbols("BASIS-MIB", "basisLines")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Gauge32, Counter32, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter32", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basisSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 69))
basisSerialMIB.setRevisions(('2003-05-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: basisSerialMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in CISCO-WAN-AXIPOP-MIB defined using SMIv1. The applicable objects from CISCO-WAN-AXIPOP-MIB are defined using SMIv2 in this MIB. Also the descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: basisSerialMIB.setLastUpdated('200305030000Z')
if mibBuilder.loadTexts: basisSerialMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: basisSerialMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: basisSerialMIB.setDescription('The MIB module to configure serial ports in Processor Module and different Service Modules(cards) in MGX8850,MGX8250 and MGX8220 ATM Edge switches.')
serialInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 1))
serialPortNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNumOfValidEntries.setStatus('current')
if mibBuilder.loadTexts: serialPortNumOfValidEntries.setDescription('This object contains number of serial ports. This identifies the number of entries in serialInterfacetable.')
serialInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1), )
if mibBuilder.loadTexts: serialInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: serialInterfaceTable.setDescription('This table represents Physical serial interfaces in the module.')
serialInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1), ).setIndexNames((0, "BASIS-SERIAL-MIB", "serialPortNum"))
if mibBuilder.loadTexts: serialInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: serialInterfaceEntry.setDescription('An entry for each serial interface. Each entry contains information on port type, port speed.')
serialPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNum.setStatus('current')
if mibBuilder.loadTexts: serialPortNum.setDescription('This object identifies the serial port number. The value 1 is used for Console Port. The Console Port is also known as control port(CP). The value 2 is used for Maintenance Port and this can be used as SLIP (Serial Line Internet Protocol) interface. The Maintenance Port is also known as Modem Port(MP).')
serialPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("main", 1), ("debug", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortType.setStatus('current')
if mibBuilder.loadTexts: serialPortType.setDescription('This object identifies the type of port. main(1) : This is applicable for Maintenance Port debug(2) : This is applicable for Console Port.')
serialPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortEnable.setStatus('current')
if mibBuilder.loadTexts: serialPortEnable.setDescription('This object is used for enabling/disabling serial port.')
serialPortbps = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bps9600", 1), ("bps2400", 2), ("bps19200", 3))).clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortbps.setStatus('current')
if mibBuilder.loadTexts: serialPortbps.setDescription('This object identifies the baud rate of the ports.')
basisSerialMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2))
basisSerialMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1))
basisSerialMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2))
basisSerialCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2, 1)).setObjects(("BASIS-SERIAL-MIB", "basisSerialConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialCompliance = basisSerialCompliance.setStatus('current')
if mibBuilder.loadTexts: basisSerialCompliance.setDescription('The compliance statement for objects related to Serial Ports.')
basisSerialConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1, 1)).setObjects(("BASIS-SERIAL-MIB", "serialPortNumOfValidEntries"), ("BASIS-SERIAL-MIB", "serialPortNum"), ("BASIS-SERIAL-MIB", "serialPortType"), ("BASIS-SERIAL-MIB", "serialPortEnable"), ("BASIS-SERIAL-MIB", "serialPortbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialConfGroup = basisSerialConfGroup.setStatus('current')
if mibBuilder.loadTexts: basisSerialConfGroup.setDescription('The collection of objects which are used to represent serial ports.')
mibBuilder.exportSymbols("BASIS-SERIAL-MIB", basisSerialConfGroup=basisSerialConfGroup, basisSerialMIBConformance=basisSerialMIBConformance, serialInterfaceEntry=serialInterfaceEntry, serialPortNum=serialPortNum, basisSerialMIBCompliances=basisSerialMIBCompliances, basisSerialCompliance=basisSerialCompliance, serialPortNumOfValidEntries=serialPortNumOfValidEntries, serialInterfaceTable=serialInterfaceTable, serialInterface=serialInterface, PYSNMP_MODULE_ID=basisSerialMIB, basisSerialMIB=basisSerialMIB, serialPortbps=serialPortbps, serialPortEnable=serialPortEnable, basisSerialMIBGroups=basisSerialMIBGroups, serialPortType=serialPortType)
