import java.util.*;
import java.util.stream.*;

public class BookRecs {
    public static void main(String[] args) {
        List<Customer> customers = new ArrayList<>(
                Arrays.asList(
                    new Customer("Bob", Arrays.asList(
                            new Purchase("book", "SICP"),
                            new Purchase("book", "CLRS"),
                            new Purchase("car", "Soul"))),
                    new Customer("Sara", Arrays.asList(
                            new Purchase("car", "Kia"),
                            new Purchase("book", "OTR"))),
                    new Customer("Mike", Arrays.asList(
                            new Purchase("book", "CLRS"),
                            new Purchase("bike", "XRS"),
                            new Purchase("book", "SICP")))));

        System.out.println("Customer List:");
        customers
            .stream()
            .forEach(System.out::println);

        System.out.println("\nPurchases List:");
        List<Purchase> allPurchases = customers
            .stream()
            .map(c -> c.purchases)
            .flatMap(List::stream)
            .collect(Collectors.toList());
        allPurchases
            .stream()
            .forEach(System.out::println);

        System.out.println("\nBooks List:");
        List<String> allBooks = allPurchases
            .stream()
            .filter(p -> p.type.equals("book"))
            .map(p -> p.name)
            .collect(Collectors.toList());
        allBooks
            .stream()
            .forEach(System.out::println);

        System.out.println("\nBook Totals:");
        Map<String, Integer> bookTotals = new HashMap<>();
        allBooks
            .stream()
            .forEach(b -> bookTotals.put(b, bookTotals.getOrDefault(b, 0) + 1));
        System.out.println(bookTotals);

        bookTotals
            .entrySet()
            .stream()
            .sorted(Map.Entry.comparingByValue((i, j) -> j - i))
            .forEach(System.out::println);
    }
}

class Customer {
    public Customer(String name, List<Purchase> purchases) {
        this.name = name;
        this.purchases = purchases;
    }
    public String toString() {
        StringBuilder sb = new StringBuilder("Customer '" + name + "': ");
        for (Purchase p : purchases) {
            sb.append(p + ", ");
        }
        return sb.toString();
    }
    public String name;
    public List<Purchase> purchases;
}

class Purchase {
    public Purchase(String type, String name) {
        this.type = type;
        this.name = name;
    }
    public String toString() {
        return "[ " + type + ", " + name + " ]";
    }
    public String type;
    public String name;
}
