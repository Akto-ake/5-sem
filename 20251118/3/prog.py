import sys, struct

s_in = sys.stdin.buffer.read()

if len(s_in) < 44:
    print('NO here')
    exit()
elif s_in[0:4] != b"RIFF" or \
        s_in[8:12] != b"WAVE" or \
        s_in[12:16] != b"fmt ":
    print("NO")
    exit()

# RIFF, size, WAV, FMT, LN, type_format, num_ch, sample_r, SBC, BC, bits_s, D, file_s_data = struct.unpack('<4sI4s4sIHHIIHH4sI', s_in[:44])
_, size, _, _, _, type_format, num_ch, sample_r, _, _, bits_s, _, file_s_data = struct.unpack('<4sI4s4sIHHIIHH4sI', s_in[:44])

print(f'Size={size}, Type={type_format}, Channels={num_ch}, Rate={sample_r}, Bits={bits_s}, Data size={file_s_data}')