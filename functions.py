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


def get_structure_pos(structure: Structure, g: Generator, rx: int, rz: int) -> tuple:
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

def find_in_range(g: Generator, structure: Structure, x: int, z:int, radius: int) -> list[tuple[int,int]]:
    res = []
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            struct = get_structure_pos(structure, g, i, j)
            if struct:
                x, z = struct
                if is_viable_structure_pos(structure, g, x, z):
                    res.append(struct)
    return res