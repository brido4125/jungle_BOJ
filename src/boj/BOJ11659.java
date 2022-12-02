package boj;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        long[] numList = new long[N+1];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 1; i < N + 1; i++) {
            numList[i] = Integer.parseInt(stringTokenizer.nextToken());
            numList[i] += numList[i-1];
        }
        for (int i = 0; i < M; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());
            long answer = numList[end] - numList[start-1];
            System.out.println(answer);
        }
    }
}
