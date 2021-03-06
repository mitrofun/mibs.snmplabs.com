#
# PySNMP MIB module RMM2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RMM2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ObjectIdentity, NotificationType, MibIdentifier, Counter64, ModuleIdentity, iso, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "Gauge32", "Integer32")
TextualConvention, DisplayString, DateAndTime, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime", "MacAddress")
intelRmm2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 343))
if mibBuilder.loadTexts: intelRmm2.setLastUpdated('200612130000Z')
if mibBuilder.loadTexts: intelRmm2.setOrganization('Intel Corporation')
rmm2 = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1))
board = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 1))
host = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 3))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 4))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 1, 1))
users = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 1, 2))
actions = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 1, 3))
hostInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 2, 1))
hostActions = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 1, 2, 2))
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
ip = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ip.setStatus('current')
netmask = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netmask.setStatus('current')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gateway.setStatus('current')
mac = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mac.setStatus('current')
hardwareRev = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareRev.setStatus('current')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 8), DisplayString())
if mibBuilder.loadTexts: eventType.setStatus('current')
eventDesc = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 9), DisplayString())
if mibBuilder.loadTexts: eventDesc.setStatus('current')
userLoginName = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 10), DisplayString())
if mibBuilder.loadTexts: userLoginName.setStatus('current')
remoteHost = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 11), IpAddress())
if mibBuilder.loadTexts: remoteHost.setStatus('current')
checkHostPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("hasPower", 1), ("hasnoPower", 2), ("error", 3), ("notsupported", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkHostPower.setStatus('current')
hostReset = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostReset.setStatus('current')
hostPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("longPress", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostPower.setStatus('current')
resetBoard = MibScalar((1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetBoard.setStatus('current')
dummyTrap = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 1))
if mibBuilder.loadTexts: dummyTrap.setStatus('current')
loginfailed = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 2)).setObjects(("RMM2-MIB", "userLoginName"), ("RMM2-MIB", "remoteHost"))
if mibBuilder.loadTexts: loginfailed.setStatus('current')
loginsuccess = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 3)).setObjects(("RMM2-MIB", "userLoginName"), ("RMM2-MIB", "remoteHost"))
if mibBuilder.loadTexts: loginsuccess.setStatus('current')
securityViolation = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 4)).setObjects(("RMM2-MIB", "userLoginName"), ("RMM2-MIB", "remoteHost"))
if mibBuilder.loadTexts: securityViolation.setStatus('current')
generic = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 5)).setObjects(("RMM2-MIB", "eventType"), ("RMM2-MIB", "eventDesc"))
if mibBuilder.loadTexts: generic.setStatus('current')
logout = NotificationType((1, 3, 6, 1, 4, 1, 343, 1, 4, 6)).setObjects(("RMM2-MIB", "userLoginName"), ("RMM2-MIB", "remoteHost"))
if mibBuilder.loadTexts: logout.setStatus('current')
mibBuilder.exportSymbols("RMM2-MIB", hardwareRev=hardwareRev, netmask=netmask, firmwareVersion=firmwareVersion, securityViolation=securityViolation, dummyTrap=dummyTrap, hostActions=hostActions, actions=actions, hostPower=hostPower, loginsuccess=loginsuccess, eventType=eventType, traps=traps, loginfailed=loginfailed, board=board, gateway=gateway, host=host, generic=generic, serialNumber=serialNumber, ip=ip, checkHostPower=checkHostPower, PYSNMP_MODULE_ID=intelRmm2, intelRmm2=intelRmm2, resetBoard=resetBoard, info=info, hostReset=hostReset, mac=mac, rmm2=rmm2, hostInfo=hostInfo, common=common, remoteHost=remoteHost, eventDesc=eventDesc, users=users, userLoginName=userLoginName, logout=logout)
