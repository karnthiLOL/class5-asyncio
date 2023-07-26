import asyncio
import time

#สร้างฟังชันด์ hello 
# ส่งoutput เป้น วันเวลา hello start/stop 
# sleep = 4
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

#สร้าง main สร้าง task 2 task
async def main():
    task1 = asyncio.create_task(hello(1)) #return immediately,
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

# กำหนดเวลา เริ่มต้น สิ้นสุด 
# สั่งรันฟังชันด์ main
# แสดงเวลาที่ทำงานทั้งหมด
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')


## Result

# Wed Jul 26 14:44:41 2023 hello 1 started
# Wed Jul 26 14:44:41 2023 hello 2 started
# Wed Jul 26 14:44:45 2023 hello 1 done
# Wed Jul 26 14:44:45 2023 hello 2 done
# Time: 4.01 sec