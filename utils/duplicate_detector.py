import pandas as pd

def detect_duplicates(patients):

    duplicate_groups = []

    # 🔥 Rule 1: Same ghost_id
    ghost_groups = patients.groupby('ghost_id')

    for ghost_id, group in ghost_groups:
        if len(group) > 1:
            group = group.copy()
            group['duplicate_reason'] = "Same Ghost ID"
            duplicate_groups.append(group)

    # 🔥 Rule 2: Same parity_group + similar age
    patients_sorted = patients.sort_values(by=['parity_group', 'age'])

    temp_group = []
    for i in range(len(patients_sorted) - 1):
        curr = patients_sorted.iloc[i]
        next_row = patients_sorted.iloc[i + 1]

        if (
            curr['parity_group'] == next_row['parity_group'] and
            abs(curr['age'] - next_row['age']) <= 2
        ):
            temp_group.append(curr)
            temp_group.append(next_row)

    if temp_group:
        df = pd.DataFrame(temp_group).drop_duplicates()
        df['duplicate_reason'] = "Same Parity + Similar Age"
        duplicate_groups.append(df)

    if duplicate_groups:
        return pd.concat(duplicate_groups)
    else:
        return pd.DataFrame()