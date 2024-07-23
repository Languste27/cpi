#include "cubiomes/generator.h"
#include "cubiomes/finders.h"
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <math.h>


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

int* INTERFACE_getSpwan(uint64_t seed, int mcVersion){
    Generator g;
    setupGenerator(&g, mcVersion, 0);
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
    case 46: {return 0;}
    case 30: {return 1;}
    case 38: {return 2;}
    case 16: {return 3;}
    }
}


int** INTERFACE_find_in_range(int structure, int mcVersion, uint64_t seed, int dimension, int srx, int srz, int erx, int erz){
    int **array;
    int xlen = abs(srx-erx);
    int zlen = abs(srz-erz);

    array = (int **)malloc((xlen*zlen + 1) * sizeof(int *));
    for(int i = 0; i < (xlen*zlen + 1); i++) {
        array[i] = (int *)malloc(2 * sizeof(int));
    }

    int counter = 1;
    Generator g;

    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, dimension, seed);

    for (int rx = srx; rx<erx;rx++){
        for (int rz = srz; rz<erz;rz++){
            Pos pos;
            if (getStructurePos(structure, mcVersion, seed, rx, rz, &pos)){
                if (isViableStructurePos(structure, &g, pos.x, pos.z, 0)){
                    
                    array[counter][0] = pos.x;
                    array[counter][1] = pos.z;
                    counter++;

                }
            }
        }
    }
    array[0][0] = counter;
    return array;
}


int* INTERFACE_find_closest_structure(int structure, int mcVersion, uint64_t seed, int dimension, int cx, int cz, int limit){
    Generator g;
    int d;
    int* posArray = (int*)malloc(2 * sizeof(int));
    
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, dimension, seed);

    for (int radius = 0; radius<=limit; radius++){
        
        for (int rx = -radius; rx<=radius; rx++){
            for (int rz=-radius; rz<=radius; rz++){
                
                d = sqrt((cx-rx)*(cx-rx) + (cz-rz)*(cz-rz));
                if ((radius-1) < d <= radius){
                    Pos loc;

                    if (getStructurePos(structure, mcVersion, seed, rx, rz, &loc)){
                        if (isViableStructurePos(structure, &g, loc.x, loc.z, 0)){

                                posArray[0] = loc.x;
                                posArray[1] = loc.z;
                                return posArray;
                        }
                    }
                }
            }
        }
    }
    posArray[0] = 0;
    posArray[1] = 0;
    return posArray;
}
