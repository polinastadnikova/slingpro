
import java.awt.font.NumericShaper;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.Word;
import edu.stanford.nlp.parser.shiftreduce.ShiftReduceParser;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;
import edu.stanford.nlp.trees.Tree;
import org.w3c.dom.ranges.Range;

import javax.management.AttributeList;

/**
 * Adapted version of the
 * ShiftReduceParser by @author John Bauer
 * @author Polina Stadnikova
 */
public class ShiftReduceAdapted {
  public static void main(String[] args) {
    /** load the model, ignore the postagger */
    String modelPath = "edu/stanford/nlp/models/srparser/englishSR.ser.gz";
    //String taggerPath = "edu/stanford/nlp/models/pos-tagger/english-left3words/english-left3words-distsim.tagger";

    for (int argIndex = 0; argIndex < args.length; ) {
      switch (args[argIndex]) {
//        case "-tagger":
//          taggerPath = args[argIndex + 1];
//          argIndex += 2;
//          break;
        case "-model":
          modelPath = args[argIndex + 1];
          argIndex += 2;
          break;
        default:
          throw new RuntimeException("Unknown argument " + args[argIndex]);
      }
    }

//    String[] text = {"I", "was", "in", "plain", "clothes", "."};
//    String[] tags ={"PPIS1", "VBDZ", "II", "JJ", "NN2", "."};
//    //MaxentTagger tagger = new MaxentTagger(taggerPath);
   ShiftReduceParser model = ShiftReduceParser.loadModel(modelPath);
//    List<TaggedWord> sentence = new ArrayList<>();
//
//    for (int i=0;i<text.length; i++){
//      sentence.add(new TaggedWord(text[i],tags[i]));
//    }
//    System.out.println(sentence);
//    Tree tree = model.apply(sentence);
//    System.out.println(tree);

    List<File> files = listf("/home/polina/Dokumente/slingpro/rsc/shiftreduce_prepared");

    /** get parse trees for each file */
    for (File file : files){
        String records = new String();
        try {

          BufferedReader reader = new BufferedReader(new FileReader(file));
          File newfile = new File("/home/polina/Dokumente/slingpro/rsc/shiftreduce-parsed/"+file.toString().split("/")[7]+"/"+file.toString().split("/")[8]);
          newfile.getParentFile().mkdir();
          newfile.createNewFile();
          BufferedWriter writer = new BufferedWriter(new FileWriter(newfile));
          String line;
          String toWrite = "";
          while ((line = reader.readLine()) != null)
          {
            records = line;
          }
          reader.close();
          String[] sep=records.split("\\s+");
          ArrayList<ArrayList<String>> words = new ArrayList<ArrayList<String>>();
          ArrayList<ArrayList<String>> tags = new ArrayList<ArrayList<String>>();
          ArrayList<String> words_temp = new ArrayList<String>();
          ArrayList<String> tags_temp = new ArrayList<String>();
          for (String s : sep){
            if (s.contains("./.")){
              words_temp.add(s.split("/")[0]);
              tags_temp.add(s.split("/")[1]);
              words.add(words_temp);
              tags.add(tags_temp);
              words_temp = new ArrayList<String>();
              tags_temp = new ArrayList<String>();
            }
            else{
              words_temp.add(s.split("/")[0]);
              tags_temp.add(s.split("/")[1]);
            }
          }
          for (int i=0;i<words.size(); i++){
            ArrayList<String> sentence = words.get(i);
            ArrayList<String> labels = tags.get(i);
            List<TaggedWord> toParse = new ArrayList<>();
            for (int k=0;k<sentence.size(); k++){
              toParse.add(new TaggedWord(sentence.get(k),labels.get(k)));
            }
            Tree tree = model.apply(toParse);
            toWrite += tree.toString()+"\n";
          }
          writer.write(toWrite);
          reader.close();
          writer.close();
        }
        catch (Exception e)
        {
          System.err.format("Exception occurred trying to read '%s'.", file);
          e.printStackTrace();
        }
    }

    //DocumentPreprocessor tokenizer = new DocumentPreprocessor(new StringReader(text));
    //for (List<HasWord> sentence : text) {
      //System.out.println(sentence);
      //List<TaggedWord> tagged = tagger.tagSentence(sentence);
      //System.err.println(tagged);
      //Tree tree = model.apply(sentence);
      //System.err.println(tree);
    //}
  }

  /** get all file and subfolders in the directory*/
  public static List<File> listf(String directoryName) {
    File directory = new File(directoryName);

    List<File> resultList = new ArrayList<File>();

    // get all the files from a directory
    File[] fList = directory.listFiles();
    //resultList.addAll(Arrays.asList(fList));
    for (File file : fList) {
      if (file.isFile()) {
        resultList.add(file);
        //System.out.println(file.getAbsolutePath());
      } else if (file.isDirectory()) {
        resultList.addAll(listf(file.getAbsolutePath()));
      }
    }
    //System.out.println(fList);
    return resultList;
  }

}
