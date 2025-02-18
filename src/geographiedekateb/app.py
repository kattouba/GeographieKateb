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
        # Charger les données
        self.data = self.load_data()
        self.current_entry = None
        self.score = 0
        self.question_count = 0
        self.show_info_screen = False  # Flag pour contrôler l'interface active

        # Conteneurs principaux
        self.main_box = self.create_main_box()
        self.info_box = self.create_info_box()

        # Ajouter le conteneur principal initialement
        self.main_window = toga.MainWindow(title="Géographie de Kateb")
        self.main_window.content = self.main_box
        self.main_window.show()

        # Initialiser le SoundPool pour les sons
        self.sound_pool = SoundPool.Builder().setMaxStreams(1).build()
        self.correct_sound = self.sound_pool.load(join(dirname(__file__), "resources/correct.mp3"), 1)
        self.wrong_sound = self.sound_pool.load(join(dirname(__file__), "resources/wrong.mp3"), 1)

        # Lancer la première question
        self.show_flag_question()

    def create_main_box(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        self.flag_label = toga.ImageView(style=Pack(height=200, alignment=CENTER, padding=(0, 5)))
        self.result_label = toga.Label("", style=Pack(padding=(0, 5), text_align=CENTER))
        main_box.add(self.flag_label)
        main_box.add(self.result_label)

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

    def load_data(self):
        data = []
        with open(join(dirname(__file__), "resources/countries_data.txt"), "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) >= 5:
                    data.append({
                        "flag": parts[0],
                        "map": parts[1],
                        "country": parts[2],
                        "capital": parts[3],
                        "info": parts[4]
                    })
        return data

    def play_sound(self, correct=True):
        if correct:
            self.sound_pool.play(self.correct_sound, 1.0, 1.0, 1, 0, 1.0)
        else:
            self.sound_pool.play(self.wrong_sound, 1.0, 1.0, 1, 0, 1.0)

    def show_flag_question(self, widget=None):
        if self.question_count >= 10:
            self.main_window.info_dialog(
                "Quiz terminé", f"Votre score final est de {self.score}/20 !"
            )
            self.exit()
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


def main():
    return GeographieDeKateb()
