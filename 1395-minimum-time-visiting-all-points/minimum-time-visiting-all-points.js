/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    const getDist = (p1, p2) => {
        const [x, y] = p1;
        const [nx, ny] = p2; 
        return Math.max(Math.abs(nx - x), Math.abs(ny - y));
    }
    let dist = 0;
    for (let i = 1; i < points.length; i++)  {
        dist += getDist(points[i - 1], points[i]);
    }
    return dist;
};