#4
from datetime import datetime
def difference(d1 , d2):
    result = d2-d1
    return result.total_seconds()
d1 = datetime(2024 , 12 , 30 , 1 , 1 , 1 , 1)
d2 = datetime(2025 , 2 , 21 , 1 , 1 , 1)
print(difference(d1 , d2))