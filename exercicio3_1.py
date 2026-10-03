#Exercício 3.1)
#Sabendo que r = alpha - c * sk
#Sendo alpha um valor de uso único e secreto, c é o hash code da mensagem a ser assinada.

#O parâmetro alpha é de uso único, nunca deve ser revelado. Neste exercicio assumiremos 
#que por algum motivo o valor foi obtido pelo adversário. Assim, dado:
#r= 15215428533696616148478039431373436389500692627721265210089498777217667288867
#c= 77010669529568219686736112771359268396136143145059193730683690451398633016132
#alpha=1181627538534364262043658325835895088564903807539555334358958613613546510155
#Determine a sk usada na assinatura.

from py_ecc.secp256k1 import secp256k1

r = 15215428533696616148478039431373436389500692627721265210089498777217667288867

c = 77010669529568219686736112771359268396136143145059193730683690451398633016132

alpha = 1181627538534364262043658325835895088564903807539555334358958613613546510155

#c^(-1) ou 1/c
cinv = pow(c, -1, secp256k1.N)

sk = ((alpha - r) * cinv) % secp256k1.N

print("SK =", sk)

#realizando a verificação da sk encontrada:
rResultante = (alpha - c * sk) % secp256k1.N

if r == rResultante:
    print("SK correto.")
else:
    print("SK incorreto.")
