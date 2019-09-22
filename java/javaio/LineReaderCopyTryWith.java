import java.io.*;

public class LineReaderCopyTryWith {
    
    public static void main(String[] args) throws IOException {

        if (args.length != 2) {
            System.out.println("Usage: LineReaderCopy src dest");
        }

        try ( 
            BufferedReader inputStream = new BufferedReader(new FileReader(args[0]));
            PrintWriter outputStream = new PrintWriter(new FileWriter(args[1]));
       ) { 
            String l;
            while ((l = inputStream.readLine()) != null){
                outputStream.println(l);
            }

        }
    }
}
