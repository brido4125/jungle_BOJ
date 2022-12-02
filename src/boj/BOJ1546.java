package boj;

import java.util.Scanner;

public class BOJ1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int numList[] = new int[num];
        for (int i = 0; i < num; i++) {
            numList[i] = sc.nextInt();
        }
        long sum = 0;
        long max = 0;
        for (int i = 0; i < num; i++) {
            if(numList[i] > max){
                max = numList[i];
            }
            sum = sum + numList[i];
        }
        //한번에 평균과 주어진 수식 함께 계산
        System.out.println(sum * 100.0 / max / num);
    }
}
