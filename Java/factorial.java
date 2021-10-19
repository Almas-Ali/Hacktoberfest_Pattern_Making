class Main {
  public static void main(String[] args) {
    System.out.println(factorial(4));
  }
  public static int factorial(int number) {
    int product = 1;
    while (number != 0) {
      product *= number;
      number--;
    }
    return product;
  }
}
