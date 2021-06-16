# particlesInABox

A really simple simulator of many particles in a box, with elastic collisions with the walls and in-between particles. The plot that is generated of the velocities resembles the general Maxwell-Boltzmann distribution. My program creates a simple plot of 5000 particles colliding in a box, and it looks like this:<img width="636" alt="Screen Shot 2021-06-16 at 5 43 16 PM" src="https://user-images.githubusercontent.com/37377528/122298266-87ae6100-ceca-11eb-8ad8-cd56e284371e.png">

After letting it run for a few minutes, I then have an histogram generated which displays in bins the magnitude of the velocities of the particles,

<img width="639" alt="Screen Shot 2021-06-16 at 5 56 01 PM" src="https://user-images.githubusercontent.com/37377528/122299561-27202380-cecc-11eb-9ea8-dc31ebe0274e.png">


and when this is compared to the actual distribution, one sees,
<img width="415" alt="Screen Shot 2021-06-16 at 5 54 41 PM" src="https://user-images.githubusercontent.com/37377528/122299456-01931a00-cecc-11eb-90ad-810e2ad69548.png">

They look roughly similar, this program could obviously be improved. One spot is to have physically consistent values reached ,for say the velocity distribution values.
