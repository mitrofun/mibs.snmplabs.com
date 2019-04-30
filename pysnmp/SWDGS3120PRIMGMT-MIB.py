#
# PySNMP MIB module SWDGS3120PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3120PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:28:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, Counter64, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3120Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117)).setLabel("dlink-Dgs3120Prod")
dlink_Dgs3120ProdModel = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1)).setLabel("dlink-Dgs3120ProdModel")
dlink_Dgs3120Prod_Dgs3120_24TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 1)).setLabel("dlink-Dgs3120Prod-Dgs3120-24TC")
dlink_Dgs3120Prod_Dgs3120_24PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 2)).setLabel("dlink-Dgs3120Prod-Dgs3120-24PC")
dlink_Dgs3120Prod_Dgs3120_24SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 3)).setLabel("dlink-Dgs3120Prod-Dgs3120-24SC")
dlink_Dgs3120Prod_Dgs3120_48TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 4)).setLabel("dlink-Dgs3120Prod-Dgs3120-48TC")
dlink_Dgs3120Prod_Dgs3120_48PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 5)).setLabel("dlink-Dgs3120Prod-Dgs3120-48PC")
dlink_Dgs3120Prod_Dgs3120_24SC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 117, 1, 6)).setLabel("dlink-Dgs3120Prod-Dgs3120-24SC-DC")
dlink_Dgs3120Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117)).setLabel("dlink-Dgs3120Proj")
dlink_Dgs3120ProjModel = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1)).setLabel("dlink-Dgs3120ProjModel")
dlink_Dgs3120Proj_Dgs3120_24TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 1)).setLabel("dlink-Dgs3120Proj-Dgs3120-24TC")
dlink_Dgs3120Proj_Dgs3120_24PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2)).setLabel("dlink-Dgs3120Proj-Dgs3120-24PC")
dlink_Dgs3120Proj_Dgs3120_24SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3)).setLabel("dlink-Dgs3120Proj-Dgs3120-24SC")
dlink_Dgs3120Proj_Dgs3120_48TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 4)).setLabel("dlink-Dgs3120Proj-Dgs3120-48TC")
dlink_Dgs3120Proj_Dgs3120_48PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 5)).setLabel("dlink-Dgs3120Proj-Dgs3120-48PC")
dlink_Dgs3120Proj_Dgs3120_24SC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 6)).setLabel("dlink-Dgs3120Proj-Dgs3120-24SC-DC")
mibBuilder.exportSymbols("SWDGS3120PRIMGMT-MIB", dlink_Dgs3120Prod_Dgs3120_24SC_DC=dlink_Dgs3120Prod_Dgs3120_24SC_DC, dlink_Dgs3120Proj_Dgs3120_48TC=dlink_Dgs3120Proj_Dgs3120_48TC, dlink_Dgs3120Proj_Dgs3120_48PC=dlink_Dgs3120Proj_Dgs3120_48PC, dlink_Dgs3120Prod_Dgs3120_24SC=dlink_Dgs3120Prod_Dgs3120_24SC, dlink_Dgs3120Proj_Dgs3120_24TC=dlink_Dgs3120Proj_Dgs3120_24TC, dlink_Dgs3120Prod_Dgs3120_24TC=dlink_Dgs3120Prod_Dgs3120_24TC, dlink_Dgs3120ProdModel=dlink_Dgs3120ProdModel, dlink_Dgs3120Prod=dlink_Dgs3120Prod, dlink_Dgs3120Proj_Dgs3120_24SC_DC=dlink_Dgs3120Proj_Dgs3120_24SC_DC, dlink_Dgs3120Proj_Dgs3120_24PC=dlink_Dgs3120Proj_Dgs3120_24PC, dlink_Dgs3120Proj=dlink_Dgs3120Proj, dlink_Dgs3120Prod_Dgs3120_48TC=dlink_Dgs3120Prod_Dgs3120_48TC, dlink_Dgs3120Prod_Dgs3120_48PC=dlink_Dgs3120Prod_Dgs3120_48PC, dlink_Dgs3120Proj_Dgs3120_24SC=dlink_Dgs3120Proj_Dgs3120_24SC, dlink_Dgs3120ProjModel=dlink_Dgs3120ProjModel, dlink_Dgs3120Prod_Dgs3120_24PC=dlink_Dgs3120Prod_Dgs3120_24PC)