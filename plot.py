import matplotlib.pyplot as plt

plt.ion()
def find(i):
    x1 = [0 for j in range(i)]
    print("x1:{}".format(x1))
    # plt.gca().cla() # optionally clear axes

    x2 = [0 for j in range(20,20+i)]

    plt.plot(x1)
    plt.plot(x2)
    plt.legend(["Dataset1","Dataset2"])
    plt.title(str(i+1))

    plt.draw()
    plt.pause(0.1)
for i in range(100):
    find(i)


#plt.show(block=True) # block=True lets the window stay open at the end of the animation.