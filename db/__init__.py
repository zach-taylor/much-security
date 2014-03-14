# database imports
from db.database import DatabaseSupport


# global db support instance
global_db = DatabaseSupport()


def get_database_support():
    """
    Get the global instance of the application's database support.
    """
    return global_db