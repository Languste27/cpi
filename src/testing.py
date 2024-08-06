import time, sys, os

m_path = os.path.join(os.getcwd(), 'cubiomespi')
if m_path not in sys.path:
    sys.path.append(m_path)

from cubiomes import *
from util import *

g = Generator(MCVersion.MC_1_16_1, 1947107924086177303, Dimension.DIM_NETHER)
yo = find_closest_structure(g, Structure.Bastion.id, 0, 0, 10)
print(yo)
print(get_bastion_variant(g, yo[0],yo[1]))
print(BastionVariant_toString(get_bastion_variant(g, yo[0],yo[1])))
# print(get_end_y_height(g, 100, 0))

