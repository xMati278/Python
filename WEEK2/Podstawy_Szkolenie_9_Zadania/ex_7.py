import datetime


class Note:
    def __init__(self, author_, content_):
        self.author = author_
        self.content = content_
        self.note_time = datetime.datetime.now()

    def __str__(self):
        return f"Author: {self.author}, Content: {self.content}, Time: {self.note_time}"


class Notebook:

    def __init__(self):
        self.notebook_list = []

    def add_new_note(self, note):
        self.notebook_list.append(note)

    def display_notes(self):
        for note in self.notebook_list:
            print(note)

    def display_amount_of_notes(self):
        print(f'Number of notes: {len(self.notebook_list)}')


def main():
    note = Note("Janek", "Bardzo ważna notatka!")
    nb = Notebook()
    nb.add_new_note(note)
    nb.display_notes()
    nb.display_amount_of_notes()


if __name__ == "__main__":
    main()
