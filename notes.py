import os
import json


class Note():
    def __init__(self, title, text):
        self.__title = title
        self.__text = text


    def get_dict(self):
        return {"title": self.__title, "text": self.__text}


    def get_title(self):
        return self.__title
    

    def get_text(self):
        return self.__text
    

    def set_title(self, title):
        self.title = title


    def set_text(self, text):
        self.title = text


class Notes_app():
    def __init__(self):
        self.__file_name = "notes"
        self.__note_list = [Note(d["title"], d["text"]) for d in self.load_notes()]


    def add_notes(self):
        note_title = input("Enter title:\n")
        note_text = input("Enter text\n")
        self.__note_list.append(Note(note_title, note_text))


    def delete_notes(self):
        index = int(input("Enter index to bo deleted:"))
        del self.__note_list[index]
        self.save_notes()


    def display_notes(self):
        for n in self.__note_list:
            print("-"*25)
            print(n.get_title())
            print(n.get_text())


    def save_notes(self):
        with open(self.__file_name + ".json", "w") as file:
            json.dump([d.get_dict() for d in self.__note_list], file, indent = 4)


    def load_notes(self):
        if os.path.isfile(self.__file_name + ".json"):
            with open(self.__file_name + ".json", "r") as file:
                return json.load(file)
        else:
            return []


new_app = Notes_app()
new_app.add_notes()
new_app.add_notes()
new_app.add_notes()
new_app.add_notes()
new_app.display_notes()
new_app.save_notes()
new_app.delete_notes()
new_app.display_notes()

new_note = Note("Download film", "Alien")
my_json = json.dumps(vars(new_note))
print(type(my_json))
#print(my_json)