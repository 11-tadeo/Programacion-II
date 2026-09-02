import java.util.Scanner;

public class EcuacionCuadratica {
    private double a;
    private double b;
    private double c;

    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return (b * b) - (4 * a * c);
    }

    public double getRaiz1() {
        return (-b + Math.sqrt(getDiscriminante())) / (2 * a);
    }

    public double getRaiz2() {
        return (-b - Math.sqrt(getDiscriminante())) / (2 * a);
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese a, b, c: ");
        double a = entrada.nextDouble();
        double b = entrada.nextDouble();
        double c = entrada.nextDouble();

        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);

        if (ecuacion.getDiscriminante() > 0) {
            System.out.println("La ecuación tiene dos raíces: " + ecuacion.getRaiz1() + " y " + ecuacion.getRaiz2());
        } else if (ecuacion.getDiscriminante() == 0) {
            System.out.println("La ecuación tiene una raíz: " + ecuacion.getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales.");
        }

        entrada.close();
    }
}