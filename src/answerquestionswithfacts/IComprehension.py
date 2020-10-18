from abc import ABC, abstractmethod


class Comprehension(ABC):
    @abstractmethod
    def validate_input(self, parameter_list):
        raise NotImplementedError

    @abstractmethod
    def process_data(self, parameter_list):
        raise NotImplementedError

    @abstractmethod
    def get_results(self, parameter_list):
        raise NotImplementedError
