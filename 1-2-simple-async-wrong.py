#import asyncio และ time
import asyncio
import time

# ทำฟังชันด์ sleep แบบ asycn 
# แต่ดันใส่ time.sleep(1) ของ sync เข้าไป 
# เป็นการเขียนที่ผิด
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# ฟังชันด์ sum
async def sum(name, numbers):
    total = 0
    #วนลูปในตัวเลขใน task
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        #sleep แล้วจึง sum และแสดงผลอีกครั้ง
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

# สร้าง loop โดยใช้ asyncio คำนวณฟังชันด์ sum
# ใน task A และ B
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1,2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
#แสดงเวลาทั้งหมดที่ดำเนินการ
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
# Time: 3.04
# Task B: Computing 3+3
# Time: 4.05
# Task B: Sum = 6

# Time: 5.06 sec