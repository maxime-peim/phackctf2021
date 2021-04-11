# Système de nom de domaine

## Sujet :

> Votre équipe est sur le point de résoudre un nouveau challenge mais le nom de domaine flag.phack.fr ne semble pas fonctionner.
> Une analyse plus poussée est peut-être nécessaire.

Tags : `network` `dns` `easy`

## Solution :
On utilise `dig` pour récupérer tous les records associés au nom de domaine :

```
$ dig flag.phack.fr @12.42.0.53 ANY
...
flag.phack.fr.          3599    IN      TXT     "PHACK{diG_i7_4nD_f0uNd_i7_In_y0uR_dNs}"
...
```

`PHACK{diG_i7_4nD_f0uNd_i7_In_y0uR_dNs}`