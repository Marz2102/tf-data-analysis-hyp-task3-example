import pandas as pd
import numpy as np

from statsmodels.stats.weightstats import ztest


chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(data) -> bool:
    p = 0.06
    stat, pval  = ztest(data, value=500, alternative='larger')
    return pval < p
