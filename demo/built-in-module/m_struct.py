
import struct


def bmp_info(file_path):
    with open(file_path, 'rb') as f:
        result = struct.unpack('<ccIIIIIIHH', f.read(30))
        if result[0] + result[1] == b'BM':
            return {
                'width': result[6],
                'height': result[7],
                'color': result[9]
            }
        else:
            return "not a bmp file"

