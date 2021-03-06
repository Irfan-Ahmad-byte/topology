from mininet.net import Mininet
import networkx as nx

def construct_mininet_from_networkx(graph, host_range):
    """ Builds the mininet from a networkx graph.

    :param graph: The networkx graph describing the network
    :param host_range: All switch indices on which to attach a single host as integers
    :return: net: the constructed 'Mininet' object
    """

    net = Mininet()
    # Construct mininet
    for n in graph.nodes:
        net.addSwitch("s_%s" % n)
        # Add single host on designated switches
        if int(n) in host_range:
            net.addHost("h%s" % n)
            # directly add the link between hosts and their gateways
            net.addLink("s_%s" % n, "h%s" % n)
    # Connect your switches to each other as defined in networkx graph
    for (n1, n2) in graph.edges:
        net.addLink('s_%s' % n1,'s_%s' % n2)
    return net

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge('c1', 'h1')
    G.add_edge('c1', 'h1')
    G.add_edge('c1', 'h2')
    G.add_edge('h2', 's1')
    G.add_edge('h2', 's2')
    G.add_edge('h1', 's1')
    G.add_edge('h1', 's3')
    G.add_edge('s2', 's3')
    nx.draw_planar(G, with_labels=True)
    
    construct_mininet_from_networkx(G, 2)
