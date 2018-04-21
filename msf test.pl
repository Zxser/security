require 'msf/core'
class Metasploit 3 < Msf::Auxiliary
    include Msf::Exploit::Remote::Tcp
    include Msf::Auxiliary::Scanner
    def initialize
            super(
                        'Name'   =>'My custom TCP scan',
                        'Version'      =>'$Revision: 1 $',
                        'Description'   =>'My quick scanner',
                        'Author'          =>'Your name here',
                        'License'          =>MSF_LICENSE
            )
        register_options(
                    [
                            Opt::Rport(12345)
                    ],self.class)
    end

    df run_host(ip)
    connect()
    sock.puts('hello world')
    data=sock.recv(1024)
    print_status("Received:#{data} from #{ip}")
    disconnect()
            end
end