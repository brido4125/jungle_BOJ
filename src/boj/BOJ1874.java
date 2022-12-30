package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        Stack<Integer> my_stack = new Stack<>();
        int[] ary = new int[N];
        my_stack.push(Integer.parseInt(st.nextToken()));
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            ary[i] = Integer.parseInt(st.nextToken());

        }


    }
}
