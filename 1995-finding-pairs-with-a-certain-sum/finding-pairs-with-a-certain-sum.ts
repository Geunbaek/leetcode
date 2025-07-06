class FindSumPairs {
    #nums1: number[]
    #nums2: number[];
    #cache: Map<number, number>;
    constructor(nums1: number[], nums2: number[]) {
        this.#nums1 = nums1;
        this.#nums2 = nums2;

        this.#cache = new Map();

        for (const num of nums2) {
            const count = this.#cache.get(num) || 0;
            this.#cache.set(num, count + 1);
        }
    }

    add(index: number, val: number): void {
        const prev = this.#nums2[index];
        const next = prev + val;

        this.#nums2[index] += val;
        this.#cache.set(prev, this.#cache.get(prev) - 1);
        this.#cache.set(next, (this.#cache.get(next) || 0) + 1);
    }

    count(tot: number): number {
        let cnt = 0;
        for (const num of this.#nums1) {
            const diff = tot - num;

            cnt += (this.#cache.get(diff) || 0);
        } 
        return cnt;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */