from scipy.spatial.distance import pdist, squareform
import numpy as np

def wall_collisions(pos,vel,leftwall,rightwall,topwall,bottomwall):
    X, Y = 0, 1
    hit_left_wall = pos[:, X] < leftwall
    hit_right_wall = pos[:, X] > rightwall
    hit_bottom_wall = pos[:, Y] < bottomwall
    hit_top_wall = pos[:, Y] > topwall
    # hit_front_wall = pos[:,Z] > 4
    # hit_back_wall = pos[:,Z] < -4
    vel[hit_left_wall | hit_right_wall, X] *= -1
    vel[hit_bottom_wall | hit_top_wall, Y] *= -1
    # vel[hit_front_wall | hit_back_wall, Z] *= -1

def inter_collisions(pos,vel, radius, softening):
    dist = squareform(pdist(pos))
    iarr, jarr = np.where(dist < 2*radius)
    k = iarr < jarr
    iarr, jarr = iarr[k], jarr[k]

    for i, j in zip(iarr, jarr):
        pos_i, vel_i = pos[i], vel[i]
        pos_j, vel_j = pos[j], vel[j]
        rel_pos, rel_vel = pos_i - pos_j, vel_i - vel_j
        r_rel = rel_pos @ rel_pos
        v_rel = rel_vel @ rel_pos
        v_rel = 2 * rel_pos * v_rel / r_rel - rel_vel
        v_cm = (vel_i + vel_j) / 2
        vel[i] = v_cm - v_rel/2
        vel[j] = v_cm + v_rel/2