package boj;

import java.util.Scanner;

public class BOJ2018 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long start = 1;
        long end = 1;
        long sum = 1;
        long answer = 1;
        while (end < N) {
            if (sum == N) {
                end++;
                answer++;
                sum += end;
            }else if (sum < N) {
                end++;
                sum += end;
            }else{
                sum -= start;
                start++;
            }
        }
        System.out.println(answer);
    }
}
