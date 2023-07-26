import asyncio
import time

#ฟังชันด์ async sleep
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

# ฟังชันด์ sum ตัวเลขใน task
# แสดง output เป็น ชื่อTask และ เลขที่บวกกัน
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

# เขียนฟังชันด์ main ให้ sum task
async def main():
    await asyncio.gather(sum("A", [1,2]),
                         sum("B", [1, 2, 3])) 

#เขียนรูปแบบให้ คำนวณเวลาที่ใช้ทำ main()
# แล้วแสดงผลเวลาออกมา
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')


## Result

# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec