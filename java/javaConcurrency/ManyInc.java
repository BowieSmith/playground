public class ManyInc {
    private static int classInt = 0;
    public static void main(String[] args) {
        for (int i = 0; i < Integer.parseInt(args[0]); i++) {
            (new Thread(() -> {
                for (int j = 0; j < Integer.parseInt(args[1]); j++) {
                    synchronized(ManyInc.class) {
                        classInt += 1;
                    }
                }
                System.out.println("classInt: " + classInt);
            })).start();
        }
    }
}
