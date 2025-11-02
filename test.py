import pandas as pd
from objective2 import preprocess_data


def test_preprocess_data():
sample = pd.DataFrame({
'Gender': ['Male', 'Female', None],
'Age Group': ['18-25', '26-35', '18-25'],
'Current Health Conditions': [2, None, 3]
})
cleaned = preprocess_data(sample)
assert cleaned.isna().sum().sum() == 0
assert 'Gender' in cleaned.columns
