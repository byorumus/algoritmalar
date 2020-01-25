import math


def question2_all(number):
    toplam=0
    #Sayıyının kucuk asal sayılarını bul
    asallar= all_primes(number)
    if len(asallar)==0:
        return False
    #Asal sayıları topla
    for i in range(len(asallar)):
        toplam= toplam + asallar[i]
    #Bu toplam verilen sayıya eşitse True değilse False
    if toplam==number:
        return True
    else:
        return False


def question2_any(number):
    return True


def all_primes(number):
    # return list(filter(is_prime, range(2, number)))
    rv = []

    for i in range(2, number):
        if is_prime(i):
            rv.append(i)

    return rv


def is_prime(number):
    if number == 1:
        return False

    s = int(math.sqrt(number)) + 1

    for i in range(2, s):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    for i in range(100):
        if question2_all(i):
            print(i)

