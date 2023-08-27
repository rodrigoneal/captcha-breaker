from captcha_breaker import CaptchaBreaker

from dotenv import dotenv_values

config = dotenv_values(".env")

captcha = CaptchaBreaker(config["KEY"])

def test_se_resolve_o_captcha_por_imagem():
    
    result = captcha.image_captcha.solve_and_return_solution("test_image.jpg")
    assert result == "qGphJ"

def test_se_resolve_recaptcha():
    result = captcha.recaptcha.solve_and_return_solution()