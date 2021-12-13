import java.util.Scanner;

import java.util.ArrayList;

public class Ocean {
    private static ArrayList<LanternFish> fish = new ArrayList<>();

    public static void main(String[] args) {
        Scanner inputscan = new Scanner(System.in);
        System.out.println("Please input your input");
        String[] input = inputscan.nextLine().split(",");
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