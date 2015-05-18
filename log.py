def tolog(texto):
    with open("log.txt","a") as log:
        log.write(texto)
        log.close()
        
def logreset():
    open('log.txt', 'w').close()