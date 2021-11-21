#!/usr/bin/env python
# Gradient-based feature detection for laser scans by KamilGos: github.com/KamilGos

import matplotlib.pyplot as plt
import numpy as np
import math
import json


def pol2cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return [x, y]


def extract_corners(data, threshold):
    """Extract corners in data using its gradient
    Args:
        data (list): data to find corners
        threshold (float): threshold for corner detection. Point is considered
            as corner when gradient is above this value
    Returns:
        [list, np.gradient]: list with found corners and gradient projection 
    """
    f = np.array(data)
    grad = np.gradient(f)
    corners_iter = []
    for i in range(len(data)):
        if grad[i] > threshold or grad[i] < -threshold:
            corners_iter.append(i)
    return corners_iter, grad


def corners_iter_to_cartesian(corners_iter, data):
    x = np.arange(0, len(data))
    angle = (np.pi / len(data)) * x
    corners = np.zeros(shape=[len(corners_iter), 2])
    for i in range(len(corners_iter)):
        corners[i, :] = pol2cart(rho=data[corners_iter[i]], phi=angle[corners_iter[i]])
    return corners


def plot_dist_angle(distance):
    x = np.arange(0, len(distance))
    angle = (360 / len(distance)) * x
    pad = plt.figure()
    ax1 = pad.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.plot(angle, distance, 'b.')
    plt.title("Distance of Angle")
    plt.xlabel("Angle [Degrees]")
    plt.ylabel("Distance")

def plot_dist_angle_with_gradient_and_corners(data, gradient, corners_iter):
    x = np.arange(0, len(data))
    angle = (360 / len(data)) * x
    padwg = plt.figure()
    ax1 = padwg.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.plot(angle, data, 'b-')
    plt.title("As Distance of Angle with Gradient and Corners")
    plt.xlabel("Angle [Degrees]")
    plt.ylabel("Distance")
    ax2 = ax1.twinx()
    ax2.plot(angle, gradient, 'r-')

    corners_angle = []
    corners_dist = []
    for i in corners_iter:
        corners_angle.append(angle[i])
        corners_dist.append(data[i])
    ax1.plot(corners_angle, corners_dist, 'go')


def plot_as_polar(data):
    x = np.arange(0, len(data))
    theta = (np.pi / len(data)) * x
    pap = plt.figure()
    ax1 = pap.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    ax1.plot(theta, data, '.')
    plt.title("As Polar")


def plot_as_cartesian(data):
    pac = plt.figure()
    ax1 = pac.add_axes([0.1, 0.1, 0.8, 0.8])
    plt.plot(data[:, 0], data[:, 1], '.')
    plt.title("As Cartesian")
    plt.xlabel("X")
    plt.ylabel("Y")


def plot_as_cartesian_with_corners(data, corners):
    pac = plt.figure()
    ax1 = pac.add_axes([0.1, 0.1, 0.8, 0.8])
    plt.plot(data[:, 0], data[:, 1], '.')
    plt.plot(corners[:, 0], corners[:, 1], 'ro')
    plt.title("As Cartesian with detected corners")
    plt.xlabel("X")
    plt.ylabel("Y")


def show_plots():
    plt.show()


if __name__=="__main__":
    json_file = open('data/data_stereo_fwd.json')
    data = json.load(json_file)
    data = data[2]["scan"]  
    print("Length of data: ", len(data))
    plot_as_polar(data=data)
    plot_dist_angle(distance=data)

    corners_iter, grad_fcn = extract_corners(data=data, threshold=0.05)
    corners_grad = corners_iter_to_cartesian(corners_iter=corners_iter, data=data)
    plot_dist_angle_with_gradient_and_corners(data=data, gradient=grad_fcn, corners_iter=corners_iter)

    # converting polar data to Cartesian
    x = np.arange(0, len(data))
    phi = (np.pi / len(data)) * x
    data_cart = np.zeros(shape=[len(data), 2])
    for i in range(len(data)):
        data_cart[i, :] = pol2cart(data[i], phi[i])

    plot_as_cartesian_with_corners(data=data_cart, corners=corners_grad)
    show_plots()