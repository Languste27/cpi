class _constant:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


class Dimension:
    DIM_NETHER = -1
    DIM_OVERWORLD = 0
    DIM_END = 1
    DIM_UNDEF = 1000


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
    Feature = _constant(0, "Feature")
    Desert_Pyramid = _constant(1, "Desert Pyramid")
    Jungle_Temple = _constant(2, "Jungle Temple")
    Jungle_Pyramid = _constant(2, "Jungle Pyramid")
    Swamp_Hut = _constant(3, "Swamp Hut")
    Igloo = _constant(4, "Igloo")
    Village = _constant(5, "Village")
    Ocean_Ruin = _constant(6, "Ocean Ruin")
    Shipwreck = _constant(7, "Shipwreck")
    Monument = _constant(8, "Monument")
    Mansion = _constant(9, "Mansion")
    Outpost = _constant(10, "Outpost")
    Ruined_Portal = _constant(11, "Ruined Portal")
    Ruined_Portal_N = _constant(12, "Ruined Portal N")
    Ancient_City = _constant(13, "Ancient City")
    Treasure = _constant(14, "Treasure")
    Mineshaft = _constant(15, "Mineshaft")
    Desert_Well = _constant(16, "Desert Well")
    Geode = _constant(17, "Geode")
    Fortress = _constant(18, "Fortress")
    Bastion = _constant(19, "Bastion")
    End_City = _constant(20, "End City")
    End_Gateway = _constant(21, "End Gateway")
    Trail_Ruin = _constant(22, "Trail Ruin")
    FEATURE_NUM = _constant(23, "FEATURE_NUM")


class BiomeID:
    none = _constant(-1, "None")
    ocean = _constant(0, "Ocean")
    plains = _constant(1, "Plains")
    desert = _constant(2, "Desert")
    mountains = _constant(3, "Mountains")
    extremeHills = _constant(3, "Extreme Hills")
    forest = _constant(4, "Forest")
    taiga = _constant(5, "Taiga")
    swamp = _constant(6, "Swamp")
    swampland = _constant(6, "Swampland")
    river = _constant(7, "River")
    nether_wastes = _constant(8, "Nether Wastes")
    hell = _constant(8, "Hell")
    the_end = _constant(9, "The End")
    sky = _constant(9, "Sky")
    frozen_ocean = _constant(10, "Frozen Ocean")
    frozenOcean = _constant(10, "Frozen Ocean")
    frozen_river = _constant(11, "Frozen River")
    frozenRiver = _constant(11, "Frozen River")
    snowy_tundra = _constant(12, "Snowy Tundra")
    icePlains = _constant(12, "Ice Plains")
    snowy_mountains = _constant(13, "Snowy Mountains")
    iceMountains = _constant(13, "Ice Mountains")
    mushroom_fields = _constant(14, "Mushroom Fields")
    mushroomIsland = _constant(14, "Mushroom Island")
    mushroom_field_shore = _constant(15, "Mushroom Field Shore")
    mushroomIslandShore = _constant(15, "Mushroom Island Shore")
    beach = _constant(16, "Beach")
    desert_hills = _constant(17, "Desert Hills")
    desertHills = _constant(17, "Desert Hills")
    wooded_hills = _constant(18, "Wooded Hills")
    forestHills = _constant(18, "Forest Hills")
    taiga_hills = _constant(19, "Taiga Hills")
    taigaHills = _constant(19, "Taiga Hills")
    mountain_edge = _constant(20, "Mountain Edge")
    extremeHillsEdge = _constant(20, "Extreme Hills Edge")
    jungle = _constant(21, "Jungle")
    jungle_hills = _constant(22, "Jungle Hills")
    jungleHills = _constant(22, "Jungle Hills")
    jungle_edge = _constant(23, "Jungle Edge")
    jungleEdge = _constant(23, "Jungle Edge")
    deep_ocean = _constant(24, "Deep Ocean")
    deepOcean = _constant(24, "Deep Ocean")
    stone_shore = _constant(25, "Stone Shore")
    stoneBeach = _constant(25, "Stone Beach")
    snowy_beach = _constant(26, "Snowy Beach")
    coldBeach = _constant(26, "Cold Beach")
    birch_forest = _constant(27, "Birch Forest")
    birchForest = _constant(27, "Birch Forest")
    birch_forest_hills = _constant(28, "Birch Forest Hills")
    birchForestHills = _constant(28, "Birch Forest Hills")
    dark_forest = _constant(29, "Dark Forest")
    roofedForest = _constant(29, "Roofed Forest")
    snowy_taiga = _constant(30, "Snowy Taiga")
    coldTaiga = _constant(30, "Cold Taiga")
    snowy_taiga_hills = _constant(31, "Snowy Taiga Hills")
    coldTaigaHills = _constant(31, "Cold Taiga Hills")
    giant_tree_taiga = _constant(32, "Giant Tree Taiga")
    megaTaiga = _constant(32, "Mega Taiga")
    giant_tree_taiga_hills = _constant(33, "Giant Tree Taiga Hills")
    megaTaigaHills = _constant(33, "Mega Taiga Hills")
    wooded_mountains = _constant(34, "Wooded Mountains")
    extremeHillsPlus = _constant(34, "Extreme Hills Plus")
    savanna = _constant(35, "Savanna")
    savanna_plateau = _constant(36, "Savanna Plateau")
    savannaPlateau = _constant(36, "Savanna Plateau")
    badlands = _constant(37, "Badlands")
    mesa = _constant(37, "Mesa")
    wooded_badlands_plateau = _constant(38, "Wooded Badlands Plateau")
    mesaPlateau_F = _constant(38, "Mesa Plateau F")
    badlands_plateau = _constant(39, "Badlands Plateau")
    mesaPlateau = _constant(39, "Mesa Plateau")
    small_end_islands = _constant(40, "Small End Islands")
    end_midlands = _constant(41, "End Midlands")
    end_highlands = _constant(42, "End Highlands")
    end_barrens = _constant(43, "End Barrens")
    warm_ocean = _constant(44, "Warm Ocean")
    warmOcean = _constant(44, "Warm Ocean")
    lukewarm_ocean = _constant(45, "Lukewarm Ocean")
    lukewarmOcean = _constant(45, "Lukewarm Ocean")
    cold_ocean = _constant(46, "Cold Ocean")
    coldOcean = _constant(46, "Cold Ocean")
    deep_warm_ocean = _constant(47, "Deep Warm Ocean")
    warmDeepOcean = _constant(47, "Deep Warm Ocean")
    deep_lukewarm_ocean = _constant(48, "Deep Lukewarm Ocean")
    lukewarmDeepOcean = _constant(48, "Deep Lukewarm Ocean")
    deep_cold_ocean = _constant(49, "Deep Cold Ocean")
    coldDeepOcean = _constant(49, "Deep Cold Ocean")
    deep_frozen_ocean = _constant(50, "Deep Frozen Ocean")
    frozenDeepOcean = _constant(50, "Deep Frozen Ocean")
    seasonal_forest = _constant(51, "Seasonal Forest")
    rainforest = _constant(52, "Rainforest")
    shrubland = _constant(53, "Shrubland")
    the_void = _constant(127, "The Void")
    sunflower_plains = _constant(129, "Sunflower Plains")
    desert_lakes = _constant(130, "Desert Lakes")
    gravelly_mountains = _constant(131, "Gravelly Mountains")
    flower_forest = _constant(132, "Flower Forest")
    taiga_mountains = _constant(133, "Taiga Mountains")
    swamp_hills = _constant(134, "Swamp Hills")
    ice_spikes = _constant(140, "Ice Spikes")
    modified_jungle = _constant(149, "Modified Jungle")
    modified_jungle_edge = _constant(151, "Modified Jungle Edge")
    tall_birch_forest = _constant(155, "Tall Birch Forest")
    tall_birch_hills = _constant(156, "Tall Birch Hills")
    dark_forest_hills = _constant(157, "Dark Forest Hills")
    snowy_taiga_mountains = _constant(158, "Snowy Taiga Mountains")
    giant_spruce_taiga = _constant(160, "Giant Spruce Taiga")
    giant_spruce_taiga_hills = _constant(161, "Giant Spruce Taiga Hills")
    modified_gravelly_mountains = _constant(162, "Modified Gravelly Mountains")
    shattered_savanna = _constant(163, "Shattered Savanna")
    shattered_savanna_plateau = _constant(164, "Shattered Savanna Plateau")
    eroded_badlands = _constant(165, "Eroded Badlands")
    modified_wooded_badlands_plateau = _constant(166, "Modified Wooded Badlands Plateau")
    modified_badlands_plateau = _constant(167, "Modified Badlands Plateau")
    bamboo_jungle = _constant(168, "Bamboo Jungle")
    bamboo_jungle_hills = _constant(169, "Bamboo Jungle Hills")
    soul_sand_valley = _constant(170, "Soul Sand Valley")
    crimson_forest = _constant(171, "Crimson Forest")
    warped_forest = _constant(172, "Warped Forest")
    basalt_deltas = _constant(173, "Basalt Deltas")
    dripstone_caves = _constant(174, "Dripstone Caves")
    lush_caves = _constant(175, "Lush Caves")
    meadow = _constant(177, "Meadow")
    grove = _constant(178, "Grove")
    snowy_slopes = _constant(179, "Snowy Slopes")
    jagged_peaks = _constant(180, "Jagged Peaks")
    frozen_peaks = _constant(181, "Frozen Peaks")
    stony_peaks = _constant(182, "Stony Peaks")
    old_growth_birch_forest = _constant(155, "Old Growth Birch Forest")
    old_growth_pine_taiga = _constant(32, "Old Growth Pine Taiga")
    old_growth_spruce_taiga = _constant(160, "Old Growth Spruce Taiga")
    snowy_plains = _constant(12, "Snowy Plains")
    sparse_jungle = _constant(23, "Sparse Jungle")
    stony_shore = _constant(25, "Stony Shore")
    windswept_hills = _constant(3, "Windswept Hills")
    windswept_forest = _constant(34, "Windswept Forest")
    windswept_gravelly_hills = _constant(131, "Windswept Gravelly Hills")
    windswept_savanna = _constant(163, "Windswept Savanna")
    wooded_badlands = _constant(38, "Wooded Badlands")
    deep_dark = _constant(183, "Deep Dark")
    mangrove_swamp = _constant(184, "Mangrove Swamp")
    cherry_grove = _constant(185, "Cherry Grove")


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
    HOUSING = _constant(0, "Housing")
    STABLES = _constant(1, "Stables")
    TREASURE = _constant(2, "Treasure")
    BRIDGE = _constant(3, "Bridge")