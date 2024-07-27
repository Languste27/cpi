from cubiomespi.cubiomes import *
import time
g = Generator(MCVersion.MC_1_16_1, 1, Dimension.DIM_OVERWORLD)

st = time.time_ns()
l = get_stronghold_pos(g, 3)
print(f'ms: {time.time_ns() - st}')
print(l)