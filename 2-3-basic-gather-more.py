import asyncio
import time

#สร้างฟังชันด์ hello 
# ส่งoutput เป้น วันเวลา hello start/stop 
# sleep = 4
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้าง main สร้าง coros ให้วนใน tange = 10
# ใช้ await ในเป้นเวลา = *coros
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

# กำหนดเวลา เริ่มต้น สิ้นสุด 
# สั่งรันฟังชันด์ main
# แสดงเวลาที่ทำงานทั้งหมด
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

## Result

# Wed Jul 26 14:54:49 2023 hello 0 started
# Wed Jul 26 14:54:49 2023 hello 1 started
# Wed Jul 26 14:54:49 2023 hello 2 started
# Wed Jul 26 14:54:49 2023 hello 3 started
# Wed Jul 26 14:54:49 2023 hello 4 started
# Wed Jul 26 14:54:49 2023 hello 5 started
# Wed Jul 26 14:54:49 2023 hello 6 started
# Wed Jul 26 14:54:49 2023 hello 7 started
# Wed Jul 26 14:54:49 2023 hello 8 started
# Wed Jul 26 14:54:49 2023 hello 9 started
# Wed Jul 26 14:54:53 2023 hello 0 done
# Wed Jul 26 14:54:53 2023 hello 2 done
# Wed Jul 26 14:54:53 2023 hello 6 done
# Wed Jul 26 14:54:53 2023 hello 9 done
# Wed Jul 26 14:54:53 2023 hello 8 done
# Wed Jul 26 14:54:53 2023 hello 5 done
# Wed Jul 26 14:54:53 2023 hello 7 done
# Wed Jul 26 14:54:53 2023 hello 4 done
# Wed Jul 26 14:54:53 2023 hello 1 done
# Wed Jul 26 14:54:53 2023 hello 3 done
# Time: 4.01 sec