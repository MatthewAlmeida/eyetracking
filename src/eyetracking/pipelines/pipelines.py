from kedro.pipeline import Pipeline, node

from ..nodes import (
    convert_OB_to_csv, convert_SB_to_csv
)

def get_pipeline_convert_excel_to_csv(**kwargs):
    return Pipeline(
        [
            node(
                convert_OB_to_csv,
                ["OB"],
                dict(
                    OB_csv="OB_csv"
                ),
            ),
            node(
                convert_SB_to_csv,
                ["SB"],
                dict(
                    SB_csv="SB_csv"
                ),
            ),
        ]
    )