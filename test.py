from tqdm import tqdm
from impl import MyFormatter
import time

for x in tqdm(range(30), bar_format=MyFormatter(), ascii=True):
    time.sleep(0.5)
