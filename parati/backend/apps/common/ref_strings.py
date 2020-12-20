class Errors:

    def __init__(self, error, code):
        self.error = error
        self.code = code


class Success:

    def __init__(self, success, code):
        self.success = success
        self.code = code


class SuccessMessage:
    success = Success('SUCCESS', 10)
    create_succesful = Success("Task was created successfully",11)
    update_successful = Success("update was successful", 12)
    delete_successful = Success("task deleted", 13)


class CommonErrorMessage:
    some_error_occurred = Errors('Something went wrong', 100)
    city_not_found = Errors("City NAHI MILLI", 101)

    @staticmethod
    def field_errors(errors):
        errors_dict = Errors(errors, 199)
        return errors_dict
