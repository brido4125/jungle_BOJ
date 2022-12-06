package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10986 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        /* 항상 int => long으로 설정하기 */
        long[] ary = new long[N+1];
        long[] mod_ary = new long[M];//해당 나머지로 나눠지는 구간합의 수를 저장
        long answer = 0;
        for (int i = 1; i < N+1; i++) {
            ary[i] = Integer.parseInt(stringTokenizer.nextToken());
            ary[i] += ary[i-1];
            ary[i] %= M;
            if (ary[i] == 0) {
                answer += 1;
            }
            mod_ary[(int) ary[i]]++;
        }
        for (long elem : mod_ary) {
            if (elem > 1) {
                answer += ( elem * (elem - 1)) / 2;
            }
        }
        System.out.println(answer);
    }
}
