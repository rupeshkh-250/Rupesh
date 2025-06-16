// Java Code (Apache Beam)
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.Count;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.transforms.SimpleFunction;
import org.apache.beam.sdk.values.KV;

public class WordCount {

    public static void main(String[] args) {
        PipelineOptions options = PipelineOptionsFactory.fromArgs(args).withValidation().create();
        Pipeline pipeline = Pipeline.create(options);

        pipeline.apply("ReadLines", TextIO.read().from("input.txt"))
                .apply("ExtractWords", MapElements.via(new SimpleFunction<String, String>() {
                    @Override
                    public String apply(String line) {
                        return line.toLowerCase().trim();
                    }
                }))
                .apply("CountWords", Count.perElement())
                .apply("FormatResults", MapElements.via(new SimpleFunction<KV<String, Long>, String>() {
                    @Override
                    public String apply(KV<String, Long> wordCount) {
                        return wordCount.getKey() + ": " + wordCount.getValue();
                    }
                }))
                .apply("WriteCounts", TextIO.write().to("output.txt").withNumShards(1));
        pipeline.run().waitUntilFinish();
    }
}
