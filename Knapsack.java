import java.util.*;
class Knapsack
{
public static int knapsack(int []wt,int []pft,int W,int n)
{
if( n == 0 || W == 0)
    return 0;
if( wt[n] > W)
    return knapsack(wt,pft,W,n-1);
if(wt[n] <= W)
    return Math.max(knapsack(wt,pft,W,n-1),pft[n-1] + knapsack(wt,pft,W-wt[n-1],n-1));
return 0;
}
public static void main(String[] args){
int size,item;
Scanner read =  new Scanner(System.in);
System.out.print("Enter the Size of Knapsack :");
size = read.nextInt();
System.out.println();
System.out.println("Enter total items : ");
item = read.nextInt();
int[] profit = new int[item];
int[] weight = new int[item];
System.out.println();
System.out.println("Enter the weights : ");
for(int i = 0 ; i < item;i++)
profit[i] = read.nextInt();
System.out.println("Enter the Profits : ");
for(int i = 0 ; i < item;i++)
weight[i] = read.nextInt();

System.out.println("The Max Profit :"+ knapsack(weight,profit,size,item-1));
}
}
