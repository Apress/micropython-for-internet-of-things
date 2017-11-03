# connect/ show IP config a specific network interface
import network
import pyb

def test_connect():
    nic = network.CC3K(pyb.SPI(2), pyb.Pin.board.Y5, pyb.Pin.board.Y4, pyb.Pin.board.Y3)
    nic.connect('YOUR_ROUTER_HERE', 'YOUR_ROUTER_PASSWORD_HERE')
    while not nic.isconnected():
        pyb.delay(50)
    print(nic.ifconfig())
    
    # now use usocket as usual
    import usocket as socket
    addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
    data = s.recv(1000)
    print(data)
    s.close()