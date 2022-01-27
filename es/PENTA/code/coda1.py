def enqueue(coda, elemento):
    coda.append(elemento)
    
def dequeue(coda):
    if len(coda) > 0: return coda.pop(0)
    else: return None

def main():
    
    cliente1 = {"nome" : "Mario Rossi", "id" : 123456}
    cliente2 = {"nome": "Johnny Depp", "id":987654}
    cliente3 = 3.1415
    coda, coda2, risp = [], [], ''
    
    enqueue(cliente1, coda)
    enqueue(cliente2, coda)
    enqueue(cliente3, coda)
    print(coda)
    
if __name__ == "__main__":
    main()
    