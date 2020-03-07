def find_dht_marker_offsets(buffer):
    import re

    d_index = []
    dht_marker = b'\xff\xc4'
    regex = re.compile(dht_marker)

    for reg_obj in regex.finditer(buffer):
        offset = reg_obj.end() - 1
        d_index.append(offset)
        print(d_index)
        print("value at index:{:02X} ".format(buffer[offset]))

if __name__ == "__main__":
    # Read the jpeg file
    with open('cross.jpg', 'rb') as in_file:
            buff = bytearray(in_file.read())

            find_dht_marker_offsets(buff)