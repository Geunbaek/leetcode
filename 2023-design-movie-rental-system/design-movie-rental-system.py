class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_shop_map = {}
        self.shop_movie_map = {}
        self.rent_logs = []

        for shop, movie, price in entries:
            if movie not in self.movie_shop_map:
                self.movie_shop_map[movie] = []

            heappush(self.movie_shop_map[movie], (price, shop, movie))

            if shop not in self.shop_movie_map:
                self.shop_movie_map[shop] = {}

            self.shop_movie_map[shop][movie] = {"price": price, "is_rented": False}

    def search(self, movie: int) -> List[int]:
        if movie not in self.movie_shop_map:
            return []

        movies = self.movie_shop_map[movie]

        shops = []
        temps = []
        while movies:
            price, shop, movie = heappop(movies)

            if not self.shop_movie_map[shop][movie]["is_rented"]:
                shops.append(shop)

            temps.append((price, shop, movie))

            if len(shops) >= 5:
                break

        for temp in temps:
            heappush(self.movie_shop_map[movie], temp)

        return shops

    def rent(self, shop: int, movie: int) -> None:
        self.shop_movie_map[shop][movie]['is_rented'] = True
        heappush(self.rent_logs, (self.shop_movie_map[shop][movie]["price"], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.shop_movie_map[shop][movie]['is_rented'] = False

    def report(self) -> List[List[int]]:
        rents = []
        temps = []
        visited = set()
        while self.rent_logs:
            price, shop, movie = heappop(self.rent_logs)
            
            if (shop, movie) in visited:
                continue
                
            if self.shop_movie_map[shop][movie]['is_rented']:
                rents.append([shop, movie])
                visited.add((shop, movie))
                temps.append((price, shop, movie))

            if len(rents) >= 5:
                break
        
        for temp in temps:
            heappush(self.rent_logs, temp)
        return rents        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()