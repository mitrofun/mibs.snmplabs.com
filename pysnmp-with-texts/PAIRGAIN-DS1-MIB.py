#
# PySNMP MIB module PAIRGAIN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-DS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Gauge32, Counter64, Counter32, enterprises, ObjectIdentity, MibIdentifier, NotificationType, iso, Unsigned32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Counter64", "Counter32", "enterprises", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Unsigned32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "DateAndTime")
pgds1Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 17))
if mibBuilder.loadTexts: pgds1Mib.setLastUpdated('0003030000Z')
if mibBuilder.loadTexts: pgds1Mib.setOrganization('Pairgain Technologies Inc.')
if mibBuilder.loadTexts: pgds1Mib.setContactInfo(' 14402 Franklin Avenue Tustin, CA 92780 ')
if mibBuilder.loadTexts: pgds1Mib.setDescription('The MIB module for managing PairGain ds1 OIDs within the Avidia System.')
pgds1MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1))
pgds1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1), )
if mibBuilder.loadTexts: pgds1ConfigTable.setStatus('current')
if mibBuilder.loadTexts: pgds1ConfigTable.setDescription('The pgDS1 Configuration table.')
pgds1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1), ).setIndexNames((0, "PAIRGAIN-DS1-MIB", "pgds1LineIndex"))
if mibBuilder.loadTexts: pgds1ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: pgds1ConfigEntry.setDescription('An entry in the DS1 Configuration table.')
pgds1LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgds1LineIndex.setStatus('current')
if mibBuilder.loadTexts: pgds1LineIndex.setDescription('This object should be made equal to ifIndex. The next paragraph describes its previous usage. Making the object equal to ifIndex allows proper use of ifStackTable and ds0/ds0bundle mibs. Previously, this object is the identifier of a DS1 Interface on a managed device. If there is an ifEntry that is directly associated with this and only this DS1 interface, it should have the same value as ifIndex. Otherwise, number the dsx1LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers.')
pgds1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgds1IfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: pgds1IfIndex.setDescription('This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
pgds1LineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgds1LineBuildout.setStatus('current')
if mibBuilder.loadTexts: pgds1LineBuildout.setDescription('The length of the ds1 line. This objects provides information for line build out circuitry. This object is only useful if the interface has configurable line build out circuitry. 0 0dB 1 -7.5dB 2 -15dB 3 -22.5dB 4 0-133ft 5 133-266ft 6 266-399ft 7 399-533ft 8 533-655ft ')
mibBuilder.exportSymbols("PAIRGAIN-DS1-MIB", pgds1ConfigEntry=pgds1ConfigEntry, pgds1LineIndex=pgds1LineIndex, pgds1IfIndex=pgds1IfIndex, pgds1LineBuildout=pgds1LineBuildout, PYSNMP_MODULE_ID=pgds1Mib, pgds1ConfigTable=pgds1ConfigTable, pgds1Mib=pgds1Mib, pgds1MibObjects=pgds1MibObjects)
