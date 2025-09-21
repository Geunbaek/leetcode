

/**
 * @param {number} memoryLimit
 */
var Router = function(memoryLimit) {
    this.limit = memoryLimit;
    this.routes = [];
    this.routesSet = new Set();
    this.routesMap = new Map();
};

Router.prototype.isFull = function() {
    return this.routesSet.size >= this.limit;
}

Router.prototype.isEmpty = function() {
    return this.routesSet.size === 0;
}

/** 
 * @param {number} source 
 * @param {number} destination 
 * @param {number} timestamp
 * @return {boolean}
 */
Router.prototype.addPacket = function(source, destination, timestamp) {
    const routeStr = [source, destination, timestamp].join("-");
    if (this.routesSet.has(routeStr)) {
        return false
    }

    if (this.isFull()) {
        const first = this.routes.shift();
        this.routesMap.get(first[1]).shift();
        this.routesSet.delete(first.join("-"))
    }
    this.routes.push([source, destination, timestamp]);
    
    const arr = this.routesMap.get(destination) || [];
    arr.push([source, destination, timestamp]);

    this.routesMap.set(destination, arr)
    this.routesSet.add(routeStr);
    return true;
};

/**
 * @return {number[]}
 */
Router.prototype.forwardPacket = function() {
    if (this.isEmpty()) return [];
    const first = this.routes.shift();
    this.routesMap.get(first[1]).shift();
    this.routesSet.delete(first.join("-"));
    return first
};

const leftBinarySearch = (routes, startTime) => {
    let [left, right] = [0, routes.length - 1];

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (routes[mid][2] < startTime) {
            left = mid + 1;
        } else {
            right = mid - 1
        }
    }
    return left;
}

const rightBinarySearch = (routes, endTime) => {
    let [left, right] = [0, routes.length - 1];

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (routes[mid][2] <= endTime) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}


/** 
 * @param {number} destination 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number}
 */
Router.prototype.getCount = function(destination, startTime, endTime) {
    if (!this.routesMap.has(destination)) return 0;
    const routes = this.routesMap.get(destination);
    if (routes?.length === 0) return 0;
    const l = leftBinarySearch(routes, startTime);
    const r = rightBinarySearch(routes, endTime);
    return r - l
};

/** 
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */