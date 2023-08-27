from .breaker import APIBreaker
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

class Recaptcha(APIBreaker):
    
    def solve_and_return_solution(self, website_key: str, website_url: str) -> str:
        solver = recaptchaV2Proxyless()
        solver.set_verbose(self.verbose)
        solver.set_key(self._key)
        solver.set_website_key(website_key)
        solver.set_website_url(website_url)

        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            return g_response
        else:
            return solver.error_code