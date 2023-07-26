import asyncio
import time

# สร้างฟังชันด์ factorital
# แสดงค่า factorial n ในตำแหน่งที่ i ทุกครั้งที่มีการ fac
# await ทุกครั้ง sleep(1) หลังจาก fac เสร็จ
async def factorial(n):
    f = 1
    for i in range(2, n+1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= 1
    return f

# กำหนดค่า factorial เป็น 2 , 3 , 4 โดยการสร้าง list ด้วย gather
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) #[2, 6, 24]

# กำหนดเวลาเริ่มต้น สิ้นสุด ให้โปรแกรมทำงาน แล้วแสดงผลเวลาทั้งหมดที่ใช้ดำเนินงาน
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')


## Result

# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [1, 1, 1]
# Time: 3.04 sec