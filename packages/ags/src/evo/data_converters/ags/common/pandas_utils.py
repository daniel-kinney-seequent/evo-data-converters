import numpy as np
import pandas as pd

import evo.logging


logger = evo.logging.getLogger("data_converters")


def coerce_to_numeric(series: pd.Series) -> pd.Series:
    try:
        numeric = pd.to_numeric(series)
    except ValueError:
        logger.warning(f"Non-numeric values found when converting series `{series.name}` to numeric; coercing errors to NaN.")
        numeric = pd.to_numeric(series, errors="coerce")
    return numeric
