#
# PySNMP MIB module A3COM-HUAWEI-DOT11S-MESH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-DOT11S-MESH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:04:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cDot11APElementIndex, H3cDot11RadioElementIndex, h3cDot11 = mibBuilder.importSymbols("A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex", "H3cDot11RadioElementIndex", "h3cDot11")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Counter64, NotificationType, Bits, iso, Integer32, ObjectIdentity, IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "NotificationType", "Bits", "iso", "Integer32", "ObjectIdentity", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
TruthValue, RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
h3cDot11sMesh = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11))
h3cDot11sMesh.setRevisions(('2009-08-01 10:00', '2008-11-07 10:00', '2008-07-08 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cDot11sMesh.setRevisionsDescriptions(('Add new nodes.', 'Modified to add new nodes and a new table.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cDot11sMesh.setLastUpdated('200908011000Z')
if mibBuilder.loadTexts: h3cDot11sMesh.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cDot11sMesh.setContactInfo('Platform Team Hangzhou H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cDot11sMesh.setDescription('The file defines a MIB to provide MESH configuration information. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. Access point (AP) Transmitter/receiver (transceiver) device that commonly connects and transports data between a wireless network and a wired network. Access control (AC) To control and manage multi-APs, it will bridge wireless and wired network. Fat AP Applied in the home, SOHO and so on, and it could work independently without help from AC. Fit AP Applied in the enterprise environment, it will work under the control and management from AC. BSS IEEE 802.11 Basic Service Set (Radio Cell). The BSS of an AP comprises of the stations directly associating with the AP. Radio The chip set to receive and send wireless signal. Mesh A network consisting of two or more mesh points which communicate with each other via mesh services. Mesh Point (MP) An IEEE 802.11 entity that contains an IEEE 802.11-conformant medium access control (MAC) and physical layer (PHY) interface to the wireless medium (WM) that supports mesh services. Mesh Access Point (MAP) A mesh point that is collocated with one or more access points. Mesh Portal Point (MPP) A mesh point that is collocated with one or more portals. Mesh Link A link between two MPs.')
h3cDot11sConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1))
h3cDot11sWDSConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2))
h3cDot11sMeshStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3))
h3cDot11sMeshGlobalPara = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 1))
h3cDot11sMeshMkdID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11sMeshMkdID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshMkdID.setDescription("This object represents the mesh key distributor identifier (MKD-ID). If the MKD-ID is not configured, the value is '00:00:00:00:00:00'.")
h3cDot11sMeshPflTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2), )
if mibBuilder.loadTexts: h3cDot11sMeshPflTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflTable.setDescription('This table is used to configure mesh profile. A mesh profile is created and mapped to a MP so that it can provide mesh services to other MPs which have the same mesh ID. When the mesh profile is enabled, all of the object in this table can not be modified except h3cDot11sMeshPflEnable. The mesh profile can not be deleted when it is bound with the radio.')
h3cDot11sMeshPflEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMeshPflIndex"))
if mibBuilder.loadTexts: h3cDot11sMeshPflEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflEntry.setDescription('Each entry contains information of a mesh profile.')
h3cDot11sMeshPflIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11sMeshPflIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflIndex.setDescription('This object represents the index of the mesh profile.')
h3cDot11sMeshPflMeshID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflMeshID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflMeshID.setDescription("This object represents the mesh ID of the mesh profile. The string length of this object is zero when the mesh ID is not configured. If the mesh ID is not configured, h3cDot11sMeshPflEnable can not be set to 'true'.")
h3cDot11sMeshPflBindIntNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 3), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflBindIntNum.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflBindIntNum.setDescription("This object represents the specified mesh interface number binding to the mesh profile. If the value is set to -1, the binding will be removed. If the mesh interface is not specified, the value of h3cDot11sMeshPflEnable can not be set to 'true'.")
h3cDot11sMeshPflKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1800))).setUnits('second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflKeepAlive.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflKeepAlive.setDescription('This object represents the mesh link keep-alive interval.')
h3cDot11sMeshPflBackhaulRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 5), Integer32()).setUnits('Kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflBackhaulRate.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflBackhaulRate.setDescription('This object represents the link backhaul rate.')
h3cDot11sMeshMkdServEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshMkdServEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshMkdServEnable.setDescription("This object indicates whether the mesh key distributor (MKD) service for the mesh profile is enabled. 'true': The MKD service for the mesh profile is enabled. 'false': The MKD service for the mesh profile is disabled.")
h3cDot11sMeshPflEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflEnable.setDescription("This object indicates whether the mesh profile is enabled. 'true': The mesh profile is enabled. 'false': The mesh profile is disabled.")
h3cDot11sMeshPflRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMeshPflRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflRowStatus.setDescription('The status of this table entry.')
h3cDot11sMpPlcyTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3), )
if mibBuilder.loadTexts: h3cDot11sMpPlcyTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyTable.setDescription("This table is used to configure MP policy. There is 'default_mp_plcy' on system by default and its index is 1. The 'default_mp_plcy' can not be deleted or modified. The MP policy can not be deleted when it is applied to a radio. It can not be modified when it is applied to an enabled radio.")
h3cDot11sMpPlcyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMpPlcyIndex"))
if mibBuilder.loadTexts: h3cDot11sMpPlcyEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyEntry.setDescription('Each entry contains information of a MP policy.')
h3cDot11sMpPlcyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11sMpPlcyIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyIndex.setDescription('This object represents the MP policy index.')
h3cDot11sMpPlcyName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMpPlcyName.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyName.setDescription("This object represents the MP policy name. MP policy can not be created with name 'a', 'al', 'all' or 'default_mp_plcy'. Modification is not supported.")
h3cDot11sMpPlcyInitEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMpPlcyInitEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyInitEnable.setDescription("This object indicates whether the link initiation for the MP policy is enabled. 'true': The link initiation for the MP policy is enabled. 'false': The link initiation for the MP policy is disabled.")
h3cDot11sMlspEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMlspEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspEnable.setDescription("This object indicates whether the mesh link switch protocol (MLSP) is enabled. 'true': MLSP is enabled. 'false': MLSP is disabled.")
h3cDot11sProbReqInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 5), Integer32()).setUnits('millisecond').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sProbReqInterval.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sProbReqInterval.setDescription('This object represents the probe request interval.')
h3cDot11sRoleAuthEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sRoleAuthEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sRoleAuthEnable.setDescription('This object indicates whether the device can play as the role of an authenticator.')
h3cDot11sLinkHoldRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100))).setUnits('dBm').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sLinkHoldRSSI.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sLinkHoldRSSI.setDescription('This object represents the link-hold receive signal strength indicator (RSSI).')
h3cDot11sLinkHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 20000))).setUnits('millisecond').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sLinkHoldTime.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sLinkHoldTime.setDescription('This object represents the link-hold time.')
h3cDot11sSwitchMargin = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('dBm').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sSwitchMargin.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sSwitchMargin.setDescription('This object represents the link-switch margin.')
h3cDot11sLinkSaturationRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 150))).setUnits('dBm').setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sLinkSaturationRSSI.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sLinkSaturationRSSI.setDescription('This object represents the link saturation receive signal strength indicator (RSSI).')
h3cDot11sLinkRateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("realtime", 2))).clone('fixed')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sLinkRateMode.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sLinkRateMode.setDescription('This object represents the rate mode of the mesh link.')
h3cDot11sMaxLinkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMaxLinkNum.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMaxLinkNum.setDescription('This object represents the maximum number of the mesh link.')
h3cDot11sMpPlcyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMpPlcyRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyRowStatus.setDescription('The status of this table entry.')
h3cDot11sMlspCfgTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 4), )
if mibBuilder.loadTexts: h3cDot11sMlspCfgTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspCfgTable.setDescription('This table is used to configure MLSP proxy MAC address. Only if the specified MP policy is modifiable and the MLSP is enabled, the row of this table can be created and deleted. The row of this table can not be modified.')
h3cDot11sMlspCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMpPlcyIndex"), (0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMlspProxyIndex"))
if mibBuilder.loadTexts: h3cDot11sMlspCfgEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspCfgEntry.setDescription('Each entry contains information of MLSP proxy MAC address.')
h3cDot11sMlspProxyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11sMlspProxyIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspProxyIndex.setDescription('This object represents the MLSP proxy MAC address index.')
h3cDot11sMlspProxyMac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMlspProxyMac.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspProxyMac.setDescription('This object represents the MLSP proxy MAC address.')
h3cDot11sMlspRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sMlspRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMlspRowStatus.setDescription('The status of this table entry.')
h3cDot11sRadioCfgTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 5), )
if mibBuilder.loadTexts: h3cDot11sRadioCfgTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sRadioCfgTable.setDescription('This table is used to configure mesh to the specified radio.')
h3cDot11sRadioCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sCfgRadioIndex"))
if mibBuilder.loadTexts: h3cDot11sRadioCfgEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sRadioCfgEntry.setDescription('Each entry contains mesh configure information of the specified radio.')
h3cDot11sCfgRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 5, 1, 1), H3cDot11RadioElementIndex())
if mibBuilder.loadTexts: h3cDot11sCfgRadioIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sCfgRadioIndex.setDescription('Represents index of the radio.')
h3cDot11sMeshPflMap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11sMeshPflMap.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshPflMap.setDescription('This object represents the number of the mesh profile mapped to the specified radio. The value is zero when the radio is not binding mesh profile.')
h3cDot11sMpPlcyMap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 5, 1, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11sMpPlcyMap.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMpPlcyMap.setDescription("This object represents the index of the MP policy mapped to the specified radio. The MP policy is 'default_mp_plcy' when the radio is not binding user-defined MP policy. The index of 'default_mp_plcy' is 1. This object can not be modified when the radio is enabled.")
h3cDot11sAPCfgTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 6), )
if mibBuilder.loadTexts: h3cDot11sAPCfgTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sAPCfgTable.setDescription('This table is used to configure mesh to the specified AP.')
h3cDot11sAPCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"))
if mibBuilder.loadTexts: h3cDot11sAPCfgEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sAPCfgEntry.setDescription('Each entry contains mesh configure information of the specified AP.')
h3cDot11sPortalEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 1, 6, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11sPortalEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sPortalEnable.setDescription("This object indicates whether the portal service is enabled. 'true': The portal service is enabled. 'false': The portal service is disabled.")
h3cDot11sWDSPeerMacTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2, 1), )
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacTable.setDescription('This table is used to configure wireless distribution system (WDS). The row of this table can not be modified.')
h3cDot11sWDSPeerMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sCfgRadioIndex"), (0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sWDSPeerMacIndex"))
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacEntry.setDescription('Each entry contains information of WDS.')
h3cDot11sWDSPeerMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacIndex.setDescription('This object represents the peer MAC address index.')
h3cDot11sWDSPeerMacAddrss = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacAddrss.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacAddrss.setDescription('This object represents the peer MAC address.')
h3cDot11sWDSPeerMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sWDSPeerMacRowStatus.setDescription('The status of this table entry.')
h3cDot11sMeshLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1), )
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatusTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatusTable.setDescription('This table is used to represent the status of mesh link.')
h3cDot11sMeshLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMeshLinkIfIndex"))
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatusEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatusEntry.setDescription('Each entry contains status information of mesh link.')
h3cDot11sMeshLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cDot11sMeshLinkIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkIfIndex.setDescription('This object represents the interface index of the mesh link.')
h3cDot11sMeshLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkName.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkName.setDescription('This object represents the name of the mesh link.')
h3cDot11sMeshLinkBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkBSSID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkBSSID.setDescription('This object represents the BSS ID of the mesh link.')
h3cDot11sMeshLinkPeerMac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkPeerMac.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkPeerMac.setDescription('This object represents the peer MAC address of the mesh link.')
h3cDot11sMeshLinkExistDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 1, 1, 5), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkExistDuration.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkExistDuration.setDescription('This object represents the time for which the link has been up.')
h3cDot11sMeshLinkStatisTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2), )
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatisTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatisTable.setDescription('This table is used to represent the statistical information of mesh link.')
h3cDot11sMeshLinkStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"), (0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMeshLinkStatIfIndex"))
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatisEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatisEntry.setDescription('Each entry contains statistical information of mesh link.')
h3cDot11sMeshLinkStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkStatIfIndex.setDescription('This object represents the interface index of the mesh link.')
h3cDot11sMeshLinkNbrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkNbrIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkNbrIndex.setDescription('Represents the neighbor index of the mesh link.')
h3cDot11sMeshLinkRxTotByte = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxTotByte.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxTotByte.setDescription('Represents the amount of bytes that the mesh link received.')
h3cDot11sMeshLinkRxTotPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxTotPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxTotPkt.setDescription('Represents the amount of packets that the mesh link received.')
h3cDot11sMeshLinkRxUniPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxUniPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxUniPkt.setDescription('Represents the amount of unicast packets that the mesh link received.')
h3cDot11sMeshLinkRxBrocPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxBrocPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxBrocPkt.setDescription('Represents the amount of broadcast packets that the mesh link received.')
h3cDot11sMeshLinkRxMuticPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxMuticPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxMuticPkt.setDescription('Represents the amount of multicast packets that the mesh link received.')
h3cDot11sMeshLinkRxDiscPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxDiscPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkRxDiscPkt.setDescription('Represents the amount of packets that the mesh link discarded.')
h3cDot11sMeshLinkTxTotByte = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxTotByte.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxTotByte.setDescription('Represents the total amount of bytes that the mesh link transmitted.')
h3cDot11sMeshLinkTxTotPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxTotPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxTotPkt.setDescription('Represents the total amount of packets that the mesh link transmitted.')
h3cDot11sMeshLinkTxUniPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxUniPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxUniPkt.setDescription('Represents the amount of unicast packets that the mesh link transmitted.')
h3cDot11sMeshLinkTxBrocPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxBrocPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxBrocPkt.setDescription('Represents the amount of broadcast packets that the mesh link transmitted.')
h3cDot11sMeshLinkTxMuticPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxMuticPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxMuticPkt.setDescription('Represents the amount of multicast packets that the mesh link transmitted.')
h3cDot11sMeshLinkTxDiscPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxDiscPkt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkTxDiscPkt.setDescription('Represents the amount of discarded packets that the mesh link transmitted.')
h3cDot11sMeshLinkIFName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 2, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkIFName.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkIFName.setDescription('Represents the name of mesh link interface.')
h3cDot11sMeshNbrStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3), )
if mibBuilder.loadTexts: h3cDot11sMeshNbrStatusTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrStatusTable.setDescription('This table represents the status information for the neighbors of MP.')
h3cDot11sMeshNbrStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"), (0, "A3COM-HUAWEI-DOT11S-MESH-MIB", "h3cDot11sMeshNbrIndex"))
if mibBuilder.loadTexts: h3cDot11sMeshNbrStatusEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrStatusEntry.setDescription('Each entry of the table will provide status information for the neighbors of MP.')
h3cDot11sMeshNbrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cDot11sMeshNbrIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrIndex.setDescription('Represents the index for the neighbor.')
h3cDot11sMeshNbrRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrRadioID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrRadioID.setDescription('Represents the radio ID of the neighbor.')
h3cDot11sMeshLocalMeshID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLocalMeshID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLocalMeshID.setDescription('Represents the local mesh ID.')
h3cDot11sMeshNbrMeshID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrMeshID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrMeshID.setDescription('Represents the mesh ID of the neighbor.')
h3cDot11sMeshNbrBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrBSSID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrBSSID.setDescription('Represents the BSS ID of the neighbor.')
h3cDot11sMeshNbrPeerMac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrPeerMac.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrPeerMac.setDescription('Represents the MAC address of the peer neighbor.')
h3cDot11sMeshLinkInMp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshLinkInMp.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshLinkInMp.setDescription('Represents the interface index of mesh link that used to connect with this neighbor.')
h3cDot11sMeshMPLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("processing", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshMPLinkStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshMPLinkStatus.setDescription('Represents the status of mesh link that used to connect with this neighbor.')
h3cDot11sMeshNbrChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrChannel.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrChannel.setDescription('Represents the channel number used by this neighbor.')
h3cDot11sMeshNbrLinkDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 10), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrLinkDuration.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrLinkDuration.setDescription('Represents the duration of mesh link that used to connect with this neighbor.')
h3cDot11sMeshNbrRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrRSSI.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrRSSI.setDescription('Represents the RSSI of mesh link that used to connect with this neighbor.')
h3cDot11sMeshNbrSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 11, 3, 3, 1, 12), Integer32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11sMeshNbrSNR.setStatus('current')
if mibBuilder.loadTexts: h3cDot11sMeshNbrSNR.setDescription('Represents the SNR of mesh link that used to connect with this neighbor.')
mibBuilder.exportSymbols("A3COM-HUAWEI-DOT11S-MESH-MIB", h3cDot11sLinkHoldTime=h3cDot11sLinkHoldTime, h3cDot11sMeshLinkStatusTable=h3cDot11sMeshLinkStatusTable, h3cDot11sMeshLinkStatisTable=h3cDot11sMeshLinkStatisTable, h3cDot11sMpPlcyEntry=h3cDot11sMpPlcyEntry, h3cDot11sMeshLinkStatusEntry=h3cDot11sMeshLinkStatusEntry, h3cDot11sAPCfgEntry=h3cDot11sAPCfgEntry, h3cDot11sMeshLinkTxTotPkt=h3cDot11sMeshLinkTxTotPkt, h3cDot11sMeshLinkRxBrocPkt=h3cDot11sMeshLinkRxBrocPkt, h3cDot11sMlspProxyMac=h3cDot11sMlspProxyMac, h3cDot11sMlspCfgEntry=h3cDot11sMlspCfgEntry, h3cDot11sMeshLinkRxUniPkt=h3cDot11sMeshLinkRxUniPkt, h3cDot11sMeshLinkRxTotByte=h3cDot11sMeshLinkRxTotByte, PYSNMP_MODULE_ID=h3cDot11sMesh, h3cDot11sMeshNbrIndex=h3cDot11sMeshNbrIndex, h3cDot11sMpPlcyName=h3cDot11sMpPlcyName, h3cDot11sMeshNbrRadioID=h3cDot11sMeshNbrRadioID, h3cDot11sMeshLinkExistDuration=h3cDot11sMeshLinkExistDuration, h3cDot11sMeshLinkPeerMac=h3cDot11sMeshLinkPeerMac, h3cDot11sMeshLinkTxMuticPkt=h3cDot11sMeshLinkTxMuticPkt, h3cDot11sMeshPflIndex=h3cDot11sMeshPflIndex, h3cDot11sMlspCfgTable=h3cDot11sMlspCfgTable, h3cDot11sMeshLinkRxTotPkt=h3cDot11sMeshLinkRxTotPkt, h3cDot11sMeshMkdID=h3cDot11sMeshMkdID, h3cDot11sMeshPflTable=h3cDot11sMeshPflTable, h3cDot11sWDSPeerMacEntry=h3cDot11sWDSPeerMacEntry, h3cDot11sMeshLinkTxUniPkt=h3cDot11sMeshLinkTxUniPkt, h3cDot11sMeshNbrRSSI=h3cDot11sMeshNbrRSSI, h3cDot11sMlspProxyIndex=h3cDot11sMlspProxyIndex, h3cDot11sMeshNbrLinkDuration=h3cDot11sMeshNbrLinkDuration, h3cDot11sMeshPflKeepAlive=h3cDot11sMeshPflKeepAlive, h3cDot11sWDSPeerMacIndex=h3cDot11sWDSPeerMacIndex, h3cDot11sRadioCfgEntry=h3cDot11sRadioCfgEntry, h3cDot11sSwitchMargin=h3cDot11sSwitchMargin, h3cDot11sMeshGlobalPara=h3cDot11sMeshGlobalPara, h3cDot11sMpPlcyTable=h3cDot11sMpPlcyTable, h3cDot11sMaxLinkNum=h3cDot11sMaxLinkNum, h3cDot11sCfgRadioIndex=h3cDot11sCfgRadioIndex, h3cDot11sMeshNbrStatusTable=h3cDot11sMeshNbrStatusTable, h3cDot11sWDSPeerMacRowStatus=h3cDot11sWDSPeerMacRowStatus, h3cDot11sMeshNbrBSSID=h3cDot11sMeshNbrBSSID, h3cDot11sMeshPflEntry=h3cDot11sMeshPflEntry, h3cDot11sMeshPflBackhaulRate=h3cDot11sMeshPflBackhaulRate, h3cDot11sRadioCfgTable=h3cDot11sRadioCfgTable, h3cDot11sMeshPflMap=h3cDot11sMeshPflMap, h3cDot11sMeshPflMeshID=h3cDot11sMeshPflMeshID, h3cDot11sMeshNbrSNR=h3cDot11sMeshNbrSNR, h3cDot11sMeshPflEnable=h3cDot11sMeshPflEnable, h3cDot11sMeshLinkRxDiscPkt=h3cDot11sMeshLinkRxDiscPkt, h3cDot11sMeshLinkName=h3cDot11sMeshLinkName, h3cDot11sMeshNbrPeerMac=h3cDot11sMeshNbrPeerMac, h3cDot11sMeshLinkTxBrocPkt=h3cDot11sMeshLinkTxBrocPkt, h3cDot11sWDSConfigGroup=h3cDot11sWDSConfigGroup, h3cDot11sWDSPeerMacAddrss=h3cDot11sWDSPeerMacAddrss, h3cDot11sMeshLinkNbrIndex=h3cDot11sMeshLinkNbrIndex, h3cDot11sLinkHoldRSSI=h3cDot11sLinkHoldRSSI, h3cDot11sMeshLocalMeshID=h3cDot11sMeshLocalMeshID, h3cDot11sMeshLinkRxMuticPkt=h3cDot11sMeshLinkRxMuticPkt, h3cDot11sRoleAuthEnable=h3cDot11sRoleAuthEnable, h3cDot11sPortalEnable=h3cDot11sPortalEnable, h3cDot11sProbReqInterval=h3cDot11sProbReqInterval, h3cDot11sMeshNbrStatusEntry=h3cDot11sMeshNbrStatusEntry, h3cDot11sAPCfgTable=h3cDot11sAPCfgTable, h3cDot11sMlspEnable=h3cDot11sMlspEnable, h3cDot11sMeshLinkTxDiscPkt=h3cDot11sMeshLinkTxDiscPkt, h3cDot11sMeshMkdServEnable=h3cDot11sMeshMkdServEnable, h3cDot11sMlspRowStatus=h3cDot11sMlspRowStatus, h3cDot11sMesh=h3cDot11sMesh, h3cDot11sMeshNbrChannel=h3cDot11sMeshNbrChannel, h3cDot11sMeshPflBindIntNum=h3cDot11sMeshPflBindIntNum, h3cDot11sMeshLinkIfIndex=h3cDot11sMeshLinkIfIndex, h3cDot11sMeshLinkStatisEntry=h3cDot11sMeshLinkStatisEntry, h3cDot11sMeshMPLinkStatus=h3cDot11sMeshMPLinkStatus, h3cDot11sMpPlcyIndex=h3cDot11sMpPlcyIndex, h3cDot11sMeshStatusGroup=h3cDot11sMeshStatusGroup, h3cDot11sMpPlcyInitEnable=h3cDot11sMpPlcyInitEnable, h3cDot11sMeshPflRowStatus=h3cDot11sMeshPflRowStatus, h3cDot11sWDSPeerMacTable=h3cDot11sWDSPeerMacTable, h3cDot11sLinkRateMode=h3cDot11sLinkRateMode, h3cDot11sMeshLinkBSSID=h3cDot11sMeshLinkBSSID, h3cDot11sMeshLinkIFName=h3cDot11sMeshLinkIFName, h3cDot11sLinkSaturationRSSI=h3cDot11sLinkSaturationRSSI, h3cDot11sMeshLinkInMp=h3cDot11sMeshLinkInMp, h3cDot11sMeshNbrMeshID=h3cDot11sMeshNbrMeshID, h3cDot11sMpPlcyMap=h3cDot11sMpPlcyMap, h3cDot11sMeshLinkTxTotByte=h3cDot11sMeshLinkTxTotByte, h3cDot11sConfigGroup=h3cDot11sConfigGroup, h3cDot11sMpPlcyRowStatus=h3cDot11sMpPlcyRowStatus, h3cDot11sMeshLinkStatIfIndex=h3cDot11sMeshLinkStatIfIndex)
