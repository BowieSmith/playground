import java.net.*;
import java.io.*;
import java.util.*;

public class NetcatEcho {
    public static void main(String[] args) throws Exception {
        InetAddress host = InetAddress.getByName(args[0]);
        int port = Integer.parseInt(args[1]);

        Socket client = new Socket(host, port);
        BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
        new Thread(() -> in.lines().forEach(System.out::println)).start();

        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));
        new Thread(() -> {
            Scanner userInput = new Scanner(System.in);
            while (true) {
                try {
                    String input = userInput.nextLine();
                    out.write(input, 0, input.length());
                    System.out.println("Wrote: " + input);
                }
                catch (Exception e) {
                    System.out.println(e.getMessage());
                }
            }
        }).start();
    }
}
