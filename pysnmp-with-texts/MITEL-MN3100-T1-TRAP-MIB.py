#
# PySNMP MIB module MITEL-MN3100-T1-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-MN3100-T1-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dsx1LineStatus, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, NotificationType, Counter64, Bits, TimeTicks, ModuleIdentity, enterprises, Integer32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "Counter64", "Bits", "TimeTicks", "ModuleIdentity", "enterprises", "Integer32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelDS1Extension = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 12))
mitelDS1Extension.setRevisions(('2003-03-24 01:41', '2002-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelDS1Extension.setRevisionsDescriptions(('Convert to SMIv2', 'MN3100 T1 trap definition Version 1.0',))
if mibBuilder.loadTexts: mitelDS1Extension.setLastUpdated('200204020000Z')
if mibBuilder.loadTexts: mitelDS1Extension.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitelDS1Extension.setContactInfo('Standards Group, Postal: MITEL Networks Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelDS1Extension.setDescription('The MITEL Mn3100 T1 trap MIB.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdCsIpera1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4))
mitelIpera1000Notifications = NotificationGroup((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)).setObjects(("MITEL-MN3100-T1-TRAP-MIB", "mitelMn3100dsx1LineSatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelIpera1000Notifications = mitelIpera1000Notifications.setStatus('current')
if mibBuilder.loadTexts: mitelIpera1000Notifications.setDescription('Call Server Ipera 1000 Notifications.')
mitelMn3100dsx1LineSatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 410)).setObjects(("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: mitelMn3100dsx1LineSatusChangeNotif.setStatus('current')
if mibBuilder.loadTexts: mitelMn3100dsx1LineSatusChangeNotif.setDescription('The mitelMn3100dsx1LineSatusChangeNotif trap indicates that the line status of a T1/E1 has changed. Please refer to RFC1406 for definition of dsx1LineStatus.')
mibBuilder.exportSymbols("MITEL-MN3100-T1-TRAP-MIB", mitelMn3100dsx1LineSatusChangeNotif=mitelMn3100dsx1LineSatusChangeNotif, mitelDS1Extension=mitelDS1Extension, mitel=mitel, mitelIpera1000Notifications=mitelIpera1000Notifications, mitelProprietary=mitelProprietary, mitelIdCsIpera1000=mitelIdCsIpera1000, PYSNMP_MODULE_ID=mitelDS1Extension, mitelIdentification=mitelIdentification, mitelIdCallServers=mitelIdCallServers)
