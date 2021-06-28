class Solution:

    def run(self, n, m, movies):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements

        movie_stack = list(range(n, 0, -1))
        books_on_top_list = []
        for movie in movies:
            movie_index = movie_stack.index(movie) + 1
            books_on_top = len(movie_stack[movie_index:len(movie_stack)])
            movie_stack.remove(movie)
            movie_stack.append(movie)
            books_on_top_list.append(str(books_on_top))
        
        return ",".join(books_on_top_list)


solution = Solution()
print(solution.run(3, 3, [3, 1, 1]))