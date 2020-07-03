# def print_grade(report):
#     for i in range(len(report)):
#         print(report[i])

# 读取 report.txt 文件中的成绩
report = []
with open('report.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.split()
        report.append(line)
report[0].insert(0, '名次')
report[0].append('总分')
report[0].append('平均分')
# print(report)

# 统计每名学生总成绩、计算平均并从高到低重新排名；
for student in report[1:]:      # the first row is header
    total = 0
    course = 0
    for grade in student[1:]:
        total += int(grade)
        course += 1
    student.append(str(total))                           # total grade: int
    student.append('%.2f' % (total/course))         # mean  grade: str
# print_grade(report)

# 汇总每一科目的平均分和总平均分（见下表第一行）；
result = sorted(report[1:], key=lambda x: x[-2], reverse=True)
# print_grade(result)

average = []    # 科目平均分
for j in range(1, len(result[1])):
    total, people = 0, 0
    for i in range(len(result)):
        total += float(result[i][j])
        people += 1
        if float(result[i][j]) < 60:
            result[i][j] = '不及格'
    average.append('%.2f' % (total/people))

average.insert(0, '平均')
result.insert(0, average)
result.insert(0, report[0])
# print(len(result[0]), len(result[1]))

# 添加名次，替换60分以下的成绩为“不及格”；
for i in range(1, len(result)):
    result[i].insert(0, str(i-1))
# print_grade(result)

# 将处理后的成绩另存为一个新文件（result.txt）
with open('result.txt', 'w', encoding='utf-8') as f:
    for res in result:
        r = ' '.join(res)
        f.writelines(r + '\n')