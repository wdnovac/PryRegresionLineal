#Programa de Regresion Lineal Platzi
#Creado por Walter Nova 14-06-21
import numpy as np
import matplotlib.pyplot as plt


def estimate_bo_b1(x,y):
    n=np.size(x)
    #obtenemos los promedios de X y Y
    m_x, m_y=np.mean(x), np.mean(y)
    #Calcular sumatoria de XY y mi sumatoria de XX
    Sumatoria_xy=np.sum((x-m_x)*(y-m_y))
    Sumatoria_xx=np.sum(x*(x-m_x))
    #Coeficientes de regresion
    b_1=Sumatoria_xy/Sumatoria_xx
    b_0=m_y-b_1*m_x

    return (b_0,b_1)

#funcion para graficar
def plot_regression (x,y,b):
    plt.scatter(x,y,color="g", marker="o", s=30 )

    y_pred=b[0]+b[1]*x
    plt.plot(x, y_pred, color="b")

    #etiquetado
    plt.xlabel('x-Indepediente')
    plt.ylabel('y-Dependiente')

    plt.show()



def run():
    x=np.array([1,2,3,4,5])
    y=np.array([2,3,5,6,5])

    #obtenemos b1 y b2
    b=estimate_bo_b1(x,y)
    print("Los valores de b0={}, b1={}".format(b[0],b[1]))
    plot_regression(x,y,b)


if __name__=='__main__':
    run()

