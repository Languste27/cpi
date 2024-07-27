import ctypes, os
from cubiomespi.constants import *

script_dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(f'{script_dir}\\lib\\lib.dll')



class Generator:
    def __init__(self, mc: int, seed: int, dimension: int) -> None:

        self.version = mc
        self.seed = seed
        self.dimension = dimension



def __c(val: int, seed=False):
    if seed:
        return ctypes.c_uint64(val)
    else:
        return ctypes.c_int(val)



def get_structure_pos(structure: Structure, g: Generator, rx: int, rz: int) -> tuple[int, int]:
    cstructure = __c(structure)
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    crx = __c(rx)
    crz = __c(rz)  
    
    lib.INTERFACE_getStructurePos.restype = ctypes.POINTER(ctypes.c_int)
    lib.INTERFACE_getStructurePos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int]
    ptr = lib.INTERFACE_getStructurePos(cstructure, cversion, cseed, crx, crz)
    coords = (ptr[0], ptr[1])
    if coords == (0,0):
        return None
    return coords


def is_viable_structure_pos(structure: Structure, g: Generator, x: int, z: int) -> bool:
    cstructure = __c(structure)
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    cdimension = __c(g.dimension)
    cx = __c(x)
    cz = __c(z)

    lib.INTERFACE_isViableStructurePos.restype = ctypes.c_int
    lib.INTERFACE_isViableStructurePos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    ptr = lib.INTERFACE_isViableStructurePos(cstructure, cversion, cseed, cdimension, cx, cz)
    return ptr == 1


def get_stronghold_pos(g: Generator, count = 3) -> list[tuple[int, int]]:
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    lib.INTERFACE_getStrongholdPos.restype = ctypes.POINTER(ctypes.c_int)
    lib.INTERFACE_getStrongholdPos.argtypes = [ctypes.c_uint64, ctypes.c_int, ctypes.c_int]
    ptr = lib.INTERFACE_getStrongholdPos(cseed, cversion, count)
    sh_locs = [[ptr[2*i], ptr[2*i+1]] for i in range(count)]
    return sh_locs


def get_spawn_pos(g: Generator) -> tuple[int, int]:
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    f = lib.INTERFACE_getSpwan
    f.restype = ctypes.POINTER(ctypes.c_int)
    f.argtypes = [ctypes.c_uint64, ctypes.c_int]
    ptr = f(cseed, cversion)
    loc = (ptr[0], ptr[1])
    return loc


def get_biome_at(g: Generator, x: int, y: int, z: int) -> BiomeID:
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    cdimension = __c(g.dimension)
    cx = __c(x)
    cy = __c(y)
    cz = __c(z)
    f = lib.INTERFACE_getBiomeAt
    f.restype = ctypes.c_int
    f.argtypes = [ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    biome = f(cversion, cseed, cdimension, cx, cy, cz)
    return biome


def get_bastion_variant(g: Generator, x: int, z: int) -> BastionType:
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    cx = __c(x)
    cz = __c(z)
    f = lib.INTERFACE_getBastionVariant
    f.restype = ctypes.c_int
    f.argtypes = [ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int]
    variant = f(cversion, cseed, cx, cz)
    return variant


def find_structure_in_range(g: Generator, structure: Structure, srx: int, srz: int, erx: int, erz: int) -> list[tuple[int,int]]:
    cstructure = __c(structure)
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    cdimension = __c(g.dimension)
    csrx = __c(srx)
    csrz = __c(srz)
    cerx = __c(erx)
    cerz = __c(erz)

    lib.INTERFACE_find_in_range.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
    lib.INTERFACE_find_in_range.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

    ptrarr = lib.INTERFACE_find_in_range(cstructure, cversion, cseed, cdimension, csrx, csrz, cerx, cerz)
    structure_count = ptrarr[0][0]
    structure_array = [(ptrarr[i][0], ptrarr[i][1]) for i in range(1,structure_count)]

    if structure_array == []:
        return None
    return structure_array


def find_closest_structure(g: Generator, structure: Structure, cx: int, cz: int, limit: int) -> tuple[int, int]:
    cstructure = __c(structure)
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    cdimension = __c(g.dimension)
    ccx = __c(cx)
    ccz = __c(cz)
    climit = __c(limit)
    
    f = lib.INTERFACE_find_closest_structure
    f.restype = ctypes.POINTER(ctypes.c_int)
    f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    ptr = f(cstructure, cversion, cseed, cdimension, ccx, ccz, climit)

    coords = (ptr[0], ptr[1])
    if coords == (0,0):
        return None
    return coords