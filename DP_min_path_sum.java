import java.util.*;
class MinPathSum{
private int minpath(int[][] nums,int row,int col){
    int[][] dp = new int[row][col];
    dp[0][0] = nums[0][0];
    for(int i = 1; i < col;i++)
        dp[0][i] = dp[0][i-1] + nums[0][i];
    for(int i = 1; i < row;i++)
        dp[i][0] = dp[i-1][0] + nums[i][0];
    for(int i = 1;i < row;i++){
        for(int j = 1; j < col ;j++){  
            dp[i][j] = Math.min(dp[i-1][j],dp[i][j-1]) + nums[i][j];
            
        }
    }
    for(int i = 0;i < row;i++){
        for(int j = 0; j < col ;j++){
            System.out.print(dp[i][j] + " ");
        }
        System.out.println();
    }
    return dp[row-1][col-1];
}
public static void main(String[] args) {
    Scanner read = new Scanner(System.in);
    int row,col;
    System.out.println("Enter row and col :");
    row = read.nextInt();
    col = read.nextInt();
    int[][] nums = new int[row][col];
    for(int i = 0; i < row;i++){
        for(int j = 0 ; j < col ; j++){
            nums[i][j] = read.nextInt();
        }
    }
    MinPathSum mp = new MinPathSum();
    System.out.println("Minimum Path Sum :"+ mp.minpath(nums,row,col));
}
}
/* Input :
Enter row and col :
3 3
1 3 1 1 5 1 4 2 1

Output:

1 4 5 
2 7 6
6 8 7
Minimum Path Sum :7
*/
