#
# PySNMP MIB module ALTEON-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTEON-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, enterprises, NotificationType, Counter32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Integer32, iso, ObjectIdentity, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "enterprises", "NotificationType", "Counter32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alteon = MibIdentifier((1, 3, 6, 1, 4, 1, 1872))
registration = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1))
private_mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2)).setLabel("private-mibs")
personalContentCache = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 3))
ics = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 3, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 1))
gs_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 2)).setLabel("gs-switch")
isd = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3))
switch_chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4)).setLabel("switch-chassis")
aws_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 5)).setLabel("aws-switch")
virt_admin = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 6)).setLabel("virt-admin")
chassis_8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4, 1)).setLabel("chassis-8600")
wsm4Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4, 1, 2))
platform = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1))
sslOffload = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 2))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3))
contentDirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 4))
aceswitch110 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 1))
acedirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 2))
aceswitch180 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 3))
acedirector2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 4))
aceswitch180e = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 5))
acedirector3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 6))
cachedirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 7))
gs_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8)).setLabel("gs-switches")
aceswitch184 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 9))
acedirector4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 10))
isd_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11)).setLabel("isd-reg")
webswitch_module = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 12)).setLabel("webswitch-module")
aws_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13)).setLabel("aws-switches")
alteonLinkOptimizer = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 14))
wsm_BladeCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 15)).setLabel("wsm-BladeCenter")
alteonLinkOptimizer143 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 16))
alteonLinkOptimizer150 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 17))
ibm_BladeCenterL3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18)).setLabel("ibm-BladeCenterL3")
copperModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18, 1))
fiberModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18, 2))
aws2000_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1)).setLabel("aws2000-switches")
aws3000_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2)).setLabel("aws3000-switches")
radwarealteon_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3)).setLabel("radwarealteon-switches")
aws2424 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 1))
aws2448 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 2))
aws2224 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 3))
aas2424s = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 4))
aas2208 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 5))
aas2216 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 6))
aws2424E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 7))
aas2424sE5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 8))
aas2208E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 9))
aas2216E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 10))
aws3408 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 1))
aws3416 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 2))
aws3408E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 3))
ods4416 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 1))
ods5412 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2))
ods4408 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 3))
odsva = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 4))
ods5224 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 5))
ods_virt_ac = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2, 1)).setLabel("ods-virt-ac")
ods_virt_vadc = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2, 2)).setLabel("ods-virt-vadc")
chas_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1)).setLabel("chas-switch")
chas_switch_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1)).setLabel("chas-switch-reg")
alteon708 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1, 1))
chas_switch_comp_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2)).setLabel("chas-switch-comp-reg")
alteonACPowerSupply7xx = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 1))
alteonDCPowerSupply7xx = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 2))
alteonFan708 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 3))
alteonModuleMP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 5))
alteonModuleSF = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 6))
alteonModuleFE_UTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 7)).setLabel("alteonModuleFE-UTP")
alteonModuleGE_SX = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 8)).setLabel("alteonModuleGE-SX")
alteonModuleGE_UTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 9)).setLabel("alteonModuleGE-UTP")
alteonContentDirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 1))
alteonSSLOffload = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 2))
alteonPersonalContentCache = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 3))
alteonFirewall = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 4))
alteonWSS = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 5))
mibBuilder.exportSymbols("ALTEON-ROOT-MIB", gs_switch=gs_switch, switch_chassis=switch_chassis, aws2424=aws2424, ods5412=ods5412, isd_reg=isd_reg, chas_switch=chas_switch, aas2208E5=aas2208E5, alteonLinkOptimizer=alteonLinkOptimizer, alteonContentDirector=alteonContentDirector, radwarealteon_switches=radwarealteon_switches, aws3408E5=aws3408E5, switch=switch, platform=platform, aceswitch184=aceswitch184, firewall=firewall, alteonModuleGE_UTP=alteonModuleGE_UTP, aws2224=aws2224, aws_switches=aws_switches, aws3416=aws3416, aceswitch110=aceswitch110, aceswitch180=aceswitch180, ods_virt_ac=ods_virt_ac, aws3000_switches=aws3000_switches, alteon708=alteon708, chas_switch_comp_reg=chas_switch_comp_reg, chassis_8600=chassis_8600, ics=ics, alteonDCPowerSupply7xx=alteonDCPowerSupply7xx, wsm4Traps=wsm4Traps, aas2216=aas2216, registration=registration, private_mibs=private_mibs, aas2216E5=aas2216E5, alteonFirewall=alteonFirewall, fiberModule=fiberModule, alteonModuleMP=alteonModuleMP, odsva=odsva, ods5224=ods5224, chas_switch_reg=chas_switch_reg, alteonModuleFE_UTP=alteonModuleFE_UTP, aws3408=aws3408, aas2208=aas2208, aws2000_switches=aws2000_switches, alteonWSS=alteonWSS, alteon=alteon, alteonModuleGE_SX=alteonModuleGE_SX, aws2448=aws2448, aceswitch180e=aceswitch180e, acedirector3=acedirector3, ods4416=ods4416, webswitch_module=webswitch_module, wsm_BladeCenter=wsm_BladeCenter, alteonPersonalContentCache=alteonPersonalContentCache, alteonLinkOptimizer150=alteonLinkOptimizer150, aas2424sE5=aas2424sE5, aws2424E5=aws2424E5, alteonModuleSF=alteonModuleSF, alteonSSLOffload=alteonSSLOffload, ods_virt_vadc=ods_virt_vadc, gs_switches=gs_switches, copperModule=copperModule, sslOffload=sslOffload, isd=isd, acedirector=acedirector, contentDirector=contentDirector, alteonLinkOptimizer143=alteonLinkOptimizer143, cachedirector=cachedirector, ibm_BladeCenterL3=ibm_BladeCenterL3, aas2424s=aas2424s, ods4408=ods4408, alteonACPowerSupply7xx=alteonACPowerSupply7xx, aws_switch=aws_switch, alteonFan708=alteonFan708, acedirector4=acedirector4, virt_admin=virt_admin, acedirector2=acedirector2, personalContentCache=personalContentCache)
