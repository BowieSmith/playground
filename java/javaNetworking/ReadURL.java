import java.net.*;
import java.io.*;

public class ReadURL {
    public static void main(String[] args) throws Exception {
        URL url = new URL(args[0]);
        try (BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()))) {
            in.lines().forEach(System.out::println);
        }
    }
}
