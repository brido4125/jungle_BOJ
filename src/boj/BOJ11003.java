package boj;

import java.io.*;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ11003 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        /* Sliding Window의 크기 = L */
        /* L을 3으로 가정하면 A(-1),A(0),A(1) 부터 Sliding Window를 계산하여 해당 윈도우 내의 최솟값을 출력 */
        st = new StringTokenizer(bf.readLine());
        Deque<Node> mydeq = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());

            while (!mydeq.isEmpty() && mydeq.getLast().value > now) {
                mydeq.removeLast();
            }
            mydeq.addLast(new Node(now, i));
            if (mydeq.getFirst().index <= i - L) {
                mydeq.removeFirst();
            }
            bw.write(mydeq.getFirst().value + " ");
        }
        bw.flush();
        bw.close();
    }
    static class Node{
        public int value;
        public int index;

        public Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}

