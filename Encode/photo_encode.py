from . import uni
from PIL import Image
import numpy as np

def ps_hide(photo,information_encode,signature,confirm):
    I = np.array(photo)

    r = I[:, :, 0]
    g = I[:, :, 1]
    g[6, ] = g[6, ] - g[6, ] % 2

    b = I[:, :, 2] - I[:, :, 2] % 2

    row_a = len(r)
    col_a = len(r[0])


    numb=0
    if confirm == 'yes':
        for i in range(col_a):
            if (numb == len(signature)):
                break
            g[6][i]+=int(signature[numb])
            numb+=1

    num = 0
    for i in range(row_a):

        if (num == len(information_encode)):
            break
        for j in range(col_a):
            b[i][j] += int(information_encode[num])
            num += 1
            # print(num)
            if (num == len(information_encode)):
                break
    # print('ok')
    print(b)
    I[:, :, 0] = r
    I[:, :, 1] = g
    I[:, :, 2] = b
    I = Image.fromarray(I)
    return I