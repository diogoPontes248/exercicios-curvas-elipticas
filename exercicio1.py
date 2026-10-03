#Exercício 1)
#Uma determinada Hardware Wallet usa um código similar a este no momento
#de gerar a PK:
#
#from py_ecc.secp256k1 import secp256k1
#import hashlib
#import random
#from datetime import datetime
#seed = int(datetime.now().timestamp())
#random.seed(seed)
#sk = random.getrandbits(250)
#pk = secp256k1.multiply(secp256k1.G,sk)
#print(pk)
#
#Considerando a seguinte chave pública:
#(109406275515507847258077495698865554479234815675118879924707993547930533500352,
#40753420948420416814450900739928784816122565151273253896471439870288961392299)
#Determine a SK sabendo que o código foi executado antes do dia 24/09/2026.

from py_ecc.secp256k1 import secp256k1
import hashlib
import random
from datetime import datetime

pkAlvo = (109406275515507847258077495698865554479234815675118879924707993547930533500352, 40753420948420416814450900739928784816122565151273253896471439870288961392299)

#Como sabemos que o alvo fez a pk antes do dia 24, 
#vamos analisar todas as seeds possíveis anteriores ao dia 24 até encontrarmos a seed geradora da pk do alvo
dt = datetime.strptime(
    "2026-09-23 23:59:59",
    "%Y-%m-%d %H:%M:%S"
)
timestamp = int(dt.timestamp())
seed = timestamp

#A cada iteração, a semente é modificada para um segundo anterior
for i in range(1000000):
    random.seed(seed)
    sk = random.getrandbits(250)
    pkteste = secp256k1.multiply(secp256k1.G, sk)

    if pkteste == pkAlvo:
        print("SK: ", sk)
        print("PK alvo: ", pkAlvo)
        print("PK teste: ", pkteste)
        break;

    seed -= 1
