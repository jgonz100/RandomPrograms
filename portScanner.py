import threading
import socket
import queue as q

print_lock = threading.Lock()

host = "172.18.77.97"

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            print('Port: ' + str(port) + ' is open')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

q = q.Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 1024):
    q.put(worker)

print('Scan complete')
