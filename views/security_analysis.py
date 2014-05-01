# python imports
from collections import OrderedDict

# application imports
from controllers.security_analysis import SecurityAnalysisController
from views import BaseView
from views import prompts


class SecurityAnalysisView(BaseView):
    supported_operations = [
        'employee_entry',
        'visitor_entry',
        'badge_reader_entry',
        'search_entry',
        'employee_report',
        'visitor_report',
        'badge_reader_report',
        'all_reports',
        'debug'
    ]

    employee_entry_success_message = 'Employee entry recorded.'
    employee_entry_error_message = 'Employee entry could not be recorded.'

    visitor_entry_success_message = 'Visitor entry recorded.'
    visitor_entry_error_message = 'Visitor entry could not be recorded.'

    badge_reader_entry_success_message = 'Badge reader entry recorded.'
    badge_reader_entry_error_message = 'Badge reader entry could not be recorded.'

    search_entry_success_message = 'Entries retrieved: %s'
    search_entry_error_message = 'Entries could not be searched.'

    employee_report_success_message = 'Employee report retrieved: %s'
    employee_report_error_message = 'Employee report could not be retrieved.'

    visitor_report_success_message = 'Visitor report retrieved: %s'
    visitor_report_error_message = 'Visitor report could not be retrieved.'

    badge_reader_report_success_message = 'Badge reader report retrieved: %s'
    badge_reader_report_error_message = 'Badge reader report could not be retrieved.'

    all_reports_success_message = 'All reports retrieved: %s'
    all_reports_error_message = 'All reports could not be retrieved.'

    def __init__(self, router):
        super(SecurityAnalysisView, self).__init__(router)

        # Security Analysis controller
        self.controller = SecurityAnalysisController()

        # Security Analysis view menu
        menu_options = OrderedDict()
        menu_options['employee_entry'] = 'Record an employee entry'
        menu_options['visitor_entry'] = 'Record a visitor entry'
        menu_options['badge_reader_entry'] = 'Record a badge reader entry'
        menu_options['search_entry'] = 'Search log entries'
        menu_options['employee_report'] = 'Get employee entry report'
        menu_options['visitor_report'] = 'Get visitor entry report'
        menu_options['badge_reader_report'] = 'Get badge reader entry report'
        menu_options['all_reports'] = 'Get all log entry reports'
        menu_options['debug'] = 'Debug'
        menu_options['back'] = '<< Back'
        self.menu_prompt = prompts.MenuPrompt(menu_options)

        # Employee entry prompts
        employee_entry_prompts = OrderedDict()
        employee_entry_prompts['entry_id'] = prompts.TextPrompt('Entry ID (auto)')
        employee_entry_prompts['badge_id'] = prompts.TextPrompt('Employee badge ID')
        employee_entry_prompts['time'] = prompts.TextPrompt('Time (now)')
        employee_entry_prompts['result'] = prompts.TextPrompt('Result (success)')
        self.employee_entry_prompt_list = prompts.PromptList(employee_entry_prompts)

        # Visitor entry prompts
        visitor_entry_prompts = OrderedDict()
        visitor_entry_prompts['entry_id'] = prompts.TextPrompt('Entry ID (auto)')
        visitor_entry_prompts['badge_id'] = prompts.TextPrompt('Visitor badge ID')
        visitor_entry_prompts['time'] = prompts.TextPrompt('Time (now)')
        visitor_entry_prompts['result'] = prompts.TextPrompt('Result (success)')
        self.visitor_entry_prompt_list = prompts.PromptList(visitor_entry_prompts)

        # Badge reader entry prompts
        badge_reader_entry_prompts = OrderedDict()
        badge_reader_entry_prompts['entry_id'] = prompts.TextPrompt('Entry ID (auto)')
        badge_reader_entry_prompts['badge_reader_id'] = prompts.TextPrompt('Badge reader ID')
        badge_reader_entry_prompts['badge_id'] = prompts.TextPrompt('Badge ID')
        badge_reader_entry_prompts['time'] = prompts.TextPrompt('Time (now)')
        badge_reader_entry_prompts['result'] = prompts.TextPrompt('Result (success)')
        self.badge_reader_entry_prompt_list = prompts.PromptList(badge_reader_entry_prompts)

        # Search entry prompts
        search_entry_prompts = OrderedDict()
        search_entry_prompts['badge_id'] = prompts.TextPrompt('Badge ID')
        search_entry_prompts['time'] = prompts.TextPrompt('Time')
        self.search_entry_prompt_list = prompts.PromptList(search_entry_prompts)

    def get_header(self):
        return 'Security Analysis'

    def get_menu_prompt(self):
        return self.menu_prompt

    def process_menu_selection(self, response):
        if response == 'back':
            self.router.back()
            return

        if response not in self.supported_operations:
            raise prompts.InvalidResponseException(response)

        getattr(self, response)()

    def employee_entry(self):
        entry_params = self.employee_entry_prompt_list.ask_and_parse_all()
        success = self.controller.employee_entry(
            entry_params['entry_id'], entry_params['badge_id'], entry_params['time'],
            entry_params['result']
        )

        if success:
            self.output.success(self.employee_entry_success_message, end='\n\n')
        else:
            self.output.fail(self.employee_entry_error_message, end='\n\n')

    def visitor_entry(self):
        entry_params = self.visitor_entry_prompt_list.ask_and_parse_all()
        success = self.controller.visitor_entry(
            entry_params['entry_id'], entry_params['badge_id'], entry_params['time'],
            entry_params['result']
        )

        if success:
            self.output.success(self.visitor_entry_success_message, end='\n\n')
        else:
            self.output.fail(self.visitor_entry_error_message, end='\n\n')

    def badge_reader_entry(self):
        entry_params = self.badge_reader_entry_prompt_list.ask_and_parse_all()
        success = self.controller.badge_reader_entry(
            entry_params['entry_id'], entry_params['badge_reader_id'], entry_params['badge_id'],
            entry_params['time'], entry_params['result']
        )

        if success:
            self.output.success(self.badge_reader_entry_success_message, end='\n\n')
        else:
            self.output.fail(self.badge_reader_entry_error_message, end='\n\n')

    def search_entry(self):
        search_params = self.search_entry_prompt_list.ask_and_parse_all()
        results = self.controller.search_entry(search_params['badge_id'], search_params['time'])
        self.output.success(self.search_entry_success_message % results, end='\n\n')

    def debug(self):
        dump = {
            'employee_entries': self.controller.get_employee_log_entry_debug(),
            'visitor_entries': self.controller.get_visitor_log_entry_debug(),
            'badge_reader_entries': self.controller.get_badge_reader_log_entry_debug()
        }
        self.output.warn(dump, end='\n\n')