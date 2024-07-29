def convert_decimal_fractional_to_binary(fract_part: float, precision=23) -> str:
    if int(fract_part) >= 1:
        raise ValueError(f"The fractional number must be lower 1!")

    binary_fractional = ''
    while precision > 0:
        fract_part *= 2
        if fract_part >= 1:
            binary_fractional += '1'
            fract_part -= 1
        else:
            binary_fractional += '0'
        precision -= 1

    return binary_fractional


def convert_float_to_binary(number: float, precision=23, size_bit=32) -> str:
    # 1. convert sign to binary '0' or '1'
    sign = '0' if number >= 0 else '1'
    number = abs(number)

    # divide number into integer and fractional parts
    integer_part = int(number)
    fractional_part = number - integer_part

    # 2. convert decimal integer part to binary_integer
    binary_integer = bin(integer_part)[2:]  # remove prefix '0b'

    # 3. convert decimal fractional part to binary_fractional
    binary_fractional = convert_decimal_fractional_to_binary(
        fractional_part, precision=precision
    )

    # 4. normalization
    # смещение экспоненты 127 для 32-bit и 1023 для 64-bit
    exp_offset = 127 if size_bit == 32 else 1023
    exp_width = 8 if size_bit == 32 else 11
    exp = len(binary_integer) - 1 + exp_offset
    exp_bin = bin(exp)[2:]
    exp_binary = f"{exp_bin:0>{exp_width}}"

    total_bin = sign + exp_binary + binary_integer[1:] + binary_fractional
    total_bin = total_bin[:size_bit]

    return total_bin

if __name__ == '__main__':
    print(convert_float_to_binary(0.4))
    print(convert_decimal_fractional_to_binary(0.4))


