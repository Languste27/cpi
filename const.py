from enum import IntEnum


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
    Feature = 0  # for locations of temple generation attempts pre 1.13
    Desert_Pyramid = 1
    Jungle_Temple = 2
    Jungle_Pyramid = 2  # Jungle_Pyramid is the same as Jungle_Temple
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
    FEATURE_NUM = 23  # Assuming FEATURE_NUM is used to indicate the total number


class BiomeID:
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
    HOUSING = 0
    STABLES = 1
    TREASURE = 2
    BRIDGE = 3