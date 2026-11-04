# Render 3D Library

Free 3D characters, animations and props used to build short 3D videos in Blender. Every file here is CC0 (public domain): free for personal and commercial use, no credit required. Each folder keeps the original licence file.

## Contents

| Folder | What it holds | Models | Creator | Licence |
|---|---|---|---|---|
| Animations/KayKitCharacterAnimations | 131 human animation clips in 8 sets (movement, general, simulation, tools, combat, special) on the Rig_Medium skeleton | 8 files | Kay Lousberg (KayKit) | CC0 |
| Characters/KayKitMannequin | Rigged neutral mannequin that plays every clip above | 1 | Kay Lousberg (KayKit) | CC0 |
| Characters/KayKitAdventurers | Barbarian, Knight, Mage, Rogue, Rogue Hooded | 5 | Kay Lousberg (KayKit) | CC0 |
| Characters/RobotExpressive | Robot with 14 clips (walk, run, wave, jump, dance, thumbs up and more) | 1 | Tomas Laulhe, modified by Don McCurdy | CC0 |
| Characters/KenneyPlatformer | Small robot character and platform props, with textures | 15 | Kenney | CC0 |
| Props/KayKitCityBuilder | Roads, buildings, cars, street props | 41 | Kay Lousberg (KayKit) | CC0 |
| Props/KayKitFurniture | Room and home furniture | 53 | Kay Lousberg (KayKit) | CC0 |
| Props/KayKitRestaurant | Kitchen, food and restaurant props | 144 | Kay Lousberg (KayKit) | CC0 |
| Props/KayKitAdventurersProps | Mugs, books, shields, tools and weapons | 27 | Kay Lousberg (KayKit) | CC0 |
| Props/KenneyCityBuilder | Roads and buildings | 15 | Kenney | CC0 |
| Props/KenneyNatureKit | Trees, plants, flowers, rocks, crops, paths, bridges and camp props | 329 | Kenney | CC0 |
| Props/KenneyFantasyTown | Town walls, roofs, stalls, carts, banners, lanterns, fences and a windmill, with one shared texture | 167 | Kenney | CC0 |

## Tested in Blender 5.2

* The mannequin plays the KayKit clips directly (same bone names). Tested clips include Idle, Walking A to C, Running, Jump, PickUp, Holding, Interact, Use Item, Throw, Waving, Cheering, Sit Chair, Sit Floor, Lie Down and Work.
* RobotExpressive imports with all 14 clips.
* glTF files load their .bin and texture files from the same folder, so keep each folder together.

## Original sources

* KayKit Character Animations 1.1, mirrored at github.com/NoLimitNexus/game-models (only the KayKit files are copied here)
* KayKit packs: github.com/KayKit-Game-Assets
* Kenney Starter Kits: github.com/KenneyNL
* Kenney Nature Kit 2.1: kenney.nl/assets/nature-kit. The .glb files only. One unused link to an empty helper node was removed from each model so that it passes the glTF Validator; the geometry and the loaded model are unchanged.
* Kenney Fantasy Town Kit 2.0: kenney.nl/assets/fantasy-town-kit. The .glb files and their texture only.
* RobotExpressive: github.com/mrdoob/three.js (examples/models/gltf)

## Credits

All files are CC0, so no credit is legally required. We credit the creators anyway, with thanks:

* Kay Lousberg (KayKit), www.kaylousberg.com: character animations, mannequin, adventurers and all KayKit prop packs
* Kenney, www.kenney.nl: Kenney Platformer, Kenney City Builder, Nature Kit and Fantasy Town Kit models
* Tomas Laulhe (Quaternius), with modifications by Don McCurdy: RobotExpressive

The creators do not endorse this library or its videos.

## Safety

Every file is checked before it is added, so the library is safe to download:

* Only plain 3D models (.glb, .gltf, .bin), textures (.png, .jpg) and text files (.txt, .md) are allowed. No programs, scripts or engine files, except the check itself in Tools.
* Each file's contents must match its type, nothing is marked as executable, and no file is over 30 MB.
* Models may only load files from their own folder: no internet links and no paths outside the folder.
* Every model is also run through the official Khronos glTF Validator.

Run the check from the repository root before every commit:

```
python3 -I Tools/SafetyCheck.py
```

Last safety check: 5 Nov 2026. PASSED for all 1,105 files. The 496 models added that day (Nature Kit and Fantasy Town Kit) also passed the glTF Validator with no errors or warnings.

Last full check: 2 Nov 2026. PASSED for all 605 files. The validator reports only a harmless precision note in RobotExpressive (its skin weights do not add up to exactly 1); this is in the original file and is not a safety issue.

## Rules for this repository

* Only CC0 files go here, each folder with its licence and, where the source has one, its original note.
* Every addition passes Tools/SafetyCheck.py and the glTF Validator before it is committed.
* Mixamo files and any file whose licence forbids sharing never go in this public repository.
