use std::collections::VecDeque;


impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let dx = [1, -1, 0, 0];
        let dy = [0, 0, 1, -1];

        // 1. 다중 시작점 BFS를 위한 dists 배열 및 큐 초기화
        // 초기값은 넉넉하게 n * n으로 설정합니다.
        let mut dists = vec![vec![(n * n) as i32; n]; n];
        let mut q = VecDeque::new();

        for y in 0..n {
            for x in 0..n {
                if grid[y][x] == 1 {
                    dists[y][x] = 0;
                    q.push_back((x, y)); // 튜플 오버헤드를 줄이기 위해 좌표만 저장
                }
            }
        }

        // 다중 시작점 BFS 진행 (각 칸에서 가장 가까운 도둑까지의 거리 사전 계산)
        while let Some((x, y)) = q.pop_front() {
            let current_d = dists[y][x];
            for i in 0..4 {
                let nx = x as i32 + dx[i];
                let ny = y as i32 + dy[i];

                if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                    let nx = nx as usize;
                    let ny = ny as usize;

                    // 더 짧은 거리를 발견했을 때만 갱신하고 큐에 삽입
                    if dists[ny][nx] > current_d + 1 {
                        dists[ny][nx] = current_d + 1;
                        q.push_back((nx, ny));
                    }
                }
            }
        }

        // 2. 특정 안전 거리 d를 유지하며 끝점까지 도달 가능한지 체크하는 헬퍼 클로저
        let can_cross = |d: i32| -> bool {
            // 시작점이나 끝점 자체가 요구하는 안전 거리 d 미만이면 바로 탈락
            if dists[0][0] < d || dists[n - 1][n - 1] < d {
                return false;
            }

            // 메모리가 터지지 않도록 고정된 크기의 2차원 방문 배열 사용
            let mut visited = vec![vec![false; n]; n];
            let mut bfs_q = VecDeque::new();

            bfs_q.push_back((0, 0));
            visited[0][0] = true;

            while let Some((x, y)) = bfs_q.pop_front() {
                if x == n - 1 && y == n - 1 {
                    return true;
                }

                for i in 0..4 {
                    let nx = x as i32 + dx[i];
                    let ny = y as i32 + dy[i];

                    if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                        let nx = nx as usize;
                        let ny = ny as usize;

                        // 도둑이 있는 칸이거나, 이미 방문했거나, 안전 거리가 d 미만이면 패스
                        if grid[ny][nx] == 1 || visited[ny][nx] || dists[ny][nx] < d {
                            continue;
                        }

                        visited[ny][nx] = true;
                        bfs_q.push_back((nx, ny));
                    }
                }
            }

            visited[n - 1][n - 1]
        };

        // 3. 이진 탐색 진행
        let mut l = 0;
        let mut r = (2 * n) as i32;
        let mut answer = 0;

        while l <= r {
            let mid = (l + r) / 2;

            if can_cross(mid) {
                answer = answer.max(mid);
                l = mid + 1; // 더 큰 안전 거리가 가능한지 확인하기 위해 오른쪽 탐색
            } else {
                r = mid - 1; // 불가능하므로 안전 거리를 줄여서 왼쪽 탐색
            }
        }

        answer
    }
}