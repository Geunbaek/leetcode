class TreeNode {
    constructor(value, index) {
        this.value = value;
        this.index = index;
        this.next = [];
    }
}

function connectPhrase(dict, parent, visited){
    const lastWord = parent.value.split(" ").pop();

    if (lastWord in dict) {
        const phrases = dict[lastWord]
        for (const { i, phrase } of phrases) {
            if (visited[i]) continue;
            visited[i] = true;
            const node = new TreeNode(phrase, i);
            parent.next.push(node);
            visited[i] = false;
        }
    } 
}

function getAfterPuzzle(node, output, words){
    if (node.next.length) {
        for (const n of node.next) {
            getAfterPuzzle(n, output, [...words, n.value.split(" ").slice(1).join(" ")]);
        }
    } else {
        output.add(words.filter(word => word).join(" "));
    }
}

/**
 * @param {string[]} phrases
 * @return {string[]}
 */
var beforeAndAfterPuzzles = function(phrases) {
    const dict = {};
    const output = new Set();
    const visited = new Array(phrases.length).fill(false);

    for (let i = 0; i < phrases.length; i++) {
        const phrase = phrases[i];
        const [firstWord] = phrase.split(" ");
        if (firstWord in dict) {
            dict[firstWord].push({ i, phrase });
        } else {
            dict[firstWord] = [{ i, phrase }];
        }
    }

    for (let i = 0; i < phrases.length; i++) {
        const phrase = phrases[i];
        visited[i] = true;
        const root = new TreeNode(phrase, i);
        connectPhrase(dict, root, visited)
        visited[i] = false

        if (!root.next.length) continue;

        const words = [root.value]
        let node = root;
        getAfterPuzzle(node, output, words)
    }
    return [...output].sort();
};