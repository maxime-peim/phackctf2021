from pyunpack import Archive
from zipfile import ZipFile
import sys
import os
import shutil

argv = sys.argv
n = 0
# on va utiliser deux dossiers pour alternativement placer le fichier décompresser 
# dans l'un puis dans l'autre
# le fichier initial doit être placé dans previous/
folders = ["previous/", "next/"]
zFilep = folders[0] + str(argv[1])
dictionary_attack = str(argv[2])

def Cracker():
    attempts = 0
    flag = 0

    print("zip file: %s" % zFilep)

    try:
        Archive(zFilep).extractall(folders[n])
    except Exception:
        pass
    else:
        return True

    print("PASSWORD")
    with open(dictionary_attack, 'r') as attack:
        for line in attack:
            try:
                passwd = line.strip('\n')
                ZipFile(zFilep).extractall(path=folders[n],pwd=str.encode(passwd))
            except Exception:
                attempts += 1
                pass
            else:
                flag = 1
                break
        return flag != 0

def extract_next():
    global zFilep
    global n

    n += 1
    n %= 2

    # on retire les fichiers présents dans le dossier dans lequel on va écrire
    for root, dirs, files in os.walk(folders[n], topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    if not Cracker():
        print("oups")

    nexts = os.listdir(folders[n])
    print(nexts)

    next = 0
    if len(nexts) > 1:
        print(nexts)
        next = int(input())

    zFilep = folders[n] + nexts[next]

if __name__ == "__main__":
    while True:
        extract_next()