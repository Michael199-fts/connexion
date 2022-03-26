class Service:
    custom_validations = []

    def __init__(self, *args, **kwargs):
        self.result = None
        self.response_status = None
        self._errors = {}
        self._cleaned_data = {}

    def run_custom_validations(self):
        for custom_validation in self.__class__.custom_validations:
            getattr(self, custom_validation)()

    @classmethod
    def execute(cls, inputs, files=None, **kwargs):
        instance = cls(inputs, files, **kwargs)
        instance.service_clean(inputs, files, **kwargs)
        return instance.process()

    def service_clean(self, inputs, files, **kwargs):
        if inputs:
            for el, val in inputs.items():
                self._cleaned_data.update({el: val})
        if files:
            for file, val in files.items():
                self._cleaned_data.update({file: val})
            """
            Something do with cleaned_data dict
            """
        return

    @property
    def cleaned_data(self):
        return self._cleaned_data

    def add_error(self, field, error):
        if self._errors.get(field):
            self._errors[field].append(error)
        else:
            self._errors[field] = [error]
        print("SDS")

    @property
    def errors(self):
        return self._errors

    def process(self):
        """
        Main method to be overridden; contains the Business Rules
        functionality.
        """
        pass

    def is_valid(self):
        return not bool(self._errors)

class ServiceOutcome:
    """
    Wrapper to execute Service objects
    """
    def __init__(self, service_object, service_object_attributes=None, service_object_files=None):
        self._errors = {}
        self._result = None
        self._response_status = None
        self._outcome = self.execute(service_object, service_object_attributes, service_object_files)

    def execute(self, service_object, service_object_attributes, service_object_files):
        outcome = service_object.execute(service_object_attributes, service_object_files)
        self._response_status = outcome.response_status
        if bool(outcome.errors):
            response_status = self.response_status if hasattr(self, 'response_status') else 400
            self._errors = outcome.errors
            self._response_status = response_status
        else:
            self._result = outcome.result
        return outcome

    @property
    def valid(self):
        return not bool(self._errors)

    @property
    def service(self):
        return self._outcome

    @property
    def result(self):
        return self._result

    @property
    def errors(self):
        return self._errors

    @property
    def response_status(self):
        return self._response_status