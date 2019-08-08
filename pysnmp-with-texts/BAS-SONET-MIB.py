#
# PySNMP MIB module BAS-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-SONET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
basSonet, = mibBuilder.importSymbols("BAS-MIB", "basSonet")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter32, Counter64, ModuleIdentity, Unsigned32, TimeTicks, iso, IpAddress, MibIdentifier, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "TimeTicks", "iso", "IpAddress", "MibIdentifier", "ObjectIdentity", "Gauge32")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
basSonetMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1))
if mibBuilder.loadTexts: basSonetMib.setLastUpdated('9810071415Z')
if mibBuilder.loadTexts: basSonetMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basSonetMib.setContactInfo(' Tech Support Broadband Access Systems 4 Technology Drive Westborough, MA 01581 U.S.A. 508-366-8833 support@basystems.com')
if mibBuilder.loadTexts: basSonetMib.setDescription('This MIB module defines the configuration and status MIB objects for a Broadband Access System SONET interface.')
basSonetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1))
basSonetPathTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1), )
if mibBuilder.loadTexts: basSonetPathTable.setStatus('current')
if mibBuilder.loadTexts: basSonetPathTable.setDescription('A table containing SONET Path specific variables for this POS implementation.')
basSonetPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: basSonetPathEntry.setStatus('current')
if mibBuilder.loadTexts: basSonetPathEntry.setDescription('Management information about a particular POS Link.')
basSonetPathB3Err = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathB3Err.setStatus('current')
if mibBuilder.loadTexts: basSonetPathB3Err.setDescription('The number of packets received on this link with B3 bit errors. Bit Interleaved Parity 8 is calculated over all bits in the SPE of each frame.')
basSonetPathG1Err = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathG1Err.setStatus('current')
if mibBuilder.loadTexts: basSonetPathG1Err.setDescription('The number of B3 errors that were detected by the remote terminal in its received signal. ')
basSonetPathPais = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathPais.setStatus('current')
if mibBuilder.loadTexts: basSonetPathPais.setDescription('The number of times a Path Alarm Indication Signal has been detected. A PAIS occurs if all the H1/H2 pointer bytes in the received SONET frame are 01.')
basSonetPathPrdi = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathPrdi.setStatus('current')
if mibBuilder.loadTexts: basSonetPathPrdi.setDescription('The number of times a Path Remote Defect Indication has been detected. A PRDI occurs if bits 5,6 and 7 of the G1 byte received with the same value for 5 onsecutive frames.')
basSonetPathPlop = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathPlop.setStatus('current')
if mibBuilder.loadTexts: basSonetPathPlop.setDescription('The number of times a Path Loss of Pointer has been detected. A PLOP occurs if all the H1/H2 pointer bytes in the received SONET frame are not all 01 indicating PRDI or the first pair equals 00 and all other pairs equaling 11 indicating normal operation.')
basSonetPathB3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSonetPathB3Threshold.setStatus('current')
if mibBuilder.loadTexts: basSonetPathB3Threshold.setDescription('The number of packets received with B3 errors hits this threshold issue an alarm.')
basSonetPathRxJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathRxJ1.setStatus('current')
if mibBuilder.loadTexts: basSonetPathRxJ1.setDescription('The first J1 byte received in last packet.')
basSonetPathRxC2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathRxC2.setStatus('current')
if mibBuilder.loadTexts: basSonetPathRxC2.setDescription('C2 byte received in last packet.')
basSonetPathRxG1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetPathRxG1.setStatus('current')
if mibBuilder.loadTexts: basSonetPathRxG1.setDescription('G1 byte received in last packet.')
basSonetLineTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2), )
if mibBuilder.loadTexts: basSonetLineTable.setStatus('current')
if mibBuilder.loadTexts: basSonetLineTable.setDescription('A table containing SONET Line specific variables for this POS implementation.')
basSonetLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: basSonetLineEntry.setStatus('current')
if mibBuilder.loadTexts: basSonetLineEntry.setDescription('Management information about a particular POS Link.')
basSonetLineTxErr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineTxErr.setStatus('current')
if mibBuilder.loadTexts: basSonetLineTxErr.setDescription('The sum of all transmit errors that caused the packet to not be transmitted. These errors consist of tx fifo error, link layer errors, minimum packet size violations, maximum packet size violations and tx parity errors.')
basSonetLineB1Err = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineB1Err.setStatus('current')
if mibBuilder.loadTexts: basSonetLineB1Err.setDescription('The number of packets received on this link with B1 bit errors. Bit Interleaved Parity 8 is calculated over all bytes of each frame. ')
basSonetLineB2Err = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineB2Err.setStatus('current')
if mibBuilder.loadTexts: basSonetLineB2Err.setDescription('The number of packets received on this link with B2 bit errors. Bit Interleaved Parity 8 is calculated over all bytes of each frame except for the first three rows of the TOH ')
basSonetLineM1Err = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineM1Err.setStatus('current')
if mibBuilder.loadTexts: basSonetLineM1Err.setDescription('The number of B2 errors that were detected by the remote terminal in its received signal.')
basSonetLineRxFifoOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxFifoOverflow.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxFifoOverflow.setDescription('The number of packets received on this link with an error detected in the receive fifo.')
basSonetLineRxAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxAbort.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxAbort.setDescription('The number of packets received on this link in which the abort sequence is detected.')
basSonetLineRxRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxRunts.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxRunts.setDescription('The number of packets received on this link which are smaller than the minimum packet size.')
basSonetLineLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLoc.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLoc.setDescription('The number of times a loss of clock has been detected. LOC occurs if no transitions are detected on the receive SONET clock for 16 periods of the transmit clock..')
basSonetLineLof = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLof.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLof.setDescription('The number of times a loss of frame has been detected. LOF occurs if RX_OOF (out-of-frame) is active continuously for 24 consecutive frames (3 ms).')
basSonetLineLos = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLos.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLos.setDescription('The number of times a loss of signal has been detected. A LOS indicates to the framer that there is no signal present from the optical receiver.')
basSonetLineLais = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLais.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLais.setDescription("The number of times a Line Alarm Indication Signal has been detected. A LAIS occurs if the 3 LSBs of K2 are received as '111' for 5 consecutive frames")
basSonetLineLrdi = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLrdi.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLrdi.setDescription("The number of times a Line Remote Defect Indication has been detected. A LRDI occurs if the 3 LSBs of K2 are not received as '110' for 5 consecutive frames.")
basSonetLineB1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSonetLineB1Threshold.setStatus('current')
if mibBuilder.loadTexts: basSonetLineB1Threshold.setDescription('The number of packets received with B1 errors hits this threshold issue an alarm.')
basSonetLineB2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSonetLineB2Threshold.setStatus('current')
if mibBuilder.loadTexts: basSonetLineB2Threshold.setDescription('The number of packets received with B2 errors hits this threshold issue an alarm.')
basSonetLineSFThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSonetLineSFThreshold.setStatus('current')
if mibBuilder.loadTexts: basSonetLineSFThreshold.setDescription('The number of packets received with B2 errors hits this threshold issue a signal fail alarm.')
basSonetLineSDThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSonetLineSDThreshold.setStatus('current')
if mibBuilder.loadTexts: basSonetLineSDThreshold.setDescription('The number of packets received with B2 errors hits this threshold issue a signal degrade alarm.')
basSonetLineLastCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 17), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineLastCleared.setStatus('current')
if mibBuilder.loadTexts: basSonetLineLastCleared.setDescription('The value of sysUpTime when these Counter32s were last cleared.')
basSonetLineRxK1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxK1.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxK1.setDescription('K1 byte received in last packet.')
basSonetLineRxK2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxK2.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxK2.setDescription('K2 byte received in last packet.')
basSonetLineRxGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basSonetLineRxGiants.setStatus('current')
if mibBuilder.loadTexts: basSonetLineRxGiants.setDescription('The number of packets received on this link which are larger than the maximum packet size.')
mibBuilder.exportSymbols("BAS-SONET-MIB", basSonetObjects=basSonetObjects, basSonetLineLrdi=basSonetLineLrdi, basSonetLineB1Threshold=basSonetLineB1Threshold, basSonetLineEntry=basSonetLineEntry, basSonetLineLos=basSonetLineLos, basSonetPathG1Err=basSonetPathG1Err, basSonetPathPlop=basSonetPathPlop, basSonetLineB1Err=basSonetLineB1Err, basSonetLineTxErr=basSonetLineTxErr, basSonetPathRxJ1=basSonetPathRxJ1, basSonetLineRxK1=basSonetLineRxK1, basSonetLineB2Threshold=basSonetLineB2Threshold, PYSNMP_MODULE_ID=basSonetMib, basSonetMib=basSonetMib, basSonetLineSFThreshold=basSonetLineSFThreshold, basSonetLineRxGiants=basSonetLineRxGiants, basSonetLineRxAbort=basSonetLineRxAbort, basSonetPathPrdi=basSonetPathPrdi, basSonetLineRxRunts=basSonetLineRxRunts, basSonetPathEntry=basSonetPathEntry, basSonetPathPais=basSonetPathPais, basSonetLineRxK2=basSonetLineRxK2, basSonetPathTable=basSonetPathTable, basSonetLineB2Err=basSonetLineB2Err, basSonetLineLoc=basSonetLineLoc, basSonetLineRxFifoOverflow=basSonetLineRxFifoOverflow, basSonetLineLastCleared=basSonetLineLastCleared, basSonetPathB3Err=basSonetPathB3Err, basSonetPathRxC2=basSonetPathRxC2, basSonetLineSDThreshold=basSonetLineSDThreshold, basSonetLineM1Err=basSonetLineM1Err, basSonetPathRxG1=basSonetPathRxG1, basSonetLineTable=basSonetLineTable, basSonetPathB3Threshold=basSonetPathB3Threshold, basSonetLineLof=basSonetLineLof, basSonetLineLais=basSonetLineLais)