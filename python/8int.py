def extract_bit_field(value, start_bit, end_bit):
    mask = (1 << (start_bit - end_bit + 1)) - 1
    return (value >> end_bit) & mask

def decode_fields(number):
    fields = [
        ('V6', extract_bit_field(number, 32, 29)),
        ('V5', extract_bit_field(number, 28, 19)),
        ('V4', extract_bit_field(number, 18, 17)),
        ('V3', extract_bit_field(number, 16, 10)),
        ('V2', extract_bit_field(number, 9, 7)),
    ]
    return [(name, str(value)) for name, value in fields]

# Примеры тестов
print(decode_fields(8121689593))  # [('V2', '6'), ('V3', '73'), ('V4', '3'), ('V5', '130'), ('V6', '15')]
print(decode_fields(417850151))   # [('V2', '6'), ('V3', '120'), ('V4', '3'), ('V5', '796'), ('V6', '0')]
print(decode_fields(356138858))   # [('V2', '6'), ('V3', '15'), ('V4', '1'), ('V5', '679'), ('V6', '0')]
print(decode_fields(3628808986))  # [('V2', '6'), ('V3', '78'), ('V4', '1'), ('V5', '777'), ('V6', '6')]
