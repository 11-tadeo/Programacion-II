import java.util.Scanner;

public class Estadistica {
    private float[] datos;

    public Estadistica(float[] datos) {
        this.datos = datos;
    }

    public float promedio() {
        float suma = 0;
        for (float dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }

    public float desviacionEstandar() {
        float prom = promedio();
        float sumaDiferenciasCuadrado = 0;

        for (float dato : datos) {
            sumaDiferenciasCuadrado += Math.pow(dato - prom, 2);
        }

        return (float) Math.sqrt(sumaDiferenciasCuadrado / (datos.length - 1));
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] numeros = new float[10];

        System.out.println("Ingresa 10 números:");
        for (int i = 0; i < 10; i++) {
            numeros[i] = entrada.nextFloat();
        }

        Estadistica estadistica = new Estadistica(numeros);

        System.out.println("El promedio es: " + estadistica.promedio());
        System.out.println("La desviación estándar es: " + estadistica.desviacionEstandar());

        entrada.close();
    }
}