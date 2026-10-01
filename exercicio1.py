from py_ecc.secp256k1 import secp256k1
import hashlib
import random
from datetime import datetime

pkAlvo = (109406275515507847258077495698865554479234815675118879924707993547930533500352, 40753420948420416814450900739928784816122565151273253896471439870288961392299)

dt = datetime.strptime(
    "2026-09-23 23:59:59",
    "%Y-%m-%d %H:%M:%S"
)
timestamp = int(dt.timestamp())
seed = timestamp

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
