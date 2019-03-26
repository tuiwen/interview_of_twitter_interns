import java.util.Random;

public class mkdate {
    public static void main(String args[]) {
        // create instance of Random class
        Random rand = new Random();
        int cnt = 0, wall = 0;
        if(args.length != 2) {
            System.out.println("usage:\n\tmkdate <interger>\n");
            System.exit(1);
        }
        System.out.println(args);
        wall = Integer.valueOf(args[1]);
        if(wall <= 0 && wall > (2 >> 16)) {
            System.out.println("error: input must be a positive integer\n");
            System.exit(1);
        }
        wall *= 10000;

        while(cnt < wall) {
            String randDate = String.format(
                                  "%d-%d-%d %d:%d:%d",
                                  rand.nextInt(20) + 2000,
                                  rand.nextInt(12) + 1,
                                  rand.nextInt(31) + 1,
                                  rand.nextInt(24) + 1,
                                  rand.nextInt(60) + 1,
                                  rand.nextInt(60) + 1);
            System.out.println(randDate);
            cnt++;
        }
    }
}

// javac mkdate.java && java mkdate main 1