# Importer Flask
from flask import Flask, render_template, request
from random import choice
import os 
reponse_possible = ["Essaye plus tard"]
"Essaye plus tard",
"Essaye encore",
"Pas d'avis",
"C'est ton destin",
"Le sort en est jeté",
"Une chance sur deux",
"Repose ta question",
"Les réponses affirmatives",
"D'après moi oui",
"C'est certain",
"Oui absolument",
"Tu peux compter dessus",
"Sans aucun doute",
"Très probable",
"Oui",
"C'est bien parti",
"Les réponses négatives",
"C'est non",
"Peu probable",
"Faut pas rêver",
"N'y compte pas",
"Impossible",

# Création de l'application = instance de la classe Flask
app = Flask(__name__)

#On crée le premier route a la racine : à la racine de notre application "/"
# @app.route() : ce décodeur permet d'associer une URL à une fonction
# root -> page racine de l'app web
@app.route("/", methods=["GET", "POST"])
def index():
    # crée variable reponse
    reponse = 0
    # on vérifie si l'utilisateur accède à la page d'acceuil ou valide le bouton
    if request.method == "POST":
        # on génère une réponse aléatoire parmi les réponses possibles
        reponse = choice(reponse_possible)
    return render_template("index.html", reponse = reponse)








##########################################################
#                   TOUJOURS A LA FIN                    #
##########################################################
# Toujours tout en bas de votre fichier main.py
# Executer l'application
# port 81 = le port sur lequel le serveur Flask écoute
app.run(host = '0.0.0.0', port = 81)



