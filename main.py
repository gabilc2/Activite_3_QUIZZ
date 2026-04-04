# Importer Flask
from flask import Flask, render_template, request, session, redirect
from random import choice
import os 

from questions import questions
from resultat import nom_resultats, resultat
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

app.secret_key = os.urandom(32)
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
    session["numero_question"] = 0
    session["score"] = {"G":0, "V":0, "T":0, "P":0}
    return render_template("index.html", reponse = reponse)

@app.route("/question")
def question():
    # rendre modifiable question dnas la fonction, rendre les modofications globales
    global questions
    # On récupere le numéro de la variable qui nous indique le numéro de la question actuelle
    numero = session["numero_question"]
    # s'il reste des questions
    if numero < len(questions) :
        # On récupère l'énoncé de la question
        enonce = questions[numero]["enonce"]
        # On crée une copie du dictionnaire qui contient la question et ses réponses possibles
        symboles_et_reponses = questions[numero].copy()
        # On retire l'nonce de cette copie
        symboles_et_reponses.pop("enonce")
        # On les symboles sous forme de liste
        symboles = list(symboles_et_reponses.keys())
        # On les réponses sous forme de liste
        reponses = list(symboles_et_reponses.values())
        # On stocke les syymboles dans un cokkie pour compter correctement les scores
        session["symboles"] = symboles
        # On affiche la question via son template HTML selon les variables créées
        return render_template("question.html", enonce = enonce, reponses = reponses, symboles = symboles)
    else :
        # On trie les scores dans l'ordre décroissant
        # Pour cela on utilise une sorted() pour obtenir une liste (car ordonnée)
        score_trie = sorted(session["score"], key = session["score"].get, reverse = True)
        # On récupère le premier élèment d'une liste
        symbole_vainqueur = score_trie[0]
        # On récup le nom et la déscription associés à l'initiale du vainqueur
        nom_vainqueur = nom_resultats[symbole_vainqueur]
        description_vainqueur = resultat[symbole_vainqueur]

        # On affiche la page d'acceuil    
        return render_template("resultat.html", nom = nom_vainqueur, description = description_vainqueur)

@app.route("/reponse/<numero>")
def reponse(numero):
    # On récupère notre cookie quio stocke les symboles pour avoir le symbole associé a la réponse sélectionnée
    symbole = session["symboles"][int(numero)]
    # On incrémente le score
    session["score"][symbole] += 1
    # On passe à la question suivante
    session["numero_question"] += 1
    # On affiche la question suivante
    return redirect("/question")





##########################################################
#                   TOUJOURS A LA FIN                    #
##########################################################
# Toujours tout en bas de votre fichier main.py
# Executer l'application
# port 81 = le port sur lequel le serveur Flask écoute
app.run(host = '0.0.0.0', port = 81)



