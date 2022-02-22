import numpy as np


# loss = (wx+b-y)**2
def compute_error_for_line_given_points(b, w, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]  # 每一个点的x值
        y = points[i, 1]  # y值
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points))


# 梯度函数
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # b和w的梯度  L对w,b求导。 除以N是因为梯度是累加的，就不用求平均了
        b_gradient += -(2 / N) * (y - ((w_current * x) + b_current))
        w_gradient += -(2 / N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b, new_w]


def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate)
    return [b, w]


def run():
    # !!!data.csv为100个点，文件确实
    points = np.genfromtxt('./data/linear.csv', delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_w = 0
    num_iterations = 1000
    print("Starting gradient descent at b={0},w={1},error={2}".format(
        initial_b, initial_w,
        compute_error_for_line_given_points(initial_b, initial_w, points)
    ))
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After{0} iteration b={1},w={2},error={3}".format(
        num_iterations, b, w, compute_error_for_line_given_points(b, w, points)
    ))


if __name__ == '__main__':
    run()
