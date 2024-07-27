import time, sys, os

m_path = os.path.join(os.getcwd(), 'cubiomespi')
if m_path not in sys.path:
    sys.path.append(m_path)

from cubiomes import *

g = Generator(MCVersion.MC_1_16_1, 1, Dimension.DIM_END)

print(get_end_y_height(g, 33, -25))

