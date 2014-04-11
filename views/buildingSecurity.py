# python imports
from collections import OrderedDict

# application imports
from controllers.personnel import PersonnelController
from views import BaseView
from views import prompts


class PersonnelView(BaseView):
    supported_operations = [
        'get_badgeReader',
        'create_badgeReader',
        'update_badgeReader',
        'delete_badgeReader',
        'get_camera',
        'create_camera',
        'update_camera',
        'delete_camera',
        'get_door',
        'create_door',
        'update_door',
        'delete_door',
        'debug'
    ]
    
    create_badgeReader_success_message = 'Badge reader created.'
    create_badgeReader_error_message = 'Could not create badge reader.'

    update_badgeReader_success_message = 'Badge reader updated.'
    update_employee_error_message = 'Could not update badge reader.'

    get_badgeReader_success_message = 'Badge reader retrieved: %s'
    get_badgeReader_error_message = 'Could not retrieve badge reader.'

    delete_badgeReader_success_message = 'Badge reader deleted.'
    delete_badgeReader_error_message = 'Could not delete badge reader.'

    create_camera_success_message = 'Camera created.'
    create_camera_error_message = 'Could not create camera.'

    update_camera_success_message = 'Camera updated.'
    update_camera_error_message = 'Could not update camera.'

    get_camera_success_message = 'Camera retrieved: %s'
    get_camera_error_message = 'Could not retrieve camera.'

    delete_camera_success_message = 'Camera deleted.'
    delete_camera_error_message = 'Could not delete camera.'
    
    create_door_success_message = 'Door created.'
    create_door_error_message = 'Could not create door.'

    update_door_success_message = 'Door updated.'
    update_door_error_message = 'Could not update door.'

    get_door_success_message = 'Door retrieved: %s'
    get_door_error_message = 'Could not retrieve door.'

    delete_door_success_message = 'Door deleted.'
    delete_door_error_message = 'Could not delete door.'
    
    def __init__(self, router):
        super(BuildingSecurityView, self).__init__(router)
        
         # BuildingSecurity controller
        self.controller = BuildingSecurityController()
        
        # Personnel view menu
        menu_options = OrderedDict()
        menu_options['get_badgeReader'] = 'Get a badge reader'
        menu_options['create_badgeReader'] = 'Create a new badge reader'
        menu_options['update_badgeReader'] = 'Update an badge reader'
        menu_options['delete_badgeReader'] = 'Delete an badge reader'
        menu_options['get_camera'] = 'Get a camera'
        menu_options['create_camera'] = 'Create a new camera'
        menu_options['update_camera'] = 'Update a camera'
        menu_options['delete_camera'] = 'Delete a camera'
        menu_options['get_door'] = 'Get a door'
        menu_options['create_door'] = 'Create a new door'
        menu_options['update_door'] = 'Update a door'
        menu_options['delete_door'] = 'Delete a door'
        menu_options['debug'] = 'Debug'
        menu_options['back'] = '<< Back'
        self.menu_prompt = prompts.MenuPrompt(menu_options)
        
        # Badge reader creation prompts
        badgeReader_creation_prompts = OrderedDict()
        badgeReader_creation_prompts['door_id'] = prompts.TextPrompt('Door Id')
        badgeReader_creation_prompts['badgeReader_id'] = prompts.TextPrompt('Badge Reader ID')
        self.badgeReader_creation_prompt_list = prompts.PromptList(badgeReader_creation_prompts)
        
        # Badge Reader update prompts
        badgeReader_update_prompts = OrderedDict()
        badgeReader_update_prompts['old_door_id'] = prompts.TextPrompt('Old door ID')
        badgeReader_update_prompts['new_door_id'] = prompts.TextPrompt('New door ID')
        badgeReader_update_prompts['badgeReader_id'] = prompts.TextPrompt('Badge Reader ID')
        self.badgeReader_update_prompt_list = prompts.PromptList(badgeReader_update_prompts)
        
        # Badge Reader retrieval prompts
        badgeReader_retrieval_prompts = OrderedDict()
        badgeReader_retrieval_prompts['badgeReader_id'] = prompts.TextPrompt('Badge Reader ID')
        self.badgeReader_retrieval_prompt_list = prompts.PromptList(badgeReader_retrieval_prompts)

        # Badge Reader deletion prompts (happen to be the same as retrieval)
        self.badgeReader_deletion_prompt_list = self.badgeReader_retrieval_prompt_list
        
        # Camera creation prompts
        camera_creation_prompts = OrderedDict()
        camera_creation_prompts['location'] = prompts.TextPrompt('Location')
        camera_creation_prompts['camera_id'] = prompts.TextPrompt('Camera ID')
        self.camera_creation_prompt_list = prompts.PromptList(camera_creation_prompts)
        
        # Camera update prompts
        camera_update_prompts = OrderedDict()
        camera_update_prompts['new_location'] = prompts.TextPrompt('New location')
        camera_update_prompts['camera_id'] = prompts.TextPrompt('Camera ID')
        self.camera_update_prompt_list = prompts.PromptList(camera_update_prompts)
        
         # Camera retrieval prompts
        camera_retrieval_prompts = OrderedDict()
        camera_retrieval_prompts['camera_id'] = prompts.TextPrompt('camera ID')
        self.camera_retrieval_prompt_list = prompts.PromptList(camera_retrieval_prompts)
        
        # Camera deletion prompts (happen to be the same as retrieval)
        self.camera_deletion_prompt_list = self.camera_retrieval_prompt_list
        
        # Door creation prompts
        door_creation_prompts = OrderedDict()
        door_creation_prompts['location'] = prompts.TextPrompt('Location')
        door_creation_prompts['door_id'] = prompts.TextPrompt('Door ID')
        self.door_creation_prompt_list = prompts.PromptList(door_creation_prompts)
        
        # Door update prompts
        door_update_prompts = OrderedDict()
        door_update_prompts['new_location'] = prompts.TextPrompt('New location')
        door_update_prompts['door_id'] = prompts.TextPrompt('Door ID')
        self.door_update_prompt_list = prompts.PromptList(door_update_prompts)
        
         # Door retrieval prompts
        door_retrieval_prompts = OrderedDict()
        door_retrieval_prompts['door_id'] = prompts.TextPrompt('Door ID')
        self.door_retrieval_prompt_list = prompts.PromptList(door_retrieval_prompts)
        
        # Door deletion prompts (happen to be the same as retrieval)
        self.door_deletion_prompt_list = self.door_retrieval_prompt_list
        
    def get_header(self):
        return 'Manage Building Security'

    def get_menu_prompt(self):
        return self.menu_prompt

    def process_menu_selection(self, response):
        if response == 'back':
            self.router.back()
            return

        if response not in self.supported_operations:
            raise prompts.InvalidResponseException(response)

        getattr(self, response)()
        
    
        