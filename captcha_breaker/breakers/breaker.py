from abc import ABC, abstractmethod
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from selenium import webdriver

class APIBreaker(ABC):

    def __init__(self, key:str = None, verbose:bool = False) -> None:
        self._key = key
        self.verbose = verbose

    @abstractmethod
    def solve_and_return_solution():
        pass

    def __balance(self):
        solver = recaptchaV2Proxyless()
        solver.set_verbose(self.verbose)
        solver.set_key(self.key)
        return solver.get_balance()
    
    @property
    def key(self):
        raise NotImplementedError
    
    @key.setter
    def key(self, key_token):
        self._key = key_token

    @property
    def get_balance(self):
        return self.__balance()

class SoundBreaker(ABC):
    def __init__(self, driver: webdriver = None) -> None:
        self.driver = driver
    
    @abstractmethod
    def resolver():
        pass