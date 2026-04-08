class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs,pos,dir,dist = {(x,y) for x,y in obstacles}, (0,0), (0,1), 0
        dirtab = {-2:{(0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0),  (1,0):(0,1)},
                  -1:{(0,1):(1,0),  (1,0):(0,-1),  (0,-1):(-1,0), (-1,0):(0,1)}}
        for cmd in commands:
            if  cmd<0:  dir = dirtab[cmd][dir]; continue
            for _ in range(cmd):
                newpos = (pos[0] +dir[0], pos[1] +dir[1])
                if  newpos in obs: break
                pos = newpos
            dist = max(dist, pos[0]*pos[0] + pos[1]*pos[1])
        return  dist

