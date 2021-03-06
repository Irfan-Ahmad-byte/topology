'''
this script will create a custom topology from mininet
'''

"""
topology: 2 hosts, 3 switches straight link 
"""

from mininet.topo import Topo

class cusTopo(Topo):
	'''a simple topology'''
	
	def __init__(self):
		Topo.__init__(self)
		
		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')
		host4 = self.addHost('h4')
		host5 = self.addHost('h5')
		host6 = self.addHost('h6')
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		
		'''create links'''
		self.addLink(host1, switch1)
		self.addLink(switch1, switch2)
		self.addLink(switch2, host2)
		self.addLink(host2, host3)
		self.addLink(host3, host4)
		self.addLink(host4, host5)
		self.addLink(host1, host4)
		self.addLink(host5, host6)
		self.addLink(host3, host6)


topos = {'cusTopo': ( lambda: cusTopo() )}
