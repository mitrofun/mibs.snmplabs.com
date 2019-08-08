#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-POLICY-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
QosInterfaceQueueType, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosInterfaceQueueType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, Counter32, Integer32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Counter32", "Integer32", "Unsigned32", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoQosPolicyConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 159))
ciscoQosPolicyConfigMIB.setRevisions(('2000-11-02 10:30', '2000-02-26 19:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setRevisionsDescriptions(("Revised version from CISCO-QOS-CONFIG-MIB. The original OID is assigned to CISCO-QOS-CONFIG-MIB and then after discussing with people in COPS group, we decided to change the name of the MIB. And also adding some objects to reflect the difference between users' QoS policy configuration and runtime QoS policy configuration.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setLastUpdated('200011021030Z')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134, USA Tel: +1 800 553-NETS E-mail: cs-wbu@cisco.com')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setDescription("This MIB module defines managed objects that support the policy source configuration of Quality of Service (QoS) on the device. Terminology : Common Open Policy Service (COPS) : A client/server model for supporting policy control over QoS Signaling Protocols and provisioned QoS resource management, etc. COPS is a query and response protocol that can be used to exchange policy information between a policy server (Policy Decision Point or PDP) and its clients (Policy Enforcement Points or PEPs). Policy Information Base (PIB) : The database of policy information stored in the COPS client device. QoS : The method which attempts to ensure that the network requirements of different applications can be met by giving preferential forwarding treatment to some traffic, perhaps at the expense of other traffic. QoS policy : a set of parameters used to achieve QoS purpose. The device uses these parameters in flow classification, flow scheduling, flow policing and codepoint mutation. RSVP : Resource Reservation Protocol. RSVP is a signaling mechanism that the application will use to signal parameters to the network, so that network can assign QoS for the application data stream. COPS-PR : a COPS client type which supports device's provisioning of QoS policy. COPS-RSVP : a COPS client type which supports device's outsourcing of QoS policy (RSVP). ")
class QosPolicySource(TextualConvention, Integer32):
    description = 'The source where a device obtains QoS policy. none (1) indicates that there is no QoS policy applied on this device. And this value only can be read and cannot be set by the users. local (2) indicates that the QoS policy is from local device configuration. For example, the QoS policy can be configured through command line interface (CLI). cops (3) indicates that the QoS policy is from a COPS server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("local", 2), ("cops", 3))

ciscoQosPolicyConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1))
qosPolicyGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1))
qosPolicyInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2))
qosEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEnabled.setStatus('current')
if mibBuilder.loadTexts: qosEnabled.setDescription('Indicates whether the QoS feature is enabled on the device. true(1) means that the QoS feature is enabled on this device. false(2) means that the QoS feature is disabled. All the QoS policy on the device will be ignored.')
qosPrAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 2), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrAdminPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosPrAdminPolicySource.setDescription("Indicates the desired source of a device's provisioning of QoS policy for the whole device. Actually, the source of an interface's provisioning of QoS policy is controlled by two level configurations. The first level is the system level to be the global control for the whole device. This object is for the system level. The second level is for each individual interface. The qosPrIfAdminPolicySource is for the interface level. So, the value of this object will decide that the value of qosPrIfAdminPolicySource can take precedence or not. If this object is configured to cops(3), the value of qosPrIfAdminPolicySource has the precedence configuration of the interface's provisioning of QoS policy source. That is to say if this object is configured to local(2), then the value of qosPrIfAdminPolicySource will be ignored. It means the provisioning of QoS policy source of all the interfaces in this device will be from local information if this MIB is configured to local(2). If this object is configured to cops(3), then the final provisioning of QoS policy of an interface is determined by the configuration of the qosPrIfAdminPolicySource object of that interface. Changing qosPrIfAdminPolicySource of an interface from cops(3) to local(2) while the value of this object is cops(3) makes the interface discard the QoS provisioning policy from the COPS server and uses the local QoS provisioning policy configuration instead.")
qosPrOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 3), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrOperPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosPrOperPolicySource.setDescription("Indicates the operational source of a device's provisioning of QoS policy. Note that when qosPrAdminPolicySource transitions to cops(3), qosPrOperPolicySource will normally also transition to cops(3). In this situation, it is possible that qosPrOperPolicySource's transition will not occur immediately because the system is initializing the COPS function at the system booting up time, but rather after a small time lag to complete certain operations before going 'cops'.")
qosRsvpAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 4), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosRsvpAdminPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosRsvpAdminPolicySource.setDescription("Indicates the desired source of a device's outsourcing of QoS policy. Outsourcing means the policy information is from outside source not from local information.")
qosRsvpOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 5), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosRsvpOperPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosRsvpOperPolicySource.setDescription("Indicates the current operational source of a device's outsourcing of QoS policy. Note that when qosRsvpAdminPolicySource transitions to cops(3), qosRsvpOperPolicySource will normally also transition to cops(3). In this situation, it is possible that qosRsvpOperPolicySource's transition will not occur immediately because the system is initializing the COPS function at the system boot up time, but rather after a small time lag to complete certain operations before going 'cops'.")
qosCopsPolicyStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keep", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCopsPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: qosCopsPolicyStatus.setDescription('This object indicates whether the QoS policy downloaded from COPS server should be kept or discarded by the system while the COPS function is not running in the system or the connection between PDP and PEP is lost or any other reason that system cannot get the QoS policy from COPS server.')
qosPrIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1), )
if mibBuilder.loadTexts: qosPrIfTable.setStatus('current')
if mibBuilder.loadTexts: qosPrIfTable.setDescription('A list of interface entries. An entry will exist for each interface which can support the provisioning of QoS policy feature.')
qosPrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qosPrIfEntry.setStatus('current')
if mibBuilder.loadTexts: qosPrIfEntry.setDescription('An entry containing the configuration of provisioning of QoS policy of a particular interface.')
qosPrIfAdminPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 1), QosPolicySource().clone('cops')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrIfAdminPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosPrIfAdminPolicySource.setDescription('Indicates the desired source of QoS provision policy for this interface. This object is only effective when the value of qosPrOperPolicySource is cops(3) and the value of qosEnabled is true(1).')
qosPrIfOperPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 2), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrIfOperPolicySource.setStatus('current')
if mibBuilder.loadTexts: qosPrIfOperPolicySource.setDescription("Indicates the operational source of QoS provisioning policy for this interface. When the value of the object qosPrOperPolicySource is local(2), the QoS provisioning policy for this interface is taken from device's local configuration. If qosPrOperPolicySource is configured to cops(3), the current operational source of QoS provisioning policy will depend on the configuration of qosPrIfAdminPolicySource object. Here is the logic. IF qosPrOperPolicySource == local(2) THEN qosPrIfOperPolicySource is local(2) ELSE IF qosPrOperPolicySource == cops(3) THEN IF qosPrIfAdminPolicySource == cops(3) THEN qosPrIfOperPolicySource is cops(3) ELSE qosPrIfOperPolicySource is local(2) ELSE qosPrIfOperPolicySource is none(1) END END For example, if qosPrOperPolicySource shows local(2), although the qosPrIfAdminPolicySource is configured cops(3), the QoS provisioning policy running on this interface is from local device configuration. It means this object will be local(2). Note that when qosPrIfAdminPolicySource transitions to cops(3) if qosPrOperPolicySource is cops(3), qosPrIfOperPolicySource will normally also transition to cops(3). In this situation, it is possible that qosPrIfOperPolicySource's transition will not occur immediately because the system is initializing the COPS function at the system boot up time, but rather after a small time lag to complete certain operations before going 'cops'.")
qosIfCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2), )
if mibBuilder.loadTexts: qosIfCapabilityTable.setStatus('current')
if mibBuilder.loadTexts: qosIfCapabilityTable.setDescription('A list of interface entries. An entry will exist for each interface which can support the QoS feature.')
qosIfCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfDirection"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfQType"))
if mibBuilder.loadTexts: qosIfCapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: qosIfCapabilityEntry.setDescription("A description of an interface's QoS capabilities.")
qosIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2), ("both", 3))))
if mibBuilder.loadTexts: qosIfDirection.setStatus('current')
if mibBuilder.loadTexts: qosIfDirection.setDescription("The traffic direction of the interface. 'ingress' means the traffic coming in the interface. 'egress' means the traffic going out the interface. 'both' means the traffic coming in and going out.")
qosIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 2), QosInterfaceQueueType())
if mibBuilder.loadTexts: qosIfQType.setStatus('current')
if mibBuilder.loadTexts: qosIfQType.setDescription('The interface type in terms of number of queues and thresholds. A queue is a buffer for storing network packets. A threshold is a water mark used to control traffic amount of a queue.')
qosIfCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 3), Bits().clone(namedValues=NamedValues(("unspecified", 0), ("inputL2Classification", 1), ("inputIpClassification", 2), ("outputL2Classification", 3), ("outputIpClassification", 4), ("inputPortClassification", 19), ("outputPortClassification", 20), ("inputUflowPolicing", 5), ("inputAggregatePolicing", 6), ("outputUflowPolicing", 7), ("outputAggregatePolicing", 8), ("policeByMarkingDown", 9), ("policeByDropping", 10), ("inputUflowShaping", 21), ("inputAggregateShaping", 22), ("outputUflowShaping", 23), ("outputAggregateShaping", 24), ("fifo", 11), ("wrr", 12), ("wfq", 13), ("cq", 14), ("pq", 15), ("cbwfq", 16), ("pqWrr", 25), ("pqCbwfq", 26), ("tailDrop", 17), ("wred", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosIfCapabilities.setStatus('current')
if mibBuilder.loadTexts: qosIfCapabilities.setDescription('An enumeration of interface capabilities. Used by the management side to select policies and configuration to push to the device.')
ciscoQosPolicyMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 2))
ciscoQosPolicyConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3))
ciscoQosPolicyConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1))
ciscoQosPolicyConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2))
ciscoQosPolicyConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrInterfaceGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosInterfaceCapabilityGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPolicyConfigMIBCompliance = ciscoQosPolicyConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIBCompliance.setDescription('The compliance statement for the CISCO-QOS-POLICY-CONFIG-MIB.')
qosGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosGlobalGroup = qosGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: qosGlobalGroup.setDescription('A collection of objects providing the ability to enable/disable QoS feature on the device.')
qosPrGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 2)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrGlobalGroup = qosPrGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: qosPrGlobalGroup.setDescription('A collection of objects providing the global configuration of the provisioning of QoS policy source on the device.')
qosRsvpGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 3)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosRsvpGlobalGroup = qosRsvpGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: qosRsvpGlobalGroup.setDescription('A collection of objects providing the global configuration of the outsourcing of QoS policy source on the device.')
qosPrInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 4)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrInterfaceGroup = qosPrInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: qosPrInterfaceGroup.setDescription('A collection of objects providing the interface level configuration of the provisioning of QoS policy source on the device.')
qosInterfaceCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 5)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosIfCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosInterfaceCapabilityGroup = qosInterfaceCapabilityGroup.setStatus('current')
if mibBuilder.loadTexts: qosInterfaceCapabilityGroup.setDescription('A collection of object providing the QoS capabilities of the interface on the device to help QoS policy configuration.')
qosCopsPolicyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 6)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosCopsPolicyStatusGroup = qosCopsPolicyStatusGroup.setStatus('current')
if mibBuilder.loadTexts: qosCopsPolicyStatusGroup.setDescription('A collection of object providing the status of QoS policy downloaded from COPS server.')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-MIB", ciscoQosPolicyConfigMIBCompliance=ciscoQosPolicyConfigMIBCompliance, qosCopsPolicyStatus=qosCopsPolicyStatus, ciscoQosPolicyConfigMIBConformance=ciscoQosPolicyConfigMIBConformance, qosPrIfEntry=qosPrIfEntry, qosPolicyGlobalObjects=qosPolicyGlobalObjects, qosRsvpAdminPolicySource=qosRsvpAdminPolicySource, qosPrIfAdminPolicySource=qosPrIfAdminPolicySource, qosPrGlobalGroup=qosPrGlobalGroup, qosIfCapabilityEntry=qosIfCapabilityEntry, ciscoQosPolicyMIBNotifications=ciscoQosPolicyMIBNotifications, qosPrAdminPolicySource=qosPrAdminPolicySource, qosIfDirection=qosIfDirection, qosIfQType=qosIfQType, qosPolicyInterfaceObjects=qosPolicyInterfaceObjects, qosPrIfTable=qosPrIfTable, qosInterfaceCapabilityGroup=qosInterfaceCapabilityGroup, qosPrInterfaceGroup=qosPrInterfaceGroup, ciscoQosPolicyConfigMIBCompliances=ciscoQosPolicyConfigMIBCompliances, qosEnabled=qosEnabled, qosCopsPolicyStatusGroup=qosCopsPolicyStatusGroup, qosRsvpGlobalGroup=qosRsvpGlobalGroup, ciscoQosPolicyConfigMIBGroups=ciscoQosPolicyConfigMIBGroups, qosGlobalGroup=qosGlobalGroup, ciscoQosPolicyConfigMIB=ciscoQosPolicyConfigMIB, qosPrIfOperPolicySource=qosPrIfOperPolicySource, ciscoQosPolicyConfigMIBObjects=ciscoQosPolicyConfigMIBObjects, qosRsvpOperPolicySource=qosRsvpOperPolicySource, qosIfCapabilityTable=qosIfCapabilityTable, qosIfCapabilities=qosIfCapabilities, PYSNMP_MODULE_ID=ciscoQosPolicyConfigMIB, qosPrOperPolicySource=qosPrOperPolicySource, QosPolicySource=QosPolicySource)