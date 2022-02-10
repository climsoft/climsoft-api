import random
import uuid

from climsoft_api.api.climsoftuser.schema import CreateClimsoftUser, ClimsoftUserRole


def get_valid_climsoft_user_input():
    return CreateClimsoftUser(
        userName=uuid.uuid4().hex,
        userRole=random.choice([role.value for role in ClimsoftUserRole])
    )
