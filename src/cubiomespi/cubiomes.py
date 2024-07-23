import ctypes, os, math

script_dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(f'{script_dir}\\lib\\lib.dll')



class Generator:
    def __init__(self, mc: int, seed: int, dimension: int) -> None:

        self.version = mc
        self.seed = seed
        self.dimension = dimension


class Dimension:
    DIM_NETHER = -1
    DIM_OVERWORLD   =    0
    DIM_END         =   +1
    DIM_UNDEF       = 1000


class MCVersion:
    MC_1_0_0 = 3
    MC_1_1_0 = 4
    MC_1_2_5 = 5
    MC_1_3_2 = 6
    MC_1_4_7 = 7
    MC_1_5_2 = 8
    MC_1_6_4 = 9
    MC_1_7_10 =10
    MC_1_8_9 = 11
    MC_1_9_4 = 12
    MC_1_10_2 = 13
    MC_1_11_2 = 14
    MC_1_12_2 = 15
    MC_1_13_2 = 16
    MC_1_14_4 = 17
    MC_1_15_2 = 18
    MC_1_16_1 = 19
    MC_1_16_5 = 20
    MC_1_17_1 = 21
    MC_1_18_2 = 22
    MC_1_19_2 = 23
    MC_1_19   = 24
    MC_1_20 = 25


class Structure:
    _name = "Structure"

    Feature = 0
    Desert_Pyramid = 1
    Jungle_Temple = 2
    Jungle_Pyramid = 2 
    Swamp_Hut = 3
    Igloo = 4
    Village = 5
    Ocean_Ruin = 6
    Shipwreck = 7
    Monument = 8
    Mansion = 9
    Outpost = 10
    Ruined_Portal = 11
    Ruined_Portal_N = 12
    Ancient_City = 13
    Treasure = 14
    Mineshaft = 15
    Desert_Well = 16
    Geode = 17
    Fortress = 18
    Bastion = 19
    End_City = 20
    End_Gateway = 21
    Trail_Ruin = 22
    FEATURE_NUM = 23


class BiomeID:
    _name = "BiomeID"

    none = -1
    ocean = 0
    plains = 1
    desert = 2
    mountains = 3
    extremeHills = 3
    forest = 4
    taiga = 5
    swamp = 6
    swampland = 6
    river = 7
    nether_wastes = 8
    hell = 8
    the_end = 9
    sky = 9
    frozen_ocean = 10
    frozenOcean = 10
    frozen_river = 11
    frozenRiver = 11
    snowy_tundra = 12
    icePlains = 12
    snowy_mountains = 13
    iceMountains = 13
    mushroom_fields = 14
    mushroomIsland = 14
    mushroom_field_shore = 15
    mushroomIslandShore = 15
    beach = 16
    desert_hills = 17
    desertHills = 17
    wooded_hills = 18
    forestHills = 18
    taiga_hills = 19
    taigaHills = 19
    mountain_edge = 20
    extremeHillsEdge = 20
    jungle = 21
    jungle_hills = 22
    jungleHills = 22
    jungle_edge = 23
    jungleEdge = 23
    deep_ocean = 24
    deepOcean = 24
    stone_shore = 25
    stoneBeach = 25
    snowy_beach = 26
    coldBeach = 26
    birch_forest = 27
    birchForest = 27
    birch_forest_hills = 28
    birchForestHills = 28
    dark_forest = 29
    roofedForest = 29
    snowy_taiga = 30
    coldTaiga = 30
    snowy_taiga_hills = 31
    coldTaigaHills = 31
    giant_tree_taiga = 32
    megaTaiga = 32
    giant_tree_taiga_hills = 33
    megaTaigaHills = 33
    wooded_mountains = 34
    extremeHillsPlus = 34
    savanna = 35
    savanna_plateau = 36
    savannaPlateau = 36
    badlands = 37
    mesa = 37
    wooded_badlands_plateau = 38
    mesaPlateau_F = 38
    badlands_plateau = 39
    mesaPlateau = 39
    small_end_islands = 40
    end_midlands = 41
    end_highlands = 42
    end_barrens = 43
    warm_ocean = 44
    warmOcean = 44
    lukewarm_ocean = 45
    lukewarmOcean = 45
    cold_ocean = 46
    coldOcean = 46
    deep_warm_ocean = 47
    warmDeepOcean = 47
    deep_lukewarm_ocean = 48
    lukewarmDeepOcean = 48
    deep_cold_ocean = 49
    coldDeepOcean = 49
    deep_frozen_ocean = 50
    frozenDeepOcean = 50
    seasonal_forest = 51
    rainforest = 52
    shrubland = 53
    the_void = 127
    sunflower_plains = plains + 128
    desert_lakes = desert + 128
    gravelly_mountains = mountains + 128
    flower_forest = forest + 128
    taiga_mountains = taiga + 128
    swamp_hills = swamp + 128
    ice_spikes = snowy_tundra + 128
    modified_jungle = jungle + 128
    modified_jungle_edge = jungle_edge + 128
    tall_birch_forest = birch_forest + 128
    tall_birch_hills = birch_forest_hills + 128
    dark_forest_hills = dark_forest + 128
    snowy_taiga_mountains = snowy_taiga + 128
    giant_spruce_taiga = giant_tree_taiga + 128
    giant_spruce_taiga_hills = giant_tree_taiga_hills + 128
    modified_gravelly_mountains = wooded_mountains + 128
    shattered_savanna = savanna + 128
    shattered_savanna_plateau = savanna_plateau + 128
    eroded_badlands = badlands + 128
    modified_wooded_badlands_plateau = wooded_badlands_plateau + 128
    modified_badlands_plateau = badlands_plateau + 128
    bamboo_jungle = 168
    bamboo_jungle_hills = 169
    soul_sand_valley = 170
    crimson_forest = 171
    warped_forest = 172
    basalt_deltas = 173
    dripstone_caves = 174
    lush_caves = 175
    meadow = 177
    grove = 178
    snowy_slopes = 179
    jagged_peaks = 180
    frozen_peaks = 181
    stony_peaks = 182
    old_growth_birch_forest = tall_birch_forest
    old_growth_pine_taiga = giant_tree_taiga
    old_growth_spruce_taiga = giant_spruce_taiga
    snowy_plains = snowy_tundra
    sparse_jungle = jungle_edge
    stony_shore = stone_shore
    windswept_hills = mountains
    windswept_forest = wooded_mountains
    windswept_gravelly_hills = gravelly_mountains
    windswept_savanna = shattered_savanna
    wooded_badlands = wooded_badlands_plateau
    deep_dark = 183
    mangrove_swamp = 184
    cherry_grove = 185


class BiomeGroups:
    Forests = [
        BiomeID.forest,
        BiomeID.forestHills,
        BiomeID.flower_forest,
        BiomeID.taiga,
        BiomeID.taiga_hills,
        BiomeID.snowy_taiga,
        BiomeID.snowy_taiga_hills,
        BiomeID.birch_forest,
        BiomeID.birch_forest_hills,
        BiomeID.tall_birch_forest,
        BiomeID.tall_birch_hills,
        BiomeID.dark_forest,
        BiomeID.dark_forest_hills
    ]

    Beaches = [
        BiomeID.beach,
        BiomeID.coldBeach,
        BiomeID.snowy_beach
    ]

    DesertBiomes = [
        BiomeID.desert,
        BiomeID.desert_hills,
        BiomeID.desert_lakes,
        BiomeID.desertHills
    ]

    Oceans = [
        BiomeID.ocean,
        BiomeID.frozen_ocean,
        BiomeID.deep_ocean,
        BiomeID.warm_ocean,
        BiomeID.lukewarm_ocean,
        BiomeID.cold_ocean,
        BiomeID.deep_warm_ocean,
        BiomeID.deep_lukewarm_ocean,
        BiomeID.deep_cold_ocean,
        BiomeID.deep_frozen_ocean,
    ]


class BastionType:
    _name = "BastionType"

    HOUSING = 0
    STABLES = 1
    TREASURE = 2
    BRIDGE = 3


class util:
    def distance_between_structures(structure1, structure2):
        xdist = structure2[0] - structure1[0]
        zdist = structure2[1] - structure1[1]
        d = math.sqrt((xdist * xdist) + (zdist*zdist))
        return d

    def distance_from_00(c1):
        return math.sqrt((c1[0] * c1[0]) + (c1[1] * c1[1]))

    def distance_between_points(x1,y1,x2,y2):
        d = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
        return d

    def convert_to_string(constant: int, typee: object):
        """constant: constant thats converted to string
           type: type of constant"""

        typee = typee._name # Scuffed, and sad. But pip module imports did not want to work....
        match typee:
            case "BastionType":
                match constant:
                    case BastionType.HOUSING: return "Housing"
                    case BastionType.STABLES: return "Stables"
                    case BastionType.TREASURE: return "Treasure"
                    case BastionType.BRIDGE: return "Bridge"
                    case _: return f"Unknown Bastion ID: {constant}"

            case "Structure":
                match constant:
                    case Structure.Feature: return "Feature"
                    case Structure.Desert_Pyramid: return "Desert Pyramid"
                    case Structure.Jungle_Temple: return "Jungle Temple"
                    case Structure.Jungle_Pyramid: return "Jungle Pyramid"
                    case Structure.Swamp_Hut: return "Swamp Hut"
                    case Structure.Igloo: return "Igloo"
                    case Structure.Village: return "Village"
                    case Structure.Ocean_Ruin: return "Ocean Ruin"
                    case Structure.Shipwreck: return "Shipwreck"
                    case Structure.Monument: return "Monument"
                    case Structure.Mansion: return "Mansion"
                    case Structure.Outpost: return "Outpost"
                    case Structure.Ruined_Portal: return "Ruined Portal"
                    case Structure.Ruined_Portal_N: return "Ruined Portal N"
                    case Structure.Ancient_City: return "Ancient City"
                    case Structure.Treasure: return "Treasure"
                    case Structure.Mineshaft: return "Mineshaft"
                    case Structure.Desert_Well: return "Desert Well"
                    case Structure.Geode: return "Geode"
                    case Structure.Fortress: return "Fortress"
                    case Structure.Bastion: return "Bastion"
                    case Structure.End_City: return "End City"
                    case Structure.End_Gateway: return "End Gateway"
                    case Structure.Trail_Ruin: return "Trail Ruin"
                    case _: return "Unknown Structure"

            case "BiomeID":
                match constant:
                    case BiomeID.none: return "None"
                    case BiomeID.ocean: return "Ocean"
                    case BiomeID.plains: return "Plains"
                    case BiomeID.desert: return "Desert"
                    case BiomeID.mountains | BiomeID.extremeHills: return "Mountains/Extreme Hills"
                    case BiomeID.forest: return "Forest"
                    case BiomeID.taiga: return "Taiga"
                    case BiomeID.swamp | BiomeID.swampland: return "Swamp/Swampland"
                    case BiomeID.river: return "River"
                    case BiomeID.nether_wastes | BiomeID.hell: return "Nether Wastes/Hell"
                    case BiomeID.the_end | BiomeID.sky: return "The End/Sky"
                    case BiomeID.frozen_ocean | BiomeID.frozenOcean: return "Frozen Ocean"
                    case BiomeID.frozen_river | BiomeID.frozenRiver: return "Frozen River"
                    case BiomeID.snowy_tundra | BiomeID.icePlains: return "Snowy Tundra/Ice Plains"
                    case BiomeID.snowy_mountains | BiomeID.iceMountains: return "Snowy Mountains/Ice Mountains"
                    case BiomeID.mushroom_fields | BiomeID.mushroomIsland: return "Mushroom Fields/Mushroom Island"
                    case BiomeID.mushroom_field_shore | BiomeID.mushroomIslandShore: return "Mushroom Field Shore/Mushroom Island Shore"
                    case BiomeID.beach: return "Beach"
                    case BiomeID.desert_hills | BiomeID.desertHills: return "Desert Hills"
                    case BiomeID.wooded_hills | BiomeID.forestHills: return "Wooded Hills/Forest Hills"
                    case BiomeID.taiga_hills | BiomeID.taigaHills: return "Taiga Hills"
                    case BiomeID.mountain_edge | BiomeID.extremeHillsEdge: return "Mountain Edge/Extreme Hills Edge"
                    case BiomeID.jungle: return "Jungle"
                    case BiomeID.jungle_hills | BiomeID.jungleHills: return "Jungle Hills"
                    case BiomeID.jungle_edge | BiomeID.jungleEdge: return "Jungle Edge"
                    case BiomeID.deep_ocean | BiomeID.deepOcean: return "Deep Ocean"
                    case BiomeID.stone_shore | BiomeID.stoneBeach: return "Stone Shore"
                    case BiomeID.snowy_beach | BiomeID.coldBeach: return "Snowy Beach"
                    case BiomeID.birch_forest | BiomeID.birchForest: return "Birch Forest"
                    case BiomeID.birch_forest_hills | BiomeID.birchForestHills: return "Birch Forest Hills"
                    case BiomeID.dark_forest | BiomeID.roofedForest: return "Dark Forest/Roofed Forest"
                    case BiomeID.snowy_taiga | BiomeID.coldTaiga: return "Snowy Taiga/Cold Taiga"
                    case BiomeID.snowy_taiga_hills | BiomeID.coldTaigaHills: return "Snowy Taiga Hills/Cold Taiga Hills"
                    case BiomeID.giant_tree_taiga | BiomeID.megaTaiga: return "Giant Tree Taiga/Mega Taiga"
                    case BiomeID.giant_tree_taiga_hills | BiomeID.megaTaigaHills: return "Giant Tree Taiga Hills/Mega Taiga Hills"
                    case BiomeID.wooded_mountains | BiomeID.extremeHillsPlus: return "Wooded Mountains/Extreme Hills Plus"
                    case BiomeID.savanna: return "Savanna"
                    case BiomeID.savanna_plateau | BiomeID.savannaPlateau: return "Savanna Plateau"
                    case BiomeID.badlands | BiomeID.mesa: return "Badlands/Mesa"
                    case BiomeID.wooded_badlands_plateau | BiomeID.mesaPlateau_F: return "Wooded Badlands Plateau/Mesa Plateau F"
                    case BiomeID.badlands_plateau | BiomeID.mesaPlateau: return "Badlands Plateau/Mesa Plateau"
                    case BiomeID.small_end_islands: return "Small End Islands"
                    case BiomeID.end_midlands: return "End Midlands"
                    case BiomeID.end_highlands: return "End Highlands"
                    case BiomeID.end_barrens: return "End Barrens"
                    case BiomeID.warm_ocean | BiomeID.warmOcean: return "Warm Ocean"
                    case BiomeID.lukewarm_ocean | BiomeID.lukewarmOcean: return "Lukewarm Ocean"
                    case BiomeID.cold_ocean | BiomeID.coldOcean: return "Cold Ocean"
                    case BiomeID.deep_warm_ocean | BiomeID.warmDeepOcean: return "Deep Warm Ocean"
                    case BiomeID.deep_lukewarm_ocean | BiomeID.lukewarmDeepOcean: return "Deep Lukewarm Ocean"
                    case BiomeID.deep_cold_ocean | BiomeID.coldDeepOcean: return "Deep Cold Ocean"
                    case BiomeID.deep_frozen_ocean | BiomeID.frozenDeepOcean: return "Deep Frozen Ocean"
                    case BiomeID.the_void: return "The Void"
                    case _: return f"Unknown Biome ID: {constant}"
        

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


def get_stronghold_pos(g: Generator, count) -> list[tuple[int, int]]:
    cversion = __c(g.version)
    cseed = __c(g.seed, True)
    lib.INTERFACE_getStrongholdPos.restype = ctypes.POINTER(ctypes.c_int)
    lib.INTERFACE_getStrongholdPos.argtypes = [ctypes.c_uint64, ctypes.c_int]
    ptr = lib.INTERFACE_getStrongholdPos(cseed, cversion)
    sh_locs = [[ptr[2*i], ptr[2*i+1]] for i in range(128)]
    return sh_locs[:count]


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