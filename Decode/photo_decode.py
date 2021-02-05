from PIL import Image
from Encode import uni
import numpy as np

def ps_decode(photo_encode,password):
    I = (Image.open(photo_encode))

    I = np.array(I)

    r = I[:, :, 0]
    g = I[:, :, 1]
    g_sig=g[6, ] % 2
    # Unicode->2->异或->b通道

    b = I[:, :, 2] % 2
    # print(b)
    row_a = len(b)
    col_a = len(b[0])
    code_ex = bin(int(password))
    code_ex = str(code_ex).replace('0b', '').rjust(20, '0')
    s_ini = ''
    s_fin = ''




    for i in range(row_a):

        for j in range(col_a):

            s_ini += str(b[i][j])
            if (len(s_ini) == 20 and s_ini.count('1') <= 0):
                break;
            if (len(s_ini) == 20):
                s_fin += uni.decode(uni.encrypt(s_ini, code_ex))
                s_ini = ''
        if (len(s_ini) == 20 and s_ini.count('1') <= 0):
            break;
    return s_fin


def ps_sif(photo_encode):
    I = (Image.open(photo_encode))
    I = np.array(I)
    g = I[:, :, 1]
    g_sig = g[6,] % 2
    a_list = ''
    for i in range(len(g_sig)):
        a_list += ''.join(str(g_sig[i]))
    sig=uni.decode(a_list)
    return sig