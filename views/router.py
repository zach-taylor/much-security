# system imports
import sys

# application imports
from cli.mixins import CLIMixin


class Router(CLIMixin):

    def __init__(self):
        self.view_stack = []

    def goto(self, view_cls):
        """
        Navigate to the given view. Note that this method does not
        stop the execution of the current view before running the
        given view, which is intended. This preserves history such
        that terminating execution of an active view will then
        naturally return execution to the previously active view.
        """
        view = view_cls(self)
        self.view_stack.append(view)
        self.output.clear()
        view.run()

    def back(self):
        """
        Stops the execution of the current view. This will return
        execution to the previously active view. If there is no
        previously active view, the application will exit.
        """
        if not self.view_stack:
            return

        self.view_stack.pop().stop()

        if not self.view_stack:
            self.exit()
            return

        self.output.clear()
        self.get_current_view().display_header()

    def get_current_view(self):
        if not self.view_stack:
            return None
        return self.view_stack[len(self.view_stack)-1]

    @staticmethod
    def exit():
        """
        Exits the application.
        """
        sys.exit()