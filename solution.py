import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 484112867# Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    return anderson_ksamp([x, y]).pvalue < alpha
