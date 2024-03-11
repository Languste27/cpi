from generator import Generator
from const import MCVersion, BiomeID, Structure, Dimension, BastionType
import util
import ctypes, os, sys
import math

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.argv[0])
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))


def c(val: int, seed=False):
    if seed:
        return ctypes.c_uint64(val)
    else:
        return ctypes.c_int(val)


lib = ctypes.CDLL(f'{script_dir}\\lib\\lib.dll')


def get_structure_pos(structure: Structure, g: Generator, rx: int, rz: int) -> list:
    cstructure = c(structure)
    cversion = c(g.version)
    cseed = c(g.seed, True)
    crx = c(rx)
    crz = c(rz)  
    
    lib.INTERFACE_getStructurePos.restype = ctypes.POINTER(ctypes.c_int)
    lib.INTERFACE_getStructurePos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int]
    ptr = lib.INTERFACE_getStructurePos(cstructure, cversion, cseed, crx, crz)
    coords = (ptr[0], ptr[1])
    if coords == (0,0):
        return None
    # print(coords)
    return coords


def is_viable_structure_pos(structure: Structure, g: Generator, x: int, z: int) -> bool:
    cstructure = c(structure)
    cversion = c(g.version)
    cseed = c(g.seed, True)
    cdimension = c(g.dimension)
    cx = c(x)
    cz = c(z)

    lib.INTERFACE_isViableStructurePos.restype = ctypes.c_int
    lib.INTERFACE_isViableStructurePos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    ptr = lib.INTERFACE_isViableStructurePos(cstructure, cversion, cseed, cdimension, cx, cz)
    return ptr == 1




def get_stronghold_pos(g: Generator, count) -> list:
    cversion = c(g.version)
    cseed = c(g.seed, True)
    lib.INTERFACE_getStrongholdPos.restype = ctypes.POINTER(ctypes.c_int)
    lib.INTERFACE_getStrongholdPos.argtypes = [ctypes.c_uint64, ctypes.c_int]
    ptr = lib.INTERFACE_getStrongholdPos(cseed, cversion)
    sh_locs = [[ptr[2*i], ptr[2*i+1]] for i in range(128)]
    return sh_locs[:count]


def get_spawn_pos(g: Generator) -> tuple:
    cversion = c(g.version)
    cseed = c(g.seed, True)
    f = lib.INTERFACE_getSpwan
    f.restype = ctypes.POINTER(ctypes.c_int)
    f.argtypes = [ctypes.c_uint64, ctypes.c_int]
    ptr = f(cseed, cversion)
    loc = (ptr[0], ptr[1])
    return loc


def get_biome_at(g: Generator, x: int, y: int, z: int) -> BiomeID:
    cversion = c(g.version)
    cseed = c(g.seed, True)
    cdimension = c(g.dimension)
    cx = c(x)
    cy = c(y)
    cz = c(z)
    f = lib.INTERFACE_getBiomeAt
    f.restype = ctypes.c_int
    f.argtypes = [ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    biome = f(cversion, cseed, cdimension, cx, cy, cz)
    return biome


def get_bastion_variant(g: Generator, structure: Structure, x: int, z: int) -> BastionType:
    cversion = c(g.version)
    cseed = c(g.seed, True)
    cx = c(x)
    cz = c(z)
    f = lib.INTERFACE_getBastionVariant
    f.restype = ctypes.c_int
    f.argtypes = [ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int]
    variant = f(cversion, cseed, cx, cz)
    return variant


def sort_by_dist(arr: list):
    return math.sqrt(arr[0]**2 + arr[1]**2)



# for i in range(1, 100000):
#     # print(i)
#     # i = -3604265396460847324
#     g = Generator(MCVersion.MC_1_16_1, i, Dimension.DIM_NETHER)

#     bastions = []
#     fortresses = []

#     for x in range(-1,1):
#         for z in range(-1,1):
#             bastion = get_structure_pos(Structure.Bastion, g, x, z)
#             fortress = get_structure_pos(Structure.Fortress, g, x, z)

#             if (bastion != None):
#                 bx, bz = bastion
#                 if (is_viable_structure_pos(Structure.Bastion, g, bx, bz)):
#                     bastions.append([bx,bz])

#             if (fortress != None):
#                 fx, fz = fortress
#                 if (is_viable_structure_pos(Structure.Fortress, g, fx,fz)):
#                     fortresses.append([fx,fz])

#     if (bastions == [] or fortresses == []):
#         continue
#     bastions.sort(key=sort_by_dist)
#     fortresses.sort(key=sort_by_dist)

#     # print(pythagoras(bastions[0], fortresses[0]), bastions[0], fortresses[0], i)
#     if pythagoras(bastions[0], [0,0]) < 100:
#         if pythagoras(bastions[0], fortresses[0]) < 100:
#             print(i, bastions[0])
    

    

    # print(bastions, fortresses)

bts = []
for i in range(1000):
    g = Generator(MCVersion.MC_1_16_1, i, Dimension.DIM_OVERWORLD)
    sx, sz = get_spawn_pos(g)
    csx, csz = sx // 16, sz // 16 # convert spawn coords to chunk coords
    
    for cx in range(csx-3, csx+3):
        for cz in range(csz-3, csz+3):
            bt = get_structure_pos(Structure.Treasure, g, cx, cz)
            if bt != None:
                x, y = bt
                if is_viable_structure_pos(Structure.Treasure, g, x,y):
                    bts.append([i, (x,y)])
                    print([i, (x,y)])
                    break
                break



print(bts)