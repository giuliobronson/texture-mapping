import numpy as np
import cv2

class TextureMapper:

    def __init__(self, canvas, texture):
        self.__canvas  = cv2.imread(canvas, 1)
        self.__texture = cv2.imread(texture, 1)
        self.__mapping = []
        self.__vertices = self.__get_texture_vertices()

    def __handle_click(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN: 
            cv2.putText(self.__canvas, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            self.__mapping.append(np.array((y, x)))

    def __get_texture_vertices(self):
        return [np.array((0, self.__texture.shape[0])), 
                np.array((self.__texture.shape[1], self.__texture.shape[0])), 
                np.array((self.__texture.shape[1], 0)), 
                np.array((0, 0))]

    def __get_T(self):
        A = np.zeros((12, 12))
        for i, point in enumerate(self.__mapping):
            A[3 * i:3 * (i + 1), :3] = np.append(point, 1)
        for i in range(A.shape[0]):
            A[i] = np.roll(A[i], 3 * (i % 3))
        for i in range(1, 4):
            A[3 * i:3 * (i + 1), 8 + i] = -np.append(self.__vertices[i], 1)

        b = np.zeros(12); b[:3] = np.append(self.__vertices[0], 1)
        x = np.linalg.solve(A, b); print(x)
        T = x[:9].reshape((3, 3)); print(T)

        return T
   
    def get_map(self):
        cv2.imshow('image', self.__canvas)
        cv2.setMouseCallback('image', self.__handle_click)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    def map(self):
        T = self.__get_T()
        for x in range(self.__canvas.shape[1]):
            for y in range(self.__canvas.shape[0]):
                texture_point = T @ np.array((x, y, 1)).T
                texture_point = texture_point.astype(int)
                if 0 <= texture_point[0] < self.__texture.shape[1] and 0 <= texture_point[1] < self.__texture.shape[0]:
                    self.__canvas[x, y] = self.__texture[texture_point[1], texture_point[0]]

        cv2.imshow('image', self.__canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()