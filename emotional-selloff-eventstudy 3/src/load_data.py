import pandas as pd
from .config import PRICES_DIR, BENCHMARK_PATH, EVENTS_PATH

def load_prices():
    dfs = [pd.read_csv(p, parse_dates=['timestamp']) for p in PRICES_DIR.glob('*.csv')]
    return pd.concat(dfs).sort_values(['ticker','timestamp'])

def load_benchmark():
    return pd.read_csv(BENCHMARK_PATH, parse_dates=['timestamp']).sort_values('timestamp')

def load_events():
    return pd.read_csv(EVENTS_PATH, parse_dates=['timestamp']).sort_values(['ticker','timestamp'])
