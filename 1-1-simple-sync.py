# 1-1-simple-sync.py
import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# ฟังชันด์บวกเลขไปเรื่อยๆโดย n = n+1
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    # แสดงผล ชื่อ Task : ผลบวก
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# กำหนด task A และ B แล้วใส่ฟังชันด์ sum 
# ซึ่งฟังชันด์ sum จะแสดง ชื่อ Task และ ผลของการบวก
# และแสดงเวลาที่ใช้ในแต่ละ task
# หลังจากดำเนินการทั้งหมดแล้ว จะแสดงเวลาทั้งหมดที่ใช้ดำเนินการ
tasks = [
    sum("A", [1,2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')


## Result

# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.02
# Task B: Computing 3+3
# Time: 4.04
# Task B: Sum = 6

# Time: 5.04 sec