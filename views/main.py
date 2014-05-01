# python imports
from collections import OrderedDict

# application imports
from views import BaseView
from views.building import BuildingView
from views.personnel import PersonnelView
from views.building_security import BuildingSecurityView
from views.security_analysis import SecurityAnalysisView
from views.prompts import MenuPrompt


class MainView(BaseView):
    next_views = {
        'buildings': BuildingView,
        'personnel': PersonnelView,
        'building_security': BuildingSecurityView,
        'security_analysis': SecurityAnalysisView
    }

    def __init__(self, router):
        super(MainView, self).__init__(router)

        options = OrderedDict()
        options['buildings'] = 'Manage Buildings'
        options['personnel'] = 'Manage Personnel'
        options['building_security'] = 'Manage Building Security'
        options['security_analysis'] = 'Security Analysis'
        options['exit'] = 'Exit'
        self.menu_prompt = MenuPrompt(options)

    def get_header(self):
        return 'Welcome to Much Security System'

    def get_menu_prompt(self):
        return self.menu_prompt

    def process_menu_selection(self, response):
        if response == 'exit':
            self.router.exit()

        next_view = self.next_views.get(response, False)
        if next_view:
            self.router.goto(next_view)