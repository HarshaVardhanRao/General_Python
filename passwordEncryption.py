import random
import string

def gen_password(length=12, complexity='medium'):
    if complexity == 'low':
        chars = string.ascii_letters + string.digits
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        raise ValueError("Invalid complexity level. Choose from 'low', 'medium', or 'high'.")
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

generated_password = gen_password(length=14, complexity='high')
print(generated_password)