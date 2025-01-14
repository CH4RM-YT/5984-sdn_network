from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

def custom_tree_topology():
    """Create a custom tree-based topology."""
    net = Mininet(controller=RemoteController, link=TCLink)

    # Add the Ryu controller
    ryu_controller = net.addController(
        'ryuController',
        controller=RemoteController,
        ip='192.168.233.129',  # IP address of the machine running the Ryu controller
        port=6633  # Default OpenFlow port
    )

    # Add core switch
    core_switch = net.addSwitch('switch1')

    # Add aggregation layer switches
    agg_switch1 = net.addSwitch('switch2')
    agg_switch2 = net.addSwitch('switch3')

    # Add access layer switches
    access_switch1 = net.addSwitch('switch4')
    access_switch2 = net.addSwitch('switch5')
    access_switch3 = net.addSwitch('switch6')
    access_switch4 = net.addSwitch('switch7')

    # Interconnect core and aggregation switches
    net.addLink(core_switch, agg_switch1, bw=50, delay='2ms', use_htb=True)
    net.addLink(core_switch, agg_switch2, bw=50, delay='2ms', use_htb=True)

    # Interconnect aggregation and access switches
    net.addLink(agg_switch1, access_switch1, bw=30, delay='5ms', use_htb=True)
    net.addLink(agg_switch1, access_switch2, bw=30, delay='5ms', use_htb=True)
    net.addLink(agg_switch2, access_switch3, bw=30, delay='5ms', use_htb=True)
    net.addLink(agg_switch2, access_switch4, bw=30, delay='5ms', use_htb=True)

    # Add hosts to access layer switches
    host1 = net.addHost('h1', ip='10.0.0.5/24')
    host2 = net.addHost('h2', ip='10.0.0.3/24')
    host3 = net.addHost('h3', ip='10.0.0.7/24')
    host4 = net.addHost('h4', ip='10.0.0.9/24')
    host5 = net.addHost('h5', ip='10.0.1.0/24')
    host6 = net.addHost('h6', ip='10.0.1.6/24')
    host7 = net.addHost('h7', ip='10.0.1.2/24')
    host8 = net.addHost('h8', ip='10.0.1.4/24')

    # Connect hosts to access layer switches
    net.addLink(host1, access_switch1)
    net.addLink(host2, access_switch1)
    net.addLink(host3, access_switch2)
    net.addLink(host4, access_switch2)
    net.addLink(host5, access_switch3)
    net.addLink(host6, access_switch3)
    net.addLink(host7, access_switch4)
    net.addLink(host8, access_switch4)

    # Start the network
    net.start()
    print("Custom tree-based topology is up. Use 'pingall' in the CLI to test connectivity.")

    # Test connectivity automatically
    net.pingAll()

    # Enter the Mininet CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    custom_tree_topology()
