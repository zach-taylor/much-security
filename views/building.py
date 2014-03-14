# python imports
from collections import OrderedDict

# application imports
from controllers.building import BuildingController
from views import BaseView
from views import prompts


class BuildingView(BaseView):
    supported_operations = [
        'get',
        'create',
        'update',
        'delete',
        'debug'
    ]

    create_building_success_message = 'Building created.'
    create_building_error_message = 'Could not create building.'

    update_building_success_message = 'Building updated.'
    update_building_error_message = 'Could not update building.'

    get_building_success_message = 'Building retrieved: %s'
    get_building_error_message = 'Could not retrieve building.'

    delete_building_success_message = 'Building deleted.'
    delete_building_error_message = 'Could not delete building.'

    def __init__(self, router):
        super(BuildingView, self).__init__(router)

        # Building controller
        self.controller = BuildingController()

        # Building view menu
        menu_options = OrderedDict()
        menu_options['get'] = 'Get a building'
        menu_options['create'] = 'Create a new building'
        menu_options['update'] = 'Update a building'
        menu_options['delete'] = 'Delete a building'
        menu_options['debug'] = 'Debug'
        menu_options['back'] = '<< Back'
        self.menu_prompt = prompts.MenuPrompt(menu_options)

        # Creation prompts
        creation_prompts = OrderedDict()
        creation_prompts['location'] = prompts.TextPrompt('Location')
        self.creation_prompt_list = prompts.PromptList(creation_prompts)

        # Update prompts
        update_prompts = OrderedDict()
        update_prompts['old_location'] = prompts.TextPrompt('Old location')
        update_prompts['new_location'] = prompts.TextPrompt('New location')
        self.update_prompt_list = prompts.PromptList(update_prompts)

        # Retrieval prompts
        retrieval_prompts = OrderedDict()
        retrieval_prompts['location'] = prompts.TextPrompt('Location')
        self.retrieval_prompt_list = prompts.PromptList(retrieval_prompts)

        # Deletion prompts (happen to be the same as retrieval)
        self.deletion_prompt_list = self.retrieval_prompt_list

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
        success = self.controller.create_building(create_params['location'])

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
        update_params = self.update_prompt_list.ask_and_parse_all()
        success = self.controller.update_building(
            update_params['old_location'], update_params['new_location']
        )

        if success:
            self.output.success(self.update_building_success_message, end='\n\n')
        else:
            self.output.fail(self.update_building_error_message, end='\n\n')

    def delete(self):
        """
        Delete an existing building by prompting the user for the building ID.
        This ID will be passed on to the building controller.
        """
        delete_params = self.deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_building(delete_params['location'])

        if success:
            self.output.success(self.delete_building_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_building_error_message, end='\n\n')

    def get(self):
        """
        Get a building. This is not in our design, but it is useful for debugging.
        """
        get_params = self.retrieval_prompt_list.ask_and_parse_all()
        building = self.controller.get_building(get_params['location'])

        if building:
            self.output.success(self.get_building_success_message % building, end='\n\n')
        else:
            self.output.fail(self.get_building_error_message, end='\n\n')

    def debug(self):
        """
        Dump the contents of the buildings table for debugging purposes.
        """
        self.output.warn(self.controller.get_building_debug(), end='\n\n')