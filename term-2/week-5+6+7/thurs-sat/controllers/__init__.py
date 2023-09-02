from controllers.users_controllers import users
from controllers.tasks_controllers import tasks
from controllers.comments_controllers import comments
from controllers.auth_controllers import auths

registered_controllers = (
    users,
    tasks,
    comments,
    auths,
)
