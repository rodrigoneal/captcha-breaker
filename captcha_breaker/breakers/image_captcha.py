from anticaptchaofficial.imagecaptcha import imagecaptcha

from .breaker import APIBreaker


class ImageCaptcha(APIBreaker):
    def solve_and_return_solution(self, image: str) -> str:
        solver = imagecaptcha()
        solver.set_verbose(self.verbose)
        solver.set_key(self._key)

        captcha_text = solver.solve_and_return_solution(image)
        if captcha_text != 0:
            return captcha_text
        else:
            return solver.error_code
