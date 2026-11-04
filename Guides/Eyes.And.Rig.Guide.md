# Eyes and Rig Guide for Cartoon 3D Characters in Blender

Working rules learned while building BE and Dot. Scripts referenced here are in the same project: Build.Rigged.Characters.py, Build.Cards.py and Build.All.Cards.py.

## Building the eye
1. Make the eye a real sphere sunk into the body, about 60% of its radius below the surface. A flattened dome sitting on top looks stuck on.
2. Make the pupil a curved patch on the eyeball's surface, on its own bone at the centre of the eye, so it rolls around the eye when it turns.
3. Aim both eyes at one point in front of the character, slightly converging. Pupils that follow the curve of a round body point outward and look wrong.
4. Keep highlights fixed to the head, because light does not move when the eye turns.
5. Rest the upper lid on the top of the eye. A fully open eye reads as a stare.
6. Keep lids just outside the eyeball, so closed eyes sit flat and do not bulge.

## Eyelid shape keys
Blink, Squint, Happy and Wink. Curve both lids in a squint, because a straight lid reads as judging.

## Timing, for the animation stage
These are starting points from the sources below. They have not been tested on BE and Dot yet.
1. A blink takes 3 to 5 frames down, a brief hold, then 2 to 4 frames to open.
2. The top lid does most of the movement, and the lower lid catches up.
3. An eye dart takes 2 to 3 frames, with about 80% of the movement in one frame.
4. Lids follow the eye soon after a dart, and the top lid moves more than the lower lid.
5. Eyes lead a head turn. Thought and action start in the eyes.
6. Use half blinks for casual characters, quick blinks for nerves and held gazes for focus.

## Rig
1. Bones: root, lower spine, upper spine, head, shoulder, upper arm, forearm, hand and two joints per finger.
2. Use IK for the arms, with a pole target so the elbow stays low and a raised forearm really rises.
3. Squash and stretch: one control on the root bone, with width set to 1 divided by the square root of 1 plus the amount, so volume is kept.
4. Known issue: squashing also scales the arm controls, which can swing an arm out, so check arms on hops and landings.

## Sources
Animation Mentor, Natasha Krinsky, How to Animate Blinks and Eye Movements for Subtlety, 2025: https://www.animationmentor.com/blog/tutorial-animate-blinks-eye-movement/
AnimSchool, Animating the Eye Dart, 2022: https://blog.animschool.edu/2022/08/31/animating-the-eye-dart/
CG Cookie, Creating an Advanced Cartoon Eye Rig, course description: https://www.cgcookie.com/courses/creating-an-advanced-cartoon-eye-rig
