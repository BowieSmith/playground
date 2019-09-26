import java.util.*;

public class HeapSort {
    public static void main(String[] args) {
        List<Object> list = new ArrayList<>();
        for (String arg : args) {
            list.add(arg);
        }
        System.out.println(HeapSort.sort(list));
    }

    public static <T> List<T> sort(Collection<? extends T> c) {
        List<T> sortedList = new ArrayList<>();
        Queue<T> pq = new PriorityQueue<>(c);

        while (pq.peek() != null) {
            sortedList.add(pq.remove());
        }

        return sortedList;
    }
}
