# application imports
from cli.decorators import keyboard_interruptible
from cli.mixins import CLIMixin
from views.prompts import InvalidResponseException


class BaseView(CLIMixin):

    def __init__(self, router):
        self.active = False
        self.router = router

    @keyboard_interruptible
    def run(self):
        """
        Main method that will display the text UI and respond to user input.
        """
        self.active = True
        self.display_header()
        menu = self.get_menu_prompt()

        while self.is_active():
            try:
                response = menu.ask().parse()
                self.process_menu_selection(response)
            except InvalidResponseException as e:
                menu.invalid_response(e.message)

    def stop(self):
        """
        Stops the execution of this view.
        """
        self.active = False

    def is_active(self):
        """
        Determines if a view is active.
        """
        return self.active

    def display_header(self):
        """
        Outputs the view's header.
        """
        self.output.header(self.get_header())

    def get_header(self):
        """
        Returns a header string for the view.
        """
        raise NotImplementedError

    def get_menu_prompt(self):
        """
        Returns a MenuPrompt object for displaying a menu and parsing the user's selection.
        """
        raise NotImplementedError

    def process_menu_selection(self, response):
        """
        Processes the user's selection for this view's menu prompt.
        """
        raise NotImplementedError