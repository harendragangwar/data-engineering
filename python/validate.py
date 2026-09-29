import functools
import pandas as pd

# simple decorator to check df health before processing
def validate_df(req_cols):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(df, *args, **kwargs):
            # check if any required col is missing
            col_errors = [c for c in req_cols if c not in df.columns]
            if col_errors:
                raise ValueError(f"missing cols in input data: {col_errors}")
            
            # alert if columns have missing/null values
            for c in req_cols:
                null_cnt = df[c].isna().sum()
                if null_cnt > 0:
                    print(f"[Warning] column '{c}' has {null_cnt} null rows.")
            
            print("schema check passed. running transformation...")
            return func(df, *args, **kwargs)
        return wrapper
    return decorator

# columns needed for this job
REQUIRED_FIELDS = ["user_id", "signup_date", "country"]

@validate_df(req_cols=REQUIRED_FIELDS)
def clean_user_records(df):
    # normalise country field to uppercase
    df["country"] = df["country"].str.upper()
    return df

# test run
if __name__ == "__main__":
    mock_data = {
        "user_id":,
        "signup_date": ["2026-01-01", "2026-01-02", None], 
        "country": ["usa", "india", "uk"]
    }
    
    input_df = pd.DataFrame(mock_data)
    
    print("starting data load...")
    try:
        out_df = clean_user_records(input_df)
        print("\nprocessed output:")
        print(out_df)
    except Exception as err:
        print(f"pipeline failed: {err}")
