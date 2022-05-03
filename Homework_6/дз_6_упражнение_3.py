import pickle
USERS = "users.csv"
HOBBY = "hobby.csv"
def processing(users, hobby):
    with open(users, 'r', encoding="utf-8") as users:
        with open(hobby, 'r', encoding="utf-8") as hobby:
            user_name = users.readline().replace("\n", "")
            user_hobby = hobby.readline().replace("\n", "")
            res = {}
            while user_name or user_hobby:
                if user_name == '':
                    return 1
                res[user_name.replace(",", " ")] = user_hobby.replace(",", ", ")
                user_name = users.readline().replace("\n", "")
                user_hobby = hobby.readline().replace("\n", "")
            for key in res:
                if res[key] == '':
                    res[key] = None
            return res
result = processing(USERS, HOBBY)
with open('result.txt', 'wb') as f:
    pickle.dump(result, f)
with open('result.txt', 'rb') as f:
    result_file = pickle.load(f, encoding="UTF-8")
print(result_file)