#include "generator.h"
#include "finders.h"
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

int** find_bastions(uint64_t seed) {
    int count = 0;
    int maxBastions = 10; // Maximum number of bastions to find
    int** bastionLocs = (int**)malloc(maxBastions * sizeof(int*));
    for (int i = 0; i < maxBastions; i++) {
        bastionLocs[i] = (int*)malloc(2 * sizeof(int)); // Each bastion has an x and z coordinate
    }

    int mcVersion = MC_1_16_1;
    Generator g;
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, DIM_NETHER, seed);

    int found = 0; // Counter for the number of bastions found
    int maxRegionDistance = 2; // Define the search area

    for (int rx = -maxRegionDistance; rx <= maxRegionDistance && found < maxBastions; ++rx) {
        for (int rz = -maxRegionDistance; rz <= maxRegionDistance && found < maxBastions; ++rz) {
            Pos pos;
            if (getStructurePos(Bastion, mcVersion, seed, rx, rz, &pos)) {
                if (isViableStructurePos(Bastion, &g, pos.x, pos.z, 0)) {
                    bastionLocs[found][0] = pos.x;
                    bastionLocs[found][1] = pos.z;
                    found++;
                }
            }
        }
    }

    count = found; // Set the out parameter to the number of bastions found
    return bastionLocs; // Return the array of bastion locations
}


int** find_forts(uint64_t seed) {
    int count = 1;
    int maxforts = 10; // Maximum number of bastions to find
    int** fortLocs = (int**)malloc(maxforts * sizeof(int*));
    for (int i = 0; i < maxforts+1; i++) {
        fortLocs[i] = (int*)malloc(2 * sizeof(int)); // Each bastion has an x and z coordinate
    }

    int mcVersion = MC_1_16_1;
    Generator g;
    setupGenerator(&g, mcVersion, 0);
    applySeed(&g, DIM_NETHER, seed);

    int found = 1; // Counter for the number of bastions found
    int maxRegionDistance = 2; // Define the search area
    for (int rx = -maxRegionDistance; rx <= maxRegionDistance && found < maxforts; ++rx) {
        for (int rz = -maxRegionDistance; rz <= maxRegionDistance && found < maxforts; ++rz) {
            Pos pos;
            if (getStructurePos(Fortress, mcVersion, seed, rx, rz, &pos)) {
                if (isViableStructurePos(Fortress, &g, pos.x, pos.z, 0)) {
                    fortLocs[found][0] = pos.x;
                    fortLocs[found][1] = pos.z;
                    found++;
                }
            }
        }
    }
    **fortLocs = found-1;
    count = found; // Set the out parameter to the number of bastions found
    return fortLocs; // Return the array of bastion locations
}




int** get_sh(uint64_t seed) {
    int** sh_locs = (int**)malloc(3 * sizeof(int*));
    for (int i = 0; i < 3; i++) {
        sh_locs[i] = (int*)malloc(2 * sizeof(int));
    }

    int mc = MC_1_16_1;
    Generator g;
    StrongholdIter sh;
    Pos pos = initFirstStronghold(&sh, mc, seed);
    setupGenerator(&g, mc, 0);
    applySeed(&g, DIM_OVERWORLD, seed);

    for (int i = 0; i < 3; i++) 
    {
        if (nextStronghold(&sh, &g) <= 0)
            break;
        sh_locs[i][0] = sh.pos.x;
        sh_locs[i][1] = sh.pos.z;
    }
    return sh_locs;
}