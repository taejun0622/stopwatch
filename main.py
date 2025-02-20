import time
import os
import pyfiglet
import sys
import select
from colorama import init, Cursor, Style, Back, Fore
import tty
import termios

init()  # colorama 초기화

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
        self.laps = []

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def pause(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.laps = []

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.laps.append(lap_time)

    def get_elapsed(self):
        return time.time() - self.start_time if self.running else self.elapsed

def clear_screen():
    os.system('clear')  # 맥 환경이므로 clear만 사용

def move_cursor_up(lines):
    print(Cursor.UP(lines), end='')

def clear_from_cursor():
    print('\033[J', end='')  # 커서 위치부터 화면 끝까지 지우기

def clear_line():
    print("\033[K", end="")

def display_time(elapsed):
    mins, secs = divmod(int(elapsed), 60)
    hours, mins = divmod(mins, 60)
    time_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
    ascii_art = pyfiglet.figlet_format(time_str)
    lines = ascii_art.split('\n')
    # 화면 중앙에 시간 표시
    for line in lines:
        if line.strip():
            print(f"{line}")

def display_laps(laps):
    if laps:
        print("Lap Times:")
        for idx, lap in enumerate(laps, 1):
            mins, secs = divmod(int(lap), 60)
            hours, mins = divmod(mins, 60)
            print(f"Lap {idx}: {hours:02d}:{mins:02d}:{secs:02d}")
        print("-" * 40)

def get_input_with_timeout():
    # 터미널 설정 저장
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # 터미널을 raw 모드로 변경
        tty.setraw(sys.stdin.fileno())
        # 입력이 있는지 확인 (0.1초 대기)
        r, _, _ = select.select([sys.stdin], [], [], 0.1)
        if r:
            return sys.stdin.read(1).lower()
    finally:
        # 터미널 설정 복구
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None

def main():
    stopwatch = Stopwatch()
    
    # 초기 화면 설정
    clear_screen()
    print("\033[?25l", end='')  # 커서 숨기기
    
    try:
        while True:
            clear_screen()
            elapsed = stopwatch.get_elapsed()
            
            # 화면 출력
            display_time(elapsed)
            display_laps(stopwatch.laps)
            print("\nControls:")
            print("[s] - Start/Pause")
            print("[l] - Lap")
            print("[r] - Reset")
            print("[q] - Quit")
            print("\nEnter command: ", end='', flush=True)

            # 키 입력 처리
            user_input = get_input_with_timeout()
            if user_input:
                if user_input in ['s', 'l', 'r', 'q']:
                    if user_input == 's':
                        if stopwatch.running:
                            stopwatch.pause()
                        else:
                            stopwatch.start()
                    elif user_input == 'l':
                        stopwatch.lap()
                    elif user_input == 'r':
                        stopwatch.reset()
                    elif user_input == 'q':
                        clear_screen()
                        print("\033[?25h", end='')  # 커서 다시 보이기
                        print("Stopwatch stopped.")
                        break

    except KeyboardInterrupt:
        clear_screen()
        print("\033[?25h", end='')  # 커서 다시 보이기
        print("\nInterrupted. Stopwatch stopped.")

if __name__ == "__main__":
    main()

