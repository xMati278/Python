class Menu:
    @staticmethod
    def show():
        print("Menu:")
        print("1. Add note")
        print("2. Add card")
        print("3. Display all notes")
        print("4. Display all business cards")
        print("5. Exit")

    @staticmethod
    def get_choice():
        return int(input("Select option: "))


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class Card:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class NotesSubManager:
    notes_list = []

    @staticmethod
    def add(title, content):
        note = Note(title, content)
        NotesSubManager.notes_list.append(note)

    @staticmethod
    def show():
        print("Notes:")
        for idx, note in enumerate(NotesSubManager.notes_list, 1):
            print(f"{idx}. Title: {note.title}, Content: {note.content}")


class CardsSubManager:
    cards_list = []

    @staticmethod
    def add(name, phone_number):
        card = Card(name, phone_number)
        CardsSubManager.cards_list.append(card)

    @staticmethod
    def show():
        print("Business cards:")
        for idx, card in enumerate(CardsSubManager.cards_list, 1):
            print(f"{idx}. Name: {card.name}, Phone Number: {card.phone_number}")


class Manager:
    def __init__(self):
        self.menu = Menu()

    @staticmethod
    def show_notes():
        NotesSubManager.show()

    @staticmethod
    def show_cards():
        CardsSubManager.show()

    @staticmethod
    def add_note():
        print("Adding a new note:")
        title = input("Enter note title: ")
        content = input("Enter the content of the note: ")
        NotesSubManager.add(title, content)

    @staticmethod
    def add_card():
        print("Adding a new business card:")
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        CardsSubManager.add(name, phone_number)

    def start(self):
        while True:
            self.menu.show()
            choice = self.menu.get_choice()

            if choice == 1:
                self.add_note()

            elif choice == 2:
                self.add_card()

            elif choice == 3:
                self.show_notes()

            elif choice == 4:
                self.show_cards()

            elif choice == 5:
                print("I'm exiting the program.")
                break

            else:
                print("Invalid selection. Please try again.")


def main():
    manager = Manager()
    manager.start()


if __name__ == "__main__":
    main()
