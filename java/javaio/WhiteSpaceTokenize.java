import java.io.*;
import java.util.Scanner;

public class WhiteSpaceTokenize {

    public static void main(String[] args) {

        if (args.length != 1) {
            System.out.println("Usage: java WhiteSpaceTokenize <file>");
            System.exit(0);
        }

        try (Scanner s = new Scanner(new BufferedReader(new FileReader(args[0])))) {
            while (s.hasNext()) {
                System.out.println(s.next());
            }
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
