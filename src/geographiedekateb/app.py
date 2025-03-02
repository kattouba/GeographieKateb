import http.client
import json
from os.path import dirname, join
import random
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from android.media import AudioManager, SoundPool
from html.parser import HTMLParser

class InfoHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data + "\n"

class GeographieDeKateb(toga.App):
    def startup(self):
        # Initialiser la fenêtre principale
        self.main_window = toga.MainWindow(title="Géographie de Kateb")

        # Créer l'interface pour demander le nom du joueur
        self.create_name_input_interface()

        # Afficher la fenêtre principale
        self.main_window.show()

    def create_name_input_interface(self):
        # Créer un champ de saisie pour le nom du joueur
        self.name_input = toga.TextInput(placeholder="Entrez votre nom", style=Pack(flex=1, padding=5))

        # Créer un bouton pour valider le nom
        self.name_button = toga.Button("Valider", on_press=self.on_name_submit, style=Pack(padding=5))

        # Créer un conteneur pour le champ de saisie et le bouton
        name_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        name_box.add(self.name_input)
        name_box.add(self.name_button)

        # Ajouter le conteneur à la fenêtre principale
        self.main_window.content = name_box

    def on_name_submit(self, widget):
        # Récupérer le nom du joueur
        self.player_name = self.name_input.value
        if not self.player_name:
            self.player_name = "Joueur"  # Nom par défaut si aucun nom n'est entré

        # Afficher l'interface de sélection du continent
        self.create_continent_selection_interface()

    def create_continent_selection_interface(self):
        # Créer une interface pour sélectionner le continent
        continent_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Titre
        title_label = toga.Label("Choisissez un continent ou le monde entier :", style=Pack(padding=(0, 5), text_align=CENTER))
        continent_box.add(title_label)

        # Boutons pour les continents
        continents = ["Afrique", "Amérique", "Asie", "Europe", "Océanie", "Monde entier"]
        for continent in continents:
            button = toga.Button(continent, on_press=self.on_continent_select, style=Pack(padding=5, flex=1))
            continent_box.add(button)

        # Ajouter le conteneur à la fenêtre principale
        self.main_window.content = continent_box

    def on_continent_select(self, widget):
        # Récupérer le continent sélectionné
        self.selected_continent = widget.text

        # Démarrer le jeu après avoir sélectionné le continent
        self.start_game()

    def start_game(self):
        # Charger les données
        self.data = self.load_data()

        # Filtrer les données en fonction du continent sélectionné
        if self.selected_continent != "Monde entier":
            self.data = [entry for entry in self.data if entry.get("continent") == self.selected_continent]

        self.current_entry = None
        self.score = 0
        self.question_count = 0
        self.show_info_screen = False  # Flag pour contrôler l'interface active

        # Conteneurs principaux
        self.main_box = self.create_main_box()
        self.info_box = self.create_info_box()

        # Ajouter le conteneur principal à la fenêtre
        self.main_window.content = self.main_box

        # Initialiser le SoundPool pour les sons
        self.sound_pool = SoundPool.Builder().setMaxStreams(1).build()
        self.correct_sound = self.sound_pool.load(join(dirname(__file__), "resources/correct.mp3"), 1)
        self.wrong_sound = self.sound_pool.load(join(dirname(__file__), "resources/wrong.mp3"), 1)

        # Lancer la première question
        self.show_flag_question()

    def create_main_box(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Créer une Box pour contenir le drapeau
        flag_box = toga.Box(style=Pack(
            height=200,  # Hauteur fixe pour la Box
            width=300,   # Largeur fixe pour la Box
            alignment=CENTER,  # Centrer le contenu
            padding=(0, 5),
        ))

        # Ajouter l'image du drapeau à la Box
        self.flag_label = toga.ImageView(style=Pack(
            flex=1,  # Remplir l'espace disponible dans la Box
            width=300,  # Largeur maximale du drapeau
            height=200,  # Hauteur maximale du drapeau
        ))
        flag_box.add(self.flag_label)

        # Ajouter la Box du drapeau à la Box principale
        main_box.add(flag_box)

        # Ajouter le label pour les résultats
        self.result_label = toga.Label("", style=Pack(padding=(0, 5), text_align=CENTER))
        main_box.add(self.result_label)

        # Ajouter les boutons pour les options
        self.buttons = []
        for _ in range(4):
            button = toga.Button("Option", on_press=self.check_country_answer, style=Pack(padding=5, flex=1))
            self.buttons.append(button)
            main_box.add(button)

        return main_box

    def create_info_box(self):
        info_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        self.map_view = toga.ImageView(style=Pack(height=200, alignment=CENTER, padding=(0, 5)))
        self.info_label = toga.MultilineTextInput(readonly=True, style=Pack(padding=10, flex=1))
        self.next_button = toga.Button("Question suivante", on_press=self.show_flag_question, style=Pack(padding=5))
        info_box.add(self.map_view)
        info_box.add(self.info_label)
        info_box.add(self.next_button)

        return info_box

    def create_end_game_interface(self):
        # Créer une nouvelle interface pour la fin du jeu
        end_game_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Afficher le score final
        score_label = toga.Label(f"Quiz terminé ! Votre score final est de {self.score}/20.", style=Pack(padding=(0, 5), text_align=CENTER))
        end_game_box.add(score_label)

        # Bouton pour afficher le classement (fusionné)
        show_leaderboard_button = toga.Button("Afficher le classement", on_press=self.send_score_and_show_leaderboard, style=Pack(padding=5))
        end_game_box.add(show_leaderboard_button)

        # Bouton pour rejouer
        replay_button = toga.Button("Rejouer", on_press=self.restart_game, style=Pack(padding=5))
        end_game_box.add(replay_button)

        return end_game_box

    def restart_game(self, widget):
        # Revenir à l'écran de saisie du nom
        self.create_name_input_interface()
        self.main_window.content = self.create_name_input_interface()

    def load_data(self):
        data = []
        with open(join(dirname(__file__), "resources/countries_data.txt"), "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) >= 6:  # Assurez-vous que le fichier contient le continent
                    data.append({
                        "flag": parts[0],
                        "map": parts[1],
                        "country": parts[2],
                        "capital": parts[3],
                        "continent": parts[4],  # Ajout du continent
                        "info": parts[5]
                    })
        return data

    def play_sound(self, correct=True):
        if correct:
            self.sound_pool.play(self.correct_sound, 1.0, 1.0, 1, 0, 1.0)
        else:
            self.sound_pool.play(self.wrong_sound, 1.0, 1.0, 1, 0, 1.0)

    def show_flag_question(self, widget=None):
        if self.question_count >= 10:
            # Basculer vers l'interface de fin de jeu
            end_game_box = self.create_end_game_interface()
            self.main_window.content = end_game_box
            return

        self.question_count += 1
        self.current_entry = random.choice(self.data)

        # Mettre à jour l'affichage principal
        flag_path = join(dirname(__file__), "resources/flags", self.current_entry["flag"])
        self.flag_label.image = flag_path
        self.result_label.text = "Choisissez le pays correspondant au drapeau."

        # Configurer les options
        options = [self.current_entry["country"]] + random.sample(
            [entry["country"] for entry in self.data if entry["country"] != self.current_entry["country"]], 3
        )
        random.shuffle(options)

        for button, option in zip(self.buttons, options):
            button.text = option
            button.on_press = self.check_country_answer
            button.enabled = True

        self.main_window.content = self.main_box

    def check_country_answer(self, widget):
        if widget.text == self.current_entry["country"]:
            self.score += 1
            self.play_sound(correct=True)
            self.result_label.text = "Bonne réponse ! Choisissez la capitale."

            # Configurer les options pour les capitales
            correct_capital = self.current_entry["capital"]
            options = [correct_capital] + random.sample(
                [entry["capital"] for entry in self.data if entry["capital"] != correct_capital], 3
            )
            random.shuffle(options)

            for button, option in zip(self.buttons, options):
                button.text = option
                button.on_press = self.check_capital_answer
                button.enabled = True
        else:
            self.play_sound(correct=False)
            self.result_label.text = f"Mauvaise réponse. Le bon pays était {self.current_entry['country']}."
            self.show_info()

    def check_capital_answer(self, widget):
        if widget.text == self.current_entry["capital"]:
            self.score += 1
            self.play_sound(correct=True)
            self.result_label.text = "Bonne réponse pour la capitale !"
        else:
            self.play_sound(correct=False)
            self.result_label.text = f"Mauvaise réponse. La bonne capitale était {self.current_entry['capital']}."

        self.show_info()

    def show_info(self):
        # Charger la carte
        map_path = join(dirname(__file__), "resources/maps", self.current_entry["map"])
        self.map_view.image = map_path if os.path.exists(map_path) else None

        # Charger les informations et retirer les balises HTML
        info_path = join(dirname(__file__), "resources/info_restcountries", self.current_entry["info"])
        if os.path.exists(info_path):
            with open(info_path, "r", encoding="utf-8") as file:
                html_content = file.read()
            parser = InfoHTMLParser()
            parser.feed(html_content)
            self.info_label.value = parser.text.strip()
        else:
            self.info_label.value = "Aucune information disponible."

        self.main_window.content = self.info_box

    def send_score_and_show_leaderboard(self, widget):
        """
        Envoie le score du joueur, puis récupère et affiche le classement.
        """
        # Connexion au serveur
        conn = http.client.HTTPConnection("studiokatebetpapa.mooo.com")

        # Données à envoyer
        data = {
            "name": self.player_name,
            "score": self.score
        }
        data_json = json.dumps(data).encode('utf-8')

        # En-têtes
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'  # En-tête pour indiquer une requête AJAX
        }

        # Envoyer la requête POST pour ajouter le score
        try:
            conn.request("POST", "/Geographie/api/add_score.php", body=data_json, headers=headers)
            response = conn.getresponse()
            response_data = response.read().decode('utf-8')
            print("Réponse de l'API (ajout du score) :", response_data)

            # Récupérer le classement après avoir envoyé le score
            conn.request("GET", "/Geographie/api/get_scores.php", headers=headers)
            response = conn.getresponse()
            response_data = response.read().decode('utf-8')
            leaderboard = json.loads(response_data)

            # Afficher le classement dans une boîte de dialogue
            leaderboard_text = "Classement des meilleurs scores :\n"
            for i, entry in enumerate(leaderboard, start=1):
                name = entry["name"]
                score = entry["score"]
                if name == self.player_name:
                    leaderboard_text += f"{i}. {name}: {score} (Vous)\n"
                else:
                    leaderboard_text += f"{i}. {name}: {score}\n"

            self.main_window.info_dialog("Classement", leaderboard_text)
        except Exception as e:
            print("Erreur lors de l'envoi du score ou de la récupération du classement :", e)
            self.main_window.info_dialog("Erreur", f"Erreur lors de l'envoi du score ou de la récupération du classement : {e}")
        finally:
            conn.close()

def main():
    return GeographieDeKateb()
