class Solution {
    int minpath(int i,int j,int row,int col,int[][] grid){
        if(i >= row || j >= col)
            return Integer.MAX_VALUE;
        if(i == row-1 && j == col -1)
            return grid[i][j];
        else
            return grid[i][j] + Math.min(minpath(i,j+1,row,col,grid),minpath(i+1,j,row,col,grid));
    }
    public int minPathSum(int[][] grid) {
        
        return minpath(0,0,grid.length,grid[0].length,grid);
    }
}