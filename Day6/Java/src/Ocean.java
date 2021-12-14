import java.util.Scanner;

import java.util.ArrayList;

public class Ocean {
    private static ArrayList<LanternFish> fish = new ArrayList<>();

    public static void main(String[] args) {
        Scanner inputscan = new Scanner(System.in);
        System.out.println("Please input your input");
        String[] input = "2,5,2,3,5,3,5,5,4,2,1,5,5,5,5,1,2,5,1,1,1,1,1,5,5,1,5,4,3,3,1,2,4,2,4,5,4,5,5,5,4,4,1,3,5,1,2,2,4,2,1,1,2,1,1,4,2,1,2,1,2,1,3,3,3,5,1,1,1,3,4,4,1,3,1,5,5,1,5,3,1,5,2,2,2,2,1,1,1,1,3,3,3,1,4,3,5,3,5,5,1,4,4,2,5,1,5,5,4,5,5,1,5,4,4,1,3,4,1,2,3,2,5,1,3,1,5,5,2,2,2,1,3,3,1,1,1,4,2,5,1,2,4,4,2,5,1,1,3,5,4,2,1,2,5,4,1,5,5,2,4,3,5,2,4,1,4,3,5,5,3,1,5,1,3,5,1,1,1,4,2,4,4,1,1,1,1,1,3,4,5,2,3,4,5,1,4,1,2,3,4,2,1,4,4,2,1,5,3,4,1,1,2,2,1,5,5,2,5,1,4,4,2,1,3,1,5,5,1,4,2,2,1,1,1,5,1,3,4,1,3,3,5,3,5,5,3,1,4,4,1,1,1,3,3,2,3,1,1,1,5,4,2,5,3,5,4,4,5,2,3,2,5,2,1,1,1,2,1,5,3,5,1,4,1,2,1,5,3,5,2,1,3,1,2,4,5,3,4,3".split(",");
        /*StringBuilder print = new StringBuilder();
        for (String s : input) {
            print.append(s + " ");
        }
        System.out.println(print);*/
        for (String i : input) {
            fish.add(new LanternFish(Integer.parseInt(i)));
        }
        System.out.println("How many days would you like to model?");
        int days = Integer.parseInt(inputscan.nextLine());
        for (int i = days; i > 0; i--) {
            System.out.println(i);
            for (int n = 0; n < fish.toArray().length; n++) {
                if (fish.get(n).getTimer() == 0) {
                    fish.add(new LanternFish());
                }
                fish.get(n).subTimer();
            }
            /*print = new StringBuilder();
            for (LanternFish l : fish) {
                print.append(l.getTimer()+" ");
            }
            System.out.println(print);*/
        }
        System.out.println(fish.toArray().length);
    }
}