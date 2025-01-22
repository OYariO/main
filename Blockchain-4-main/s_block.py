# Оптимізована реалізація S-блоку: пряме та зворотне перетворення

# Таблиця заміни (масив замість словника)
S_BOX = [
    0b1110, 0b0100, 0b1101, 0b0001, 0b0010, 0b1111, 0b1011, 0b1000,
    0b0011, 0b1010, 0b0110, 0b1100, 0b0101, 0b1001, 0b0000, 0b0111
]

# Зворотна таблиця заміни (генерується автоматично)
S_BOX_INV = [0] * 16
for i, v in enumerate(S_BOX):
    S_BOX_INV[v] = i

def s_block_direct(input_bits):
    """Пряме перетворення S-блоку."""
    return S_BOX[input_bits & 0xF]  # Маска для обмеження 4-бітного вводу

def s_block_inverse(output_bits):
    """Зворотне перетворення S-блоку."""
    return S_BOX_INV[output_bits & 0xF]

# Тестування
if __name__ == "__main__":
    test_input = 0b0010
    output = s_block_direct(test_input)
    recovered = s_block_inverse(output)
    print(f"Input: {bin(test_input)} -> S-Block: {bin(output)} -> Inverse: {bin(recovered)}")
