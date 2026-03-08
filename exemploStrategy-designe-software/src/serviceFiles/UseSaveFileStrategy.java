package serviceFiles;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;

public class UseSaveFileStrategy {
    private SaveFileInterface strategy;

    public void setStrategy(SaveFileInterface strategy) {
        this.strategy = strategy;
    }

    public Path executeStrategy(File file, Path path) throws IOException {
        return strategy.save(file,path);
    }

}
