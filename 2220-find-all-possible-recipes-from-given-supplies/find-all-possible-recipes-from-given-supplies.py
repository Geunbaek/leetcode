class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        degrees = defaultdict(int)

        for recipe, target_ingredients in zip(recipes, ingredients):
            for ingredient in target_ingredients:
                degrees[recipe] += 1
                degrees[ingredient] += 0
                graph[ingredient].append(recipe)

        recipes = set(recipes)
        supplies = set(supplies)
        q = deque()

        for key, degree in degrees.items():
            if degree == 0 and key in supplies:
                q.append(key)
        
        answer = []
        while q:
            now = q.popleft()
            if now in recipes:
                answer.append(now)

            for _next in graph[now]:
                degrees[_next] -= 1
                if degrees[_next] == 0:
                    q.append(_next)
                
        return answer