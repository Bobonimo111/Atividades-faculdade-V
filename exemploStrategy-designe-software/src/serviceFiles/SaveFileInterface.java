package serviceFiles;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;

public interface SaveFileInterface {
    /**
    * @Param file arquivo que vai ser salvo ou transferido
    * @Param path caminho relativo ao definido nas varivais de ambiente, PATHS.HOME
     * @Return caminho aonde o arquivo foi salvo.
     **/
    Path save(File file, Path path) throws IOException;
}
