public class ManyHellos {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java ManyHellos <numThreads> <numHellos>");
            System.exit(0);
        }
        try {
            for (int i = 0; i < Integer.parseInt(args[0]); i++) {
                Integer I = i + 1;
                (new Thread(() -> {
                    for (int j = 0; j < Integer.parseInt(args[1]); j++) {
                        System.out.println("Hello " + (j + 1) + " from thread " + I);
                    }
                })).start();
            }
        }
        catch (NumberFormatException e) {
            System.out.println("Must use integer: " + e.getMessage());
        }
    }
}
