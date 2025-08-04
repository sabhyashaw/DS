class A {
    int len = 5;
    int wide = 10;

    void abc() {
        int area = len * wide;
        System.out.println(area);
    }
}

class Main {
    public static void main(String args[]) {
        A obj = new A();
        obj.abc();
    }
}
