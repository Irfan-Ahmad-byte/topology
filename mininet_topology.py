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
		
		startHost = self.addHost('h1')
		endHost = self.addHost('h2')
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		
		'''create links'''
		self.addLink(startHost, switch1)
		self.addLink(switch1, switch2)
		self.addLink(switch2, switch3)
		self.addLink(switch3, endHost)
		
topos = {'cusTopo': ( lambda: cusTopo() )}
