# system imports
from sys import stdin

# python imports
from collections import OrderedDict

# application imports
from cli.mixins import CLIMixin


class InvalidResponseException(Exception):
    """
    Raised when a response to a prompt is invalid.
    """

    def __init__(self, invalid_response, *args, **kwargs):
        message = 'Invalid response: %s' % invalid_response
        super(InvalidResponseException, self).__init__(message, *args, **kwargs)


class Prompt(CLIMixin):
    PROMPT = '> '

    def __init__(self, question=''):
        self.question = question

    def ask(self):
        self.output.info('%s:\n%s' % (self.question, self.PROMPT), end='')
        return self

    def parse(self):
        return self.get_response()

    @staticmethod
    def get_response():
        """
        Get the response from standard input. This is a blocking operation.
        """
        return stdin.readline()

    def invalid_response(self, message):
        if message:
            self.output.warn(message, end='\n')
        else:
            self.output.warn('Invalid response.', end='\n')


class TextPrompt(Prompt):

    def parse(self):
        response = super(TextPrompt, self).parse()
        return response.strip() if response else ''


class MenuPrompt(Prompt):

    def __init__(self, options):
        super(MenuPrompt, self).__init__()

        # store options in an OrderedDict in order to make key retrieval easy
        self.options = OrderedDict()
        for key, option in options.iteritems():
            self.options[key] = option

    def ask(self):
        menu_options = []
        for i, option in enumerate(self.options.values()):
            menu_options.append('%s) %s' % (i+1, option))

        self.output.info('\n'.join(menu_options + [self.PROMPT]), end='')
        return self

    def parse(self):
        response = super(MenuPrompt, self).parse()
        self.output.newline()
        try:
            index = int(response) - 1
            if index < 0 or index >= len(self.options):
                raise InvalidResponseException(response)
            return self.options.keys()[index]
        except ValueError:
            raise InvalidResponseException(response)


class PromptList(CLIMixin):

    def __init__(self, prompts):
        self.prompts = prompts

    def ask_and_parse_all(self):
        responses = {}

        for key, prompt in self.prompts.iteritems():
            try:
                responses[key] = prompt.ask().parse()
            except InvalidResponseException:
                # in the future, we could add some exception handling here
                raise

        self.output.newline()
        return responses