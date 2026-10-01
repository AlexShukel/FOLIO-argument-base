"""Tests for the prover runner's resource guards.

Nine unbounded swipl workers took a 16 GB Mac down four times (kernel
watchdog panics while thrashing swap), so every worker now has a hard
memory cap and the runner refuses a jobs x memory budget the machine
cannot hold.
"""
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

import run_seqprover as rs

ROOT = Path(__file__).resolve().parents[1]

# A stand-in prover that grabs ~50 MB every 50 ms and never finishes.
HOG = [sys.executable, "-c",
       "import time\nb=[]\nwhile True:\n b.append(bytearray(50*1024*1024))\n time.sleep(0.05)"]


def test_worker_over_memory_cap_is_killed_and_reported(tmp_path):
    seq = tmp_path / "x.pl"
    seq.write_text("", "utf-8")
    t0 = time.time()
    r = rs.run_one(seq, threshold=5, timeout=60, max_mem_mb=200, cmd=HOG)
    assert r["status"] == "memout"
    assert "# MEMOUT" in r["output"]
    assert time.time() - t0 < 20, "hog should be killed well before the 60 s timeout"


def test_timeout_still_reported_as_timeout(tmp_path):
    seq = tmp_path / "x.pl"
    seq.write_text("", "utf-8")
    sleeper = [sys.executable, "-c", "import time; time.sleep(30)"]
    r = rs.run_one(seq, threshold=5, timeout=1, max_mem_mb=1024, cmd=sleeper)
    assert r["status"] == "timeout"
    assert "# TIMEOUT" in r["output"]


@pytest.mark.skipif(not shutil.which("swipl"), reason="swipl not installed")
def test_real_prover_hits_memory_cap_fast():
    # ARG-05.neg grows ~180 MB/s with threshold 5; cap it well under that.
    r = rs.run_one(ROOT / "sequents" / "ARG-05.neg.pl", threshold=5, timeout=60, max_mem_mb=512)
    assert r["status"] == "memout"
    assert r["seconds"] < 30


def test_budget_refuses_jobs_that_exceed_half_of_ram():
    with pytest.raises(SystemExit):
        rs.check_memory_budget(jobs=9, max_mem_mb=1024, total_mb=16 * 1024)


def test_budget_accepts_jobs_within_half_of_ram():
    rs.check_memory_budget(jobs=2, max_mem_mb=1024, total_mb=16 * 1024)


def test_default_jobs_fit_a_quarter_of_ram():
    # 16 GB machine, 1 GB per worker, 10 cpus -> 4 workers, not 9.
    assert rs.default_jobs(max_mem_mb=1024, total_mb=16 * 1024, cpus=10) == 4
    # Never below 1, never above cpus - 1.
    assert rs.default_jobs(max_mem_mb=8192, total_mb=16 * 1024, cpus=10) == 1
    assert rs.default_jobs(max_mem_mb=64, total_mb=16 * 1024, cpus=4) == 3


def test_memout_counts_as_disagreement():
    assert rs.agrees({"goal": "memout", "negated_goal": "not_proved"},
                     {"goal": False, "negated_goal": False}) is False
    assert rs.agrees({"goal": "proved", "negated_goal": "not_proved"},
                     {"goal": True, "negated_goal": False}) is True
