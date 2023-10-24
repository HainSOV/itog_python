import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем новые столбцы для каждой категории
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

# Удаляем исходный столбец 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()
