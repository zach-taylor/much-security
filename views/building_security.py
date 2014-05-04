# python imports
from collections import OrderedDict

# application imports
from controllers.building_security import BuildingSecurityController
from views import BaseView
from views import prompts


class BuildingSecurityView(BaseView):
    supported_operations = [
        'get_badge_reader',
        'create_badge_reader',
        'update_badge_reader',
        'delete_badge_reader',
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
    
    create_badge_reader_success_message = 'Badge reader created.'
    create_badge_reader_error_message = 'Could not create badge reader.'

    update_badge_reader_success_message = 'Badge reader updated.'
    update_badge_reader_error_message = 'Could not update badge reader.'

    get_badge_reader_success_message = 'Badge reader retrieved: %s'
    get_badge_reader_error_message = 'Could not retrieve badge reader.'

    delete_badge_reader_success_message = 'Badge reader deleted.'
    delete_badge_reader_error_message = 'Could not delete badge reader.'

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
        menu_options['get_badge_reader'] = 'Get a badge reader'
        menu_options['create_badge_reader'] = 'Create a new badge reader'
        menu_options['update_badge_reader'] = 'Update an badge reader'
        menu_options['delete_badge_reader'] = 'Delete an badge reader'
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
        badge_reader_creation_prompts = OrderedDict()
        badge_reader_creation_prompts['door_id'] = prompts.TextPrompt('Door Id')
        badge_reader_creation_prompts['badge_reader_id'] = prompts.TextPrompt('Badge Reader ID')
        self.badge_reader_creation_prompt_list = prompts.PromptList(badge_reader_creation_prompts)
        
        # Badge Reader update prompts
        badge_reader_update_prompts = OrderedDict()
        badge_reader_update_prompts['old_badge_reader_id'] = prompts.TextPrompt('Old badge reader ID')
        badge_reader_update_prompts['new_badge_reader_id'] = prompts.TextPrompt('New badge reader ID')
        badge_reader_update_prompts['door_id'] = prompts.TextPrompt('door ID')
        self.badge_reader_update_prompt_list = prompts.PromptList(badge_reader_update_prompts)
        
        # Badge Reader retrieval prompts
        badge_reader_retrieval_prompts = OrderedDict()
        badge_reader_retrieval_prompts['badge_reader_id'] = prompts.TextPrompt('Badge Reader ID')
        self.badge_reader_retrieval_prompt_list = prompts.PromptList(badge_reader_retrieval_prompts)

        # Badge Reader deletion prompts (happen to be the same as retrieval)
        self.badge_reader_deletion_prompt_list = self.badge_reader_retrieval_prompt_list
        
        # Camera creation prompts
        camera_creation_prompts = OrderedDict()
        camera_creation_prompts['location'] = prompts.TextPrompt('Location')
        camera_creation_prompts['camera_id'] = prompts.TextPrompt('Camera ID')
        self.camera_creation_prompt_list = prompts.PromptList(camera_creation_prompts)
        
        # Camera update prompts
        camera_update_prompts = OrderedDict()
        camera_update_prompts['old_camera_id'] = prompts.TextPrompt('Old Camera ID')
        camera_update_prompts['new_camera_id'] = prompts.TextPrompt('New Camera ID')
        camera_update_prompts['location'] = prompts.TextPrompt('Location')
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
        door_creation_prompts['locked'] = prompts.TextPrompt('Locked (True)')
        self.door_creation_prompt_list = prompts.PromptList(door_creation_prompts)
        
        # Door update prompts
        door_update_prompts = OrderedDict()
        door_update_prompts['old_door_id'] = prompts.TextPrompt('Old Door ID')
        door_update_prompts['new_door_id'] = prompts.TextPrompt('New Door ID')
        door_update_prompts['location'] = prompts.TextPrompt('Location')
        door_update_prompts['locked'] = prompts.TextPrompt('Locked')
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
        
    def create_badge_reader(self):
        """
        Create a new badge_reader by prompting the user for the necessary information.
        The gathered parameters will be passed on to the BuildingSecurity controller.
        """
        create_params = self.badge_reader_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_badge_reader(
            create_params['door_id'], create_params['badge_reader_id']
        )

        if success:
            self.output.success(self.create_badge_reader_success_message, end='\n\n')
        else:
            self.output.fail(self.create_badge_reader_error_message, end='\n\n')

    def update_badge_reader(self):
        """
        Update an existing badge reader by prompting the user for the badge_reader ID and
        the information to be updated. The gathered parameters will be passed on
        to the building security controller.
        """
        update_params = self.badge_reader_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_badge_reader(
            update_params['old_badge_reader_id'], update_params['new_badge_reader_id'], update_params['door_id']
        )

        if success:
            self.output.success(self.update_badge_reader_success_message, end='\n\n')
        else:
            self.output.fail(self.update_badge_reader_error_message, end='\n\n')

    def delete_badge_reader(self):
        """
        Delete an existing badge reader by prompting the user for the badge reader ID.
        This ID will be passed on to the building security controller.
        """
        delete_params = self.badge_reader_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_badge_reader(delete_params['badge_reader_id'])

        if success:
            self.output.success(self.delete_badge_reader_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_badge_reader_error_message, end='\n\n')

    def get_badge_reader(self):
        """
        Get a badge reader. This is not in our design, but it is useful for debugging.
        """
        get_params = self.badge_reader_retrieval_prompt_list.ask_and_parse_all()
        badge_reader = self.controller.get_badge_reader(get_params['badge_reader_id'])

        if badge_reader:
            self.output.success(self.get_badge_reader_success_message % badge_reader, end='\n\n')
        else:
            self.output.fail(self.get_badge_reader_error_message, end='\n\n')
            
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
            update_params['old_camera_id'], update_params['new_camera_id'], update_params['location']
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
            create_params['location'], create_params['door_id'], create_params['locked']
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
            update_params['old_door_id'], update_params['new_door_id'], update_params['location'],
            update_params['locked']
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
        Dump the contents of the badge_reader, camera, and door tables for debugging purposes.
        """
        dump = {
            'badge_reader': self.controller.get_badge_reader_debug(),
            'camera': self.controller.get_camera_debug(),
            'door': self.controller.get_door_debug()
        }
        self.output.warn(dump, end='\n\n')