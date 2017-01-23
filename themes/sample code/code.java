import java.io.File;

public class FileSizeExample { 
   public static void main(String[] args) { 
      File file = new File("C:\\Users\\TutorialsPoint7\\Desktop\\abc.png");
      if(file.exists()) { 
         double bytes = file.length();
         double kilobytes = (bytes / 1024);
         double megabytes = (kilobytes / 1024);
         double gigabytes = (megabytes / 1024);
         double terabytes = (gigabytes / 1024);
         double petabytes = (terabytes / 1024);
         double exabytes = (petabytes / 1024);
         double zettabytes = (exabytes / 1024);
         double yottabytes = (zettabytes / 1024);
         
         System.out.println("bytes : " + bytes);
         System.out.println("kilobytes : " + kilobytes);
         System.out.println("megabytes : " + megabytes);
         System.out.println("gigabytes : " + gigabytes);
         System.out.println("terabytes : " + terabytes);
         System.out.println("petabytes : " + petabytes);
         System.out.println("exabytes : " + exabytes);
         System.out.println("zettabytes : " + zettabytes);
         System.out.println("yottabytes : " + yottabytes);
      } else {
         System.out.println("File does not exists!");
      }
   }
}