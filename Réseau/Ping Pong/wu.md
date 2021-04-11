# Ping Pong

## Sujet :

> Votre collegue a trouvé des traces inquiétantes en analysant le réseau de Weak'corp.
> Pouvez-vous l'aider à comprendre ce que c'est ?

Tags : `network` `ping` `easy`

## Solution :
Avec un peu la même mécanique que le challenge Thief, on a une série de paquet ICMP qui contiennent un payload de un octet chacun.

En récupérant tous les payloads, on a le flag :

`PHACK{p1n9_p0n9_p1n9_p0n9_qu1_4_d3j4_j0u3_4u_73nn15_d3_74813_?}`