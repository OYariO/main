# Оптимізована реалізація P-блоку: пряме та зворотне перетворення

# Таблиця перестановок (1-based позиції)
P_BOX = [2, 4, 3, 1]

# Зворотна таблиця перестановок
P_BOX_INV = [0] * len(P_BOX)
for i, pos in enumerate(P_BOX):
    P_BOX_INV[pos - 1] = i

def p_block_direct(input_bits):
    """Пряме перетворення P-блоку."""
    output = 0
    for i, pos in enumerate(P_BOX):
        output |= ((input_bits >> (len(P_BOX) - pos)) & 1) << (len(P_BOX) - 1 - i)
    return output

def p_block_inverse(output_bits):
    """Зворотне перетворення P-блоку."""
    input_bits = 0
    for i, pos in enumerate(P_BOX_INV):
        input_bits |= ((output_bits >> (len(P_BOX) - 1 - i)) & 1) << (len(P_BOX) - 1 - pos)
    return input_bits

# Тестування
if __name__ == "__main__":
    test_input = 0b1101
    output = p_block_direct(test_input)
    recovered = p_block_inverse(output)
    print(f"Input: {bin(test_input)} -> P-Block: {bin(output)} -> Inverse: {bin(recovered)}")
