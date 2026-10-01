from py_ecc.secp256k1 import secp256k1
import secrets
import hashlib
import random
from datetime import datetime

def assinatura(sk,message):
    seed = int(datetime.now().timestamp())
    random.seed(seed)
    alpha = random.getrandbits(250)
    alphaG = secp256k1.multiply(secp256k1.G,alpha)
    temp = hashlib.sha256()
    temp.update(message.encode("UTF-8"))
    temp.update(str(alphaG).encode("UTF-8"))
    c= temp.hexdigest()
    r = (alpha-int(c,16)*sk) % secp256k1.N
    return (int(c,16),r)

def assina_exercicio():
    m1 = "Mensagem 1"
    m2 = "Mensagem 2"
    sk = secrets.randbits(256)
    print(datetime.now())
    # Gasta um tempo...
    (c1,r1) = assinatura(sk,m1)
    print("c1=",c1)
    print("r1=",r1)
    # Gasta um tempo...
    (c2,r2) = assinatura(sk,m2)
    print("c2=",c2)
    print("r2=",r2)

# r1 = alfa1 - c1 * sk
# r2 = alfa2 - c2 * sk
# sk1 = (alfa1 - r1) / c1 
# sk2 = (alfa2 - r2) / c2
# sk1 = sk2
#2026-09-23 23:26:33.944888
#c1= 17574914162398755519845112831929872204794539148722560696530206738132537352309
#r1= 63702942183361152324349542819753229638304952016842535130701509206274961205200
#c2= 114394360644184457979898691066605911217074940116193361021583715765885654775545
#r2= 9307637531528717922211193650645999199252047737686460977332255290062646194943

c1= 17574914162398755519845112831929872204794539148722560696530206738132537352309
r1= 63702942183361152324349542819753229638304952016842535130701509206274961205200
c2= 114394360644184457979898691066605911217074940116193361021583715765885654775545
r2= 9307637531528717922211193650645999199252047737686460977332255290062646194943

dt = datetime.strptime(
    "2026-09-23 23:26:33",
    "%Y-%m-%d %H:%M:%S"
)
timestamp = int(dt.timestamp())

for seed1 in range(timestamp - 10, timestamp + 11):
    random.seed(seed1)
    alpha1 = random.getrandbits(250)
    for seed2 in range(seed1, timestamp + 11):
        random.seed(seed2)
        alpha2 = random.getrandbits(250)
        sk1 = ((alpha1 - r1) * pow(c1, -1, secp256k1.N)) % secp256k1.N
        sk2 = ((alpha2 - r2) * pow(c2, -1, secp256k1.N)) % secp256k1.N

        if sk1 == sk2:
            print("Sk encontrado!")
            print("SK: ", sk1)