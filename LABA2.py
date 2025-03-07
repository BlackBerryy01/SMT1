import time
import hashlib
def generate(alphabet, max_len):

    if max_len <= 0: return

    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len-1):
            yield c + next

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = (input('Введите пароль:', )).upper()
start = time.process_time()
hashermd5 = hashlib.md5(password.encode())
print(hashermd5.hexdigest())
masgen = []
mashash = []

start = time.process_time()

gen = generate(alpha, 5)
for item in gen:
    masgen.append(item)
    hasher = hashlib.md5(item.encode())
    mashash.append(hasher.hexdigest())
finish = time.process_time()


print('Время работы в секундах MD5: ', finish)
for i in range(10000000):
    if mashash[i] == hashermd5.hexdigest():
        print('Пароль найден:', masgen[i])

finish = time.process_time()


print('Время выполнения всего цикла  в секундах: ', finish)

