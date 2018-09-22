def print_matrix(factors):  # print current matrix
    for elements in factors:
        for element in elements:
            print('%f\t' % element, end='')
        print()


def get_factors(str):  # get the matrix from file
    factors_str = []
    fr = open(str, 'r')

    while True:  # get the elements from txt one by one
        elements = fr.readline()
        if elements:
            factors_str.append(elements)
        else:
            break

    fr.close()

    print(factors_str)

    factors_li = []
    for ele_line in factors_str:  # transfer these data from str to float
        array1 = ele_line.strip().split(',')
        temp_eles = []
        for ele in array1:
            temp_eles.append(float(ele))
        factors_li.append(temp_eles)
    print('the original equation is：')
    print_matrix(factors_li)
    return factors_li


def up_triangle(factors):
    algorithm_step = 0
    magic_factor = 0.0
    steps = len(factors)
    for j in range(steps - 1):
        for i in range(j + 1, steps):
            magic_factor = - factors[i][j] / factors[j][j]
            algorithm_step += 1
            for k in range(j, steps + 1):
                factors[i][k] = factors[j][k] * magic_factor + factors[i][k]
            print('step %d for up triangle' % algorithm_step)
            print_matrix(factors)


# def overturn_trinagle(factors):
#     length = len(factors)
#     for i in range(int(length / 2)):
#         temp = factors[length - 1 - i]
#         print(temp)
#         factors[length - 1 - i] = factors[i]
#         factors[i] = temp


def down_trinagle(factors):
    algorithm_step = 0
    magic_factor = 0.0
    steps = len(factors)
    for j in range(steps - 1, -1, -1):

        for i in range(j - 1, -1, -1):
            magic_factor = - factors[i][j] / factors[j][j]
            algorithm_step += 1
            for k in range(j, -1, -1):
                factors[i][k] = factors[j][k] * magic_factor + factors[i][k]
            factors[i][steps] = factors[j][steps] * magic_factor + factors[i][steps]
            print('step %d for down triangle' % algorithm_step)
            print_matrix(factors)


def result(factors):
    result_li = []
    steps = len(factors)
    for i in range(steps):
        result_li.append(factors[i][steps] / factors[i][i])

    return result_li


def resolve(str_path):
    factors = get_factors(str_path)  # get the data from file and transfer them to float
    up_triangle(factors)  # transfer the matrix to up striangle
    down_trinagle(factors)  # transfer the matrix to down striangle
    print(result(factors))  # get the answer for the equation


if __name__ == '__main__':
    resolve('matrix')
