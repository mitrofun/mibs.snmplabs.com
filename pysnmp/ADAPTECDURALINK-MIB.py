#
# PySNMP MIB module ADAPTECDURALINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADAPTECDURALINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:58:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Gauge32, ObjectIdentity, Counter64, Unsigned32, IpAddress, Integer32, NotificationType, MibIdentifier, enterprises, ModuleIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "enterprises", "ModuleIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
adaptec = MibIdentifier((1, 3, 6, 1, 4, 1, 795))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 795, 3))
nic = MibIdentifier((1, 3, 6, 1, 4, 1, 795, 3, 1))
npg = MibIdentifier((1, 3, 6, 1, 4, 1, 795, 3, 1, 2))
duralink = MibIdentifier((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3))
information = MibIdentifier((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1))
numInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numInterfaces.setStatus('mandatory')
numPorts = MibScalar((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numPorts.setStatus('mandatory')
numCards = MibScalar((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numCards.setStatus('mandatory')
interfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2), )
if mibBuilder.loadTexts: interfaceStatsTable.setStatus('mandatory')
interfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1), ).setIndexNames((0, "ADAPTECDURALINK-MIB", "iInterfaceIndex"))
if mibBuilder.loadTexts: interfaceStatsEntry.setStatus('mandatory')
iInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iInterfaceIndex.setStatus('mandatory')
iInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iInterfaceName.setStatus('mandatory')
iInterfacePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iInterfacePorts.setStatus('mandatory')
iPermNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iPermNetAddress.setStatus('mandatory')
iCurrentNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iCurrentNetAddress.setStatus('mandatory')
iDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iDataRate.setStatus('mandatory')
iTotalPacketsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalPacketsTransmitted.setStatus('mandatory')
iTotalBytesTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalBytesTransmitted.setStatus('mandatory')
iTotalPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalPacketsReceived.setStatus('mandatory')
iTotalBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalBytesReceived.setStatus('mandatory')
iTotalTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalTransmitErrors.setStatus('mandatory')
iTotalReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iTotalReceiveErrors.setStatus('mandatory')
iInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standalone", 1), ("failover", 2), ("loadBalanced", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iInterfaceType.setStatus('mandatory')
portStatsTable = MibTable((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3), )
if mibBuilder.loadTexts: portStatsTable.setStatus('mandatory')
portStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1), ).setIndexNames((0, "ADAPTECDURALINK-MIB", "pInterfaceIndex"), (0, "ADAPTECDURALINK-MIB", "pPortIndex"))
if mibBuilder.loadTexts: portStatsEntry.setStatus('mandatory')
pInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pInterfaceIndex.setStatus('mandatory')
pPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pPortIndex.setStatus('mandatory')
pPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pPortName.setStatus('mandatory')
pCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pCardNumber.setStatus('mandatory')
pCardPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pCardPortNumber.setStatus('mandatory')
pPermNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pPermNetAddress.setStatus('mandatory')
pCurrentNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pCurrentNetAddress.setStatus('mandatory')
pDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pDataRate.setStatus('mandatory')
pTotalPacketsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalPacketsTransmitted.setStatus('mandatory')
pTotalBytesTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalBytesTransmitted.setStatus('mandatory')
pTotalPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalPacketsReceived.setStatus('mandatory')
pTotalBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalBytesReceived.setStatus('mandatory')
pTotalTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalTransmitErrors.setStatus('mandatory')
pTotalReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pTotalReceiveErrors.setStatus('mandatory')
pStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("portActive", 1), ("portDown", 2), ("portInStandby", 3), ("portDisabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pStatus.setStatus('mandatory')
cardInformationTable = MibTable((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4), )
if mibBuilder.loadTexts: cardInformationTable.setStatus('mandatory')
cardInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1), ).setIndexNames((0, "ADAPTECDURALINK-MIB", "cCardIndex"))
if mibBuilder.loadTexts: cardInformationEntry.setStatus('mandatory')
cCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCardIndex.setStatus('mandatory')
cCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCardDescription.setStatus('mandatory')
cPortsOnCard = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPortsOnCard.setStatus('mandatory')
cardPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5), )
if mibBuilder.loadTexts: cardPortInfoTable.setStatus('mandatory')
cardPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1), ).setIndexNames((0, "ADAPTECDURALINK-MIB", "cpCardIndex"), (0, "ADAPTECDURALINK-MIB", "cpPortIndex"))
if mibBuilder.loadTexts: cardPortInfoEntry.setStatus('mandatory')
cpCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpCardIndex.setStatus('mandatory')
cpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpPortIndex.setStatus('mandatory')
cpInterfaceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpInterfaceNumber.setStatus('mandatory')
cpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpPortNumber.setStatus('mandatory')
cpTableNumber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpTableNumber1.setStatus('mandatory')
duralinkStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3) + (0,1)).setObjects(("ADAPTECDURALINK-MIB", "pInterfaceIndex"), ("ADAPTECDURALINK-MIB", "pPortIndex"), ("ADAPTECDURALINK-MIB", "pStatus"))
mibBuilder.exportSymbols("ADAPTECDURALINK-MIB", nic=nic, iTotalTransmitErrors=iTotalTransmitErrors, pTotalPacketsReceived=pTotalPacketsReceived, pStatus=pStatus, pCardNumber=pCardNumber, numCards=numCards, adaptec=adaptec, interfaceStatsTable=interfaceStatsTable, portStatsTable=portStatsTable, cpInterfaceNumber=cpInterfaceNumber, duralinkStatusTrap=duralinkStatusTrap, numInterfaces=numInterfaces, cpPortIndex=cpPortIndex, duralink=duralink, iPermNetAddress=iPermNetAddress, iTotalBytesTransmitted=iTotalBytesTransmitted, pPortIndex=pPortIndex, cCardDescription=cCardDescription, cardPortInfoTable=cardPortInfoTable, iInterfaceName=iInterfaceName, pTotalBytesTransmitted=pTotalBytesTransmitted, products=products, iTotalPacketsReceived=iTotalPacketsReceived, iDataRate=iDataRate, pCurrentNetAddress=pCurrentNetAddress, pTotalReceiveErrors=pTotalReceiveErrors, interfaceStatsEntry=interfaceStatsEntry, iTotalPacketsTransmitted=iTotalPacketsTransmitted, portStatsEntry=portStatsEntry, iInterfaceIndex=iInterfaceIndex, iInterfacePorts=iInterfacePorts, cPortsOnCard=cPortsOnCard, iTotalReceiveErrors=iTotalReceiveErrors, cardInformationEntry=cardInformationEntry, cpPortNumber=cpPortNumber, cardPortInfoEntry=cardPortInfoEntry, pCardPortNumber=pCardPortNumber, pPermNetAddress=pPermNetAddress, numPorts=numPorts, npg=npg, cCardIndex=cCardIndex, iInterfaceType=iInterfaceType, iTotalBytesReceived=iTotalBytesReceived, pTotalBytesReceived=pTotalBytesReceived, cpTableNumber1=cpTableNumber1, cardInformationTable=cardInformationTable, iCurrentNetAddress=iCurrentNetAddress, information=information, pTotalTransmitErrors=pTotalTransmitErrors, cpCardIndex=cpCardIndex, pTotalPacketsTransmitted=pTotalPacketsTransmitted, pInterfaceIndex=pInterfaceIndex, pDataRate=pDataRate, pPortName=pPortName)
