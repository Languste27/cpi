# Cubiomes Python Interface (CPI) Documentation

## Overview

The Cubiomes Python Interface (CPI) is a python interface for [Cubiomes](https://github.com/Cubitect/cubiomes)

## Classes

### `Generator`

Stores data about the Minecraft world generator.

- **Attributes:**
  - `version` (int): Minecraft version number.
  - `seed` (int): Random seed for world generation.
  - `dimension` (int): Dimension ID.


## Dimension

Defines Minecraft dimensions with constants.

    Constants:
        DIM_NETHER = -1
        DIM_OVERWORLD = 0
        DIM_END = 1
        DIM_UNDEF = 1000

## MCVersion

Defines Minecraft version constants.

    Constants:
        MC_1_0_0 = 3
        MC_1_1_0 = 4
        MC_1_2_5 = 5
        ... (and so on up to MC_1_20)

## Structure

Defines various Minecraft structures with constants.

    Constants:
        Feature = 0
        Desert_Pyramid = 1
        Jungle_Temple = 2
        ... (and so on)

## BiomeID

Defines Minecraft biomes with constants.

    Constants:
        none = -1
        ocean = 0
        plains = 1
        ... (and so on, including custom biomes)

## BiomeGroups

Groups of biomes for convenience.

    Attributes:
        Forests
        Beaches
        DesertBiomes
        Oceans

## BastionType

Defines various bastion types.

    Constants:
        HOUSING = 0
        STABLES = 1
        TREASURE = 2
        BRIDGE = 3

# Functions
## distance_between_structures(structure1, structure2) -> float

### Calculates the distance between two structures.

    Parameters:
        structure1 (tuple[int, int]): Coordinates of the first structure.
        structure2 (tuple[int, int]): Coordinates of the second structure.

    Returns:
        float: Distance between the two structures.

## distance_from_00(c1) -> float

### Calculates the distance from the origin (0,0) to a given coordinate.

    Parameters:
        c1 (tuple[int, int]): Coordinates.

    Returns:
        float: Distance from the origin.

## distance_between_points(x1, y1, x2, y2) -> float

### Calculates the distance between two points.

    Parameters:
        x1, y1, x2, y2 (int): Coordinates of the two points.

    Returns:
        float: Distance between the two points.

## convert_to_string(constant: int, typee: object) -> str

### Converts a constant value to its string representation based on its type.

    Parameters:
        constant (int): The constant to convert.
        typee (object): The type of the constant (e.g., BastionType, Structure, BiomeID).

    Returns:
        str: String representation of the constant.

## get_structure_pos(structure: Structure, g: Generator, rx: int, rz: int) -> tuple[int, int]

### Gets the position of a structure.

    Parameters:
        structure (Structure): The structure to find.
        g (Generator): The generator instance.
        rx, rz (int): Coordinates.

    Returns:
        tuple[int, int]: Coordinates of the structure or None if not found.

## is_viable_structure_pos(structure: Structure, g: Generator, x: int, z: int) -> bool

### Checks if a position is viable for a structure.

    Parameters:
        structure (Structure): The structure to check.
        g (Generator): The generator instance.
        x, z (int): Coordinates.

    Returns:
        bool: True if viable, otherwise False.

## get_stronghold_pos(g: Generator, count: int) -> list[tuple[int, int]]

### Gets positions of strongholds.

    Parameters:
        g (Generator): The generator instance.
        count (int): Number of strongholds to retrieve.

    Returns:
        list[tuple[int, int]]: List of stronghold positions.

## get_spawn_pos(g: Generator) -> tuple[int, int]

### Gets the spawn position of the world.

    Parameters:
        g (Generator): The generator instance.

    Returns:
        tuple[int, int]: Spawn coordinates.

## get_biome_at(g: Generator, x: int, y: int, z: int) -> BiomeID

### Gets the biome at a specific coordinate.

    Parameters:
        g (Generator): The generator instance.
        x, y, z (int): Coordinates.

    Returns:
        BiomeID: ID of the biome at the coordinates.

## get_bastion_variant(g: Generator, x: int, z: int) -> BastionType

### Gets the bastion variant at a specific coordinate.

    Parameters:
        g (Generator): The generator instance.
        x, z (int): Coordinates.

    Returns:
        BastionType: Type of bastion at the coordinates.

## find_structure_in_range(g: Generator, structure: Structure, srx: int, srz: int, erx: int, erz: int) -> list[tuple[int, int]]

### Finds structures within a specified range.

    Parameters:
        g (Generator): The generator instance.
        structure (Structure): The structure to find.
        srx, srz, erx, erz (int): Range coordinates.

    Returns:
        list[tuple[int, int]]: List of structure positions or None if no structures are found.

## find_closest_structure(g: Generator, structure: Structure, cx: int, cz: int, limit: int) -> tuple[int, int]

### Finds the closest structure to a given coordinate.

    Parameters:
        g (Generator): The generator instance.
        structure (Structure): The structure to find.
        cx, cz (int): Coordinates.
        limit (int): Maximum search distance.

    Returns:
        tuple[int, int]: Coordinates of the closest structure or None if not found.