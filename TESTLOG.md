# Test log — news-image-20261125-recorded

Built 2026-11-25 in a fresh recorded Muse session (agent
b5a8818a-17e7-481e-b60d-b81dae2a3cf5, started 13:08 UTC, after the
competition opened 2026-11-25 00:00 UTC).

## News verification

All six stories re-verified by web search against Reuters on
25 Nov 2026 (plus Xinhua for Shenzhou-24):

- Houthis / Ras Tanura / Riyadh financial district — Reuters 25 Nov:
  Houthis said they attacked the refinery and the district; coalition
  intercepted 4 drones; 11 wounded on Tuesday.
- Shenzhou-24 — Reuters / Xinhua 25 Nov: launched 08:18 Beijing;
  Pakistani astronaut Muhammad Zeeshan Ali, first foreigner aboard
  Tiangong; crew docked the same day.
- Samara refineries — Reuters 25 Nov: Syzran / Kuibyshev refineries
  hit overnight; one person killed; 145 drones downed in the region.
  (An earlier draft said 305 — corrected to the Reuters figure.)
- Markets — Reuters 25 Nov: Asian stocks tumbled on tariff fears;
  Nvidia -5.9%, Anthropic -6.5% to below its $83 IPO price.
- Puigdemont — Reuters 25 Nov: return to Spain on Dec 12, ending
  nearly a decade of self-imposed exile.
- Huawei / Microsoft / consumer confidence — Reuters 24–25 Nov:
  Huawei guilty on 10 of 12 counts; Microsoft Code Red after the
  Nov 12–13 24-hour outage; confidence index 103.3, highest since
  Jan 2025.

## Image

- `python3 generate_entry.py entry.png` → 1024x1024 PNG, 146,951 bytes
  (≤ 1 MiB), sha256
  `8ea86561063440a27995ab0dbf01daf0ecbfba8824eb3cbc9e5810c47d653c80`.
- Visual inspection (two renders): all text inside its boxes, no
  clipping, no overflow. One revision after the first render: added
  "The crew docked the same day." to story 2; re-rendered and
  re-verified.

## Determinism

- `python3 main.py /tmp/run1/entry.png` and
  `python3 main.py /tmp/run2/entry.png` both wrote sha256
  `8ea86561063440a27995ab0dbf01daf0ecbfba8824eb3cbc9e5810c47d653c80`,
  identical to `entry.png`.
- `main.py` uses only the Python standard library, no network.
