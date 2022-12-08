package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ1940 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        int[] ary = new int[N];
        for (int i = 0; i < N; i++) {
            ary[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(ary);
        int start = 0;
        int end = N-1;
        int answer = 0;
        while (start < end) {
            if (ary[start] + ary[end] == M) {
                answer++;
                end--;
            } else if (ary[start] + ary[end] < M) {
                start++;
            } else {
                end--;
            }
        }
        System.out.println(answer);
    }
}
