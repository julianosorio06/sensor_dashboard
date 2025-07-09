from datetime import datetime
import pandas as pd
import os

def log_to_csv(filepath, data_dict):
    row = {"timestamp": datetime.now(), **data_dict}
    df = pd.DataFrame([row])
    df.to_csv(filepath, mode="a", header=not os.path.exists(filepath), index=False)