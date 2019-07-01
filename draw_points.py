import cv2
from mtcnn.mtcnn import MTCNN

color = [0, 255, 255]
color1 = [0, 255, 0]
color2 = [255, 0, 0]
color3 = [255, 0, 255]

def show_points(frame, box, keypoints, alpha, beta):

    (x, y, w, h) = box
    dep_y = int(h * alpha)
    dep_x = int(w * beta)

    le = keypoints['left_eye']
    re = keypoints['right_eye']
    lm = keypoints['mouth_left']
    rm = keypoints['mouth_right']
    no = keypoints['nose']

    cv2.circle(frame, (le), 2, color, 2)
    cv2.circle(frame, (re), 2, color, 2)
    cv2.circle(frame, (no), 2, color, 2)
    cv2.circle(frame, (lm), 2, color, 2)
    cv2.circle(frame, (rm), 2, color, 2)
    cv2.circle(frame, (x + int(w/2), y + h + dep_y), 2, color, 2)
    cv2.circle(frame, (x + w + dep_x, y + int(h/2)), 2, color, 2)
    cv2.circle(frame, (x + int(w/2), y-dep_y), 2, color, 2)
    cv2.circle(frame, (x-dep_x, y + int(h/2)), 2, color, 2)
    cv2.circle(frame, (x + w, y), 2, color, 2)
    cv2.circle(frame, (x, y), 2, color, 2)
    cv2.circle(frame, (x + w, y + h), 2, color, 2)
    cv2.circle(frame, (x, y+h), 2, color, 2)


def draw_lines(frame, box, keypoints, alpha, beta):

    (x, y, w, h) = box
    dep_y = int(h * alpha)
    dep_x = int(w * beta)

    le = keypoints['left_eye']
    re = keypoints['right_eye']
    lm = keypoints['mouth_left']
    rm = keypoints['mouth_right']
    no = keypoints['nose']

    cv2.line(frame, (le), (x + w, y + h), color1, 1)  # from left eye
    cv2.line(frame, (le), (x, y), color1, 1)
    cv2.line(frame, (le), (x, y + h), color1, 1)
    cv2.line(frame, (le), (x + w, y), color1, 1)
    cv2.line(frame, (le), (x - dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (le), (x + int(w / 2), y - dep_y), color1, 1)
    cv2.line(frame, (le), (x + w + dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (le), (x + int(w / 2), y + h + dep_y), color1, 1)

    cv2.line(frame, (re), (x + w, y + h), color1, 1)  # from left_nose
    cv2.line(frame, (re), (x, y), color1, 1)
    cv2.line(frame, (re), (x, y + h), color1, 1)
    cv2.line(frame, (re), (x + w, y), color1, 1)
    cv2.line(frame, (re), (x - dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (re), (x + int(w / 2), y - dep_y), color1, 1)
    cv2.line(frame, (re), (x + w + dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (re), (x + int(w / 2), y + h + dep_y), color1, 1)

    cv2.line(frame, (lm), (x + w, y + h), color1, 1)  # from left_mouth
    cv2.line(frame, (lm), (x, y), color1, 1)
    cv2.line(frame, (lm), (x, y + h), color1, 1)
    cv2.line(frame, (lm), (x + w, y), color1, 1)
    cv2.line(frame, (lm), (x - dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (lm), (x + int(w / 2), y - dep_y), color1, 1)
    cv2.line(frame, (lm), (x + w + 5, y + int(h / 2)), color1, 1)
    cv2.line(frame, (lm), (x + int(w / 2), y + h + dep_y), color1, 1)

    cv2.line(frame, (rm), (x + w, y + h), color1, 1)  # from right_mouth
    cv2.line(frame, (rm), (x, y), color1, 1)
    cv2.line(frame, (rm), (x, y + h), color1, 1)
    cv2.line(frame, (rm), (x + w, y), color1, 1)
    cv2.line(frame, (rm), (x - dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (rm), (x + int(w / 2), y - dep_y), color1, 1)
    cv2.line(frame, (rm), (x + w + dep_x, y + int(h / 2)), color1, 1)
    cv2.line(frame, (rm), (x + int(w / 2), y + h + dep_y), color1, 1)

    cv2.line(frame, (no), (x + w, y + h), (color3), 1)  # from nose
    cv2.line(frame, (no), (x, y), (color3), 1)
    cv2.line(frame, (no), (x, y + h), (color3), 1)
    cv2.line(frame, (no), (x + w, y), (color3), 1)
    cv2.line(frame, (no), (x - dep_x, y + int(h / 2)), (color3), 1)
    cv2.line(frame, (no), (x + int(w / 2), y - dep_y), (color3), 1)
    cv2.line(frame, (no), (x + w + dep_x, y + int(h / 2)), (color3), 1)
    cv2.line(frame, (no), (x + int(w / 2), y + h + dep_y), (color3), 1)


    cv2.line(frame, (x, y), (x + int(w / 2), y - dep_y), (color2), 1)
    cv2.line(frame, (x + int(w / 2), y - dep_y), (x + w, y), (color2), 1)
    cv2.line(frame, (x + w, y), (x + w + dep_x, y + int(h / 2)), (color2), 1)
    cv2.line(frame, (x + w + dep_x, y + int(h / 2)), (x + w, y + h), (color2), 1)
    cv2.line(frame, (x + w, y + h), (x + int(w / 2), y + h + dep_y), (color2), 1)
    cv2.line(frame, (x + int(w / 2), y + h + dep_y), (x, y + h), (color2), 1)
    cv2.line(frame, (x, y + h), (x - dep_x, y + int(h / 2)), (color2), 1)
    cv2.line(frame, (x - dep_x, y + int(h / 2)), (x, y), (color2), 1)

    cv2.line(frame, (le), (re), color1, 1)
    cv2.line(frame, (le), (rm), color1, 1)
    cv2.line(frame, (le), (lm), color1, 1)
    cv2.line(frame, (le), (no), color1, 1)
    cv2.line(frame, (re), (rm), color1, 1)
    cv2.line(frame, (re), (lm), color1, 1)
    cv2.line(frame, (re), (no), color1, 1)
    cv2.line(frame, (lm), (rm), color1, 1)
    cv2.line(frame, (lm), (no), color1, 1)
    cv2.line(frame, (rm), (no), color1, 1)





