import math
import ctypes
import macro

def __c(val: int, seed=False):
    if seed:
        return ctypes.c_uint64(val)
    else:
        return ctypes.c_int(val)

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

def convert_to_string(constant: int, type: int):
    """constant: constant thats converted to string
       type: type of constant"""
    import constants
    from constants import BastionType
    from constants import BiomeID
    from constants import Structure

    
    match type:
        case constants.BastionType:
            match constant:
                case BastionType.HOUSING: return "Housing"
                case BastionType.STABLES: return "Stables"
                case BastionType.TREASURE: return "Treasure"
                case BastionType.BRIDGE: return "Bridge"
    
        case constants.Structure:
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

        case constants.BiomeID:
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
        