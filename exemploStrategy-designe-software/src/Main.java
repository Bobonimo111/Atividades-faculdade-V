import serviceFiles.SaveImage;
import serviceFiles.SavePdf;
import serviceFiles.UseSaveFileStrategy;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        UseSaveFileStrategy strategy = new UseSaveFileStrategy();
        strategy.setStrategy(new SaveImage());
        try {
            strategy.executeStrategy(new File(
                    "C:/Users/william/Downloads/moo.JPG"),
                    Path.of("C:/Users/william/Desktop/move_here/"));
        }catch (IOException io){
            System.out.println(io.getMessage());
        }
    }
}