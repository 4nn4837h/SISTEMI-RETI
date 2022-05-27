#---------------------------------------------------------------------------------------------------------------------------------codice del client
# importazione librerie necessarie
import socket, threading, queue, serial

q = queue.Queue()

class Read_Microbit(threading.Thread):
    """classe thread per la lettura dei dati ricevuti da microbit"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
      
    def terminate(self):
        self.running = False
        
    def run(self):
        port = "COM32"
        s = serial.Serial(port)             #porta seriale del microbit
        s.baudrate = 115200
        while self.running:
            data = s.readline().decode()    # lettura dati dalla porta seriale
            q.put(data)                     # inserimento dei dati nella coda
        
def main():
    rm = Read_Microbit()                                    # thread per la continua ricezione dei dati
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # creazione del socket con indirizzo ipv4 e protocollo TCP
    rm.start()                                              # inizio ricezione dei dati da micro bit
    s.connect(("192.168.88.87", 8000))                      # connessione al server centrale 
    while True:
        dati = str(q.get())                                 # conversione in stringa i dati 
        s.sendall(dati.encode())                            # invio dati al server

if __name__ == "__main__":
    main()