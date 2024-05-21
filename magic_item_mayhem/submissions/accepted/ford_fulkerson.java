// Don't include this. It makes problemtools give a run time error
// package magic_item_mayhem.submissions.accepted;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.LinkedList;

public class ford_fulkerson {
	public static void main(String[] args) {
        new ford_fulkerson().Solve();
	}

    Node source = new Node();
    Node sink = new Node();

    public ford_fulkerson() {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            String[] a = reader.readLine().strip().split(" ");
            int N = Integer.parseInt(a[0]);
            int M = Integer.parseInt(a[1]);

            Dictionary<String,Node[]> playerCategories = new Hashtable<>();

            for (int i = 0; i < N; i++) {
                String name = reader.readLine().strip();

                Node player = new Node();
                Connect(source,player,3);
                playerCategories.put(name, new Node[5]);

                for (int j = 0; j < 5; j++) {
                    Node category = new Node();
                    Connect(player, category, 1);
                    playerCategories.get(name)[j] = category;
                }
            }

            for (int i = 0; i < M; i++) {
                String[] itemData = reader.readLine().strip().split(" ");

                int category = Integer.parseInt(itemData[0]) - 1;
                Node item = new Node();
                Connect(item, sink, 1);

                for (int j = 1; j < itemData.length; j++) {
                    Node playerCategory = playerCategories.get(itemData[j])[category];
                    Connect(playerCategory, item, 1);
                }
            }

            reader.close();
        } catch (Exception e) { System.out.println(e);}
    }

    public void Connect(Node from, Node to, int capacity) {
        from.neighbors.put(to, capacity);
        to.neighbors.put(from, 0);
    }

    public class Node {
        Dictionary<Node,Integer> neighbors = new Hashtable<>();
    }

    public boolean DFS(Dictionary<Node,Node> path) {
        HashSet<Node> visited = new HashSet<>();
        LinkedList<Node> queue = new LinkedList<>();
        visited.add(source);
        queue.add(source);

        while (!queue.isEmpty()) {
            Node current = queue.pop();
            Enumeration<Node> e = current.neighbors.keys();
            while (e.hasMoreElements()) {
                Node next = e.nextElement();
                if (current.neighbors.get(next) > 0 && !visited.contains(next)) {
                    path.put(next, current);
                    if (next == sink) return true;
                    visited.add(next);
                    queue.add(next);
                }
            }
        }
        return false;
    }

    public void Solve() {
        Dictionary<Node,Node> path = new Hashtable<>();
        while (DFS(path)) {
            Node node = sink;
            while (node != source) {
                Node prev = path.get(node);
                prev.neighbors.put(node, prev.neighbors.get(node) - 1);
                node.neighbors.put(prev, node.neighbors.get(prev) + 1);
                node = prev;
            }
        }

        Enumeration<Integer> e = sink.neighbors.elements();
        int sum = 0;
        while (e.hasMoreElements()) sum += e.nextElement();
        System.out.println(sum);
    }
}

