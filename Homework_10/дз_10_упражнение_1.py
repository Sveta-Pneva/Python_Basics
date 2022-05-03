class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
    def __str__(self):
        result = ""
        for i in self.list_of_lists:
            i = [str(j) for j in i]
            result += " ".join(i) + "\n"
        result = result[:len(result) - 1]
        return result
    def __add__(self, other):
        self.other = other
        result = ""
        for i in range(len(self.list_of_lists)):
            first_list = self.list_of_lists[i]
            other_list = other[i]
            result += " ".join([str(other_list[j] + first_list[j]) for j in range(len(other_list))]) + "\n"
        result = result[:len(result) - 1]
        return result


matr = Matrix([[1, 2, 34], [4, 59, 6], [23, 67, 98]])
print(matr.__str__())
print("   ")
print(matr.__add__([[1, 2, 34], [4, 59, 6], [23, 67, 98]]))