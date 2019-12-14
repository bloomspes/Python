# 파이썬 파일 입출력 구문
# 현업에서도 자주 등장하는 try-except을 활용한 코드
# 아직 익숙하지 않지만 try-except 구문을 효과적으로 쓰기위한 지침을 좀더 고민해보자s.

import sys

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename):
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return lines

def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w")
        for line in lines:
            fh.write(line)
    except (EnvironmentError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

def remove_blank_lines():
    if len(sys.argv) < 2:
        print("Usage: python {0} [ ]".format(sys.argv[0]))

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == "__main__":
    remove_blank_lines()