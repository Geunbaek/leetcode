
var FileSystem = function() {
  this.cache = {}  
};

function findDirectory(paths, sources) {
    for (let source of sources) {
        if (!Reflect.has(paths, source)) return -1;
        paths = paths[source];
    }

    return paths
}

/** 
 * @param {string} path 
 * @param {number} value
 * @return {boolean}
 */
FileSystem.prototype.createPath = function(path, value) {
    const sources = path.split("/").filter(el => el);
    const parentDir = findDirectory(this.cache, sources.slice(0, -1));
  
    if (parentDir === -1) return false;

    const lastSource = sources.at(-1);
    if (Reflect.has(parentDir, lastSource)) return false
    parentDir[lastSource] = {"/": value};
    return true;
};

/** 
 * @param {string} path
 * @return {number}
 */
FileSystem.prototype.get = function(path) {
    const sources = path.split("/").filter(el => el);
    const parentDir = findDirectory(this.cache, sources.slice(0, -1));
    if (parentDir === -1) return -1;

    const lastSource = sources.at(-1)
    if (!Reflect.has(parentDir, lastSource)) return -1;
    return parentDir[lastSource]["/"];
};

/** 
 * Your FileSystem object will be instantiated and called as such:
 * var obj = new FileSystem()
 * var param_1 = obj.createPath(path,value)
 * var param_2 = obj.get(path)
 */