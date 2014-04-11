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