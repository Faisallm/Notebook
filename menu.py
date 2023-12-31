from notebook import Note, Notebook
import sys


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        # initialize a new Notebook
        self.notebook = Notebook()

        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Notes
        5. Quit
    """)

    def run(self):
        """Display a menu and responds to choices"""

        while True:
            self.display_menu()
            choice = input("Enter a choice: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):

        if not notes:
            # this will return the list of notes
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id,
                note.tags,
                note.memo
            ))

    def search_notes(self, filter):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo")
        self.notebook.new_note(memo)
        print("Your note have been added")

    def modify_note(self):
        id = input("Enter a note id:")
        memo = input("Enter a memo:")
        tags = input("Enter tags: ")

        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()