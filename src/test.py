import time, sys, os

m_path = os.path.join(os.getcwd(), 'cubiomespi')
if m_path not in sys.path:
    sys.path.append(m_path)

from cubiomes import *

g = Generator(MCVersion.MC_1_16_1, 1, Dimension.DIM_OVERWORLD)

st = time.time_ns()
l = get_stronghold_pos(g, 3)

print(f'ms: {time.time_ns() - st}')
if (l == [[-220, -1916], [1556, 660], [-1484, 1204]]):
    print('success')
    exit(0)
exit(1)