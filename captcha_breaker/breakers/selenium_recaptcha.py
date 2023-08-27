from selenium_recaptcha_solver import RecaptchaSolver

from selenium.webdriver.remote.webelement import WebElement

from captcha_breaker.breakers.breaker import SoundBreaker


class SeleniumRecaptcha(SoundBreaker):
    def resolver(self, element: WebElement) -> None:
        solver = RecaptchaSolver(driver=self.driver)
        solver.click_recaptcha_v2(iframe=element)
