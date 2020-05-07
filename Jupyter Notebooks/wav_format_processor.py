#WAVE no permite utilizar archivos con una frecuencia de sampleo >48kHz
#Scipy.io.wavfile no trabaja con 24 bits.

import struct

class WavFormatProcessor():
    
    def wav_file_properties(self, filename):

        wave_file = open(filename, "rb")
        
        # subchunk del archivo que especifica el formato = fmt.
        fmt = wave_file.read(36)  # levanto los primeros 36 bytes del archivo

        number_channels_string = fmt[22:24] # el numero de canales esta en los bytes 22 y 23 del subchunk fmt.
        # print (number_channels_string)
        number_channels = struct.unpack("<H", number_channels_string)[0]
        # print(number_channels)

        sample_rate_string = fmt[24:28]  # la frecuencia de sampleo esta en los bytes 24, 25, 26 y 27 del subchunk fmt.
        # print (sample_rate_string)
        sample_rate = struct.unpack("<I", sample_rate_string)[0]
        # print (sample_rate)

        bit_depth_string = fmt[34:36]  # la profundidad de bits esta en los bytes 34 y 35 del subchunk fmt.
        # print (bit_depth_string)
        bit_depth = struct.unpack("<H", bit_depth_string)[0]
        # print (bit_depth)

        return (number_channels, sample_rate, bit_depth)