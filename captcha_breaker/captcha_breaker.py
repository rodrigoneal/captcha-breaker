from captcha_breaker.breakers.image_captcha import ImageCaptcha
from captcha_breaker.breakers.recaptcha import Recaptcha
from captcha_breaker.breakers.selenium_recaptcha import SeleniumRecaptcha
from captcha_breaker.breakers.breaker import APIBreaker, SoundBreaker
from selenium import webdriver


class CaptchaBreaker:
    image_captcha = ImageCaptcha()
    recaptcha = Recaptcha()
    selenium_recaptcha = SeleniumRecaptcha()

    def _reflection(self, key, verbose, driver):
        for atributo in dir(self):
            atributo_real = getattr(self, atributo)
            if isinstance(atributo_real, APIBreaker):
                atributo_real.key = key
                atributo_real.verbose = verbose
            elif isinstance(atributo_real, SoundBreaker):
                atributo_real.driver = driver

    def __init__(
        self, key: str = None, verbose: bool = False, driver: webdriver = None
    ) -> None:
        self._reflection(key, verbose, driver)
