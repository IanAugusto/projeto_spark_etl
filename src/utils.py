# utils.py

def clean_data(df, coluna):
    df[coluna] = df[coluna].str.strip().str.title()
    return df