#
# PySNMP MIB module BAS-CARD-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-CARD-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
BasLogicalPortId, BasSlotId, BasChassisId, BasCardClass, basCardInfo, BasInterfaceId = mibBuilder.importSymbols("BAS-MIB", "BasLogicalPortId", "BasSlotId", "BasChassisId", "BasCardClass", "basCardInfo", "BasInterfaceId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, Integer32, IpAddress, Unsigned32, MibIdentifier, TimeTicks, iso, Counter32, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "TimeTicks", "iso", "Counter32", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
basCardInfoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1))
if mibBuilder.loadTexts: basCardInfoMib.setLastUpdated('9810081200Z')
if mibBuilder.loadTexts: basCardInfoMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basCardInfoMib.setContactInfo(' Tech Support Broadband Access Systems 201 Forest Street Marlboro, MA 01752 U.S.A. 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basCardInfoMib.setDescription('This MIB module defines the configuration MIB objects for a Broadband Access System Chassis cards.')
basCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1))
basCardInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: basCardInfoTable.setStatus('current')
if mibBuilder.loadTexts: basCardInfoTable.setDescription('Info about this slot.')
basCardInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "BAS-CARD-INFO-MIB", "basCardInfoChassis"), (0, "BAS-CARD-INFO-MIB", "basCardInfoSlot"), (0, "BAS-CARD-INFO-MIB", "basCardInfoIf"), (0, "BAS-CARD-INFO-MIB", "basCardInfoLPort"))
if mibBuilder.loadTexts: basCardInfoEntry.setStatus('current')
if mibBuilder.loadTexts: basCardInfoEntry.setDescription('Chassis and slot information.')
basCardInfoChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basCardInfoChassis.setStatus('current')
if mibBuilder.loadTexts: basCardInfoChassis.setDescription('The BAS Chassis ID of this card.')
basCardInfoSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basCardInfoSlot.setStatus('current')
if mibBuilder.loadTexts: basCardInfoSlot.setDescription('The BAS Slot ID of this card.')
basCardInfoIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basCardInfoIf.setStatus('current')
if mibBuilder.loadTexts: basCardInfoIf.setDescription('The BAS interface ID of this card.')
basCardInfoLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basCardInfoLPort.setStatus('current')
if mibBuilder.loadTexts: basCardInfoLPort.setDescription('The BAS logical port ID of this card.')
basCardInfoChassisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basCardInfoChassisNumber.setStatus('current')
if mibBuilder.loadTexts: basCardInfoChassisNumber.setDescription('The BAS Chassis serial number of this card.')
basCardInfoClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 6), BasCardClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basCardInfoClass.setStatus('current')
if mibBuilder.loadTexts: basCardInfoClass.setDescription('The BAS card class of this card.')
basAgentConfigSave = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("save", 2), ("saving", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basAgentConfigSave.setStatus('current')
if mibBuilder.loadTexts: basAgentConfigSave.setDescription('The BAS save configuration Object')
basAgentConfigSaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("passed", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: basAgentConfigSaveStatus.setStatus('current')
if mibBuilder.loadTexts: basAgentConfigSaveStatus.setDescription('The BAS save configuration status Object')
basBcmIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basBcmIpAddress.setStatus('current')
if mibBuilder.loadTexts: basBcmIpAddress.setDescription('The BCM IP Address Object')
basCardReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCardReset.setStatus('current')
if mibBuilder.loadTexts: basCardReset.setDescription('The BAS Card Reset Object. In order to set this object to reset(2), the object basCardResetState must first be set to unlocked(2).')
basAgentSharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basAgentSharedKey.setStatus('current')
if mibBuilder.loadTexts: basAgentSharedKey.setDescription('The Agent Shared Key Object')
basAgentUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basAgentUdpPort.setStatus('current')
if mibBuilder.loadTexts: basAgentUdpPort.setDescription('The BAS Agent SNMP UDP Port Object')
basAgentTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basAgentTcpPort.setStatus('current')
if mibBuilder.loadTexts: basAgentTcpPort.setDescription('The BAS Agentx Tcp Port Object')
basCardInfoAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("loading", 4), ("loaded", 5), ("registering", 6), ("registered", 7), ("agentxstarting", 8), ("agentxstarted", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: basCardInfoAdminStatus.setStatus('current')
if mibBuilder.loadTexts: basCardInfoAdminStatus.setDescription('The desired state of the card. The testing(3) state indicates that the card is under test, the IFs are not operational.')
basCardResetState = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCardResetState.setStatus('current')
if mibBuilder.loadTexts: basCardResetState.setDescription('The state of the basCardReset object. If this object is set to locked(1), then the card cannot be reset without first setting this object to unlocked(2).')
basCardWatchdogTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCardWatchdogTimer.setStatus('current')
if mibBuilder.loadTexts: basCardWatchdogTimer.setDescription('This object may be set to enable(1) to enable the watchdog timer or to disable(2) to disable the watchdog timer. Setting this object to notSupported(3) has no affect. A notSupported(3) value returned means the watchdog timer is not supported by the hardware.')
basCardRSTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2), )
if mibBuilder.loadTexts: basCardRSTable.setStatus('current')
if mibBuilder.loadTexts: basCardRSTable.setDescription('A table specifying a list of Route Servers for this card.')
basCardRSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1), ).setIndexNames((0, "BAS-CARD-INFO-MIB", "basCardChassis"), (0, "BAS-CARD-INFO-MIB", "basCardSlot"), (0, "BAS-CARD-INFO-MIB", "basCardIf"), (0, "BAS-CARD-INFO-MIB", "basCardLPort"), (0, "BAS-CARD-INFO-MIB", "basCardRSChassis"), (0, "BAS-CARD-INFO-MIB", "basCardRSSlot"), (0, "BAS-CARD-INFO-MIB", "basCardRSIf"), (0, "BAS-CARD-INFO-MIB", "basCardRSLPort"))
if mibBuilder.loadTexts: basCardRSEntry.setStatus('current')
if mibBuilder.loadTexts: basCardRSEntry.setDescription('Card specific Route Server information entry.')
basCardChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 1), BasChassisId())
if mibBuilder.loadTexts: basCardChassis.setStatus('current')
if mibBuilder.loadTexts: basCardChassis.setDescription('The BAS Chassis ID of this card.')
basCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 2), BasSlotId())
if mibBuilder.loadTexts: basCardSlot.setStatus('current')
if mibBuilder.loadTexts: basCardSlot.setDescription('The BAS Slot ID of this card.')
basCardIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 3), BasInterfaceId())
if mibBuilder.loadTexts: basCardIf.setStatus('current')
if mibBuilder.loadTexts: basCardIf.setDescription('The BAS interface ID of this card.')
basCardLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 4), BasLogicalPortId())
if mibBuilder.loadTexts: basCardLPort.setStatus('current')
if mibBuilder.loadTexts: basCardLPort.setDescription('The BAS logical port ID of this card.')
basCardRSChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 5), BasChassisId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basCardRSChassis.setStatus('current')
if mibBuilder.loadTexts: basCardRSChassis.setDescription('The BAS Chassis ID of a Route Server known by this card.')
basCardRSSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 6), BasSlotId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basCardRSSlot.setStatus('current')
if mibBuilder.loadTexts: basCardRSSlot.setDescription('The BAS Slot ID of a Route Server known by this card.')
basCardRSIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 7), BasInterfaceId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basCardRSIf.setStatus('current')
if mibBuilder.loadTexts: basCardRSIf.setDescription('The BAS interface ID of a Route Server known by this card.')
basCardRSLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 8), BasLogicalPortId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basCardRSLPort.setStatus('current')
if mibBuilder.loadTexts: basCardRSLPort.setDescription('The BAS logical port ID of a Route Server known by this card.')
basCardRSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2, 1, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basCardRSStatus.setStatus('current')
if mibBuilder.loadTexts: basCardRSStatus.setDescription('The row status object used to create and delete a conceptual row according to RowStatus conventions.')
mibBuilder.exportSymbols("BAS-CARD-INFO-MIB", basCardRSEntry=basCardRSEntry, basCardRSSlot=basCardRSSlot, basCardInfoSlot=basCardInfoSlot, basCardLPort=basCardLPort, basCardChassis=basCardChassis, basCardRSStatus=basCardRSStatus, basCardInfoTable=basCardInfoTable, basCardSlot=basCardSlot, basCardRSChassis=basCardRSChassis, basCardInfoEntry=basCardInfoEntry, basAgentConfigSave=basAgentConfigSave, basCardInfoChassis=basCardInfoChassis, basAgentSharedKey=basAgentSharedKey, basCardInfoClass=basCardInfoClass, basCardInfoAdminStatus=basCardInfoAdminStatus, basCardRSTable=basCardRSTable, basAgentTcpPort=basAgentTcpPort, basCardInfoMib=basCardInfoMib, basCardObjects=basCardObjects, basCardReset=basCardReset, basCardWatchdogTimer=basCardWatchdogTimer, basBcmIpAddress=basBcmIpAddress, basCardInfoLPort=basCardInfoLPort, basCardRSIf=basCardRSIf, PYSNMP_MODULE_ID=basCardInfoMib, basCardResetState=basCardResetState, basCardInfoChassisNumber=basCardInfoChassisNumber, basCardRSLPort=basCardRSLPort, basCardInfoIf=basCardInfoIf, basAgentConfigSaveStatus=basAgentConfigSaveStatus, basAgentUdpPort=basAgentUdpPort, basCardIf=basCardIf)
