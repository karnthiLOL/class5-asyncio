import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

#ฟังชันด์ sleep แบบ synci
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# สร้างฟังชันด์ sum ที่แสดง ชื่อ task และ เลขที่บวกกัน
# โดยการใช้ _executor ซึ่งจะแปลงจาก async เป้น sync
async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}: Sum = {total}\n')

# กำหนดเวลาเริ่มต้น
start = time.time()

# สร้างลูปเพื่อทำการ sum task
loop = asyncio.get_event_loop()
task = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3]))
]
# วนลูปจนกว่าจะหมด task
loop.run_until_complete(asyncio.wait(task))
loop.close()

end = time.time()

#แสดงเวลาดำเนินการ
print(f'Time: {end-start:.2f} sec')

## Result

# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task B: Computing 1+2
# Task A: Computing 1+2
# Time: 1.01
# Time: 1.02
# Task B: Computing 3+3
# Task A: Sum = 3

# Time: 2.02     
# Task B: Sum = 6

# Time: 3.04 sec