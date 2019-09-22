import java.nio.file.*;
import java.io.*;

public class RootDirs {
    public static void main(String[] args) {
        for (Path name : FileSystems.getDefault().getRootDirectories()) {
            System.out.println("\nRoot Directory: " + name.getFileName());
            try (DirectoryStream<Path> stream = Files.newDirectoryStream(name)) {
                for (Path file : stream) {
                    System.out.println("\nSubDirectory: " + file.getFileName());
                    try (DirectoryStream<Path> subStream = Files.newDirectoryStream(file)) {
                        for (Path file2 : subStream) {
                            System.out.println(file2.getFileName());
                        }
                    }
                    catch (IOException e) {
                        System.out.println(e.getMessage());
                    }
                }
            }
            catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
