import pandas as pd

import client

fitbit_client = client.get_client()

oneDate = pd.datetime(year = 2021, month = 6, day = 18)
fitbit_client.heart(oneDate)