# python imports
from collections import OrderedDict

# application imports
from controllers.building import BuildingController
from views import BaseView
from views import prompts


class BuildingView(BaseView):
    supported_operations = [
        'create',
        'update',
        'delete'
    ]

    create_building_success_message = 'Building created.'
    create_building_error_message = 'Could not create building.'

    def __init__(self, router):
        super(BuildingView, self).__init__(router)

        # Building controller
        self.controller = BuildingController()

        # Building view menu
        menu_options = OrderedDict()
        menu_options['create'] = 'Create a new building'
        menu_options['update'] = 'Update a building'
        menu_options['delete'] = 'Delete a building'
        menu_options['back'] = '<< Back'
        self.menu_prompt = prompts.MenuPrompt(menu_options)

        # Creation prompts
        creation_prompts = OrderedDict()
        creation_prompts['id'] = prompts.TextPrompt('Building ID')
        creation_prompts['location'] = prompts.TextPrompt('Location')
        self.creation_prompt_list = prompts.PromptList(creation_prompts)

    def get_header(self):
        return 'Manage Buildings'

    def get_menu_prompt(self):
        return self.menu_prompt

    def process_menu_selection(self, response):
        if response == 'back':
            self.router.back()
            return

        if response not in self.supported_operations:
            raise prompts.InvalidResponseException(response)

        getattr(self, response)()

    def create(self):
        """
        Create a new building by prompting the user for the necessary information.
        The gathered parameters will be passed on to the building controller.
        """
        create_params = self.creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_building(
            create_params['id'], create_params['location']
        )

        if success:
            self.output.success(self.create_building_success_message, end='\n\n')
        else:
            self.output.fail(self.create_building_error_message, end='\n\n')

    def update(self):
        """
        Update an existing building by prompting the user for the building ID and
        the information to be updated. The gathered parameters will be passed on
        to the building controller.
        """
        pass

    def delete(self):
        """
        Delete an existing building by prompting the user for the building ID.
        This ID will be passed on to the building controller.
        """
        pass