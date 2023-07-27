class Node {
    constructor(value = null) {
        this.value = value;
        this.end = false;
        this.children = new Map();
    }
}

var Trie = function() {
    this.root = new Node();
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;

    for (let i = 0; i < word.length; i ++) {
        const char = word[i];
        if (!node.children.has(char)) {
            node.children.set(char, new Node(char));
        }
        node = node.children.get(char);
    }
    node.end = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
        
    for (let i = 0; i < word.length; i ++) {
        const char = word[i];
        if (!node.children.has(char)) {
            return false;
        }
        node = node.children.get(char)
    }
    return node.end;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
        
    for (let i = 0; i < prefix.length; i ++) {
        const char = prefix[i];
        if (!node.children.has(char)) {
            return false;
        }
        node = node.children.get(char)
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */