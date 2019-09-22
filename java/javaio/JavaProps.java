import java.util.Properties;

public class JavaProps {
    public static void main(String[] args) {
        Properties p = System.getProperties();
        p.forEach((k,v) -> System.out.println(k + ": " + v));
    }
}
