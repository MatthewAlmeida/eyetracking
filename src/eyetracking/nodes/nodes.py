import pandas as pd

def convert_OB_to_csv(
    OB:pd.DataFrame
) -> pd.DataFrame:

    return dict(
        OB_csv=OB
    )

def convert_SB_to_csv(
    SB:pd.DataFrame
) -> pd.DataFrame:

    return dict(
        SB_csv=SB
    )