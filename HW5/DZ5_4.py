def rleEncoding(data):
    encode = ""
    var_char = ""
    count = 1
    for char in data:
        if char != var_char:
            if var_char:
                encode += str(count) + var_char
            count = 1
            var_char = char
        else:
            count += 1
    encode += str(count) + var_char
    return encode

def rleDecoding(data):
    decode = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode

print(rleEncoding("GGGGDDAAAAFAAFWWWWWWWWGGGG"))
print(rleDecoding("4G2D4A1F2A1F8W4G"))