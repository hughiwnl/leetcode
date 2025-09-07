class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        starting_pixel = image[sr][sc] # this is the first pixel you start on

        self.dfs(image, sr, sc, color, starting_pixel) #calls our helper function passing in the image, row, column, color, and starting pixel

        return image 

    def dfs(self, image, sr, sc, color, starting_pixel): # helper function 

        if sr < 0 or sr > len(image[0])-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return
        # if row & column less than 0 or bigger than length, its out of range
        # if it already equals the color skip, or if there is no longer a value of a starting pixel
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, starting_pixel) # one to the right
        self.dfs(image, sr-1, sc, color, starting_pixel) # one to the left
        self.dfs(image, sr, sc+1, color, starting_pixel) # one up
        self.dfs(image, sr, sc-1, color, starting_pixel) # one down

        # so as long as its in range, and it isnt the right color and it is a starting pixel
        # this will run up, down, left, right and the image[sr][sc] aka the specific row and column will be the color