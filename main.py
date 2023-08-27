from captcha_breaker import CaptchaBreaker

captcha = CaptchaBreaker(key='01d6c184e20c008008d2c1d6c4f0a17b')
breakpoint()
captcha.image_captcha.resolver("test_image.jpg")