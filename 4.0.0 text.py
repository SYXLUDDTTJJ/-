import math
import tkinter as tk
import turtle
import time


def calculate_numbers():
    a = input_integer('第一个数：')
    b = input_integer('第二个数：')
    c = input_integer('a的几次方：')
    d = input_integer('b的几次方：')

    # 计算各项值
    max_comm_factor = calculate_max_common_factor(a, b)
    min_comm_multiple = a * b // max_comm_factor
    product = a * b
    quotient = a / b
    sum_ = a + b
    difference = a - b
    a_squared = pow(a, 2)
    b_squared = pow(b, 2)
    a_to_c = pow(a, c)
    b_to_d = pow(b, d)

    # 输出计算结果
    print('最大公因数：', max_comm_factor)
    print('最小公倍数：', min_comm_multiple)
    print('它们的积是：', product)
    print('它们的商是：', quotient)
    print('它们的和是：', sum_)
    print('它们的差是：', difference)
    print('a的乘方2是：', a_squared)
    print('b的乘方2是：', b_squared)
    print('a的乘方', c, '是：', a_to_c)
    print('b的乘方', d, '是：', b_to_d)


def input_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print('输入格式有误，请重新输入！')
    return value


def calculate_max_common_factor(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
def calculate_cylinder():
    radius = input_positive_number_half('半径是：')
    height = input_positive_number_tall('高是：')
    digits = input_precision('保留小数点后几位，最多六位：')
    unit = input('单位是：')

    # 计算圆柱体
    surface_area = round(2 * math.pi * radius ** 2 + 2 * math.pi * radius * height, digits)
    lateral_area = round(2 * math.pi * radius * height, digits)
    base_area = round(math.pi * radius ** 2, digits)
    volume = round(base_area * height, digits)

    # 输出计算结果
    print('体积是：', volume, unit, '的立方')
    print('表面积是：', surface_area, unit, '的平方')
    print('侧面积是：', lateral_area, unit, '的平方')
    print('底面积是：', base_area, unit, '的平方')


def yuanzhu_input_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            break
        except ValueError:
            print('输入格式有误，必须输入正数！')
    return value


def input_precision(prompt):
    while True:
        try:
            value = int(input(prompt))
            if not (0 <= value <= 6):
                raise ValueError
            break
        except ValueError:
            print('输入格式有误，必须是 0~6 的整数！')
    return value

def yuan_calculate_circle():
    radius = input_positive_number('半径是：')
    digits = input_precision('保留小数点后几位，最多六位：')
    unit = input('单位是：')

    # 计算圆的周长和面积
    area = round(math.pi * radius ** 2, digits)
    perimeter = round(2 * math.pi * radius, digits)

    # 输出计算结果
    print('面积是：', area, unit, '的平方')
    print('周长是：', perimeter, unit)


def yuan_input_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            break
        except ValueError:
            print('输入格式有误，必须输入正数！')
    return value


def TULTLE_input_precision(prompt):
    while True:
        try:
            value = int(input(prompt))
            if not (0 <= value <= 6):
                raise ValueError
            break
        except ValueError:
            print('输入格式有误，必须是 0~6 的整数！')
    return value


def draw_turtle_figure(length, width, height):
    if not valid_dimensions(length, width, height):
        return -1

    # 计算比例尺
    scale = length // 100 + 1

    # 绘制图形
    pen = turtle.Turtle()

    print('这个图形与原大小的比例是 1:', scale)
    pen.setposition(0, height / scale)
    pen.setposition(length / scale, height / scale)
    pen.setposition(length / scale, scale)
    pen.setposition(0, 0)
    pen.setposition(0, height / scale)

    pen.left(45)
    pen.forward(width / (2 * scale))
    pen.right(45)
    pen.forward(length / scale)
    pen.right(135)
    pen.forward(width / (2 * scale))
    pen.left(180)
    pen.forward(width / (2 * scale))
    pen.right(135)
    pen.forward(height / scale)
    pen.right(45)
    pen.forward(width / (2 * scale))

    time.sleep(5)
    pen.home()
    pen.clear()

    # 关闭 turtle 窗口
    turtle.done()


def precision_validate(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        print('输入值必须是正数！')
        return False
    if length <= height or width <= height:
        print('长度和宽度必须大于高度！')
        return False
    return True
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title('Calculator')

        # 创建控件

        # 创建一个 Notebook 控件并将各页作为它的选项卡添加到其中
        self.notebook = tk.ttk.Notebook(master)
        self.circle_tab = tk.Frame(self.notebook)
        self.cylinder_tab = tk.Frame(self.notebook)
        self.turtle_tab = tk.Frame(self.notebook)
        self.notebook.add(self.circle_tab, text='圆')
        self.notebook.add(self.cylinder_tab, text='圆柱体')
        self.notebook.add(self.turtle_tab, text='绘制图形')
        self.notebook.pack(padx=10, pady=10)

        # 创建圆的计算页面控件
        radius_label = tk.Label(self.circle_tab, text='半径')
        radius_label.grid(row=0, column=0)
        self.radius_entry = tk.Entry(self.circle_tab)
        self.radius_entry.grid(row=0, column=1)
        precision_label = tk.Label(self.circle_tab, text='保留小数点后几位')
        precision_label.grid(row=1, column=0)
        self.precision_entry = tk.Entry(self.circle_tab, validate='key', validatecommand=(self.precision_validate, '%P'))
        self.precision_entry.grid(row=1, column=1)
        unit_label = tk.Label(self.circle_tab, text='单位')
        unit_label.grid(row=2, column=0)
        self.unit_entry = tk.Entry(self.circle_tab)
        self.unit_entry.grid(row=2, column=1)
        calculate_button = tk.Button(self.circle_tab, text='计算', command=self.calculate_circle)
        calculate_button.grid(row=3, columnspan=2)

        # 创建圆柱体的计算页面控件
        radius_label = tk.Label(self.cylinder_tab, text='半径')
        radius_label.grid(row=0, column=0)
        self.radius_entry_cylinder = tk.Entry(self.cylinder_tab)
        self.radius_entry_cylinder.grid(row=0, column=1)
        height_label = tk.Label(self.cylinder_tab, text='高')
        height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(self.cylinder_tab)
        self.height_entry.grid(row=1, column=1)
        precision_label = tk.Label(self.cylinder_tab, text='保留小数点后几位')
        precision_label.grid(row=2, column=0)
        self.precision_entry_cylinder = tk.Entry(self.cylinder_tab, validate='key', validatecommand=(self.precision_validate, '%P'))
        self.precision_entry_cylinder.grid(row=2, column=1)
        unit_label = tk.Label(self.cylinder_tab, text='单位')
        unit_label.grid(row=3, column=0)
        self.unit_entry_cylinder = tk.Entry(self.cylinder_tab)
        self.unit_entry_cylinder.grid(row=3, column=1)
        calculate_button = tk.Button(self.cylinder_tab, text='计算', command=self.calculate_cylinder)
        calculate_button.grid(row=4, columnspan=2)

        # 创建海龟绘图页面的控件
        length_label = tk.Label(self.turtle_tab, text='长度')
        length_label.grid(row=0, column=0)
        width_label = tk.Label(self.turtle_tab, text='宽度')
        width_label.grid(row=1, column=0)
        height_label = tk.Label(self.turtle_tab, text='高度')
        height_label.grid(row=2, column=0)
        self.length_entry = tk.Entry(self.turtle_tab)
        self.length_entry.grid(row=0, column=1)
        self.width_entry = tk.Entry(self.turtle_tab)
        self.width_entry.grid(row=1, column=1)
        self.height_entry_turtle = tk.Entry(self.turtle_tab)
        self.height_entry_turtle.grid(row=2, column=1)
        draw_button = tk.Button(self.turtle_tab, text='绘图', command=self.draw_turtle_figure)
        draw_button.grid(row=3, columnspan=2)

    def calculate_circle(self):
        # 获取输入值
        radius = self.get_positive_number(self.radius_entry, '半径')
        precision = self.get_precision(self.precision_entry, '保留小数点后几位')
        unit = self.unit_entry.get()

        # 计算圆的周长和面积
        area = round(math.pi * radius ** 2, precision)

