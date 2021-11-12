#! python3
import logging
logging.basicConfig(filename='ucheLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('Start of program Yeah!')

def factorial(n):
    logging.debug('Start of my program lolz(%s)' %(n))
    total = 1
    for i in range (1,n+1):
        total *=i
        logging.debug('i is '+ str(i) + ', total is '+str(total) + ' Lolz there is definitely something fishy with this code ')
    logging.debug('End of factorial(%s)' %(n))
    print(total)
    return total
    
(factorial(5))
logging.debug('This is where the program ends')