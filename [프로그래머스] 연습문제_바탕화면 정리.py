def solution(wallpaper):
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == "#":
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x+1)
                rdy = max(rdy, y+1)
    return [lux, luy, rdx, rdy]