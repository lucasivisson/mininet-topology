from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf, OVSLink
from subprocess import call


def myNetwork():
    info('*** Clearing existing interfaces\n')
    call(['mn', '-c'])

    net = Mininet(topo=None,
                  build=False,
                  link=OVSLink,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='172.17.0.2',
                           protocol='tcp',
                           port=6633)

    info('*** Add hosts\n')
    sao_luis = net.addHost('h1', cls=Host,
                           ip='10.0.0.1', defaultRoute=None)
    fortaleza = net.addHost('h2', cls=Host,
                            ip='10.0.0.2', defaultRoute=None)
    teresina = net.addHost('h3', cls=Host,
                           ip='10.0.0.3', defaultRoute=None)
    natal = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    joao_pessoa = net.addHost('h5', cls=Host,
                              ip='10.0.0.5', defaultRoute=None)
    campina_grande = net.addHost(
        'h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    recife = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    maceio = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    aracaju = net.addHost('h9', cls=Host,
                          ip='10.0.0.9', defaultRoute=None)
    salvador = net.addHost('h10', cls=Host,
                           ip='10.0.0.10', defaultRoute=None)

    info('*** Add switches\n')
    sw_sao_luis = net.addSwitch(
        's1', cls=OVSKernelSwitch, dpid='00:00:00:00:00:01', protocols=["OpenFlow10"])
    sw_fortaleza = net.addSwitch('s2', cls=OVSKernelSwitch,
                                 dpid='00:00:00:00:00:02', protocols=["OpenFlow10"])
    sw_teresina = net.addSwitch('s3', cls=OVSKernelSwitch,
                                dpid='00:00:00:00:00:03', protocols=["OpenFlow10"])
    sw_natal = net.addSwitch(
        's4', cls=OVSKernelSwitch, dpid='00:00:00:00:00:04',  protocols=["OpenFlow10"])
    sw_joao_pessoa = net.addSwitch('s5', cls=OVSKernelSwitch,
                                   dpid='00:00:00:00:00:05', protocols=["OpenFlow10"])
    sw_campina_grande = net.addSwitch('s6', cls=OVSKernelSwitch,
                                      dpid='00:00:00:00:00:06', protocols=["OpenFlow10"])
    sw_recife = net.addSwitch(
        's7', cls=OVSKernelSwitch, dpid='00:00:00:00:00:07', protocols=["OpenFlow10"])
    sw_maceio = net.addSwitch('s8', cls=OVSKernelSwitch,
                              dpid='00:00:00:00:00:08', protocols=["OpenFlow10"])
    sw_aracaju = net.addSwitch('s9', cls=OVSKernelSwitch,
                               dpid='00:00:00:00:00:09', protocols=["OpenFlow10"])
    sw_salvador = net.addSwitch('s10', cls=OVSKernelSwitch,
                                dpid='00:00:00:00:00:10', protocols=["OpenFlow10"])

    info('*** Add links to switches\n')
    net.addLink(sw_sao_luis, sw_fortaleza, bw=100)
    net.addLink(sw_fortaleza, sw_natal, bw=100)
    net.addLink(sw_fortaleza, sw_salvador, bw=100)
    net.addLink(sw_fortaleza, sw_teresina, bw=100)
    net.addLink(sw_natal, sw_campina_grande, bw=100)
    net.addLink(sw_joao_pessoa, sw_campina_grande, bw=10)
    net.addLink(sw_joao_pessoa, sw_recife, bw=10)
    net.addLink(sw_campina_grande, sw_recife, bw=100)
    net.addLink(sw_recife, sw_maceio, bw=100)
    net.addLink(sw_campina_grande, sw_salvador, bw=40)
    net.addLink(sw_maceio, sw_aracaju, bw=100)
    net.addLink(sw_aracaju, sw_salvador, bw=100)

    info('*** Add links to hosts\n')
    net.addLink(sw_fortaleza, fortaleza)
    net.addLink(sw_salvador, sao_luis)
    net.addLink(sw_teresina, teresina)
    net.addLink(sw_natal, natal)
    net.addLink(sw_salvador, salvador)
    net.addLink(sw_campina_grande, campina_grande)
    net.addLink(sw_joao_pessoa, joao_pessoa)
    net.addLink(sw_recife, recife)
    net.addLink(sw_maceio, maceio)
    net.addLink(sw_salvador, salvador)
    net.addLink(sw_aracaju, aracaju)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
