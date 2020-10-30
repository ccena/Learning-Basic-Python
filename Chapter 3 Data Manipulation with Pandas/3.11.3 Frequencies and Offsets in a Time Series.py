# -*- coding: utf-8 -*-
"""
Fundamental to these Pandas time series tools is the concept of a frequency or
date offset. Just as we saw the D (day) and H (hour) codes previously, we can
use such codes to specify any desired frequency spacing.
"""

import pandas as pd
from pandas.tseries.offsets import BDay

print('For a frequency of 2 hours 30 minutes, 2H30T: ')
x = pd.timedelta_range(0, periods=9, freq="2H30T")
print(x); print('')

print('Creating a business day offset:')
print(pd.date_range('2020-10-9', periods=5, freq=BDay()))