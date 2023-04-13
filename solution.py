import pandas as pd
import numpy as np

from scipy.stats import ttest_1samp


chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(data) -> bool:
    E = 500
    t_stat, p_value = ttest_1samp(data, E)
    p = 0.06
    if p_value/2 < p and t_stat < 0:
        return True
    else:
        return False
