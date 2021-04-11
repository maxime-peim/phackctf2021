# WE-2 (Zipline)

## Sujet :

> Deux semaines avant le CTF, vous avez eu accès à un amuse bouche.
>
> On vient de trouver ce fichier sur une clé USB sur le trottoir en face de chez @lulu.
> On pense qu'il y a des infos intéressantes dessus. On vous laisse regarder ! :eyes:

Tags : `starting` `compress` `easy`

## Solution :

C'est une suite de fichiers compressés.
Soit on le fait à la main, soit un code un petit truc en python pour aller plus vite, et qui teste les mots de passe de la liste qu'on nous fourni lorsqu'il y en a besoin.
On affichant les noms des archives qu'on extrait, on se rend compte que les dernières donnent un flag.

`PHACK{R3ady_4_a_z1pl1n3_r1d3}`