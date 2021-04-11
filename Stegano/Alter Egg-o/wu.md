# Alter Egg-o

## Sujet :

> L'agent Smith de la HSA (Hack Secret Agency) a retiré trop rapidement la clé USB de son PC (ce n00b !!). La preuve qu'il voulait vous montrer semble corrompue.
>
> Montrer lui que vous pouvez lui sauver la mise et récupérer ce fichier.

Tags : `stegano` `magic` `medium`

## Solution :

En ouvrant le fichier dans un éditeur hexadécimal, on remarque que les premiers octets ne correspondent pas à la signature d'un PNG.

On remplace donc les octets DEADBEEF par 80504E47, et on a une image non corrompue !

`PHACK{ju5t_ch4ng3d_a_m4gic_nUmb3R_i5_i7_b4d?}`