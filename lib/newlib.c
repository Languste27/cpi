#include "generator.h"
#include "finders.h"
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>


int* INTERFACE_getStructurePos(int structuretype, int mcVersion, uint64_t seed, int rx, int rz)
{
    Pos pos;

    if (getStructurePos(structuretype, mcVersion, seed, rx, rz, &pos))
    {
    int* posArray = (int*)malloc(2 * sizeof(int));
    posArray[0] = pos.x;
    posArray[1] = pos.z;
    return posArray;
    }

    int* posArray = (int*)malloc(2 * sizeof(int));
    posArray[0] = 0;
    posArray[1] = 0;
    return posArray;
}

int INTERFACE_isViableStructurePos(int structuretype, int mcVersion, uint64_t seed, int dimension, int x, int z){
    Generator g;
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, dimension, seed);

    return isViableStructurePos(structuretype, &g, x, z, 0);
}

int* INTERFACE_getStrongholdPos(uint64_t seed, int mcVersion){
    Generator g;
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, DIM_OVERWORLD, seed);
    StrongholdIter sh;
    Pos pos = initFirstStronghold(&sh, mcVersion, seed);

    int* StrongholdPositions = (int*)malloc(128 * 2 * sizeof(int));
    
    for (int i=0; i<=127; i++){
        nextStronghold(&sh, &g);
        StrongholdPositions[i * 2] = sh.pos.x; // Store x position
        StrongholdPositions[i * 2 + 1] = sh.pos.z; // Store z position
    }
    return StrongholdPositions;
}

int* INTERFACE_getSpwan(uint64_t seed, int mcVerion){
    Generator g;
    setupGenerator(&g, mcVerion, 0);
    applySeed(&g, DIM_OVERWORLD, seed);
    Pos pos = getSpawn(&g);
    int* position = (int*)malloc(2*sizeof(int));
    position[0] = pos.x;
    position[1] = pos.z;
    return position;
}

int INTERFACE_getBiomeAt(int mcVersion, uint64_t seed, int dimension, int x, int y, int z){
    Generator g;
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, dimension, seed);
    int biome = getBiomeAt(&g, 1, x, y, z);
    return biome;
}


int INTERFACE_getBastionVariant(int mcVersion, uint64_t seed, int x, int z){
    StructureVariant sv;
    int bastion_type = getVariant(&sv, Bastion, mcVersion, seed, x, z, -1);

    switch (sv.sx)
    {
    case 46:{return 0;}
    case 30:{return 1;}
    case 38:{return 2;}
    case 16:{return 3;}
    }
}

// int main(){

//     uint64_t seed = -3604265396460847324;

//     int mcVersion = MC_1_16_1;
//     Generator g;
//     setupGenerator(&g, mcVersion, 0);
//     applySeed(&g, DIM_NETHER, -seed);

//     int found = 0; // Counter for the number of bastions found
//     int maxRegionDistance = 2; // Define the search area


//             Pos pos;
//             // pos.x = 48;
//             // pos.z = -288;
//             if (getStructurePos(Bastion, mcVersion, seed, 0, -1, &pos)) {
//                 printf("%i, %i", pos.x, pos.z);
//                 printf("%i", isViableStructurePos(Bastion, &g, pos.x, pos.z, 0));
//             }

// }
