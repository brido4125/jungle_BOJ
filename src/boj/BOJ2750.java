package boj;

import java.util.Scanner;

public class BOJ2750 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String s = sc.next();
        char[] cStr = s.toCharArray();
        long sum = 0;
        for (int i = 0; i < cStr.length; i++) {
            sum += cStr[i] - '0';
        }
        System.out.println(sum);
    }
}
