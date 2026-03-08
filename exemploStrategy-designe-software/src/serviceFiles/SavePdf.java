package serviceFiles;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class SavePdf implements SaveFileInterface {
    @Override
    public Path save(File file, Path path) throws IOException {
        Path destino = path.resolve(file.getName());
        return Files.move(file.toPath(),destino, StandardCopyOption.REPLACE_EXISTING);
    }
}
