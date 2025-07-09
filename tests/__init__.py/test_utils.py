from utils import log_to_csv
import pandas as pd

def test_log_to_csv_creates_file(temp_file_pth):
    #create tempporary file path
    filepth = temp_file_pth / "test_log.csv"
    #create test data
    test_data = {"temperature": 24.0, "humidity": 49.0}
    #call log_to_csv
    log_to_csv(filepth, test_data)
    #create dataframe
    df = pd.read_csv(filepth)
    #use assertions to check rows
    assert not df.empty
    assert "temperature" in df.columns
    assert "humidity" in df.columns
    assert "timestamp" in df.columns
