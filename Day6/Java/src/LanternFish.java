public class LanternFish {
    private int timer;

    public LanternFish(int timer) {
        this.timer = timer;
    }

    public LanternFish() {
        this(9);
    }

    public void subTimer() {
        if (this.timer == 0) {
            this.timer=6;
        } else{
            this.timer--;
        }
    }

    public int getTimer() {
        return this.timer;
    }
}
