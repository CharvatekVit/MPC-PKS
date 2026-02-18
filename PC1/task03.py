import struct
import socket
import time
#adresa a port prijemce (zada vyucujici)
host = "147.229.150.222"
port = 50000
#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#zaslani zpravy
for i in range(5):
    data = struct.pack("!LLL", i, 246850, 21)
    n = udp_socket.sendto(data,(host, port))     
    print("Odeslano {} byte\n".format(n))
    try:
        data, address = udp_socket.recvfrom(512)
        Rseq, Rn1, Rn2 = struct.unpack("!LLL", data)
    except TimeoutError:
        print("No response from server")
    except struct.error:
        print("Unable to unpack packet from {}".format(address))
    else:
        file = "udp.log"
        log = "Received: a={}, p={}, s={}, n1={}, n2 ={}".format(*address, Rseq, Rn1, Rn2)
        print(log)
        fo = open(file, "a") #soubor otevřít v řežimu “append”
        fo.write(log + "\n") #přidat znak nového řádku
        fo.close
        time.sleep(0.5)


#uzavreni socketu
udp_socket.close()