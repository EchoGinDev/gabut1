nums = range(1, 100)  # Perbaikan: tanda koma, bukan titik

def is_prima(num):
    if num < 2:  # Perbaikan: angka < 2 bukan bilangan prima
        return False
    for x in range(2, int(num**0.5) + 1):  # Optimasi: cukup sampai akar dari num
        if num % x == 0:
            return False
    return True

prima = list(filter(is_prima, nums))
print(prima)
