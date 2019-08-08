#
# PySNMP MIB module ASCEND-MIBHDSL2NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBHDSL2NET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Counter64, MibIdentifier, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "MibIdentifier", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibhdsl2NetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 14))
mibhdsl2NetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 14, 1), )
if mibBuilder.loadTexts: mibhdsl2NetworkProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibhdsl2NetworkProfileTable.setDescription('A list of mibhdsl2NetworkProfile profile entries.')
mibhdsl2NetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1), ).setIndexNames((0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Shelf-o"), (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Slot-o"), (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibhdsl2NetworkProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibhdsl2NetworkProfileEntry.setDescription('A mibhdsl2NetworkProfile entry containing objects that maps to the parameters of mibhdsl2NetworkProfile profile.')
hdsl2NetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 1), Integer32()).setLabel("hdsl2NetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Shelf_o.setDescription('')
hdsl2NetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 2), Integer32()).setLabel("hdsl2NetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Slot_o.setDescription('')
hdsl2NetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 3), Integer32()).setLabel("hdsl2NetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Item_o.setDescription('')
hdsl2NetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 4), DisplayString()).setLabel("hdsl2NetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Name.setDescription('For future use. The current design does not use the name field but instead references Hdsl2 lines by the physical address; we may in the future support referencing Hdsl2 lines by name as well as by address. The name consists of a null terminated ascii string supplied by the user; it defaults to the ascii form of the Hdsl2 line physical address.')
hdsl2NetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("hdsl2NetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
hdsl2NetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("hdsl2NetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
hdsl2NetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 7), Integer32()).setLabel("hdsl2NetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
hdsl2NetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("hdsl2NetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Enabled.setDescription('TRUE if the line is enabled, otherwise FALSE.')
hdsl2NetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("hdsl2NetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_SparingMode.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_SparingMode.setDescription('Port sparing operational mode for this port.')
hdsl2NetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("hdsl2NetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_IgnoreLineup.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_IgnoreLineup.setDescription('Ignore line up value for this port.')
hdsl2NetworkProfile_ProfileNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 9), Integer32()).setLabel("hdsl2NetworkProfile-ProfileNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ProfileNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ProfileNumber.setDescription('For potential backwards compatibility. The current design consists of one line profile numbered 0.')
hdsl2NetworkProfile_LineConfig_TrunkGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 10), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-TrunkGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_TrunkGroup.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_TrunkGroup.setDescription('The trunk group to which this line is assigned. 0 means this line is not part of a trunk group.')
hdsl2NetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 11), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_NailedGroup.setDescription('A number that identifies the set of lines that makes up a nailed group. 0 means this line is not part of a nailed group.')
hdsl2NetworkProfile_LineConfig_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 12), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-VpSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_VpSwitchingVpi.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_VpSwitchingVpi.setDescription('The Vpi to be used for the VP switching. Rest of the valid VPIs in valid vpi-vci-range will be used for the VC switching. Changes in this range will take effect immediately. THE USER SHOULD BE VERY CAREFUL WHILE CHANGING THIS VALUE BECAUSE ALL CONNECTIONS ON THE LIM WHERE THIS PORT BELONGS WILL BE DROPPED IN ORDER TO MAKE THIS NEW VALUE EFFECTIVE IMMEDIATELY.')
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 13), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setDescription('')
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 14), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setDescription('TNT is a multi shelf system. To minimise the changes required to existing code the shelf number is added to this structure as it will almost always be needed when a slot number is needed.')
hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 15), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setDescription('')
hdsl2NetworkProfile_LineConfig_Activation = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dsrActive", 2), ("dcdDsrActive", 3)))).setLabel("hdsl2NetworkProfile-LineConfig-Activation").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_Activation.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_Activation.setDescription('Line activation mode.')
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("hdsl2NetworkProfile-LineConfig-CallRouteInfo-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("hdsl2NetworkProfile-LineConfig-CallRouteInfo-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 19), Integer32()).setLabel("hdsl2NetworkProfile-LineConfig-CallRouteInfo-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
hdsl2NetworkProfile_LineConfig_UnitType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coe", 1), ("cpe", 2)))).setLabel("hdsl2NetworkProfile-LineConfig-UnitType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_UnitType.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_UnitType.setDescription('The Unit Type defines if a line is acting as either a Central Office (COE) or Customer Premise Equipment (CPE). Note that the remote unit needs to be configured opposite to this configureation.')
hdsl2NetworkProfile_LineConfig_NtrEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("hdsl2NetworkProfile-LineConfig-NtrEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_NtrEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_NtrEnabled.setDescription('TRUE if NTR functionality is enabled, otherwise FALSE. If the unit-type is COE, it will take the system clock as the input when NTR is enabled and allow the remote CPE port to recover the clock. If the unit-type is CPE, it will allow the port to possibly output the recovered clock as the system clock (if elected, see clock-source and clock-priority fields) when NTR is enabled.')
hdsl2NetworkProfile_LineConfig_ClockSource = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eligible", 1), ("notEligible", 2)))).setLabel("hdsl2NetworkProfile-LineConfig-ClockSource").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_ClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_ClockSource.setDescription('Determine whether the 8KHz clock from the HDSL2 line (unit-type has to be CPE and ntr-enabled has to be yes) is eligible to be used as the 8KHz system clock source.')
hdsl2NetworkProfile_LineConfig_ClockPriority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("highPriority", 2), ("middlePriority", 3), ("lowPriority", 4)))).setLabel("hdsl2NetworkProfile-LineConfig-ClockPriority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_ClockPriority.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_ClockPriority.setDescription('Clock priority assigned to the HDSL2 line. Used to select a particular HDSL2 line as the 8KHz system clock source.')
hdsl2NetworkProfile_LineConfig_LoopBack = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("analog", 2), ("digital", 3)))).setLabel("hdsl2NetworkProfile-LineConfig-LoopBack").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_LoopBack.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_LoopBack.setDescription('Configuration of different modem loopbacks.')
hdsl2NetworkProfile_LineConfig_Margin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17))).clone(namedValues=NamedValues(("n-0db", 1), ("n-1db", 2), ("n-2db", 3), ("n-3db", 4), ("n-4db", 5), ("n-5db", 6), ("n-6db", 7), ("n-7db", 8), ("n-8db", 9), ("n-9db", 10), ("n-10db", 11), ("disable", 17)))).setLabel("hdsl2NetworkProfile-LineConfig-Margin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_Margin.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_Margin.setDescription('Selects a margin range between the signal to noise floor.')
hdsl2NetworkProfile_LineConfig_SnextMargin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("n-0db", 1), ("n-1db", 2), ("n-2db", 3), ("n-3db", 4), ("n-4db", 5), ("n-5db", 6), ("n-6db", 7), ("n-7db", 8), ("n-8db", 9), ("n-9db", 10), ("n-10db", 11), ("n-plus-10db", 12), ("n-plus-9db", 13), ("n-plus-8db", 14), ("n-plus-7db", 15), ("n-plus-6db", 16), ("n-plus-5db", 17), ("n-plus-4db", 18), ("n-plus-3db", 19), ("n-plus-2db", 20), ("n-plus-1db", 21), ("disable", 22)))).setLabel("hdsl2NetworkProfile-LineConfig-SnextMargin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_SnextMargin.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_SnextMargin.setDescription('Selects a Snext margin range with a worst-case self next noise model given current loop insertion loss.')
hdsl2NetworkProfile_LineConfig_RateMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("auto", 2)))).setLabel("hdsl2NetworkProfile-LineConfig-RateMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RateMode.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_RateMode.setDescription('Used for G.SHDSL technology. Selects if the modem operates in Fixed or Auto rate mode.')
hdsl2NetworkProfile_LineConfig_MinRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(72001, 136001, 200001, 264001, 328001, 392001, 520001, 776001, 1032001, 1160001, 1288001, 1544001, 2056001, 2312001))).clone(namedValues=NamedValues(("n-72000", 72001), ("n-136000", 136001), ("n-200000", 200001), ("n-264000", 264001), ("n-328000", 328001), ("n-392000", 392001), ("n-520000", 520001), ("n-776000", 776001), ("n-1032000", 1032001), ("n-1160000", 1160001), ("n-1288000", 1288001), ("n-1544000", 1544001), ("n-2056000", 2056001), ("n-2312000", 2312001)))).setLabel("hdsl2NetworkProfile-LineConfig-MinRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_MinRate.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_MinRate.setDescription('Used for G.SHDSL technology. When the rate-mode is set to Auto, this is the minimum rate the modem will train to.')
hdsl2NetworkProfile_LineConfig_MaxRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(72001, 136001, 200001, 264001, 328001, 392001, 520001, 776001, 1032001, 1160001, 1288001, 1544001, 2056001, 2312001))).clone(namedValues=NamedValues(("n-72000", 72001), ("n-136000", 136001), ("n-200000", 200001), ("n-264000", 264001), ("n-328000", 328001), ("n-392000", 392001), ("n-520000", 520001), ("n-776000", 776001), ("n-1032000", 1032001), ("n-1160000", 1160001), ("n-1288000", 1288001), ("n-1544000", 1544001), ("n-2056000", 2056001), ("n-2312000", 2312001)))).setLabel("hdsl2NetworkProfile-LineConfig-MaxRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_MaxRate.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_MaxRate.setDescription('Used for G.SHDSL technology. When the rate-mode is set to Auto, this is the maximum rate the modem will train to. When the rate-mode is set to Fixed, this is the only rate the mode trains to.')
hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("northAmericanAnnexA", 1), ("europeanAnnexB", 2), ("autoDetect", 3)))).setLabel("hdsl2NetworkProfile-LineConfig-GshdslStandardNetworkType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType.setDescription("Per the G.SHDSL Standard G.991.2. This parameter allows selection for the modem to operate either the North American Annex 'A' or European Annex 'B' standard network types. The setting of auto-detect is only valid for CPE to train off of COE Standard Network settings.")
hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("hdsl2NetworkProfile-LineConfig-AnnexbAnfpEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled.setDescription('TRUE if Annex B ANFP functionality is enabled, otherwise FALSE. The gshdsl-standard-network-type must be set to European Annex B, and the port cannot be CPE. This field makes the modem perform in Annex B mode, but slightly differently. This is to comply with the UK ANFP requirements and pass the BTexact Technologies PSD measurement technique to meet BT approval. Only enable this field for that test specifically.')
hdsl2NetworkProfile_LineConfig_GshdslPsdType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetric776kPsdAnnexA", 4), ("asymmetric1544kPsdAnnexA", 5), ("asymmetric2056kPsdAnnexB", 6), ("asymmetric2312kPsdAnnexB", 7), ("autoDetect", 8)))).setLabel("hdsl2NetworkProfile-LineConfig-GshdslPsdType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_GshdslPsdType.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_LineConfig_GshdslPsdType.setDescription("Per the G.SHDSL Standard G.911.2. This parameter allows selection for the modem to output a symmetric PSD at all rates or asymmetric PSD's at fixed rates of 776kbps, 784kbps, 1544kbps, or 1552kbps for Annex A networks. Annex B networks support fixed rates of 2056kbps or 2304kbps. The setting of auto-detect is only valid for CPE to train off of COE PSD settings.")
hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 36), DisplayString()).setLabel("hdsl2NetworkProfile-ThreshProfiles-SpanThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile.setDescription('The name consists of a null terminated ascii string supplied by the user. This profile defines the thresholds for all the HDSL2/SHDSL units for this port unless otherwise specified by the individual parameters in this subprofile.')
hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 37), DisplayString()).setLabel("hdsl2NetworkProfile-ThreshProfiles-XtucThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile.setDescription('The name consists of a null terminated ascii string supplied by the user. This profile defines the thresholds for the DSLAM.')
hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 38), DisplayString()).setLabel("hdsl2NetworkProfile-ThreshProfiles-XturThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile.setDescription('The name consists of a null terminated ascii string supplied by the user. This profile defines the thresholds for the remote CPE.')
hdsl2NetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("hdsl2NetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_Action_o.setDescription('')
mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 14, 2), ).setLabel("mibhdsl2NetworkProfile-ThreshProfiles-UnitThreshProfilesTable")
if mibBuilder.loadTexts: mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable.setDescription('A list of mibhdsl2NetworkProfile__thresh_profiles__unit_thresh_profiles profile entries.')
mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1), ).setLabel("mibhdsl2NetworkProfile-ThreshProfiles-UnitThreshProfilesEntry").setIndexNames((0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Shelf-o"), (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Slot-o"), (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Item-o"), (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Index-o"))
if mibBuilder.loadTexts: mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry.setDescription('A mibhdsl2NetworkProfile__thresh_profiles__unit_thresh_profiles entry containing objects that maps to the parameters of mibhdsl2NetworkProfile__thresh_profiles__unit_thresh_profiles profile.')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 1), Integer32()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o.setDescription('')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 2), Integer32()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o.setDescription('')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 3), Integer32()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o.setDescription('')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 4), Integer32()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o.setDescription('')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 5), DisplayString()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-XruNetThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile.setDescription('The name consists of a null terminated ascii string supplied by the user. This profile defines the thresholds for the network side of regenerator unit 1.')
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 6), DisplayString()).setLabel("hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-XruCustThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile.setDescription('The name consists of a null terminated ascii string supplied by the user. This profile defines the thresholds for the customer side of regenerator unit 1.')
mibBuilder.exportSymbols("ASCEND-MIBHDSL2NET-MIB", hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot=hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o, hdsl2NetworkProfile_LineConfig_NtrEnabled=hdsl2NetworkProfile_LineConfig_NtrEnabled, hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf=hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf, hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber=hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber, mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable=mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable, hdsl2NetworkProfile_LineConfig_LoopBack=hdsl2NetworkProfile_LineConfig_LoopBack, hdsl2NetworkProfile_Slot_o=hdsl2NetworkProfile_Slot_o, hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled=hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled, DisplayString=DisplayString, hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile=hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile, hdsl2NetworkProfile_Item_o=hdsl2NetworkProfile_Item_o, hdsl2NetworkProfile_LineConfig_VpSwitchingVpi=hdsl2NetworkProfile_LineConfig_VpSwitchingVpi, hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber=hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber, hdsl2NetworkProfile_LineConfig_Margin=hdsl2NetworkProfile_LineConfig_Margin, mibhdsl2NetworkProfile=mibhdsl2NetworkProfile, hdsl2NetworkProfile_PhysicalAddress_Slot=hdsl2NetworkProfile_PhysicalAddress_Slot, hdsl2NetworkProfile_LineConfig_NailedGroup=hdsl2NetworkProfile_LineConfig_NailedGroup, hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile=hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile, hdsl2NetworkProfile_SparingMode=hdsl2NetworkProfile_SparingMode, hdsl2NetworkProfile_Shelf_o=hdsl2NetworkProfile_Shelf_o, hdsl2NetworkProfile_LineConfig_UnitType=hdsl2NetworkProfile_LineConfig_UnitType, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile, hdsl2NetworkProfile_LineConfig_Activation=hdsl2NetworkProfile_LineConfig_Activation, hdsl2NetworkProfile_LineConfig_MinRate=hdsl2NetworkProfile_LineConfig_MinRate, hdsl2NetworkProfile_ProfileNumber=hdsl2NetworkProfile_ProfileNumber, hdsl2NetworkProfile_Action_o=hdsl2NetworkProfile_Action_o, hdsl2NetworkProfile_PhysicalAddress_Shelf=hdsl2NetworkProfile_PhysicalAddress_Shelf, mibhdsl2NetworkProfileEntry=mibhdsl2NetworkProfileEntry, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o, hdsl2NetworkProfile_LineConfig_TrunkGroup=hdsl2NetworkProfile_LineConfig_TrunkGroup, hdsl2NetworkProfile_LineConfig_RateMode=hdsl2NetworkProfile_LineConfig_RateMode, hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile=hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o, hdsl2NetworkProfile_LineConfig_MaxRate=hdsl2NetworkProfile_LineConfig_MaxRate, mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry=mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry, hdsl2NetworkProfile_Enabled=hdsl2NetworkProfile_Enabled, hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber=hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber, hdsl2NetworkProfile_LineConfig_ClockPriority=hdsl2NetworkProfile_LineConfig_ClockPriority, hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o=hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o, hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType=hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType, mibhdsl2NetworkProfileTable=mibhdsl2NetworkProfileTable, hdsl2NetworkProfile_Name=hdsl2NetworkProfile_Name, hdsl2NetworkProfile_LineConfig_ClockSource=hdsl2NetworkProfile_LineConfig_ClockSource, hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber=hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber, hdsl2NetworkProfile_PhysicalAddress_ItemNumber=hdsl2NetworkProfile_PhysicalAddress_ItemNumber, hdsl2NetworkProfile_IgnoreLineup=hdsl2NetworkProfile_IgnoreLineup, hdsl2NetworkProfile_LineConfig_GshdslPsdType=hdsl2NetworkProfile_LineConfig_GshdslPsdType, hdsl2NetworkProfile_LineConfig_SnextMargin=hdsl2NetworkProfile_LineConfig_SnextMargin)