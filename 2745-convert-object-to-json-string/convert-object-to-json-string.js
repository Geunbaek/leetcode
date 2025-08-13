/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (typeof object === 'string') return `"${object}"`
    if (typeof object !== "object" || object === null) return `${object}`;
    const keys = Reflect.ownKeys(object);

    const values = keys.map(key => {
        const value = object[key];
        if (Array.isArray(object) && key == "length") return null
        if (typeof value === "string") return Array.isArray(object) ? `"${value}"` : `"${key}":"${value}"`;
        if (typeof value !== "object" || value === null) return Array.isArray(object) ? `${value}` : `"${key}":${value}`;
        const child = jsonStringify(object[key])
        return Array.isArray(object)? jsonStringify(object[key]) : `"${key}":${child}`;
    }).filter(value => value)

    if (Array.isArray(object)) return `[${values.join(",")}]`
    return `{${values.join(",")}}`
};