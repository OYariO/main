import random

# Генерація S-блоку та зворотного S-блоку
def generate_s_box(size):
    """Генерує випадкову таблицю заміни для S-блоку заданого розміру."""
    values = list(range(size))
    random.shuffle(values)
    s_box = {i: values[i] for i in range(size)}
    reverse_s_box = {v: k for k, v in s_box.items()}
    return s_box, reverse_s_box

# Пряме перетворення через S-блок
def s_box_transform(data, s_box):
    """Пряме перетворення через S-блок."""
    high_nibble = (data >> 4) & 0b1111  # Старші 4 біти
    low_nibble = data & 0b1111         # Молодші 4 біти
    return (s_box[high_nibble] << 4) | s_box[low_nibble]

# Зворотне перетворення через S-блок
def s_box_reverse_transform(data, reverse_s_box):
    """Зворотне перетворення через S-блок."""
    high_nibble = (data >> 4) & 0b1111
    low_nibble = data & 0b1111
    return (reverse_s_box[high_nibble] << 4) | reverse_s_box[low_nibble]

# Генерація P-блоку (перестановки)
def generate_p_box_permutation(size):
    """Генерує випадкову перестановку для P-блоку заданого розміру."""
    permutation = list(range(size))
    random.shuffle(permutation)
    return permutation

# Пряме перетворення через P-блок
def p_box_permute(data, permutation):
    """Пряме перетворення через P-блок."""
    result = 0
    for i, bit_position in enumerate(permutation):
        bit = (data >> (len(permutation) - 1 - bit_position)) & 1
        result |= bit << (len(permutation) - 1 - i)
    return result

# Тестування S-блоку та P-блоку
if __name__ == "__main__":
    # Генерація S-блоку
    s_box, reverse_s_box = generate_s_box(16)
    print("S-Box:", s_box)
    print("Reverse S-Box:", reverse_s_box)

    # Тестові дані для S-блоку
    original_data = 0b10101100
    encrypted_data = s_box_transform(original_data, s_box)
    decrypted_data = s_box_reverse_transform(encrypted_data, reverse_s_box)

    print(f"Оригінальні дані: {bin(original_data)}")
    print(f"Зашифровані дані: {bin(encrypted_data)}")
    print(f"Розшифровані дані: {bin(decrypted_data)}\n")

    # Генерація P-блоку
    p_box = generate_p_box_permutation(8)
    print("P-Box перестановка:", p_box)

    # Тестові дані для P-блоку
    original_p_data = 0b11001101
    permuted_data = p_box_permute(original_p_data, p_box)

    print(f"Оригінальні P-дані: {bin(original_p_data)}")
    print(f"Переставлені P-дані: {bin(permuted_data)}")
