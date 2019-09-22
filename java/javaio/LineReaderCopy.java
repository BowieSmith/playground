import java.io.*;

public class LineReaderCopy {
    
    public static void main(String[] args) throws IOException {

        if (args.length != 2) {
            System.out.println("Usage: LineReaderCopy src dest");
        }

        BufferedReader inputStream = null;
        PrintWriter outputStream = null;

        try {

            inputStream = new BufferedReader(new FileReader(args[0]));
            outputStream = new PrintWriter(new FileWriter(args[1]));
        
            String l;
            while ((l = inputStream.readLine()) != null){
                outputStream.println(l);
            }

        }
        finally {
            if (inputStream != null) {
                inputStream.close();
            }

            if (outputStream != null) {
                outputStream.close();
            }
        }
    }
}
