import java.util.Random;

class Cronometro {
    private double inicia;
    private double finaliza;

    public Cronometro() {
        this.inicia = System.currentTimeMillis();
    }

    public double getInicia() {
        return this.inicia;
    }

    public double getFinaliza() {
        return this.finaliza;
    }

    public void inicia() {
        this.inicia = System.currentTimeMillis();
    }

    public void detener() {
        this.finaliza = System.currentTimeMillis();
    }

    public double lapsoDeTiempo() {
        return this.finaliza - this.inicia;
    }
}

public class Main {
    public static void ordenacionPorSeleccion(int[] arreglo) {
        int n = arreglo.length;
        for (int i = 0; i < n - 1; i++) {
            int indiceMinimo = i;
            for (int j = i + 1; j < n; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }
            int temp = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = temp;
        }
    }

    public static void main(String[] args) {
        int tamano = 100000;
        int[] numeros = new int[tamano];
        Random random = new Random();

        for (int i = 0; i < tamano; i++) {
            numeros[i] = random.nextInt(100000);
        }

        Cronometro cronometro = new Cronometro();

        System.out.println("Iniciando la ordenación por selección de " + tamano + " elementos...");
        
        cronometro.inicia();
        ordenacionPorSeleccion(numeros);
        cronometro.detener();

        System.out.println("Ordenación finalizada.");
        System.out.println("Tiempo transcurrido: " + cronometro.lapsoDeTiempo() + " ms.");
    }
}