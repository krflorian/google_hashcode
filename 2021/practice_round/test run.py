# %%
import time

#%%
start1 = time.time()
!python3 practice.py
end1 = time.time()
# %%
start2 = time.time()
!python3 practice_m.py
end2 = time.time()
# %%
print(f'single-core execution time {end1 - start1}')
print(f'multi-core execution time {end2 - start2}')
# %%


