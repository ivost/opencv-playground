import sys
import time
import logging as log
from dataclasses import dataclass

# _pv = sys.version_info
# if _pv[0] == 3 and _pv[1] == 6:
#     # if using py 3.6 - backport of 3.7 dataclasses
#     from dataclasses import dataclass

MS = 1000
USEC = MS * MS

@dataclass
class Stats:
    begin_time: float
    end_time: float
    process_duration: float
    mark_time: float
    total_count: int
    failed: int

    def __init__(self):
        self.process_duration = 0
        self.total_count = 0
        self.failed_count = 0
        self.begin()
        self.end()

    def begin(self):
        self.begin_time = time.perf_counter()

    def end(self):
        self.end_time = time.perf_counter()

    def mark(self):
        self.mark_time = time.perf_counter()

    def bump(self, is_error=False):
        delta = time.perf_counter() - self.mark_time
        if delta > 0:
            self.process_duration += delta
        self.total_count += 1
        if is_error:
            self.failed_count += 1

    def inference_summary(self):
        if self.begin_time > self.end_time:
            self.end_time = time.perf_counter()
        dur = self.end_time - self.begin_time
        str = f"\n  Elapsed time: {dur:.2f} sec\n"
        if dur > 0 and self.total_count > 0:
            avg = self.process_duration / self.total_count
            ips = 1/avg
            str += f"  Total images: {self.total_count}, failed: {self.failed_count}\n"
            str += f"Inference time: {self.process_duration:.2f} sec\n"
            str += f"       Average: {avg:.2f} ms, {ips:.2f} inf/sec\n"
        return str

    def fps_summary(self):
        if self.begin_time > self.end_time:
            self.end_time = time.perf_counter()
        dur = self.end_time - self.begin_time
        str = f"\n  Elapsed time: {dur:.2f} sec\n"
        str += f"  Capture time: {self.process_duration:.2f} sec\n"
        if dur > 0 and self.total_count > 0:
            fps = self.total_count / self.process_duration
            str += f"  Total frames: {self.total_count}\n"
            str += f"    frames/sec: {fps:.2f}\n"
        return str

    def __str__(self):
        # return self.inference_summary()
        return self.fps_summary()


if __name__ == '__main__':
    s = Stats()
    s.begin()
    time.sleep(0.3)
    # 1
    s.mark()
    time.sleep(0.3)
    s.bump()
    time.sleep(0.1)
    # 2
    s.mark()
    time.sleep(0.4)
    # s.bump(is_error=True)
    s.bump()
    time.sleep(0.1)
    s.end()
    print(s.inference_summary())
    print(s.fps_summary())
    exit(0)

