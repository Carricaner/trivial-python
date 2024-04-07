import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5, 6])
    np.save("save_numpy_sample_here", a)
    # save the sata into a file with extension as ".npy"
    b = np.load("save_numpy_sample_here" + ".npy")
    print(b)
    # [1 2 3 4 5 6]

    csv_arr = np.array([10, 2, 3, 4, 5, 6, 7, 8])
    np.savetxt("new_file.csv", csv_arr)
    np.loadtxt("new_file.csv")

    data = [['Billie Holiday', 'Jazz', 1300000, 27000000],
            ['Jimmie Hendrix', 'Rock', 2700000, 70000000],
            ['Miles Davis', 'Jazz', 1500000, 48000000],
            ['SIA', 'Pop', 2000000, 74000000]]
    df = pd.DataFrame(data, columns=['Artist', 'Genre', 'Albums Sold', 'Plays'])
    df.to_csv("music.csv", index=False)

    x = pd.read_csv('music.csv', header=0).values
    print(x)
    # [['Billie Holiday' 'Jazz' 1300000 27000000]
    #  ['Jimmie Hendrix' 'Rock' 2700000 70000000]
    #  ['Miles Davis' 'Jazz' 1500000 48000000]
    #  ['SIA' 'Pop' 2000000 74000000]]
    x = pd.read_csv('music.csv', usecols=['Artist', 'Plays']).values
    print(x)
    # [['Billie Holiday' 27000000]
    #  ['Jimmie Hendrix' 70000000]
    #  ['Miles Davis' 48000000]
    #  ['SIA' 74000000]]

    a = np.array([[-2.58289208, 0.43014843, -1.24082018, 1.59572603],
                  [0.99027828, 1.17150989, 0.94125714, -0.14692469],
                  [0.76989341, 0.81299683, -0.95068423, 0.11769564],
                  [0.20484034, 0.34784527, 1.96979195, 0.51992837]])

    df = pd.DataFrame(a)
    print(df)
    #           0         1         2         3
    # 0 -2.582892  0.430148 -1.240820  1.595726
    # 1  0.990278  1.171510  0.941257 -0.146925
    # 2  0.769893  0.812997 -0.950684  0.117696
    # 3  0.204840  0.347845  1.969792  0.519928
    df.to_csv('pd.csv')
    data = pd.read_csv('pd.csv')
    np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')

    a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    plt.plot(a)
    plt.show()
    x = np.linspace(0, 5, 20)
    y = np.linspace(0, 10, 20)
    plt.plot(x, y, 'purple')  # line
    plt.plot(x, y, 'o')  # dots
    plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    X = np.arange(-5, 5, 0.15)
    Y = np.arange(-5, 5, 0.15)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
    plt.show()
