# python imports
from collections import OrderedDict

# application imports
from controllers.personnel import PersonnelController
from views import BaseView
from views import prompts


class PersonnelView(BaseView):
    supported_operations = [
        'get_employee',
        'create_employee',
        'update_employee',
        'delete_employee',
        'get_visitor',
        'create_visitor',
        'update_visitor',
        'delete_visitor',
        'debug'
    ]

    create_employee_success_message = 'Employee created.'
    create_employee_error_message = 'Could not create employee.'

    update_employee_success_message = 'Employee updated.'
    update_employee_error_message = 'Could not update employee.'

    get_employee_success_message = 'Employee retrieved: %s'
    get_employee_error_message = 'Could not retrieve employee.'

    delete_employee_success_message = 'Employee deleted.'
    delete_employee_error_message = 'Could not delete employee.'

    create_visitor_success_message = 'Visitor created.'
    create_visitor_error_message = 'Could not create visitor.'

    update_visitor_success_message = 'Visitor updated.'
    update_visitor_error_message = 'Could not update visitor.'

    get_visitor_success_message = 'Visitor retrieved: %s'
    get_visitor_error_message = 'Could not retrieve visitor.'

    delete_visitor_success_message = 'Visitor deleted.'
    delete_visitor_error_message = 'Could not delete visitor.'

    def __init__(self, router):
        super(PersonnelView, self).__init__(router)

        # Personnel controller
        self.controller = PersonnelController()

        # Personnel view menu
        menu_options = OrderedDict()
        menu_options['get_employee'] = 'Get an employee'
        menu_options['create_employee'] = 'Create a new employee'
        menu_options['update_employee'] = 'Update an employee'
        menu_options['delete_employee'] = 'Delete an employee'
        menu_options['get_visitor'] = 'Get a visitor'
        menu_options['create_visitor'] = 'Create a new visitor'
        menu_options['update_visitor'] = 'Update a visitor'
        menu_options['delete_visitor'] = 'Delete a visitor'
        menu_options['debug'] = 'Debug'
        menu_options['back'] = '<< Back'
        self.menu_prompt = prompts.MenuPrompt(menu_options)

        # Employee creation prompts
        employee_creation_prompts = OrderedDict()
        employee_creation_prompts['badge_id'] = prompts.TextPrompt('Badge ID')
        employee_creation_prompts['name'] = prompts.TextPrompt('Name')
        self.employee_creation_prompt_list = prompts.PromptList(employee_creation_prompts)

        # Employee update prompts
        employee_update_prompts = OrderedDict()
        employee_update_prompts['old_badge_id'] = prompts.TextPrompt('Old badge ID')
        employee_update_prompts['new_badge_id'] = prompts.TextPrompt('New badge ID')
        employee_update_prompts['name'] = prompts.TextPrompt('Name')
        self.employee_update_prompt_list = prompts.PromptList(employee_update_prompts)

        # Employee retrieval prompts
        employee_retrieval_prompts = OrderedDict()
        employee_retrieval_prompts['badge_id'] = prompts.TextPrompt('Badge ID')
        self.employee_retrieval_prompt_list = prompts.PromptList(employee_retrieval_prompts)

        # Employee deletion prompts (happen to be the same as retrieval)
        self.employee_deletion_prompt_list = self.employee_retrieval_prompt_list

        # Visitor creation prompts
        visitor_creation_prompts = OrderedDict()
        visitor_creation_prompts['badge_id'] = prompts.TextPrompt('Temporary badge ID')
        visitor_creation_prompts['name'] = prompts.TextPrompt('Name')
        visitor_creation_prompts['associated_employee'] = prompts.TextPrompt('Associated employee')
        self.visitor_creation_prompt_list = prompts.PromptList(visitor_creation_prompts)

        # Visitor update prompts
        visitor_update_prompts = OrderedDict()
        visitor_update_prompts['old_badge_id'] = prompts.TextPrompt('Old badge ID')
        visitor_update_prompts['new_badge_id'] = prompts.TextPrompt('New badge ID')
        visitor_update_prompts['name'] = prompts.TextPrompt('Name')
        visitor_update_prompts['associated_employee'] = prompts.TextPrompt('Associated employee')
        self.visitor_update_prompt_list = prompts.PromptList(visitor_update_prompts)

        # Visitor retrieval prompts
        visitor_retrieval_prompts = OrderedDict()
        visitor_retrieval_prompts['badge_id'] = prompts.TextPrompt('Badge ID')
        self.visitor_retrieval_prompt_list = prompts.PromptList(visitor_retrieval_prompts)

        # Visitor deletion prompts (happen to be the same as retrieval)
        self.visitor_deletion_prompt_list = self.visitor_retrieval_prompt_list

    def get_header(self):
        return 'Manage Personnel'

    def get_menu_prompt(self):
        return self.menu_prompt

    def process_menu_selection(self, response):
        if response == 'back':
            self.router.back()
            return

        if response not in self.supported_operations:
            raise prompts.InvalidResponseException(response)

        getattr(self, response)()

    def create_employee(self):
        """
        Create a new employee by prompting the user for the necessary information.
        The gathered parameters will be passed on to the personnel controller.
        """
        create_params = self.employee_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_employee(
            create_params['badge_id'], create_params['name']
        )

        if success:
            self.output.success(self.create_employee_success_message, end='\n\n')
        else:
            self.output.fail(self.create_employee_error_message, end='\n\n')

    def update_employee(self):
        """
        Update an existing employee by prompting the user for the badge ID and
        the information to be updated. The gathered parameters will be passed on
        to the personnel controller.
        """
        update_params = self.employee_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_employee(
            update_params['old_badge_id'], update_params['new_badge_id'], update_params['name']
        )

        if success:
            self.output.success(self.update_employee_success_message, end='\n\n')
        else:
            self.output.fail(self.update_employee_error_message, end='\n\n')

    def delete_employee(self):
        """
        Delete an existing employee by prompting the user for the employee badge ID.
        This ID will be passed on to the personnel controller.
        """
        delete_params = self.employee_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_employee(delete_params['badge_id'])

        if success:
            self.output.success(self.delete_employee_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_employee_error_message, end='\n\n')

    def get_employee(self):
        """
        Get a employee. This is not in our design, but it is useful for debugging.
        """
        get_params = self.employee_retrieval_prompt_list.ask_and_parse_all()
        employee = self.controller.get_employee(get_params['badge_id'])

        if employee:
            self.output.success(self.get_employee_success_message % employee, end='\n\n')
        else:
            self.output.fail(self.get_employee_error_message, end='\n\n')

    def create_visitor(self):
        """
        Create a new visitor by prompting the user for the necessary information.
        The gathered parameters will be passed on to the personnel controller.
        """
        create_params = self.visitor_creation_prompt_list.ask_and_parse_all()
        success = self.controller.create_visitor(
            create_params['badge_id'], create_params['name'], create_params['associated_employee']
        )

        if success:
            self.output.success(self.create_visitor_success_message, end='\n\n')
        else:
            self.output.fail(self.create_visitor_error_message, end='\n\n')

    def update_visitor(self):
        """
        Update an existing visitor by prompting the user for the badge ID and
        the information to be updated. The gathered parameters will be passed on
        to the personnel controller.
        """
        update_params = self.visitor_update_prompt_list.ask_and_parse_all()
        success = self.controller.update_visitor(
            update_params['old_badge_id'], update_params['new_badge_id'], update_params['name'],
            update_params['associated_employee']
        )

        if success:
            self.output.success(self.update_visitor_success_message, end='\n\n')
        else:
            self.output.fail(self.update_visitor_error_message, end='\n\n')

    def delete_visitor(self):
        """
        Delete an existing visitor by prompting the user for the visitor badge ID.
        This ID will be passed on to the personnel controller.
        """
        delete_params = self.visitor_deletion_prompt_list.ask_and_parse_all()
        success = self.controller.delete_visitor(delete_params['badge_id'])

        if success:
            self.output.success(self.delete_visitor_success_message, end='\n\n')
        else:
            self.output.fail(self.delete_visitor_error_message, end='\n\n')

    def get_visitor(self):
        """
        Get a visitor. This is not in our design, but it is useful for debugging.
        """
        get_params = self.visitor_retrieval_prompt_list.ask_and_parse_all()
        visitor = self.controller.get_visitor(get_params['badge_id'])

        if visitor:
            self.output.success(self.get_visitor_success_message % visitor, end='\n\n')
        else:
            self.output.fail(self.get_visitor_error_message, end='\n\n')

    def debug(self):
        """
        Dump the contents of the employee and visitor tables for debugging purposes.
        """
        dump = {
            'employees': self.controller.get_employee_debug(),
            'visitors': self.controller.get_visitor_debug()
        }
        self.output.warn(dump, end='\n\n')