#
# PySNMP MIB module JUNIPER-CHASSIS-FWDD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-CHASSIS-FWDD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:58:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Counter32, Gauge32, Bits, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, ModuleIdentity, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Counter32", "Gauge32", "Bits", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "ModuleIdentity", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxFwdd = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 34))
if mibBuilder.loadTexts: jnxFwdd.setLastUpdated('200602162158Z')
if mibBuilder.loadTexts: jnxFwdd.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxFwdd.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxFwdd.setDescription("This is Juniper Networks' implementation of enterprise specific MIB for J-Series FWDD module from the router chassis box.")
jnxFwddProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1))
jnxFwddMicroKernelCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddMicroKernelCPUUsage.setStatus('current')
if mibBuilder.loadTexts: jnxFwddMicroKernelCPUUsage.setDescription('The FWDD Micro Kernel CPU utilization in percentage. Zero if unavailable or inapplicable.')
jnxFwddRtThreadsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddRtThreadsCPUUsage.setStatus('current')
if mibBuilder.loadTexts: jnxFwddRtThreadsCPUUsage.setDescription('The FWDD Realtime threads total CPU utilization in percentage. Zero if unavailable or inapplicable.')
jnxFwddHeapUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddHeapUsage.setStatus('current')
if mibBuilder.loadTexts: jnxFwddHeapUsage.setDescription('The FWDD Heap utilization in percentage. Zero if unavailable or inapplicable.')
jnxFwddDmaMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddDmaMemUsage.setStatus('current')
if mibBuilder.loadTexts: jnxFwddDmaMemUsage.setDescription('The FWDD DMA Memory utilization in percentage. Zero if unavailable or inapplicable.')
jnxFwddUpTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddUpTime.setStatus('current')
if mibBuilder.loadTexts: jnxFwddUpTime.setDescription('The FWDD Module uptime expressed in seconds. Zero if unavailable or inapplicable.')
mibBuilder.exportSymbols("JUNIPER-CHASSIS-FWDD-MIB", jnxFwddMicroKernelCPUUsage=jnxFwddMicroKernelCPUUsage, jnxFwddDmaMemUsage=jnxFwddDmaMemUsage, jnxFwddProcess=jnxFwddProcess, jnxFwddUpTime=jnxFwddUpTime, jnxFwdd=jnxFwdd, jnxFwddHeapUsage=jnxFwddHeapUsage, PYSNMP_MODULE_ID=jnxFwdd, jnxFwddRtThreadsCPUUsage=jnxFwddRtThreadsCPUUsage)
