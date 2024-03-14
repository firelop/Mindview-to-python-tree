# Mindview to python tree
Ce projet a pour but de convertir un arbre mindview en arbre python avec une représentation sous forme de liste ou de dictionnaire qui pourra directement être copié et utilisé dans un programme python.

## Installation
### Téléchargement
Vous pouvez **télécharger le fichier directement [ici](https://codeload.github.com/firelop/Mindview-to-python-tree/zip/refs/heads/main.zip)**.
Puis **décompressez** le dossier fichier dans le dossier **vide** de votre choix.

### Installation des dépendances
Pour installer les dépendances, vous pouvez utiliser **la commande suivante** dans le dossier du projet:
```bash
python3 -m pip install -r requirements.txt
```

### Configuration
Il est possible de configurer la manière dont le programme exportera l'arbre.
Par défaut l'export se faire sous forme de dictionnaire. 
Si vous souhaitez exporter sous forme de liste, ouvrez **main.py**, dans les premières lignes du fichier et modifiez la ligne:
```PYTHON
is_list_representation = False
```
par:
```PYTHON
is_list_representation = True
```

## Utilisation
### Création du projet mindview
Pour créer un projet mindview, vous pouvez utiliser le logiciel [MindView](https://www.matchware.com/mindview) qui est payant mais qui propose une version d'essai de 30 jours. Créez un projet mindview qui correspond à l'abre que vous souhaiter créer et **enregistrez le** dans le dossier du projet.

### Conversion
Pour convertir le fichier mindview en arbre python, vous pouvez utiliser la commande suivante:
```bash
python3 main.py
```
Le programme prendra alors le **premier fichier .mdvx** du dossier d'execution et le convertira dans le fichier **output.py**.
