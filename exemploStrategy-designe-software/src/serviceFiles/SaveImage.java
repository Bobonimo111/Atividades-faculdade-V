package serviceFiles;

import javax.imageio.IIOImage;
import javax.imageio.ImageIO;
import javax.imageio.ImageWriteParam;
import javax.imageio.ImageWriter;
import javax.imageio.stream.ImageOutputStream;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.Iterator;

public class SaveImage implements SaveFileInterface {

    @Override
    public Path save(File file, Path path) throws IOException {

        BufferedImage inputImage = ImageIO.read(file);
        String[] nomeDeArquivoSplitado = file.getName().split("\\.");
        Iterator<ImageWriter> writers = ImageIO.getImageWritersByFormatName(nomeDeArquivoSplitado[nomeDeArquivoSplitado.length-1]);
        ImageWriter writer = writers.next();

        /* Inicio Area de compressão */
        ImageWriteParam params = writer.getDefaultWriteParam();
        params.setCompressionMode(ImageWriteParam.MODE_EXPLICIT);
        params.setCompressionQuality(0.5f);
        /* Fim Area de compressão */
        Path destinoComNomeDeArquivo = path.resolve(file.getName());
        ImageOutputStream outputStream = ImageIO.createImageOutputStream(new File(destinoComNomeDeArquivo.toUri()));
        writer.setOutput(outputStream);

        writer.write(null, new IIOImage(inputImage, null, null), params);
        outputStream.close();
        writer.dispose();

        return null;
    }
}
