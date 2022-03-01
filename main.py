
#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sipfullproxy as sip_proxy


if __name__ == "__main__":
    sip_proxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=sip_proxy.logging.INFO,
                                  datefmt='%H:%M:%S')
    sip_proxy.logging.info(sip_proxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sip_proxy.time.localtime()))
    sip_proxy.hostname = sip_proxy.socket.gethostname()
    sip_proxy.logging.info(sip_proxy.hostname)

    sip_proxy.ipaddress = sip_proxy.socket.gethostbyname(sip_proxy.hostname)

    if sip_proxy.ipaddress == "127.0.0.1":
        sip_proxy.ipaddress = sip_proxy.sys.argv[1]
    sip_proxy.logging.info(sip_proxy.ipaddress)

    sip_proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sip_proxy.ipaddress, sip_proxy.PORT)
    sip_proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sip_proxy.ipaddress, sip_proxy.PORT)
    server = sip_proxy.SocketServer.UDPServer((sip_proxy.HOST, sip_proxy.PORT), sip_proxy.UDPHandler)
    print(sip_proxy.ipaddress)
    server.serve_forever()
