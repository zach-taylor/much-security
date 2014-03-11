# application imports
from views.main import MainView
from views.router import Router

# setup the application router that will handle navigation between views
app_router = Router()

if __name__ == '__main__':
    # navigate to the main view first
    app_router.goto(MainView)