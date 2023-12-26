import random
import time

def generate_verification_code():
    verification_code = ''.join(random.choice('0123456789') for _ in range(6))
    return verification_code

def is_code_valid(verification_code, expiration_time):
    current_time = time.time()
    code_creation_time = verification_code.get('creation_time', 0)
    return current_time - code_creation_time <= expiration_time

def get_user_input():
    user_input = input("Şifreyi giriniz: ")
    return user_input

# Kullanım örneği
verification_code = generate_verification_code()
verification_code_data = {
    'code': verification_code,
    'creation_time': time.time()
}
expiration_time = 50

print("Doğrulama kodu:", verification_code)

# Kullanıcıdan şifreyi alın
user_input = get_user_input()

# Şifre kontrolü
if user_input == verification_code_data['code'] and is_code_valid(verification_code_data, expiration_time):
    print("Kod geçerli.")
else:
    print("Kod geçerliliğini yitirdi veya şifre yanlış.")
