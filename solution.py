import pandas as pd
import numpy as np


chat_id = 515069313 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = anderson_ksamp([x, y])
    return res.pvalue < 0.09 # Ваш ответ, True или False
