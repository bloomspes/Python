# threading 모듈 학습
# 스레드가 여러 대로 분리되면, 락과 데드락을 회피하는데 신경을 써야 한다.
# 내부에서 lock 관리 ==> queue 모듈 사용

# 프로그램이 종료되지 않는 문제는 스레드를 daemon으로 변환 시키면
# 데몬이 실행되지 않는 즉시 프로그램이 종료된다.

import queue
import threading

q = queue.Queue()

def worker(num):
    while True:
        item = q.get()
        if item is None:
            break
        print("스레드 {0} : 처리 완료 {1}".format(num+1, item))
        q.task_done()

if __name__ == "__main__":
    num_worker_threads = 5
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(20):
        q.put(item)

    # 모든 작업이 끝날 때까지 대기한다(block).
    q.join()

    # 워커 스레드 종료
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()