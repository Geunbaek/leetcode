impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut res = 0;

        for i in 0..32 {
            let bit_a = (a >> i) & 1;
            let bit_b = (b >> i) & 1;
            let bit_c = (c >> i) & 1;

            if bit_c == 0 {
                res += bit_a + bit_b;
            } else {
                res += if bit_a + bit_b == 0 { 1 } else { 0 };
            }
        }

        res
    }
}