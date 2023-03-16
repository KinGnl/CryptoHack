a = 66528
b = 52920

def get_the_divisors(number):
    a = number
    d_a = []
    i = 2
    while (i):
        if (a == 1):
            break
        if (a%i == 0):
            d_a.append(i)
            a = int(a/i)
            i = 2
        else:
            i += 1
    return (d_a)

def get_the_primes(d_a):
    p_a = []
    map_numbers = {}

    for d in d_a:
        if (d_a.count(d) != 0 and (d in p_a) == False):
            map_numbers[d] = d_a.count(d)
    return (map_numbers)

def determine_gcd(a, b):
    d_a = get_the_divisors(a)
    d_b = get_the_divisors(b)
    m_a = get_the_primes(d_a)
    m_b = get_the_primes(d_b)
    pgd = 1

    if (len(m_a.keys()) < len(m_b.keys())):
        for k in m_a.keys():
            if ((k in m_b.keys()) == True):
                if (m_a[k] >= m_b[k]):
                    pgd += k ** m_b[k]
                else:
                    pgd += k ** m_a[k]
    else:
        for k in m_b.keys():
            if ((k in m_a.keys()) == True):
                if (m_b[k] >= m_a[k]):
                    pgd *= k ** m_a[k]
                else:
                    pgd *= k ** m_b[k]
    return (pgd)

determine_gcd(a, b)
