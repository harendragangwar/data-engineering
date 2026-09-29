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
