import re
class ciscoConfParser:
  def __init__(self, obj):
    self.obj = obj
    self.parse = self.__createParserMap__()

  def __createParserMap__(self):
    parse={}
    parse['comment'] = self.comment
    parse['banner'] = self.comment
    parse['interface'] = self.interface
    parse['dns'] = self.dns
    parse['same-security-traffic'] = self.sameSecurityTraffic
    parse['object'] = self.objct
    parse['object-group'] = self.objectGroup
    parse['access-list'] = self.accessList
    parse['pager'] = self.pager
    parse['logging'] = self.logging
    parse['mtu'] = self.mtu
    parse['monitor-interface'] = self.monitorInterface
    parse['icmp'] = self.icmp
    parse['no'] = self.no
    parse['arp'] = self.arp
    parse['access-group'] = self.accessGroup
    parse['route'] = self.route
    parse['timeout'] = self.timeout
    parse['user-identity'] = self.userIdentity
    parse['aaa'] = self.aaa
    parse['crypto'] = self.crypto
    parse['telnet'] = self.telnet
    parse['ssh'] = self.ssh
    parse['username'] = self.username
    parse['class-map'] = self.classMap
    parse['policy-map'] = self.policyMap
    parse['service-policy'] = self.servicePolicy
    parse['Cryptochecksum'] = self.cryptochecksum
    return parse

  def comment(self):
    #ignore everything
    print "ignore"
    return None

  def interface(self):
    return None

  def dns(self):
    return None

  def sameSecurityTraffic(self):
    return None

  def objct(self):
    return None

  def objectGroup(self):
    return None

  def accessList(self):
    return None

  def pager(self):
    return None

  def logging(self):
    return None

  def mtu(self):
    return None

  def monitorInterface(self):
    return None

  def icmp(self):
    return None

  def no(self):
    return None

  def arp(self):
    return None

  def accessGroup(self):
    return None

  def route(self):
    return None

  def timeout(self):
    return None

  def userIdentity(self):
    return None

  def aaa(self):
    return None

  def crypto(self):
    return None

  def telnet(self):
    return None

  def ssh(self):
    return None

  def username(self):
    return None

  def classMap(self):
    return None

  def policyMap(self):
    return None

  def servicePolicy(self):
    return None

  def cryptochecksum(self):
    return None