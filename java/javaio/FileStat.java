import java.nio.file.*;
import java.nio.file.attribute.*;
import java.io.IOException;

public class FileStat {
    public static void main(String[] args) {
        try {
            BasicFileAttributes fileStat = Files.readAttributes(Paths.get(args[0]), PosixFileAttributes.class);
            System.out.println("creation: " + fileStat.creationTime());
            System.out.println("lastAccess: " + fileStat.lastAccessTime());
            System.out.println("lastModify: " + fileStat.lastModifiedTime());
            System.out.println("size: " + fileStat.size());
        }
        catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
