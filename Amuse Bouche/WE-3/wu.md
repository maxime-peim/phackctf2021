# WE-3 (Checkmate)

## Sujet :

> Trois semaines avant le CTF, vous avez eu accès à un amuse bouche.
> Format du flag : PHACK{<md5_du_fichier_en_minuscules>}

> Le fichier à l'intérieur de l'archive a été corrompu. Mais c'est quand même un chouette souvenir, donc vous voulez absolument le récupérer.
> Le flag sera le md5sum du fichier corrigé, gardez-le précieusement d'ici le début du CTF.
> Il y a exactement 16 octets à corriger.
> Le mot de passe de l'archive est le nom d'une jolie ville de France, en minuscules.

Tags : `starting` `checkmat` `easy`

## Solution :

L'archive est protégée par un mot de passe qui est une ville de France.

On va récupérer une liste sur Internet (https://sql.sh/736-base-donnees-villes-francaises), et un petit code en python pour brute-force une archive avec des mots de passe venant d'une liste (https://github.com/igniteflow/violent-python/blob/master/pwd-crackers/zip-crack.py).

Le mot de passe est donc `briare`. On récupère donc le fichier 'corrompu', qui est en fait la description d'une partie d'échec.

La partie incomplète : 

`e4.e?.Nf3.???.d4.exd4.Nxd4.Nxd4.?xd4.Nf6.e5.Nh5.g4.f6.gxh5.fxe5.?xe5+.B??.Nc3.d6.Qe4.???.Qxf5.Rf8.Qe4.h6.Bc4.Qd7.???.c5.Re1.b6.B??.Qxb5.Qxe7#`

On joue la partie sur https://www.iechecs.com/iechecs.htm, et on trouve les mouvements manquants.

Voici une partie valide : 

`e4.e5.Nf3.Nc6.d4.exd4.Nxd4.Nxd4.Qxd4.Nf6.e5.Nh5.g4.f6.gxh5.fxe5.Qxe5+.Be7.Nc3.d6.Qe4.Bf5.Qxf5.Rf8.Qe4.h6.Bc4.Qd7.Kd1.c5.Re1.b6.Bb5.Qxb5.Qxe7#`

Et le flag : `PHACK{cb51e1b764c10a01c5983e99f3d8d386}`