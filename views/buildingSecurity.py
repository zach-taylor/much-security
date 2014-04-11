# python imports
from collections import OrderedDict

# application imports
from controllers.buildingSecurity import BuildingSecurityController
from views import BaseView
from views import prompts


class BuildingSecurityView(BaseView):
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
        
    def create_badgeReader(self):
        """
        Create a new badgeReader by prompting the user for the necessary information.
        The gathered parameters will be passed on to the BuildingSecurity controller.
        """
        create_params = self.badgeReader_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_badgeReader(
            create_params['door_id'], create_params['badgeReader_id']
        )

        if success:
            self.output.success(self.create_badgeReader_success_message, end='\n\n')
        else:
            self.output.fail(self.create_badgeReader_error_message, end='\n\n')

    def update_badgeReader(self):
        """
        Update an existing badge reader by prompting the user for the badgeReader ID and
        the information to be updated. The gathered parameters will be passed on
        to the building security controller.
        """
        update_params = self.badgeReader_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_badgeReader(
            update_params['old_door_id'], update_params['new_door_id'], update_params['badgeReader_id']
        )

        if success:
            self.output.success(self.update_badgeReader_success_message, end='\n\n')
        else:
            self.output.fail(self.update_badgeReader_error_message, end='\n\n')

    def delete_badgeReader(self):
        """
        Delete an existing badge reader by prompting the user for the badge reader ID.
        This ID will be passed on to the building security controller.
        """
        delete_params = self.badgeReader_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_badgeReader(delete_params['badgeReader_id'])

        if success:
            self.output.success(self.delete_badgeReader_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_badgeReader_error_message, end='\n\n')

    def get_badgeReader(self):
        """
        Get a badge reader. This is not in our design, but it is useful for debugging.
        """
        get_params = self.badgeReader_retrieval_prompt_list.ask_and_parse_all()
        badgeReader = self.controller.get_badgeReader(get_params['badgeReader_id'])

        if badgeReader:
            self.output.success(self.get_badgeReader_success_message % badgeReader, end='\n\n')
        else:
            self.output.fail(self.get_badgeReader_error_message, end='\n\n')
            
    def create_camera(self):
        """
        Create a new camera by prompting the user for the necessary information.
        The gathered parameters will be passed on to the BuildingSecurity controller.
        """
        create_params = self.camera_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_camera(
            create_params['location'], create_params['camera_id']
        )

        if success:
            self.output.success(self.create_camera_success_message, end='\n\n')
        else:
            self.output.fail(self.create_camera_error_message, end='\n\n')

    def update_camera(self):
        """
        Update an existing camera by prompting the user for the camera ID and
        the information to be updated. The gathered parameters will be passed on
        to the building security controller.
        """
        update_params = self.camera_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_camera(
            update_params['new_location'], update_params['camera_id']
        )

        if success:
            self.output.success(self.update_camera_success_message, end='\n\n')
        else:
            self.output.fail(self.update_camera_error_message, end='\n\n')

    def delete_camera(self):
        """
        Delete an existing camera by prompting the user for the camera ID.
        This ID will be passed on to the building security controller.
        """
        delete_params = self.camera_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_camera(delete_params['camera_id'])

        if success:
            self.output.success(self.delete_camera_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_camera_error_message, end='\n\n')

    def get_camera(self):
        """
        Get a camera. This is not in our design, but it is useful for debugging.
        """
        get_params = self.camera_retrieval_prompt_list.ask_and_parse_all()
        camera = self.controller.get_camera(get_params['camera_id'])

        if camera:
            self.output.success(self.get_camera_success_message % camera, end='\n\n')
        else:
            self.output.fail(self.get_camera_error_message, end='\n\n')
            
    def create_door(self):
        """
        Create a new door by prompting the user for the necessary information.
        The gathered parameters will be passed on to the BuildingSecurity controller.
        """
        create_params = self.door_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_door(
            create_params['location'], create_params['door_id']
        )

        if success:
            self.output.success(self.create_door_success_message, end='\n\n')
        else:
            self.output.fail(self.create_door_error_message, end='\n\n')

    def update_door(self):
        """
        Update an existing door by prompting the user for the door ID and
        the information to be updated. The gathered parameters will be passed on
        to the building security controller.
        """
        update_params = self.door_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_door(
            update_params['new_location'], update_params['door_id']
        )

        if success:
            self.output.success(self.update_door_success_message, end='\n\n')
        else:
            self.output.fail(self.update_door_error_message, end='\n\n')

    def delete_door(self):
        """
        Delete an existing door by prompting the user for the door ID.
        This ID will be passed on to the building security controller.
        """
        delete_params = self.door_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_door(delete_params['door_id'])

        if success:
            self.output.success(self.delete_door_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_door_error_message, end='\n\n')

    def get_door(self):
        """
        Get a door. This is not in our design, but it is useful for debugging.
        """
        get_params = self.door_retrieval_prompt_list.ask_and_parse_all()
        door = self.controller.get_door(get_params['door_id'])

        if door:
            self.output.success(self.get_door_success_message % door, end='\n\n')
        else:
            self.output.fail(self.get_door_error_message, end='\n\n')
            
    def debug(self):
        """
        Dump the contents of the badgeReader, camera, and door tables for debugging purposes.
        """
        dump = {
            'badgeReader': self.controller.get_badgeReader_debug(),
            'camera': self.controller.get_camera_debug(),
            'door': self.controller.get_door_debug()
        }
        self.output.warn(dump, end='\n\n')
            
    
    
        