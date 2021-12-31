//  We have two choices either we can Cut or Don't cut the rod.
import java.util.*;
int maxval;
int cutRodMax(int[] price,int N){
if(N <= 0)
return 0;
for(int i = 0; i < N-1;i++)
    maxval = Math.max(maxval,price[i] + cutRodMax(price,N-i-1));
return maxval;
}
public static void main(String... args) throws Throwable{
    int len=0;
    Scanner read =  new Scanner(System.in);
    System.out.print("Enter the length of the rod :");
    len = read.nextInt();
    int length[] = new int[len];
    int price[] = new int[len];
    System.out.println("Enter the cut of lengths:");
    for(int i = 0 ; i<len;i++)
    price[i] = read.nextInt();
    System.out.println("Max profit is :"+cutRodMax(price,len));
}
