package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        int[][] board = new int[N+1][N+1];
        int[][] sumBoard = new int[N+1][N+1];
        /* Board 생성 */
        for (int i = 1; i < N + 1; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int j = 1; j < N + 1; j++) {
                board[i][j] = Integer.parseInt(stringTokenizer.nextToken());
                sumBoard[i][j] = sumBoard[i][j-1] + sumBoard[i-1][j] - sumBoard[i-1][j-1] + board[i][j];
            }
        }
        /* 구해야할 구간 합 입력 */
        for (int i = 0; i < M; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int x1 = Integer.parseInt(stringTokenizer.nextToken());
            int y1 = Integer.parseInt(stringTokenizer.nextToken());
            int x2 = Integer.parseInt(stringTokenizer.nextToken());
            int y2 = Integer.parseInt(stringTokenizer.nextToken());
            int answer = sumBoard[x2][y2] - sumBoard[x1 - 1][y2] - sumBoard[x2][y1 - 1] + sumBoard[x1-1][y1-1];
            System.out.println(answer);
        }
    }
}
