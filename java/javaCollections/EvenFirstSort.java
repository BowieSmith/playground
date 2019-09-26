import java.util.*;
import java.util.stream.*;
import java.io.*;

public class EvenFirstSort {

    private String usage = "java EvenFirstSort\n" +
                           "  Integers fed through stdin, space delimited";

    private static Comparator<Integer> evenFirstComparator = new Comparator<Integer>() {
        public int compare(Integer a, Integer b) {
            if (a == b) {
                return 0;
            }
            if (a % 2 == 0 && b % 2 == 0) {
                return a.compareTo(b);
            }
            if (a % 2 == 1 && b % 2 == 1) {
                return a.compareTo(b);
            }
            if (a % 2 == 0) {
                return -1;
            }
            else {
                return 1;
            }
        }
    };

    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> intList = in
            .lines()
            .map(s -> s.split("\\s+"))
            .flatMap(arr -> Arrays.stream(arr)
                    .filter(str -> !str.equals(""))
                    .map(str -> Integer.parseInt(str)))
            .collect(Collectors.toList());

        Collections.sort(intList, evenFirstComparator);
        System.out.println(intList);
    }
}
