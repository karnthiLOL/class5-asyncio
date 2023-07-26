import time

my_compute_time = 0.08333333333 # 5 sec / 1 min = 0.08333333333 min
opponent_compute_time = 0.91666666666 # 55 sec / 1 min = 0.91666666666 min
opponents = 1 # from 24
move_pairs = 30


def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")


## คำนวณเวลาทำงาน 
# คิด my_compute_time กับ opponent_compute_time = move_pairs 1 รอบ
# เพราะ จำนวนครั้งที่สามารถเดินได้ทั้งหมด = move_pairs และใช้เวลารวม = my_compute_time + opponent_compute_time 
# แปลว่ากระดานนี้จะใช้เวลาต่อ 1 กระดาน = (5 + 55) x 30 = 1800 วินาที
# ซึ่งมีทั้งหมด 24 กระดาน จึงใช้เวลาทั้งหมด 1800 x 24 = 43200 วินาที ซึ่งเท่ากับ 12 ชั่วโมง
# ดังนั้นใช้เวลาทั้งหมดในแบบ sync = 12 Hr
