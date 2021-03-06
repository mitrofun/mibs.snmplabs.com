#
# PySNMP MIB module NBS-OSA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-OSA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifAlias, = mibBuilder.importSymbols("IF-MIB", "ifAlias")
nbs, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, NotificationType, Bits, MibIdentifier, Unsigned32, TimeTicks, Counter32, Integer32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "Bits", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter32", "Integer32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsOsaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 207))
if mibBuilder.loadTexts: nbsOsaMib.setLastUpdated('200912090000Z')
if mibBuilder.loadTexts: nbsOsaMib.setOrganization('NBS')
class InterfaceIndex(Integer32):
    pass

nbsOsaPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 1))
if mibBuilder.loadTexts: nbsOsaPortGrp.setStatus('current')
nbsOsaSpectrumGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 2))
if mibBuilder.loadTexts: nbsOsaSpectrumGrp.setStatus('current')
nbsOsaChannelGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 3))
if mibBuilder.loadTexts: nbsOsaChannelGrp.setStatus('current')
nbsOsaTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 207, 4))
if mibBuilder.loadTexts: nbsOsaTraps.setStatus('current')
nbsOsaPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaPortTableSize.setStatus('current')
nbsOsaPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 1, 2), )
if mibBuilder.loadTexts: nbsOsaPortTable.setStatus('current')
nbsOsaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaPortIfIndex"))
if mibBuilder.loadTexts: nbsOsaPortEntry.setStatus('current')
nbsOsaPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: nbsOsaPortIfIndex.setStatus('current')
nbsOsaPortAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaPortAttenuation.setStatus('current')
nbsOsaPortChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaPortChannels.setStatus('current')
nbsOsaSpectrumTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumTableSize.setStatus('current')
nbsOsaSpectrumTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 2, 2), )
if mibBuilder.loadTexts: nbsOsaSpectrumTable.setStatus('current')
nbsOsaSpectrumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaSpectrumIfIndex"), (0, "NBS-OSA-MIB", "nbsOsaSpectrumWavelength"))
if mibBuilder.loadTexts: nbsOsaSpectrumEntry.setStatus('current')
nbsOsaSpectrumIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: nbsOsaSpectrumIfIndex.setStatus('current')
nbsOsaSpectrumWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 3), Integer32())
if mibBuilder.loadTexts: nbsOsaSpectrumWavelength.setStatus('current')
nbsOsaSpectrumTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumTimestamp.setStatus('current')
nbsOsaSpectrumRxPowerOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaSpectrumRxPowerOper.setStatus('current')
nbsOsaChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 207, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelTableSize.setStatus('current')
nbsOsaChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 207, 3, 2), )
if mibBuilder.loadTexts: nbsOsaChannelTable.setStatus('current')
nbsOsaChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1), ).setIndexNames((0, "NBS-OSA-MIB", "nbsOsaChannelIfIndex"), (0, "NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaChannelEntry.setStatus('current')
nbsOsaChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsOsaChannelIfIndex.setStatus('current')
nbsOsaChannelFrequencyNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsOsaChannelFrequencyNominal.setStatus('current')
nbsOsaChannelBand = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("cBand", 1), ("hBand", 2), ("lBand", 3), ("qBand", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelBand.setStatus('current')
nbsOsaChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelNumber.setStatus('current')
nbsOsaChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelStatus.setStatus('current')
nbsOsaChannelTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelTimestamp.setStatus('current')
nbsOsaChannelFrequencyOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelFrequencyOper.setStatus('current')
nbsOsaChannelRxPowerOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 8), Integer32().clone(-100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerOper.setStatus('current')
nbsOsaChannelRxPowerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerMin.setStatus('current')
nbsOsaChannelRxPowerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelRxPowerMax.setStatus('current')
nbsOsaChannelOSNROper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOsaChannelOSNROper.setStatus('current')
nbsOsaChannelOSNRMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 12), Integer32().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelOSNRMin.setStatus('current')
nbsOsaChannelOSNRMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 13), Integer32().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOsaChannelOSNRMax.setStatus('current')
nbsOsaTrapPortChannelAdded = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 1)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaTrapPortChannelAdded.setStatus('current')
nbsOsaTrapPortChannelDropped = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 2)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
if mibBuilder.loadTexts: nbsOsaTrapPortChannelDropped.setStatus('current')
nbsOsaTrapPortRxPowerTooLow = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 3)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMin"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerTooLow.setStatus('current')
nbsOsaTrapPortRxPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 4)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerOK.setStatus('current')
nbsOsaTrapPortRxPowerTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 5)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMax"), ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
if mibBuilder.loadTexts: nbsOsaTrapPortRxPowerTooHigh.setStatus('current')
nbsOsaTrapPortOSNRTooLow = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 6)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNRMin"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNRTooLow.setStatus('current')
nbsOsaTrapPortOSNROK = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 7)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNROK.setStatus('current')
nbsOsaTrapPortOSNRTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 207, 4, 8)).setObjects(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-OSA-MIB", "nbsOsaChannelBand"), ("NBS-OSA-MIB", "nbsOsaChannelNumber"), ("NBS-OSA-MIB", "nbsOsaChannelOSNRMax"), ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
if mibBuilder.loadTexts: nbsOsaTrapPortOSNRTooHigh.setStatus('current')
mibBuilder.exportSymbols("NBS-OSA-MIB", nbsOsaChannelEntry=nbsOsaChannelEntry, nbsOsaSpectrumGrp=nbsOsaSpectrumGrp, nbsOsaChannelStatus=nbsOsaChannelStatus, InterfaceIndex=InterfaceIndex, nbsOsaTrapPortOSNRTooLow=nbsOsaTrapPortOSNRTooLow, nbsOsaChannelTable=nbsOsaChannelTable, nbsOsaChannelBand=nbsOsaChannelBand, nbsOsaChannelTimestamp=nbsOsaChannelTimestamp, nbsOsaSpectrumWavelength=nbsOsaSpectrumWavelength, nbsOsaPortTable=nbsOsaPortTable, nbsOsaChannelTableSize=nbsOsaChannelTableSize, nbsOsaSpectrumRxPowerOper=nbsOsaSpectrumRxPowerOper, nbsOsaTrapPortRxPowerOK=nbsOsaTrapPortRxPowerOK, nbsOsaSpectrumTimestamp=nbsOsaSpectrumTimestamp, nbsOsaChannelRxPowerOper=nbsOsaChannelRxPowerOper, nbsOsaTrapPortRxPowerTooHigh=nbsOsaTrapPortRxPowerTooHigh, nbsOsaChannelOSNROper=nbsOsaChannelOSNROper, nbsOsaChannelGrp=nbsOsaChannelGrp, nbsOsaPortChannels=nbsOsaPortChannels, nbsOsaTraps=nbsOsaTraps, nbsOsaChannelRxPowerMax=nbsOsaChannelRxPowerMax, nbsOsaChannelIfIndex=nbsOsaChannelIfIndex, nbsOsaChannelOSNRMin=nbsOsaChannelOSNRMin, nbsOsaPortTableSize=nbsOsaPortTableSize, nbsOsaTrapPortChannelAdded=nbsOsaTrapPortChannelAdded, nbsOsaMib=nbsOsaMib, nbsOsaTrapPortChannelDropped=nbsOsaTrapPortChannelDropped, nbsOsaSpectrumTableSize=nbsOsaSpectrumTableSize, nbsOsaChannelRxPowerMin=nbsOsaChannelRxPowerMin, nbsOsaChannelFrequencyNominal=nbsOsaChannelFrequencyNominal, nbsOsaSpectrumIfIndex=nbsOsaSpectrumIfIndex, nbsOsaPortIfIndex=nbsOsaPortIfIndex, nbsOsaSpectrumTable=nbsOsaSpectrumTable, nbsOsaChannelOSNRMax=nbsOsaChannelOSNRMax, nbsOsaSpectrumEntry=nbsOsaSpectrumEntry, nbsOsaTrapPortRxPowerTooLow=nbsOsaTrapPortRxPowerTooLow, nbsOsaPortGrp=nbsOsaPortGrp, PYSNMP_MODULE_ID=nbsOsaMib, nbsOsaPortAttenuation=nbsOsaPortAttenuation, nbsOsaTrapPortOSNROK=nbsOsaTrapPortOSNROK, nbsOsaChannelNumber=nbsOsaChannelNumber, nbsOsaTrapPortOSNRTooHigh=nbsOsaTrapPortOSNRTooHigh, nbsOsaPortEntry=nbsOsaPortEntry, nbsOsaChannelFrequencyOper=nbsOsaChannelFrequencyOper)
