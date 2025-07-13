import pandas as pd

def load_tasks():
    return pd.read_csv("tasks.csv")

def get_pending_tasks_by_mode(mode):
    df = load_tasks()
    return df[(df['status'] == 'pending') & (df['mode'] == mode)]

def get_random_task(mode="Do"):
    tasks = get_pending_tasks_by_mode(mode)
    if not tasks.empty:
        return tasks.sample(1).iloc[0].to_dict()
    return None
